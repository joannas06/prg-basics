###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a_string = input('a=')
a = int(a_string)
b_string = input('b=')
b = int(b_string)
c_string = input('c=')
c = int(c_string)

volume = a*b*c
surface_area = 2*a*(b+c)

print(f'The volume of the cuboid is {volume}')
print(f'The surface area of the cuboid is {surface_area}')
