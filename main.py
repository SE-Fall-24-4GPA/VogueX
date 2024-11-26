# main.py
import streamlit as st
from agents.fashion_agent import FashionAgent
from tools.database_tool import DatabaseManager
import uuid


def initialize_session_state():
    """Initialize session state variables."""
    if 'user_id' not in st.session_state:
        st.session_state.user_id = str(uuid.uuid4())
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []


def main():
    st.set_page_config(
        page_title="Fashion Recommender",
        page_icon="👗",
        layout="wide"
    )

    st.title("Fashion Recommender: A Style for Every Story 🌦👗")

    # Initialize session state
    initialize_session_state()

    # Sidebar for user settings
    with st.sidebar:
        st.header("Settings")
        if st.button("Clear Conversation"):
            st.session_state.chat_history = []
            st.rerun()

    try:
        # Initialize components
        db_manager = DatabaseManager()
        fashion_agent = FashionAgent()

        # Chat interface
        st.write("Chat with your personal fashion assistant!")

        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.write(message["content"])

        # Chat input
        if prompt := st.chat_input("What's your fashion question?"):
            # Display user message
            with st.chat_message("user"):
                st.write(prompt)

            # Add user message to chat history
            st.session_state.chat_history.append({"role": "user", "content": prompt})

            # Get assistant response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response = fashion_agent.get_response(prompt)
                    st.write(response)

            # Store conversation
            db_manager.store_conversation(st.session_state.user_id, prompt, response)

            # Add assistant response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": response})

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.warning("Please try refreshing the page or clearing the conversation.")


if __name__ == "__main__":
    main()