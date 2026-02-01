from growwapi import GrowwAPI
import pyotp
 
api_key = "API_KEY"
secret="SECRET_KEY"
 
access_token = GrowwAPI.get_access_token(api_key=api_key, secret=secret)
# Use access_token to initiate GrowwAPI
groww = GrowwAPI(access_token)