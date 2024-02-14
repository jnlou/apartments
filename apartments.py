import apartment_ops
apartments = {'Unit 1': {'Price': 950,
                         'Sq Ft': 900,
                         'Bedrooms': 1,
                         'Bathrooms': 1},
              'Unit 2': {'Price' : 1000,
                         'Sq Ft' : 1100,
                         'Bedrooms' : 1,
                         'Bathrooms' : 1.5},
              'Unit 3': {'Price' : 1100,
                         'Sq Ft': 1200,
                         'Bedrooms': 2,
                         'Bathrooms': 2},
              'Unit 4': {'Price' : 1200,
                         'Sq Ft' : 1300,
                         'Bedrooms' : 2,
                         'Bathrooms' : 2},
              'Unit 5': {'Price' : 1400,
                         'Sq Ft' : 1350,
                         'Bedrooms' : 2,
                         'Bathrooms' : 2.5},
              'Unit 6': {'Price' : 1600,
                         'Sq Ft' : 1450,
                         'Bedrooms' : 3,
                         'Bathrooms' : 3}
              }


accounts = {'James': 'james1',
            'Jodie' : 'jodie101'}

accounts_favs = {'James': ['Unit 1', 'Unit 3', 'Unit 6'],
                 'Jodie' : ['Unit 4']}


saved_data = {'James' : {},
              'Jodie' : {}}
def main():
    
    while True:
        user = apartment_ops.sign_in(accounts, accounts_favs)
        # Meaning, if the user doesn't exist or if the user doesn't have any data to load
        if user not in accounts or not saved_data[user]:
            user_preference = apartment_ops.filtering(apartments, user)
            # Creates an empty shopping cart
            cart = []
            # Updates the shopping cart
            cart = apartment_ops.shopping(cart, apartments, user, user_preference, accounts_favs, saved_data)
        

        else:
            user_preference, cart = apartment_ops.load_data(user, saved_data)
            # Updates the shopping cart
            cart = apartment_ops.shopping(cart, apartments, user, user_preference, accounts_favs, saved_data)

        if cart is not None:
            break
    print(f'Your request has been sent to {len(cart)} apartment complexes')
    print('Thanks for shopping!')

if __name__ == "__main__":
    main()


