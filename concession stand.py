#tasting dictionaries

import time

offers = {"cotton candy": 5,
          "heart balloon": 10,
          "bubble blower": 3
          }

bill = 0
reciept = []

print("here's all our items:")

for food, price in offers.items():
    print(f"{food:20} : ${price:.2f}")

while True:
    order = input("""--------------------
what would you like to order? (q for quit) """).strip().lower()
    if order == "q":
        break
    else:
        reciept.append(order)
        bill += offers.get(order)

print(f"""-------------BILL---------------
you ordered {reciept} for a total of ${bill}""")