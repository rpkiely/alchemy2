import json
import mysql.connector
import app

from flask import Flask
from flask import request

app = Flask(__name__)


#db 
db_host='127.0.0.1'
db_user='root'
db_passwd='admin1!'
db_database='ships'
db_port=3306



@app.route('/spacecraft')
def spacecraft():
	try:
            shipname = request.args.get('name')
            shipclass = request.args.get('class')
            shipstatus = request.args.get('status')

            db = mysql.connector.connect(host=db_host, user=db_user, passwd=db_passwd, db=db_database, port=db_port)
            cursor=db.cursor(dictionary=True)

            sql = "select id, name, status from spacecraft"

            if shipname:
                sql = sql + (f" where name={shipname}")

            if shipclass:
                sql = sql + (f" where class={shipclass}")

            if shipstatus:
                sql = sql + (f" where status={shipstatus}")                                

            cursor.execute(sql)
            rows=cursor.fetchall()

            dict1={}
            dict1["data"]=rows

            resp=json.dumps(dict1, indent = 4)
            return resp

	except Exception as e:
		    print(e)

	finally:
		    cursor.close() 
		    db.close()





@app.route('/singleship')
def singleship():
	try:
            id = request.args.get('id')
            if not id:
                id = 1
                
            db = mysql.connector.connect(host=db_host, user=db_user, passwd=db_passwd, db=db_database, port=db_port)           
            cursor=db.cursor(dictionary=True)

            cursor.execute(f"SELECT * FROM spacecraft where id={id}")
            rows1 = cursor.fetchall()

            dict1={}
            for row in rows1:
                dict1.update(row)

            cursor.execute(f"SELECT * FROM arms where id={id}")
            rows2 = cursor.fetchall()

            list1 = []
            for row in rows2:
                dict2={}
                dict2["title"]=row["title"]
                dict2["qty"]=row["qty"]
                list1.append(dict2)
            
            dict1["armament"]=list1
            resp=json.dumps(dict1, indent = 4)
            return resp

	except Exception as e:
		    print(e)

	finally:
		    cursor.close() 
		    db.close()



if __name__ == "__main__":
    app.run()