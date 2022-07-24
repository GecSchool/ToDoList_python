import pickle
from datetime import date


class Cmd:
    def __init__(self):
        self.TdlDict = dict()

    def loadData(self):
        with open('TDL_DATA.txt', "rb") as file:
            self.TdlDict = pickle.load(file)

    def saveData(self):
        with open('TDL_DATA.txt', "wb") as file:
            pickle.dump(self.TdlDict, file)

    def addTDL(self):

        # def mainFuntion():
        # def startScreen():
        # def mainScreen():

        # def modifyTDL():
        # def removeTDL():
        # def showExTDL():
        # def deleteTDL():
        # 1. TDL 추가하기
        # 2. TDL 수정하기
        # 3. TDL 완료
        # 4. TDL 삭제하기
        # 5. 이전 TDL 조회하기
        # 6. 프로그램 종료


class TDL:
    def __init__(self):
        self.TDL = list()
        self.key = str(date.today())

    def printTDL(self):
        for TD in self.TDL:
            print(TD.printTD)

    def addTD(self):
        name = input()
        newTD = TD(name=name)
        self.TDL.append(newTD)


class TD:
    def __init__(self, name):
        self.name = name
        self.complete = 'X'

    def printTD(self):
        print(self.name, end="")
        if(self.complete):
            # complete
            print('   ( O )')
        else:
            # madamada
            print('   ( X )')


# main
a = Cmd()
a.loadData()
