import platform
import subprocess
import sys

class System:

    @staticmethod
    def getOperatingSystem():
        return platform.system()
    
    @staticmethod
    def isDockerRunning():

        try:
            system = System.getOperatingSystem()
            if system == "Windows":
                result = subprocess.run(["docker", "info"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                
            elif system == "Linux" or system == "Darwin":
                result = subprocess.run(["docker", "info"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
            if result.returncode == 0:
                return True
            else:
                print("Docker não está sendo executado.")
                sys.exit(1)

        except Exception as e:
            return False, f"Error occurred: {str(e)}"
    