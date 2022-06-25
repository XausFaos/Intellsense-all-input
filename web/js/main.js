eel.expose(addKeyEel);
eel.expose(getWordsEel);
eel.expose(showWordsEel);
eel.expose(nextWordEel);
eel.expose(prevWordEel);
eel.expose(setButtonLangText);
eel.expose(setWindowsSize);
eel.expose(GetSelectedWordEel);

function addKeyEel(name) {
    globalThis.app.addKey(name);
}

function getWordsEel(words) {
    globalThis.app.getWords(words);
}

function showWordsEel() {
    globalThis.app.showWords();
}

function nextWordEel() {
    globalThis.app.nextWord();
}

function prevWordEel() {
    globalThis.app.previousWord();
}

function setButtonLangText(lang) {
    document.getElementById("lang").innerHTML = `Language: ${lang}`;
}

function setWindowsSize(x, y) {
    console.log(x, y);
    window.resizeTo(x, y);
}

function GetSelectedWordEel() {
    var word = globalThis.app.getWord();
    alert(word);
    if (word) {
        return word;
    }
    return null;
}

window.onload = function() {
    var app = new App();
    window.globalThis.app = app;
}

class App {

    constructor() {
        this.words = [];
        this.selectedWord = 0;
        this.textPressed = document.getElementById('text-pressed');

        async function StartAsync() {
            let lang = await getLanguage();
            setButtonLangText(lang)
        }

        StartAsync();
    }

    addKey(key) {
        if (key == '') {
            this.textPressed.innerHTML = this.textPressed.innerHTML.slice(0, -1);
            return;
        }
        this.textPressed.innerHTML += key;
    }

    getWords(words) {
        this.words = words;
    }

    showWords() {
        this.textPressed.innerHTML = "";
        if (this.words.length != 0) {
            for (var i = 0; i < this.words.length; i++) {
                this.textPressed.innerHTML += `<div class="word">${this.words[i]}</div>`;
            }
            this.updateSelectedWord();
        }
    }

    updateSelectedWord() {
        var words = document.getElementsByClassName('word');
        if (words.lenght == 0) {
            return
        }

        for (var i = 0; i < words.length; i++) {
            words[i].classList.remove('selected');
        }

        if (this.selectedWord > words.length - 1) {
            this.selectedWord = words.length - 1;
        }

        words[this.selectedWord].classList.add('selected');
    }

    nextWord() {
        if (this.selectedWord < this.words.length - 1) {
            this.selectedWord++;
        }
        this.updateSelectedWord();
    }

    previousWord() {
        if (this.selectedWord > 0) {
            this.selectedWord--;
        }
        this.updateSelectedWord();
    }

    getWord() {
        var words = document.getElementsByClassName('word');
        return words[this.selectedWord].innerHTML;
    }
}


async function GetWindowSize() {
    return eel.GetWindowSize()();
}

async function swithLanguage(button) {
    await eel.swithLanguageEel()();
    let lang = await getLanguage();
    setButtonLangText(lang);
}

async function getLanguage() {
    return eel.getLanguageEel()();
}