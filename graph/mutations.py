import json
import requests
from config import url, headers

class Mutation():

    def create_campaign(variables):
        data_request = """
            createCampaign($input: CreateCampaignInput!) {
                createCampaign(input:$input){
                    campaign {
                        id
                        name
                        organization {
                            id
                        }
                        kind
                        advertiser {
                            id
                        }
                        cost
                        goal
                        expectedStartAt
                        expectedEndAt
                    }
                }
            }
        """
        return Mutation.mutation(data_request, variables)

    def mutation(data_request, variables):
        query = f"""
            mutation {data_request}
        """
        return Mutation.execute(query, variables)

    def execute(query, variables=None):
        """Execute a mutation call to the API"""
        print('Executing Mutation...\n\n')
        print(f"{query}\n\n")
        response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
        print(json.loads(response.text))

        return json.loads(response.text)