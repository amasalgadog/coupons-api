from app.api import app

def test_success_reservation():
    client = app.test_client()
    res = client.post('/price', json={"prince":990, "coupon":"OFERTA10"})
    assert res.status_code == 200

