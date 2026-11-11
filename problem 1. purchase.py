#problem 1


name = input("Enter Customer Name: ")
purchase = int(input("Purchase amount: "))
premium = input("Are you a premium member? (yes/no) ").strip().lower()
final = ""

if purchase <= 0:
    print ("Invalid Purchase Amount")
else:
    if purchase >= 500:
        
        discount = 20
        if premium == "yes" :
            discount += 5 
        discount_cal = (discount / 100)
        discount_amount = purchase * discount_cal
        final = purchase - discount_amount
    elif purchase >= 300:
        discount = 15
        if premium == "yes" :
            discount += 5
        discount_cal = (discount / 100)
        discount_amount = purchase * discount_cal
        final = purchase - discount_amount
    elif purchase >= 100:
        discount = 10
        if premium == "yes" :
            discount += 5 
        discount_cal = (discount / 100)
        discount_amount = purchase * discount_cal
        final = purchase - discount_amount
    else:
        discount = 0
        if premium == "yes" :
            discount += 5 
        discount_cal = (discount / 100)
        discount_amount = purchase * discount_cal
        final = purchase - discount_amount

    print ("\n             RESULTS              \n")
    print (f"Original Amount: ${purchase}")
    print (f"Discount: {discount}%")
    print (f"Discount Amount: ${discount_amount}")
    print (f"Final Amount: ${final}\n")
    if premium == "yes" and purchase >= 500 :
        print ("You are eligible for VIP benefits!\n")
            
    print ("               END               ")    

        
            
