from pydantic import BaseModel

class mahasiswaGetAllResponse(BaseModel):
    nim : int
    nama : str