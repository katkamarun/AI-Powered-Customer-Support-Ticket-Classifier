import pytest
from unittest.mock import patch
from src.ticket_classifier import classify_ticket, TicketClassification


# Mock OpenAI API call
@patch("openai.ChatCompletion.create")
def test_classify_order_issue(mock_openai):
    # Mock the response from OpenAI to simulate the classification result
    mock_openai.return_value = {"choices": [{"message": {"content": "order_issue"}}]}

    ticket = "I ordered a laptop but received a tablet instead."

    # Call the classify_ticket function, which should now use the mocked OpenAI response
    result = classify_ticket(ticket)

    # Check if the app is returning the expected outputs
    assert result.category == "order_issue"
    # Add more assertions if needed
    # Example assertions for urgency, sentiment, and confidence if implemented:
    assert result.urgency == "high"  # Assuming you expect this to be high
    assert result.sentiment == "frustrated"  # Based on your logic
    # Example assertion
