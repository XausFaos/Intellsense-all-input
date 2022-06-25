import threading
import keyboard
from pynput.mouse import Listener
import eel

codes = {"q": "й", "w": "ц", "e": "у", "r": "к", "t": "е", "y": "н", "u": "г", "i": "ш", "o": "щ", "p": "з", "a": "ф", "s": "ы", "d": "в", "f": "а", "g": "п", "h": "р", "j": "о", "k": "л", "l": "д", "z": "я", "x": "ч", "c": "с", "v": "м", "b": "и", "n": "т", "m": "ь", "Q": "Й", "W": "Ц", "E": "У", "R": "К", "T": "Е", "Y": "Н", "U": "Г", "I": "Ш", "O": "Щ", "P": "З", "A": "Ф", "S": "Ы", "D": "В", "F": "А", "G": "П", "H": "Р", "J": "О", "K": "Л", "L": "Д", "Z": "Я", "X": "Ч", "C": "С", "V": "М", "B": "И", "N": "Т", "M": "Ь",
             ".": "ю", ";": "ж", ",": "б", "[": "х", "]": "ъ", "`": "ё"}

codesForSpecialKeys = {"enter": '\n', "backspace": '', "space": " "}

deleteKeys = ["delete", "shift", "ctrl", "alt", "caps_locktest lang 8932", "tab", "left", "right", "up", "down", "home", "end", "page_up", "page_down", "insert", "pause", "escape", "print_screen", "scroll_lock", "num_lock", "pause", "break", "insert", "help", "menu", "win_left", "win_right", "win_up", "win_down", "win_menu", "win_lock", "win_print", "win_scroll", "win_pause", "win_close", "win_back", "win_forward", "win_refresh", "win_stop", "win_search", "win_favorites", "win_home", "win_start", "win_print", "win_execute", "win_snapshot", "win_delete", "win_help", "win_undo", "win_redo", "win_copy", "win_cut", "win_paste", "win_close", "win_save", "win_open", "win_find", "win_props", "win_stop", "win_print", "win_open",
                "win_close", "win_quit", "win_properties", "win_redo", "win_undo", "win_cut", "win_copy", "win_paste", "win_pastespecial", "win_pageup", "win_pagedown", "win_home", "win_end", "win_insert", "win_delete", "win_selectall", "win_print", "win_printsetup", "win_printpreview", "win_save", "win_open", "win_close", "win_quit", "win_exit", "win_sleep", "win_wake", "win_print", "win_send", "win_spell", "win_cut", "win_copy", "win_paste", "win_pastespecial", "win_attention", "win_contacts", "win_calendar", "win_mail", "win_media", "win_browser", "win_chat", "win_clock", "win_search", "win_connect", "win_games", "win_tools", "win_settings", "win_setup", "win_support", "win_help", "win_unavailable", "win_new", "win_open", "left windows", "alt gr", "esc"]

allowkeys = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM.,;'[]`1234567890-=!@#$%^&*()_+|~<>?/{}\йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ"

def UpdateWords(words):
    eel.getWordsEel(words)
    eel.showWordsEel()
    

class Inputs:

    lastNumEng = ["", "", ""]

    word = ""
    

    def __init__(self, TextFinder):
        threading.Thread(target=self.WaitKey, args=(), daemon=True).start()
        threading.Thread(target=self.WaitMouseKey, args=(), daemon=True).start()
        
        self.textAnalyzer = TextFinder
        self.lang = 'ru'

    def SetGui(self, obj):
        self.gui = obj
        

    def WaitKey(self):
        keyboard.hook(self.PressKey)
        keyboard.wait()


    def WaitMouseKey(self):
        
        def OnClick(x, y, button, pressed):
            if str(button) == "Button.left" and pressed and self.lastNumEng.count("alt") == 3:
                self.gui.SetWindowPosition(x, y)
                self.lastNumEng[-1] = "_"            
            
                
        with Listener(on_click=OnClick) as listener:
            listener.join()


    def AnalyzeKey(self, key):
        if self.lang == 'ru' and key in codes.keys():
            return codes[key]
        
        elif key in allowkeys:
            return key
        
        if key in deleteKeys:
            return ""

        elif key in codesForSpecialKeys.keys():
            return codesForSpecialKeys[key]

        return None


    def AddKeyToLastKeyList(self, key):
        self.lastNumEng.append(key)
        self.lastNumEng.pop(0)

        if len(self.lastNumEng) > 3:
            self.lastNumEng = self.lastNumEng[-3:]


    def CheckCombinations(self):
        # this is for switching language
        if self.lastNumEng[-2] == "left windows" and self.lastNumEng[-1] == "space":
            if self.lang == 'ru':
                self.lang = 'en'
            else:
                self.lang = 'ru'

            eel.setButtonLangText(self.lang)
            return False


        # this combinations is used to screenshot
        if self.lastNumEng[0] == "left windows" and self.lastNumEng[1] == "shift" and self.lastNumEng[2].lower() == "s":
            return False


        # this combination is used to clear input
        if self.lastNumEng[0] == "left windows" and self.lastNumEng[1] == "shift" and self.lastNumEng[2].lower() == "c":
            self.word = ""
            UpdateWords(self.word)
            return False
        
        print(self.lastNumEng)
        if self.lastNumEng[1] == "ctrl" and self.lastNumEng[2] == "right shift":
            self.SendWord()

        return True

    def SendWord(self):
        selectedWord = eel.GetSelectedWordEel()()
        print(selectedWord)
        if selectedWord in ["", " ", None]:
            return
        
        keyboard.write(selectedWord.replace(self.word, ""))
        
        self.word = ""
    
    def PressKey(self, e):
        if e.event_type == 'down':
            
            if e.name == "up":
                eel.prevWordEel()
                return
            
            elif e.name == "down":
                eel.nextWordEel()
                return
            
            #elif e.name == "enter":
            #    return

            self.AddKeyToLastKeyList(e.name)

            allowNext = self.CheckCombinations()
            if not allowNext:
                return

            key = self.AnalyzeKey(e.name)
            print(key)
            
            if key == "":
                self.word = self.word[:-1]
                
            elif key == " ":
                self.word = ""
                
            elif key in deleteKeys:
                self.word += ""
                
            else:
                self.word += key


            potencialWords = self.textAnalyzer.FindWords(self.word)
            UpdateWords(potencialWords)