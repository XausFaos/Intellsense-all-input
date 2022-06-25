import eel
import GUI
import Inputs


class TextFinder:

    def __init__(self, filename: str):
        with open(filename, "r", encoding="utf-8") as file:
            self.words = file.read().split("\n")

    def FindWords(self, text: str):
        text = text.lower()
        if text == "":
            return []

        wordsList = []
        for word in self.words:
            if word.lower().startswith(text):
                wordsList.append(word)

        return wordsList


@eel.expose
def swithLanguageEel():
    lang = getLanguageEel()
    if lang == 'ru':
        setLanguage('en')
        return

    setLanguage('ru')

@eel.expose
def getLanguageEel():
    return board.lang


def setLanguage(lang):
    board.lang = lang

    
if __name__ == "__main__":
    
    textAnalyzer = TextFinder("words.txt")
    board = Inputs.Inputs(textAnalyzer)
    gui = GUI.GUI(board)

# решить проблему с resize при перемещении окна