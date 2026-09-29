class User:
    def __init__(self, uuid, name, user_level):
        self.uuid = uuid
        self.name = name
        self.user_level = user_level

    def elevate(self):
        self.user_level = 999

user0 = User(uuid="xxxx0001", name="supremeAdmin", user_level=1)
user1 = User(uuid="xxxx0002", name="Hart", user_level=3)

user0.elevate()

print(f"{user0.uuid}, {user0.name}, {user0.user_level}")
print(f"{user1.uuid}, {user1.name}, {user1.user_level}")
