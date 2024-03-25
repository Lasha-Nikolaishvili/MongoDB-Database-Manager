import json
from pymongo import MongoClient


def regions():
    with open("data\\data.json", "r") as f:
        data = json.load(f)
    return list(data.keys())


class DatabaseManager:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.database = self.client["Database"]

    def create_table(self):
        pass

    def add_data(self, table_name, **kwargs):
        self.database[table_name].insert_one(kwargs)

    def get_existing_relations(self):
        result = self.database["student_advisor"].find()
        # return [(i['student_id'], i['advisor_id']) for i in result]
        return [tuple(entry.values()) for entry in result]

    def delete_row(self, table_name, row_id):
        if table_name == "advisors":
            self.database[table_name].delete_one({"advisor_id": row_id})
        else:
            self.database[table_name].delete_one({"student_id": row_id})

    def load_data(self, table_name):
        return [tuple(entry.values()) for entry in self.database[table_name].find()]

    def search(self, table_name, **search_terms):
        if search_terms:
            return [tuple(entry.values()) for entry in self.database[table_name].find(search_terms)]
        else:
            return self.load_data(table_name)

    def update(self, table_name, **update_terms):
        if table_name == "students":
            return (self.database[table_name]
                    .update_one(
                        {
                            "student_id": update_terms.get("id")
                        },
                        {"$set": update_terms})
                    .modified_count)
        elif table_name == "advisors":
            return (self.database[table_name]
                    .update_one(
                        {
                            "advisor_id": update_terms.get("id")
                        },
                        {"$set": update_terms})
                    .modified_count)

    def check_bd(self):
        result = self.database["student_advisor"].find()
        return True if not result else False

    def list_advisors_with_students_count(self, order_by):
        pipeline = [
            {
                "$lookup": {
                    "from": "student_advisor",
                    "localField": "advisor_id",
                    "foreignField": "advisor_id",
                    "as": "students"
                }
            },
            {
                "$group": {
                    "_id": "$advisor_id",
                    "name": {"$first": "$name"},
                    "surname": {"$first": "$surname"},
                    "student_count": {"$sum": {"$size": "$students"}}
                }
            },
            {
                "$project": {
                    "advisor_id": "$_id",
                    "name": 1,
                    "surname": 1,
                    "student_count": 1,
                    "_id": 0
                }
            },
            {
                "$sort": {"student_count": order_by}
            }
        ]

        result = self.database['advisors'].aggregate(pipeline)
        return [tuple(entry.values()) for entry in result]

    def list_students_with_advisors_count(self, order_by):
        pipeline = [
            {
                "$lookup": {
                    "from": "student_advisor",
                    "localField": "student_id",
                    "foreignField": "student_id",
                    "as": "advisors"
                }
            },
            {
                "$group": {
                    "_id": "$student_id",
                    "name": {"$first": "$name"},
                    "surname": {"$first": "$surname"},
                    "advisor_count": {"$sum": {"$size": "$advisors"}}
                }
            },
            {
                "$project": {
                    "student_id": "$_id",
                    "name": 1,
                    "surname": 1,
                    "advisor_count": 1,
                    "_id": 0
                }
            },
            {
                "$sort": {"advisor_count": order_by}
            }
        ]

        result = self.database['students'].aggregate(pipeline)
        return [tuple(entry.values()) for entry in result]
