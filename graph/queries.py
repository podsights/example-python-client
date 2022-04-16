import json
import requests
from config import url, headers

class Query():

    def get_orgs():
        data_request = """
            me {
                organizations {
                    name
                    id
                }
            }
        """
        return Query.query(data_request)

    def get_brands(search_brand):
        print(search_brand)
        data_request = f"""
            me {{
                companySearch(query: "{search_brand}") {{
                    name
                    id
                }}
            }}
        """
        return Query.query(data_request)

    def get_tracking_urls(variables):
        data_request = """
            query CampaignTrackingUrlsQuery($organizationId: ID!, $campaignId: ID!) {
                me {
                    id
                    organization(id: $organizationId) {
                        id
                        campaign(id: $campaignId) {
                            id
                            campaignStreamings {
                                id
                                name
                            }
                            campaignDynamics {
                                id
                                name
                                spotifyTrackingUrl
                            }
                        }
                    }
                }
            }
        """
        return Query.execute(data_request, variables)

    def query(data_request, variables=None):
        query = f"""
            query {{
                {data_request}
            }}
        """
        return Query.execute(query, variables)

    def execute(query, variables=None):
        """Execute a query call to the API"""
        print('\nExecuting Query\n\n')
        print(query)
        response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
        print(json.loads(response.text))

        return json.loads(response.text)

