from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")


df = pd.read_csv("src/files/topics.csv")
pdf.add_page()

pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="Hello There", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="Hi There", align="L", ln=1, border=1)

for index, row in df.iterrows():
    print(row)
    print("Vale", row["Topic"])
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border=1)



pdf.output("pdf_file.pdf")
print("pdf generated")