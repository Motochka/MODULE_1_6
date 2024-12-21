my_dict={'Vasya': 1975,'Igor': 1999,'Masha':2002}
print(my_dict)
print("Existing value:",my_dict['Masha'])
print("Not existing value:",my_dict.get('Kamila') )
#my_dict ={'Kamila': 1981,'Artem': 1915}
rem_val=my_dict['Igor']
del my_dict["Igor"]
print('Delete value:', rem_val)
my_dict['Kaila']=1981
my_dict['Artem']=1915
print("modifite dictionary:",my_dict)

my_set={1,'apple',1,1,42.314,'apple'}
print('SET:',my_set)
print(my_set.add(13))
print(my_set)
print(my_set.remove(1))
#print(my_set.add(5,6))
numb=[5,6,1.6]
my_set.update(numb)
print('Modifite set:',my_set)