# LangGraph Project

A collection of LangGraph and LangChain prototypes demonstrating state graph workflows, tool-enabled chatbots, human-in-the-loop flows, conditionally routed graph execution, tracing, and memory checkpointing.

## What this project includes

- `simple_graph.py`: a simple state graph example for chained state transformation.
- `HITL.py`: a human-in-the-loop graph that uses tool calls, interruptions, and a resume flow.
- `chatbot.ipynb`: a notebook building a state graph chatbot with LangGraph and Ollama.
- `tool_call.ipynb`: a notebook demonstrating tool calls inside a LangGraph workflow.
- `tool_call-agent.ipynb`: a notebook showing an agent-style tool-enabled graph in LangGraph.
- `graph_with_condition.ipynb`: a notebook showing conditional graph execution paths.
- `langsmith_tracing.ipynb`: a notebook showing LangSmith tracing integration.
- `memory.ipynb`: a notebook demonstrating memory checkpointing and state persistence.
- `main.py`: a minimal sample entry point.

## Key technologies

- Python 3.11
- LangGraph
- LangChain
- Ollama (`langchain-ollama`)
- LangSmith tracing
- Google Generative AI support
- Jupyter notebooks for experiment-driven development

## Setup

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
python -m pip install -U pip
python -m pip install -r requirements.txt
```

> If `requirements.txt` is not present, use:
>
> ```bash
> python -m pip install google-generativeai ipykernel langchain langchain-google-genai langchain-ollama langgraph langsmith[claude-agent-sdk] notebook python-dotenv
> ```

3. Configure environment variables:

- Create a `.env` file in the project root.
- Add provider credentials and configuration values required by your model and tracing setup.

Example `.env` content:

```env
# Example values; update for your environment
OLLAMA_API_KEY=your_ollama_api_key
GOOGLE_API_KEY=your_google_api_key
LANGSMITH_API_KEY=your_langsmith_api_key
```

## Running the examples

### Python scripts

- Run the simple state graph example:

```bash
python simple_graph.py
```

- Run the human-in-the-loop example:

```bash
python HITL.py
```

### Jupyter notebooks

Launch Jupyter and open the notebooks in the project root:

```bash
jupyter notebook
```

Then open one of:

- `chatbot.ipynb`
- `tool_call.ipynb`
- `tool_call-agent.ipynb`
- `graph_with_condition.ipynb`
- `langsmith_tracing.ipynb`
- `memory.ipynb`

## Example workflows

- `simple_graph.py`: builds a `StateGraph` with basic node transitions and state transformations.
- `HITL.py`: defines tools, binds them to an Ollama chatbot, and demonstrates interrupt/resume behavior.
- Notebooks: explore interactive experiments with LangGraph, tools, conditional edges, tracing, and memory.

## Notes

- This repository is designed as an experimental playground for LangGraph-based AI workflows.
- Ensure your chosen model provider is available and configured correctly.
- The notebook examples assume a compatible Ollama model and may require API credentials or local Ollama server access.

## Project structure

- `.env`: environment variable file for secrets/configuration
- `main.py`: minimal example entry point
- `simple_graph.py`: state graph prototype
- `HITL.py`: human-in-the-loop workflow example
- `*.ipynb`: interactive notebooks for language model graph experiments

## License

No license is specified. Add a license file if you want to share or publish this project.
