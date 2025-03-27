import os
import webbrowser
import psutil
import subprocess

class SystemFunctions:
    @staticmethod
    def open_chrome():
        """Open Google Chrome browser"""
        try:
            webbrowser.open("https://www.google.com")
            return "Chrome opened successfully"
        except Exception as e:
            return f"Failed to open Chrome: {str(e)}"
    
    @staticmethod
    def open_calculator():
        """Open system calculator"""
        try:
            if os.name == 'nt':  # Windows
                os.system("calc")
            elif os.name == 'posix':  # MacOS and Linux
                subprocess.Popen(['gnome-calculator'])
            return "Calculator opened successfully"
        except Exception as e:
            return f"Failed to open calculator: {str(e)}"
    
    @staticmethod
    def get_system_resources():
        """Retrieve current system CPU and RAM usage"""
        return {
            "cpu_usage": psutil.cpu_percent(),
            "memory_usage": psutil.virtual_memory().percent
        }
    
    @staticmethod
    def run_shell_command(command=None):
        """Execute a shell command"""
        if command is None:
            return "No command provided"
        
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            return {
                "stdout": result.stdout,
                "stderr": result.stderr,
                "returncode": result.returncode
            }
        except Exception as e:
            return {"error": str(e)}
