from flask import Flask, render_template, request, jsonify
import razorpay

app = Flask(__name__)

# Replace with your Razorpay API key and secret
RAZORPAY_API_KEY = "rzp_live_X0kPZAwgC5N2p4"
RAZORPAY_API_SECRET = "moLAbB1Jd5ghgufOp4S2jVbk"

razorpay_client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET))

@app.route('/')
def home():
    return render_template('index.html', razorpay_key=RAZORPAY_API_KEY)

@app.route('/create_order', methods=['POST'])
def create_order():
    data = request.json
    amount = data.get('amount',0)
    print(amount[1])
    # cart = request.json
    # cart1= cart.get('cart')
    
    try:
        amount_in_paise = int(float(amount[1]) * 100)  # Convert amount to paise
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400
    
    # print(cart1)
    # for item in cart:
    #     print(f"Product ID: {item['productId']}, Product Name: {item['productName']}, Quantity: {item['quantity']}")

    payment_order = razorpay_client.order.create(dict(amount=amount_in_paise, currency='INR'))
    return jsonify(payment_order)
if __name__ == '__main__':
    app.run(debug=True)
