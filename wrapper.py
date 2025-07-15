import yaml
import importlib
from pathlib import Path
from typing import Dict, Any
import httpx


class APIWrapper:
    def __init__(self, auth_url: str, client_id: str, client_secret: str, api_list_path: str, clients_package: str = "clients"):
        self.auth_url = auth_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.api_list_path = Path(api_list_path)
        self.clients_package = clients_package  # e.g., "clients"
        self.token = None
        self.clients: Dict[str, Any] = {}

    def authenticate(self):
        # Replace this with your actual auth request to get bearer token
        import requests
        data = f'grant_type=client_credentials&client_id={self.client_id}&client_secret={self.client_secret}'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }        
        resp = requests.post(self.auth_url, headers=headers, data=data)
        resp.raise_for_status()
        self.token = resp.json().get("access_token")

        # After token obtained, initialize clients
        self._init_clients()

    def _init_clients(self):
        with open(self.api_list_path, "r") as f:
            api_list = yaml.safe_load(f)

        for api in api_list:
            name = api["name"]
            base_url = api["base_url"]

            # Dynamically import the generated client package
            # e.g., clients.ai_factory_product_build_azure_openai
            module_path = f"{self.clients_package}.{name}"

            try:
                client_module = importlib.import_module(module_path)
            except ModuleNotFoundError as e:
                raise RuntimeError(f"Generated client module '{module_path}' not found. Did you generate it?") from e

            # Create the Client instance
            client = client_module.Client(base_url=base_url)

            # Create the Client instance with custom headers
            # Pass the Authorization header directly to the client's HTTP transport
            headers = {"Authorization": f"Bearer {self.token}"}
            # Initialize the client with custom httpx.Client to include headers
            client = client_module.Client(
                base_url=base_url,
                headers=headers
            )

            # # Patch the client's internal _request_options to include bearer token header
            # # This is a private detail of openapi-python-client but works in practice
            # def add_auth_headers(request_options):
            #     headers = request_options.get("headers", {})
            #     headers["Authorization"] = f"Bearer {self.token}"
            #     request_options["headers"] = headers
            #     return request_options

            # # Wrap or patch client's _request_options method to inject headers
            # original_request_options = client._request_options

            # def patched_request_options(*args, **kwargs):
            #     ro = original_request_options(*args, **kwargs)
            #     return add_auth_headers(ro)

            # client._request_options = patched_request_options

            self.clients[name] = client
            

    def get_client(self, name: str):
        client = self.clients.get(name)
        if not client:
            raise ValueError(f"Client '{name}' is not initialized or does not exist.")
        return client