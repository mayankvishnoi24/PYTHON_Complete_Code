# Dictionary Datatype

# # Indentification Dictionary {} courly Bracket

# Example:   
#             {   'a'   :   'apple'   }
#                 Key        # Value

#             {   'a'   :   ['apple','ant','anaconda']}
#                             Multiple values in a dictionary

dic = {'a':['apple','ant','anaconda'],1:200,False:0}
print(dic)
print(type(dic))
print(dic['a'])           # ['apple','ant','anaconda']
print(dic[1])             # 100
print(dic[False])         # 0
dic[1]= 300               # Update the Data
dic['b'] = 'ball'         # Adding the data

print(dic['a'][2])

print(dic)

# dic = {'a':'apple','b':'ball'}
# print(dic)