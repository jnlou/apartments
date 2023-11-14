import random

def sign_in(accounts, accounts_fav):
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
                    break
                
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
                        accounts_fav[new_user] = []
                        return new_user
        except ValueError as e:
            print(f'Value error occured: {e}')
            print('Try again')


def shopping(apartments, user, user_preference, account_favs):
        selected = []
        while True:
            print(f'Shopping Cart: {selected}')
            print(f'Favorites: {account_favs[user]}')
            shop = input('Shop All, Shop Favorites, see Shopping Cart, or Sign Out?: ').title().strip()
            if shop == 'Shop Favorites':
                while True:
                    if not account_favs[user]:
                        print('You have nothing in your favorites')
                        break
                    favs = [i for i in account_favs[user] if i not in selected]
                    if not favs:
                        print("You've selected everything in your favorites")
                        break
                    fav_unit = random.choice(favs)
                    print(fav_unit)

                    for desc, num in apartments[fav_unit].items():
                        print(f'{desc}: {num}')
                    want_fav = input('Buy? ("y" for yes, anything else for no), or "exit" to exit: ').lower().strip()

                    if want_fav == 'y':
                        selected.append(fav_unit)
                        favs.remove(fav_unit)
                        print(f'{fav_unit} has been added to your shopping cart')

                    elif want_fav == 'exit':
                        break
            
            if shop == 'Shop All':
                # Meaning the user picked 'Shop All' or the length of their favorites list is empty
                while True:
                    filtered_units = [i for i in user_preference if i not in selected]
                    if not filtered_units:
                        print("You've selected all available units")
                        break
                    chosen_unit = random.choice(filtered_units)
                    print(chosen_unit)

                    for category, digit in apartments[chosen_unit].items():
                        print(f'{category}: {digit}')
                    want_unit = input('Interested? ("y" for yes, anything else for no), or "exit" to exit: ').lower().strip()

                    if want_unit == 'y':
                        selected.append(chosen_unit)

                    elif want_unit == 'exit':
                        break

            if shop == 'Shopping Cart':
                while True:
                    try:
                        if not selected:
                            print('You have nothing in your cart.')
                            break
                        print(selected)
                        print('1: Select unit ')
                        print('2: Add more units')
                        print('3: Checkout')
                        option = int(input('Enter one of the numbers above: ').strip())
                        if option not in [1,2,3]:
                            print('Numbers must be either 1, 2, or 3')

                        if option == 1:
                            selected_unit = input('Enter unit: ').strip().title()
                            print(selected_unit)
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
                            break

                        if option == 3:
                            return selected
                    except ValueError as e:
                        print(f'Error occured, try again: {e}')
            if shop == 'Sign Out':
                return None




    
    
    



    

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
                selected.append(select)
            else:
                removal = input('Already selected, would you like to remove this option? ("y" for yes, anything else for no): ').lower().strip()
                if removal == 'y':
                    selected.remove(select)
            if select == 'Price':
                price = float(input('Set a highest price: ').strip())
                limits['Price'] = price
                
            elif select == 'Sq Ft':
                sq_ft = int(input('Set highest square feet: ').strip())
                limits['Sq Ft'] = sq_ft

            elif select == 'Bedrooms':
                bedrooms = int(input('Set highest number of bedrooms: ').strip())
                limits['Bedrooms'] = bedrooms
            
            elif select == 'Bathrooms':
                bathrooms = int(input('Set highest number of bathrooms: ').strip())
                limits['Bathrooms'] = bathrooms
            
            if select == 'None' or len(selected) == 4:
                break

        except Exception as e:
            print(f'Value error: {e}, try again')
    filtered_apartments = {}
    for unit, desc in apartments.items():
        if all(desc[i] <= limits[i] for i in limits):
            filtered_apartments[unit] = desc
    return filtered_apartments
