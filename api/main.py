import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_engine.vector_store import FunctionVectorStore
from automation_functions.system_functions import SystemFunctions
from utils.code_generator import DynamicCodeGenerator
from utils.logger import function_logger
import traceback

class ExecutionRequest(BaseModel):
    prompt: str

app = FastAPI(title="Automation Function Execution API")

function_store = FunctionVectorStore()
function_store.add_function('open_chrome', 'Open Google Chrome browser')
function_store.add_function('open_calculator', 'Open system calculator')
function_store.add_function('get_system_resources', 'Retrieve current CPU and RAM usage')
function_store.add_function('run_shell_command', 'Execute a shell command')

@app.post("/execute")
async def execute_function(request: ExecutionRequest):
    start_time = function_logger.log_function_start(request.prompt)

    try:

        retrieved_functions = function_store.retrieve_function(request.prompt)
        
        if not retrieved_functions:
            raise HTTPException(status_code=404, detail="No matching function found")
        
        best_match = retrieved_functions[0]
        function_name = best_match['name']
        
        generated_code = DynamicCodeGenerator.generate_function_code(
            function_name, 
            SystemFunctions
        )
        
        if generated_code.startswith("Error generating code:"):
            raise ValueError(generated_code)
        

        function_logger.log_function_success(function_name, start_time)
        
        return {
            "function": function_name,
            "description": best_match['description'],
            "code": generated_code
        }
    
    except Exception as e:
        function_logger.log_function_failure(request.prompt, start_time, str(e))

        print(traceback.format_exc())     

        raise HTTPException(
            status_code=500, 
            detail=f"Error executing function: {str(e)}"
        )
    
@app.get("/metrics")
async def get_execution_metrics():
    """
    Endpoint to retrieve execution metrics
    """
    try:
        with open('logs/function_metrics.json', 'r') as f:
            metrics = json.load(f)
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving metrics: {e}")
