from docx import Document
from collections import defaultdict

def get_rgb_components(color):
    if not color:
        return 'Default'
    # Extracting RGB components from the integer
    red = color.rgb >> 16
    green = (color.rgb >> 8) & 0xFF
    blue = color.rgb & 0xFF
    return (red, green, blue)

def get_words_by_color(doc_path):
    doc = Document(doc_path)
    color_words = set()

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            color = run.font.color.rgb
            color_words.add(color)

    return color_words

# Example usage
doc_path = './lda_words/white_column_data.docx'  # Replace with your document's path
words_by_color = get_words_by_color(doc_path)
print(words_by_color)
