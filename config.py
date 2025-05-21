# Configuration settings for the application
from dotenv import load_dotenv
load_dotenv()
import os

# Razorpay Configuration
RAZORPAY_KEY = os.getenv("RAZORPAY_KEY_ID")  # Replace with your actual Razorpay key
RAZORPAY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")  # Replace with your actual Razorpay secret

# Telegram Configuration
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")  # Replace with your actual Telegram bot token
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Replace with your actual Telegram chat ID

# Application Configuration
DEBUG = os.getenv('DEBUG')  # Set to False in production
REGISTRATION_FEE = 1