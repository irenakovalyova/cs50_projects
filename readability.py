from cs50 import get_string

def alphacount(txt):
    l = 0
    i = 0
    for i in range(0, len(txt)):
        if txt[i].isalpha():
            l += 1
    return l
    
def wordcount(txt):
    w = 1
    i = 1
    for i in range(0, len(txt)):
        if txt[i].isspace():
            w += 1
    return w

def sentcount(txt):
    s = 0
    for i in range(0, len(txt)):
        if (txt[i] == '!' or txt[i] == '.' or txt[i] == '?'):
            s += 1
    return s

def main():
    text = get_string("Text: ")
    letters = alphacount(text)
    words = wordcount(text)
    sentences = sentcount(text)
    
    print(letters)
    print(words)
    print(sentences)
    
    l = (letters * 100) / words
    s = (sentences * 100) / words
    index = (0.0588 * l) - (0.296 * s) - 15.8
    
    print(index)
    
    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {int(round(index))}")
        
if __name__ == "__main__":
    main()