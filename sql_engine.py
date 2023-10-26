import mysql.connector
connectionstring='bizcard.cwoakibr9oeh.ap-south-1.rds.amazonaws.com'
password='Thinesh1234'
user='Thinesh'

connection=mysql.connector.connect(host=connectionstring,user=user,password=password)
cursor_object=connection.cursor()

def load(results):
    cursor_object.execute('use bizcard')
    cursor_object.execute('create table if not exists contact (Name varchar(100),phone varchar(50), email varchar(100), Role varchar(100),website varchar(100),address varchar(250),company varchar(25))')
    connection.commit()
    query='insert into contact (name, phone, email, role,website,address,company) values(%s,%s,%s,%s,%s,%s,%s)'
    for result in results:
         value=list(result.values())
         cursor_object.execute(query,value)
         connection.commit()

def one_img_extracted_data(result):
     
    cursor_object.execute('use bizcard')
    cursor_object.execute('create table if not exists contact (Name varchar(100),phone varchar(50), email varchar(100), Role varchar(100),website varchar(100),address varchar(250),company varchar(25))')
    connection.commit()
    query='insert into contact (name, phone, email, role,website,address,company) values(%s,%s,%s,%s,%s,%s,%s)'
    value=list(result.values())
    cursor_object.execute(query,value)
    connection.commit()

         