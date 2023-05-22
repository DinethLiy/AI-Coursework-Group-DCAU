import streamlit as st

# Define a dictionary of responses
responses = {
    "hi": "Hello!",
    "how are you?": "I'm doing well, thank you. How can I help you today?",
    "what's your name?": "My name is ChatBot. What's yours?",
    "bye": "Goodbye! Have a nice day."
}

# Define a function to generate a response to the user's message
def generate_response(user_input):
    # Convert user input to lowercase and remove any punctuation
    cleaned_input = user_input.lower().strip(".,!?\n")

    # Check if the input matches any of the responses in our dictionary
    if cleaned_input in responses:
        return responses[cleaned_input]
    else:
        return "I'm sorry, I don't understand. Can you please try again?"

# Set Streamlit app title and description
st.set_page_config(page_title="ChatBot", page_icon=":robot_face:", layout="wide")
st.title("ChatBot")
st.markdown("Type your message below and press Enter to send it to the chatbot:")

# Define a list to store the chat history
chat_history = []

# Define a text input field for the user's message
user_input = st.text_input("")

# Define a button to send the user's message to the chatbot
if st.button("Send"):
    # Display the user's message
    st.write("You:", user_input)

    # Generate a response from the chatbot based on the user's message
    response = generate_response(user_input)

    # Display the chatbot's response
    st.write("Chatbot:", response)

    # Add the user's message and the chatbot's response to the chat history
    chat_history.append(("You", user_input))
    chat_history.append(("Chatbot", response))

# Display the chat history on the page
st.write("")
st.write("Chat history:")
for name, message in chat_history:
    st.write(name + ":", message)
