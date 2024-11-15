# calculate the total amount paid
def amount(bill_amount,tips_perc):
    '''this function will help calculate the amount paid including the tip'''
    total= bill_amount*(1+0.01*tips_perc)
    total= round(total,2)
    print(f"the total amount paid is ${total}")
print(amount.__doc__)
amount(150,20)
