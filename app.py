from flask import Flask, render_template, request, jsonify, redirect
import requests
import hmac
import hashlib
from config import REGISTRATION_FEE, TELEGRAM_TOKEN, TELEGRAM_CHAT_ID
from urllib.parse import quote

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a12@4rr&$%gxd57dd'  # Important for session security

# No need for Razorpay client initialization since we're using Razorpay.me links

def generate_razorpayme_link(amount, purpose, customer_name, email, contact):
    """
    Generate a Razorpay.me payment link
    """
    base_url = "https://razorpay.me/@pycraftr"
    params = {
        'amount': amount * 100,  # Convert to paise
        'purpose': purpose,
        'name': customer_name,
        'email': email,
        'contact': contact
    }
    # query_string = '&'.join([f"{k}={quote(str(v))}" for k, v in params.items()])
    return f"{base_url}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_payment', methods=['POST'])
def create_payment():
    """
    Create a Razorpay.me payment link and redirect user
    """
    if request.method != 'POST':
        return jsonify({"error": "Method not allowed"}), 405

    try:
        data = request.form
        
        # Validate required fields
        required_fields = ['name', 'phone', 'course']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({"error": f"Missing required field: {field}"}), 400

        # Generate payment link
        payment_link = generate_razorpayme_link(
            amount=float(REGISTRATION_FEE),
            purpose=f"{data['course']} Course Registration",
            customer_name=data['name'],
            email=data.get('email', ''),
            contact=data['phone']
        )

        # Store the form data in session for verification later
        # You might want to use a database in production
        app.logger.info(f"Payment initiated for {data['name']} - {data['phone']}")

        return jsonify({
            "status": "success",
            "payment_link": payment_link,
            "redirect": True
        })

    except Exception as e:
        app.logger.error(f"Error creating payment: {str(e)}")
        return jsonify({"error": "Failed to create payment link"}), 500

@app.route('/payment_webhook', methods=['POST'])
def payment_webhook():
    """
    Handle Razorpay.me payment webhook
    """
    try:
        # In production, you should verify the webhook signature
        # This is a simplified version - implement proper verification
        data = request.json

        # Check if payment was successful
        if data.get('event') == 'payment.captured':
            payment_id = data['payload']['payment']['entity']['id']
            amount = data['payload']['payment']['entity']['amount'] / 100  # Convert to rupees
            customer = data['payload']['payment']['entity'].get('notes', {})

            # Send Telegram message
            message = f"""🧾 *New Registration Payment Received*
👤 Name: {customer.get('name', 'Not Provided')}
📞 Phone: {customer.get('contact', 'Not Provided')}
📧 Email: {customer.get('email', 'Not Provided')}
💰 Amount: ₹{amount}
🆔 Payment ID: {payment_id}"""

            telegram_url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
            payload = {
                "chat_id": TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "Markdown"
            }
            
            response = requests.post(telegram_url, json=payload, timeout=10)
            response.raise_for_status()

        return jsonify({"status": "success"}), 200

    except Exception as e:
        app.logger.error(f"Webhook processing error: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)