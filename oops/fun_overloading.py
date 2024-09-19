# def get_person(**kwargs):
#     print(kwargs.get("name"))

#     print(kwargs.get("w_place"))




# get_person(name="hari",w_place="tvm",n_place="kakkanad")    




# *args arguments in tuple format
# **kwargs key value arguments dictionay format

def flat_list(*args):
    
    flat=[]

    for arg in args:

        if isinstance(arg,list):

            flat.extend(flat_list(*arg))
            
        else:
            flat.append(arg)
            
    return flat
    

print(flat_list((1,2,[10,20],[10,[100,200]])))
        