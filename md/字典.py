# # -*- coding: utf-8 -*-  
# person = {'name':'zhangsan','age':18,'math':98,
#             'chinese':95,'english':95,'height':180,'weight':150}

# # print(person['age'])   #18
# # print(person.get('gender') )
# del person['math']
# print(person)

# x1={'name':'zhangsan','age':18}
# x2={'english':95,'height':180,'weight':150}
# x1.update(x2)
# print(x1)

# person =   {'name':'zhangsan','age':18,'math':98,'chinese':95}


# # for x in person: #x返回key
# #     print(x ,'=',person[x])
# # for x in person.items():
# # 	print(x[0],'=',x[1])

# for k,v in person.items():
# 	print(k,'=',v)
# chars=['a','a','a']
# char_count={}
# for char in chars:
#     char_count[char]=1
# print(char_count)


# person = [
#     {'name':'zs','age':'12'},
#     {'name':'ls','age':'15'},
#     {'name':'ww','age':'2'},
#     {'name':'zl','age':'122'},
    
# ]

# name_in=input('name')
# for each in person:
#     if name_in==each['name']:
#         print(each['age'])
#         break
# else:
#     age_in=input('添加数据请输入age')
#     each['name']=name_in
#     each['age']=age_in
#     person.append(each)
# print(person)


x1={'name':'zs','age':'12'}
x2 = {k:m for m,k in x1.items()}
print(x2)