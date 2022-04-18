import json

import requests

from config import HEADERS, URL


class Query:
    @staticmethod
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

    @staticmethod
    def get_brands(search_brand):
        data_request = f"""
            me {{
                companySearch(query: "{search_brand}") {{
                    name
                    id
                }}
            }}
        """
        return Query.query(data_request)

    @staticmethod
    def get_payers(organization_id, company_id):
        data_request = f"""
            me {{
                organization(id: "{organization_id}") {{
                    payerOrganizations(companyId: "{company_id}"){{
                        id
                        name
                    }}
                }}
            }}
        """
        return Query.query(data_request)

    @staticmethod
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

    @staticmethod
    def query(data_request, variables=None):
        query = f"""
            query {{
                {data_request}
            }}
        """
        return Query.execute(query, variables)

    @staticmethod
    def execute(query, variables=None):
        """Execute a query call to the API"""
        print("\nExecuting Query")
        print(query)
        response = requests.post(
            URL, headers=HEADERS, json={"query": query, "variables": variables}
        )

        print(f"\nResponse\n{json.loads(response.text)}\n\n")

        return json.loads(response.text)
