import random


class Oyun():

    def userinputs(self):
        self.userinput = input("[ tas | kagit | makas ] : ")
        if self.userinput in self.myList:
            return self.userinput
        else:
            "gecersiz"

    def randomSelection(self):
        self.myList = myList = ["tas", "kagit", "makas"]
        self.randomList = random.choice(myList)
        return self.randomList

    def puanlama(self):
        pass

    def gameBrain(self):
        computerscore = 0
        userscore = 0
        self.computerscore = computerscore
        self.userscore = userscore

        def yazdir():
            print(f"Computer : {self.randomList} [] Sen : {self.userinput}")
            print(f"{self.computerscore} - {self.userscore}")

        # __init methodu calısyor zaten o yüzden eklemedim
        while True:
            if self.computerscore == 3 or self.userscore == 3:
                if self.computerscore == 3:
                    print(f"Kazanan Computer \n Skorlar : {self.computerscore} - {self.userscore}")
                else:
                    print(f"Kazanan Sensin \n Skorlar : {self.computerscore} - {self.userscore}")
                a = input("tekrar oynamak ister misin (e/h)")
                if a == "e":
                    self.computerscore = 0
                    self.userscore = 0
                    print("Oyun tekrar başlatıldı :) Bol şans\n\n")
                else:
                    break

            self.randomSelection()
            self.userinputs()
            if self.randomList == self.userinput:
                print(f"{self.randomList} {self.userinput} Berabere")
            else:

                if self.userinput == "tas":
                    if self.randomList == "kagit":
                        self.computerscore += 1
                        yazdir()
                    else:
                        self.userscore += 1
                        yazdir()

                if self.userinput == "kagit":
                    if self.randomList == "makas":
                        self.computerscore += 1
                        yazdir()
                    else:
                        self.userscore += 1
                        yazdir()

                if self.userinput == "makas":
                    if self.randomList == "tas":
                        self.computerscore += 1
                        yazdir()
                    else:
                        self.userscore += 1
                        yazdir()


s1 = Oyun()
s1.gameBrain()
