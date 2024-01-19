import sender_stand_request
import data

def positive_assert(body):
    track = sender_stand_request.post_new_orders(body)
    response_positive = sender_stand_request.get_orders(track)

    assert response_positive.status_code == 200

def test_API():
    positive_assert(data.orders_body)