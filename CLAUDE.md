# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
streamlit run analytics.py
```

Dependencies: `pip install streamlit`

## Project Overview

This is a single-file Streamlit portfolio website (`analytics.py`) for showcasing general data science and analytics work. All UI, content, and layout live in that one file.

## Architecture

- **`analytics.py`** — the entire application: page config, bio header, project cards (image + markdown description + link), and a commented-out contact footer.
- **Image assets** (e.g., `sdt_bar.png`) — referenced by `st.image()` and must live in the same directory as `analytics.py`.

## Adding Projects

Each project block follows this pattern:

```python
st.subheader("Project Title")
st.image("image_filename.png", use_column_width=True)
st.markdown("""
**Tools:** ...
**Description:** ...
**View report:** [Link text](url)
""")
```

Commented-out example blocks for "Claims Analytics Report" and "Geospatial Access Map" can serve as templates.

## Enabling the Contact Footer

The footer block at the bottom of `analytics.py` is commented out. Uncomment it and replace placeholder URLs/email before deploying publicly.
