# Online Admission Registration & Payment System

## 📝 Description

A modern web-based admission management system designed to streamline the admission process for educational institutions. The system features a user-friendly interface for student registration, secure payment processing via Razorpay, and instant admin notifications through Telegram.

![Admission System](https://img.shields.io/badge/Admission-System-green)
![Python](https://img.shields.io/badge/Python-Flask-blue)
![Razorpay](https://img.shields.io/badge/Payment-Razorpay-blue)
![Telegram](https://img.shields.io/badge/Notification-Telegram-blue)

## ✨ Features

- 📋 Intuitive admission form with real-time validation
- 💳 Secure payment integration with Razorpay
- 📱 Mobile-responsive design
- 🔔 Instant Telegram notifications for administrators
- 🔒 Secure payment verification system
- 📊 Age verification system
- 🎨 Modern UI with smooth animations

## 🛠️ Technology Stack

- **Frontend:**

  - HTML5, CSS3
  - JavaScript (Vanilla)
  - Razorpay Checkout

- **Backend:**

  - Python 3.x
  - Flask Framework
  - Razorpay Python SDK

- **Notifications:**
  - Telegram Bot API

## 🚀 Setup Instructions

1. **Clone the repository:**

   ```powershell
   git clone <repository-url>
   cd admission-system
   ```

2. **Install dependencies:**

   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure the application:**
   Create `config.py` with the following settings:

   ```python
   # Razorpay Configuration
   RAZORPAY_KEY = "your_razorpay_key"
   RAZORPAY_SECRET = "your_razorpay_secret"

   # Telegram Configuration
   TELEGRAM_TOKEN = "your_bot_token"
   TELEGRAM_CHAT_ID = "your_group_id"

   # Application Configuration
   REGISTRATION_FEE = 500  # Fee in INR
   ```

4. **Run the application:**
   ```powershell
   python app.py
   ```

## 💡 Usage

1. **Student Registration:**

   - Fill out the admission form with required details
   - System validates age requirement (minimum 15 years)
   - Real-time form validation with instant feedback

2. **Payment Process:**

   - Secure payment through Razorpay gateway
   - Amount: ₹500 (configurable in config.py)
   - Payment status updates in real-time

3. **Admin Notifications:**
   - Instant Telegram notifications for new registrations
   - Detailed student information in formatted messages
   - Payment confirmation status

## 🔒 Security Features

- Razorpay payment signature verification
- Secure form validation
- Protected API endpoints
- Error handling and logging
- Data validation and sanitization

## 📁 Project Structure

```
admission-system/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── static/
│   └── style.css      # CSS styles
└── templates/
    └── index.html     # Main admission form
```

## ⚙️ Configuration

### Required Environment Variables:

- `RAZORPAY_KEY`: Your Razorpay API key
- `RAZORPAY_SECRET`: Your Razorpay API secret
- `TELEGRAM_TOKEN`: Your Telegram bot token
- `TELEGRAM_CHAT_ID`: Your Telegram group/channel ID

## 📱 Mobile Responsiveness

The system is fully responsive and works seamlessly on:

- Desktop browsers
- Tablets
- Mobile devices

## 🛡️ Error Handling

- Comprehensive error handling for payments
- Form validation errors with user feedback
- Payment processing error handling
- Network error handling
- Telegram notification failure handling

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Authors

- Your Name
- Email: your.email@example.com

## 🙏 Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [Razorpay](https://razorpay.com/)
- [Telegram Bot API](https://core.telegram.org/bots/api)

## 📞 Support

For support, email your.email@example.com or create an issue in the repository.
