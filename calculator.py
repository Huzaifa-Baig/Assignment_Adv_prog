#gal is gallon
#ba1r is barrell
#the purpose of this program is to calculate the carbon footprint
gal = int (input("please insert here the relevant number of gasoline:"))
print("The first number of gallons of gasoline is:")
litre = float(gal*5.9)
bar= float(gal/9.5)
petrol = float(gal*25.7)
price = float(gal*6.8)

print (gal, "gal is equal to", litre,"litre")
print(gal, "gal of gas needs", bar,"bar of oil")
print(gal,"gal of gas produces", petrol,"pounds of carbon dioxide")
print(gal," gal of gas needs",price,"euro")
print("Thank you for participating")
