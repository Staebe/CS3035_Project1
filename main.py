from kivy.lang import Builder
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label

class TicTacToe(App):
    def build(self):
        return Builder.load_file('Board.kv')

    user = "O"

    winner = False

    def presser(self, button):
        if self.user == 'O':
            button.text = "O"
            button.disabled = True
            self.check_if_winner()
            if self.winner == False: 
                self.root.ids.infoLabel.text = "Your turn X"
                self.root.ids.infoLabel.text_colour = "red"
            self.user  = "X"
        else:
            button.text = "X"
            button.disabled = True
            self.check_if_winner()
            if self.winner == False: 
                self.root.ids.infoLabel.text = "Your turn O"
            self.user  = "O"

    def check_if_winner(self):
        #check horizontal
        topLeftButton = self.root.ids.btnTopLeft
        topMidButton = self.root.ids.btnTopMid
        topRightButton = self.root.ids.btnTopRight

        #TOP ROW
        if topLeftButton.text!= "" and topLeftButton.text == topMidButton.text ==topRightButton.text:
            self.update_winning_buttons(topLeftButton, topMidButton, topRightButton)


    def update_winning_buttons(self, button1, button2, button3):
        self.root.ids.infoLabel.text = f"Player {self.user} Wins!"
        self.root.ids.infoLabel.colour = (0, 1, 0, 1)
        self.winner = True
        for button in (button1, button2, button3):
            button.background_color = (0, 1, 0, 1)  # Green background
            button.background_disabled_normal = ""  
            button.color = (0, 0, 0, 1)  # Black text
        
        self.diable_all_buttons()
        
    def disable_all_buttons(self): # to implement to disable after winning
        pass

    def reset_board(self, button):
        pass  #implement later, would just need to reset all 9 tictactoe buttons to starting vals from Board.kv

TicTacToe().run()