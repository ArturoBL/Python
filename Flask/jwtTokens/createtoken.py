from jwtmanager import JWTManager

# JWTManager uses a secret key to manage tokens
# once a user is added a db file is created in json format
# a user can be revoked or reactivated
jman = JWTManager(secret_key="MySecret.456")
User = 'User10days'
token = jman.add_user(User, expiration_days=10)

print(f"User for 10 days: {User}")
print(f"Token: {token}")

User = 'UserNoExpiration'
token = jman.add_user(User, no_expiration=True)

print(f"User No Expiration: {User}")
print(f"Token: {token}")
