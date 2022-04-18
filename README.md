INTRODUCTION
------------
This client will demonstrate how Python can use the request library to make calls to a GraphQL endpoint.  When making a call to a GraphQL endoint it will typically be a "POST" request - even when retrieving data.  The URL, HEADERS, and query (in JSON format) are all required.  Variables are optional, they are passed when the query or mutation expects an identifier for the call (ie, an ID for a specific object).


REQUIREMENTS
-------------
This client was built with Python 3.8 and will need the packages in the requirements.txt 


CONFIGURATION
-------------
This client is interactive to show you the data you need to gather for various calls, as well as calls you can use to get your data.  This repo also includes a .env.template file.  You will want to remove the .template and fill in the variables in the environment.  The PUBLISHER_ID can be filled in using the interactive client - however the other variables will need to be filled in before starting.

To get your API Secret and Key you will need to login to Podsights and click manage on the left-hand side.  There will be an option to click API Keys - there you can generate your key and secret.  They cannot be retrieved so please document them.

STARTING
---------
To start you need to run the main python file.  That will give you options of different helpers that will kick off different mutations or queries.  If you do not know your PUBLISHER_ID when starting then the variable should look like this in your env file: ```PODSIGHTS_PUBLISHER_ID=```