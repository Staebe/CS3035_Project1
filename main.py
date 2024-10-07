from kivy.lang import Builder
from kivymd.app import MDApp

class TicTacToe(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange";
        return Builder.load_file('Board.kv')

    user = "O"

    def presser(self, button):
        if self.user == 'O':
            button.text = "O"
            button.disabled = True
            self.root.ids.infoLabel.text = "Your turn X"
            button.color = [1,0,1,1]
            self.user  = "X"
        else:
            button.text = "X"
            button.disabled = True
            self.root.ids.infoLabel.text = "Your turn O"
            button.color = [0,0,1,1]
            self.user  = "O"
        
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


TicTacToe().run()