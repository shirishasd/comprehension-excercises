num_list=[]
for i in range(1,101):
   if (i % 3 == 0 and i % 5 == 0):
     num_list.append("FizzBuzz")
   elif( i % 3 == 0 ):
     num_list.append("Fizz")
   elif i % 5 == 0:
     num_list.append("Buzz")
   else:
     num_list.append(i)

print('Num_list is :' + str(num_list))

num_list2=[]
num_list2= [ ('FizzBuzz') if i % 3 == 0 and i % 5 == 0 else ("Fizz") if i % 3 == 0  else ("Buzz") if i % 5 == 0 else i  for i in range (1,101)]

print('Num_list2 is :' + str(num_list2))