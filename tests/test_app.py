# tests/test_app.py
from src.ticket_classifier import classify_ticket


def test_ticket_classification_workflow():
    ticket_text = "I ordered a laptop with order #12345 but received a tablet instead."

    result = classify_ticket(ticket_text)

    # Check if the app is returning the expected outputs
    assert result.category == "order_issue"
    assert result.urgency == "high"
    assert "order #12345" in result.key_information
