# Apigee X Client

## Why

The Mayo API Proxy **Apigee X** provides an universal interface and authentication to many different APIs that connect to variety of services and data sources. Those services and data sources may have their own APIs, which often require different mechanisms for authentication and data access. 

Apigee X abstracts away those differences, therefore Apigee X's users could use one single authentication to access all services. In addition, the users do not need to worry about any changes or upgrade in the underlying APIs, Apigee X Team is constantly taking care of that for us.

This **apigeex_client** package allows you to use those APIs without explicitly include any endpoint URL in the code. Each of the endpoints (in the suppored APIs) is represented by a Python function whose input arguments are the parameters required by the endpoint. All you need to do is to determine the correct function to use.

## Supported APIs in this package
- llm-azure-openai
- healthcare search
- clinical trials search (non-prod only)

## Requirement

You need to provide CLIENT_ID and CLIENT_SECRET in an ```.env``` file as follow.

```
PRODUCTION=true # Set to false if you're using Non-prod Apigee X

NON_PROD_APIGEE_X_KEY=<NON_PROD_CLIENT_ID>
NON_PROD_APIGEE_X_SECRET=<NON_PROD_CLIENT_SECRET>

PROD_APIGEE_X_KEY=<PROD_CLIENT_ID>
PROD_APIGEE_X_SECRET=<PROD_CLIENT_SECRET>
```


## Installation

- In your Python environment, run

```
pip install git+ssh://git@github.com/riaz-ai-lab/apigeex_client.git
```


## Run an example

Use the OpenAI chat/completions:

```python
import json
from dotenv import load_dotenv
load_dotenv()

# import the API wrapper, this is standard to any API
from apigeex_client.wrapper import wrapper

# import relevant functions from OpenAI API
from apigeex_client.clients.llm_azure_openai.api.default import chat_completions_create
from apigeex_client.clients.llm_azure_openai.models.create_chat_completion_request import CreateChatCompletionRequest
from apigeex_client.clients.llm_azure_openai.models.chat_completion_request_message import ChatCompletionRequestMessage
from apigeex_client.clients.llm_azure_openai.models.chat_completion_request_message_role import ChatCompletionRequestMessageRole


# Create a OpenAI API client from the wrapper
client = wrapper.get_client("llm_azure_openai")
API_VERSION = '2024-10-21'


# Helper function to quickly query the LLM and get the answer.
def query_llm(user_prompt: str, system_prompt: str, engine: str = 'gpt-4'):

    system_prompt = ChatCompletionRequestMessage( role=ChatCompletionRequestMessageRole.SYSTEM, content=system_prompt )
    message = ChatCompletionRequestMessage( role=ChatCompletionRequestMessageRole.USER, content=user_prompt )   
    completion_request_body = CreateChatCompletionRequest( messages=[ system_prompt, message ] ) 

    response = chat_completions_create.sync_detailed(
        deployment_id=engine,
        client=client,
        body=completion_request_body,
        api_version=API_VERSION,
    )

    if response.status_code == 200:
        data_dict = response.parsed.to_dict()
        return data_dict['choices'][0]['message']['content']
    else:
        print("ERROR:", response.status_code)
        print(response)
        return None



if __name__ == "__main__":

    context = "You are an AI assistant that helps doctors find medical information."
    prompt = "What are the prescription guidelines for Methotrexate?" 

    reply = query_llm(prompt, context, engine='gpt-4')

    print(reply)
```

## Feedback

Please direct any feedback to Phu Tran at tran.phu@mayo.edu. Thank you!