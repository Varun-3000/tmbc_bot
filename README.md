# TMBC WhatsApp Messaging Bot 🚀

A FastAPI-based service that sends WhatsApp messages using Meta's WhatsApp Business Cloud API.

---

## ✅ Objective

Expose an API endpoint `/send_message` that sends a message to a specified WhatsApp number using Meta’s Cloud API.

---

## 📨 Message Format

The message sent:
> "Hello, this is a test message from our TMBC bot!"

---

## 📌 Features

- Accepts `phone_number` as a query parameter
- Validates phone number format (E.164 standard)
- Integrates with Meta’s WhatsApp Business API
- Sends either:
  - A **template message** (recommended for production)
  - A plain text message (only works within 24h session)
- Returns success/failure JSON response

---

## ⚙️ Tech Stack

- Python 3.10+
- FastAPI
- Uvicorn
- `requests` library

---

## 📂 Project Structure
tmbc_bot/

├── main.py            # 📌 This is where your FastAPI app lives — the entry point

├── utils.py           # 🔧 Contains helper functions (e.g., phone validation, sending messages)

├── requirements.txt   # 📦 Lists all dependencies you need to install

└── README.md          # 📘 Documentation file

---

## 🧪 Prerequisites

1. **Meta Developer Account**
2. **A WhatsApp Business Account (WABA)**
3. **A verified phone number (sandbox works for testing)**
4. **Your WhatsApp Access Token**
5. **Your Phone Number ID** (from Meta Dev Portal)

---

## 🔐 Add Your Credentials

In `utils.py`, update the following constants:

```python
WHATSAPP_TOKEN = "your_generated_access_token"
PHONE_NUMBER_ID = "your_whatsapp_phone_number_id"
