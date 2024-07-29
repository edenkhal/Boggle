
#################################################################
# FILE : class_game.py
# WRITER : Eden Khalifa , eden_khalifa , 323065318
# EXERCISE : intro2cs ex11 2022-2023
# DESCRIPTION: A simple program that is a boggle "rules".
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: youtube for videos about tkinter 

#################################################################
import boggle_board_randomizer
import ex11_utils
from typing import *




class BoggleGame:
    def __init__(self, words : list):

        self.__board : list[list]= boggle_board_randomizer.randomize_board()
        self.__lst_of_cord_board : list= ex11_utils.lst_of_cords(self.__board)
        self.__points :int = 0
        self.__words : list = words
        self.__max_points : int = 0
        self.__found_words : list = list()
        self.__curr_path : list= list()
        self.__curr_word : str= ""
        self.__user_words  : list= []
        self.__possible_moves : dict = ex11_utils.dict_of_possible_moves(self.__lst_of_cord_board)
        self.set_max_points()

    def set_max_points(self) -> None: 
        """updates max points"""
        max_paths = ex11_utils.max_score_paths(self.__board, self.__words)
        max_points = 0 
        for path in max_paths:
            max_points += len(path)**2
        self.__max_points = max_points

    def after_single_round(self, path):
        """updates that are needed after every user's choice/click on enter"""
        res = self.__curr_word
        
        if res not in self.__found_words and self.__curr_word in self.__words:
            if res != None:
                self.__points += (len(path)**2)
                self.__found_words.append(res)
                return True
            
    def update_word_from_path(self) -> str:
        """updates current word according to current path when needed"""
        path = self.__curr_path
        self.__curr_word = ""
        for coordinate in path:
            self.__curr_word += self.__board[coordinate[0]][coordinate[1]]
        return self.__curr_word




    def click_on_cube(self, click : tuple) -> None: #click_coor
        """updates that are needed after every user's choice/click on letter button"""
        if (len(self.__curr_path ) == 0 or 
        (click in self.__possible_moves[self.__curr_path[-1]] and (click not in self.__curr_path))) :

            self.__curr_path.append(click)

            
    def set_path(self, enter : bool = False) -> None:
        """enter or clear sre clicked the curr path is updated"""
        if not enter and self.__curr_path:
            self.__curr_path.pop()
        else:  
            self.__curr_path = []

        
    def change_board(self) -> list[list]:
        """for game over button, another board needs to be set"""
        self.__board = boggle_board_randomizer.randomize_board()
        return self.__board


###################################################################################
#                                   GETTERS                                       #
###################################################################################
    def get_board(self) -> list[list]:
        return self.__board
    def winning(self) -> bool:
        return self.__points == self.__max_points
    def get_curr_word(self)-> str:
        return self.__curr_word
    def get_curr_path(self) -> list:
        return self.__curr_path
    def get_max_points(self) -> int:
        return self.__max_points
    def get_points(self) -> int:
        return self.__points
    def get_found_words(self) -> list:
        return self.__found_words
    def get_word(self) -> list[list]:
        return self.__board
    def get_lst_of_cords(self) -> list:
        return self.__lst_of_cord_board
    def get_path(self) -> list:
        return self.__curr_path

        


