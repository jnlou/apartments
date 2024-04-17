import random


# This is used for validation of the user sign-in/sign-up process
def sign_in(accounts, accounts_favs):
    while True:
        try:
            sign = input('Sign Up or Sign In?: ').capitalize().strip()

            if sign in ['Sign In', 'Sign-in', 'Sign in', 'Sign-In']:
                user = input('Enter user: ').capitalize().strip()
                pw = input('Enter password: ')
                for name, password in accounts.items():
                    if user == name and pw == password:
                        return user
                else:
                    print('User not found, try again')
                
            if sign in ['Sign Up', 'Sign-up', 'Sign Up', 'Sign up']:
                while True:
                    new_user = input('Enter user: ').capitalize().strip()
                    new_pw = input('Enter password: ').strip()
                    if new_user in accounts:
                        found = input('Account already found, wanna sign in? ("y" for yes, anything else for no): ').lower().strip()
                        if found == 'y':
                            break
                    else:
                        accounts[new_user] = new_pw
                        accounts_favs[new_user] = []
                        return new_user
        except ValueError as e:
            print(f'Value error occured: {e}')
            print('Try again')




# This is used for selecting a unit at random, inside of the user's "favorites" list.
# Which then, prompts the user to select whether "y" if they're interested in the unit and/or "f" if they would like to favorite the unit.
# Also an "exit" option to exit the menu altogether
def shop_fav(selected, apartments, accounts_favs, user):
    while True:
        if not accounts_favs[user]:
            print('You have nothing in your favorites')
            return selected
        # a list used to only contain all units in the user's favorites, that the user doesn't already have in their cart. 
        favs = [i for i in accounts_favs[user] if i not in selected]
        # If it's empty, this means every unit in the user's favorites list, is already in their shopping cart.
        # Thus, it will just return the shopping cart.
        if not favs:
            print("You've selected everything in your favorites")
            return selected
            
        # Chooses a unit inside the user's favorites list at random
        fav_unit = random.choice(favs)
        print(fav_unit)

        # Shows the information about the current chosen unit
        for desc, num in apartments[fav_unit].items():
            print(f'{desc}: {num}')
        
        # Would add a try block here, but since the line says "anything else" for no, it's not neccessarily required
        want_fav = input('Interested? ("y" for yes, "f" to unfavorite, anything else for no), or "exit" to exit: ').lower().strip()

        # The unit gets added to the user's shopping cart
        if want_fav == 'y':
            selected.append(fav_unit)
            print(f'{fav_unit} has been added to your shopping cart')
        
        elif want_fav == 'f':
            accounts_favs[user].remove(fav_unit)
            print(f'{fav_unit} has been removed from your favorites')
            
        elif want_fav == 'exit':
            return selected    


def shop_all(selected, user_preference, apartments, accounts_favs, user):
                while True:
                    filtered_units = [i for i in user_preference if i not in selected]
                    if not filtered_units:
                        print("You've selected all available units")
                        return selected
                    chosen_unit = random.choice(filtered_units)
                    print(chosen_unit)

                    for category, digit in apartments[chosen_unit].items():
                        print(f'{category}: {digit}')
                    while True:
                        try:
                            want_unit = input('Interested? ("y" for yes, "f" to favorite, anything else for no), or "exit" to exit: ').lower().strip()

                            if want_unit == 'y':
                                selected.append(chosen_unit)
                                print(f'{chosen_unit} is now added to your cart.')
                                break
                            
                            elif want_unit == 'exit':
                                return selected
                            
                            if want_unit == 'f' and chosen_unit not in accounts_favs[user]:
                                accounts_favs[user].append(chosen_unit)
                                print(f'{chosen_unit} is now added to your favorites.')
                            else:
                                print('This unit is already in your favorites.')

                            if want_unit not in ['y', 'exit', 'f']:
                                break
                        except ValueError as err:
                            print(f"Value error occured: {err}, try again")


# This is used to display what's in the user's shopping cart.
# It then, displays three options: Select a particular unit in their shopping cart, go back to the previous menu to potentially add more units, or checkout.
#

def shop_cart(selected, apartments):
    while True:
        try:
            print(f'Shopping Cart: {", ".join(selected)}')

            print('1: Select unit ')
            print('2: Add more units')
            print('3: Checkout')
            option = int(input('Enter one of the numbers above: ').strip())
            if option not in [1,2,3]:
                print('Numbers must be either 1, 2, or 3')

            if option == 1:
                selected_unit = input('Enter unit: ').strip().title()
                print(f'You chose: {selected_unit}')
                for types, number in apartments[selected_unit].items():
                    print(f'{types}: {number}')

                while True:
                    print('1: Delete from shopping cart')
                    print('2: Go back')
                    select = int(input('Enter one of the numbers above: ').strip())
                    if select not in [1,2]:
                        print('Numbers must be either 1 or 2')
                    
                    if select == 1:
                        selected.remove(selected_unit)
                        break
                    
                    else:
                        break
            if option == 2:
                return selected, False

            if option == 3:
                return selected, True

        except ValueError as e:
            print(f'Error occured, try again: {e}')



def price_processing(select, selected, limits, apartments):
    while True:
        try:
            price = float(input('Set a highest price or 0 to go back: ').strip())
            if price >= min([price_info.get('Price') for price_info in apartments.values()]):
                    limits['Price'] = price
                    selected.append(select)
                    return selected, limits

            elif price == 0:
                return selected, limits

            else:
                price_again = input("Your desired price option is too low for any apartment options, would you like to try again? ('y' for yes, anything else for no): ").strip().lower()
                if price_again != 'y':
                    return selected, limits

        except ValueError as price_err:
            print(f"Value error occured: {price_err}, try again")


