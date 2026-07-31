# 🌧️ Rain Alert

A Python automation that checks the weather forecast and sends an SMS notification if rain is expected.

This project uses the **OpenWeather API** to retrieve weather forecast data and the **Twilio API** to send SMS alerts. It is designed to run automatically using **GitHub Actions**, but it can also be executed locally.

---

## ✨ Features

- 🌦️ Retrieves weather forecast data from OpenWeather
- 📱 Sends SMS notifications using Twilio
- 🔐 Stores sensitive credentials securely using environment variables
- 🤖 Supports automated daily execution with GitHub Actions
- 💻 Can also be run manually on your local machine

---

## 🛠️ Technologies

- Python 3
- Requests
- Twilio
- OpenWeather API
- GitHub Actions

---

## 📂 Project Structure

```text
rain_alert/
│
├── .github/
│   └── workflows/
│       └── rain_alert.yml
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── main.py
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/rain_alert.git
cd rain_alert
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## 🔑 Required Accounts

To use this project you need:

- An **OpenWeather** account to generate an API key
- A **Twilio** account to send SMS notifications
- A Twilio phone number
- A verified recipient phone number (Twilio trial accounts)

---

## 🔒 Environment Variables

Create the following environment variables before running the application:

| Variable | Description |
|----------|-------------|
| `ACCOUNT_SID` | Twilio Account SID |
| `AUTH_TOKEN` | Twilio Authentication Token |
| `WEATHER_API_KEY` | OpenWeather API Key |
| `SENDER_PHONE` | Twilio phone number |
| `RECIPIENT_PHONE` | Recipient phone number |

Example:

```bash
export ACCOUNT_SID="your_account_sid"
export AUTH_TOKEN="your_auth_token"
export WEATHER_API_KEY="your_api_key"
export SENDER_PHONE="+1234567890"
export RECIPIENT_PHONE="+41791234567"
```

---

## ▶️ Run the Application

```bash
python main.py
```

The application checks the upcoming weather forecast.

If rain is expected, an SMS notification is sent:

> It's going to rain 🌧️ today. Remember to bring an ☔️.

---

## 🤖 GitHub Actions

This project can run automatically using GitHub Actions.

Add the following repository secrets:

- `ACCOUNT_SID`
- `AUTH_TOKEN`
- `WEATHER_API_KEY`
- `SENDER_PHONE`
- `RECIPIENT_PHONE`

These secrets are securely injected into the workflow during execution.

---

## 📍 Weather Configuration

The location is configured inside `main.py` using latitude and longitude.

Example:

```python
weather_params = {
    "lat": 43.293674,
    "lon": 13.450901,
    "appid": WEATHER_API_KEY,
    "cnt": 4,
}
```

Change the latitude and longitude to monitor a different location.

---

## 📦 Dependencies

Install all required packages:

```bash
pip install -r requirements.txt
```

Current dependencies:

```text
requests
twilio
```

---

## 🔐 Security

Sensitive information is **never stored** in the source code.

All credentials are loaded from environment variables.

Do **not** commit:

- API keys
- Authentication tokens
- Phone numbers
- `.env` files

---

## 🚀 Future Improvements

- Email notifications
- Telegram notifications
- WhatsApp notifications
- Multiple locations
- Multiple recipients
- Logging
- Error handling
- Unit tests

---

## 👨‍💻 Author

**Mick Kuyenda Misamu**

Cyber Security & Network Engineer

---

## 📄 License

This project is licensed under the MIT License.
