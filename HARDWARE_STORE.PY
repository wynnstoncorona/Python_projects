def main():
    print('Welcome to Estes Parts!')
    while True:
        print('Please make a selection from the menu below.')
        print('_' * 25)
        print('1. Sales and Returns')
        print('2. Inventory Managment')
        print('3. Exit')
        print('_' * 25)
        choice = getInt('Selection: ')
        if choice == 1:
            menu1()
        elif choice == 2:
            menu2()
        elif choice == 3:
            print('Program exiting...')
            break
        else:
            print('Please enter a valid entry.')

def menu2():
    while True:
        print('Inventory Managment')
        print('_' * 25)
        print('1. Add Item')
        print('2. Remove Item')
        print('3. Display All Items')
        print('4. Return to previous menu')
        print('_' * 25)
        choice = getInt('Selection: ')
        if choice == 1:
            addItem()
        elif choice == 2:
            deleteItems()
        elif choice == 3:
            displayItems()
        elif choice == 4:
            break
        else:
            print('Please enter a valid entry.')

def menu1():
    while True:
        print('Sales and Returns')
        print('_' * 25)
        print('1. Process Sale')
        print('2. Process Return')
        print('3. Return to previous menu')
        print('_' * 25)
        choice = getInt('Selection: ')
        if choice == 1:
            sale()
        elif choice == 2:
            refund()
        elif choice == 3:
            break
        else:
            print('Please enter a valid entry.')

def addItem():
    with open("inventory.txt", "r+") as f:
        lines = f.readlines()
        name = input('What is the items name: ').lower()
        for line in lines:
            if line.startswith(name):
                print('That item already exsists')
                return None
        while True:
            try:
                price = float(input('what is the items price: '))
                break
            except ValueError:
                print('Invalid entry please try again')
            
        qty = getInt('What is the quantity: ')

        string = f"{name},{qty},{price}\n"

        f.write(string)

    
    print(f'{name} was added successfully!')

def deleteItems():
   while True:
        target = input('Item you would like to remove?: ').lower()
        with open("inventory.txt", "r+") as f:
            lines = f.readlines()
            search = False
            f.seek(0)
            for line in lines:
                if not line.startswith(target):
                    f.write(line)
                else:
                    search = True
                f.truncate()
            if search is True:
                print('Entry deleted')
                break
            else:
                print('That item is not in the system')
                return None
                
def displayItems():
    print('Items in Inventory')
    print('_' * 25)
    with open('inventory.txt', 'r+') as f: 
        for i in f:
            item = i.strip().split(',')
            name = item[0]
            qty = item[1]
            price = item[2]
            print(f'{name}, Qty {qty}, Price ${price}')

    print('_' * 25)

def sale():
    while True:
        print('Process Sale')
        print('Select an item from the options below')
        print('_' * 25)
        with open("inventory.txt", 'r+') as f:
            for i, line in enumerate(f, start=1):
                words=line.replace(','," ").split()
                print(f'{i} = {words[0]}', end='\n')
        print('0 = Retun to previous menu')
        print('_' * 25)
        item = getInt('Selection: ')
        if item == 0:
            break
        elif item > i or item < 1:
            print('Enter a number shown for a product')
        else:
            with open("inventory.txt", 'r+') as f:
                shop = []
                for line in f:
                    finalItem = line.strip().split(',')
                    shop.append(finalItem)
            target = shop[item-1]  
            name = target[0]
            price = target[2] 
            quantity = target[1] 
            while True:
                amount = getInt('How many would you like to buy?: ')
                if amount > int(quantity):
                    print('We dont have that many sorry')
                elif amount == 0:
                    break
                else:
                    total = amount * float(price)
                    target[1] = str(int(quantity) - amount)
                    finalShop= []
                    for Item in shop:
                        if Item[1] == str(0):
                            continue
                        finalShop.append(','.join(Item))

                    with open("inventory.txt", 'w') as f:
                       for item in finalShop:
                            f.write((str( item)))
                            f.write(' \n')
                    print(f'You purchased {amount} {name} at ${price} each for a total of ${total}')
                    return None

def refund():
    while True:
        print('Process Return')
        print('Select an item from the options below')
        print('_' * 25)
        with open("inventory.txt", 'r+') as f:
            for i, line in enumerate(f, start=1):
                words=line.split(",")
                print(f'{i} = {words[0]}', end='\n')
            print('0 = Retun to previous menu')
            print('_' * 25)
            choice = getInt('Selection: ')
            if choice == 0:
                break
            elif choice > i or choice < 1:
                print('Enter a number shown for a product')
            else:
                with open("inventory.txt", 'r+') as f:
                    shop = []
                    for line in f:
                        finalItem = line.strip().split(',')
                        shop.append(finalItem)
                target = shop[choice-1]  
                name = target[0]
                price = target[2] 
                quantity = target[1]
                while True:
                    amount = getInt('How many would you like to return?: ')
                    if amount == 0:
                        break
                    else:
                        total = amount * float(price)
                        target[1] = str(int(quantity) + amount)
                        finalShop= []
                        for Item in shop:
                            finalShop.append(','.join(Item))
                        with open("inventory.txt", 'w') as f:
                            for item in finalShop:
                                f.write((str( item)))
                                f.write(' \n')
                        print(f'You retuned {amount} {name} at ${price} each for a total refund of ${total}')
                        return None


def getInt(promt):
    while True:
        try:
            num =int(input(promt))
            return num
        except ValueError:
            print('Invalid entry please try again')
    

main()