from flask import Flask, request
from flask_restful import Resource, Api
import sqlite3

# Starting our app
app = Flask(__name__)
api = Api(app)


# to see all data from the database

class Show_users(Resource):
    def get(self):
        db = sqlite3.connect('database.db')
        ptr = db.cursor()
        sql = """SELECT * FROM users"""
        ptr.execute(sql)
        user_data = ptr.fetchall()
        user_details = []
        for i in range(0, len(user_data)):
            user_details.append(({'id': user_data[i][0], 'first_name': user_data[i][1], 'last_name': user_data[i][2],
                                  'company_name': user_data[i][3], 'age': user_data[i][4], 'city': user_data[i][5],
                                  'state': user_data[i][6], 'zip': user_data[i][7],
                                  'email': user_data[i][8], 'web': user_data[i][9]}))
        return user_details, 200


# showing data by its unique id

class Show_user(Resource):
    def get(self, id):
        db = sqlite3.connect('database.db')
        ptr = db.cursor()
        ptr.execute("""SELECT * FROM users WHERE Id={}""".format(id))
        user_data = ptr.fetchall()
        if user_data == []:  # If the id doesn't found in database
            return {'message': "The given id is not found"}, 404  # 404 is the status code for file not found
        user_details = {'id': '', 'first_name': '', 'last_name': '', 'company_name': '',
                        'age': '', 'city': '', 'state': '', 'zip': '', 'email': '', 'web': ''}

        for user in user_details:
            user_details = {'id': user_data[0][0], 'first_name': user_data[0][1], 'last_name': user_data[0][2],
                            'company_name': user_data[0][3], 'age': user_data[0][4], 'city': user_data[0][5],
                            'state': user_data[0][6], 'zip': user_data[0][7],
                            'email': user_data[0][8], 'web': user_data[0][9]}
            return user_details, 200  # 200 is the status code for success


# creating a new user

class Create_User(Resource):
    def post(self, id):
        # if the user{id} already exists
        # search id in database if found which means user already exists if not then create
        # make a query for search
        db = sqlite3.connect('database.db')
        ptr = db.cursor()
        ptr.execute("SELECT * FROM users WHERE id={}".format(id))
        show_data = ptr.fetchall()
        if (show_data != []):
            return {'message': 'user with id {} is already exists in our database'.format(
                id)}, 400  # 400 is status code for BAD REQUEST
        else:
            data = request.get_json()  # Requesting data from json payload
            #  SQL query for adding data into database
            sql = """INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,?);"""
            values = (id, data['first_name'], data['last_name'], data['company_name'],
                      data['age'], data['city'], data['state'], data['zip'],
                      data['email'], data['web'])
            ptr.execute(sql, values)
            db.commit()
        # data = request.get_json()
        item = {'id': id, 'first_name': data['first_name'], 'last_name': data['last_name'],
                'company_name': data['company_name'], 'age': data['age'], 'city': data['city'], 'state': data['state'],
                'zip': data['zip'], 'email': data['email'], 'web': data['web']}

        return item, 201  # 201 is status code for created


# For deleting the user of specific id

class Delete_User(Resource):
    def delete(self, id):
        db = sqlite3.connect('database.db')
        ptr = db.cursor()
        ptr.execute("SELECT * FROM users WHERE id={}".format(id))
        show_data = ptr.fetchall()
        if (show_data != []):
            ptr.execute("DELETE FROM users WHERE id={}".format(id))
            db.commit()
            return {'message': "id {} Successfully deleted".format(id)}, 200
        else:
            return {'message': "user having id {} doesn't  exists in our database".format(id)}, 404

# For Updating user's Info
class Update_user(Resource):
    def put(self, id):
        db = sqlite3.connect('database.db')
        ptr = db.cursor()
        ptr.execute("""SELECT * FROM users WHERE Id={}""".format(id))
        user_data = ptr.fetchall()
        if user_data == []:  # If the id doesn't found in database
            return {'message': 'id {} is not found in database'.format(id)}, 404
        else:
            data = request.get_json()
            sql = """UPDATE users SET `First` = ?,
             `Last`= ?, Age= ? WHERE id= ?"""
            values = (data['first_name'], data['last_name'], data['age'], id)
            ptr.execute(sql, values)
            db.commit()
            return {'first_name': data['first_name'], 'last_name': data['last_name'], 'age': data['age']},200


# ENDPOINTS
api.add_resource(Show_users, '/users')  # this api gives you all users
api.add_resource(Show_user, '/users/<int:id>')  # this api will give you user with specified id
api.add_resource(Create_User, '/users/<int:id>')  # this api will create a new user in database
api.add_resource(Delete_User, '/users/<int:id>')  # this api will delete user with the specific id
api.add_resource(Update_user, '/users/<int:id>')  # this api will update user information  with specific id

if __name__ == "__main__":
    app.run(debug=True)
