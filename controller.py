import view
import model

def choose():
    option = int(input(view.get_choice()))
    if option == 0:
        location_lists = model.location_lists_maker()
        view.location_list(location_lists)
    elif option == 4:
        view.endview()

choose()