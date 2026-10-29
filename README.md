
# EduBot – Education Chatbot

## Project Overview
EduBot is an interactive education chatbot developed using
Python and Ollama. It uses a locally running Llama 3.2
language model to answer educational questions.

## Objectives
- Build a command-line chatbot using a local LLM.
- Maintain conversation history.
- Save questions and responses with timestamps.
- Test the chatbot using different types of questions.

## Technologies Used
- Python
- Ollama
- Llama 3.2
- Pandas
- Jupyter Notebook
- CSV and text files

## Installation
1. Install Ollama from https://ollama.com/download/windows
2. Download the model using: ollama pull llama3.2
3. Create a Python virtual environment.
4. Install dependencies using:
   pip install -r requirements.txt

## Execution
Run the chatbot using:

python chatbot.py

Type exit to stop the chatbot.

## Dataset
sample_questions.csv contains 20 sample education questions.

## Output Files
- chat_history.csv
- responses.csv
- chatbot_logs.txt

## Limitations
- Responses depend on the selected language model.
- Some answers may be incorrect or incomplete.
- Model performance depends on available computer resources.
- Conversation history is maintained during the current run.

## Future Enhancement
The chatbot can be integrated with LangChain to provide
more structured conversation management.
