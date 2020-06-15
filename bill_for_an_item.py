quant=int(input("enter the quantity sold="))
val=int(input("enter the value of item="))
dis=int(input("enter the discount percentage="))
tax=int(input("enter the tax percentage="))
total_amount=quant*val
dis_amt=(total_amount*dis)/100
after_dis=total_amount-dis_amt
tax_amt=(after_dis*tax)/100
after_tax=after_dis+tax_amt
print("\n")
print("********bill********")
print("Quantity Sold: \t\t"+str(quant))
print("val of item: \t\t"+str(val))
print("\t\t -----------")
print("Amount: \t\t"+str(total_amount))
print("Discount:\t\t"+"-"+str(dis_amt))
print("\t\t -----------")
print("Discounted amount: \t" +str(after_dis))
print("Tax: \t\t\t"+"+"+str(tax_amt))
print("\t\t -----------")
print("Total Amount To Be Paid:"+str(after_tax))
      
