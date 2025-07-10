def apply_coupon(price, coupon):
    discount = {
        "OFERTA10": 0.10,
        "SUPER20": 0.20,
        "NUEVO": 0.15
    }
    
    if coupon in discount:
        return round(price * (1 - discount[coupon]), 2)
    return price

def get_final_price(base_price, coupon, tax_rate=0.19):
    discount_price = apply_coupon(base_price, coupon)
    return round(discount_price * (1 + tax_rate), 2)