#!/usr/bin/python3

import pickle


class Example:
    
    def __init__(self, value1, value2 , value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        
    def __str__(self):
        return "{} {} {}".format(self.value1, self.value2, self.value3)

    
class ExampleList:
    exampleList = []

    def __init__(self):
        exampleFileList = open("files/external_file", "ab+")
        exampleFileList.seek(0)
        try:
            self.exampleList = pickle.load(exampleFileList)
            print("{} people were loaded in the file".format(len(self.exampleList)))
        except:
            print("The file is empty")
        finally:
            exampleFileList.close()

    def addExample(self, persona):
        self.exampleList.append(persona)
    
    def showExample(self):
        for persona in self.exampleList:
            print(persona)

    def saveExampleListInFile(self):
        exampleFileList = open("files/external_file", "wb")
        print("{} people were saved in the file".format(len(self.exampleList)))
        pickle.dump(self.exampleList, exampleFileList)
        exampleFileList.close()
        del(exampleFileList)

    def showExampleListInFile(self):
        print("The following records have been saved:")
        for persona in self.exampleList:
            print(persona)


miLista = ExampleList()

persona = Example("aaaa", "bbbb", 10)
miLista.addExample(persona)
persona = Example("cccc", "dddd", 43)
miLista.addExample(persona)

miLista.saveExampleListInFile()
miLista.showExampleListInFile()
