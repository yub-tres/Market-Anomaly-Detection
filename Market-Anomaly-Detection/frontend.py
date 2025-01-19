import streamlit as st
import requests

# Streamlit app title
st.title("Market Anomaly Detection Chatbot")

# Instructions for the user
st.write("Ask me about portfolio performance, anomalies, or anything related to your financial data!")

# Input box for user query
user_query = st.text_input("Enter your query:", placeholder="e.g., Detect anomalies in my data.")

if st.button("Submit"):
    if user_query:
        # Send the user query to the Flask backend
        try:
            url = "http://127.0.0.1:5002/chat"  # Ensure this matches Flask's port
            response = requests.post(url, json={"query": user_query})
            if response.status_code == 200:
                chatbot_response = response.json().get("response", "No response received.")
                st.success(f"Chatbot says: {chatbot_response}")
            else:
                st.error(f"Error: Received status code {response.status_code} from backend.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query!")
