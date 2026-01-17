# This does the exact same thing as your function above
array = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

names = lambda x: [f"{i.upper()}, {j}" for i, j in x]

print("\n".join(names(array)))