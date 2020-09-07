import os
import json
from django.conf import settings


DB_DIR = str(settings.BASE_DIR) + '/db.json'


class JsonDB:
    def __init__(self, location):

        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load_db()
        else:
            self.db = {}
            self.dump_db()

    def _load_db(self):
        with open(self.location) as file:
            self.db = json.load(file, )

    def dump_db(self):
        with open(self.location, 'w') as file:
            json.dump(self.db, file, ensure_ascii=False)

    def set(self, key, value):
        try:
            self.db[str(key)] = value
            self.dump_db()
        except Exception as e:
            print(f"Error Saving Values to Database : {e}")

    def get(self, key):
        try:
            return self.db[str(key)]
        except KeyError:
            print(f"No Value Can Be Found for {key}")

    def delete(self, key):
        if key in self.db:
            del self.db[str(key)]
        self.dump_db()

    def get_max_id(self):
        return len(self.db.keys())



