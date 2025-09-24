import numpy as np
import pandas as pd
df = pd.DataFrame(columns=['Stock', 'Panels'])
cars = []
# user inputs stock neumber 
def stock_recieve():
    print("Enter stock number:")
    user_stock = input()
    return user_stock

# user inputs panels
def panels_recieve():
    print("Enter Panels:")
    user_panels = input()
    return user_panels

def combine_inputs(stock_number, panels):
    car = np.array([[stock_number, panels]])
    cr = pd.DataFrame(car, columns=['Stock', 'Panels'])
    return cr
def main():
    stock_number = stock_recieve()
    print("Entered stock number:", stock_number)
    panels = panels_recieve()
    print("Entered panels:", panels)
    car_df = combine_inputs(stock_number, panels)
    print("Current entry:")
    print(car_df)
    cars.append(car_df)

print("Add operations? (y/n)")
while True:
    choice = input().lower()
    if choice == 'y':
        main()
        # Print the growing list after each addition
        if cars:
            all_cars_df = pd.concat(cars, ignore_index=True)
            print("All cars entered so far:")
            print(all_cars_df)
        else:
            print("No cars were entered yet.")
    elif choice == 'n':
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

# Final summary after exiting loop
if cars:
    all_cars_df = pd.concat(cars, ignore_index=True)
    print("All cars entered:")
    print(all_cars_df)
else:
    print("No cars were entered.")