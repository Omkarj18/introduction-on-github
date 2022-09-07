# typecasting is used to to convert the datatype to respective datatype as per requirment.

a =10
b =23.67
c ='145.22'

a1=float(a)   # it will convert int datatype to float datatype


#print(a1)    # it will display converted result to the o/p
# print(a+c)   # it will sow error bcz both datatpe is diferent 'int & str'
#print(a+b)

# convert str to int
#c1 =int(c) # it will show error bcz string value is in .format ,so first we have to convert it into float the we can convert into integer
print(int(float(c))+b) # this will add c variable and b variable

