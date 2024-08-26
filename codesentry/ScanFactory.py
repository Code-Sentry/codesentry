from .scans.methods.SQLInjectionScan import SQLInjectionScan
from .scans.methods.XSSScan import XSSScan
from .scans.methods.AllMethodScan import AllMethodScan
# from .scans.methods.StaticAnalysis.StaticAnalysis import StaticAnalysisScan

class ScanFactory:
    @staticmethod
    def get_scan(scan_type):
        scans = {
            'sql-injection': SQLInjectionScan,
            'xss': XSSScan,
            'full': AllMethodScan,
            # 'static-analysis': StaticAnalysisScan,
        }
        scan_class = scans.get(scan_type)
        if scan_class:
            return scan_class()
        else:
            raise ValueError(f"Scan type '{scan_type}' is not recognized.")