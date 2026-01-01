# AI Employee Interview Helper
An AI-powered logic engine designed to help students/employees by generating interview questions and analyzing responses by providing interview pdf documents. This project uses the **OpenRouter API** to access a variety of LLMs (like GPT-4, Qwen, or Llama) through a single interface.

## 🛠️ Setup & Installation

### 1. Configure the Environment
Ensure you have a `.env` file in the root directory with the following variables:
```text
OPENROUTER_API_KEY=your_openrouter_key_here 
```
### 2. Setup Virtual Environment

```# Create the environment
python -m venv env

# Activate it (Windows)
env\Scripts\activate

# Activate it (Mac/Linux)
source ./env/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt 
```

### 4. Run 

```
python3 test_brain.py
```