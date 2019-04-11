from connect_db import *
conn=sql_connect();
mycursor = conn.cursor();

def ifExists(tablename):
    res = mycursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = '"+tablename+"'");
    if(res!=None):
        return False
    return True

def check_for_validation(tablename,coloum_list,values_list):
    if(ifExists(tablename) and coloum_list!=None and values_list!=None):
        if(len(coloum_list)==len(values_list)):
            return True
    return False


#this will give me insert query string from coloum list till values
def build_insert_query_string(coloum_list,value_list):
    count=0
    coloum_names=""
    values = ""
    values+="'";
    # coloum_names+="";
    for value in range(len(coloum_list)):
        count+=1
        values+=value_list[value]
        coloum_names+=coloum_list[value]
        if(len(coloum_list)!=count):
            values+="',"
            coloum_names+=","
        values+="'";
        # coloum_names+="'";
    result = "("+coloum_names+") VALUES ("+values+")";
    print(result)
    return result


    # for coloum_name in coloum_list:
	# 	coloum_names+=coloum_name+","

	
def build_update_query_string(coloum_list,value_list):
    count=0
    # coloum_names+="";
    mainString=""
    for value in range(len(coloum_list)):
        count+=1
        mainString += coloum_list[value] + "='"+value_list[value]+"'"
        if(len(coloum_list)!=count):
            mainString+=","
    return mainString

c=build_update_query_string(["Station_Code","Station_Name"],["u","t"])
print(c)

