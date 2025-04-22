from pydantic import BaseModel

class VentPost(BaseModel):
    user_id: str
    content: str
