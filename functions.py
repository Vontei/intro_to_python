
# Reverse a String with slice syntax

myName = 'Nick'
print myName[::-1]


# Reverse a String with a function

print "".join(myName[c] for c in xrange(len(myName) - 1, -1, -1))



# while loop
num = 0
while (num < 20):
   print 'The count is:',num
   num+=1

print "BYE"


# for loops, are for in


for thing in 'this long string':
   print 'Current Character is :', thing

fruitsArray = ['banana', 'apple',  'mango']
for fruit in fruitsArray:
   print 'Current fruit is:', fruit

print "BAI"



# More complex
# code sample taken for prime numbers

for num in range(10,20):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
