from ..core.DatabaseManager import *
import io
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os
import json

class ReportBuilder:

    def __init__(self, result, path) -> None:
        if isinstance(result, str):
            self.result = json.loads(result)

        self.pathReport = "C:/Users/Kaio/Documents/"
        nameFile = self.pathReport + "report_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".pdf"
        self.current_project = self.get_project(path)

        self.canvas = canvas.Canvas(nameFile, pagesize=letter)
        self.width, self.height = letter

        self.save_path_report(nameFile)
        
    def mount(self):
        self.header()
        self.vulnerabilities(self.result.get('results', []))

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

    def vulnerabilities(self, vulnerabilities_list):
        y_position = self.height - 100
        self.canvas.setFont("Helvetica", 12)

        for vulnerability in vulnerabilities_list:
            # print(vulnerability)
            if y_position < 100:
                self.canvas.showPage()
                y_position = self.height - 100

            # Adiciona informacoes iniciais
            self.canvas.drawString(50,  y_position, "Severidade: " + vulnerability.get('extra', {}).get('severity', 'N/A'))
            y_position -= 20
            self.canvas.drawString(50,  y_position, "Caminho do Arquivo: " + vulnerability.get('path', 'N/A'))
            y_position -= 20

            vulnerability_class = vulnerability.get('extra', {}).get('metadata', {}).get('vulnerability_class', [])
            if isinstance(vulnerability_class, list):
                vulnerability_class = ' | '.join(vulnerability_class)
            else:
                vulnerability_class = str(vulnerability_class)
            self.canvas.drawString(50, y_position, "Classe de vulnerabilidade: " + vulnerability_class)
            y_position -= 20

            self.canvas.drawString(50,  y_position, "Mensagem: " + vulnerability.get('extra', {}).get('message', 'N/A'))
            y_position -= 20

            # Adiciona linhas de início e fim
            self.canvas.drawString(50,  y_position, "Linhas " )
            y_position -= 20
            self.canvas.drawString(70,  y_position, "Inicio: " + str(vulnerability.get('start', {}).get('line', 'N/A')))
            self.canvas.drawString(150,  y_position, "Final: " + str(vulnerability.get('end', {}).get('line', 'N/A')))

            # Adiciona tecnologias
            y_position -= 20
            technologies = vulnerability.get('extra', {}).get('metadata', {}).get('technology', [])
            if isinstance(technologies, list):
                technologies = ' | '.join(technologies)
            else:
                technologies = str(technologies)
            self.canvas.drawString(50, y_position, "Tecnologia: " + technologies)

            y_position -= 20
            self.canvas.drawString(50, y_position, "Impacto: " + vulnerability.get('extra', {}).get('metadata', {}).get('impact', 'N/A'))
            y_position -= 20

            cwe_list = vulnerability.get('extra', {}).get('metadata', {}).get('cwe', [])
            if isinstance(cwe_list, list):
                cwe_text = ' | '.join(cwe_list)
            else:
                cwe_text = str(cwe_list)
            self.canvas.drawString(50, y_position, "CWE: " + cwe_text)
            y_position -= 20

            owasp_list = vulnerability.get('extra', {}).get('metadata', {}).get('owasp', [])
            if isinstance(owasp_list, list):
                owasp_text = ' | '.join(owasp_list)
            else:
                owasp_text = str(owasp_list)
            self.canvas.drawString(50, y_position, "OWASP: " + owasp_text)
            y_position -= 20

            references = vulnerability.get('extra', {}).get('metadata', {}).get('references', [])
            if isinstance(references, list):
                references_text = ' | '.join(references)
            else:
                references_text = str(references)
            self.canvas.drawString(50, y_position, "Referências externas: " + references_text)


            y_position -= 20
            self.canvas.line(50, y_position, self.width - 40, y_position)
            y_position -= 10

    def get_project(self, url):
        try:
            projects_path = os.path.join(os.path.expanduser('~'), 'Documents', 'projects.json')
            with open(projects_path, "r") as file:
                projects = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("O arquivo 'projects.json' não foi encontrado.")

        for project in projects:
            if project.get("url") == url:
                return project

        raise ValueError("Nenhum projeto atual foi encontrado no arquivo 'projects.json'.")

    def save_path_report(self, path):
        try:
            reports_path = os.path.join(os.path.expanduser('~'), 'Documents', 'reports.json')
            with open(reports_path, "r") as file:
                reports = json.load(file)
        except FileNotFoundError:
            reports = []

        new_report = {
            "name": self.current_project.get("name", "N/A") + " " + datetime.today().strftime('%d/%m/%Y'),
            "path": self.current_project.get("url", "N/A"),
            "project": self.current_project.get("name", "N/A"),
            "lastRun": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "status": "Completed",
            "file": path
        }
        reports.append(new_report)

        with open(reports_path, "w") as file:
            json.dump(reports, file, indent=4)