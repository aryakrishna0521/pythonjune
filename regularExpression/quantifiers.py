from re import finditer
text="ab12xyz678#$pqr123 cdef"
# pattern="[a-z]{3}"            #to mention quantity we use {count}

# pattern="[0-9]{3}"

# pattern="[a-z]{3}|[0-9]{3}"

# pattern="[c-h]|[t-z]"         #c-h or t-z

# pattern="[a-z]"                #all alpha
 
#pattern="\d"                    # [0-9]

# pattern="\D"                   #[^0-9]       also use \\

# pattern="\w"                    #[a-zA-Z0-9]

# pattern="\W"                    #[^A-Za-z0-9]

# pattern="\s"                    #space

#pattern="\S"                       #excllude space

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==",m.group())