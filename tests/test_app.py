# tests/test_app.py
from unittest.mock import patch
from src.ticket_classifier import classify_ticket, TicketClassification


# Mock the OpenAI API response
@patch("src.ticket_classifier.openai.ChatCompletion.create")
def test_ticket_classification_workflow(mock_openai):
    # Simulate a mocked response from OpenAI API
    mock_openai.return_value = {"choices": [{"message": {"content": "order_issue"}}]}

    # Input ticket text for the test
    ticket_text = "I ordered a laptop with order #12345 but received a tablet instead."

    # Call the classify_ticket function, which should now use the mocked OpenAI response
    result = classify_ticket(ticket_text)

    # Assertions to check if the app returns the expected outputs
    assert result.category == "order_issue"
    assert result.urgency == "high"  # Assuming this is the expected output
    assert result.sentiment == "frustrated"  # Assuming this is the expected output
    assert "order #12345" in result.key_information
    assert (
        result.suggested_action
        == "Initiate a return for the tablet and expedite the delivery of the correct laptop."
    )
