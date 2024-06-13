# Langchain Agent for Guardrails lab 

A simple implementation of a Langchain Tools Agent using Azure OpenAI. 

## Dependencies 

1. Azure OpenAI Resource.  

2. Restaurant APIs which the agent will make calls to.  Options for running this:
   - Clone https://github.com/chassweeting/agentslab-apis , install and run locally as per the README
   - Clone https://github.com/chassweeting/agentslab-apis , build and run with Docker as per the README
   
3. Python (versions 3.10 to 3.12.3), and Poetry.
   - Use pyenv for different Python versions: https://github.com/pyenv/pyenv
   - Pipx is recommended for installing Poetry: https://pipx.pypa.io/stable/installation/ 
   - Installing and using Poetry: https://python-poetry.org/docs/
   
   <br>

## Configuration 

If running the Restaurant APIs locally, then all you need provide is the Azure OpenAI resource configuration. 

Create Please create a `.env` file, and provide your own values for the following environment variables: 
 
```bash
AZURE_OPENAI_API_KEY=*****************************
AZURE_OPENAI_DEPLOYMENT=gpt-4-32k
AZURE_OPENAI_API_VERSION=2024-05-01-preview
AZURE_OPENAI_ENDPOINT=https://******.openai.azure.com/
```

<br>

## Running 

Install the Python dependencies. Note that this will also create a virtualenv in `.venv` within the same directory. 

```bash 
poetry install
```

Running the FastAPI application locally: 

```bash 
make serve 
```


## Running Docker 

You can also build and run a Docker image using: 

```bash 
make build

# Run using the local .env file with your configuration variables 
make run 

# To kill/clean-up running containers
make docker-clean
```
<br>


## Further reading 

See the [docs](/docs) for ideas how to use the APIs and create Guardrails. 

<br>


## References: 

- The Azure OpenAI API Versioning:  https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation.  Note that some functionality is only available on more recent versions.
- Note that we use 3.12.3 due to this Pydantic bug afflicting Python 3.12.4 and up. https://github.com/pydantic/pydantic/issues/9609
