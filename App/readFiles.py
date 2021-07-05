import file_preprocess
import getTriplets_B
import drawKG
import re
#files=["Doc.txt","s.txt"]
triplets = {}
def process_files(files):
    for i in files:
        try:
            j='Files\\'+i
            f=open(j,'r',encoding='utf-8')
            text=f.read().replace('\n',' ')
            #print(text)
        
        finally:
            f.close()

        text=file_preprocess.clean(text)



        pattern = re.compile("[0-9]+.")
        from nltk import tokenize
        def getSentences(text):
            return tokenize.sent_tokenize(text)

        sentences = getSentences(text)
        
        for sentence in sentences:
            if(pattern.fullmatch(sentence)!=None):
                sentences.remove(sentence)
                
        t=getTriplets_B.fin(sentences)
        triplets[i]=t
        drawKG.printGraph(t,i.split(".")[0])
    return triplets


