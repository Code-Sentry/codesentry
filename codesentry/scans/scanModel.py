from abc import ABC, abstractmethod

class scanModel(ABC):
    @abstractmethod
    def run(self, directory):
        self.directory = directory
        """Executa o scan. Todos os scans devem implementar este método."""
        pass

    @abstractmethod
    def description(self):
        """Retorna uma descrição do scan."""
        pass

    def scan_directory(self, directory, file_extension):
        """Percorre o diretório para encontrar arquivos com uma extensão específica."""
        pass