import PyPDF2
from os import listdir
from os.path import isfile, join
import re
import numpy as np

path_1 = "../../../OneDrive - ISM University of Management and Economics/University stuff/Investment Management/Slides/"
onlyfiles = [f for f in listdir(path_1) if isfile(join(path_1, f))]

new_path = path_1 + onlyfiles[0]

with open(new_path, mode='rb') as f:

    reader = PyPDF2.PdfFileReader(f)
    print(reader.pages(()))

