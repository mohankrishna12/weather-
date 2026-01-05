from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def pdf_agent(text, filename="weather_report.pdf"):
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Weather Report")

    c.setFont("Helvetica", 12)
    y = height - 100
    for line in text.split("\n"):
        c.drawString(50, y, line)
        y -= 18

    c.save()
    return filename
