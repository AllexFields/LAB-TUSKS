# Menu of a Shopping List

shopping_lst=['Grocery','Dairy','Snacks','Cereal','Household']
print(f"Shopping list is as follows: {shopping_lst}")
while True:
    print(f"Choose an option from below: \n1)Add \n2)Update \n3)Delete \n4)Search \n5)Exit")
    user_choice=int(input("Enter your choice from the menu above: "))
    
    match user_choice:
        case 1:
            add=input("What do you want to add? ").capitalize()
            shopping_lst.append(add)
            print(f"Congratulations!! {add} has been added to your shopping list.\nYour updated shopping list is as follows: \n---> {shopping_lst} <---")

        case 2:
            remove=input("Which item you want to update? --- ").capitalize()
            if remove in shopping_lst:
                remove=remove.capitalize()
                index=shopping_lst.index(remove)
                # print(index)
                shopping_lst.pop(index)
                update=input("What item you want to replace with? ---").capitalize()
                shopping_lst.insert(index,update)
                print(f"Congratulations!! {remove} has been removed from your shopping list. \nYour updated shopping list is as follows: ---> {shopping_lst} <---")
            else:
                print(f"Wrong item. It's not available in your shopping list.\n{shopping_lst}")
        case 3:
            delete=input("Which item you want to delete? --- ")
            delete=delete.capitalize()
            index=shopping_lst.index(delete)
            shopping_lst.pop(index)
            print(f"{delete} has been deleted.\nYour updated shopping list is as follows: \n---> {shopping_lst} <---")

        case 4:
            item=input("Enter the item name you want to search in shopping list: ")
            item=item.capitalize()
            if item in shopping_lst:
                print(f"Yess!! {item} is in your shopping list.")
            else:
                print(f"Ooops!! {item} is not in your shopping list.")
        case 5:
            print("You've successfully exited the program!!")
            break
            