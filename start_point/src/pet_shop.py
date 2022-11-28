# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(input_petshop):
    return input_petshop ["name"]

def get_total_cash(input_cash):
    return input_cash ["admin"]["total_cash"]

def add_or_remove_cash(input_petshop, number): # for tests 3 and 4 
    input_petshop["admin"]["total_cash"] += number

def get_pets_sold(input_petshop):
    return input_petshop["admin"]["pets_sold"]

def increase_pets_sold(input_petshop, number):
    input_petshop["admin"]["pets_sold"] += number

def get_stock_count(input_petshop):
    return len(input_petshop["pets"])
        
def get_pets_by_breed(petshop,breed): # for tests 8 and 9
    given_breed = []
    for pet in petshop["pets"]:
        if pet["breed"] == breed:
            given_breed.append(pet)
    return given_breed

def find_pet_by_name(petshop, pet_name): # for tests 10, 11
    for pet in petshop["pets"]:
        if pet["name"] == pet_name:
            return pet
        
    return None

def remove_pet_by_name(petshop, pet_name): # for test 12
    pet_to_remove = find_pet_by_name(petshop, pet_name)
    petshop["pets"].remove(pet_to_remove)

def add_pet_to_stock (petshop, new_pet):
    petshop["pets"].append(new_pet)

def get_customer_cash(customers):  
    return customers["cash"]

def remove_customer_cash (customer, value):
    customer["cash"] = customer["cash"] - value

def get_customer_pet_count (customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)
    
def customer_can_afford_pet(customer, new_pet): # for optional tests x3
    customer_cash = get_customer_cash(customer)
    if customer_cash >= new_pet["price"]:
            return True
    
    return False


# def test_sell_pet_to_customer__pet_found(self):   
#     customer = self.customers[0]                            # will pull in Alice
#     pet = find_pet_by_name(self.cc_pet_shop,"Arthur")       # to find Arthur

#     sell_pet_to_customer(self.cc_pet_shop, pet, customer)

#     self.assertEqual(1, get_customer_pet_count(customer))
#     self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
#     self.assertEqual(100, get_customer_cash(customer))
#     self.assertEqual(1900, get_total_cash(self.cc_pet_shop))

def sell_pet_to_customer (petshop, pet, customer):
    pet = find_pet_by_name(petshop, pet)

    pet_count = get_customer_pet_count (customer) # failing 1 != 0 
    pets_sold = get_pets_sold (petshop)
    customer_cash = get_customer_cash(customer)
    total_cash = get_total_cash (petshop)
    
    return pet_count, pets_sold, customer_cash, total_cash