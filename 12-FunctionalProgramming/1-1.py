###
# Calculates arithmetic mean of two integer numbers
#
def mean(x,y):
   srednia = (x+y)/2
   return srednia

# takes two numbers from keyboard
n1 = int(input("Enter x: "))
n2 = int(input("Enter y: "))

# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f'The arithmetic mean of the numbers {n1} and {n2} is {result}')