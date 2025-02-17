# Llama LLM-powered Account Balance Simulator

![image](https://github.com/user-attachments/assets/aa2195fd-1728-46ff-a77c-4936e34ead3d)

A project utilizing Llama LLM to simulate user operations on their account balance. The LLM agent interprets user inputs and calls predefined code functions to perform operations like deposits, withdrawals, and balance checks through an API.

[Colab Notebook](https://colab.research.google.com/drive/1ggufeUZwEGzxhjO2y4CHznCf9ow8NmA5?usp=sharing)

## Installation

To install the project, you need to have python and pip installed. Then, you can run the following command:

- create and activate a env (for mac and linux users)

```bash
python3 -m venv ai-agent
```

- activate the env

```bash
source ai-agent/bin/activate
```

```bash
pip install -r requirements.txt
```

### Install ollama

go to https://ollama.com/download and folow the instructions

## Usage

Pull the model

```bash
ollama pull lama3.2:1b
```

run

```bash
python main.py
```

And start prompting
