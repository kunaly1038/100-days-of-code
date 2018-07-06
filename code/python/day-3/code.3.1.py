
def lcm(x, y, z, a):



   if (x > y) & (x > a) & (x> z) :
       greater = x
   elif (y > x) & (y > a) & (y > z):
       greater =y
   elif (a > x) & (a > y) & (a > z):
       greater=a
   else:
       greater = z

   while(True):
       if((greater % x == 0) & (greater % y == 0) & (greater % a ==0) & (greater % z ==0)):
           lcm = greater
           break
       greater += 1

   return lcm




def hcf(x, y, a, z):


    if (x < y & x < a & x < z):
        smaller = x
    elif (y < x & y < a & y < z):
        smaller = y
    elif (a < x & a < y & a < z):
        smaller = a
    else:
        smaller = z

    while(True):
        if((x % smaller == 0) & (y % smaller == 0) & (a % smaller ==0) & (z % smaller ==0)):
           hcf = smaller
           break
        smaller += 1

    return hcf


num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))
num3 = int(input('Enter the third number:'))
num4 = int(input('Enter the fourth number:'))

print("The LCM of", num1,"and", num2,num3,"and", num4,"is", lcm(num1, num2,num3,num4))
print("The HCF of", num1,"and", num2,num3,"and", num4,"is", hcf(num1,num2,num3,num4))
