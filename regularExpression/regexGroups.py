from re import finditer
text="abc34 @kPfg"
# pattern="[a-k]"           #[ ] not list  means either a or b or k   a to k
# pattern="[a-kA-Z0-9]"                                              #FOR ALL ALPHANUMERIC VALUE
# pattern="[^a-kA-Z0-9\s]"                                           #excluding alphanumerics
# pattern="[^0-9]"                                                   #excluding numerics
pattern="[\s]"                                                       #chck for space
matcher=finditer(pattern,text)
count=0
for p in matcher:
    print(p.start(),"==",p.group())
    