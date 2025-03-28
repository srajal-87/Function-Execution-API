# LLM + RAG-Based Function Execution API 

## Prerequisites
- Python 3.8+ 
- pip (Python package manager)
- Virtual environment (recommended)

## Step-by-Step Setup

### 1. Clone the Project
```bash
git clone https://github.com/srajal-87/Function-Execution-API.git
cd function-execution-api
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```


### 4. Run the API
```bash
# Run with Uvicorn
uvicorn api.main:app --reload
```

### 5. Testing the API
You can test the API using:

#### Option 1: Swagger UI
- Open a web browser
- Navigate to `http://127.0.0.1:8000/docs`
- Use the interactive Swagger UI to test endpoints

#### Option 2: cURL
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/execute' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Open Chrome"
}'
```

#### Option 3: Python Requests
```python
import requests

url = "http://127.0.0.1:8000/execute"
payload = {"prompt": "Open Chrome"}
response = requests.post(url, json=payload)
print(response.json())
```

## Supported Queries
- "Open Chrome"
- "Open Calculator"
- "Get System Resources"
- "Run Shell Command"


