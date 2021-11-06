import csv
import random
myMenu = []

# Code Snippet to read Menu.csv file and store it into datastructure.
# It prints the menu too.
with open('Menu.csv', newline='') as menu:
    filereader = csv.reader(menu, delimiter=',', quotechar='|')
    print("Item No    Half Plate    Full Plate")
    count = 0
    for i in filereader:
        count += 1
        if count == 1:
            myMenu.append(i)
            continue
        print('            '.join(i))
        myMenu.append(i)


print("Enter your order details")
print("Enter in the following format")
print("Item No, half for half plate and full for full plate and quantity")
print("Enter plate details in comma separeted values and | for next plate")
order = input("Enter order\n")
print("If you would like to pay tip")
print("0, 10% and 20%")
tip = input("Enter tip percentage: ")

# Splitting order based on delimitter '|'.
order_arr = order.split('|')
total_bill = 0
mydict = {}

# Calculating total bill based on input from user.
for i in range(0, len(order_arr)):
    plate = order_arr[i].split(' ')
    item_no = int(plate[0])
    if plate[1] == "half":
    	isHalf = True
    else:
	    isHalf = False
    quantity = int(plate[2])

    pair = ()
    if isHalf:
	    pair = (item_no, "Half")
    else:
	    pair = (item_no, "Full")
	    
    prev_quant = 0	    
    if pair in mydict.keys():
	    prev_quant = mydict.get(pair)
	    prev_quant += quantity
	    mydict.update({pair: prev_quant})
    else:
    	    mydict[pair] = quantity
    #print(mydict.values())

    if(isHalf):
        total_bill += int(myMenu[item_no][1]) * quantity
    else:
        total_bill += int(myMenu[item_no][2]) * quantity


total_bill += (total_bill) * (int(tip)/100)
print("Please pay " + (str("{0:.2f}".format(total_bill))) + "Rs")
intermediate_bill = total_bill

no_of_people = input("Enter number of people: ")
bill_share = total_bill / (int(no_of_people))
print("Bill per person is " + (str("{0:.2f}".format(bill_share))))

print("You have a chance to get more discount")
print("Note that there is 50% chance that the bill amount increases by 20%")
would_participate = input(
    "Would you like to participate in out 'Test your luck' event? Enter YES or NO: ")

# If user participates in the event, then it will get executed

if(would_participate == "YES"):

    discount = 0
    increment = 0
    chance = random.randint(1, 100)
    if 1 <= chance and chance <= 5:
        discount = 50
    elif 6 <= chance and chance <= 15:
        discount = 25
    elif 16 <= chance and chance <= 30:
        discount = 10
    elif 31 <= chance and chance <= 80:
        increment = 20
    elif 81 <= chance and chance <= 100:
        dicount = 0

    # Damn, Bill will get incremented.
    if increment != 0:
        total_bill += (total_bill) * (increment/100)
        print("Sorry, The bill increased by " + str((total_bill*increment)/100))

        print(" ",end="")
        for i in range(0, 4):
            print("*", end="")
        print("")
        for i in range(0, 4):
            print("*    *") 
        print(" ",end="")
        for i in range(0, 4):
            print("*", end="")

    # Wow, Bill will get decremented
    elif discount != 0:
        total_bill -= (total_bill) * (discount/100)
        print("Congratulations, You got a discount of " +
              str((total_bill*discount)/100))
	
        print(" ",end="")
        for i in range(0, 4):
            print("*", end="")
        for i in range(0, 6):
            print(" ", end="")
        print("  ",end="")
        for i in range(0, 4):
            print("*", end="")

        print("")
        for i in range(0, 3):
            print("|    |", end="")
            for j in range(0, 6):
                print(" ", end="")
            print("|    |", end="")
            print("")
	
        print(" ",end="")
        for j in range(0, 4):
            print("*", end="")
        for j in range(0, 6):
            print(" ", end="")
        print("  ",end="")
        for j in range(0, 4):
            print("*", end="")

        print("")
        print("")
        print("        {}")
        print("")
        print("      ______")
    else:
        print("Neutral, The bill neither increased not decreased")
else:
	discount=0
	increment=0
print("")

# printing Bill
print("Bill Breakdown")
print("------------------------------------")
total_bill = 0
for items, half in mydict:
    pair = (items, half)
    quantity = mydict[pair]
    item_no = items
    isHalf = half

    print("Item "+str(item_no), end="")
    if(isHalf == "Half"):
        print(" [Half]"+"["+str(quantity)+"]: " +
              str("{0:.2f}".format(int(myMenu[item_no][1]) * quantity)))
        total_bill += int(myMenu[item_no][1]) * quantity
    else:
        print(" [Full]"+"["+str(quantity)+"]: " +
              str("{0:.2f}".format(int(myMenu[item_no][2]) * quantity)))
        total_bill += int(myMenu[item_no][2]) * quantity

print("Total: "+str("{0:.2f}".format(total_bill)))
print("Tip Percentage: "+str(tip)+"%")
if(discount != 0):
    print("Discount/Increase: -" + 
          str("{0:.2f}".format(intermediate_bill-total_bill)))
    temp = intermediate_bill-(intermediate_bill*discount)/100
    print("Final Total: " +
          str("{0:.2f}".format(intermediate_bill-(intermediate_bill*discount)/100)))
    print("Each person has to contibute: " +
          str("{0:.2f}".format(int(temp)/int(no_of_people))))

elif(increment != 0):
    print("Discount/Increase: +" + 
          str("{0:.2f}".format(intermediate_bill-total_bill)))
    temp = intermediate_bill+(intermediate_bill*increment)/100
    print("Final Total: " +
          str("{0:.2f}".format(intermediate_bill+(intermediate_bill*increment)/100)))
    print("Each person has to contibute: " +
          str("{0:.2f}".format(int(temp)/int(no_of_people))))
else:
    temp = intermediate_bill+(intermediate_bill*increment)/100
    print("Discount/Increase: " + "0.00")
    print("Final Total: " +
          str("{0:.2f}".format(intermediate_bill+(intermediate_bill*increment)/100)))
    print("Each person has to contibute: " +
          str("{0:.2f}".format(int(temp)/int(no_of_people))))
print("------------------------------------")
