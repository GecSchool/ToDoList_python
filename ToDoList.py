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
            pass
        else:
            todayTDL = TDL()
            self.TdlDict.update({key: todayTDL})

    def appendTDL(self):
        key = str(date.today())
        print('Before')
        self.printTDL(key=key)
        newTD = input('새로 추가할 계획을 입력하시오 : ')
        self.TdlDict[key].addTD(newTD)
        print('After')
        self.printTDL(key=key)

    def modifyTDL(self):
        key = str(date.today())
        self.printTDL(key=key)
        while True:
            try:
                index = int(input('수정할 계획의 번호를 입력하시오 : '))
                break
            except ValueError as e:
                print('잘못된 값을 입력했습니다, 숫자값를 입력하십시요.')
        AfterTD = input('수정할 내용을 입력하시오 : ')
        print('Before')
        self.TdlDict[key].modifyTD(index-1, AfterTD)
        print('After')
        self.printTDL(key=key)

    def removeTD(self):
        key = str(date.today())
        print('Before')
        self.printTDL(key=key)
        while True:
            try:
                index = int(input('삭제할 계획의 번호를 입력하시오 : '))
                break
            except ValueError as e:
                print('잘못된 값을 입력했습니다, 숫자값를 입력하십시요.')
        print('After')
        self.TdlDict[key].deleteTD(index-1)
        self.printTDL(key=key)

    def showTDL(self):
        while True:
            key = input('조회 할 날짜를 양식에 맞춰 입력하시오 (YYYY-MM-DD) : ')
            try:
                self.printTDL(key=key)
                break
            except KeyError as e:
                print('잘못된 입력이 들어왔습니다. 다시 입력하시오')

    def completeTD(self):
        key = str(date.today())
        print('Before')
        self.printTDL(key=key)
        while True:
            try:
                index = int(input('완료한 계획의 번호를 입력하시오 : '))
                break
            except ValueError as e:
                print('잘못된 값을 입력했습니다, 숫자값를 입력하십시요.')
        self.TdlDict[key].complete(index-1)
        print('After')
        self.printTDL(key=key)

    def printTDL(self, key):
        key = str(date.today())
        print('-------------------------------')
        if(len(self.TdlDict[key].TDL)):
            self.TdlDict[key].printTDL()
        else:
            print('empty')
        print('-------------------------------')


class TD:
    def __init__(self, name):
        self.name = name
        self.complete = 'X'

    def printTD(self, index):
        print('{}. {} ( {} )'.format(index, self.name, self.complete))


class TDL:

    def __init__(self):
        self.TDL = list()
        self.key = str(date.today())

    def printTDL(self):
        for index, TD in enumerate(self.TDL, 1):
            TD.printTD(index)

    def addTD(self, name):
        newTD = TD(name=name)
        self.TDL.append(newTD)

    def deleteTD(self, index):
        try:
            self.TDL.pop(index)
        except IndexError:
            print('잘못된 값을 입력했습니다.')

    def modifyTD(self, index, modifyedTD):
        try:
            self.TDL[index].name = modifyedTD
        except IndexError:
            print('잘못된 값을 입력했습니다.')

    def complete(self, index):
        try:
            self.TDL[index].complete = 'O'
        except IndexError:
            print('잘못된 값을 입력했습니다.')


# main
os.system('CLS')
cmd = Cmd()
print('오늘의 To Do List')
cmd.printTDL(str(date.today()))
while True:
    curCmd = input('''
사용할 기능에 맞는 숫자를 입력하시오

1) 금일 To Do List 추가하기
2) 금일 To Do List 삭제하기
3) 금일 To Do List 수정하기
4) To Do List 완료 마킹하기
5) 지난 To Do List 조회하기
6) 프로그램 종료
    
    ''')
    os.system('CLS')
    if curCmd == '1':
        cmd.appendTDL()
    elif curCmd == '2':
        cmd.removeTD()
    elif curCmd == '3':
        cmd.modifyTDL()
    elif curCmd == '4':
        cmd.completeTD()
    elif curCmd == '5':
        cmd.showTDL()
    elif curCmd == '6':
        cmd.exitProgram()
        break
    else:
        print('잘못 된 숫자를 입력했습니다. 다시 입력해 주세요')
