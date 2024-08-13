import re

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def check_username(self):
        if len(self.username) < 6 or len(self.username) > 30:
            return False
        
        if not re.match(r'^[a-zA-Z0-9.]{6,30}$', self.username):
            return False
        if '..' in self.username:
            return False
        
        return True

    def check_password(self):
        if len(self.password) < 8 or len(self.password) > 128:
            return False
        if not re.search(r'[A-Z]', self.password):
            return False
        if not re.search(r'[a-z]', self.password):
            return False
        if not re.search(r'[0-9]', self.password):
            return False
        if ' ' in self.password:
            return False
        if not re.search(r'[~!?@#$%^&*_\-+()\[\]{}><\\/|"\',:;]', self.password):
            return False
        
        return True

user = User("valid.username", "ValidPassword1!")
print("Username valid:", user.check_username())
print("Password valid:", user.check_password())
