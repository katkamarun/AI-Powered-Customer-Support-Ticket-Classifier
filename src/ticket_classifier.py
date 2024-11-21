# ------------------------------------
# AI-powered Customer Support Ticket Classifiation System
# ------------------------------------
from langfuse.openai import OpenAI
import instructor
from enum import Enum
from pydantic import BaseModel, Field
from typing import List
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LANGFUSE_API_KEY = os.getenv("LANGFUSE_SECRET_KEY")
LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY")
LANGFUSE_HOST = "https://cloud.langfuse.com"





Client = instructor.patch(OpenAI())


class TicketCategory(str, Enum):
    ORDER_ISSUE = "order_issue"
    ACCOUNT_ACCESS = "account_access"
    PRODUCT_INQUIRY = "product_inquiry"
    TECHNICAL_SUPPORT = "technical_support"
    BILLING = "billing"
    OTHER = "other"


class CustomerSentiment(str, Enum):
    ANGRY = "angry"
    FRUSTRATED = "frustrated"
    NEUTRAL = "Neutral"
    SATISFIED = "satisfied"


class TicketUrgency(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class TicketClassification(BaseModel):
    category: TicketCategory
    urgency: TicketUrgency
    sentiment: CustomerSentiment
    confidence: float = Field(
        ge=0, le=1, description="confidence score for the classification"
    )
    key_information: List[str] = Field(
        description="List of key points extracted from the ticket"
    )
    suggested_action: str = Field(description="Brief suggestion for handing the ticket")





def classify_ticket(ticket_text: str) -> TicketClassification:
    try:
        response = Client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=TicketClassification,
            temperature=0,
            max_retries=3,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": ticket_text},
            ],
        )
        return response

    except Exception as e:
        print(f"Error processing ticket: {e}")
        return None
