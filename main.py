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
        self.root.ids.btnTL.disabled = False;
        self.root.ids.btnL.disabled = False;
        self.root.ids.btnBL.disabled = False;
        self.root.ids.btnTC.disabled = False;
        self.root.ids.btnC.disabled = False;
        self.root.ids.btnBC.disabled = False;
        self.root.ids.btnTR.disabled = False;
        self.root.ids.btnR.disabled = False;
        self.root.ids.btnBR.disabled = False;
            
        self.root.ids.btnTL.text = "";
        self.root.ids.btnL.text = "";
        self.root.ids.btnBL.text = "";
        self.root.ids.btnTC.text = "";
        self.root.ids.btnC.text = "";
        self.root.ids.btnBC.text = "";
        self.root.ids.btnTR.text = "";
        self.root.ids.btnR.text = "";
        self.root.ids.btnBR.text = "";


TicTacToe().run()