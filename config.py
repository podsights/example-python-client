from utils import Option
# variables for inputs

# campaigns
org_id = ""
company_id = ""
name = ""
kind = ""
cost = ""
goal = ""
start_date = ""
end_date = ""

# common
url = "http://api.pdst.fm/graph/analytics"
kind_options = [Option(id="attribution", name="attribution"), Option(id="marketing", name="marketing"), Option(id="reporting", name="reporting")]

headers = {
  'Authorization': '',
  'Content-Type': 'application/json',
  'Cookie': ''
}