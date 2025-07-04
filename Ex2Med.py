def countWords(text):
    dict={}
    cleanText= text.lower().replace(".", "")
    for word in cleanText.lower().split():
        dict[word]=0
    for word in cleanText.lower().split():
        dict[word]+=1
    return dict       



message="AI is the future. The future is now"
print(countWords(message))