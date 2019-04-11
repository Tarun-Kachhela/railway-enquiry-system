from connect_db import *
from utility_functions import *
conn=sql_connect();
mycursor = conn.cursor();

mycursor.execute("SET autocommit=0");

def select(tablename,condition="1"):
    mycursor.execute("SELECT * FROM "+tablename+" WHERE "+condition)
    return mycursor.fetchall()



def insert(tablename,coloumn_list,values_list):
    # conn=sql_connect();
    mycursor = conn.cursor()
    print(len(coloumn_list))
    if(check_for_validation(tablename,coloumn_list,values_list)):
         print("INSERT INTO "+tablename+build_insert_query_string(coloumn_list,values_list));
         mycursor.execute("INSERT INTO "+tablename+build_insert_query_string(coloumn_list,values_list))
         return True;
    else:
        return False;
    # return mycursor.()

#data = select("station");
#print(data)
#data = insert("stoppage",["Train_No","Station_Code","Arrival_Time","Departure_Time"],["12559","c","",""])
#print(data)


#data = select("station");
#print(data)

def update(tablename,coloum_list,values_list,condition=1):
    conn=sql_connect();
    mycursor = conn.cursor()
    print(len(coloum_list))
    if(check_for_validation(tablename,coloum_list,values_list)):
        query ="UPDATE "+tablename+" SET "+build_update_query_string(coloum_list,values_list)+" WHERE "+condition;
        mycursor.execute("UPDATE "+tablename+" SET "+build_update_query_string(coloum_list,values_list)+" WHERE "+condition)
        print(query)
    else:
        return False;

data = update("station",["Station_Name"],["qqqq"],"Station_Code='NDLS'")
print(data)
