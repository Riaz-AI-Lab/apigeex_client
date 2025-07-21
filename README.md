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

- Copy the file `api_list.yaml` to your project

## Run an example

Use the OpenAI chat/completions:

```
import os
import json
from dotenv import load_dotenv
load_dotenv()
from apigeex_client.wrapper import APIWrapper


if __name__ == "__main__":

    # Declare the environment
    production = True
    
    # Create an API client for OpenAI Chat Completions
    if production:
        # Production environment
        wrapper = APIWrapper(
            auth_url="https://mcc.apix.mayo.edu/oauth/token",
            client_id=os.getenv('PROD_APIGEE_X_KEY'),
            client_secret=os.getenv('PROD_APIGEE_X_SECRET'),
            api_list_path="api_list.yaml",  # provide the path to api_list.yaml
            clients_package="clients",
            production=production
        ).authenticate()        
    else:
        # Non-Production environment
        wrapper = APIWrapper(
            auth_url="https://dev.mcc.apix.mayo.edu/oauth/token",
            client_id=os.getenv('NON_PROD_APIGEE_X_KEY'),
            client_secret=os.getenv('NON_PROD_APIGEE_X_SECRET'),
            api_list_path="api_list.yaml", # provide the path to api_list.yaml
            clients_package="clients",
            production=production
        ).authenticate()        

    client = wrapper.get_client("llm_azure_openai")
    
    # Import function from the Apigee X OpenAI APIs
    from apigeex_client.clients.llm_azure_openai.api.default import chat_completions_create
    from apigeex_client.clients.llm_azure_openai.models.create_chat_completion_request import CreateChatCompletionRequest
    from apigeex_client.clients.llm_azure_openai.models.chat_completion_request_message import ChatCompletionRequestMessage
    from apigeex_client.clients.llm_azure_openai.models.chat_completion_request_message_role import ChatCompletionRequestMessageRole

    context = "You are an AI assistant that helps doctors find medical information."
    prompt = "What are the prescription guidelines for Methotrexate?"
   
    system_prompt = ChatCompletionRequestMessage( role=ChatCompletionRequestMessageRole.SYSTEM, content=context )
    message = ChatCompletionRequestMessage( role=ChatCompletionRequestMessageRole.USER, content=prompt )    
    
    response = chat_completions_create.sync_detailed(
        deployment_id="gpt-4o",
        client=client,
        body=CreateChatCompletionRequest( messages=[ system_prompt, message ] ),
        api_version='2024-10-21',
    )

    if response.status_code == 200:
        data_dict = response.parsed.to_dict()
        json_str = json.dumps(data_dict, indent=2)
        print(json_str)
    else:
        print("ERROR:", response.status_code)
        print(response)
```

## Feedback

Please direct any feedback to Phu Tran at tran.phu@mayo.edu. Thank you!