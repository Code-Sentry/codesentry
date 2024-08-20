from abc import ABC, abstractmethod

class scanModel(ABC):
    @abstractmethod
    def run(self):
        """Executa o scan. Todos os scans devem implementar este método."""
        pass

    @abstractmethod
    def description(self):
        """Retorna uma descrição do scan."""
        pass