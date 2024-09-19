class operations:
    def perform_add(self,*args):
        total=sum([arg for arg in args if isinstance(arg,(int,float))])
        return total

    
    def perform_max_number(self,*args):
        return max(args)
       

math=operations()
print(math.perform_add(90,10,30.5,"hello"))
print(math.perform_max_number(2,78,98,100,101.2))




