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
            self.root.ids.infoLabel.text_colour = "red"
            self.user  = "X"
        else:
            button.text = "X"
            button.disabled = True
            self.root.ids.infoLabel.text = "Your turn O"
            self.user  = "O"

TicTacToe().run()