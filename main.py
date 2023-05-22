from PyPDF2 import PdfWriter, PdfReader
import io
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3, A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

NAME_FONT = pdfmetrics.registerFont(TTFont('Roca-Two', 'Roca-Two-Bold.ttf'))
FILEPATH = ""

def make_certificate(PER_NAME):
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)
    can.setFillColorRGB(1, 1, 1)
    can.setFont('Roca-Two', 44)
    fName = can.drawString(220, 320, PER_NAME)
    can.save()
    # move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfReader(packet)
    # read your existing PDF
    existing_pdf = PdfReader(open("example.pdf", "rb"))
    output = PdfWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.pages[0]
    page.merge_page(new_pdf.pages[0])
    output.add_page(page)
    # finally, write "output" to a real file
    output_stream = open(f"{PER_NAME}_certificate.pdf", "wb")
    output.write(output_stream)
    output_stream.close()



df = pd.read_excel(FILEPATH)
name_list = df.to_dict(orient='records')

for names in name_list:
    pdfGen = {'name': names['name']}


    PER_NAME = pdfGen['name']

    make_certificate(PER_NAME)
    print(PER_NAME)
