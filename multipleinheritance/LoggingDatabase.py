
class Logger:
    def __init__(self, log_level):
        self.log_level = log_level

    def log(self, message):
        print(f"[{self.log_level}] {message}")


class Database:
    def __init__(self, db_name):
        self.db_name = db_name

    def connect(self):
        print(f"Connected to database: {self.db_name}")

class Application(Logger, Database):
    def __init__(self, log_level, db_name):
        Logger.__init__(self, log_level)
        Database.__init__(self, db_name)

obj_app = Application("INFO", "CustomerDB")

obj_app.log("Application started")
obj_app.connect()
