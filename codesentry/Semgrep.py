import subprocess
import json
from typing import Dict, List, Optional
from .report.ReportBuilder import *

class SemgrepScan:
    def __init__(self, config: str = "auto", output_format: str = "json"):
        self.config = config
        self.output_format = output_format
    
    def run(self, path: str, additional_args: Optional[List[str]] = None) -> Dict:
        """
        Executa o Semgrep no diretório ou arquivo especificado.

        :param path: Caminho do diretório ou arquivo a ser escaneado.
        :param additional_args: Argumentos adicionais para o comando Semgrep.
        :return: Resultados do scan em formato JSON.
        """

        # command = ["semgrep", "--config", self.config, path, f"--{self.output_format}"]
        command = [
            "docker", "run", "--rm", 
            "-v", f"{path}:/src", 
            "returntocorp/semgrep", 
            "semgrep", "--config", self.config, "/src", 
            f"--{self.output_format}"
        ]

        if additional_args:
            command.extend(additional_args)

        try:
            result = subprocess.run(
                command, 
                capture_output=True, 
                text=True, 
                encoding='utf-8'
            )

            print(result.stdout)
            if result.returncode != 0:
                print(f"Erro ao executar o Semgrep no Docker: {result.stderr}")
            
            report_builder = ReportBuilder(result.stdout)
            report_builder.mount()
                
        except FileNotFoundError:
            print("Docker não foi encontrado. Verifique se está instalado e disponível no PATH.")
        except Exception as e:
            print(f"Erro ao executar o comando Docker: {e}")

        if result.returncode != 0:
            raise RuntimeError(f"Erro ao executar Semgrep: {result.stderr}")

        return json.loads(result.stdout)