def sq_ft_processing(select, selected, limits, apartments):
    while True:
        try:
            sq_ft = int(input('Set highest square feet or 0 to go back: ').strip())
            if sq_ft >= min([ft_info.get('Sq Ft') for ft_info in apartments.values()]):
                    limits['Sq Ft'] = sq_ft
                    selected.append(select)
                    return selected, limits

            elif sq_ft == 0:
                return selected, limits
            else:
                sq_again = input("Your desired square feet option is too low for any apartment options, would you like to try again? ('y' for yes, anything else for no): ").strip().lower()
                if sq_again != 'y':
                    return selected, limits

        except ValueError as sq_err:
            print(f"Value error occured: {sq_err}, try again")



def bedroom_processing(select, selected, limits, apartments):
    while True:
        try:
            bedrooms = int(input('Set highest number of bedrooms or 0 to go back: ').strip())
            if bedrooms >= min([bed_info.get('Sq Ft') for bed_info in apartments.values()]):
                limits['Bedrooms'] = bedrooms
                selected.append(select)
                return selected, limits

            elif bedrooms == 0:
                return selected, limits

            else:
                bed_again = input("Your desired square feet option is too low for any apartment options, would you like to try again? ('y' for yes, anything else for no): ").strip().lower()
                if bed_again != 'y':
                    return selected, limits

        except ValueError as bed_err:
            print(f"Value error occured: {bed_err}, try again")


def bathroom_processing(select, selected, limits, apartments):
    while True:
        try:
            bathrooms = int(input('Set highest number of bathrooms or 0 to go back: ').strip())
            if bathrooms >= min([bath_info.get('Sq Ft') for bath_info in apartments.values()]):
                limits['Bathrooms'] = bathrooms
                selected.append(select)
                return selected, limits

            elif bathrooms == 0:
                return selected, limits    

            else:
                bath_again = input("Your desired square feet option is too low for any apartment options, would you like to try again? ('y' for yes, anything else for no): ").strip().lower()
                if bath_again != 'y':
                    return selected, limits

        except ValueError as bath_err:
            print(f"Value error occured: {bath_err}, try again")


# This function is in charge of filtering every apartment according to limits the user sets in each category
def filtering(apartments, user):
    print(f'Hello {user}!')
    filter_by = ['Price', 'Sq Ft', 'Bedrooms', 'Bathrooms']
    selected = []
    limits = {}
    while True:
        try:
            print(f'{", ".join([i for i in filter_by if i not in selected])}')
            select = input('What would you like to filter by?, or type "None" to continue: ').title().strip()
            if select not in selected:
                if select == 'Price':
                   selected, limits = price_processing(select, selected, limits, apartments)

                elif select == 'Sq Ft':
                   selected, limits = sq_ft_processing(select, selected, limits, apartments)

                elif select == 'Bedrooms':
                    selected, limits = bedroom_processing(select, selected, limits, apartments)

                    
                elif select == 'Bathrooms':
                    selected, limits = bathroom_processing(select, selected, limits, apartments)

            else:
                removal = input('Already selected, would you like to remove this option? ("y" for yes, anything else for no): ').lower().strip()
                if removal == 'y':
                    selected.remove(select)

            
            
            if select == 'None' or len(selected) == len(filter_by):
                break

        except ValueError as e:
            print(f'Value error: {e}, try again')

    filtered_apartments = {}
    for unit, desc in apartments.items():
        if all(desc[i] <= limits[i] for i in limits):
            filtered_apartments[unit] = desc
    return filtered_apartments


# The purpose of this function is to provide a text-based UI which displays available options to decide from
def shopping(cart, apartments, user, user_preference, accounts_favs, saved_data):
        while True:
            print(f'Shopping Cart: {cart if cart else "Empty"}')
            print(f'Favorites: {accounts_favs[user]}')
            shop = input('Shop All, Shop Favorites, see Shopping Cart, Checkout, Refilter your preferences, Sign Out?: ').title().strip()
            
            if shop in ['Shop Favorites', 'Favorites']:
                cart = shop_fav(cart, apartments, accounts_favs, user)
                
            
            elif shop in ['Shop All', 'All']:
                    cart = shop_all(cart, user_preference, apartments, accounts_favs, user)

            elif shop in ['Shopping Cart', 'Cart']:
                if not cart:
                    print('You have nothing in your cart.')
                else:
                    # New variable "checkout", used to check if the user decides to checkout directly from the shopping cart
                    cart, checkout = shop_cart(cart, apartments)
                    if checkout:
                        return cart


            elif shop == 'Refilter':
                user_preference = filtering(apartments, user) 

            elif shop == 'Sign Out':
                save_data(user, user_preference, accounts_favs, cart, saved_data)
                # Used as an indicator so the program knows the user is deciding to sign out
                return None
            elif shop == 'Checkout':
                return cart

            else:
                print("Please select one of the displayed options")


# This functions sends the all of the user's information as a dictionary, into a dictionary named "saved_data"
def save_data(user, user_preference, accounts_favs, selected, saved_data):
    user_data = {f"{user}'s Information" : {"Apartment Preferences" : user_preference,
                                            "Favorites" : accounts_favs[user],
                                            "Shopping Cart" : selected}
                }
    saved_data[user] = user_data
    
# This function loads an already saved portion of the dictionary that contains the user's informational data
def load_data(user, saved_data):
    # returns the user's apartment preferences, and their shopping cart
    return saved_data[user][f"{user}'s Information"]["Apartment Preferences"], saved_data[user][f"{user}'s Information"]["Shopping Cart"]
