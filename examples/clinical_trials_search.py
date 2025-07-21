import os
import json
from dotenv import load_dotenv
load_dotenv()

from apigeex_client.wrapper import APIWrapper

key = os.getenv('APIGEEx_KEY')
secret = os.getenv('APIGEEx_SECRET')

wrapper = APIWrapper(
    auth_url="https://dev.mcc.apix.mayo.edu/oauth/token",
    client_id=os.getenv('APIGEEx_KEY'),
    client_secret=os.getenv('APIGEEx_SECRET'),
    api_list_path="api_list.yaml",
    clients_package="clients"
)

wrapper.authenticate()

client = wrapper.get_client("clinical_trials")

if __name__ == "__main__":

    # from clients.clinical_trials.api.v_1_search import first_study_v_1_first_get
    # response = first_study_v_1_first_get.sync_detailed(client=client)

    from apigeex_client.clients.clinical_trials.api.v_1_search import study_by_nct_number_v_1_nct_number_nct_number_get    
    response = study_by_nct_number_v_1_nct_number_nct_number_get.sync_detailed(
        nct_number='NCT05514054', 
        client=client
    )

    if response.status_code == 200:
        data_dict = response.parsed.to_dict()
        json_str = json.dumps(data_dict, indent=2)
        print(json_str)
    else:
        print("ERROR:", response.status_code)
        print(response.content)