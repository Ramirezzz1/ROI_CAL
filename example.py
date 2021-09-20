# my_data = {
#     'name': "ronald ramirez"
#     'abilites': ['walk','run',]
# }


my_list = []
start, end = 1,20

if start < end :
    my_list.extend(range(start,end))
    my_list.append(end)
print(my_list)