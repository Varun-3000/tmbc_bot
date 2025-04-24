# FastAPI WhatsApp Messaging Application

This FastAPI application integrates with Meta's WhatsApp Business Manager API to send a test message to a specified WhatsApp number.

## Requirements

- Python 3.8 or later
- FastAPI
- Uvicorn
- Requests
- python-dotenv

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/<yourusername>/tmbc_bot.git
    cd tmbc_bot
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root of the project with the following content:
    ```
    WHATSAPP_TOKEN=<your_whatsapp_access_token>
    WHATSAPP_PHONE_NUMBER_ID=<your_whatsapp_phone_number_id>
    ```

4. Run the FastAPI application:
    ```bash
    uvicorn main:app --reload
    ```

5. Visit the endpoint in your browser or via cURL:
    ```
    http://127.0.0.1:8000/send_message?phone_number=%2B<phone_number>
    ```
    Note: %2B is the URL-encoded form for '+'

## Endpoint

- `GET /send_message?phone_number=<E.164_format_number>`
    - Sends a test message to the provided phone number.
