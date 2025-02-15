import torch
torch.set_default_device("cpu")

import os
import torch
import streamlit

torch.classes.__path__ = [os.path.join(torch.__path__[0], torch.classes.__file__)] 
torch.classes.__path__ = []

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=100):
    """Generate a summary using BART model."""
    if not text:
        return "No summary available."
    summary = summarizer(text, max_length=max_length, min_length=30, do_sample=False)
    return summary[0]['summary_text']
