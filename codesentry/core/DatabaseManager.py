import sqlite3
from .VulnerabilityManager import *

class DatabaseManager:
    def __init__(self, result, db_name='codesentry.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.VulnerabilityManager = VulnerabilityManager(result)
        
    def insertDataScan(self):
        self.createScan()
        
    def insertVulnerability(self):
        self.cursor.execute('''
            INSERT INTO vulnerabilities (description, severity, createdAt)
            VALUES (?, ?, datetime('now'))
        ''', (description, severity))
        
        self.connection.commit()
        
    def createScan(self):
        scannedFiles = self.VulnerabilityManager.getPathsScanned()
        severityVulnerability = json.loads(self.VulnerabilityManager.getVulnrebilitySeverityNumber())
        countVulnerability = self.VulnerabilityManager.getCountVulnerabilities()
        
        self.cursor.execute('''
            INSERT INTO scans (scannedFiles, totalOfVulnerabilities, totalInfo, totalWarning, totalError, executedAt)
            VALUES (?, ?, ?, ?, ?, datetime('now'))
        ''', (scannedFiles, countVulnerability, severityVulnerability['info'], severityVulnerability['warning'], severityVulnerability['error']))
        
        self.connection.commit()