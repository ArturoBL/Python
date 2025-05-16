from jwtmanager import JWTManager
from datetime import datetime

jman = JWTManager(secret_key="MySecret.456")

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlVzZXIxMGRheXMiLCJleHAiOjE3NDgzMTEzMDcuMjkwNjQ3fQ.NLn5uUwtuQSS-Yr_TKRsOMjiN1KS0TvJYMES2Tbv1bY'

#get user and expiration
user = jman.get_user(token)
exp = jman.get_expiration(token)
exps = datetime.fromtimestamp(exp).strftime('%Y-%m-%d %H:%M:%S')

#print data
print("User: ",user)
print("Expiration: ",exps)
