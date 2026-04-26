class User:
    def __init__(self, user_id, name, role):
        self.user_id = user_id
        self.name = name
        self.role = role

    def login(self):
        return f"{self.name} logged in"

    def logout(self):
        return f"{self.name} logged out"