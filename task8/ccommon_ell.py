def is_comment_element(lst1, lst2):
    
    for n1 in lst1:
        
        if n1 in lst2:
            
            return True
        else:
        
            return False

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9,2]


print(is_comment_element(l1, l2))