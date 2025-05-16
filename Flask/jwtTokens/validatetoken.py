from jwtmanager import JWTManager

jman = JWTManager(secret_key="MySecret.456")

#token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IlVzZXJOb0V4cGlyYXRpb24ifQ.-mix3VPCGFi52qZS-B98PH_roWNzA00OE0yU13w8PpA'
token = 'abc123'

if jman.validate_token(token):
    print("Valid token")
else:
    print("Invalid token")

