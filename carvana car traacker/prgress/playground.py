import numpy as np
import pandas as pd

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
    print("Enteres stock number:", stock_number)
    panels = panels_recieve()
    print("Entered panels:", panels)
    df = combine_inputs(stock_number, panels)
    print(df)
    cars.append(df)
    return df

print("Add operations? (y/n)")
while True:
    choice = input().lower()
    if choice == 'y':
        main()
    elif choice == 'n':
        print("Exiting program.")
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")


print(cars)
#print(cr)

#print(df)





"""
##########################################################################################################################################################
print("Enter stock number:")
user_stock = input()
print("Enter Panels:")
user_panels = input()

# Define possible optiions
panel_options = ['Front bumber, Rear bumber', 'Hood', 'Roof', 'Lift gate', 'Driver Fender', 'Passenger Fender', 'Driver Front Door', 'Passenger Front Door', 'Driver Rear Door', 'Passenger Rear Door', 'Driver Quarter Panel', 'Passenger Quater Panel', 'Driver Mirror', 'Passenger Mirror', 'Driver Roof Rail', 'Padssenger Roof Rail', 'Driver Rocker Panel', 'Passenger Rocker Panel', 'finished']

while user_panels == panel_options & user_stock == '':




# Validate panels (allow multiple, comma-separated)
selected_panels = [p.strip() for p in user_panels.split(',')]
while not all(panel in panel_options for panel in selected_panels):
    print(f"Invalid panel(s). Choose one or more from: {', '.join(panel_options)}")
    user_panels = input()
    selected_panels = [p.strip() for p in user_panels.split(',')]

print(f"Selected stock: {user_stock}")
print(f"Selected panels: {selected_panels}")

# For labeling columns in a 2D array, use pandas DataFrame:

data = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(df)
"""