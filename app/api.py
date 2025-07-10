from flask import Flask, request, jsonify
from app.coupons import get_final_price

app = Flask(__name__)

@app.route('/price', methods=['POST'])
def calculate_price():
    data = request.get_json()
    price = data.get('price')
    coupon = data.get('coupon')
    tax_rate = data.get('tax_rate', 0.19)
    
    final_price = get_final_price(price, coupon, tax_rate)
    return jsonify({"final_price": final_price})