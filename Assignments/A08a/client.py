#!/usr/bin/env python3
"""

"""
import time
from simple_term_menu import TerminalMenu
from client_helper import ClientHelper

config = {
    'token' : '892db29a750c4bd0e87184c04db19237ece',
    'uid' : '8020',
    'api' : 'http://msubackend.xyz/api/?route='
}

ch = ClientHelper(**config)

def generateKeyPair():
    ch.generate_keys()
    result = ch.publishKey()
    
    if result['success']:
        print("Key Generated !!!")


if __name__ == "__main__":

    token = config['token']
    api = config['api']
    uid = config['uid']
   
    main_menu_title = "  Main Menu\n"
    main_menu_items = ["Generate Key Pair", "List Active Users", "Check Messages", "Send Message", "Quit"]
    main_menu_cursor = "> "
    main_menu_cursor_style = ("fg_blue", "bold")
    main_menu_style = ("bg_blue", "fg_green")
    main_menu_exit = False

    main_menu = TerminalMenu(menu_entries=main_menu_items,
                             title=main_menu_title,
                             menu_cursor=main_menu_cursor,
                             menu_cursor_style=main_menu_cursor_style,
                             menu_highlight_style=main_menu_style,
                             cycle_cursor=True,
                             clear_screen=True)

    # edit_menu_title = "  Edit Menu\n"
    # edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]
    # edit_menu_back = False
    # edit_menu = TerminalMenu(edit_menu_items,
    #                          edit_menu_title,
    #                          main_menu_cursor,
    #                          main_menu_cursor_style,
    #                          main_menu_style,
    #                          cycle_cursor=True,
    #                          clear_screen=True)

    while not main_menu_exit:
        main_sel = main_menu.show()

        # if main_sel == 0:
        #     while not edit_menu_back:
        #         edit_sel = edit_menu.show()
        #         if edit_sel == 0:
        #             print("Edit Config Selected")
        #             time.sleep(5)
        #         elif edit_sel == 1:
        #             print("Save Selected")
        #             time.sleep(5)
        #         elif edit_sel == 2:
        #             edit_menu_back = True
        #             print("Back Selected")
        #     edit_menu_back = False
        
        if main_sel == 0:
            print("Generating Key Pair")
            generateKeyPair()
            time.sleep(1)
        elif main_sel == 1:
            print("Listing Active Users")
            active = ch.getActive()
            print(active)
            time.sleep(1)
        elif main_sel == 2:
            print("Checking Messages")
        elif main_sel == 3:
            print("Sending Message")
        elif main_sel == 4:
            main_menu_exit = True
            print("Quit Selected")


