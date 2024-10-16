import pytest
from unittest.mock import patch
from src.ticket_classifier import classify_ticket


# Mock OpenAI API call
@patch("openai.ChatCompletion.create")
def test_classify_order_issue(mock_openai):
    # Mock the response from OpenAI
    mock_openai.return_value = {"choices": [{"message": {"content": "order_issue"}}]}

    ticket = "I ordered a laptop but received a tablet instead."
    result = classify_ticket(ticket)

    assert result.category == "order_issue"
