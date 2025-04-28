dictionary={'Arjun':50, 'Krishna':96, 'Raghav':75, 'Rakesh':63}
marks=input("Enter Student's Name: ")
if marks in dictionary:
    print("Academic Marks of ",marks,{dictionary[marks]})
else:
    print("NO RESULTS FOUND - INVALID NAME", marks, {dictionary[marks]})
'''
print(dictionary)
dictionary['d']='Dog'
print(dictionary)
del(dictionary['b'])
print(dictionary)
'''