import jwt
import json
import os
from datetime import datetime, timedelta

SECRETKEY = 'Secret$123'

class JWTManager:
    def __init__(self, db_file='users_db.json', secret_key=SECRETKEY):
        self.secret_key = secret_key
        self.db_file = './' + db_file        
        self._load_db()

    def _load_db(self):
        if not os.path.exists(self.db_file):
            self.db = []
            self._save_db()
        else:
            try:
                with open(self.db_file, 'r') as f:
                    self.db = json.load(f)
            except:
                print('no se encontro users_db.json')

    def _save_db(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.db, f, indent=4)

    def _find_record(self, username):
        for record in self.db:
            if record['username'] == username:
                return record
        return None
    
    def _find_token(self,token):
        for record in self.db:
            if record['token'] == token:
                return record
        return None

    def add_user(self, username, expiration_days=7, no_expiration=False):
        """
        Add a new user with an expiring token.
        
        Args:
            username (str): The username to add
            expiration_days (int): Days until token expires (default: 7)
            no_expiration (bool): If True, creates a token without expiration (default: False)
        """
        if self._find_record(username):
            raise ValueError(f"Usuario '{username}' ya existe.")
        
        # Calculate expiration time
        if no_expiration:
            payload = {'username': username}
            expiration = None
        else:
            expiration = datetime.utcnow() + timedelta(days=expiration_days)
            payload = {
                'username': username,
                'exp': expiration.timestamp()  # Store expiration as Unix timestamp
            }
                
        
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        if expiration:
            record = {
                'username': username,
                'token': token,
                'created_at': datetime.utcnow().isoformat(),
                'status': 'active',
                'expiration': expiration.isoformat()
            }
        else:
            record = {
                'username': username,
                'token': token,
                'created_at': datetime.utcnow().isoformat(),
                'status': 'active',
                'expiration': None
            }
        self.db.append(record)
        self._save_db()
        return token

    def revoke_token(self, username):
        record = self._find_record(username)
        if not record:
            raise ValueError(f"Usuario '{username}' no encontrado.")
        record['status'] = 'revoked'
        self._save_db()

    def reactivate_token(self, username):
        record = self._find_record(username)
        if not record:
            raise ValueError(f"Usuario '{username}' no encontrado.")
        record['status'] = 'active'
        self._save_db()

    def validate_user_token(self, username, token):
        record = self._find_record(username)
        if not record:
            return False
        if record['status'] != 'active':
            return False
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            # Check if token has expired (only if it has an expiration claim)
            if 'exp' in decoded and decoded['exp'] < datetime.utcnow().timestamp():
                return False
            return decoded.get('username') == username
        except jwt.InvalidTokenError:
            return False
    
    def validate_token(self, token):
        record = self._find_token(token)
        if not record:
            return False        
        if record['status'] != 'active':
            return False
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            # Check if token has expired (only if it has an expiration claim)
            if 'exp' in decoded and decoded['exp'] < datetime.utcnow().timestamp():
                return False
            return decoded.get('username') == record['username']    #el usuario corresponde al token
        except jwt.InvalidTokenError:
            return False

    def get_user(self, token):
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return decoded.get('username')
        except jwt.InvalidTokenError:
            return ""
    
    def get_expiration(self, token):
        try:
            decoded = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            return decoded.get('exp')
        except jwt.InvalidTokenError:
            return ""

    def get_all_users(self):
        return self.db
