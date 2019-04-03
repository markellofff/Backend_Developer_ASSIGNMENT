# Backend_Developer_ASSIGNMENT
Backend Developer Assignment  Solution for Data Peace AI Technology Private Limited


Setting Environment
1. use command in terminal, pip install Flask for installing flask 
2. use command in terminal, pip install Flask-RESTful 
3. Download Postman app for checking the API's . Link for the app (https://www.getpostman.com/downloads/)



Setting Project
1. After Environment Setup
2. Download app.py, creating_database.py, users.json file 
3. Ensure that all these files must have at same level directory
4. Run creating_database.py only once. NOTE: If u run twice or more than 1 times then it will give an error that the table name is
   already created in database.
5. Run app.py file it will start your server the output must be like ( * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit))
   and few lines more
6. Copy the link and paste in the postman app
7. Check For endpoints


Endpoints 
1.  http://127.0.0.1:5000/users   And Method Must be GET
    It gives you the details of the users that already exists in database
    
2.  http://127.0.0.1:5000/users/{id} And Method Must be GET
    It gives you the detail of the user with id={id}
     (example : if id= 15 then API will be http://127.0.0.1:5000/users/15)
    
3.  http://127.0.0.1:5000/users/{id} And Method Must be POST
    It creates a user with Id given and data given by postman app 
    
    Example: if you have to add a user with id =601
    ( http://127.0.0.1:5000/users/601 and json payload is raw in postman app)
    For posting data in database you have to setup postman app 
    setting up Postman App:-
    1. goto Headers in postman app and enter in Content-Type key coloumn and application/json in value coloumn.
        for reference see image file headers.png
    2. goto body in postman app and select raw and write in the following json format
        for reference see image file body.png
     {
        "first_name": "James",
        "last_name": "Butt",
        "company_name": "Benton, John B Jr",
        "city": "New Orleans",
        "state": "LA",
        "zip": 70116,
        "email": "jbutt@gmail.com",
        "web": "http://www.bentonjohnbjr.com",
        "age": 70
      }
    3. save 
    
4.  http://127.0.0.1:5000/users/{id} And Method must be PUT
    It updates the user data of the specific id given 
     Example  http://127.0.0.1:5000/users/601
     For Updating data in database you have to setup postman app 
    setting up Postman App:-
    1. goto Headers in postman app and enter in Content-Type key coloumn and application/json in value coloumn.
        for reference see image file headers.png
    2. goto body in postman app then select raw and write in the following json format
        for reference see image file body.png
      {
        "first_name": "Josephine",
        "last_name": "Darakjy",
        "age": 48
      }
5.  http://127.0.0.1:5000/users/{id} And Method Must be DELETE
    It deletes data from the database fro a specific id given by user
    Example : http://127.0.0.1:5000/users/601
            It deletes the data of id=601 from database
            
     
  
