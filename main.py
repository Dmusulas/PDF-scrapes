import pdfplumber
from os import listdir
from os.path import isfile, join
import re
import numpy as np

path_1 = "../../../OneDrive - ISM University of Management and Economics/University stuff/Investment Management/Slides/"
onlyfiles = [f for f in listdir(path_1) if isfile(join(path_1, f))]

new_paths = [path_1 + i for i in onlyfiles]


def extractTextFromPDF(path, method="dict"):
    with pdfplumber.open(path) as pdf:
        if method == "dict":
            full_text = {"page": [], "text": []}
        else:
            full_text = np.array([])
        for i in range(len(pdf.pages)):
            page = pdf.pages[i]
            try:
                list_of_chars = page.chars
            except:
                continue
            page_text = []
            for item in list_of_chars:
                letter = item["text"]
                page_text.append(letter)
            page_text = "".join(page_text)
            page_text = re.sub("§", " ", page_text)
            page_text = re.split(r"(?<=[a-z]{1})(?=[A-Z]|\d)", page_text)
            page_text = " ".join(page_text)
            page_text = re.sub(r"Silviu\s{1}Ursu\s{1}M\d{2}|\s+ISM Vilnius,Lithuania\s+September-October\s2021", "", page_text)
            page_text = f'Page {i+1}:' + page_text

            if method == "dict":
                full_text["page"].append(i + 1)
                full_text["text"].append(page_text)
            else:
                full_text = np.append(full_text, page_text)
        if method == "dict":
            return [f'{page} + {text}' for page, text in full_text.items()]
        else:
            return np.array2string(full_text)

with open('test.doc', 'w', encoding='utf-8') as f:
    for file in range(len(new_paths)):
        f.write(f'{onlyfiles[file]} \n')
        f.write(extractTextFromPDF(new_paths[file], method=" "))
