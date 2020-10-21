import requests

# You can find the documentation here : https://www.ai-compare.com/v1/redoc/#operation/Syntax%20Analysis

#Enter your API Token
headers = {'Authorization': 'Bearer your API Key'} #You can get your free API token here https://www.ai-compare.com/accounts/login/?next=/my_apis

# Select API
url = 'https://www.ai-compare.com/v1/pretrained/text/syntax_analysis'

# Select providers, and language
payload = {'providers': '[\'google_cloud\', \'aws\', \'ibm\']','text':'I am angry today','language': 'en-US'}

# Request to AI COMPARE
response = requests.request("POST", url, headers=headers, data = payload, files = files)

# Print result
print(response.text.encode('utf8'))
