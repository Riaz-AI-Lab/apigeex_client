import os
import json
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('APIGEEx_KEY')
secret = os.getenv('APIGEEx_SECRET')

from apigeex_client.wrapper import APIWrapper
wrapper = APIWrapper(
    auth_url="https://dev.mcc.apix.mayo.edu/oauth/token",
    client_id=os.getenv('APIGEEx_KEY'),
    client_secret=os.getenv('APIGEEx_SECRET'),
    api_list_path="api_list.yaml",
    clients_package="clients"
)

wrapper.authenticate()


if __name__ == "__main__":

    client = wrapper.get_client("lpr")

    print(client._headers)

    from apigeex_client.clients.lpr.api.patient import patient_read, patient_search 

    # response = patient_read.sync_detailed(id="82400e81-04d6-4a42-93a6-0530b356f182", client=client)
    response = patient_search.sync_detailed(        
        active=True,
        client=client
    )

    if response.status_code == 200:
        data_dict = response.parsed.to_dict()
        json_str = json.dumps(data_dict, indent=2)
        print(json_str)
    else:
        print("ERROR:", response.status_code)
        print(response)


