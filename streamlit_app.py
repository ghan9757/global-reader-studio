
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Global Reader Understanding Studio",
    layout="wide"
)

# Document upload section
st.title("Global Reader Understanding Studio")
st.subheader("Upload documents for comparison")

st.write(
    "Upload a Plain Language Summary and its corresponding "
    "source document to begin the review process."
)

col1, col2 = st.columns(2)

with col1:
    pls_file = st.file_uploader(
        "1. Upload Plain Language Summary",
        type=["pdf", "docx"],
        key="pls_upload"
    )

with col2:
    source_file = st.file_uploader(
        "2. Upload Source Document (e.g., Protocol)",
        type=["pdf", "docx"],
        key="source_upload"
    )

# Display uploaded file information
if pls_file is not None:
    st.success("PLS document received!")
    st.caption(
        f"File: {pls_file.name} | "
        f"Size: {pls_file.size / 1024:.1f} KB"
    )

if source_file is not None:
    st.success("Source document received!")
    st.caption(
        f"File: {source_file.name} | "
        f"Size: {source_file.size / 1024:.1f} KB"
    )

# Confirm when both documents are uploaded
if pls_file is not None and source_file is not None:
    st.success(
        "Both documents have been uploaded successfully!"
    )
    st.info(
        "Next step: Extract document sections and prepare "
        "them for AI comparison."
    )
else:
    st.info("Please upload both documents to continue.")

st.divider()

# Display existing HTML prototype
html_file = Path(__file__).parent / "index.html"

html_content = html_file.read_text(encoding="utf-8")

components.html(
    html_content,
    height=1000,
    scrolling=True
)
