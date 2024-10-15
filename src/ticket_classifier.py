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

# Ensure that you pass these keys to the OpenAI client


# ----------------------------------------------
# step 1: Get Clear On Your Objectives
# ----------------------------------------------
"""
Objective:Develop an AI- Powered ticket classification system that:
-Accurately categorizes customer support tickets
-Assesses the urgency and Sentiment of each ticket
-Extracts key information for quick resolution
-Provides confidence scores to flag uncertain cases for human review


Business Impact:
-Reduce average response time by routing tickets to the right department
-Improve customer satisfaction by prioritizing urgent and negative sentiment tickets
-Increase efficiency by providing agents with key information upfront
-optimize workforce allocation by automating routine classifications
"""


# -----------------------------------------------------
# step 2: Patch your LLM with Instructor
# -----------------------------------------------------

# Instructor makes it easy to get structured data like JSON from LLMs
Client = instructor.patch(OpenAI())

# ----------------------------------------------------------
# Step 3: Define Pydantic data models
# ----------------------------------------------------------
""" This code defines a structured data model for classifying customer support tickets using pydantic and
python's Enum class. It specifies categories,urgency levels, customer sentiments, and other relevant information
as predefined options or constrained fields.This structure ensures data consistency, enables automatic validation, and facilitates easy integration with AI models
and other parts of a support ticket system"""


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


# ---------------------------------------------------------
# Step 4: Optimize your prompts and experiment
# ---------------------------------------------------------
# To optimize:
# 1.Refine the system message to  provide more context about your business
# 2.Experiment with different models(e.g.gpt-3.5-turbo vs gpt-4)
# 3.Fine-tune the model on your specific ticket data if available
# 4.Adjust the TicketClassification model based on business needs

SYSTEM_PROMPT = """
You are an AI assistant for a large e-commerce platform's customer support team.
Your role is to analyze incoming customer support tickets and provide structured information  to help our team respond quickly and effectively.


Business Context:
- We handle thousands of tickets daily across various categories (orders, accounts, products, technical issues, billing).
- Quick and accurate classification is crucial for customer satisfaction and operational efficiency.
- We prioritize based on urgency and customer sentiment.

Your tasks:
1. Categorize the ticket into the most appropriate category.
2. Assess the urgency of the issue (low, medium, high, critical).
3. Determine the customer's sentiment.
4. Extract key information that would be helpful for our support team.
5. Suggest an initial action for handling the ticket.
6. Provide a confidence score for your classification.


Remember:
- Be objective and base your analysis solely on the information provided in the ticket.
- If you're unsure about any aspect, reflect that in your confidence score.
- For 'key_information', extract specific details like order numbers, product names, or account issues.
- The 'suggested_action' should be a brief, actionable step for our support team.

Analyze the following customer support ticket and provide the requested information in the specified format.
"""


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
