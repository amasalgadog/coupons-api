from app.api import app

def test_success_reservation():
    client = app.test_client()
    res = client.post('/price', json={"price":990, "coupon":"OFERTA10"})
    print("Response1:", res.get_json())
    assert res.status_code == 200

def test_failure():
    client = app.test_client()
    res = client.post('/price', json={"price":"990", "coupon":"OFERTA10"})
    print("Response2:", res.get_json())
    assert res.status_code == 500

