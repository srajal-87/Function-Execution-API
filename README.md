# 🤖 LLM + RAG-Based Function Execution API

## 📌 Project Overview

A FastAPI-powered application that executes system functions through natural language commands using Retrieval-Augmented Generation (RAG).

This API interprets everyday language instructions (like "open Chrome" or "check CPU usage") and dynamically retrieves and executes the corresponding system functions. Perfect for automating routine desktop tasks or building voice-controlled system tools without complex command syntax.

## 🚀 Features

- ✅ Natural language processing for system function execution
- 🔍 RAG-based approach for intelligent function matching
- 📊 Function execution metrics and logging
- 🔐 Error handling and exception management
- 🌐 RESTful API with Swagger documentation
- 🧩 Modular design for easy extension with new functions

## 🛠️ Tech Stack

- **Python 3.8+** - Core programming language
- **FastAPI** - Modern, high-performance web framework
- **Pydantic** - Data validation and settings management
- **RAG (Retrieval-Augmented Generation)** - For function mapping
- **Vector Store** - Function indexing and retrieval
- **Dynamic Code Generation** - Runtime function execution
- **Uvicorn** - ASGI server for running the API

## 📁 Project Structure

```
function-execution-api/
├── api/
│   └── main.py                    # FastAPI application entry point
├── rag_engine/
│   └── vector_store.py            # Function storage and retrieval
├── automation_functions/
│   └── system_functions.py        # System function implementations
├── utils/
│   ├── code_generator.py          # Dynamic code generation utilities
│   └── logger.py                  # Execution logging functionality
├── logs/
│   └── function_metrics.json      # Execution metrics storage
├── requirements.txt               # Project dependencies
└── README.md                      # Project documentation
```

## 🧠 How It Works

1. **User Input**: Send a natural language command to the API (e.g., "Open Chrome browser")
2. **Function Retrieval**: The RAG engine matches the command to available functions in the vector store
3. **Code Generation**: The system dynamically generates executable code for the matched function
4. **Execution**: The function is executed and results are returned
5. **Logging**: All executions are logged with metrics for performance analysis

```
┌──────────┐      ┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│  User    │──────▶ RAG Vector  │──────▶  Dynamic Code │──────▶ System      │
│  Query   │      │   Store     │      │  Generation   │      │ Execution   │
└──────────┘      └─────────────┘      └──────────────┘      └─────────────┘
                                                                    │
┌──────────┐      ┌─────────────┐                                   │
│  API     │◀─────┤  Execution  │◀──────────────────────────────────┘
│ Response │      │   Metrics   │
└──────────┘      └─────────────┘
```

## 🧪 Setup & Installation

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/function-execution-api.git
cd function-execution-api
```

2. **Create and activate virtual environment**
```bash
# Create virtual environment
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the API**
```bash
uvicorn api.main:app --reload
```

5. **Access the API**
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

### Example Usage

**Using cURL:**
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/execute' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Open Chrome"
}'
```

**Using Python requests:**
```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/execute",
    json={"prompt": "Open Chrome"}
)
print(response.json())
```

## 📊 Supported Functions

Current system functions include:
- Opening Google Chrome browser
- Opening system calculator
- Retrieving system resources (CPU/RAM usage)
- Running shell commands

To view execution metrics:
```bash
curl http://127.0.0.1:8000/metrics
```

## 🧑‍💻 Contributing

Contributions are welcome! Here's how you can contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


