import streamlit as st
import time
import json
from src.scripts.generate_data import load_words
from src.scripts.speech_to_text import record_audio
from scripts.clustering import cluster_responses

from adapters.openai import OpenAIAdapter
from adapters.together import TogetherAdapter

# Load LLM adapters
openai_adapter = OpenAIAdapter()
together_adapter = TogetherAdapter()

# Streamlit Configuration
st.set_page_config(page_title="Word Response Test", layout="centered")
st.title("Word Response Test")

# Sidebar - Language Selection
language = st.sidebar.selectbox("Choose a language:", ["English", "Russian", "Dutch"])

# Load words
if "words" not in st.session_state:
    st.session_state.words = load_words(language.lower())
    st.session_state.responses = []

# Show words with decreasing intervals
if st.session_state.words:
    current_word = st.session_state.words.pop(0)
    st.write(f"### 📝 Say the first word that comes to mind for: **{current_word}**")

    # Record user response
    if st.button("🎤 Start Recording"):
        response_text, response_time = record_audio()
        st.write(f"**You said:** {response_text}")
        st.write(f"⏳ Response Time: {response_time:.2f} seconds")

        # Save response
        st.session_state.responses.append({"word": current_word, "text": response_text, "time": response_time})

        # Adjust presentation interval (faster each time)
        interval = max(1.0, 3.0 - (len(st.session_state.responses) * 0.05))
        time.sleep(interval)

# Run Clustering Analysis
if st.button("🔍 Analyze Results"):
    clustered_data = cluster_responses(st.session_state.responses)

    # Use LLM to analyze the clusters
    analysis_prompt = f"Clustered response data:\n{json.dumps(clustered_data, indent=2)}\nAnalyze patterns in response speed and meaning."
    llm_response = openai_adapter.generate(analysis_prompt)

    st.write("### 📊 Analysis by LLM")
    st.write(llm_response)

    # Show Clustering Results
    st.write("### 🔬 Clustering Results")
    st.json(clustered_data)
