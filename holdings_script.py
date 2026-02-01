from growwapi import GrowwAPI
 
# Groww API Credentials (Replace with your actual credentials)
API_AUTH_TOKEN = "AUTH_TOKEN"
# Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)
 
holdings_response = groww.get_holdings_for_user(timeout=5)
print(holdings_response)

