#################################################################
# FILE : boggle.py
# WRITER : Eden Khalifa , eden_khalifa , 323065318
# EXERCISE : intro2cs ex11 2022-2023
# DESCRIPTION: A simple program that is a graphic interface of boggle.
# STUDENTS I DISCUSSED THE EXERCISE WITH: Bugs Bunny, b_bunny.
#								 	      Daffy Duck, duck_daffy.
# WEB PAGES I USED: youtube for videos about tkinter 
#NOTES: in my gui class i have two sub classes of start frame and end frame because they have a very specific 
#       purpose but when it gets to the main frame in order to avoid circular imports 
#       i made another class for it and created a object of it in BoggleGui class.
#################################################################

import tkinter as tki 
import tkinter.font as tkFont
import class_interface
from typing import *
# importimportfrom PIL import ImageTk, Image

class BoggleGui:

    def __init__(self):
        """creating main game frame object and interface object, 
        and a main window of tk"""
        boggling : tki = tki.Tk()
        boggling.title("Boggle Game")
        boggling.geometry("500x500")
        boggling.resizable(width = False, height = False)
        self.__main_window : MainGame = boggling
        self.__interface : class_interface.Boggle = class_interface.Boggle()
        self.__board : List = self.__interface.get_board()
        self.__lst_of_board_cords : List = self.__interface.get_lst_of_cords()
        self.__button : Dict= dict()
        self.__found_words = None
        self.run()


    def get_main_frame(self) -> tki.Frame:
        return self.__main_frame

    def set_all_buttons(self, buttons_dict : Dict):
        self.__button = buttons_dict

    def get_all_buttons(self) -> dict:
        return self.__button 

    def get_boggle(self) -> tki:
        return self.__main_window

    def get_missing_points(self) -> int:
        return self.__interface.get_missing_points()


    def raise_frames(self, screen_type : str) -> None:
        """a function that switches between two frame- the frame of the class whom 
        called this function is destroyed(before call) and the function raises the screen_type frame"""

        if screen_type == "start":
            self.__board = self.__interface.get_changed_board()
            frame = self.StartBoggle(self.__main_window,self).get_frame()

        if screen_type == "main":
            main_game_obj = MainGame(self.__main_window, self, self.__board, self.__lst_of_board_cords)
            self.__interface.set_main_game(main_game_obj)
            self.__interface.set_all_buttons_command_board(main_game_obj, main_game_obj.get_buttons())
            frame = main_game_obj.get_frame()

        if screen_type == "end":
            if self.__interface.get_users_words() == self.__interface.get_all_words():
                frame = self.EndGame(self.__main_window,self, True).get_frame()
            else:
                frame = self.EndGame(self.__main_window,self, False).get_frame()
                
        frame.tkraise()
       


    def run(self) -> None:
        self.StartBoggle(self.__main_window,self)
        self.__main_window.mainloop()


    class StartBoggle:
        """START FRAME SUBCLASS"""
        def __init__(self, master : tki, boggle):


            # load = Image.open("TITLE.png")
            TEXT_RULES = "RULES: \n Words must be at least three letters in length.\n\
                        Each letter after the first must be a horizontal, vertical, or diagonal\nneighbor of the one before it.\n\
                        No individual letter cube may be used more than once in a word.\n\
                            In this Boggle if you exit before finding all words- you lose.\n NOW GO AHEAD AND BOGGLE IT!"
            PHOTO = tki.PhotoImage(file = "TITLE.png")
            self.__boggle = boggle
            self.__main  = master

            ####BACK FRAME###
            self.__back  = tki.Frame(master = self.__main, bg = "Black")
            self.__back.pack(expand=1,fill=tki.BOTH)

            ####MAPPING BACK FRAME####
            for col in range(10):
                tki.Grid.columnconfigure(self.__back, col , weight = 1)
            for row in range(10):
                tki.Grid.rowconfigure(self.__back, row , weight = 1)

            ####TITLE###
            self.__title_frame = tki.Frame(master = self.__back, bg = "green")
            self.__title_frame.grid(row = 0, column=0,rowspan= 4, columnspan=10, sticky=tki.NSEW)
            self.__title_frame.propagate(0)
            self.__title = tki.Label(master= self.__title_frame, image= PHOTO, bg = "black")
            self.__title.photo = PHOTO
            self.__title.pack(fill="both", expand = True)

            ####START BUTTON###
            self.__start = tki.Button(master = self.__back,
                                         bg = "#fc4dbb", fg = "#000000",text = "START GAME!", 
                                         relief = "flat", font = tkFont.Font(family='Times',size=17),
                                        justify = "center", command=self.end_start_window)
            self.__start.grid(row = 8, column=0,columnspan=10)

            ### RULES FRAME AND LABEL####
            self.__rules_frame = tki.Frame(master = self.__back)
            self.__rules = tki.Label(master= self.__rules_frame, fg="#efb4d9", bg = "black", font = tkFont.Font(family='Times',size=12), justify="center")

            self.__rules.config(text = TEXT_RULES)
            self.__rules_frame.propagate(0)
            self.__rules_frame.grid(row =5, column=0,rowspan = 3,columnspan=10, sticky=tki.NSEW)
            self.__rules.pack(fill="both", expand = 1)

            
        def get_frame(self) -> tki.Frame:
            return self.__back


        def end_start_window(self) -> None:
            """start button command"""
            self.__back.destroy()
            self.__boggle.raise_frames('main')
            

    class EndGame():
        def __init__(self,  master, boggle, win : bool ) -> None:
            LOSS_TEXT = "This is Theodore Roosevelt.\n In this situation \n I think you should read his speech -\n The Man In The Arena" 
            PHOTO = tki.PhotoImage(file="lost_image.png")
            self.__boggle = boggle
            self.__main = master
            self.__back = tki.Frame(master=self.__main, bg="#f0c3df")
            self.__back.pack(fill= "both", expand=1)
            
            
            ###MAPPING BACK###
            for col in range(10):
                tki.Grid.columnconfigure(self.__back, col , weight = 1)
            for row in range(10):
                tki.Grid.rowconfigure(self.__back, row , weight = 1)
            

            ###RESULT LABEL###
            if win:
                self.__res_msg = tki.Label(master=self.__back, bg = "#f0c3df",
                                             text = "YOU BOGGLED IT!",
                                              font = tkFont.Font(family='Times',size=30) )

            else:
                self.__res_msg = tki.Label(master=self.__back,
                                             bg = "#f0c3df", text = "OH NO! YOU LOST.",
                                              font = tkFont.Font(family='Times',size=30) )
                self.__photo_frame = tki.Frame(master = self.__back, bg = "green")
                self.__photo_frame.grid(row = 2, column=0,rowspan= 5, columnspan=10, sticky=tki.NSEW)
                self.__photo_frame.propagate(0)
                self.__photo = tki.Label(master= self.__photo_frame, image= PHOTO, bg = "#f0c3df")
                self.__photo.photo = PHOTO
                self.__photo.pack(fill="both", expand = True)
                self.__res_msg.grid(row= 0 , column=0, rowspan = 1,columnspan=10,sticky=tki.NSEW)

                self.__lose_text = tki.Label(master = self.__back, justify = "center",
                                    text = LOSS_TEXT, bg ="#f0c3df",font = tkFont.Font(family='Times',size=15 ))

                self.__lose_text.grid(row = 7, column = 0, rowspan=2,columnspan=10,sticky=tki.NSEW)


            ###GAME OVER BUTTON###
            self.__game_over= tki.Button(master=self.__back, bg = "#b4daf6", 
                                        text= "GAME OVER", font = tkFont.Font(family='Times',size=14), 
                                        command = self.reset_game)
            self.__game_over.grid(row= 9 , column=3, columnspan=4) 

            ####MISSING POINTS LABEL###
            self.__points_missing= tki.Label(master= self.__back, 
                                text=f"{self.__boggle.get_missing_points()} POINTS WERE MISSING",
                                     bg = "#f0c3df")
            self.__points_missing.grid(row= 10, column=3, columnspan=4)



        def get_frame(self) -> tki.Frame:
            return self.__back

        def reset_game(self) -> None:
            """game over button command"""
            self.__back.destroy()
            self.__boggle.raise_frames("start")

    
