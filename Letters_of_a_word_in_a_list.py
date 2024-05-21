def can_make(lst,string):
    for i in string:
        if i not in lst:
            return False
    return True 

lst = ['a','l','p','c','e','d']
string = 'apple'
result = can_make(lst,string)
print(result)
