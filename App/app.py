from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLD = '/Users/dell/Documents/Final year proj/dsf/App/Files'
UPLOAD_FOLDER = os.path.join(APP_ROOT, UPLOAD_FOLD)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    import libs
    return render_template('home.html')


@app.route("/about")
def about():
    return render_template("about.html")


@app.route('/addRegion', methods=['POST'])
def addRegion():
    #x=request.form['files']
    fs=[]
    r={}
    x=request.files.getlist('files')
    import functions
    for f in x:
        fs.append(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    print(fs)
    imfs=[]
    for i in fs:
        imfs.append(i.split(".")[0]+".png")
    r=functions.getTriplets(fs)
    #r={"a.txt":[["DISCHARGE SUMMARY PATIENT INFORMATION NAME Mary Smith MRN12345","by","Dr. John Lee ADMISSION DATE 112914 DISCHARGE DATE 12114 DISCHARGE DIAGNOSIS Acute COPD exacerbation DISPOSITION Home"],["DISCHARGE SUMMARY PATIENT INFORMATION NAME Mary Smith MRN12345","DICTATED","Dr. John Lee ADMISSION DATE 112914 DISCHARGE DATE 12114 DISCHARGE DIAGNOSIS Acute COPD exacerbation DISPOSITION Home"],["Dr. John Lee ADMISSION DATE 112914 DISCHARGE DATE 12114 DISCHARGE DIAGNOSIS Acute COPD exacerbation DISPOSITION Home","improve","condition"],["Dr. John Lee ADMISSION DATE DISCHARGE DATE 12114 DISCHARGE DIAGNOSIS Acute COPD exacerbation DISPOSITION Home","improve","condition"],["I","ask","patient"],["patient","within","next week"],["HOSPITAL  COURSE","refer","to  HP"],["","a.",""],["patient","be","very pleasant woman"],["pleasant old woman","with","severe COPD"],["patient","old","COPD"],["patient","be","very pleasant 67 year old woman with severe COPD"],["patient","pleasant","COPD"],["patient","be","very pleasant 67 year old woman"],["She","in","quite short of breath"],["She","in","quite short"],["She","in","short"],["She","in","tachypnic"],["She","with","steroids"],["She","be","treated"],["She","be","treated"],["She","with","nebulizer treatments"],["She","over","her 2 day stay"],["She","avoid","intubation"],["She","avoid","intubation"],["","Today",""],["she","on","my exam"],["I","think baseline",""],["Her lungs","at_time","today"],["She","get","somewhat hypoxic with exertion"],["She","get","hypoxic"],["She","get","somewhat hypoxic"],["She","qualify","for  oxygen"],["patient","be","stable"],["patient","be","otherwise stable"],["I","ask","her"],["her","with","her PCP"],["She","given","short  course"],["She","given","antibiotics"],["She","have","PFTs"],["","a.",""],["","high",""],["","Stabilized by","time"],["","BP",""],["","a.",""],["","Stable",""],["","Follow","with  PCP"],["","a.",""],["","Stable",""],["","a.",""],["Stable DISCHARGE MEDICATIONS","Discharge","Medications Albuterol Fluticasonesalmeterol Aspirin 81 mg 1 tab PO daily Multivitamin 1 tab daily HCTZ 25 mg 1 tab PO"],["Stable DISCHARGE MEDICATIONS","Discharge","Medications Albuterol Fluticasonesalmeterol Aspirin 81 mg 1 tab PO Multivitamin 1 tab daily HCTZ 25 mg 1 tab PO"],["Stable DISCHARGE MEDICATIONS","Discharge","Medications Albuterol Fluticasonesalmeterol Aspirin 81 mg 1 tab PO Multivitamin 1 tab HCTZ 25 mg 1 tab PO"],["Stable DISCHARGE MEDICATIONS","daily","Medications Albuterol Fluticasonesalmeterol Aspirin 81 mg 1 tab PO daily Multivitamin 1 tab daily HCTZ 25 mg 1 tab PO"]],"b.txt":[["RECENT HOSPITALIZATION","from","CARE"],["PERSON","with","ADVANCED COPD"],["","DICTATION","BY Dr. John  Lee"],["","DICTATION","BY Dr. John  Lee"],["","DICTATION","BY Dr. John  Lee"],["She","visited",""],["","She",""],["She","be","sent"],["She","be","recently sent home"],["She","be","recently sent"],["She","on","azithromycin"],["She","be","prednisone taper"],["She","be","recently prednisone taper"],["She she","says",""],["She she","says","inhalers"],["she","have","cough"],["she","have","chronic cough"],["she","have","cough"],["she","have","chronic cough"],["she","have","cough"],["she","have","chronic cough"],["Her sputum","be","white"],["She","deny","chest pain"],["She","deny","fever"],["She","deny","chills"],["She","deny","night sweats"],["She","has","lower extremity  edema"],["REVIEW","","SYSTEMS"],["","REVIEW","OF  SYSTEMS"],["REVIEW","","SYSTEMS"],["","hypothyroidism",""],["","replacement Allergies",""],["","allergies",""],["CURRENT MEDICATIONS Albuterol  inhaler","fluticasonesalmeterol","inhaler"],["","Is teacher",""],["She","lives",""],["Her family","often","her"],["Her family","visit","her"],["FAMILY HISTORY Father","from","MI"],["PHYSICAL EXAMINATION  Temperature rate","C is breaths","heart respiratory per  minute"]]}
    return render_template("options.html",results=r,f=imfs)
    #return(functions.getTriplets(fs))

@app.route('/page', methods=['POST'])
def page():
    import ast
    x=request.form["results"]
    t=ast.literal_eval(x)
    import functions
    score=functions.computescore(t)
    print("score---",score)
    s=""
    for i,j in score.items():
        s=s+"\n"+str(i)+" is "+str(j)+"%.     9\n"
    print(s)
    return render_template("result.html",results=t,st=s)
    #return(functions.getTriplets(fs))


@app.route('/search', methods=['POST'])
def search():
    import ast
    x=request.form["results"]
    t=ast.literal_eval(x)
    import functions
    key=request.form["key"]
    print("key---",key)
    s=""
    searchscore=functions.keywordsearch(key,t)
    for i,j in searchscore.items():
        s=s+"\n"+str(i)+" is "+str(j)+"%.       \n"
    print(s)
    return render_template("search.html",results=t,st=s)

@app.route('/visualize',methods=['POST'])
def visualize():
    n=request.form["imgfile"]
    import ast
    n=ast.literal_eval(n)
    print("names---",n,type(n))
    return render_template("show.html",im=n)


if __name__ == '__main__':
    app.run(debug=True)