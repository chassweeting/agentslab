import os
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_API_KEY"],
    api_version=os.environ["AZURE_OPENAI_ENDPOINT"],
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
    )

deployment_name = os.getenv["AZURE_OPENAI_DEPLOYMENT"]

