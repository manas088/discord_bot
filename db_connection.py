import psycopg2
from constants import DATABASE_NAME, USER, PASSWORD, HOST, PORT


# getting connection of the db, i have not handled any exception due to time constraint
def get_connection():
    con = psycopg2.connect(database=DATABASE_NAME, user=USER, password=PASSWORD, host=HOST,
                           port=PORT)
    return con


# this function is to insert in database the search key and the username of the user
def inser_to_db(search_word, user_name):
    sql = "INSERT INTO  search_history(search_word,user_name) VALUES ('" + search_word + "','" + user_name + "')"
    con = get_connection()
    cur = con.cursor()
    cur.execute(
        sql)
    con.commit()
    con.close()


# this function is searching the word from db and returning them as list in case found
# search is based on user and search word
def search_from_db(search_word, user_name):
    sql_query = "select search_word from search_history where user_name='" + user_name + "' and search_word like '%" + search_word + "%' "
    print(sql_query)
    con = get_connection()
    cur = con.cursor()
    cur.execute(sql_query)
    # this return  list of tuple in python
    row = cur.fetchall()
    # conveting to list of list
    result_list = [list(elem) for elem in row]
    # creating set
    unique_set = set()
    for word in result_list:
        unique_set.add(word[0])
    con.close()
    return list(unique_set)
