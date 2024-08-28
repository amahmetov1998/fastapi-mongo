from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    email: EmailStr
    telegram: str
    phone: str
    code: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "foo@bar.com",
                "telegram": "@foobar",
                "phone": "123456789",
                "code": "ABCD"
            }
        }


class EmailResponse(BaseModel):
    code: str
    email: EmailStr


class TelegramResponse(BaseModel):
    code: str
    telegram: str


class PhoneResponse(BaseModel):
    code: str
    phone: str
