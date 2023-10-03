'''
liste = [19,2,31,45,6,11,121,27]
'''
for x in range(1, 100):
 if x % 3  == 0 and x % 5 == 0:
  print("Fizz_Buzz", sep=' \n')
 elif x % 3  == 0:
  print("Fizz", sep=' \n')
 elif x % 5  == 0:
  print("Buzz", sep=' \n')
 else:
  print(x, sep= ' \n')