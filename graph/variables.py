from dataclasses import dataclass


@dataclass
class Campaign:
    pub_id: str
    name: str
    kind: str
    brand_id: str
    cost: int
    goal: int
    start_date: str
    end_date: str
    id: str = None


@dataclass
class DynamicLineItem:
    campaign_id: str
    name: str
    goal: int
    cost: int
    duration: int
    start_date: str
    end_date: str
    id: str = None

@dataclass
class StreamingLineItem:
    campaign_id: str
    name: str
    goal: int
    cost: int
    duration: int
    id: str = None


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
    confirm_variables(input)
    return input


def create_dynamic_input(line_item: DynamicLineItem):
    """Input for creating dynamic line items"""
    input = f""" {{
        "input" : {{
            "campaignId" : "{line_item.campaign_id}",
            "name" : "{line_item.name}",
            "cost" : {line_item.cost},
            "goal" : {line_item.goal},
            "expectedStartAt" : "{line_item.start_date}",
            "expectedEndAt" : "{line_item.end_date}",
            "duration" : {line_item.duration}
        }}
    }}
    """
    confirm_variables(input)
    return input

def create_streaming_input(line_item: StreamingLineItem):
    """Input for creating streaming line items"""
    input = f""" {{
        "input" : {{
            "campaignId" : "{line_item.campaign_id}",
            "name" : "{line_item.name}",
            "cost" : {line_item.cost},
            "goal" : {line_item.goal},
            "duration" : {line_item.duration}
        }}
    }}
    """
    confirm_variables(input)
    return input


def create_tracking_urls_input(pub_id: str, campaign_id: str):
    """When creating input the keys and strings need quotes."""
    input = f""" {{
        "organizationId" : "{pub_id}",
        "campaignId" : "{campaign_id}"
    }}
    """
    confirm_variables(input)
    return input

def create_delete_campaign_input(campaign_id: str):
    """When creating input the keys and strings need quotes."""
    input = f""" {{
        "input" : {{
            "id" : "{campaign_id}"
        }}
    }}
    """
    confirm_variables(input)
    return input


def confirm_variables(data: str):
    print(f"\n{data}")
    selection = str(input(f"\nIs the above data correct? y/n "))
    if selection not in ("y", "n"):
        print("\n\nPlease enter a valid option!")
        return confirm_variables(data)

    if selection == "y":
        return

    if selection == "n":
        print("\n\nIncorrect data...Exiting\n\n")
        exit()
