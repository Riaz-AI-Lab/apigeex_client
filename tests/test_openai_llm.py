import os
import json
from dotenv import load_dotenv
load_dotenv()

from wrapper import APIWrapper

key = os.getenv('APIGEE_X_KEY')
secret = os.getenv('APIGEE_X_SECRET')

wrapper = APIWrapper(
    auth_url="https://dev.mcc.apix.mayo.edu/oauth/token",
    client_id=os.getenv('APIGEE_X_KEY'),
    client_secret=os.getenv('APIGEE_X_SECRET'),
    api_list_path="api_list.yaml",
    clients_package="clients"
)

wrapper.authenticate()

client = wrapper.get_client("llm_azure_openai")

if __name__ == "__main__":

    from clients.llm_azure_openai.api.default import chat_completions_create

    response = chat_completions_create.sync_detailed(
        client=client,
        deployment_id="gpt-4",
        api_version='2024'
    )

    if response.status_code == 200:
        data_dict = response.parsed.to_dict()
        json_str = json.dumps(data_dict, indent=2)
        print(json_str)
    else:
        print("ERROR:", response.status_code)
        print(response.content)