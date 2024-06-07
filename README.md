# Agents Lab 

## Pre-requisites 

If running this lab locally, you will require: 
- Python version 3.10 or later installed. 


## Running locally

If you have Poetry installed locally. 

```shell script
pyenv install  3.10.14
brew install pipx
pipx install poetry
```

Install dependencies to set up your enivronment: 

```shell script
poetry install

```

Run: 

`poetry run jupyter lab`


## Dependencies 

You will require access to the 


## Set configuration 

To successfully make a call against the Azure OpenAI service, you'll need the following: 

https://learn.microsoft.com/en-us/azure/ai-services/openai/quickstart?tabs=command-line%2Cpython-new&pivots=programming-language-python

Create a file `.env` in project root with this information: 
```bash 

```

The Azure OpenAI API Versioning is described here. https://learn.microsoft.com/en-us/azure/ai-services/openai/api-version-deprecation
Note that some functionality is only available on more recent versions. 


## Running with VS Code 

When you run commands using `poetry run`, environment variables are automatically loaded.

So, instead of running `jupyter lab` you run `poetry run jupyter lab` 



## References: 

Jupyter Lab 

https://github.com/jupyterlab/jupyterlab 


## Running in the cloud. Options: 

1. Running Jupyter locally from my laptop. But does that give you multiople access ? 

Azure Lab Services 
https://learn.microsoft.com/en-us/azure/lab-services/quick-create-resources
https://learn.microsoft.com/en-us/azure/lab-services/class-type-jupyter-notebook
https://visualstudio.microsoft.com/vs/features/notebooks-at-microsoft/

2. Open the Repo with Binder 

https://mybinder.org/


3. ALso Python Anywhere or the Littlest Jupyter Hub 

https://the-littlest-jupyterhub.readthedocs.io/en/latest/index.html

https://www.reddit.com/r/Python/comments/9107qu/best_way_to_share_a_jupyter_notebook_during_a/


4. Other commercial services 

https://www.jetbrains.com/datalore/
https://deepnote.com/