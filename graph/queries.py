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

    def query(data_request):
        # pass variables around here somehwere
        query = f"""
            query {{
                {data_request}
            }}
        """
        return Query.execute(query)

    def execute(query, variables=None):
        """Execute a query call to the API"""
        print('\nExecuting Query\n\n')
        response = requests.post(url, headers=headers, json={"query": query, "variables": variables})
        # print(json.loads(response.text))

        return json.loads(response.text)

