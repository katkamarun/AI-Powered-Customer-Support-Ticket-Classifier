# tests/conftest.py
import pytest


@pytest.fixture
def mock_ticket_data():
    return {
        "text": "I ordered a laptop but received a tablet instead.",
        "category": "order_issue",
        "urgency": "high",
        "sentiment": "angry",
        "confidence": 0.95,
    }
