import math
import re
from collections import Counter

WORD = re.compile(r"\w+")


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


text1 = "CASE REPORT: A 67 y/o (year old) female from Western Africa initially presented to the Emergency Department (ED) complaining of fatigue and subjective fevers for the past 2 days. Patient complained that her fevers were associated with headaches, but not chills, rigors, or chest pain. Index of suspicion for malaria was high as patient had recently traveled from an endemic region. Patients travel history to Western Africa and the presenting symptoms also made us consider a possibility of Ebola virus disease. Past medical history included diabetes, hypertension, and a history of recent travel to her home country of Togo for 5 months. Patient had returned 5 days ago from her travel and started to develop symptoms of fevers and fatigue. Patient denied any immunizations received before traveling. Past surgical history included a left breast mastectomy done back in France 1987. Medication history included Amlodipine, Aspirin, Calcium Carbonate, Synthroid, Pioglitazone, Humalog, Glucovance, Crestor, Januvia, and Lisinopril. After initial presentation to the ED for 2 days of fevers and fatigue, she was accepted by Medicine and transferred to the general medical floors. The patient had a blood pressure of 123/55, pulse of 86 beats per minute (bpm), Temperature of 98.5 °F, and respiratory rate of 16 at the time of admission. Physical examination did not disclose any specific abnormalities. Labs including complete blood count, chemistry, liver function tests, malaria peripheral smears, and reitculocyte level were withdrawn from the patient. Patient had white blood cell (WBC) count of 12.6, Hb (hemoglobin) 10.7, Hct (hematocrit) 30.6, Plt (platelet) 80, BUN (blood urea nitrogen) 12, Creat (creatinine) 0.3, and blood glucose of 291 consistent with diabetes. Blood smears were positive for P. falciparum malaria at 9.6% and reticulocyte count was reported at 3.2%. New York City's Department of Health and Mental Hygiene (DOHMH), was contacted and Ebola was not considered to be in Togo, most likely diagnosis was malaria from chloroquine resistant region. Patient was started on quinine 648 mg and doxycycline 100 mg, intravenous (IV) fluids, Lantus 21 U, Lispro 7 U, and was monitored in telemetry unit of medicine (Figures 1–3)."
text2 = "CASE REPORT: A 67 y/o (year old) female from Western Africa initially presented to the Emergency Department (ED) complaining of fatigue and subjective fevers for the past 2 days. Patient complained that her fevers were associated with headaches, but not chills, rigors, or chest pain. Index of suspicion for malaria was high as patient had recently traveled from an endemic region. Patients travel history to Western Africa and the presenting symptoms also made us consider a possibility of Ebola virus disease. Past medical history included diabetes, hypertension, and a history of recent travel to her home country of Togo for 5 months. Patient had returned 5 days ago from her travel and started to develop symptoms of fevers and fatigue. Patient denied any immunizations received before traveling. Past surgical history included a left breast mastectomy done back in France 1987. Medication history included Amlodipine, Aspirin, Calcium Carbonate, Synthroid, Pioglitazone, Humalog, Glucovance, Crestor, Januvia, and Lisinopril. After initial presentation to the ED for 2 days of fevers and fatigue, she was accepted by Medicine and transferred to the general medical floors. The patient had a blood pressure of 123/55, pulse of 86 beats per minute (bpm), Temperature of 98.5 °F, and respiratory rate of 16 at the time of admission. Physical examination did not disclose any specific abnormalities."

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)

cosine = get_cosine(vector1, vector2)

print("Cosine:", cosine)