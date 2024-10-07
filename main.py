from kivy.lang import Builder
from kivymd.app import MDApp

class TicTacToe(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange";
        return Builder.load_file('Board.kv')

    user = "O"

    winner = False
    score_O = 0
    score_X = 0

    def presser(self, button):
        if self.user == 'O':
            button.text = "O"
            button.disabled = True
            button.color = [1,0,1,1]
            self.check_if_winner()
            if self.winner == False: 
                self.root.ids.infoLabel.text = "Your turn X"
            self.user  = "X"
        else:
            button.text = "X"
            button.disabled = True
            button.color = [0,0,1,1]
            self.check_if_winner()
            if self.winner == False:
                self.root.ids.infoLabel.text = "Your turn O"
            self.user  = "O"
    def check_if_winner(self):
        #check horizontal (3)
        topLeftButton = self.root.ids.btnTL
        topMidButton = self.root.ids.btnTC
        topRightButton = self.root.ids.btnTR
        midLeftButton = self.root.ids.btnL
        midMidButton = self.root.ids.btnC
        midRightButton = self.root.ids.btnR
        botLeftButton = self.root.ids.btnBL
        botMidButton = self.root.ids.btnBC
        botRightButton = self.root.ids.btnBR


        #TOP ROW (1/3)
        if  topLeftButton.text!= "" and  topLeftButton.text == topMidButton.text ==topRightButton.text:
            self.update_winning_buttons( topLeftButton, topMidButton, topRightButton)
            self.disable_all_buttons()
            return True
        # MIDDLE ROW
        if midLeftButton.text != "" and midLeftButton.text == midMidButton.text == midRightButton.text:
            self.update_winning_buttons(midLeftButton, midMidButton, midRightButton)
            self.disable_all_buttons()
            return True
        # BOTTOM ROW
        if botLeftButton.text != "" and botLeftButton.text == botMidButton.text == botRightButton.text:
            self.update_winning_buttons(botLeftButton, botMidButton, botRightButton)
            self.disable_all_buttons()
            return True

        # Vertical wins (3 columns)
        # LEFT COLUMN
        if topLeftButton.text != "" and topLeftButton.text == midLeftButton.text == botLeftButton.text:
            self.update_winning_buttons(topLeftButton, midLeftButton, botLeftButton)
            self.disable_all_buttons()
            return True
        # MIDDLE COLUMN
        if topMidButton.text != "" and topMidButton.text == midMidButton.text == botMidButton.text:
            self.update_winning_buttons(topMidButton, midMidButton, botMidButton)
            self.disable_all_buttons()
            return True
        # RIGHT COLUMN
        if topRightButton.text != "" and topRightButton.text == midRightButton.text == botRightButton.text:
            self.update_winning_buttons(topRightButton, midRightButton, botRightButton)
            self.disable_all_buttons()
            return True

        # Diagonal wins (2 diagonals)
        # TOP-LEFT to BOTTOM-RIGHT DIAGONAL
        if topLeftButton.text != "" and topLeftButton.text == midMidButton.text == botRightButton.text:
            self.update_winning_buttons(topLeftButton, midMidButton, botRightButton)
            self.disable_all_buttons()
            return True
        # TOP-RIGHT to BOTTOM-LEFT DIAGONAL
        if topRightButton.text != "" and topRightButton.text == midMidButton.text == botLeftButton.text:
            self.update_winning_buttons(topRightButton, midMidButton, botLeftButton)
            self.disable_all_buttons()
            return True

        # No winner
        return False


    def update_winning_buttons(self, button1, button2, button3):
        self.root.ids.infoLabel.text = f"PLAYER {self.user} Wins!"
        self.root.ids.infoLabel.colour = (0, 1, 0, 1)
        self.winner = True
        for button in (button1, button2, button3):
            button.background_color = (0, 1, 0, 1)  # Green background
            button.background_disabled_normal = ""  
            button.color = (0, 0, 0, 1)  # Black text
        
        self.disable_all_buttons()

        if self.winner:  # to update scoreboard
            self.update_score()

    def update_score(self):
        if self.user == "O":
            self.score_O += 1
        else:
            self.score_X += 1

        self.root.ids.scoreLabel.text = f"PLAYER O: {self.score_O}          PLAYER X: {self.score_X}"
        
    def disable_all_buttons(self): # to implement to disable after winning
        
        buttons = [self.root.ids.btnTL, self.root.ids.btnL, self.root.ids.btnBL,
                self.root.ids.btnTC, self.root.ids.btnC, self.root.ids.btnBC,
                self.root.ids.btnTR, self.root.ids.btnR, self.root.ids.btnBR]
        
        for button in buttons:
            button.disabled = True

    def reset_scoreboard(self):
        self.score_O = 0
        self.score_X = 0
        self.root.ids.scoreLabel.text = f"PLAYER O: {self.score_O}          PLAYER X: {self.score_X}"


    def reset(self):
        # self.user = "O" if commented out, whoever lost goes first next time
        # Reset all button states and colors
        buttons = [self.root.ids.btnTL, self.root.ids.btnL, self.root.ids.btnBL,
                self.root.ids.btnTC, self.root.ids.btnC, self.root.ids.btnBC,
                self.root.ids.btnTR, self.root.ids.btnR, self.root.ids.btnBR]
        
        for button in buttons:
            button.disabled = False
            button.text = ""
            button.background_color = "teal"  #initial from .kv file
            button.color = [1, 1, 1, 1]  #Apparently this initial state too
             # undoes change from update winning buttons:
             # New in version 1.8.0. background_disabled_normal is a StringProperty 
             # and defaults to ‘atlas://data/images/defaulttheme/button_disabled’."
            button.background_disabled_normal = 'atlas://data/images/defaulttheme/button_disabled'
            self.root.ids.infoLabel.colour = (0, 0, 0, 0)
            self.root.ids.infoLabel.text = f"Your turn {self.user}"

        self.winner = False

TicTacToe().run()