#################################################################
# FILE : class_interface.py
# WRITER : Eden Khalifa , eden_khalifa , 323065318
# EXERCISE : intro2cs ex11 2022-2023
# DESCRIPTION: A simple program that is interface of boggle.
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: youtube for videos about tkinter 

#################################################################

from class_game import BoggleGame
from typing import *


class Boggle:
    def __init__(self):
        ####WORDS LST####
        WORDS_FILE = "boggle_dict.txt"
        self.__word_lst = []
        with open(WORDS_FILE) as words_file:
               for line in words_file:
                    line = line.split()
                    self.__word_lst += line


        self.__game = BoggleGame(self.__word_lst)
        self.__board = self.__game.get_board()
        self.__get_lst_of_cords = self.__game.get_lst_of_cords()
        self.__main_game = None
        
        
    def get_changed_board(self): 
        """IF THE PLAYER STARTS A NEW GAME (GAME OVER)"""
        self.__board = self.__game.change_board()
        return self.__board

    def get_missing_points(self):
        """functionto get missing points"""
        return self.__game.get_max_points() - self.__game.get_points()

    def get_users_words(self):
        return self.__game.get_found_words()
    
    def get_all_words(self):
        return self.__word_lst

    def set_main_game(self, main_game_obj):
        self.__main_game = main_game_obj
     

    def get_board(self):
        return self.__board

    def get_lst_of_cords(self):
        return self.__get_lst_of_cords     
    

###################################################################################
#                              BUTTONS COMMAND                                    #
###################################################################################

    def set_all_buttons_command_board(self, main_obj , buttons) -> None:
        """sets all button commands after start button is pressed"""
        for button in buttons.keys():
            if buttons[button]["text"] == "ENTER":
                main_obj.set_button_command(button, self.enter_command)
            elif buttons[button]["text"] == "CLEAR":
                main_obj.set_button_command(button, self.clear_command)
            else:
                main_obj.set_button_board_command(button, self.letter_board_command)
            


    def letter_board_command(self, coordinate : tuple) -> None:
        """letters commands"""
        game = self.__game

        game.click_on_cube(coordinate)
        curr_word = game.update_word_from_path()
        self.__main_game.set_display_label(curr_word)


    def enter_command(self) -> None:
        """enter button command"""
        game = self.__game
        path = game.get_path()

        if game.after_single_round(path):
            self.__main_game.set_points_label(f"SCORE: {game.get_points()}")
            self.__main_game.add_to_stack(game.update_word_from_path())
            game.set_path(True)

        game.set_path(True)
        self.__main_game.set_display_label(game.update_word_from_path())

       
    def clear_command(self) -> None:
        """clear button command"""
        game = self.__game
        game.set_path()
        self.__main_game.set_display_label(game.update_word_from_path())


        

