import json

from dotenv import load_dotenv
load_dotenv()


if __name__ == "__main__":

    # import the API wrapper, this is standard to any API
    from apigeex_client.wrapper import wrapper
    
    # import relevant functions from OpenAI API
    from apigeex_client.clients.llm_azure_openai.api.default import chat_completions_create
    from apigeex_client.clients.llm_azure_openai.models.create_chat_completion_request import CreateChatCompletionRequest
    from apigeex_client.clients.llm_azure_openai.models.chat_completion_request_message import ChatCompletionRequestMessage
    from apigeex_client.clients.llm_azure_openai.models.chat_completion_request_message_role import ChatCompletionRequestMessageRole

    # Create a OpenAI API client from the wrapper
    client = wrapper.get_client("llm_azure_openai")

    # Create system and user prompt objects
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