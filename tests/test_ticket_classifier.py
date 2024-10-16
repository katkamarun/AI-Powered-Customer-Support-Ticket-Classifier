import pytest
from unittest.mock import patch
from src.ticket_classifier import classify_ticket, TicketClassification


# Mock the OpenAI API call directly
@patch("src.ticket_classifier.openai.ChatCompletion.create")
def test_classify_order_issue(mock_openai):
    # Mock the response from OpenAI
    mock_openai.return_value = {"choices": [{"message": {"content": "order_issue"}}]}

    ticket = "I ordered a laptop but received a tablet instead."

    # Call the classify_ticket function, which will use the mocked OpenAI response
    result = classify_ticket(ticket)

    # Check if the app is returning the expected outputs
    assert result.category == "order_issue"
