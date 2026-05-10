"""

Mallory Rich 
IS 303

Calculates shipping cost based on weight and destination zone

INPUTS
- weight
- destinamtion zone

PROCESSES
- Tiered pricing by weight (under 2 lbs, 2-10 lbs, over 10 lbs),
  multiplied by zone factor (local, regional, national)
- under 2 lbs ($5), 2-10 lbs ($8), 10+ lbs ($10)
- local (1x), regional (1.5x), national (2x)

OUTPUTS
- shipping cost
- weight
- destination zone

"""

#INPUTS
weight = float(input("How much does your package weigh? - "))
zone = input("Where are you sending your package? (local, regional, national) - ").lower()

#INPUT VALIDATION
is_valid = True

if weight < 0 or weight > 100:
      print("You have entered an invalid number. Please enter a number bewteen 0 and 100.")
      is_valid = False


#PROCESSES

if is_valid:
    if weight < 2:
        price = 5
    elif weight <= 10:
        price = 8
    elif weight > 10:
        price = 10
        

    if zone == "local":
            shipping = price * 1
    elif zone == "regional":
            shipping = price * 1.5
    elif zone == "national":
            shipping = price * 2
    else:
        print("You have entered an invalid input. Please enter local, regional, or national.")

    print(f"Your package weighs {weight} lbs. Your package is shipping {zone}. Your shipping cost is ${shipping}.")