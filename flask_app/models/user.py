from flask_app.config.mysqlconnection import connectToMySQL

class User:
    # constant with db name
    DB = "users_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # READ
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"

        # use results to store query results
        results = connectToMySQL(cls.DB).query_db(query)
        users = []

        # turn query rows into User instances
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_one(cls, user_id):
        query = "SELECT * FROM  users WHERE id = %(user_id)s"

        # use results to store query results
        results = connectToMySQL(cls.DB).query_db(query, {"user_id":user_id})
        # return a User instance
        return cls(results[0])


    
    # CREATE
    @classmethod
    def save(cls,data):
        query = """INSERT INTO users (first_name, last_name, email)
                VALUES (%(first_name)s, %(last_name)s, %(email)s)"""

        # query db and return the id of the newly created user in users
        return connectToMySQL(cls.DB).query_db(query, data)
    
    # UPDATE
    @classmethod
    def update(cls,data):
        query = """UPDATE users 
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW()
                WHERE id = %(id)s"""
        # query db with update and return
        return connectToMySQL(cls.DB).query_db(query,data)

    # DELETE
    @classmethod
    def delete(cls,user_id):
        query = """DELETE FROM users
                    WHERE id = %(user_id)s"""
        # query db with delete and return
        return connectToMySQL(cls.DB).query_db(query, {"user_id": user_id})