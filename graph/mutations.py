import json

import requests

from config import URL, HEADERS


class Mutation:
    @staticmethod
    def create_campaign(variables):
        data_request = """
            createCampaign($input: CreateCampaignInput!) {
                authed{
                    success
                }
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

    @staticmethod
    def create_dynamic_line_item(variables):
        data_request = """
            createCampaignDynamic($input: CreateCampaignDynamicInput!) {
                authed{
                    success
                }
                createCampaignDynamic(input: $input){
                    campaignDynamic {
                    campaign{
                        id
                    }
                    name
                    duration
                    cost
                    goal
                    expectedEndAt
                    expectedStartAt
                    }
                }
            }
        """
        return Mutation.mutation(data_request, variables)

    @staticmethod
    def create_streaming_line_item(variables):
        data_request = """
            createCampaignStreaming($input: CreateCampaignStreamingInput!) {
                authed{
                    success
                }
                createCampaignStreaming(input: $input){
                    campaignStreaming {
                    campaign{
                        id
                    }
                    name
                    duration
                    cost
                    goal
                    }
                }
            }
        """
        return Mutation.mutation(data_request, variables)

    @staticmethod
    def mutation(data_request, variables):
        query = f"""
            mutation {data_request}
        """
        return Mutation.execute(query, variables)

    @staticmethod
    def execute(query, variables=None):
        """Execute a mutation call to the API"""
        print("Executing Mutation...\n\n")
        print(f"{query}\n\n")
        response = requests.post(
            URL, headers=HEADERS, json={"query": query, "variables": variables}
        )
        print(json.loads(response.text))

        return json.loads(response.text)
