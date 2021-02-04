# alchemy2

ships.sql : mysql dump of db

app.py : python flask implementation of a rest api

requirements.txt : library requirements for app.py (flask and mysql)

alchemy.postman_collection.json : collection of postman tests


To Test:
1) Run the app.py
2) Use the postman collection to test

Postman tests:
1) spacecraft : Use name OR class OR status singulary to test api. Defaults to all if no params passed.
2) singleship : Use id to specify ship. Defaults to id=1 if no param passed.
