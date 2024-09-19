placement={"testing":45,"jango":55,"flutter":30,"mern":40}
def get_value(key):
    return placement.get(key)

srt=sorted(placement,key=get_value,reverse=True)
print(srt)