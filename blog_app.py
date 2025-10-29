import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("GROQ_API_KEY not found in .env file.")
    st.stop()

# Initialize Groq client
client = Groq(api_key=api_key)

# Blog generator function
def generate_blog(topic):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "You are a professional blog writer."},
                {"role": "user", "content": f"Write a detailed, engaging blog post about: {topic}"}
            ],
            max_tokens=800,
            temperature=0.6,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f" Error: {e}"


st.title("Blog Generation")

topic = st.text_input("Enter a blog topic:", placeholder="e.g. The Future of Artificial Intelligence")

if st.button("Generate Blog"):
    if topic.strip():
        with st.spinner("Generating..."):
            blog = generate_blog(topic)
            st.subheader("Generated Blog")
            st.write(blog)
    else:
        st.warning("Please enter a topic first.")

