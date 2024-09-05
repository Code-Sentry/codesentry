from ..core.DatabaseManager import *

class ReportBuilder:
    
    def __init__(self, result) -> None:
        self.result = result
        self.DatabaseManager = DatabaseManager(self.result)
        
    def mount(self):
        self.DatabaseManager.insertDataScan()
        