import json
from dotenv import load_dotenv
import os
load_dotenv()

# import the API wrapper, this is standard to any API
from apigeex_client.wrapper import wrapper

# Create a OpenAI API client from the wrapper
client = wrapper.get_client("hls_search")


if __name__ == "__main__":

    # Import data model and API endpoint for Healthcare Search
    from apigeex_client.clients.hls_search.models.search_request_type_0 import SearchRequestType0
    from apigeex_client.clients.hls_search.api.default \
        import post_v_1_alpha_projects_lpr_healthcare_locations_us_collections_default_collection_data_stores_lpr_healthcare_serving_configs_default_searchsearch \
        as search
    
    
    patient_id = os.getenv('DEMO_PATIENT_ID')

    query = "Last visit"
    
    request_body = SearchRequestType0.from_dict({
        "query": query,
        "pageSize": 100,
        "queryExpansionSpec": {
            "condition": "AUTO"
        },
        "spellCorrectionSpec": {
            "mode": "AUTO"
        },
        "contentSearchSpec": {
        "summarySpec": {
                "summaryResultCount": 1,
                "ignoreAdversarialQuery": True,
                "includeCitations": True
            },
            "snippetSpec": {
                "maxSnippetCount": 1,
                "returnSnippet": True
            }
        },
        "naturalLanguageQueryUnderstandingSpec": {
            "filterExtractionCondition": "ENABLED"
        },
        "filter": "patient_id: ANY(\"" + patient_id + "\")"
    })  
    

    response = search.sync_detailed(
        client=client,
        body=request_body  
    )

    if response.status_code == 200:
        results = json.loads(response.content)
        for r in results['results']:
            print(r)
            print("\n\n")
        print(results['summary']['summaryText'])
    else:
        print("ERROR:", response.status_code)
        print(response)