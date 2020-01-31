from app import views
from app.todoitem import TodoItem

def main_loop():
    while True:
        choice = views.main_menu()
        if choice is None:
            views.bad_input()
        
        elif choice == "6":
            views.goodbye()
            break
        
        elif choice == "1":
            #incomplete items
            items = TodoItem.select_all(complete = 0)

            for item in items:
                views.show_item(item)

            change_choice = views.change_status()
            if change_choice:
                item_choice = views.select_item()
                changed_item = TodoItem.select_one(item_choice)
                change = TodoItem(pk = changed_item[0], title = changed_item[1], description = changed_item[2], complete = changed_item[3])
                if changed_item:
                    change.complete = 1
                    change.save()
                else:
                    views.bad_input()
                views.enter_to_continue()

        elif choice == "2":
            items = TodoItem.select_all(complete = 1)
  
            for item in items:
                views.show_item(item)

            change_choice = views.change_status()
            if change_choice:
                item_choice = views.select_item()
                changed_item = TodoItem.select_one(item_choice)
                change = TodoItem(pk = changed_item[0], title = changed_item[1], description = changed_item[2], complete = changed_item[3])
                if changed_item:
                    change.complete = 0
                    change.save()
                else:
                    views.bad_input()
                views.enter_to_continue()

        elif choice == "3":     
            # show all items
            items = TodoItem.select_all()
            for item in items:
                views.show_item(item)
            views.enter_to_continue

        elif choice == "4":
            title, descrip, complete = views.add()
            item = TodoItem(title = title, description = descrip, complete = complete)
            TodoItem.save(item)

        elif choice == "5":
            #show all items, choose one, then delete it
            items = TodoItem.select_all()
            for item in items:
                views.show_item(item)
            
            delete = views.delete_one()
            d = TodoItem.select_one(delete)
            item = TodoItem(pk = d[0][0])
            item.delete()
            



def run():
    main_loop()

            