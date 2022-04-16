from dataclasses import dataclass
from utils import confirm_variables
# Give endpoint to get publishers
# Create config.py to import variables -- Ravin for example will "hardcode" known variables
# 1. get orgs - return id 
# ***HOW TO, not actually use***

@dataclass
class Campaign():
    pub_id: str=None
    name: str=None
    kind: str=None 
    brand_id: str=None 
    cost: int=None 
    goal: int=None 
    start_date: str=None 
    end_date: str=None 
    id: str=None 
    duration: int=None
    line_item_name: str=None

def create_campaign_input(campaign: Campaign):
    """When creating input the keys and strings need quotes."""
    input = f""" {{
        "input" : {{
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

def create_tracking_urls_input(campaign: Campaign):
    """When creating input the keys and strings need quotes."""
    input = f""" {{
        "organizationId" : "{campaign.pub_id}",
        "campaignId" : "{campaign.id}"
    }}
    """
    print(input)
    confirm_variables("\nIs the above data correct?")
    return input

def create_dynamic_input(campaign: Campaign):
    """Input for creating dynamic line items"""
    input = f""" {{
        "input" : {{
            "campaignId" : "{campaign.id}",
            "name" : "{campaign.line_item_name}",
            "cost" : {campaign.cost},
            "goal" : {campaign.goal},
            "expectedStartAt" : "{campaign.start_date}",
            "expectedEndAt" : "{campaign.end_date}",
            "duration" : {campaign.duration}
        }}
    }}
    """
    print(input)
    confirm_variables("\nIs the above data correct?")
    return input


def create_streaming_input(campaign: Campaign):
    """Input for creating streaming line items"""
    input = f""" {{
        "input" : {{
            "campaignId" : "{campaign.id}",
            "name" : "{campaign.line_item_name}",
            "cost" : {campaign.cost},
            "goal" : {campaign.goal},
            "duration" : {campaign.duration}
        }}
    }}
    """
    print(input)
    confirm_variables("\nIs the above data correct?")
    return input
