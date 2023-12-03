**Workflow for GPT story generation and analysis:**
1. Extract the first sentence: extract_text.py. Output: all_books_with_prompt_sentence.json
2. Generate the full GPT stories using all_books_with_prompt_sentence.json, the code is on Google Drive. Output: a folder full of txt files
3. With the stories, do guided LDA, and the code is on Google Drive. Output: lda_results_generated_stories_adj_only.csv
4. Using the CSV, let GPT identity bias: gpt_eval.py. Output: gpt_analysis_on_books_and_literatures (a directory full of Txt file analysis)
5. Extract the word lists from all the txt files, and format the analysis results in a JSON file: gpt_analysis_info_extraction.py. Output: generated_stories_gpt_analysis_report.json
6. And then I do human labeling. The results of the labels are stored in Word docs and then processed by human_analysis.py (to break it down into more Word documents) and human_analysis_info_extraction.py to generate generated_stories_human_analysis_report.json

NOTE: you have to change the file paths in the original code in order to run it properly