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

    """
    Example coming soon.
    """
    
    pass

