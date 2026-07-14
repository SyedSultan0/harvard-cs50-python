from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", format="A4")
pdf.add_page()

pdf.set_font("Helvetica", size=40)
pdf.cell(0, 40, "CS50 Shirtificate", align="C", ln=True)

shirt_width = 160
pdf.image("shirtificate.png", x=(210 - shirt_width) / 2, y=60, w=shirt_width)

pdf.set_font("Helvetica", size=24)
pdf.set_text_color(255, 255, 255)

pdf.set_xy(0, 140)
pdf.cell(210, 10, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
