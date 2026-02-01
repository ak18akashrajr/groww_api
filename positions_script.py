from growwapi import GrowwAPI
 
# Groww API Credentials (Replace with your actual credentials)
API_AUTH_TOKEN = "AUTH_TOKEN"
# Initialize Groww API
groww = GrowwAPI(API_AUTH_TOKEN)
 
# Get all positions (CASH, FNO, and COMMODITY)
user_positions_response = groww.get_positions_for_user()
 
# Get positions for specific segment
cash_positions_response = groww.get_positions_for_user(segment=groww.SEGMENT_CASH)
fno_positions_response = groww.get_positions_for_user(segment=groww.SEGMENT_FNO)
commodity_positions_response = groww.get_positions_for_user(segment=groww.SEGMENT_COMMODITY)
 
print(user_positions_response)