# Jung’s Word-Association Experiments – Research & Analysis

## Overview

This repository is dedicated to the exploration, analysis, and practical application of Carl Gustav Jung’s Word-Association Test (WAT), a pioneering psychological tool used to investigate the unconscious mind and emotional complexes.

The project aims to:

- Implement the classical Word-Association Test methodology as a web application powered by LLMs.
- Analyze patterns in reaction times, semantic associations, and emotional responses.
- Develop ML-based tools for identifying subconscious patterns and personal complexes.
- Provide open-source tools for further psychological research.

## Background

Jung’s Word-Association Test was a groundbreaking psychological experiment in which subjects were presented with stimulus words and asked to respond with the first word that came to mind. Jung observed delays, errors, or unusual responses as indicators of emotional complexes hidden in the unconscious.

Key elements in WAT analysis:

- Reaction Time: Delay in response hints at internal conflict.
- Repeating Words: Reflects persistent thought patterns.
- Emotional Responses: Indicate underlying psychological content.

## Methodology

1. **Language Selection**:

   - The user selects the language for the test: English, Russian, or Dutch.
2. **Data Generation (generate_data.py)**:

   - The script randomly selects 100 words from the national corpus of the chosen language:
     - British National Corpus (English): http://www.natcorp.ox.ac.uk
     - Russian National Corpus: https://ruscorpora.ru/en/
     - Dutch Corpus (e.g., SoNaR corpus): https://www.clarin.eu/content/dutch-language-corpora
3. **Test Procedure**:

   - The 100 randomly chosen words are shown one by one to the user.
   - Presentation intervals gradually shorten as the task progresses, requiring faster responses.
4. **User Response**:

   - The user verbally or textually provides an association for each word as quickly as possible.
5. **Data Analysis (LLM + Clustering)**:

   - After the task, an LLM (e.g., GPT-based) analyzes the user's responses:
     - Clustering by Response Time: Classifies responses based on time delays.
     - Semantic Clustering: Groups responses with similar meanings using semantic similarity analysis.
     - Response Time Analysis: Calculates the average response time across all words.
6. **Complexity & Deep Analysis**:

   - Semantic clusters associated with response times longer than average are flagged for further analysis.
   - The flagged responses are further interpreted using LLM analysis (e.g., assessing emotional content, potential personal significance, or complex activation).
