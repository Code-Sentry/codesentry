from ..scanModel import scanModel
from ...Semgrep import *

class AllMethodScan(scanModel):
    def __init__(self):
        print("Initializing Full Scan")

    def description(self):
        # Descrição do scan que será usada no print
        return "SQL Injection vulnerability scan"

    def run(self, directory):
        # Implementação do scan
        print("Running Full Scan...")

        semgrep = SemgrepScan()
        semgrep.run(directory)
        
        # Aqui você pode adicionar a lógica real de detecção de SQL Injection
        print("Full Scan completed")