class MainGame:
    
    def __init__(self,master,boggle, board, lst_of_cords):

        BOARD_BUTTONS_COLOR = "#f5b2dc"
        BUTTON_STYLE = {"rowspan" : 1, "columnspan" : 1, "font" : tkFont.Font(family='Times',size=12)}
        self.__main = master
        self.__boggle = boggle


        ###BACK FRAME###
        self.__back = tki.Frame(master = self.__main, bg = "Black")
        self.__back.pack(fill= "both", expand = 1)
    

        ###MAPPING MAIN BACKROUND###
        for col in range(4):
            tki.Grid.columnconfigure(self.__back, col , weight = 1)
        for row in range(5):
            tki.Grid.rowconfigure(self.__back, row , weight = 1)


        ###DISPLAY LABEL###
        self.__display_label_Frame = tki.LabelFrame(master = self.__back,
                                                        background= "#e7a1a1",
                                                        text = "CURRENT WORD", 
                                                        font = tkFont.Font(family='Times'
                                                        ,size=17))
        self.__display_label_Frame.grid(row = 0, column = 0, rowspan=1, columnspan=5, sticky=tki.NSEW)

        self.__display_label = tki.Label(master = self.__display_label_Frame,
                                            background="#efdbdb",
                                            text = "", font = tkFont.Font(family='Times'
                                                        ,size=20))
        self.__display_label.pack(fill="both", expand = 1, side = "top")

    

        ##STACK AND SCORLLBAR##
        self.__stack_frame = tki.LabelFrame(master = self.__back,
                                                bg = "#dfc3d5", text = "FOUND WORDS",
                                                font = tkFont.Font(family='Times',size=11))
        self.__stack_frame.grid(row = 1, column = 0, rowspan=3, sticky=tki.NSEW)
        self.__stack = tki.Listbox(self.__stack_frame,width = 1, bg="#dfc3d5", fg="black", font=("Courier", 18))
        self.__scrollbar = tki.Scrollbar(self.__stack_frame, orient=tki.VERTICAL, command=self.__stack.yview)
        self.__stack['yscrollcommand'] = self.__scrollbar.set
        self.__scrollbar.pack(side=tki.LEFT, expand=0,fill=tki.Y)
        self.__stack.pack(fill = "both", expand = 1)


        ###BOARD###
        self.__board_frame = tki.Frame(master = self.__back, bg="WHITE", highlightbackground="white", highlightcolor="white")
        self.__board_frame.grid(row = 1, column = 1, rowspan=3, columnspan=3,sticky=tki.NSEW)
        
        
        ##LOWER FRAME##
        self.__lower_frame = tki.Frame(master = self.__back, bg = BOARD_BUTTONS_COLOR)
        self.__lower_frame.grid(row = 4, column = 0, rowspan=2, columnspan=5, sticky=tki.NSEW)
    
        ###MAPPING###
        self.mapping_lower_frame()
        self.mapping_board_frame()
        
        ###TIMER###
        self.__timer = tki.Label(master = self.__lower_frame, text ="03:00"
                                ,bg =  BOARD_BUTTONS_COLOR ,justify = "center", 
                                    font = tkFont.Font(family='Times',size=13))
        self.__timer.grid(row = 0, column=0, sticky=tki.NSEW)


        ###POINTS###
        self.__points = tki.Label(master = self.__lower_frame, text = "SCORE : 00"
                                ,bg =  BOARD_BUTTONS_COLOR,justify = "center", 
                                    font = tkFont.Font(family='Times',size=13))
        self.__points.grid(row= 0, column=1, sticky=tki.W )


        ##BUTTONS##
        self.__buttons = dict()
        for coordinate in lst_of_cords:
            letter = board[coordinate[0]][coordinate[1]]
            self._make_button(self.__board_frame, letter,2, BOARD_BUTTONS_COLOR,coordinate[0], coordinate[1], **BUTTON_STYLE)

        ###CLEAR AND ENTER BUTTONS###
        self._make_button(self.__board_frame, "CLEAR", 2, BOARD_BUTTONS_COLOR,0,4,2, 1, tkFont.Font(family='Times',size=12))
        self._make_button(self.__board_frame, "ENTER", 2,BOARD_BUTTONS_COLOR,2,4,2, 1, tkFont.Font(family='Times',size=12))
        

        #EXIT BUTTON -> SINCE IT HAS A SPECIFIC ROLE I THOUGHT IT SHOULD BE DEFINED ALONE ALONG WITH ITS COMMAND.
        self.__exit = self._make_button(self.__lower_frame, "EXIT", 1, BOARD_BUTTONS_COLOR , 0, 2,**BUTTON_STYLE)
        self.__exit.configure(command = self.end_game)
        
    
        ###BUTTONS UPDATED IN MAIN CLASS###
        self.__boggle.set_all_buttons(self.__buttons)
        self.timer()


    def create_board_buttons(self, coordinate, letter, color, **BUTTON_STYLE) -> None:
        """function that creates all board buttons according to the given board and updates its dict(buttons)"""
        self._make_button(self.__board_frame, letter, 2, color, coordinate[0], coordinate[1], **BUTTON_STYLE)    

    ########MAPPING FUNCTIONS########

    def mapping_lower_frame(self) -> None:

        for col in range(2):
            tki.Grid.columnconfigure(self.__lower_frame, col , weight = 1)
        for row in range(1):
            tki.Grid.rowconfigure(self.__lower_frame, row , weight = 1)

    def mapping_board_frame(self) -> None:
        for col in range(5):
            tki.Grid.columnconfigure(self.__board_frame, col , weight = 1)
        for row in range(4):
            tki.Grid.rowconfigure(self.__board_frame, row , weight = 1)

    ########MAKE BUTTON#########

    def _make_button(self, frame, button_char : str, borderwidth : int, bg : str,
                        row : int, col : int, rowspan, columnspan, font) -> tki.Button: #bogglegame
            """a fuction that creates button"""


            button = tki.Button(master=frame, 
                                text = button_char, bg = bg,
                                font = font,
                                borderwidth= borderwidth, cursor= "pirate")
            button.grid(row = row , column = col, rowspan= rowspan, columnspan= columnspan, sticky=tki.NSEW)

            def _on_enter(event : any):
                button["background"] = "lightGreen"
            def _on_leave(event : any):
                button["background"] = "#f5b2dc"

            button.bind("<Enter>", _on_enter)
            button.bind("<Leave>", _on_leave)

            if button_char == "EXIT": #line 281
                return button

            self.__buttons.update({(row, col) : button})
            return button


    ##########SETTERS#################

    def set_button_command(self, button_tuple : tuple, command : callable) -> None:
        self.__buttons[button_tuple].configure(command = command)
    
    def set_button_board_command(self, button_tuple : tuple, command : callable) -> None:
        self.__buttons[button_tuple].configure(command = lambda : command(button_tuple))
    
    def set_points_label(self, text) -> None:
        self.__points.config(text= text)
    
    def set_display_label(self, text) -> None:
        self.__display_label.config(text = text )

    #####TIMER########

    def timer(self) -> None:
        """timer function that counts down 3 minutes"""
        seconds = self.__timer["text"][-2:]
        minutes = self.__timer["text"][1:2]

        if seconds == "00" and minutes == "0":
            return self.end_game()

        elif seconds == "00":
            seconds = "59"
            minutes = int(minutes) - 1
        else:
            seconds = int(seconds) - 1

        if len(str(seconds)) == 1:
            seconds = "0" + str(seconds)
        self.__timer.config(text = f"0{minutes}:{seconds}")
        return self.__back.after(1000, self.timer)

    def add_to_stack(self, word : str) -> None:
        """changes stack text if needed"""
        self.__stack.insert(tki.END, word)

    def get_frame(self) -> tki.Frame:
        return self.__back

    def change_label(self, curr_word) -> None: 
        """chages label according to curr word"""
        self.__display_label["text"] = curr_word


    def end_game(self) -> None:
        self.__back.destroy()
        self.__boggle.raise_frames("end")
    
    def get_buttons(self) -> dict:
        return self.__buttons

       

if __name__ == "__main__":

    BoggleGui()



        
