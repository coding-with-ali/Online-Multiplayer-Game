import random
import tkinter
from NFYP.Network import Network


def getRandNo():
    return random.randint(1, 6)

class UiManager:
    def __init__(self):
        self.n = Network()
        self.nR= self.n.connect()
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(height=200, width=200)
        self.file_name = ""
        self.dice_img = ""
        self.total_numbers = 20
        self.numbers_left = 20
        self.my_score = 0
        self.op_score = 0
        self.turn=False
        self.title = "RandCas"
        print(self.nR)



    def design_window(self):
        self.window.title(self.title)
        self.window.config(padx=20, pady=20)

    def design_numbers_left_label(self):
        numbers_left = tkinter.Label(text=f"Numbers {self.numbers_left}/{self.total_numbers}", bg="green")
        numbers_left.grid(row=0, column=0, columnspan=2)

    def design_img_canvas(self,randNo):
        self.randNo = randNo
        print(self.randNo)
        self.file_name = f"./../Images/{self.randNo}.png"
        self.dice_img = tkinter.PhotoImage(file=self.file_name)
        self.canvas.create_image(100, 100, image=self.dice_img)
        self.canvas.grid(row=1, column=0, columnspan=2)

    def design_score_labels(self):
        my_score_label = tkinter.Label(text="My Score", bg="green")
        my_score_label.grid(row=2, column=0)
        opp_score_label = tkinter.Label(text="Op Score", bg="red")
        opp_score_label.grid(row=2, column=1)

    def design_my_score_value(self,myscore):
        self.my_score=myscore
        my_score_value = tkinter.Label(text=f"{self.my_score}", bg="green")
        my_score_value.grid(row=3, column=0)


    def design_op_score_value(self,opscore):
        self.op_score = opscore
        op_score_value = tkinter.Label(text=f"{self.op_score}", bg="red")
        op_score_value.grid(row=3, column=1)



    def onDiceRoll(self):
        self.randNo=getRandNo()

        if (self.randNo==6):
            self.my_score+=1
            self.design_my_score_value(self.my_score)
        self.numbers_left=int(self.numbers_left)-1
        self.design_numbers_left_label()
        self.design_img_canvas(self.randNo)

        self.opdata=self.sendData(self.my_score,self.numbers_left)
        self.opdata = self.opdata.split(",")
        print(self.opdata)

        self.op_score=self.opdata[0]
        self.numbers_left=self.opdata[1]
        self.design_op_score_value(self.op_score)

        # if (self.numbers_left==0):
        #     self.exit_game()



    def sendData(self, randNo, numberleft):
        self.data = f"{randNo},{numberleft}"
        self.receved_data=self.n.send(self.data)
        return self.receved_data




    def exit_game(self):
        print("All done")





    def design_dice_button(self):
        self.die_btn = tkinter.Button(text="Roll Die", bg="blue", fg="white", width=40)
        self.die_btn['command'] = self.onDiceRoll
        self.die_btn.grid(row=4, column=0, columnspan=2)
        self.window.mainloop()





def main():
    player = UiManager()
    player.design_window()
    player.design_numbers_left_label()
    player.design_img_canvas(getRandNo())
    player.design_score_labels()
    player.design_my_score_value(0)
    player.design_op_score_value(0)
    player.design_dice_button()



main()
