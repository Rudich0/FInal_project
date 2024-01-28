def pizza():
    while True:
        try:
            amount_pizza=int(input("How many pizza do you want:"))
            if amount_pizza > 0:
                total_price=amount_pizza*12
                return amount_pizza, total_price
            else:
                print("Please enter a positive integer.")
        except TypeError:
            print("Please enter a positive integer!")
        except ValueError:
            print("Please enter a number!")
        except:
            print("Invalit responce Please try again")

def day_discount(total_price):
       while True:
        day= input("Is it Tuesday? ")
        if day.lower()== "y" or day.lower()== "yes":
            total_price=total_price-(total_price*0.5)
            return total_price,total_price*0.5
        elif day.lower()== "n" or day.lower()== "no":
            return total_price,0
        else:
            print("Please enter (Y/N)")
    
    
def app_discount(total_price):
    while True:
        app= str(input("Did the customer use the app? "))
        if app.lower()=="y" or app.lower()=="yes":
            total_price=total_price-(total_price*0.25)
            return total_price,total_price*0.25
        elif app.lower()=="n" or app.lower()=="no":
            return total_price,0
        else:
            print("Please enter (Y/N)")
    
def delivery(total_price,amount_pizza):
    while True:
        delivery=(input("Is delivery required? "))
        if delivery.lower()=="y" or delivery.lower()=="yes":
            if amount_pizza<= 5:
                total_price=total_price+2.50
                return total_price,2.50
            else:
                return total_price,0
        elif delivery.lower()=="n" or delivery.lower()=="no":
            return total_price,0
        else:
            print("Please enter (Y/N)")

def print_price(final_price,discount_app,discount_day,discount_delivery,amount,price):
    print("BPP Pizza Price Calculator")
    print("=================================================================")
    print(f"Pizza                              :£{amount}")
    print(f"Price of {amount} pizzz                   :£{price}")
    print(f"App Discount                       :£{discount_app}")
    print(f"Tuseday Discount                   :£{discount_day}")
    print("==================================================================")
    print(f"Dilivery Discount(only if 5 or more pizzas):£{discount_delivery}")
    print("==================================================================")
    print(f"Final prize:                       :£{final_price}")




amount,price=pizza()
delivery_price,discount_delivery=delivery(price,amount)
tuseday_price,discount_day=day_discount(delivery_price)
total_price,discount_app=app_discount(tuseday_price)
rounded_price = round(total_price, 2)
print_price(rounded_price,discount_app,discount_day,discount_delivery,amount,price)
