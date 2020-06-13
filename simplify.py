# Temporary program that simplifies textbooks for the development process

from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import sys
import os
import glob

# Later, I will allow the simplify.py to take arguments (page ranges)
# path = argv[1]
# pagesString = argv[2]

# pagesList = map(int, pagesString.strip('[]').split(','))

path = 'textbooks/the-great-conversation.pdf'

pagesList = [*range(722,746), *range(776,782), *range(788,800)]

def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]

    pdf = PdfFileReader(path)
    pdf_merger = PdfFileMerger()
    for page in pagesList:
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        fileName = 'page_{}.pdf'.format(page+1)

        with open(fileName, 'wb') as out:
            pdf_writer.write(out)

        print('Created: {}'.format(fileName))

def merger(output_path, input_paths):
    pdf_merger = PdfFileMerger()
    file_handles = []
    
    for path in input_paths:
        pdf_merger.append(path)
        print('Removed: {}'.format(path))
        os.remove(path)
        
    with open(output_path, 'wb') as fileobj:
        pdf_merger.write(fileobj)

if __name__ == '__main__':
    pdf_splitter(path)
    paths = glob.glob('page_*.pdf')
    paths.sort()
    merger('simplified.pdf', paths)