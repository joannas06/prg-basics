array = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

def names(x):
    result = []
    for i,j in x:
        result.append(f"{i.upper()}, {j}")
    return result
    
if __name__ == "__main__":
    print("\n".join(names(array)))