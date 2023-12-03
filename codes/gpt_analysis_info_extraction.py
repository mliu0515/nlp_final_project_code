import os
import glob
import json
from analysis_info_extraction import AnalysisBase, Descriptor

'''for each txt file, the information I want to extract:
1. Title of the book
2. Each seed descriptor
    a. all the list of words
    b. the ones with positive connotations
    c. the ones with negative connotations
3. Overall analysis
'''
# Change this to gpt_analysis_on_generated_stories to get the analysis on generated stories
gpt_analysis_on_generated_stories = glob.glob("gpt_analysis_on_books_and_literatures/*.txt")

class AnalysisResult(AnalysisBase):
    def __init__(self, title, raw_text):
        super().__init__(title)
        self.raw_text = raw_text.lower()
        self.overall_analysis = self.raw_text.split("------\n")[-1].replace("overall analysis: ", "").strip()

        parts = self.raw_text.split("------\n")[1:-1]
        
        for i, descriptor_name in enumerate(AnalysisBase.seed_descriptors):
            try:
                cur_part = parts[i]
                # Extracting words with positive and negative connotations, and additional descriptions
                positive_words = cur_part.split("positive: ")[1].split("negative: ")[0].strip().split(", ")
           
                negative_words = cur_part.split("negative: ")[1].split("neutral: ")[0].strip().split(", ")
                # print(negative_words)
                neutral_words = cur_part.split("neutral: ")[1].lstrip().split(", ")
                # if (len(positive_words) + len(negative_words) + len(neutral_words)) != 20:
                #     print(title)
                #     break
                # additional_description = parts[2].split(": ")[1] # The second element after splitting by ": "
                cur_descriptor = Descriptor(descriptor_name, positive_words, negative_words, neutral_words)
                self.descriptor_word_table[descriptor_name] = cur_descriptor
            except Exception as e:
                print(f"Error occured when processing {self.title}, {descriptor_name}")
                [print(part + "\n------\n") for part in parts]
                print(e)
                break

    def generate_report(self):
        '''
        Generate a report of the analysis result, output that in a json object. What we want in the analysis
        title: the title of the book
        for each seed_descriptor:
        {
            positive_count: <number of positive words>
            positive_words: <list of positive words>
            negative_count: <number of negative words>
            negative_words: <list of negative words>
            all_count: <number of all words>
            all_words: <list of all words>
            positive_ratio: <positive count / all count>
            negative_ratio: <negative count / all count>
            overall_analysis: <overall analysis>
        }
        '''
        report = super().generate_report()
        report["overall_analysis"] = self.overall_analysis
        return report


if __name__ == "__main__":
    gpt_analysis_report = {}
    for file in gpt_analysis_on_generated_stories:
        text = ""
        with open(file, "r") as f:
            for line in f:
                # Remove tabs
                line_without_tabs = line.replace('\t', '')
                # Check if the line is not empty after removing tabs and newlines
                if line_without_tabs.strip() != '':
                    if "Descriptors" in line_without_tabs or "Descritpors" in line_without_tabs:
                        # Dude lol I misspelled a word lmaoooo
                        text += "------\n"
                    else:
                        if "Overall Analysis" in line_without_tabs:
                            text += "------\n"
                        text += line_without_tabs.replace("[", "").replace("]", "").replace("\'", "").lstrip() + "\n"
        title = file.split("/")[1].split(".txt")[0]
        if title.lower == "beloved.txt":
            gpt_analysis_report[title] = None
        else:
            analysis_result = AnalysisResult(title, text)
 
        report = analysis_result.generate_report()
        gpt_analysis_report[title] = report

    with open("books_gpt_analysis_report.json", "w") as f:
        json.dump(gpt_analysis_report, f, indent=2)