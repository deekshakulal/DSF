import readFiles
import json

# files=["x.txt","s.txt"]
def getTriplets(files):
    tripletss=readFiles.process_files(files)
    #print((tripletss))
    try:
        f = open('Triplets.txt', 'w')
        json.dump(tripletss, f)
        #f=open("Triplets.txt",'w',encoding='utf-8')
        #f.write(tripletss)
    except:
        print("Couldn't open the file ",f)
    finally:
        f.close()
    return tripletss



#tripletss=[[['It', 'was', 'summer'], ['It', 'was', 'hot summer'], ['Nobody', 'go', ''], ['patient', 'got', 'covid 19'], ['She', 'was', 'quarantined']], [['patient', 'was suffering from', 'breathing problem'], ['patient', 'was suffering from', 'problem'], ['She', 'consulted', 'doctor'], ['she', 'was', 'quarantined'], ['she', 'was', 'then quarantined for 14 days'], ['she', 'was quarantined for', '14 days'], ['she', 'was', 'then quarantined']]]

def computescore(triplets):
    a=[]
    score={}
    #only for subject-object comparison
    # for tp in triplets.values():
    #     #print("-->",tp)
    #     x=(([(t[0]+" "+t[2]).lower() for t in tp]))
    #     a.append(x)

    #only for subject-verb-object comparison
    for tp in triplets.values():
        #print("-->",tp)
        x=(([(t[0]+" "+t[1]+" "+t[2]).lower() for t in tp]))
        a.append(x)

    for i in range(len(a)):
        for j in range(i+1,len(a)):
            #print(i,"-",a[i],"<->",j,'-',a[j])
            #similarity score
            s=(len(set(a[j]) & set(a[i])) / float(len(set(a[j]) | set(a[i]))) * 100) # (common strings/ all strings without repetition)*100
            #print("Similarity score of",list(triplets.keys())[i]," and",list(triplets.keys())[j],"==> ",s)
            score[list(triplets.keys())[i]+" & "+list(triplets.keys())[j]]=round(s,2)
    return score

def keywordsearch(keyword,triplets):
    search={}
    a=[]
    for tp in triplets.values():
        r=[]
        for t in tp:
            for i in t:
                r.append(i)
        a.append(r)
    for i in range(len(a)):
        p=(a[i].count(keyword)/len(a[i]))*100
        search[keyword+ " in "+list(triplets.keys())[i]]=round(p,2)
        #print("occurance of ",k, "in ",list(tripletss.keys())[i],"==> ",round(p,2),"%") # (common strings/ all strings without repetition)*100
    return search

    
