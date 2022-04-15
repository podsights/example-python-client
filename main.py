from graph.queries import *
from graph.variables import *
from graph.mutations import *
import config
from utils import selector, Option
import arrow


if __name__ == "__main__":

    # Gather Variables
    print("You're running the create a campaign helper")
    print("getting your orgs ...")
    orgs = [Option(**o) for o in Query.get_orgs()["data"]["me"]["organizations"]]
    print(orgs)
    pub_id = config.org_id if config.org_id else selector("Which org would you like to use?", orgs)
    print(pub_id)
    search_brand = str(input("\n\nEnter the brand that is advertising in this campaign.\n\n"))
    brands = [Option(**b) for b in Query.get_brands(search_brand)["data"]["me"]["companySearch"]]
    print(brands)
    brand_id = config.company_id if config.company_id else selector("Which brand would you like to use?", brands)
    print(brand_id)
    campaign_name = config.name if config.name else input("\n\nWhat is the name of your campaign?\n\n")
    kind = config.kind if config.kind else selector("\nWhat type of campaign are you creating?", config.kind_options)
    cost = config.cost if config.cost else int(input("\n\nWhat is the estimated cost of the campaign?\n\n"))
    goal = config.goal if config.goal else int(input("\n\nWhat is the estimated goal of the campaign?\n\n"))
    start_date = config.start_date if config.start_date else arrow.get(input("\n\nWhen is the start of your campaign (MM/DD/YYYY)?\n\n"),'MM/DD/YYYY')
    print(start_date)
    end_date = config.end_date if config.end_date else arrow.get(input("\n\nWhen is the end of your campaign (MM/DD/YYYY)?\n\n"),'MM/DD/YYYY')
    print(end_date)

    # CREATE CAMPAIGN
    campaign = Campaign(pub_id, campaign_name, kind, brand_id, cost, goal, start_date, end_date)
    campaign_input = create_campaign_input(campaign)
    Mutation.create_campaign(campaign_input)
