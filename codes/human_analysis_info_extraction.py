import pandas as pd
from analysis_info_extraction import AnalysisBase, Descriptor
from docx import Document
import glob
import json


class HumanAnalysisResult(AnalysisBase):

    def __init__(self, title):
        super().__init__(title)

def extract_titles(csv_path):
    df = pd.read_csv(csv_path)
    new_df = pd.DataFrame({
    "Row": [f"Row {i+1}" for i in range(len(df))],
    "Title": df.iloc[:, 0]  # Assuming the title is in the first column
    })

    output_path = 'titles.csv'
    new_df.to_csv(output_path, index=False)
    print(f"Saved {output_path}")


def csv_to_dict(csv_path):
    df = pd.read_csv(csv_path)
    return {row[0]: row[1] for row in df.values}

title_dict = csv_to_dict("./Ruchi_labels/titles.csv") # Change this to ./labels/titles.csv to get the titles of the gpt generated stories
result_dict = {title: HumanAnalysisResult(title) for title in title_dict.values()} # the list is going to be a list of Descriptor objects
def docx_formatter(docx_path):
    # given the docx file
    # Change this to ./labels/ to do process labels of the gpt generated stories
    descriptor, connotation = docx_path.replace("./Ruchi_labels/", "").split("_column")[0] + "_descriptors", docx_path.split("_")[-1].split(".docx")[0]
    texts = Document(docx_path).paragraphs
    for t in texts:
        i = t.text
        if i:
            title = title_dict[i.split(": ")[0].strip().replace(":", "")]
            words = i.split(":")[1].replace(" - ", "-").strip().split(" ")
            result_dict[title].descriptor_word_table[descriptor] = result_dict[title].descriptor_word_table.get(descriptor, Descriptor(descriptor, [], [], []))
            if connotation == "positive":
                result_dict[title].descriptor_word_table[descriptor].add_positive_words(words)
            elif connotation == "negative":
                result_dict[title].descriptor_word_table[descriptor].add_negative_words(words)
            else:
                result_dict[title].descriptor_word_table[descriptor].add_neutral_words(words)
        
if __name__ == "__main__":
    # change this to ./labels to process the labels of the gpt generated stories
    docx_list = glob.glob("./Ruchi_labels/*.docx")
    human_analysis_report = {}
    for doc in docx_list:
        print(doc)
        docx_formatter(doc)
    for title, analysis_result in result_dict.items():
        new_title = title.replace(" ", "_").replace(".txt", "")
        human_analysis_report[new_title] = analysis_result.generate_report()
    
    with open("book_human_analysis_report.json", "w") as f:
        json.dump(human_analysis_report, f, indent=2)

    