
def build_update_query_string(coloum_list,value_list):
    count=0
    # coloum_names+="";
    mainString="UPDATE train SET "
    for value in range(len(coloum_list)):
        count+=1
        mainString += coloum_list[value] + "='"+value_list[value]+"'"
        if(len(coloum_list)!=count):
            mainString+=","
    mainString+=" WHERE condition"
    return mainString

c=build_update_query_string(["Station_Code","Station_Name"],["u","t"])
print(c)
