import pandas as pd
from transformers import pipeline
import matplotlib.pyplot as plt

# Load the language model pipeline for summarization
summarizer = pipeline("summarization")

# Load the Excel sheet
excel_path = "path/to/your/excel/file.xlsx"
df = pd.read_excel(excel_path)

# Get user query
query = input("Enter your query: ")

# Assume you want to create a summary
if "summary" in query.lower():
    # Concatenate all columns into a single string for summarization
    text_to_summarize = " ".join(str(cell) for cell in df.values.flatten())
    
    # Use the language model to generate a summary
    summary = summarizer(text_to_summarize, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, temperature=0.5)
    
    print("Summary:", summary[0]['summary_text'])

# Assume you want to create a chart
elif "chart" in query.lower():
    # Plot a bar chart of numeric columns
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            plt.figure(figsize=(10, 6))
            plt.bar(df.index, df[column])
            plt.title(f'Bar Chart for {column}')
            plt.xlabel('Index')
            plt.ylabel(column)
            plt.show()
