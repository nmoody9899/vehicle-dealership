from classes.vehicle import Vehicle
from classes.showroom import Showroom
from classes.dealership import Dealership
import curses


def run_gui(background):
    # Removes the flashing cursor
    curses.curs_set(0)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

    main_window = background.derwin(41, 157, 0, 0)
    main_window.border(0, 0, 0, 0)
    main_window.addstr(0, 2, ' DEALERSHIP MANAGEMENT SYSTEM ', curses.color_pair(1))

    menu_window = main_window.derwin(13, 45, 2, 2)
    menu_window.border(0, 0, 0, 0)
    menu_window.addstr(0, 2, ' Menu Options ', curses.color_pair(2))
    selections = [
        '[0] Update dealership capacity',
        '[1] Add showroom to dealership',
        '[2] Remove showroom from dealership',
        '[3] Update showroom capacity',
        '[4] Add vehicle to showroom',
        '[5] Update vehicle in showroom',
        '[6] Remove vehicle from showroom',
        '[7] Move a vehicle',
        '[8] Add vehicle to lot',
        '[9] Remove vehicle from lot',
        '[Q] Quit'
    ]
    for selection, option in enumerate(selections, start=1):
        menu_window.addstr(selection, 2, option)    

    update_window = main_window.derwin(13, 45, 2, 48)
    update_window.border(0, 0, 0, 0)
    update_window.addstr(0, 2, ' Modify Inventory ', curses.color_pair(2))
    update_window.addstr(1, 2, 'Adding a new vehicle to a showroom...')
    inputs = [
        'Showroom:',
        '',
        'Year:',
        'Make:',
        'Model:',
        'Price:',
        'Mileage:'
    ]
    for row, input in enumerate(inputs, start=3):
        update_window.addstr(row, 2, input)

    inventory_window = main_window.derwin(38, 61, 2, 94)
    inventory_window.border(0, 0, 0, 0)
    inventory_window.addstr(0, 2, ' Complete Inventory ', curses.color_pair(2))

    statistics_window = main_window.derwin(8, 91, 16, 2)
    statistics_window.border(0, 0, 0, 0)
    statistics_window.addstr(0, 2, ' Dealership Statistics ', curses.color_pair(2))

    audit_window = main_window.derwin(15, 91, 25, 2)
    audit_window.border(0, 0, 0, 0)
    audit_window.addstr(0, 2, ' Activity Log ', curses.color_pair(2))

    while True:
        background.refresh()
        input = background.getch()

        if input == ord('Q') or input == ord('q'):
            curses.endwin()
            break


if __name__ == '__main__':
    curses.wrapper(run_gui)