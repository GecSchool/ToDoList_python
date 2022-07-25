from operator import index
import pickle
from datetime import date
from requests import delete


class Cmd:
    def __init__(self):
        self.TdlDict = dict()
        self.loadData()

    def loadData(self):
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
        pass

    def modifyTDL(self):
        key = str(date.today())
        self.TdlDict[key].printTDL()
        index = input('수정할 계획의 번호를 입력하시오')
        AfterTD = input('수정할 내용을 입력하시오')
        self.modifyTDL(index, AfterTD)

    def removeTDL(self):
        key = str(date.today())
        self.TdlDict[key].printTDL()
        index = input('삭제할 계획의 번호를 입력하시오')
        delete(index)

    def showTDL(self):
        key = input('조회 할 날짜를 양식에 맞춰 입력하시오 (YYYY-MM-DD)')
        self.TdlDict[key].printTDL()
        # def deleteTDL():
        # 1. TDL 추가하기
        # 2. TDL 수정하기
        # 3. TDL 완료
        # 4. TDL 삭제하기
        # 5. 이전 TDL 조회하기
        # 6. 프로그램 종료


class TDL:
    class TD:
        def __init__(self, name):
            self.name = name
            self.complete = 'X'

        def printTD(self):
            print(self.name, end="")
            if(self.complete):
                # complete
                print(' ( O )')
            else:
                # madamada
                print(' ( X )')

    def __init__(self):
        self.TDL = list()
        self.key = str(date.today())

    def printTDL(self):
        for index, TD in self.TDL:
            print(index, TD.printTD)

    def addTD(self, name):
        newTD = self.TD(name=name)
        self.TDL.append(newTD)

    def deleteTD(self, index):
        self.TDL.pop(index)

    def modifyTD(self, index, AfterTD):
        self.TDL[index].name = AfterTD


# main
a = Cmd()
a.loadData()
