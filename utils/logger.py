import logging
import time
import os
from datetime import datetime
import json

class FunctionExecutionLogger:
    def __init__(self, log_dir='logs'):

        os.makedirs(log_dir, exist_ok=True)
        
        self.logger = logging.getLogger('function_execution_logger')
        self.logger.setLevel(logging.INFO)
        

        log_file = os.path.join(log_dir, f'function_execution_{datetime.now().strftime("%Y%m%d")}.log')
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        console_handler = logging.StreamHandler() 
        console_handler.setLevel(logging.INFO)
        

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
        
        self.metrics_file = os.path.join(log_dir, 'function_metrics.json')
        self.metrics = {
            'total_executions': 0,
            'successful_executions': 0,
            'failed_executions': 0,
            'execution_times': {}
        }
    
    def log_function_start(self, function_name):
        """Log the start of function execution"""
        self.logger.info(f"Starting execution of function: {function_name}")
        return time.time()
    
    def log_function_success(self, function_name, start_time):
        """Log successful function execution"""
        execution_time = time.time() - start_time
        self.logger.info(f"Function {function_name} executed successfully in {execution_time:.4f} seconds")
        
        self.metrics['total_executions'] += 1
        self.metrics['successful_executions'] += 1
        self.metrics['execution_times'][function_name] = execution_time
        
        self._save_metrics()
    
    def log_function_failure(self, function_name, start_time, error):
        """Log function execution failure"""
        execution_time = time.time() - start_time
        self.logger.error(f"Function {function_name} failed. Error: {error}")
        
        self.metrics['total_executions'] += 1
        self.metrics['failed_executions'] += 1
        
        self._save_metrics()
    
    def _save_metrics(self):
        """Save metrics to a JSON file"""
        try:
            with open(self.metrics_file, 'w') as f:
                json.dump(self.metrics, f, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to save metrics: {e}")


function_logger = FunctionExecutionLogger()