from fastapi import FastAPI, Query, HTTPException
from utils import validate_phone_number, send_whatsapp_message

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the TMBC WhatsApp bot API"}

@app.get("/send_message")
def send_message(phone_number: str = Query(..., description="Phone number in E.164 format (e.g. +1234567890)")):
    if not validate_phone_number(phone_number):
        raise HTTPException(status_code=400, detail="Invalid phone number format. Use E.164 format like +1234567890")

    response = send_whatsapp_message(phone_number)

    if response.status_code == 200:
        return {"success": True, "message": "Message sent successfully"}
    else:
        return {
            "success": False,
            "status_code": response.status_code,
            "error": response.json()
        }
