
email_id="johnsmith@gmail.com"
at_index_pos=email_id.index("@")

user_name=email_id[:at_index_pos]
print(user_name)

mail=email_id[at_index_pos:]
print(mail)