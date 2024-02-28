class UserData:
    def __init__(self):
        self.data = "aaaa"

    def get_data(self):
        return self.data


class UserContext:
    def __init__(self):
        pass

    def get_user_data_by_id(self, id) -> UserData:
        return UserData()
