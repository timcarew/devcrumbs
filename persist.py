import os
import psycopg2

dbuser = "timcarew"
dbpassword = "123test"
dbhost = "127.0.0.1"
dbport = "5432"
dbdatabase="newflask"

DATABASE_URL = os.environ['DATABASE_URL']

def add_user(name):
  try:
    connection = psycopg2.connect(DATABASE_URL, sslmode='require')
    cursor = connection.cursor()
    add_user_query = ''' INSERT INTO users (name) VALUES ('''
    add_user_query += " \'" + name + "\')"
    cursor.execute(add_user_query)
    connection.commit()
    count = cursor.rowcount
    print(count, "name added to database")

  except (Exception, psycopg2.DatabaseError) as error:
    print("Error while adding name to PostgreSQL db", error)
  finally:
  #closing database connection.
    if(connection):
      cursor.close()
      connection.close()
      print("PostgreSQL connection is closed")

def get_users():
  users = []
  try:
    connection = psycopg2.connect(user=dbuser,
                                  password=dbpassword,
                                  host=dbhost,
                                  port=dbport,
                                  database=dbdatabase)
    cursor = connection.cursor()
    get_users_query = "SELECT name FROM users"
    cursor.execute(get_users_query)
    names = cursor.fetchall()
    for row in names:
      users.append(row[0])
    return users

  except (Exception, psycopg2.Error) as error:
      print("Error while getting users in PostgreSQL", error)
  finally:
      #closing database connection.
          if(connection):
              cursor.close()
              connection.close()
              print("PostgreSQL connection is closed")
  return users
