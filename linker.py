from PyPDF2 import PdfFileReader, PdfFileWriter

class linker:

    def createLink(self, filePath, origin, destination, location):
        rdr = PdfFileReader(filePath)
        writer = PdfFileWriter()
        writer.appendPagesFromReader(rdr)
        writer.addLink(origin, destination, location, "dott")

        output_path = "linked.pdf"

        with open(output_path, 'wb') as fileobj:
            writer.write(fileobj)

if __name__ == '__main__':
    fp = input("File path: ")
    orig = 0
    dest = 1
    loc = [100,200,150,250]
    linkerObj = linker()
    linkerObj.createLink(fp, orig, dest, loc)