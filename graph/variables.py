from dataclasses import dataclass
from utils import confirm_variables
# Give endpoint to get publishers
# Create config.py to import variables -- Ravin for example will "hardcode" known variables
# 1. get orgs - return id 
# ***HOW TO, not actually use***

@dataclass
class Campaign():
    pub_id: str
    name: str
    kind: str
    brand_id: str
    cost: int
    goal: int
    start_date: str
    end_date: str
    id: str=None 

def create_campaign_input(campaign: Campaign):
    """When creating input the keys and strings need quotes."""
    input = f""" {{
        "input" : {{
            "allowRetargeting" : "false",
            "organizationId" : "{campaign.pub_id}",
            "name" : "{campaign.name}",
            "kind" : "{campaign.kind}",
            "companyId" : "{campaign.brand_id}",
            "cost" : {campaign.cost},
            "goal" : {campaign.goal},
            "expectedStartAt" : "{campaign.start_date}",
            "expectedEndAt" : "{campaign.end_date}"
        }}
    }}
    """
    print(input)
    confirm_variables("\nIs the above data correct?")
    return input