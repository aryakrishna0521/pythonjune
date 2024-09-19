f=open("C:\\Users\\acer\\Desktop\\PythonJuneWorks\\fileworks.py\\landslide.txt","r")
data=[]
for line in f:
    # print(line)
    lst=line.rstrip("\n").split(" ")
    dic={"state":lst[0],"year":lst[1],"death":int(lst[2])}
    data.append(dic)
# print(data)


# #-----------------------------------------------------------------------------------------------------------------------------

#1 death_per_state

death_per_state={}
for dic in data:
    state=dic.get("state")
    death_count=dic.get("death")
    if state in death_per_state:
        death_per_state[state]+=death_count
    else:
        death_per_state[state]=death_count
#print(death_per_state) 
          

#------------------------------------------------------------------------------------------------------------------------------

#2 death_per_year
death_per_year={}
for dic in data:
    year=dic.get("year")
    death_count=dic.get("death")
    if year in death_per_year:
        death_per_year[year]+=death_count
    else:
        death_per_year[year]=death_count
# print(death_per_year)        


#--------------------------------------------------------------------------------------------------------------------------------

#3 state with highest death_count
def get_value(value):
    return death_per_state.get(value)
for w in death_per_state:
    srt=sorted(death_per_state,key=get_value,reverse=True)
print(f"state with highest death count is {srt[0]} deaths {get_value(srt[0])}")


#-------------------------------------------------------------------------------------------------------------------------

#death count in kerala on 2018

