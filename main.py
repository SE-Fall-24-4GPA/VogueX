import streamlit as st
import asyncio
from agents.fashion_agent import FashionAgent
from tools.database_tool import DatabaseManager
import uuid
import requests
from io import BytesIO
from PIL import Image


def initialize_session_state():
    if 'user_id' not in st.session_state:
        st.session_state['user_id'] = str(uuid.uuid4())
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_preferences' not in st.session_state:
        st.session_state.user_preferences = {
            'favorite_colors': [],
            'preferred_styles': [],
            'restrictions': []
        }
    if 'db_initialized' not in st.session_state:
        st.session_state.db_initialized = False
    if 'shopping_suggestions' not in st.session_state:
        st.session_state.shopping_suggestions = []


def show_preferences_sidebar():
    with st.sidebar:
        st.title("Style Preferences")

        #Gender input
        gender = st.selectbox(
            'Select Gender',
            ('Male', 'Female', 'Unisex'),
            key='gender_selection',
            index=None,
            placeholder="Choose your gender..."
        )

        # Location input
        location = st.text_input("Location", "London")

        # Color preferences
        colors = st.multiselect(
            "Favorite Colors",
            ["Black", "White", "Blue", "Red", "Green", "Yellow", "Purple", "Pink"],
            st.session_state.user_preferences['favorite_colors']
        )

        # Style preferences
        styles = st.multiselect(
            "Preferred Styles",
            ["Casual", "Formal", "Sporty", "Bohemian", "Minimalist", "Vintage"],
            st.session_state.user_preferences['preferred_styles']
        )

        # Restrictions
        restrictions = st.multiselect(
            "Style Restrictions",
            ["No leather", "No fur", "No synthetic materials", "Modest clothing"],
            st.session_state.user_preferences['restrictions']
        )

        # Update preferences in session state
        st.session_state.user_preferences = {
            'gender': gender,
            'favorite_colors': colors,
            'preferred_styles': styles,
            'restrictions': restrictions
        }

        # Display shopping suggestions if available
        if st.session_state.shopping_suggestions:
            st.divider()
            st.subheader("Shopping Suggestions")
            for idx, suggestion in enumerate(st.session_state.shopping_suggestions):
                st.markdown(f"🛍️ [{suggestion['retailer']}]({suggestion['url']})")

        return location


def display_images(image_data: list):
    """Display images in a grid layout"""
    if not image_data:
        return

    # Images Section
    st.subheader("Outfit Suggestions")
    num_cols = min(3, len(image_data))
    cols = st.columns(num_cols)

    for idx, (col, img_info) in enumerate(zip(cols, image_data)):
        try:
            with col:
                with st.container():
                    img_url = img_info['image_url'] if isinstance(img_info, dict) else img_info
                    response = requests.get(img_url, timeout=5)
                    if response.status_code == 200:
                        try:
                            img = Image.open(BytesIO(response.content))
                            st.markdown(f"#### Look {idx + 1}")
                            st.image(
                                img,
                                use_container_width=True,
                                output_format="PNG"
                            )
                        except Exception as img_error:
                            st.error(f"Invalid image format: {str(img_error)}")
                    else:
                        st.error(f"Failed to load image (HTTP {response.status_code})")
        except requests.exceptions.Timeout:
            col.warning("Image loading timed out")
        except requests.exceptions.RequestException as e:
            col.warning(f"Network error: {str(e)}")
        except Exception as e:
            col.warning(f"Error: {str(e)}")

    # Fill remaining columns
    remaining_cols = num_cols - len(image_data)
    if remaining_cols > 0:
        for _ in range(remaining_cols):
            with cols[_].container():
                st.empty()


async def process_chat_input(
    fashion_agent: FashionAgent,
    prompt: str,
    location: str,
    chat_history: list,
    user_preferences: dict
):
    """Process chat input asynchronously"""
    response_text, images, shopping_links = await fashion_agent.get_response_with_suggestions(
        user_query=prompt,
        chat_history=chat_history[:-1],
        location=location,
        user_preferences=user_preferences
    )
    return response_text, images, shopping_links


def main():
    st.title('VogueX : A Style for Every Story')

    try:
        initialize_session_state()

        # Initialize database with reset option in sidebar
        with st.sidebar:
            if not st.session_state.db_initialized:
                reset_db = st.checkbox("Reset database on startup")
                if st.button("Initialize Database"):
                    db_manager = DatabaseManager(reset_if_exists=reset_db)
                    st.session_state.db_initialized = True
                    st.session_state.db_manager = db_manager
                    st.success("Database initialized successfully!")
                    st.rerun()

            if st.session_state.db_initialized and st.button("Reset Database"):
                st.session_state.db_manager.clear_all_data()
                st.session_state.db_initialized = False
                st.success("Database reset successfully!")
                st.rerun()

        location = show_preferences_sidebar()

        if not st.session_state.db_initialized:
            st.warning("Please initialize the database using the sidebar controls.")
            return

        fashion_agent = FashionAgent()

        # Chat interface
        st.write("Chat with your fashion assistant!")

        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])
                if "images" in message:
                    display_images(message["images"])

        # Chat input
        if prompt := st.chat_input("What's your fashion question?"):
            try:
                # Add user message to chat history
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": prompt
                })

                # Process input asynchronously
                response_text, images, shopping_links = asyncio.run(process_chat_input(
                    fashion_agent,
                    prompt,
                    location,
                    st.session_state.chat_history,
                    st.session_state.user_preferences
                ))

                # Update shopping suggestions in session state
                st.session_state.shopping_suggestions = shopping_links

                # Store conversation
                st.session_state.db_manager.store_conversation(
                    st.session_state.user_id,
                    prompt,
                    response_text,
                    st.session_state.user_preferences.get('gender')
                )

                # Add assistant response to chat history with images
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response_text,
                    "images": images
                })

                # Force refresh
                st.rerun()

            except Exception as e:
                st.error(f"Error processing your request: {str(e)}")
                import traceback
                st.error(traceback.format_exc())

    except Exception as e:
        st.error(f"Application initialization error: {str(e)}")
        import traceback
        st.error(traceback.format_exc())


if __name__ == '__main__':
    main()