class New_phrase:
    def __init__(self, phrase, mode, n):
        self.phrase = phrase
        self.mode = mode
        self.n = n
    def __str__(self):
        return

class Translation:
    def __init__(self,new_phrase):
        self.new_phrase = new_phrase
    def translation(self):
        letters = ' abcdefghijklmnopqrstuvwxyz'
        n = self.new_phrase.n
        translation = ""
        for i in self.new_phrase.phrase:
            if self.new_phrase.mode == "right":
                translation += letters[(letters.index(i) + n) % len(letters)]
            else:
                translation += letters[(letters.index(i) - n) % len(letters)]
        return f"The translation is {translation}"

def new_phrase():
    print ("Use only  English letters!\n")
    phrase = input("Enter your word/phrase: ")
    phrase = phrase.lower()
    A = True
    while A == True:
        B = True
        while B == True:
            mode = input("\nChoose the mode\n"
                         "1 - shift to the right\n"
                         "2 - shift to the left\n"
                         "Your value:  ")
            if mode == "1":
                print("\nAll letters will be shifted to the right!")
                mode = "right"
                B = False
            elif mode == "2":
                print("\nAll letters will be shifted to the left!")
                mode = "left"
                B = False
            else:
                B = True
        C = True
        while C == True:
            n = input("\nEnter the number of steps: ")
            if n.isdigit() == False:
                print("Please, use only non-negative integers!")
            else:
                n = int(n)
                C = False
        print(f"\nYour phrase: {phrase}; \nWe'll shift letters to the {mode} by {n}")
        q = input("\nDo you want to change sth? (y/whatever you want for no):  ")
        if q == "y":
            A = True
        else:
            A = False
    new_phrase = New_phrase(phrase, mode, n)
    translation = Translation(new_phrase)
    print(translation.translation())

if __name__ == "__main__":
    new_phrase()