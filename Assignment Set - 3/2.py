def calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity):
    price_dict = {gems_list[i]: price_list[i] for i in range(len(gems_list))}
    reqd_dict = {reqd_gems[i]: reqd_quantity[i] for i in range(len(reqd_gems))}

    try:
        bill = sum(price_dict[gem] * reqd_dict[gem] for gem in reqd_dict)
    except KeyError:
        return -1

    if bill > 30000:
        bill = 0.95*bill
    return bill


#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)  