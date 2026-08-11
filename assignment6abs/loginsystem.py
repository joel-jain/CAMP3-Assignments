from abc import ABC, abstractmethod


class LoginSystem(ABC):
    def __init__(self, username, password):
        self.username = username
        self._password = password

    @abstractmethod
    def login(self, username, password):
        pass

    @abstractmethod
    def logout(self):
        pass

class AdminLogin(LoginSystem):
    def login(self, username, password):
        if self.username == username and self._password == password:
            print(f"Admin {self.username} logged in successfully.")
        else:
            print("Invalid username or password")

    def logout(self):
        print(f"Admin {self.username} logged out.")

class UserLogin(LoginSystem):
    def login(self, username, password):
        if self.username == username and self._password == password:
            print(f"User {self.username} logged in successfully.")
        else:
            print("Invalid user credentials.")

    def logout(self):
        print(f"User {self.username} logged out.")


if __name__ == "__main__":
    user = UserLogin("ramu", "user123")
    admin = AdminLogin("admin", "admin123")

    user.login("ramu", "user123")
    user.logout()

    admin.login("admin", "wrongpass")
    admin.login("admin", "admin123")
    admin.logout()
