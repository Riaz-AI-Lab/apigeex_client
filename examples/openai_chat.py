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