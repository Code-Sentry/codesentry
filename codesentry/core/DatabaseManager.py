import sqlite3
from .VulnerabilityManager import *

class DatabaseManager:
    def __init__(self, result, db_name='./codesentry/core/codesentry.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.VulnerabilityManager = VulnerabilityManager(result)
        
    def insertDataScan(self):
        self.createScan()
        self.insertVulnerability()
        
    def insertVulnerability(self):
        vulnerabilities = self.VulnerabilityManager.getVulnerabilities()
        
        for item in dados_para_inserir:
            self.cursor.execute('''
                INSERT INTO vulnerabilities (description, severity, createdAt)
                VALUES (?, ?, datetime('now'))
            ''', (description, severity))
        
        self.connection.commit()
        
    def createScan(self):
        scannedFiles = self.VulnerabilityManager.getPathsScanned()
        severityVulnerability = json.loads(self.VulnerabilityManager.getVulnrebilitySeverityNumber())
        countVulnerability = self.VulnerabilityManager.getCountVulnerabilities()
        
        try:
            self.cursor.execute('''
                INSERT INTO scans (scannedFiles, totalOfVulnerabilities, totalInfo, totalWarning, totalError, executedAt)
                VALUES (?, ?, ?, ?, ?, datetime('now'))
            ''', (str(scannedFiles), countVulnerability, severityVulnerability['info'], severityVulnerability['warning'], severityVulnerability['error']))
            
            self.connection.commit()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")