students=[
    {id:100,"name":"arya","course":"django","mark":450},
    {id:101,"name":"anu","course":"django","mark":450},
    {id:102,"name":"arjun","course":"asp","mark":450},
    {id:103,"name":"akash","course":"mearnstack","mark":450},
    {id:104,"name":"arun","course":"datascience","mark":450},

]
studenr_name=[st.get("name")for st in students]
print(studenr_name)

django_stu=[st.get("name") for st in students if st.get("course")=="django"]
print(django_stu)