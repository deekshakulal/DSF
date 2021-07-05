import sys
import spacy
#text="confused and frustrated, connie decides to leave on her own. later, a woman’s scream is heard in the distance. christian is then paralyzed by an elder. the temple is set on fire. outside, the cult wails with him. it's a parable of a woman's religious awakening— c. mackenzie, and craig vincent joined the cast. later, craig di francia and action bronson were revealed to have joined the cast. sebastian maniscalco and paul ben-victor were later revealed as being part of the cast. we just tried to make the film. we went through all these tests and things m global was also circling to bid for the film's international sales rights. canadian musician robbie robertson supervised the soundtrack. it features both original and existing music tracks. it is the worst reviewed film in the franchise. but she injures quicksilver and accidentally kills mystique before flying away. military forces tasked with her arrest."
#text="she was confused"

from spacy.lang.en import English

nlp_model = spacy.load('en_core_web_sm')

def getSentences(text):
    nlp = English()
    nlp.add_pipe('sentencizer')
    document = nlp(text)
    return [sent.text.strip() for sent in document.sents]

def printToken(token):
    print(token.text, "->", token.dep_)

def appendChunk(original, chunk):
    return original + ' ' + chunk

def isRelationCandidate(token):
    deps = ["ROOT", "adj", "attr", "agent"]
    return any(subs in token.dep_ for subs in deps)

def isConstructionCandidate(token):
    deps = ["compound", "prep", "conj", "mod","amod"]
    for subs in deps:
        if(subs==token.dep_):
            return True
    return False

def processSubjectObjectPairs(tokens):
    t=0
    s=0
    c=0
    x=0
    subject = ''
    object = ''
    relation = ''
    subjectConstruction = ''
    objectConstruction = ''
    for token in tokens:
        if(x==0):
            #printToken(token)
            if "punct" in token.dep_:
                continue
            if isRelationCandidate(token):
                t=1
                # relation = appendChunk(relation, token.lemma_) #for lemmatization
                relation = appendChunk(relation, token.text)
            if isConstructionCandidate(token):
                if(t==0):
                    if(s==0):
                        if subjectConstruction:
                            subjectConstruction=appendChunk(subjectConstruction,token.text)
                            s=0
                        else:
                            subjectConstruction=appendChunk(subject,token.text)
                            s=0
                else:
                    if(c==0):
                        if objectConstruction:
                            objectConstruction = appendChunk(objectConstruction, token.text)
                            c=0
                        else:
                            objectConstruction=appendChunk(object, token.text)
                            c=0
                
            if "subj" in token.dep_:
                subject = appendChunk(subject, token.text)
                subject = appendChunk(subjectConstruction, subject)
                #print("sub",subject)
                subjectConstruction = ''
            if "obj" in token.dep_:
                object = appendChunk(object, token.text)
                object = appendChunk(objectConstruction, object)
                x=1
                #print("o",object)
                objectConstruction = ''

    #print (subject.strip(), ",", relation.strip(), ",", object.strip())
    return (subject.strip(), relation.strip(), object.strip())

def processSentence(sentence):
    tokens = nlp_model(sentence)
    #print('Tokens-->',tokens)
    return processSubjectObjectPairs(tokens)

def printGraph(triples):
    G = nx.Graph()
    for triple in triples:
        G.add_node(triple[0])
        #G.add_node(triple[1])
        G.add_node(triple[2])
        G.add_edge(triple[0], triple[2])
        #G.add_edge(triple[1], triple[2])
        

    pos = nx.spring_layout(G,k=50)
    plt.figure()
    nx.draw(G, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='seagreen', alpha=0.9,
            labels={node: node for node in G.nodes()})
    #for triple in triples:
        #edge_labels=dict([((triple[0],triple[2],),triple[1]) for u,v,d in G.edges(data=True)])
        #nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
    for triple in triples:
        nx.draw_networkx_edge_labels(G,pos,edge_labels={(triple[0],triple[2]):triple[1]},font_color='red')
    
    plt.axis('off')
    plt.show()

def tripsC(text):
    sentences = getSentences(text)
    

    triples = []
    for sentence in sentences:
        #print('Sent-->',sentence)
        triples.append(list(processSentence(sentence)))
    
    #printGraph(triples)
    #print(triples)
    return(triples)
#tripsC(text)
