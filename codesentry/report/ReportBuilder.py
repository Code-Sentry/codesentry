from ..core.DatabaseManager import *
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime

class ReportBuilder:

    def __init__(self, result) -> None:
        self.result = result
        self.pathReport = "C:/Users/Kaio/Documents/"

        self.canvas = canvas.Canvas(self.pathReport + "report_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".pdf", pagesize=letter)
        self.width, self.height = letter
        
    def mount(self):
        self.header()

        self.canvas.showPage()
        self.canvas.save()

    def header(self):
        # Adicionar cabeçalho com o nome da ferramenta e data atual
        self.canvas.setFont("Helvetica-Bold", 20)
        header_text = f"CodeSentry - Relatório {datetime.today().strftime('%d/%m/%Y')}"
        text_width = self.canvas.stringWidth(header_text, "Helvetica-Bold", 20)
        self.canvas.drawString((self.width - text_width) / 2, self.height - 50, header_text)

        # Adicionar linha preta abaixo do cabeçalho
        self.canvas.setStrokeColorRGB(0, 0, 0)
        self.canvas.line(50, self.height - 60, self.width - 50, self.height - 60)