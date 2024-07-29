#################################################################
# FILE : ex11_utils.py
# WRITER : Eden Khalifa
# EXERCISE : intro2cs ex11 2022-2023
# DESCRIPTION: A simple program that is a graphic interface of boggle.
#################################################################



from boggle_board_randomizer import *
from typing import List, Tuple, Iterable, Optional
import functools

Board = List[List[str]]
Path = List[Tuple[int, int]]


def lst_of_cords(board : Board) -> List[Tuple]:
    return [(i, j) for i in range(len(board)) for j in range(len(board[0]))]


def dict_of_possible_moves(lst_of_coordinates : list) -> dict[tuple : List[tuple]]:
    """a function that creates a dict with possible moves per cube"""
    main_dict : dict[tuple : List[tuple]] = dict()
    for coordinate in lst_of_coordinates:
        main_dict.update({coordinate :  []})
        row, col = coordinate[0], coordinate[1]
        for i in range(-1,2):
            for j in range(-1, 2):
               possible_move = (row + i, col + j)
               if possible_move in lst_of_coordinates and possible_move != coordinate: #checks if we are in board and not appending the coordinate itself in case i=j=0
                    main_dict[coordinate].append(possible_move)
    return main_dict 


def all_starters(words : Iterable) -> set:
    """all subwords-starters out of the words"""
    set_of_sub_words = set()
    lst_of_len = list()
    for word in words:
        lst_of_len.append(len(word))
        for i in range(len(word), -1,-1):
            set_of_sub_words.add(word[:i])
    return set_of_sub_words, lst_of_len


def valid_move(dict_of_possible_moves : dict, coordinate : Tuple, move : Tuple) -> bool:
    """checks if move is valid"""
    return coordinate in dict_of_possible_moves and move in dict_of_possible_moves[coordinate] 

##################################################################################
#                               VALID PATH                                       #
##################################################################################

def is_valid_path(board: Board, path: Path, words: Iterable[str]) -> Optional[str]:
    """a function that checks if path is valid"""

    all_coordinates : List[tuple] =  lst_of_cords(board)
    dict_possible_moves = dict_of_possible_moves(all_coordinates)
    word = ""

    if len(path) == 0:
        return None

    previous_move = path[0] #first move
    not_first_iteration = False
    valid = False


    for move in path: 
        if not not_first_iteration and move in all_coordinates:
            valid = True
        if path.count(move) > 1: #cannot use twice same cube in one path
            return None
        if not_first_iteration:
            valid = valid_move(dict_possible_moves, previous_move, move)
        not_first_iteration = True
        if valid:
            word += board[move[0]][move[1]]
        else:
            return None
        previous_move = move

    if word in words:
        return word

        
##################################################################################
#                                  N-PATHS                                       #
##################################################################################

