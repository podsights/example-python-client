from dataclasses import dataclass
from config import PUBLISHER_ID, DATE_FORMAT
import arrow

from graph.mutations import Mutation
from graph.queries import Query

from graph.variables import Campaign, DynamicLineItem, StreamingLineItem, create_campaign_input, create_dynamic_input, create_streaming_input, \
    create_tracking_urls_input


@dataclass
class Option:
    id: str
    name: str


START_OPTIONS = [
    Option("campaign", "Create a campaign"),
    Option("dynamic", "Create a dynamic"),
    Option("streaming", "Create a streaming"),
    Option("urls", "Retrieve tracking urls"),
]

CAMPAIGN_KIND_OPTIONS = [
    Option("attribution", "Attribution"),
    Option("marketing", "Marketing"),
    Option("reporting", "Reporting"),
]


def ask(question):
    return input(f"\n\n{question} ")


def selector(question, options):
    selections = "\n".join([f"{i}: {option.name}" for i, option in enumerate(options)])
    try:
        selection = int(input(f"{question}\n\n{selections}\n\n"))
    except ValueError:
        print("\n\nPlease enter a valid integer!")
        return selector(question, options)

    if 0 <= selection < len(options):
        option = options[selection]
        return option.id

    print("Please select a valid option number!")
    return selector(question, options)


def start():
    q = "What would you like to do?"
    return selector(q, START_OPTIONS)


def run_create_campaign():
    # GATHER VARIABLES
    print("Executing Create Campaign Helper.")
    print("We will retrieve your organizations and then ask you some questions to gather data.")

    orgs = [Option(**o) for o in Query.get_orgs()["data"]["me"]["organizations"]]
    question = "Which org would you like to use?"
    pub_id = PUBLISHER_ID if PUBLISHER_ID else selector(question, orgs)

    search_brand = str(ask("Enter the brand that is advertising in this campaign."))
    brands = [Option(**b) for b in Query.get_brands(search_brand)["data"]["me"]["companySearch"]]
    brand_id = selector("Which brand would you like to use?", brands)

    campaign_name = str(ask("Name of your campaign?"))

    kind = selector("Type of Campaign?", CAMPAIGN_KIND_OPTIONS)
    cost = int(ask("Cost of the campaign?"))
    goal = int(ask("Impression Goal of campaign?"))

    start_date = str(arrow.get(str(ask(f"Start of your campaign {DATE_FORMAT}?")), DATE_FORMAT))
    end_date = str(arrow.get(str(ask(f"End of your campaign {DATE_FORMAT}?")), DATE_FORMAT))

    # CREATE CAMPAIGN
    campaign = Campaign(pub_id, campaign_name, kind, brand_id, cost, goal, start_date, end_date)
    campaign_input = create_campaign_input(campaign)
    Mutation.create_campaign(campaign_input)


def run_create_line_item(kind: str = "dynamic"):
    print("Executing Create Line Item Helper. We'll ask you a few questions to gather data.")

    campaign_id = str(ask("What is your campaign id?"))
    name = str(ask("Name of line item?"))
    cost = int(ask("Cost of line item?"))
    goal = int(ask("Impression goal of line item?"))
    duration = int(ask("Duration of ad in seconds?"))

    if kind == "dynamic":
        start_date = str(arrow.get(str(ask(f"Start of line item {DATE_FORMAT}?")), DATE_FORMAT))
        end_date = str(arrow.get(str(ask(f"Start of line item {DATE_FORMAT}?")), DATE_FORMAT))

        # CREATE DYNAMICS LINE ITEMS
        dynamic_line_item = DynamicLineItem(
            campaign_id, name, goal, cost, duration, start_date, end_date
        )
        dynamic_line_item_input = create_dynamic_input(dynamic_line_item)
        Mutation.create_dynamic_line_item(dynamic_line_item_input)
    elif kind == "streaming":
        # CREATE DYNAMICS LINE ITEMS
        streaming_line_item = StreamingLineItem(
            campaign_id, name, goal, cost, duration
        )
        streaming_line_item_input = create_streaming_input(streaming_line_item)
        Mutation.create_streaming_line_item(streaming_line_item_input)


def run_retrieve_tracking_urls():
    campaign_id = str(ask("What campaign are you retrieving tracking urls for?"))

    orgs = [Option(**o) for o in Query.get_orgs()["data"]["me"]["organizations"]]
    question = "Which org would you like to use?"
    pub_id = PUBLISHER_ID if PUBLISHER_ID else selector(question, orgs)

    # RETRIEVE TRACKING URLS
    tracking_urls_input = create_tracking_urls_input(pub_id, campaign_id)
    Query.get_tracking_urls(tracking_urls_input)
