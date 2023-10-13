class MockDBController:

    @staticmethod
    def get_user_hash(name):
        pass

    @staticmethod
    def get_ship(id):
        pass

    @staticmethod
    def get_all_ships_from_user_id_db(id):
        pass

    @staticmethod
    def create_ship(user, name, id, is_active, capacity):
        pass

    @staticmethod
    def update_ship(user, name, id, is_active, capacity):
        pass

    @staticmethod
    def delete_ship(user):
        pass

    @staticmethod
    def get_all_quests_from_user_id_db(user):
        pass

    @staticmethod
    def get_quest(user):
        pass

    @staticmethod
    def create_quest(user, name, id, is_active, resource, items_per_capacity, demand):
        pass

    @staticmethod
    def update_quest(user, name, id, is_active, resource, items_per_capacity, demand):
        pass

    @staticmethod
    def delete_quest(id):
        pass

    @staticmethod
    def get_all_users():
        pass

    @staticmethod
    def get_user():
        pass

    @staticmethod
    def create_user(name, id):
        pass

    @staticmethod
    def update_user(name, id):
        pass

    @staticmethod
    def delete_user(id):
        pass