def find_length_n_paths(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """finds all n length paths on board"""

    lst_of_all_paths = []

    if n < 1:
        return lst_of_all_paths

    lst_of_coordinates = lst_of_cords(board) 
    dict_of_pos_moves = dict_of_possible_moves(lst_of_coordinates)
    set_of_subwords = all_starters(words)[0]

    for i in range(len(board)):
        for j in range(len(board[0])):
            _helper_n_paths([(i,j)], n, board,lst_of_all_paths, dict_of_pos_moves,set_of_subwords,words,board[i][j])

    return lst_of_all_paths




def _helper_n_paths(path :list, n : int, board : Board, lst : list, dict_possible_moves : dict,set_of_subwords :set,words : Iterable,word : str) -> list:
    """helper function for find n length paths"""

    if word not in set_of_subwords:
        return

    if len(path) == n:
        if word in words:
            lst.append(path[:])  
            return 
        return

    for coordinate in dict_possible_moves[path[-1]]:
        path.append(coordinate)    
        if not is_valid_path_n(path):
            del path[-1]
            continue
        _helper_n_paths(path, n, board,lst , dict_possible_moves, set_of_subwords,words, word+board[coordinate[0]][coordinate[1]])
        del path[-1]

    return lst


def is_valid_path_n(path: Path) -> Optional[str]:
    return path.count(path[-1]) == 1


    
def is_path_a_word(board: Board, path : Path, words):

    word = ""
    for move in path:
        word += board[move[0]][move[1]]
    if word in words:
        return word



def is_score_a_word(board: Board, path : Path, words):
    word = ""
    for move in path:
        word += board[move[0]][move[1]]
    if word == words:
        return word


##################################################################################
#                                  N-WORDS PATHS                                 #
##################################################################################

def filter_n_words(words : Iterable, n  :int) -> list: 
    """filter all words that are not length n in words"""
    return list(filter((lambda word : len(word) == n), words))



def find_length_n_words(n: int, board: Board, words: Iterable[str]) -> List[Path]:
    """finds all path for n length words"""

    lst_of_n_words = filter_n_words(words, n)
    all_paths = []
    lst_of_coordinates = lst_of_cords(board) 
    dict_of_pos_moves = dict_of_possible_moves(lst_of_coordinates)
    res_of_all_starters = all_starters(lst_of_n_words)
    SET_OF_SUBWORDS, LEN_WORDS = res_of_all_starters[0], res_of_all_starters[1]

    if n not in LEN_WORDS:
        return all_paths
    # for i in range(n + 1):
    for i in range(len(board)):
        for j in range(len(board[0])):
            _helper_n_words([(i,j)], n, board, all_paths, dict_of_pos_moves,SET_OF_SUBWORDS,lst_of_n_words,board[i][j])

    return all_paths

    
def _helper_n_words(path : list, n : int, board : Board, lst : list, dict_possible_moves :dict ,set_of_subwords :set,words : Iterable ,word: str) -> list:

    if word not in set_of_subwords:
        return

    if len(path) == n:
        if word in words:
            lst.append(path[:])  
            return 
        return

    for coordinate in dict_possible_moves[path[-1]]:
        path.append(coordinate)    
        if not is_valid_path_n(path):
            del path[-1]
            continue
        _helper_n_words(path, n, board,lst , dict_possible_moves, set_of_subwords,words, word+board[coordinate[0]][coordinate[1]])
        del path[-1]

    return lst



##################################################################################
#                                MAX SCORE                                       #
##################################################################################



def max_score_paths(board: Board, words: Iterable[str]) -> list:

    lst_of_max_paths = list()
    dict_of_max_paths = dict()
    lst_of_coordinates = lst_of_cords(board) 
    dict_of_pos_moves = dict_of_possible_moves(lst_of_coordinates)
    res_of_all_starters = all_starters(words)
    SET_OF_SUBWORDS, LEN_MAX_WORD = res_of_all_starters[0], max(res_of_all_starters[1])

    for l in range(LEN_MAX_WORD, 0, -1):
        for i in range(len(board)):
            for j in range(len(board[0])):
                _helper_max_paths([(i,j)], l, board,dict_of_max_paths, dict_of_pos_moves,
                SET_OF_SUBWORDS,words,board[i][j])

    for max_path in dict_of_max_paths.values():
        lst_of_max_paths.append(max_path)

    return lst_of_max_paths



def _helper_max_paths(path : list, n : int, board :list[list], dict : dict, dict_possible_moves : dict,set_of_subwords :set,words : Iterable,word :str) -> dict:

    if word not in set_of_subwords:
        return

    if len(path) == n:
        if word in words and len(dict.get(word, [])) < n :
            dict.update({word : path[:]})  
            return 
        return

    for coordinate in dict_possible_moves[path[-1]]:
        path.append(coordinate)    
        if not is_valid_path_n(path):
            del path[-1]
            continue
        _helper_max_paths(path, n, board,dict, dict_possible_moves, set_of_subwords,words,
         word+board[coordinate[0]][coordinate[1]])
        del path[-1]

    return dict



             
    

