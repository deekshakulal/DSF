#this is for text file with simple sentences from which proper triplets can be extracted


import nltk
from pycorenlp import *
import collections
import json
nlp=StanfordCoreNLP("http://localhost:9000/")
import getTriplets_C
import simplifier


#sn=["That was big ", "She was confused but she managed to handle it"]

def fin(sn):
    ans=[]

    def tripsA(sn):
        for s in sn:
            #print(s)
            try:
                
                # op = nlp.annotate(s, properties={"annotators":"tokenize,ssplit,pos,lemma,depparse,natlog,openie",
                #                                  "outputFormat": "json","openie.triple.strict":"true","openie.max_entailments_per_clause":"3"})
                op = nlp.annotate(s)
                output= json.loads(op)
                #print(op)
                result = [output["sentences"][0]["openie"] for item in output]
                for i in result:
                    if(len(i)!=0):
                        for rel in i:
                            relatn=getlemma(rel['relation'])
                            relationSent=rel['subject'],relatn,rel['object']
                            #relationSent=rel['subject'],rel['relation'],rel['object']
                            #print(relationSent)
                            ans.append(list(relationSent))
                    else:
                        
                        ss=simplifier.simplification(s)
                        #print("ss-->",ss[0],s)
                        if(ss[0]!=s):
                            tripsA(ss)
                        else:
                            res=getTriplets_C.tripsC(s)
                            for r in res:
                                ans.append(r)

            except:
                res=getTriplets_C.tripsC(s)
                for r in res:
                    ans.append(r)
    #lemmatization only if required uncomment it and call above 
    def getlemma(x):
        tokens = getTriplets_C.nlp_model(x)
        print('Tokens-->',tokens)
        for token in tokens:
            if "punct" in token.dep_:
                continue
            if getTriplets_C.isRelationCandidate(token):
                print(token.lemma_)
        return token.lemma_
    tripsA(sn)
    return ans

#print(fin(sn))  
#tripsA(s)








 #,"openie.triple.strict":"true","openie.max_entailments_per_clause":"1"