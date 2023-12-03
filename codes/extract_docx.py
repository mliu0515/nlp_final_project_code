import pandas as pd
from docx import Document

# Load the Excel file
excel_path = 'ruchi_lda_labels.xlsx'  # Update with your file path
df = pd.read_excel(excel_path)

# Columns to be extracted
columns_to_extract = ['Male Positive', 'Male Negative', 'Male Neutral', 
                      'Female Positive', 'Female Negative', 'Female Neutral', 
                      'White Positive', 'White Negative', 'White Neutral', 
                      'Non-white Positive', 'Non-white Negative', 'Non-white Neutral', 
                      'Wealthy Positive', 'Wealthy Negative', 'Wealthy Neutral', 
                      'Non-wealthy Positive', 'Non-wealthy Negative', 'Non-wealthy Neutral']

for col in columns_to_extract:
    # Create a Word document for each column
    doc = Document()
    for index, row in df.iterrows():
        paragraph_text = f"Row {index + 1}: {row[col]}"
        doc.add_paragraph(paragraph_text)

    # Save the document with a name based on the column
    valance = col.split(' ')[1].lower()
    descriptor = col.split(' ')[0].lower().replace('-', '_').replace("wealthy", "rich").replace("non_wealthy", "poor")
    doc.save(f'./Ruchi_labels/{descriptor}_column_data_{valance}.docx')
