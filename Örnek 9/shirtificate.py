from fpdf import FPDF

def create_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("Arial", style="B", size=24)
    pdf.cell(0, 40, "CS50 Shirtificate", ln=True, align="C")

    pdf.image("shirtificate.png", x=10, y=60, w=190)

    pdf.set_text_color(255, 255, 255)

    pdf.set_font("Arial", style="B", size=24)


    pdf.set_xy(10, 145)
    pdf.cell(190, 10, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

def main():
    name = input("Enter your name: ").strip()
    create_shirtificate(name)
    print("Shirtificate generated as 'shirtificate.pdf'.")

if __name__ == "__main__":
    main()
