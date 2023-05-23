import streamlit as st
import streamlit_lottie as lottie
import requests
from PIL import Image
import pickle
import sklearn

xIcon = Image.open("images/Xicon.ico")

st.set_page_config(page_title="iCare", page_icon = xIcon, layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html = True)

local_css("style/style.css")

lottie_doc = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_bYskKBq3WY.json")
logo = Image.open("images/Logo.png")

st.markdown(
    """
    <style>
    .centered-image {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load Models to the code
with open('models/covid_model.pickle', 'rb') as f:
    covid_model = pickle.load(f)

with open('models/monkey_pox_model.pickle', 'rb') as f:
    monkey_pox_model = pickle.load(f)

with open('models/lung_cancer_model.pkl', 'rb') as f:
    lung_cancer_model = pickle.load(f)

with st.container():
    left, center, right = st.columns(3)
    with left:
        lottie.st_lottie(lottie_doc, height=350, width=350)
    with center:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.empty()
        with col2:
            st.image(logo, caption=None, width=200, use_column_width=True, clamp=False)
        with col3:
            st.empty()

        st.write("---")
        type = st.selectbox('Select the disease type', ('Select', 'Covid', 'Heart disease', 'Lung Cancer', 'Monkey Pox'))

        if(type == 'Select'):
            st.empty()

        if(type == 'Covid'):
            st.write(':robot_face: : Select the relevant disease type.')
            st.write(':male-office-worker: : Covid')
            st.write(':robot_face: : Did the patient treated in a medical unit?')
            usmr = st.selectbox('Select the answer', ('Select', 'Yes', 'No'))
            usmr_val = 0
            usmr_ans_stat = False
            if(usmr == 'Select'):
                st.empty()
            if (usmr == 'Yes'):
                usmr_val = 1
                usmr_ans_stat = True
                st.write(':male-office-worker: : Yes')
            if (usmr == 'No'):
                usmr_val = 2
                usmr_ans_stat = True
                st.write(':male-office-worker: : No')

            if(usmr_ans_stat):
                st.write(':robot_face: : Select gender of the patient.')
                sex = st.selectbox('Gender', ('Select', 'Male', 'Female'))
                sex_val = 0
                gender_ans_stat = False
                if (sex == 'Select'):
                    st.empty()
                if (sex == 'Male'):
                    sex_val = 2
                    gender_ans_stat = True
                    st.write(':male-office-worker: : Male')
                if (sex == 'Female'):
                    sex_val = 1
                    gender_ans_stat = True
                    st.write(':male-office-worker: : Female')
                if(gender_ans_stat):
                    st.write(':robot_face: : Did the patient returned home or hospitalized after the checkup?')
                    patient_type = st.selectbox('Select the patient type', ('Select', 'Returned Home', 'Hospitalized'))
                    patient_type_val = 0
                    patient_type_ans_stat = False
                    if (patient_type == 'Select'):
                        st.empty()
                    if (patient_type == 'Returned Home'):
                        patient_type_val = 1
                        patient_type_ans_stat = True
                        st.write(':male-office-worker: : Returned Home')
                    if (patient_type == 'Hospitalized'):
                        patient_type_val = 2
                        patient_type_ans_stat = True
                        st.write(':male-office-worker: : Hospitalized')

                    if(patient_type_ans_stat):
                        st.write(':robot_face: : Did the patient was connected to the ventilator?')
                        intubed = st.selectbox('Select relevant answer', ('Select', 'Yes', 'No', 'No Idea'))
                        intubed_val = 0
                        intubed_ans_stat = False
                        if (intubed == 'Select'):
                            st.empty()
                        if (intubed == 'Yes'):
                            intubed_val = 1
                            intubed_ans_stat = True
                            st.write(':male-office-worker: : Yes')
                        if (intubed == 'No'):
                            intubed_val = 2
                            intubed_ans_stat = True
                            st.write(':male-office-worker: : No')
                        if(intubed == 'No Idea'):
                            intubed_val = 97
                            intubed_ans_stat = True
                            st.write(':male-office-worker: : No Idea')

                        if(intubed_ans_stat):
                            st.write(':robot_face: : Did the patient already have air sacs inflammation?')
                            pneumonia = st.selectbox('Select the answer about pneumonia', ('Select', 'Yes', 'No', 'No Idea'))
                            pneumonia_val = 0
                            pneumonia_ans_stat = False
                            if (pneumonia == 'Select'):
                                st.empty()
                            if (pneumonia == 'Yes'):
                                pneumonia_val = 1
                                pneumonia_ans_stat = True
                                st.write(':male-office-worker: : Yes')
                            if (pneumonia == 'No'):
                                pneumonia_val = 2
                                pneumonia_ans_stat = True
                                st.write(':male-office-worker: : No')
                            if (pneumonia == 'No Idea'):
                                pneumonia_val = 97
                                pneumonia_ans_stat = True
                                st.write(':male-office-worker: : No Idea')

                            if(pneumonia_ans_stat):
                                st.write(':robot_face: : Enter the age of the patient.')
                                age = st.number_input("Enter your age", min_value=0, max_value=120, value=0)
                                st.write(f':male-office-worker: : {age}')

                                if(age != 0):
                                    st.write(':robot_face: : Did the patient was pregnant?')
                                    pregnant = st.selectbox('Select the answer about pregnancy', ('Select', 'Yes', 'No', 'No Idea'))
                                    pregnant_val = 0
                                    pregnant_ans_stat = False
                                    if (pregnant == 'Select'):
                                        st.empty()
                                    if (pregnant == 'Yes'):
                                        pregnant_val = 1
                                        pregnant_ans_stat = True
                                        st.write(':male-office-worker: : Yes')
                                    if (pregnant == 'No'):
                                        pregnant_val = 2
                                        pregnant_ans_stat = True
                                        st.write(':male-office-worker: : No')
                                    if (pregnant == 'No Idea'):
                                        pregnant_val = 97
                                        pregnant_ans_stat = True
                                        st.write(':male-office-worker: : No Idea')

                                    if(pregnant_ans_stat):
                                        st.write(':robot_face: : Did the patient have diabetes?')
                                        diabetes = st.selectbox('Select the answer about diabetes', ('Select', 'Yes', 'No', 'No Idea'))
                                        diabetes_val = 0
                                        diabetes_ans_stat = False
                                        if (diabetes == 'Select'):
                                            st.empty()
                                        if (diabetes == 'Yes'):
                                            diabetes_val = 1
                                            diabetes_ans_stat = True
                                            st.write(':male-office-worker: : Yes')
                                        if (diabetes == 'No'):
                                            diabetes_val = 2
                                            diabetes_ans_stat = True
                                            st.write(':male-office-worker: : No')
                                        if (diabetes == 'No Idea'):
                                            diabetes_val = 97
                                            diabetes_ans_stat = True
                                            st.write(':male-office-worker: : No Idea')

                                        if(diabetes_ans_stat):
                                            st.write(':robot_face: : Did the patient has Chronic Obstructive Pulmonary Disease?')
                                            copd = st.selectbox('Select the answer about COPD', ('Select', 'Yes', 'No', 'No Idea'))
                                            copd_val = 0
                                            copd_ans_stat = False
                                            if (copd == 'Select'):
                                                st.empty()
                                            if (copd == 'Yes'):
                                                copd_val = 1
                                                copd_ans_stat = True
                                                st.write(':male-office-worker: : Yes')
                                            if (copd == 'No'):
                                                copd_val = 2
                                                copd_ans_stat = True
                                                st.write(':male-office-worker: : No')
                                            if (copd == 'No Idea'):
                                                copd_val = 97
                                                copd_ans_stat = True
                                                st.write(':male-office-worker: : No Idea')

                                            if(copd_ans_stat):
                                                st.write(':robot_face: : Did the patient has Asthma?')
                                                asthma = st.selectbox('Select the answer about asthma', ('Select', 'Yes', 'No', 'No Idea'))
                                                asthma_val = 0
                                                asthma_ans_stat = False
                                                if (asthma == 'Select'):
                                                    st.empty()
                                                if (asthma == 'Yes'):
                                                    asthma_val = 1
                                                    asthma_ans_stat = True
                                                    st.write(':male-office-worker: : Yes')
                                                if (asthma == 'No'):
                                                    asthma_val = 2
                                                    asthma_ans_stat = True
                                                    st.write(':male-office-worker: : No')
                                                if (asthma == 'No Idea'):
                                                    asthma_val = 97
                                                    asthma_ans_stat = True
                                                    st.write(':male-office-worker: : No Idea')

                                                if(asthma_ans_stat):
                                                    st.write(':robot_face: : Did the patient have immunosuppression?')
                                                    inmsupr = st.selectbox('Select the answer about immunosuppression', ('Select', 'Yes', 'No', 'No Idea'))
                                                    inmsupr_val = 0
                                                    inmsupr_ans_stat = False
                                                    if inmsupr == 'Select':
                                                        st.empty()
                                                    elif inmsupr == 'Yes':
                                                        inmsupr_val = 1
                                                        inmsupr_ans_stat = True
                                                        st.write(':male-office-worker: : Yes')
                                                    elif inmsupr == 'No':
                                                        inmsupr_val = 2
                                                        inmsupr_ans_stat = True
                                                        st.write(':male-office-worker: : No')
                                                    else:
                                                        inmsupr_val = 97
                                                        inmsupr_ans_stat = True
                                                        st.write(':male-office-worker: : No Idea')

                                                    if(inmsupr_ans_stat):
                                                        st.write(':robot_face: : Did the patient have hypertension?')
                                                        hypertension = st.selectbox('Select the answer about hypertension', ('Select', 'Yes', 'No', 'No Idea'))
                                                        hypertension_val = 0
                                                        hypertension_ans_stat = False
                                                        if hypertension == 'Select':
                                                            st.empty()
                                                        elif hypertension == 'Yes':
                                                            hypertension_val = 1
                                                            hypertension_ans_stat = True
                                                            st.write(':male-office-worker: : Yes')
                                                        elif hypertension == 'No':
                                                            hypertension_val = 2
                                                            hypertension_ans_stat = True
                                                            st.write(':male-office-worker: : No')
                                                        else:
                                                            hypertension_val = 97
                                                            hypertension_ans_stat = True
                                                            st.write(':male-office-worker: : No Idea')

                                                        if hypertension_ans_stat:
                                                            st.write(':robot_face: : Did the patient has other disease?')
                                                            other_disease = st.selectbox('Select the answer about other disease', ('Select', 'Yes', 'No', 'No Idea'))
                                                            other_disease_val = 0
                                                            other_disease_ans_stat = False
                                                            if other_disease == 'Select':
                                                                st.empty()
                                                            elif other_disease == 'Yes':
                                                                other_disease_val = 1
                                                                other_disease_ans_stat = True
                                                                st.write(':male-office-worker: : Yes')
                                                            elif other_disease == 'No':
                                                                other_disease_val = 2
                                                                other_disease_ans_stat = True
                                                                st.write(':male-office-worker: : No')
                                                            else:
                                                                other_disease_val = 97
                                                                other_disease_ans_stat = True
                                                                st.write(':male-office-worker: : No Idea')

                                                            if other_disease_ans_stat:
                                                                st.write(':robot_face: : Did the patient has heart or blood vessels related disease?')
                                                                cardiovascular = st.selectbox('Select the answer about cardiovascular', ('Select', 'Yes', 'No', 'No Idea'))
                                                                cardiovascular_val = 0
                                                                cardiovascular_ans_stat = False
                                                                if cardiovascular == 'Select':
                                                                    st.empty()
                                                                elif cardiovascular == 'Yes':
                                                                    cardiovascular_val = 1
                                                                    cardiovascular_ans_stat = True
                                                                    st.write(':male-office-worker: : Yes')
                                                                elif cardiovascular == 'No':
                                                                    cardiovascular_val = 2
                                                                    cardiovascular_ans_stat = True
                                                                    st.write(':male-office-worker: : No')
                                                                else:
                                                                    cardiovascular_val = 97
                                                                    cardiovascular_ans_stat = True
                                                                    st.write(':male-office-worker: : No Idea')

                                                                if cardiovascular_ans_stat:
                                                                    st.write(':robot_face: : Did the patient obese?')
                                                                    obesity = st.selectbox('Select the answer about obesity', ('Select', 'Yes', 'No', 'No Idea'))
                                                                    obesity_val = 0
                                                                    obesity_ans_stat = False
                                                                    if obesity == 'Select':
                                                                        st.empty()
                                                                    elif obesity == 'Yes':
                                                                        obesity_val = 1
                                                                        obesity_ans_stat = True
                                                                        st.write(':male-office-worker: : Yes')
                                                                    elif obesity == 'No':
                                                                        obesity_val = 2
                                                                        obesity_ans_stat = True
                                                                        st.write(':male-office-worker: : No')
                                                                    else:
                                                                        obesity_val = 97
                                                                        obesity_ans_stat = True
                                                                        st.write(':male-office-worker: : No Idea')

                                                                    if obesity_ans_stat:
                                                                        st.write(':robot_face: : Did the patient has chronic renal disease?')
                                                                        renal_chronic = st.selectbox('Select the answer about chronic renal disease', ('Select', 'Yes', 'No', 'No Idea'))
                                                                        renal_chronic_val = 0
                                                                        renal_chronic_ans_stat = False
                                                                        if renal_chronic == 'Select':
                                                                            st.empty()
                                                                        elif renal_chronic == 'Yes':
                                                                            renal_chronic_val = 1
                                                                            renal_chronic_ans_stat = True
                                                                            st.write(':male-office-worker: : Yes')
                                                                        elif renal_chronic == 'No':
                                                                            renal_chronic_val = 2
                                                                            renal_chronic_ans_stat = True
                                                                            st.write(':male-office-worker: : No')
                                                                        else:
                                                                            renal_chronic_val = 97
                                                                            renal_chronic_ans_stat = True
                                                                            st.write(':male-office-worker: : No Idea')

                                                                        if renal_chronic_ans_stat:
                                                                            st.write(':robot_face: : Did the patient is a tobacco user?')
                                                                            tobacco = st.selectbox('Select the answer about use of tobacco', ('Select', 'Yes', 'No', 'No Idea'))
                                                                            tobacco_val = 0
                                                                            tobacco_ans_stat = False
                                                                            if tobacco == 'Select':
                                                                                st.empty()
                                                                            elif tobacco == 'Yes':
                                                                                tobacco_val = 1
                                                                                tobacco_ans_stat = True
                                                                                st.write(':male-office-worker: : Yes')
                                                                            elif tobacco == 'No':
                                                                                tobacco_val = 2
                                                                                tobacco_ans_stat = True
                                                                                st.write(':male-office-worker: : No')
                                                                            else:
                                                                                tobacco_val = 97
                                                                                tobacco_ans_stat = True
                                                                                st.write(':male-office-worker: : No Idea')

                                                                            if tobacco_ans_stat:
                                                                                st.write(':robot_face: : Did the patient had been admitted to an Intensive Care Unit?')
                                                                                icu = st.selectbox('Select the answer about ICU', ('Select', 'Yes', 'No', 'No Idea'))
                                                                                icu_val = 0
                                                                                icu_ans_stat = False
                                                                                if icu == 'Select':
                                                                                    st.empty()
                                                                                elif icu == 'Yes':
                                                                                    icu_val = 1
                                                                                    icu_ans_stat = True
                                                                                    st.write(':male-office-worker: : Yes')
                                                                                elif icu == 'No':
                                                                                    icu_val = 2
                                                                                    icu_ans_stat = True
                                                                                    st.write(':male-office-worker: : No')
                                                                                else:
                                                                                    icu_val = 0
                                                                                    icu_ans_stat = True
                                                                                    st.write(':male-office-worker: : No')

                                                                                if icu_ans_stat:
                                                                                    covid_pred = covid_model.predict([[
                                                                                        usmr_val, sex_val,
                                                                                        patient_type_val,
                                                                                        intubed_val, pneumonia_val, age,
                                                                                        pregnant_val,
                                                                                        diabetes_val, copd_val,
                                                                                        asthma_val, inmsupr_val,
                                                                                        hypertension_val,
                                                                                        other_disease_val,
                                                                                        cardiovascular_val,
                                                                                        obesity_val, renal_chronic_val,
                                                                                        tobacco_val, icu_val
                                                                                    ]])

                                                                                    # covid test findings.
                                                                                    # Values 1-3 mean that the patient was diagnosed with covid in different degrees.
                                                                                    # 4 or higher means that the patient is not a carrier of covid or that the test is inconclusive.

                                                                                    if (covid_pred == 1):
                                                                                        st.error(
                                                                                              ':robot_face: : Based on the given data, The patient was diagnosed with covid in extremely dangerous situation.')
                                                                                    elif (covid_pred == 2):
                                                                                        st.error(
                                                                                              ':robot_face: : Based on the given data, The patient was diagnosed with covid in critical situation.')
                                                                                    elif (covid_pred == 3):
                                                                                        st.error(
                                                                                              ':robot_face: : Based on the given data, The patient was diagnosed with covid')

                                                                                    elif (covid_pred >= 4):
                                                                                        st.success(
                                                                                              ':robot_face: : Based on the given data, The patient is not a carrier of covid or that the test is inconclusive.')
                                                                                    else:
                                                                                        st.error(':robot_face: : Unsupported Data !')
        if (type == 'Heart disease'):
            st.balloons()

        if (type == 'Lung Cancer'):
            if (type == 'Lung Cancer'):
                st.write(':robot_face: : Select the relevant disease type.')
                st.write(':male-office-worker: : Lung Cancer')
                st.write(':robot_face: : Select your gender?')
                gender = st.selectbox('Select the answer', ('Select', 'Male', 'Female'))
                gender_val = 0
                gender_val_stat = False
                if (gender == 'Select'):
                    st.empty()
                    gender_val_stat = False
                if (gender == 'Male'):
                    gender_val = 1
                    st.write(
                        f':male-office-worker: : Male')
                    gender_val_stat = True
                if (gender == 'Female'):
                    gender_val = 2
                    st.write(
                        f':male-office-worker: : Female')
                    gender_val_stat = True
                if (gender_val_stat):
                    st.write(':robot_face: : Enter the age of the patient.')
                    age = st.number_input("Enter your age", min_value=0, max_value=120, value=0)
                    st.write(f':male-office-worker: : {age}')

                    if (age != 0):
                        st.write(':robot_face: : Are you smoking?')
                        smoking = st.selectbox('Select the answer', ('Select', 'Yes', 'No'))
                        smoking_val = 0
                        smoking_val_stat = False

                        if (smoking == 'Select'):
                            st.empty()
                            smoking_val_stat = False
                        if (smoking == 'Yes'):
                            smoking_val = 2
                            st.write(f':male-office-worker: : Yes')
                            smoking_val_stat = True
                        if (smoking == "No"):
                            smoking_val = 1
                            st.write(
                                f':male-office-worker: : No')
                            smoking_val_stat = True

                        if (smoking_val_stat):
                            st.write(':robot_face: : Are you having Yellow Fingers?')
                            yellow_fingers = st.selectbox('Select the answer about Yellow Fingers', ('Select', 'Yes', 'No'))
                            yellow_fingers_val = 0
                            yellow_fingers_val_stat = False
                            if (yellow_fingers == 'Select'):
                                st.empty()
                                yellow_fingers_val_stat = False
                            if (yellow_fingers == 'Yes'):
                                yellow_fingers_val = 2
                                st.write(f':male-office-worker: : Yes')
                                yellow_fingers_val_stat = True

                            if (yellow_fingers == 'No'):
                                yellow_fingers_val = 1
                                st.write(
                                    f':male-office-worker: : No')
                                yellow_fingers_val_stat = True

                            if (yellow_fingers_val_stat):
                                st.write(':robot_face: : Are you having Anxiety?')
                                anxiety = st.selectbox('Select the answer about Anxiety', ('Select', 'Yes', 'No'))
                                anxiety_val = 0
                                anxiety_val_stat = False

                                if (anxiety == 'Select'):
                                    st.empty()
                                    anxiety_val_stat = False
                                if (anxiety == 'Yes'):
                                    anxiety_val = 2
                                    st.write(f':male-office-worker: : Yes')
                                    anxiety_val_stat = True
                                if (anxiety == 'No'):
                                    anxiety_val = 1
                                    st.write(
                                            f':male-office-worker: : No')
                                    anxiety_val_stat = True

                                if (anxiety_val_stat):
                                    # Peer_pressure
                                    st.write(':robot_face: : Are you having peer pressure?')
                                    peer_pressure = st.selectbox('Select the answer about peer pressure',
                                                                 ('Select', 'Yes', 'No'))
                                    peer_pressure_val = 0
                                    peer_pressure_stat = False
                                    if (peer_pressure == 'Select'):
                                        st.empty()
                                        peer_pressure_stat = False
                                    if (peer_pressure == 'Yes'):
                                        peer_pressure_val = 2
                                        st.write(f':male-office-worker: : Yes')
                                        peer_pressure_stat = True
                                    if peer_pressure == 'No':
                                        peer_pressure_val = 1
                                        st.write(
                                            f':male-office-worker: : No')
                                        peer_pressure_stat = True

                                    if peer_pressure_stat:
                                        # Chronic Disease
                                        st.write(':robot_face: : Are you having Chronic Disease?')
                                        chronic_disease = st.selectbox('Select the answer about Chronic Disease',
                                                                       ('Select', 'Yes', 'No'))
                                        chronic_disease_val = 0
                                        chronic_disease_val_stat = False

                                        if chronic_disease == 'Select':
                                            st.empty()
                                            chronic_disease_val_stat = False

                                        if chronic_disease == 'Yes':
                                            chronic_disease_val = 2
                                            st.write(f':male-office-worker: : Yes')
                                            chronic_disease_val_stat = True

                                        if chronic_disease == 'No':
                                            chronic_disease_val = 1
                                            st.write(
                                                f':male-office-worker: : No')
                                            chronic_disease_val_stat = True

                                        if chronic_disease_val_stat:
                                            st.write('Are you experiencing Fatigue?')
                                            fatigue = st.selectbox('Select the answer about Fatigue',
                                                                   ('Select', 'Yes', 'No'))
                                            fatigue_val = 0
                                            fatigue_val_stat = False
                                            if fatigue == 'Select':
                                                st.empty()
                                                fatigue_val_stat = False
                                            if fatigue == 'Yes':
                                                fatigue_val = 2
                                                st.write(f':male-office-worker: : Yes')
                                                fatigue_val_stat = True
                                            if fatigue == 'No':
                                                fatigue_val = 1
                                                st.write(
                                                    f':male-office-worker: : No')
                                                fatigue_val_stat = True

                                            if fatigue_val_stat:
                                                st.write('Do you have Allergy?')
                                                allergy = st.selectbox('Select the answer about Allergy',
                                                                       ('Select', 'Yes', 'No'))
                                                allergy_val = 0
                                                allergy_val_stat = False
                                                if allergy == 'Select':
                                                    st.empty()
                                                    allergy_val_stat = False
                                                if allergy == 'Yes':
                                                    allergy_val = 2
                                                    st.write(f':male-office-worker: : Yes')
                                                    allergy_val_stat = True
                                                if allergy == 'No':
                                                    allergy_val = 1
                                                    st.write(
                                                        f':male-office-worker: : No')
                                                    allergy_val_stat = True

                                                if allergy_val_stat:
                                                    st.write('Are you experiencing Wheezing?')
                                                    wheezing = st.selectbox(
                                                        'Select the answer about Wheezing',
                                                        ('Select', 'Yes', 'No'))
                                                    wheezing_val = 0
                                                    wheezing_val_stat = False
                                                    if wheezing == 'Select':
                                                        st.empty()
                                                        wheezing_val_stat = False
                                                    if wheezing == 'Yes':
                                                        wheezing_val = 2
                                                        st.write(f':male-office-worker: : Yes')
                                                        wheezing_val_stat = True
                                                    if wheezing == 'No':
                                                        wheezing_val = 1
                                                        st.write(
                                                            f':male-office-worker: : No')
                                                        wheezing_val_stat = True

                                                    if wheezing_val_stat:
                                                        st.write('Do you consume alcohol?')
                                                        alcohol = st.selectbox(
                                                            'Select the answer about consume alcohol',
                                                            ('Select', 'Yes', 'No'))
                                                        alcohol_val = 0
                                                        alcohol_val_stat = False
                                                        if alcohol == 'Select':
                                                            st.empty()
                                                            alcohol_val_stat = False
                                                        if alcohol == 'Yes':
                                                            alcohol_val = 2
                                                            st.write(f':male-office-worker: : Yes')
                                                            alcohol_val_stat = True
                                                        if alcohol == 'No':
                                                            alcohol_val = 1
                                                            st.write(
                                                                f':male-office-worker: : No')
                                                            alcohol_val_stat = True

                                                        if alcohol_val_stat:
                                                            st.write('Are you experiencing Coughing?')
                                                            coughing = st.selectbox(
                                                                'Select the answer about Coughing',
                                                                ('Select', 'Yes', 'No'))
                                                            coughing_val = 0
                                                            coughing_val_stat = False
                                                            if coughing == 'Select':
                                                                st.empty()
                                                                coughing_val_stat = False
                                                            if coughing == 'Yes':
                                                                coughing_val = 2
                                                                st.write(f':male-office-worker: : Yes')
                                                                coughing_val_stat = True
                                                            if coughing == 'No':
                                                                coughing_val = 1
                                                                st.write(
                                                                    f':male-office-worker: : No')
                                                                coughing_val_stat = True

                                                            if coughing_val_stat:
                                                                st.write(
                                                                    'Are you experiencing Shortness of Breath?')
                                                                breathlessness = st.selectbox(
                                                                    'Select the answer about Shortness of Breath',
                                                                    ('Select', 'Yes', 'No'))
                                                                breathlessness_val = 0
                                                                breathlessness_val_stat = False
                                                                if breathlessness == 'Select':
                                                                    st.empty()
                                                                    breathlessness_val_stat = False
                                                                if breathlessness == 'Yes':
                                                                    breathlessness_val = 2
                                                                    st.write(f':male-office-worker: : Yes')
                                                                    breathlessness_val_stat = True
                                                                if breathlessness == 'No':
                                                                    breathlessness_val = 1
                                                                    st.write(
                                                                        f':male-office-worker: : No')
                                                                    breathlessness_val_stat = True

                                                                if breathlessness_val_stat:
                                                                    st.write('Do you have Swallowing Difficulty?')
                                                                    swallowing_difficulty = st.selectbox(
                                                                        'Select the answer about Swallowing Difficulty',
                                                                        ('Select', 'Yes', 'No'))
                                                                    swallowing_difficulty_val = 0
                                                                    swallowing_difficulty_val_stat = False
                                                                    if swallowing_difficulty == 'Select':
                                                                        st.empty()
                                                                        swallowing_difficulty_val_stat = False
                                                                    if swallowing_difficulty == 'Yes':
                                                                        swallowing_difficulty_val = 2
                                                                        st.write(
                                                                            f':male-office-worker: : Yes')
                                                                        swallowing_difficulty_val_stat = True
                                                                    if swallowing_difficulty == 'No':
                                                                        swallowing_difficulty_val = 1
                                                                        st.write(
                                                                            f':male-office-worker: : No')
                                                                        swallowing_difficulty_val_stat = True

                                                                    if swallowing_difficulty_val_stat:
                                                                        st.write('Are you experiencing Chest pain')
                                                                        chest_pain = st.selectbox(
                                                                            'Select the answer about Chest pain?',
                                                                            ('Select', 'Yes', 'No'))
                                                                        chest_pain_val = 0
                                                                        chest_pain_val_stat = False
                                                                        if chest_pain == 'Select':
                                                                            st.empty()
                                                                            chest_pain_val_stat = False
                                                                        if chest_pain == 'Yes':
                                                                            chest_pain_val = 2
                                                                            st.write(
                                                                                f':male-office-worker: : Yes')
                                                                            chest_pain_val_stat = True
                                                                        if chest_pain == 'No':
                                                                            chest_pain_val = 1
                                                                            st.write(
                                                                                f':male-office-worker: : No')
                                                                            chest_pain_val_stat = True

                                                                        if chest_pain_val_stat:
                                                                            st.write(
                                                                                'Have you been diagnosed with Lung Cancer?')
                                                                            lung_cancer = st.selectbox(
                                                                                'Select the answer about Lung Cancer?',
                                                                                ('Select', 'Yes', 'No'))
                                                                            lung_cancer_val = 0
                                                                            lung_cancer_val_stat = False
                                                                            if lung_cancer == 'Select':
                                                                                st.empty()
                                                                                lung_cancer_val_stat = False
                                                                            if lung_cancer == 'Yes':
                                                                                lung_cancer_val = 2
                                                                                st.write(
                                                                                    f':male-office-worker: : Yes')
                                                                                lung_cancer_val_stat = True
                                                                            if lung_cancer == 'No':
                                                                                lung_cancer_val = 1
                                                                                st.write(
                                                                                    f':male-office-worker: : No')
                                                                                lung_cancer_val_stat = True

                                                                            if (lung_cancer_val_stat):
                                                                                lung_cancer_data = [
                                                                                    gender_val, age,
                                                                                    smoking_val,
                                                                                    yellow_fingers_val,
                                                                                    anxiety_val,
                                                                                    peer_pressure_val,
                                                                                    fatigue_val,
                                                                                    allergy_val,
                                                                                    wheezing_val,
                                                                                    alcohol_val,
                                                                                    coughing_val,
                                                                                    breathlessness_val,
                                                                                    swallowing_difficulty_val,
                                                                                    chest_pain_val,
                                                                                    lung_cancer_val]

                                                                                lung_cancer_pred = lung_cancer_model.predict(
                                                                                    [lung_cancer_data])

                                                                                if lung_cancer_pred == 1:
                                                                                    st.error(
                                                                                        ':robot_face: : You may have the lung caner based on the provided data.')

                                                                                elif lung_cancer_pred == 2:
                                                                                    st.success(
                                                                                        ':robot_face: : You may not have the lung caner based on the provided data.')
                                                                                else:
                                                                                    st.error(
                                                                                        ':robot_face: : Unsupported Data !')

        if (type == 'Monkey Pox'):
            st.write(':robot_face: : Select the relevant disease type.')
            st.write(':male-office-worker: : Monkey Pox')
            st.write(':robot_face: : Do you have any of this common diseases?')
            Systemic_Illness = st.selectbox('Select the type of disease', ('Select',
                                                                           'None',
                                                                           'Fever',
                                                                           'Swollen Lymph Nodes',
                                                                           'Muscle Aches and Pain'))
            Systemic_Illness_val = 0
            Systemic_Illness_val_stat = False
            if (Systemic_Illness == 'Select'):
                st.empty()
                Systemic_Illness_val_stat = False
            elif (Systemic_Illness == 'None'):
                Systemic_Illness_val = 0
                st.write(
                    f':male-office-worker: : None')
                Systemic_Illness_val_stat = True
            elif (Systemic_Illness == 'Fever'):
                Systemic_Illness_val = 1
                st.write(
                    f':male-office-worker: : Fever')
                Systemic_Illness_val_stat = True
            elif (Systemic_Illness == 'Swollen Lymph Nodes'):
                Systemic_Illness_val = 2
                st.write(
                    f':male-office-worker: : Swollen Lymph Nodes')
                Systemic_Illness_val_stat = True
            else:
                Systemic_Illness_val = 3
                st.write(
                    f':male-office-worker: : Muscle Aches and Pain')
                Systemic_Illness_val_stat = True


            if (Systemic_Illness_val_stat):
                st.write(':robot_face: : Do you have any rectal pain?')
                Rectal_Pain = st.selectbox('Select the answer', ('Select', 'Yes', 'No'))
                Rectal_Pain_val = 0
                Rectal_Pain_val_stat = False
                if (Rectal_Pain == 'Select'):
                    st.empty()
                    Rectal_Pain_val_stat = False
                elif (Rectal_Pain == 'Yes'):
                    Rectal_Pain_val = 1
                    st.write(
                        f':male-office-worker: : Yes')
                    Rectal_Pain_val_stat = True
                else:
                    Rectal_Pain_val = 0
                    st.write(
                        f':male-office-worker: : No')
                    Rectal_Pain_val_stat = True

                if (Rectal_Pain_val_stat):
                    st.write(':robot_face: : Do you feel any soreness in your throat?')
                    Sore_throat = st.selectbox('Select the answer about throat', ('Select', 'Yes', 'No'))
                    Sore_throat_val = 0
                    Sore_throat_val_stat = False
                    if (Sore_throat == 'Select'):
                        st.empty()
                        Sore_throat_val_stat = False
                    elif (Sore_throat == 'Yes'):
                        Sore_throat_val = 1
                        st.write(
                            f':male-office-worker: : Yes')
                        Sore_throat_val_stat = True
                    else:
                        Sore_throat_val = 0
                        st.write(
                            f':male-office-worker: : No')
                        Sore_throat_val_stat = True

                    if (Sore_throat_val_stat):
                        st.write(':robot_face: : Do you feel any Penile Oedema?')
                        Penile_Oedema = st.selectbox('Select the answer about Penile Oedema', ('Select', 'Yes', 'No'))
                        Penile_Oedema_val = 0
                        Penile_Oedema_val_stat = False
                        if (Penile_Oedema == 'Select'):
                            st.empty()
                            Penile_Oedema_val_stat = False
                        elif (Penile_Oedema == 'Yes'):
                            Penile_Oedema_val = 1
                            st.write(
                                f':male-office-worker: : Yes')
                            Penile_Oedema_val_stat = True
                        else:
                            Penile_Oedema_val = 0
                            st.write(
                                f':male-office-worker: : No')
                            Penile_Oedema_val_stat = True

                        if (Penile_Oedema_val_stat):
                            st.write(':robot_face: : Do you have Oral Lesions?')
                            Oral_Lesions = st.selectbox('Select the answer about Oral Lesions',
                                                         ('Select', 'Yes', 'No'))
                            Oral_Lesions_val = 0
                            Oral_Lesions_val_stat = False
                            if (Oral_Lesions == 'Select'):
                                st.empty()
                                Oral_Lesions_val_stat = False
                            elif (Oral_Lesions == 'Yes'):
                                Oral_Lesions_val = 1
                                st.write(
                                    f':male-office-worker: : Yes')
                                Oral_Lesions_val_stat = True
                            else:
                                Oral_Lesions_val = 0
                                st.write(
                                    f':male-office-worker: : No')
                                Oral_Lesions_val_stat = True

                            if (Oral_Lesions_val_stat):
                                st.write(':robot_face: : Do you have Solitary Lesion?')
                                Solitary_Lesion = st.selectbox('Select the answer about Solitary Lesion',
                                                               ('Select', 'Yes', 'No'))
                                Solitary_Lesion_val = 0
                                Solitary_Lesion_val_stat = False
                                if (Solitary_Lesion == 'Select'):
                                    st.empty()
                                    Solitary_Lesion_val_stat = False
                                elif (Solitary_Lesion == 'Yes'):
                                    Solitary_Lesion_val = 1
                                    st.write(
                                        f':male-office-worker: : Yes')
                                    Solitary_Lesion_val_stat = True
                                else:
                                    Solitary_Lesion_val = 0
                                    st.write(
                                        f':male-office-worker: : No')
                                    Solitary_Lesion_val_stat = True

                                if (Solitary_Lesion_val_stat):
                                    st.write(':robot_face: : Do you have Swollen Tonsils?')
                                    Swollen_Tonsils = st.selectbox('Select the answer about Swollen Tonsils',
                                                                   ('Select', 'Yes', 'No'))
                                    Swollen_Tonsils_val = 0
                                    Swollen_Tonsils_val_stat = False
                                    if (Swollen_Tonsils == 'Select'):
                                        st.empty()
                                        Swollen_Tonsils_val_stat = False
                                    elif (Swollen_Tonsils == 'Yes'):
                                        Swollen_Tonsils_val = 1
                                        st.write(
                                            f':male-office-worker: : Yes')
                                        Swollen_Tonsils_val_stat = True
                                    else:
                                        Swollen_Tonsils_val = 0
                                        st.write(
                                            f':male-office-worker: : No')
                                        Swollen_Tonsils_val_stat = True

                                    if (Swollen_Tonsils_val_stat):
                                        st.write(':robot_face: : Do you have you ever infected HIV?')
                                        HIV_Infection = st.selectbox('Select the answer about HIV Infection',
                                                                       ('Select', 'Yes', 'No'))
                                        HIV_Infection_val = 0
                                        HIV_Infection_val_stat = False
                                        if (HIV_Infection == 'Select'):
                                            st.empty()
                                            HIV_Infection_val_stat = False
                                        elif (HIV_Infection == 'Yes'):
                                            HIV_Infection_val = 1
                                            st.write(
                                                f':male-office-worker: : Yes')
                                            HIV_Infection_val_stat = True
                                        else:
                                            HIV_Infection_val = 0
                                            st.write(
                                                f':male-office-worker: : No')
                                            HIV_Infection_val_stat = True

                                        if (HIV_Infection_val_stat):
                                            st.write(':robot_face: : Do you have any Sexually Transmitted Infection?')
                                            Sexually_Transmitted_Infection = st.selectbox('Select the answer about Sexually Transmitted Infection',
                                                                         ('Select', 'Yes', 'No'))
                                            Sexually_Transmitted_Infection_val = 0
                                            Sexually_Transmitted_Infection_val_stat = False
                                            if (Sexually_Transmitted_Infection == 'Select'):
                                                st.empty()
                                                Sexually_Transmitted_Infection_val_stat = False
                                            elif (Sexually_Transmitted_Infection == 'Yes'):
                                                Sexually_Transmitted_Infection_val = 1
                                                st.write(
                                                    f':male-office-worker: : Yes')
                                                Sexually_Transmitted_Infection_val_stat = True
                                            else:
                                                Sexually_Transmitted_Infection_val = 0
                                                st.write(
                                                    f':male-office-worker: : No')
                                                Sexually_Transmitted_Infection_val_stat = True

                                            if (Sexually_Transmitted_Infection_val_stat):
                                                monkey_pox_pred = monkey_pox_model.predict([[
                                                    Systemic_Illness_val, Rectal_Pain_val,
                                                    Sore_throat_val,
                                                    Penile_Oedema_val, Oral_Lesions_val, Solitary_Lesion_val,
                                                    Swollen_Tonsils_val,
                                                    HIV_Infection_val, Sexually_Transmitted_Infection_val
                                                ]])
                                                if monkey_pox_pred == 1:
                                                    st.error(
                                                        ':robot_face: : You may have the Monkey Pox virus based on the provided data.')

                                                elif monkey_pox_pred == 2:
                                                    st.success(
                                                        ':robot_face: : You may not have the Monkey Pox virus based on the provided data.')
                                                else:
                                                    st.error(
                                                    ':robot_face: : Unsupported Data !')


    with right:
        st.empty()