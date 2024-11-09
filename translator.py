import random
import subprocess

wordDictionary = {"idc" : ["🤷"],
                  "mad" : ["😡","🤬"],
                  "angry" : ["😡","🤬"],
                  "love" : ["❤️"],
                  "sun" : ["🌞", "☀️"],
                  "moon" : ["🌕", "🌑", "🌙", "🌚"],
                  "cookie" : ["🍪"],
                  "ggb" : ["🌉", "🌁"],
                  "tired" : ["🥱"],
                  "christmas" : ["🎅", "🎄"],
                  "you" : ["🫵"],
                  "snow" : ["🌨️", "❄️"],
                  "today" : ["📆"],
                  "to": ["2️⃣"],
                  "two": ["2️⃣"],
                  "too": ["2️⃣"],
                  "2" : ["2️⃣"],
                  "hi" : ["👋"],
                  "hello" : ["👋"],
                  "hey" : ["👋"],
                  
}

while True:
    scriptOutput = ""
    userInput = input("Input a sentence, idiot. ").lower().split()
    
    for word in userInput:
        if word in wordDictionary:
            emojiList = wordDictionary[word] 
            scriptOutput = scriptOutput + " " + emojiList[random.randint(0, len(emojiList)-1)]    

        else:  
            scriptOutput = scriptOutput + " " + word
    
    applescript = 'display dialog "'+ scriptOutput + """" ¬
    with title "This is a pop-up window" ¬
    with icon caution ¬
    buttons {"Done"}
    """
    subprocess.call("osascript -e '{}'".format(applescript), shell=True)




