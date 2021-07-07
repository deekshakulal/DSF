#prefered one
#since it simplifies the sentence first 

import nltk
from pycorenlp import *
import collections
import json
nlp=StanfordCoreNLP("http://localhost:9000/")
import getTriplets_C
import simplifier

cons = [",","and","but","or","when","than","because","while",'so', 'though', 'since', 'until', 'whether', 'before', 'though', 'nor', 'like','unless','except']

#sn=["If it was nice i would have taken that", "She was confused but she managed to handle it"]

def fin(sn):
    ans=[]

    def tripsA(sn):
        for sent in sn:
            #print("sent->",sent)
            l=[]
            if(any(i in sent for i in cons)):
                #print("simp->",sent)
                sent=simplifier.simplification(sent)
                #print("fied,",sent)
            else:
                sent=[sent]
                #print(sent)
            for s in sent:
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
                            res=getTriplets_C.tripsC(s)
                            for r in res:
                                ans.append(r)

                except:
                    res=getTriplets_C.tripsC(s)
                    for r in res:
                        ans.append(r)
    #lemmatization 
    def getlemma(x):
        tokens = getTriplets_C.nlp_model(x)
        #print('Tokens-->',tokens)
        for token in tokens:
            if "punct" in token.dep_:
                continue
            if getTriplets_C.isRelationCandidate(token):
                lem=token.lemma_
        return lem
    tripsA(sn)
    return ans

#print(fin(sn))  
#tripsA(s)








 #,"openie.triple.strict":"true","openie.max_entailments_per_clause":"1"