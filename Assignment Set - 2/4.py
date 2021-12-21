

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    delivery_charge = 0
    #write your logic here
    if(distance_in_kms<=0 or quantity_ordered <= 0 or (food_type!='V' and food_type!='N')):
        return -1
    if(distance_in_kms>3 and distance_in_kms<=6):
        delivery_charge = (distance_in_kms - 3) * 3
    elif(distance_in_kms>6):
        delivery_charge = (distance_in_kms - 6) * 6 + 9
    else:
        delivery_charge = 0
    if(food_type=='V'):
        bill_amount = 120 * quantity_ordered + delivery_charge
    else:
        bill_amount = 150 * quantity_ordered + delivery_charge
        
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)