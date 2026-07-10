#shopping cart program

food = []
toys = []

category = input("what do you wanna shop for? (food/toys) ").strip().lower()

while True:
    if category == "food":
        item = input("what are you craving? (q for quit) ")
        if not item == "q":
            food.append(item)
        else:
            print(f"you have ordered:")
            for x in food:
                print(x, end=" 😎 ")
            break
    elif category == "toys":
        item = input("what do you wanna play with? (q to quit) ")

        if item == "q":
            print(f"you have ordered these toys:")
            for x in toys:
                print(x, end=" 😎 ")
            break
        else:
            toys.append(item)
    else:
        break
