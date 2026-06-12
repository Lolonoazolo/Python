#expense tracker

expenses = [] # list of all expenses in form of dictionaries
print("Welcome to Expense Tracker")

while True:
    print("====menu====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice= int(input("Please Enter Your Choice:"))

#add expense
    if(choice==1):
        date=input("Kis date pe kharcha kiya :")
        category=input("kis type ka kharahcha kiya :")
        description =input ("Aur koi detai : ")
        amount =float(input("Kitna kharcha kiya;"))

        expense = {
            "date " : date ,
            "category" : category ,
            "description" : description ,
            "Amount" : amount
        }

        expenses.append(expense)
        print(" \n Expense added successfully")

    #view expense
    elif(choice==2):
      if (len(expenses)==0):
        print("\n No expenses added yet")
      else:
        print("==== Expenses ====")
        count=1
        for eachkharacha in expenses:
          print(f"kharcha number {count} -> {eachkharcha["date"]},{eachkharacha [category]} , {eachkharacha [description]}, {eachkharacha [amount]} ")
          count+=1

      #total expense
    elif (choice==3):
      total=0
      for eachkarcha in expenses:
       total = total + eachkarcha["amount"]
       print("\n Total Kharcha =" , total)

    # exit :
    elif (choice ==4):
      print("Thank you for using Expense Tracker")
      break

    else:
      print("Invalid choice. Please try again")