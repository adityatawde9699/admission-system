from flask import Flask, render_template, request, jsonify
import razorpay, requests, hmac, hashlib
from config import *

app = Flask(__name__)

razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY, RAZORPAY_SECRET))

def verify_razorpay_signature(payment_id, order_id, signature):
    msg = f'{order_id}|{payment_id}'
    generated_signature = hmac.new(
        RAZORPAY_SECRET.encode(),
        msg.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(generated_signature, signature)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create_order', methods=['POST'])
def create_order():
    try:
        data = request.form
        amount = REGISTRATION_FEE * 100  # Convert to paise
        order = razorpay_client.order.create({
            "amount": amount,
            "currency": "INR",
            "payment_capture": 1
        })
        return jsonify({
            "key": RAZORPAY_KEY,
            "order_id": order["id"],
            "amount": amount
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/verify_payment', methods=['POST'])
def verify_payment():
    try:
        data = request.json
        # Verify the payment signature
        if not verify_razorpay_signature(
            data['razorpay_payment_id'],
            data['razorpay_order_id'],
            data['razorpay_signature']
        ):
            return jsonify({"error": "Invalid payment signature"}), 400

        # Send Telegram message
        message = f"""🧾 *New Registration Request*
👤 Name: {data['name']}
📞 Phone: {data['phone']}
📧 Email: {data.get('email', 'Not Provided')}
📚 Course: {data['course']}
🎂 DOB: {data.get('dob', 'Not Provided')}
💲 Fees Paid: ✅ Yes
🆔 Request ID: {data['razorpay_payment_id']}"""
        
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an exception for bad responses

        return jsonify({"status": "success"})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to send notification", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
