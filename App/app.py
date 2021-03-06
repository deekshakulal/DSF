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
    print(x)
    import functions
    for f in x:
        fs.append(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    print(fs)
    imfs=[]
    for i in fs:
        imfs.append(i.split(".")[0]+".png")
    r=functions.getTriplets(fs)
    #r={"c1.txt": [["female", "", "Africa"], ["female", "", "Africa"], ["Patient", "complain", ""], ["her fevers", "be", "associated"], ["her fevers", "associate", "headaches"], ["Patient", "complain", ""], ["her fevers", "be", "associated"], ["her fevers", "associate", "headaches"], ["", "pain", ""], ["Index", "be", "high"], ["patient", "travel", "endemic region"], ["Patients", "history", "Western Africa"], ["Patients", "travel", "history"], ["us", "consider", "possibility of Ebola virus disease"], ["us", "consider", "possibility"], ["us", "possibility", "Ebola virus disease"], ["Past history", "include", "diabetes"], ["Past medical history", "include", "diabetes"], ["Past medical history", "include", "her home country of Togo"], ["Past history", "include", "hypertension"], ["Past medical history", "include", "hypertension"], ["Past medical history", "include", "hypertension to her home country of Togo"], ["Past medical history", "include", "history"], ["Past medical history", "include", "history of recent travel to her home country of Togo for 5 months"], ["Past medical history", "include", "history for 5 months"], ["Patient", "return", "her travel"], ["Patient", "develop", "symptoms"], ["Patient", "develop", "symptoms of fevers fatigue"], ["Patient", "deny", "immunizations received before traveling"], ["Past surgical  history", "include", "left breast  mastectomy"], ["Medication history", "include", "Amlodipine Aspirin Calcium Carbonate"], ["Medication history", "include", "Amlodipine Aspirin Calcium Synthroid"], ["Medication history", "include", "Amlodipine Aspirin Calcium Pioglitazone"], ["Medication history", "include", "Amlodipine Aspirin Calcium Humalog"], ["Medication history", "include", "Amlodipine Aspirin Calcium Glucovance"], ["Medication history", "include", "Amlodipine Aspirin Calcium Crestor"], ["Medication history", "include", "Amlodipine Aspirin Calcium Januvia"], ["Medication history", "include", "Amlodipine Aspirin Calcium"], ["Medication history", "include", "Amlodipine Aspirin Calcium Lisinopril"], ["she", "be", "After initial presentation to ED accepted by Medicine"], ["she", "be", "After initial presentation to ED for 2 days of fevers fatigue accepted by Medicine"], ["she", "by", "Medicine"], ["she", "transfer", "initial presentation to ED for 2 days of fevers fatigue"], ["patient", "have", "blood pressure of 12355"], ["patient", "have", "blood pressure"], ["patient", "have", "pulse of 86 beats"], ["patient", "have", "Temperature"], ["patient", "have", "Temperature of 98.5 F"], ["patient", "have", "respiratory rate"], ["patient", "have", "respiratory rate of 16"], ["Physical  examination", "disclose", "specific  abnormalities"], ["Labs", "be", "withdrawn"], ["Labs", "be", "withdrawn"], ["Labs", "be", "withdrawn"], ["Labs", "be", "withdrawn"], ["Labs", "be", "withdrawn"], ["Patient", "have", "white blood cell count of 12.6 consistent"], ["Patient", "have", "white blood cell count of 12.6 consistent with diabetes"], ["Patient", "have", "white blood cell count"], ["Patient", "have", "blood cell count"], ["Patient", "have", "white blood cell count"], ["Patient", "have", "blood cell count"], ["Patient", "have", "white blood cell count of Hb"], ["Patient", "have", "white blood cell count"], ["Patient", "have", "white blood cell count of Hct"], ["Patient", "have", "blood cell count"], ["Patient", "have", "white blood cell count of Plt 80"], ["Patient", "have", "white blood cell count"], ["Patient", "have", "blood cell count"], ["Patient", "have", "white blood cell count of Plt 80 consistent with diabetes"], ["Patient", "have", "white blood cell count of BUN 12"], ["Patient", "have", "white blood cell count of BUN 12 consistent with diabetes"], ["Patient", "have", "white blood cell count"], ["Patient", "have", "blood cell count"], ["Patient", "have", "white blood cell count of Creat 0.3"], ["Patient", "have", "white blood cell count"], ["Patient", "have", "blood cell count"], ["Patient", "have", "white blood cell count of Creat 0.3 consistent with diabetes"], ["Patient", "have", "white blood cell count of blood glucose of 291 consistent with diabetes"], ["Patient", "have", "white blood cell count of blood glucose"], ["Patient", "have", "white blood cell count"], ["Patient", "have", "blood cell count"], ["Blood smears", "be", "positive"], ["Blood smears", "be", "P. falciparum malaria"], ["Blood smears", "be", "positive for P. falciparum malaria at 9.6 reticulocyte count reported at 3.2"], ["Blood smears", "be", "positive for P. falciparum malaria at 9.6 reticulocyte count"], ["Blood smears", "be", "positive"], ["Blood smears", "be", "positive for P. falciparum malaria at 9.6"], ["Blood smears", "be", "P. falciparum malaria"], ["New York City Department", "contact", "most likely diagnosis"], ["New York City Department", "contact", "likely diagnosis"], ["New York City Department", "contact", "most likely diagnosis"], ["New York City Department", "contact", "likely diagnosis"], ["Ebola", "consider", "in  Togo"], ["Patient", "start", "quinine 648 mg"], ["Patient", "be", "started"], ["", "doxycycline", "intravenous  fluids"], ["Patient", "monitor", "telemetry unit"], ["Patient", "be", "monitored"], ["Patient", "monitor", "telemetry unit of medicine"]], "c2.txt": [["female", "", "Africa"], ["female", "", "Africa"], ["Patient", "complain", ""], ["her fevers", "be", "associated"], ["her fevers", "associate", "headaches"], ["Patient", "complain", ""], ["her fevers", "be", "associated"], ["her fevers", "associate", "headaches"], ["", "pain", ""], ["Index", "be", "high"], ["patient", "travel", "endemic region"], ["Patients", "history", "Western Africa"], ["Patients", "travel", "history"], ["us", "consider", "possibility of Ebola virus disease"], ["us", "consider", "possibility"], ["us", "possibility", "Ebola virus disease"], ["Past history", "include", "diabetes"], ["Past medical history", "include", "diabetes"], ["Past medical history", "include", "her home country of Togo"], ["Past history", "include", "hypertension"], ["Past medical history", "include", "hypertension"], ["Past medical history", "include", "hypertension to her home country of Togo"], ["Past medical history", "include", "history"], ["Past medical history", "include", "history of recent travel to her home country of Togo for 5 months"], ["Past medical history", "include", "history for 5 months"], ["Patient", "return", "her travel"], ["Patient", "develop", "symptoms"], ["Patient", "develop", "symptoms of fevers fatigue"], ["Patient", "deny", "immunizations received before traveling"], ["Past surgical  history", "include", "left breast  mastectomy"], ["Medication history", "include", "Amlodipine Aspirin Calcium Carbonate"], ["Medication history", "include", "Amlodipine Aspirin Calcium Synthroid"], ["Medication history", "include", "Amlodipine Aspirin Calcium Pioglitazone"], ["Medication history", "include", "Amlodipine Aspirin Calcium Humalog"], ["Medication history", "include", "Amlodipine Aspirin Calcium Glucovance"], ["Medication history", "include", "Amlodipine Aspirin Calcium Crestor"], ["Medication history", "include", "Amlodipine Aspirin Calcium Januvia"], ["Medication history", "include", "Amlodipine Aspirin Calcium"], ["Medication history", "include", "Amlodipine Aspirin Calcium Lisinopril"], ["she", "be", "After initial presentation to ED accepted by Medicine"], ["she", "be", "After initial presentation to ED for 2 days of fevers fatigue accepted by Medicine"], ["she", "by", "Medicine"], ["she", "transfer", "initial presentation to ED for 2 days of fevers fatigue"], ["patient", "have", "blood pressure of 12355"], ["patient", "have", "blood pressure"], ["patient", "have", "pulse of 86 beats"], ["patient", "have", "Temperature"], ["patient", "have", "Temperature of 98.5 F"], ["patient", "have", "respiratory rate"], ["patient", "have", "respiratory rate of 16"], ["Physical  examination", "disclose", "specific  abnormalities"]], "c3.txt": [["Blood smears", "be", "positive for P. falciparum malaria at 9.6 reticulocyte count"], ["Blood smears", "be", "positive"], ["Blood smears", "be", "positive for P. falciparum malaria at 9.6"], ["Blood smears", "be", "P. falciparum malaria"], ["New York City Department", "contact", "most likely diagnosis"], ["New York City Department", "contact", "likely diagnosis"], ["New York City Department", "contact", "most likely diagnosis"], ["New York City Department", "contact", "likely diagnosis"], ["Ebola", "consider", "in  Togo"], ["Patient", "start", "quinine 648 mg"], ["Patient", "be", "started"], ["", "doxycycline", "intravenous  fluids"], ["Patient", "monitor", "telemetry unit"], ["Patient", "be", "monitored"], ["Patient", "monitor", "telemetry unit of medicine"], ["emergency department", "be", "Netherlands"], ["old  man", "", "Liberia"], ["old  man", "", "Liberia"], ["episode", "be", "past"], ["His travel history", "indicate", "2008"], ["he", "by", "car"], ["four week holiday", "be", "Barcelona Italy"], ["he", "by", "car"], ["four week holiday", "be", "Spain Italy"], ["four week holiday", "be", "Treviso Italy"], ["he", "by", "car"], ["he", "be", "his travel"], ["he", "during", "his travel"], ["he", "have", "fevers"], ["he", "have", "his travel"], ["some", "be", "his travel"], ["", "", "travel"], ["some", "have", "his travel"], ["some", "have", "fevers"], ["", "stay", "with  immigrants"], ["", "during", "travel"], ["", "return", "from  Africa"], ["Some", "", "whom"], ["Some", "", "whom"], ["Some", "have", "fevers"], ["patient", "report", "in  places"], ["Many indoor  insects", "", "mosquitoes"], ["other risk  factors", "", "transmission"]]}
    
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
    return render_template("result.html",results=t,st=score)
    #return(functions.getTriplets(fs))


@app.route('/search', methods=['POST'])
def search():
    import ast
    x=request.form["results"]
    t=ast.literal_eval(x)
    import functions
    key=request.form["key"]
    print("key---",key)
    searchscore=functions.keywordsearch(key,t)
    return render_template("search.html",results=t,st=searchscore,k=key)

@app.route('/visualize',methods=['POST'])
def visualize():
    n=request.form["imgfile"]
    import ast
    n=ast.literal_eval(n)
    print("names---",n,type(n))
    return render_template("show.html",im=n)


if __name__ == '__main__':
    app.run(debug=True)