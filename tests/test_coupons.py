from app.coupons import apply_coupon, get_final_price

def test_discount_oferta10():
    assert apply_coupon(100, "OFERTA10") == 90.0

def test_discount_super20():
    assert apply_coupon(100, "SUPER20") == 80.0

def test_discount_new():
    assert apply_coupon(100, "NUEVO") == 85.0

def test_invalid_coupon():
    assert apply_coupon(990, "FALSO") == 990.0

def test_final_price_with_tax():
    assert get_final_price(100, "OFERTA10") == 107.1