

#IMMUTABLE: int, 
## Immutable vs immutable var

#Case3:
# default parameter for append_list() is empty list lst []. but it is a mutable variable. Let's see what happen with the following codes:
def append_list(item, lst=[]):
    lst.append(item)
    return lst

print(append_list("item 1"))  # ['item 1']
print(append_list("item 2"))  # ['item 1', 'item 2']
# Shouldn't use mutable var as a parameter
def append_list(item, lst= None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst

#Case2: don't use += for string, because string is immutable. Instead, use join() method
msg= ""
for i in range(1000):
    msg+= "hello"
# each for loop, new msg varible created and that make RAM quickly full


#Case1: //list is mutable
def double_list(lists):
    for i in range(len(lists)):
        lists[i] = lists[i]*2
    return lists

lists = [x for x in range(1, 12)]
doubled = double_list(lists)

for i in range(len(lists)):
    print(doubled[i] / lists[i])
