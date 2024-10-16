from src.ticket_classifier import classify_ticket
from unittest.mock import patch
from src.ticket_classifier import TicketClassification


# Mock the OpenAI API response
@patch("openai.ChatCompletion.create")
def test_ticket_classification_workflow(mock_openai):
    # Simulate a mocked response from OpenAI API
    mock_openai.return_value = {"choices": [{"message": {"content": "order_issue"}}]}

    # Input ticket text for the test
    ticket_text = "I ordered a laptop with order #12345 but received a tablet instead."

    # Mock expected classification result
    mock_response = TicketClassification(
        category="order_issue",
        urgency="high",
        sentiment="frustrated",
        confidence=0.9,
        key_information=["order #12345", "received tablet instead of laptop"],
        suggested_action="Initiate a return for the tablet and expedite the delivery of the correct laptop.",
    )

    # Instead of calling the real API, we return the mocked response
    with patch("src.ticket_classifier.classify_ticket", return_value=mock_response):
        result = classify_ticket(ticket_text)

        # Assertions to check if the app returns the expected outputs
        assert result.category == "order_issue"
        assert result.urgency == "high"
        assert "order #12345" in result.key_information
