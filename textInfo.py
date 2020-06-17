from pdfminer.layout import LAParams, LTTextBox,LTTextLine, LTTextBoxHorizontal, LTFigure
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice
import pdfminer

from io import StringIO

output_string = StringIO()

fp = open('short.pdf', 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)
textDict = {}

def parse_obj(lt_objs):
    validTypes = (LTTextBox, LTTextLine, LTTextBoxHorizontal, LTFigure)
    if isinstance(lobj, validTypes):
        # loop over the object list
        for obj in lt_objs:

            if isinstance(obj, pdfminer.layout.LTTextLine):
                textLine = obj.get_text()
                x0, y0, x1, y1 = obj.bbox[0], obj.bbox[1], obj.bbox[2], obj.bbox[3]
                output_string.write("%6d, %6d, %6d, %6d, %s" % (x0, y0, x1, y1, textLine))
                textDict.update({textLine.replace('\n', '') : [pageNum, x0, y0, x1, y1]})

            # if it's a textbox, also recurse
            if isinstance(obj, pdfminer.layout.LTTextBoxHorizontal):
                parse_obj(obj._objs)

            # if it's a container, recurse
            elif isinstance(obj, pdfminer.layout.LTFigure):
                parse_obj(obj._objs)


for pageNumber, page in enumerate(pages):
    print('Processing next page...')
    interpreter.process_page(page)
    layout = device.get_result()
    pageNum = pageNumber
    for lobj in layout:
        parse_obj(lobj)
        #if isinstance(lobj, LTTextBox):
            #x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
            #print('At %r is text: %s' % ((x, y), text))
            #output_string.write('At %r is text: %s' % ((x, y), text))


content = output_string.getvalue()
output_file= open("textInfo.txt","w")
output_file.write(content)
output_file.close()

print(textDict)