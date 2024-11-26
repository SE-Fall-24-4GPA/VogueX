from pydantic import BaseModel


class FashionAgent(BaseModel):
    def get_response(self, user_input : str) -> str:
        return "hi"