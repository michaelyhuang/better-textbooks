from PyPDF2 import PdfFileReader, PdfFileWriter
import fpdf

rdr = PdfFileReader("short.pdf")
print(rdr.getNamedDestinations())

writer = PdfFileWriter()
writer.appendPagesFromReader(rdr)
writer.addLink(0, 1, [63,192,260,204], "dott")

output_path = "linked.pdf"

with open(output_path, 'wb') as fileobj:
    writer.write(fileobj)