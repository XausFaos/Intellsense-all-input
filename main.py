import keyboard
import threading
import eel
import keyboard


def UpdateWords(words):
    eel.getWordsEel(words)
    eel.showWordsEel()
    
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

class Keyboard:

    # create codes to conver eng to rus
    codes = {"q": "й", "w": "ц", "e": "у", "r": "к", "t": "е", "y": "н", "u": "г", "i": "ш", "o": "щ", "p": "з", "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п", "h": "р", "j": "о", "k": "л", "l": "д", "z": "я", "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т", "m": "ь", "Q": "Й", "W": "Ц", "E": "У", "R": "К", "T": "Е", "Y": "Н", "U": "Г", "I": "Ш", "O": "Щ", "P": "З", "A": "Ф", "S": "Ы", "D": "В", "F": "А", "G": "П", "H": "Р", "J": "О", "K": "Л", "L": "Д", "Z": "Я", "X": "Ч", "C": "С", "V": "М", "B": "И", "N": "Т", "M": "Ь",
             ".": "ю", ";": "ж", ",": "б", "[": "х", "]": "ъ", "`": "ё"}

    codesForSpecialKeys = {"enter": '\n', "backspace": '', "space": " "}
    deleteKeys = ["delete", "shift", "ctrl", "alt", "caps_locktest lang 8932", "tab", "left", "right", "up", "down", "home", "end", "page_up", "page_down", "insert", "pause", "escape", "print_screen", "scroll_lock", "num_lock", "pause", "break", "insert", "help", "menu", "win_left", "win_right", "win_up", "win_down", "win_menu", "win_lock", "win_print", "win_scroll", "win_pause", "win_close", "win_back", "win_forward", "win_refresh", "win_stop", "win_search", "win_favorites", "win_home", "win_start", "win_print", "win_execute", "win_snapshot", "win_delete", "win_help", "win_undo", "win_redo", "win_copy", "win_cut", "win_paste", "win_close", "win_save", "win_open", "win_find", "win_props", "win_stop", "win_print", "win_open",
                  "win_close", "win_quit", "win_properties", "win_redo", "win_undo", "win_cut", "win_copy", "win_paste", "win_pastespecial", "win_pageup", "win_pagedown", "win_home", "win_end", "win_insert", "win_delete", "win_selectall", "win_print", "win_printsetup", "win_printpreview", "win_save", "win_open", "win_close", "win_quit", "win_exit", "win_sleep", "win_wake", "win_print", "win_send", "win_spell", "win_cut", "win_copy", "win_paste", "win_pastespecial", "win_attention", "win_contacts", "win_calendar", "win_mail", "win_media", "win_browser", "win_chat", "win_clock", "win_search", "win_connect", "win_games", "win_tools", "win_settings", "win_setup", "win_support", "win_help", "win_unavailable", "win_new", "win_open", "left windows", "alt gr", "esc"]

    lastNumEng = ["", "", ""]
    
    word = ""

    def __init__(self,TextFinder):
        threading.Thread(target=self.waitKey, args=(), daemon=True).start()
        self.textAnalyzer = TextFinder
        self.lang = 'ru'

    def waitKey(self):
        keyboard.hook(self.pressKey)
        keyboard.wait()

    def analyze_key(self, key):
        if key in self.deleteKeys:
            return ""

        if self.lang == 'ru' and key in self.codes.keys():
            key = self.codes[key]

        elif key in self.codesForSpecialKeys.keys():
            key = self.codesForSpecialKeys[key]

        return key

    def add_key_to_last_key_list(self, key):
        self.lastNumEng.append(key)
        self.lastNumEng.pop(0)
        
        if len(self.lastNumEng) > 3:
            self.lastNumEng = self.lastNumEng[-3:]
            
    def chekCombinations(self):
        print(self.lastNumEng)
        def switch_lang():
            if self.lang == 'ru':
                self.lang = 'en'
            else:
                self.lang = 'ru'
        
        if self.lastNumEng[-2] == "left windows" and self.lastNumEng[-1] == "space":
            print("Switch lang")
            switch_lang()
            self.add_key_to_last_key_list("")
        
        if self.lastNumEng[0] == "left windows" and self.lastNumEng[1] == "shift" and (self.lastNumEng[2].lower() in ["s", "ы"]):
            return False
        
        return True
            
    def pressKey(self, e):            
        if e.event_type == 'down':
            
            if e.name == "up":
                eel.prevWordEel()
                print("Previous word")
                return
            
            if e.name == "down":
                eel.nextWordEel()
                print("Next word")
                return
        
            self.add_key_to_last_key_list(e.name)
            
            allowNext = self.chekCombinations()
            print(allowNext)
            if not allowNext:
                return
            
            key = self.analyze_key(e.name)
            
            if key == "":
                print("Backspace")
                self.word = self.word[:-1]
            elif key == " ":
                self.word = ""
            elif key in self.deleteKeys:
                self.word += ""
            else:
                self.word += key
                print("Word: " + self.word)

            potencialWords = textAnalyzer.FindWords(self.word)
            print(potencialWords)
            UpdateWords(potencialWords)

class GUI:

    def __init__(self):
        eel.init('web')
        eel.start('main.html', size=(300, 300))


@eel.expose
def swithLanguageEel():
    lang = getLanguageEel()
    if lang == 'ru':
        setLanguage('en')
        return
    
    setLanguage('ru')

@eel.expose 
def getLanguageEel():
    print(board.lang)
    return board.lang

def setLanguage(lang):
    board.lang = lang

if __name__ == "__main__":

    textAnalyzer = TextFinder("words.txt")
    board = Keyboard(textAnalyzer)
    gui = GUI()
