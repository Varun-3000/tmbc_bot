import os
import requests
from dotenv import load_dotenv
import re
load_dotenv()

ACCESS_TOKEN = os.getenv("WHATSAPP_TOKEN")
PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID")


def validate_phone_number(phone_number: str) -> bool:
    """
    Validate phone number format (E.164 format).
    """
    # Check if the phone number matches the E.164 format (i.e., starts with + followed by digits)
    # The number can be between 4 to 15 digits long
    return bool(re.match(r"^\+[1-9]\d{1,14}$", phone_number))
    

def send_whatsapp_message(to_number: str, message: str = "Hello, this is a test message from our TMBC bot!"):
    """
    Send a WhatsApp message using Meta's API.
    """
    url = f"https://graph.facebook.com/v22.0/{PHONE_NUMBER_ID}/messages"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to_number,
        "type": "text",
        "text": {"body": message}
    }

    response = requests.post(url, headers=headers, json=payload)

    # Debug logging
    print("Request Payload:", payload)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
    return response
