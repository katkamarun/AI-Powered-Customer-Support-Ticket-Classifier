import streamlit as st
from ticket_classifier import classify_ticket  # Import your classification function

# Streamlit UI elements
st.title("AI-Powered Customer Support Ticket Classifier")
st.write(
    "This application classifies customer support tickets based on their content, "
    "assessing category, urgency, sentiment, and more. Try it out below!"
)

# Set default value for ticket_input and example_choice in session_state
if "ticket_input" not in st.session_state:
    st.session_state["ticket_input"] = ""
if "example_choice" not in st.session_state:
    st.session_state["example_choice"] = "Select an example"

# Dropdown for example tickets
example_options = {
    "Select an example": "",
    "Order Issue": "I ordered a laptop but received a tablet instead. Can you help?",
    "Account Access": "I'm having trouble logging into my account. The reset link isn't working.",
    "Technical Support": "The software crashes every time I open the settings. Can you help?",
    "Billing": "I was charged twice for my order. Please refund the extra payment.",
}

# Display the dropdown with the selected example
st.session_state["example_choice"] = st.selectbox(
    "Choose an example ticket:",
    list(example_options.keys()),
    index=list(example_options.keys()).index(st.session_state["example_choice"]),
)

# If an example ticket is selected, update the ticket_input
if st.session_state["example_choice"] != "Select an example":
    st.session_state["ticket_input"] = example_options[
        st.session_state["example_choice"]
    ]

# Clear button to reset ticket input and example choice
if st.button("Clear"):
    st.session_state["ticket_input"] = ""
    st.session_state["example_choice"] = "Select an example"

# Input text area for ticket input
ticket_input = st.text_area(
    "Enter the customer support ticket text:", st.session_state["ticket_input"]
)

# Input validation
if len(ticket_input.strip()) < 10:
    st.warning("Please enter a meaningful ticket (at least 10 characters).")

# Classify ticket button
if st.button("Classify Ticket"):
    if ticket_input.strip() != "" and len(ticket_input.strip()) >= 10:
        with st.spinner("Classifying the ticket..."):
            # Call the classifier function to process the input
            result = classify_ticket(ticket_input)

            # Display the classification results
            st.markdown("---")
            st.subheader("Classification Results")
            st.write(f"**Category**: {result.category}")
            st.write(f"**Urgency**: {result.urgency}")
            st.write(f"**Sentiment**: {result.sentiment}")
            st.write(f"**Confidence**: {result.confidence}")
            st.write(f"**Key Information**: {', '.join(result.key_information)}")
            st.write(f"**Suggested Action**: {result.suggested_action}")
    else:
        st.warning("Please enter a valid customer support ticket.")
