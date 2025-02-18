# Jung’s Word-Association Experiments – Research & Analysis

## Overview

This repository is dedicated to the exploration, analysis, and practical application of **Carl Gustav Jung’s Word-Association Test (WAT)**, a pioneering psychological tool used to investigate the unconscious mind and emotional complexes.

The project aims to:

- Implement the classical **Word-Association Test** methodology as a web app powered by LLMs.
- Analyze patterns in reaction times, associations, and emotional responses.
- Develop ML-based tools for identifying subconscious patterns and personal complexes.
- Provide open-source tools for further research.

---

## Background

**Jung’s Word-Association Test** was a groundbreaking psychological experiment in which subjects were presented with stimulus words and asked to respond with the first word that came to mind. Jung observed delays, errors, or unusual responses as indicators of **emotional complexes** hidden in the unconscious.

Key elements in WAT analysis:

- **Reaction Time**: Delay in response hints at internal conflict.
- **Repeating Words**: Reflects persistent thought patterns.
- **Emotional Responses**: Indicate underlying psychological content.

---


## Data Source and Generation

Data for the Word Association Test (WAT) will be sourced from national language corpora. We are planning to cover three languages:

* **Russian**
* **English**
* **Dutch**

Words will be sorted by frequency, with the selection range expected to be between **2,000 and 3,000 most common words**.

This data extraction and initial processing will be handled by the `generate_initial_wordset.py `script

## References

* British National Corpus (BNC). (n.d.). Retrieved from [http://www.natcorp.ox.ac.uk](http://www.natcorp.ox.ac.uk)
* Fitzpatrick, T., Playfoot, D., Wray, A., & Wright, M. J. (2015). Establishing the reliability of word association data for investigating individual and group differences. Applied Linguistics, 36(1), 23–50. [https://doi.org/10.1093/applin/amt020]()
