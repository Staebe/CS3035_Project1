from kivy.lang import Builder
from kivymd.app import MDApp

class TicTacToe(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange";
        return Builder.load_file('Board.kv')

    user = "O"

    winner = False

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

        #TOP ROW (1/3)
        if  topLeftButton.text!= "" and  topLeftButton.text == topMidButton.text ==topRightButton.text:
            self.update_winning_buttons( topLeftButton, topMidButton, topRightButton)

    def update_winning_buttons(self, button1, button2, button3):
        self.root.ids.infoLabel.text = f"Player {self.user} Wins!"
        self.root.ids.infoLabel.colour = (0, 1, 0, 1)
        self.winner = True
        for button in (button1, button2, button3):
            button.background_color = (0, 1, 0, 1)  # Green background
            button.background_disabled_normal = ""  
            button.color = (0, 0, 0, 1)  # Black text
        
        self.disable_all_buttons()
        
    def disable_all_buttons(self): # to implement to disable after winning
        pass

    def reset(self):
        self.user = "O"
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

TicTacToe().run()