import mysql.connector
from constants import *

# Open database connection
def sql_connect():
    connection = mysql.connector.connect(host=HOST,user=USERNAME,passwd=PASSWORD,database=DB)
    return connection;

