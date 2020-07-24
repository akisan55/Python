import tkinter
import random
import numpy


class game:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('1540x800')
        self.root.title('Multi Color Puzzle')
        self.canvas = tkinter.Canvas(self.root, width=1540, height=800, bg="gold")
        self.canvas.place(x=0, y=0)
        self.label = tkinter.Label(self.root, text="SPACE KEY を押してスタート", font=("system", 30), bg="gold")
        self.label.place(x=550, y=200)
        self.numlist = []
        (self.x3, self.y3) = 1200, 200
        self.score = 0
        self.label_ = {0: tkinter.Label(self.root, text="SPACE KEY を押してスタート", font=("system", 30), bg="gold"),
                       2: tkinter.Label(self.root, text="GAMEOVER", font=("system", 500), bg="gold"),
                       3: tkinter.Label(self.root, text="LEVEL1", font=("system", 70)),
                       4: tkinter.Label(self.root, text="SCORE＝" + str(self.score), font=("system", 50)),
                       }
        self.color_list = {1: "red", 2: "blue", 3: "gold", 4: "limegreen", 5: "deeppink", 6: "purple", 7: "cyan",
                           8: "orange", 9: "ivory", 10: "navy", 11: "violet", 12: "indianred", 13: "gainsboro",
                           14: "mistyrose", 15: "skyblue", 16: "khaki", 17: "coral", 18: "greenyellow", 19: "tan",
                           20: "snow", 21: "maroon", 22: "olive", 23: "crimson", 24: "green"}
        self.a = numpy.array([6] * 24)
        self.exlist = [495, 545, 595, 645, 695, 745, 795, 845, 895, 945, 995, 1045]
        self.exlistArray = numpy.array(self.exlist)
        self.eylist = [125, 175, 225, 275, 325, 375, 375, 425, 475, 525, 575, 625, 675]
        self.eylistArray = numpy.array(self.eylist)
        self.list_move = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
        self.key = ""
        self.index = 0
        self.x2 = 250
        self.y2 = 70

    def key_down(self, e):
        self.key = e.keysym
        if self.index == 0:
            if self.key == "space":
                self.canvas.delete("all")
                self.label.place_forget()
                self.index += 1
                self.main_two()

    def now_square(self):
        self.canvas.create_rectangle(self.x3, self.y3, self.x3 + 70, self.y3 + 70, fill="#E6E6FA", outline="navy",
                                     width=4)

    def square(self):
        self.canvas.create_rectangle(self.x1, self.y1, self.x1 + 50, self.y1 + 50, fill=self.color)
        self.canvas.create_rectangle(self.x1 + 30, self.y1 + 5, self.x1 + 45, self.y1 + 10, fill="white",
                                     outline="white", width=0)
        self.canvas.create_rectangle(self.x1 + 40, self.y1 + 10, self.x1 + 45, self.y1 + 20, fill="white", width=0)
        self.canvas.create_rectangle(self.x1 + 40, self.y1 + 25, self.x1 + 45, self.y1 + 30, fill="white",
                                     outline="black", width=1)
        self.canvas.create_line(self.x1 + 30, self.y1 + 5, self.x1 + 45, self.y1 + 5, self.x1 + 45, self.y1 + 5,
                                self.x1 + 45, self.y1 + 20, self.x1 + 40, self.y1 + 20,
                                self.x1 + 45,
                                self.y1 + 20, fill="black", width=1)
        self.canvas.create_line(self.x1 + 30, self.y1 + 5, self.x1 + 30, self.y1 + 10, self.x1 + 30, self.y1 + 10,
                                self.x1 + 40, self.y1 + 10, self.x1 + 40, self.y1 + 10,
                                self.x1 + 40,
                                self.y1 + 20, fill="black", width=1)

    def block_move_sub(self):
        self.canvas.delete("all")
        self.label_[2] = tkinter.Label(self.root, text="GAMEOVER", font=("system", 500), bg="gold")
        self.label_[2].place(x=550, y=200)
        self.label_[3].place_forget()
        self.index += 1
        self.numlist.extend([self.score])
        self.label_[5] = tkinter.Label(self.root, text="最高得点は" + str(max(self.numlist)), font=("system", 50))
        self.label_[5].place(x=10, y=720)
        for i in range(6, 30):
            self.label_[i].place_forget()
        self.root.after(5000, self.main_two_sub)

    def block_move(self, e):
        if self.index == 1:
            self.point_y = e.y
            self.point_x = e.x
            self.pos_x = (numpy.abs(self.exlistArray - self.point_x)).argmin()
            self.pos_y = (numpy.abs(self.eylistArray - self.point_y)).argmin()
            exnumber = self.exlistArray[self.pos_x] - 25
            eynumber = self.eylistArray[self.pos_y] - 25
            list_number = int(((exnumber - 470) / 50 + (eynumber - 100) / 50 * 12) + 12)
            if self.list_move[list_number] == 0:
                if self.point_x >= 470 and self.point_x <= 1070 and self.point_y >= 100 and self.point_y <= 700:
                    self.x1 = exnumber
                    self.y1 = eynumber
                    self.square()
                    self.list_move[list_number] = self.brn
                    if self.list_move[list_number - 1] == self.brn or self.list_move[list_number + 1] == self.brn or \
                            self.list_move[
                                list_number - 12] == self.brn or self.list_move[list_number + 12] == self.brn:
                        self.root.after(500, self.block_move_sub)
                    else:
                        self.score += 3
                        self.score_pack()
                        self.label_[6].place_forget()
                        self.label_[7].place_forget()
                        for i in range(8, 30):
                            self.label_[i].place_forget()
                        self.color_determine()
        else:
            pass

    def color_determine(self):
        self.block_number = random.randint(1, 24)
        self.brn = self.block_number
        w = "white"
        self.x1 = self.x3 + 10
        self.y1 = self.y3 + 10
        if self.index == 1:
            tmp = 0
            for i in range(1, 25):
                if self.brn == i and self.a[i] != 0:
                    tmp = 1
                    self.a[self.brn - 1] -= 1
                    self.color = self.color_list[self.brn]
                    break

            if tmp == 0:
                self.block_number = random.randint(1, 24)
                self.brn = self.block_number
                self.root.after(1, self.color_determine)
            for i in range(6, 30):
                self.label_[i] = tkinter.Label(self.root, text="＝" + str(self.a[i - 6]), font=(None, 10), bg=w)

        k = 6
        for i in range(285, 605, 40):
            for j in range(45, 345, 100):
                self.label_[k].place(x=j, y=i)
        self.square()
        self.score_pack()

    def canvas_delete_all(self):
        self.canvas.delete("all")
        self.main_tree()

    def main_two(self):
        self.canvas.create_rectangle(0, 0, 1540, 1540, fill="black")
        self.score = 0
        self.root.after(3000, self.canvas_delete_all)

    def main_two_sub(self):
        self.label_[2].place_forget()
        self.score = 0
        self.score_pack()
        self.index -= 1
        if __name__ == "__main__":
            self.main_two()

    def score_pack(self):
        self.label_[4].place_forget()
        self.label_[4] = tkinter.Label(self.root, text="SCORE＝" + str(self.score), font=("system", 50))
        self.label_[4].place(x=10, y=170)

    def main_tree(self):
        self.label_[3] = tkinter.Label(self.root, text="LEVEL1", font=("system", 70))
        self.label_[3].place(x=10, y=10)
        self.label_[4] = tkinter.Label(self.root, text="SCORE＝" + str(self.score), font=("system", 50))
        self.label_[4].place(x=10, y=170)
        self.canvas.create_rectangle(470, 100, 470 + 600, 100 + 600, fill="#E6E6FA", width=0)
        self.canvas.create_rectangle(420, 50, 470, 750, fill="#006400", width=0)
        self.canvas.create_rectangle(420, 50, 1120, 100, fill="#006400", width=0)
        self.canvas.create_rectangle(1070, 50, 1120, 750, fill="#006400", width=0)
        self.canvas.create_rectangle(420, 700, 1120, 750, fill="#006400", width=0)
        for i in range(13):
            y = i * 50 + 100
            self.canvas.create_line(470, y, 1070, y, fill="black")
            x = i * 50 + 470
            self.canvas.create_line(x, 100, x, 700, fill="black")
        self.now_square()
        self.canvas.create_rectangle(10, 280, 300, 600, fill="white")
        self.canvas.create_rectangle(20, 290, 40, 310, fill="red")
        self.canvas.create_rectangle(120, 290, 140, 310, fill="blue")
        self.canvas.create_rectangle(220, 290, 240, 310, fill="gold")
        self.canvas.create_rectangle(20, 330, 40, 350, fill="limegreen")
        self.canvas.create_rectangle(120, 330, 140, 350, fill="deeppink")
        self.canvas.create_rectangle(220, 330, 240, 350, fill="purple")
        self.canvas.create_rectangle(20, 370, 40, 390, fill="cyan")
        self.canvas.create_rectangle(120, 370, 140, 390, fill="orange")
        self.canvas.create_rectangle(220, 370, 240, 390, fill="ivory")
        self.canvas.create_rectangle(20, 410, 40, 430, fill="navy")
        self.canvas.create_rectangle(120, 410, 140, 430, fill="violet")
        self.canvas.create_rectangle(220, 410, 240, 430, fill="indianred")
        self.canvas.create_rectangle(20, 450, 40, 470, fill="gainsboro")
        self.canvas.create_rectangle(120, 450, 140, 470, fill="mistyrose")
        self.canvas.create_rectangle(220, 450, 240, 470, fill="skyblue")
        self.canvas.create_rectangle(20, 490, 40, 510, fill="khaki")
        self.canvas.create_rectangle(120, 490, 140, 510, fill="coral")
        self.canvas.create_rectangle(220, 490, 240, 510, fill="greenyellow")
        self.canvas.create_rectangle(20, 530, 40, 550, fill="tan")
        self.canvas.create_rectangle(120, 530, 140, 550, fill="snow")
        self.canvas.create_rectangle(220, 530, 240, 550, fill="maroon")
        self.canvas.create_rectangle(20, 570, 40, 590, fill="olive")
        self.canvas.create_rectangle(120, 570, 140, 590, fill="crimson")
        self.canvas.create_rectangle(220, 570, 240, 590, fill="green")
        self.color_determine()
        self.canvas.bind("<1>", self.block_move)

    def start(self):
        self.root.bind("<Key>", self.key_down)
        self.root.mainloop()


if __name__ == "__main__":
    game().start()
