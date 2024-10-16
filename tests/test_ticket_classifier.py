# tests/test_ticket_classifier.py
import pytest
from src.ticket_classifier import classify_ticket, TicketClassification


# Mocking the API call or response
def mock_classify_ticket(ticket_text: str) -> TicketClassification:
    # Example mock response (simulates classification results)
    return TicketClassification(
        category="order_issue",
        urgency="high",
        sentiment="angry",
        confidence=0.95,
        key_information=["Order #12345"],
        suggested_action="Contact customer to resolve order issue",
    )


def test_classify_order_issue():
    ticket = "I ordered a laptop with order  #12345 but received a tablet instead."
    result = mock_classify_ticket(ticket)

    assert result.category == "order_issue"
    assert result.urgency == "high"
    assert result.sentiment == "angry"
    assert result.confidence >= 0.9
