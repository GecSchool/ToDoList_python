import pickle
from datetime import date
import os


class Cmd:
    def __init__(self):
        self.TdlDict = dict()
        self.loadData()
        self.addTDL()

    def loadData(self):
        if os.path.getsize('TDL_DATA.b') > 0:
            with open('TDL_DATA.b', "rb") as file:
                self.TdlDict = pickle.load(file)

    def saveData(self):
        with open('TDL_DATA.b', "wb") as file:
            pickle.dump(self.TdlDict, file)

    def exitProgram(self):
        self.saveData()

    def addTDL(self):
        key = str(date.today())
        if key in self.TdlDict:
            # exist
            pass
        else:
            # none
            todayTDL = TDL()
            self.TdlDict.update({key: todayTDL})

        # def mainFuntion():
        # def startScreen():
        # def mainScreen():
    def appendTDL(self):
        key = str(date.today())
        self.TdlDict[key].printTDL()
        newTD = input('새로 추가할 계획을 입력하시오 : ')
        self.TdlDict[key].addTD(newTD)

    def modifyTDL(self):
        key = str(date.today())
        self.TdlDict[key].printTDL()
        index = int(input('수정할 계획의 번호를 입력하시오 : '))
        AfterTD = input('수정할 내용을 입력하시오 : ')
        self.TdlDict[key].modifyTD(index-1, AfterTD)

    def removeTD(self):
        key = str(date.today())
        self.TdlDict[key].printTDL()
        index = int(input('삭제할 계획의 번호를 입력하시오 : '))
        self.TdlDict[key].deleteTD(index-1)

    def showTDL(self):
        key = input('조회 할 날짜를 양식에 맞춰 입력하시오 (YYYY-MM-DD) : ')
        self.TdlDict[key].printTDL()

    def completeTD(self)
    key = str(date.today())
    index = int(input('완료한 계획의 번호를 입력하시오 : '))
    self.TdlDict[key].complete(index-1)
    # 1. TDL 추가하기
    # 2. TDL 수정하기
    # 3. TDL 완료
    # 4. TDL 삭제하기
    # 5. 이전 TDL 조회하기
    # 6. 프로그램 종료


class TD:
    def __init__(self, name):
        self.name = name
        self.complete = 'X'

    def printTD(self):
        print('{} ( {} )'.format(self.name, self.complete))


class TDL:

    def __init__(self):
        self.TDL = list()
        self.key = str(date.today())

    def printTDL(self):
        for index, TD in enumerate(self.TDL, 1):
            print(index, end=" ")
            TD.printTD()

    def addTD(self, name):
        newTD = TD(name=name)
        self.TDL.append(newTD)

    def deleteTD(self, index):
        self.TDL.pop(index)

    def modifyTD(self, index, modifyedTD):
        self.TDL[index].name = modifyedTD

    def complete(self, index):
        self.TDL[index].complete = 'O'


# main
a = Cmd()
a.appendTDL()
a.appendTDL()
a.modifyTDL()
a.removeTD()
a.appendTDL()
a.exitProgram()
