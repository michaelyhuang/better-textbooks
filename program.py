# pdfminer to html did not work well
# pdf2txt.py -o pdfminer-simplified.html simplified.pdf


import pdfminer
print(pdfminer.__version__)

import indexToDict

# Convert index to a dictionary
index = indexToDict.converter()
print(index)