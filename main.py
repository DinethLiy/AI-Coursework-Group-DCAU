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

with open('models/covid_model.pickle', 'rb') as f:
    covid_model = pickle.load(f)

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
        type = st.selectbox('Select the disease type', ('Select', 'Covid', 'Heart disease', 'Lung Cancer'))

        if(type == 'Select'):
            st.empty()

        if(type == 'Covid'):
            st.write('BOT : Select the relevant disease type.')
            st.write('You : Covid')
            st.write('BOT : Did the patient treated in a medical unit?')
            usmr = st.selectbox('Select the answer', ('Select', 'Yes', 'No'))
            usmr_val = 0
            usmr_ans_stat = False
            if(usmr == 'Select'):
                st.empty()
            if (usmr == 'Yes'):
                usmr_val = 1
                usmr_ans_stat = True
                st.write('You : Yes')
            if (usmr == 'No'):
                usmr_val = 0
                usmr_ans_stat = True
                st.write('You : No')

            if(usmr_ans_stat):
                st.write('BOT : Select gender of the patient.')
                sex = st.selectbox('Gender', ('Select', 'Male', 'Female'))
                sex_val = 0
                gender_ans_stat = False
                if (sex == 'Select'):
                    st.empty()
                if (sex == 'Male'):
                    sex_val = 2
                    gender_ans_stat = True
                    st.write('You : Male')
                if (sex == 'Female'):
                    sex_val = 1
                    gender_ans_stat = True
                    st.write('You : Female')
                if(gender_ans_stat):
                    st.write('BOT : Did the patient returned home or hospitalized after the checkup?')
                    patient_type = st.selectbox('Select the patient type', ('Select', 'Returned Home', 'Hospitalized'))
                    patient_type_val = 0
                    patient_type_ans_stat = False
                    if (patient_type == 'Select'):
                        st.empty()
                    if (patient_type == 'Returned Home'):
                        patient_type_val = 1
                        patient_type_ans_stat = True
                        st.write('You : Returned Home')
                    if (patient_type == 'Hospitalized'):
                        patient_type_val = 2
                        patient_type_ans_stat = True
                        st.write('You : Hospitalized')

                    if(patient_type_ans_stat):
                        st.write('BOT : Did the patient was connected to the ventilator?')
                        intubed = st.selectbox('Select relevant answer', ('Select', 'Yes', 'No', 'No Idea'))
                        intubed_val = 0
                        intubed_ans_stat = False
                        if (intubed == 'Select'):
                            st.empty()
                        if (intubed == 'Yes'):
                            intubed_val = 1
                            intubed_ans_stat = True
                            st.write('You : Yes')
                        if (intubed == 'No'):
                            intubed_val = 2
                            intubed_ans_stat = True
                            st.write('You : No')
                        if(intubed == 'No Idea'):
                            intubed_val = 97
                            intubed_ans_stat = True
                            st.write('You : No Idea')

                        if(intubed_ans_stat):
                            st.write('BOT : Did the patient already have air sacs inflammation?')
                            pneumonia = st.selectbox('Select the answer about pneumonia', ('Select', 'Yes', 'No', 'No Idea'))
                            pneumonia_val = 0
                            pneumonia_ans_stat = False
                            if (pneumonia == 'Select'):
                                st.empty()
                            if (pneumonia == 'Yes'):
                                pneumonia_val = 1
                                pneumonia_ans_stat = True
                                st.write('You : Yes')
                            if (pneumonia == 'No'):
                                pneumonia_val = 2
                                pneumonia_ans_stat = True
                                st.write('You : No')
                            if (pneumonia == 'No Idea'):
                                pneumonia_val = 97
                                pneumonia_ans_stat = True
                                st.write('You : No Idea')

                            if(pneumonia_ans_stat):
                                st.write('BOT : Enter the age of the patient.')
                                age = st.number_input("Enter your age", min_value=0, max_value=120, value=0)
                                st.write(f'You : {age}')

                                if(age != 0):
                                    st.write('BOT : Did the patient was pregnant?')
                                    pregnant = st.selectbox('Select the answer about pregnancy', ('Select', 'Yes', 'No', 'No Idea'))
                                    pregnant_val = 0
                                    pregnant_ans_stat = False
                                    if (pregnant == 'Select'):
                                        st.empty()
                                    if (pregnant == 'Yes'):
                                        pregnant_val = 1
                                        pregnant_ans_stat = True
                                        st.write('You : Yes')
                                    if (pregnant == 'No'):
                                        pregnant_val = 2
                                        pregnant_ans_stat = True
                                        st.write('You : No')
                                    if (pregnant == 'No Idea'):
                                        pregnant_val = 97
                                        pregnant_ans_stat = True
                                        st.write('You : No Idea')

                                    if(pregnant_ans_stat):
                                        st.write('BOT : Did the patient have diabetes?')
                                        diabetes = st.selectbox('Select the answer about diabetes', ('Select', 'Yes', 'No', 'No Idea'))
                                        diabetes_val = 0
                                        diabetes_ans_stat = False
                                        if (diabetes == 'Select'):
                                            st.empty()
                                        if (diabetes == 'Yes'):
                                            diabetes_val = 1
                                            diabetes_ans_stat = True
                                            st.write('You : Yes')
                                        if (diabetes == 'No'):
                                            diabetes_val = 2
                                            diabetes_ans_stat = True
                                            st.write('You : No')
                                        if (diabetes == 'No Idea'):
                                            diabetes_val = 97
                                            diabetes_ans_stat = True
                                            st.write('You : No Idea')

                                        if(diabetes_ans_stat):
                                            st.write('BOT : Did the patient has Chronic Obstructive Pulmonary Disease?')
                                            copd = st.selectbox('Select the answer about COPD', ('Select', 'Yes', 'No', 'No Idea'))
                                            copd_val = 0
                                            copd_ans_stat = False
                                            if (copd == 'Select'):
                                                st.empty()
                                            if (copd == 'Yes'):
                                                copd_val = 1
                                                copd_ans_stat = True
                                                st.write('You : Yes')
                                            if (copd == 'No'):
                                                copd_val = 2
                                                copd_ans_stat = True
                                                st.write('You : No')
                                            if (copd == 'No Idea'):
                                                copd_val = 97
                                                copd_ans_stat = True
                                                st.write('You : No Idea')

                                            if(copd_ans_stat):
                                                st.write('BOT : Did the patient has Asthma?')
                                                asthma = st.selectbox('Select the answer about asthma', ('Select', 'Yes', 'No', 'No Idea'))
                                                asthma_val = 0
                                                asthma_ans_stat = False
                                                if (asthma == 'Select'):
                                                    st.empty()
                                                if (asthma == 'Yes'):
                                                    asthma_val = 1
                                                    asthma_ans_stat = True
                                                    st.write('You : Yes')
                                                if (asthma == 'No'):
                                                    asthma_val = 2
                                                    asthma_ans_stat = True
                                                    st.write('You : No')
                                                if (asthma == 'No Idea'):
                                                    asthma_val = 97
                                                    asthma_ans_stat = True
                                                    st.write('You : No Idea')

                                                if(asthma_ans_stat):
                                                    st.write('BOT : Did the patient have immunosuppression?')
                                                    inmsupr = st.selectbox('Select the answer about immunosuppression', ('Select', 'Yes', 'No', 'No Idea'))
                                                    inmsupr_val = 0
                                                    inmsupr_ans_stat = False
                                                    if inmsupr == 'Select':
                                                        st.empty()
                                                    elif inmsupr == 'Yes':
                                                        inmsupr_val = 1
                                                        inmsupr_ans_stat = True
                                                        st.write('You : Yes')
                                                    elif inmsupr == 'No':
                                                        inmsupr_val = 2
                                                        inmsupr_ans_stat = True
                                                        st.write('You : No')
                                                    else:
                                                        inmsupr_val = 97
                                                        inmsupr_ans_stat = True
                                                        st.write('You : No Idea')

                                                    if(inmsupr_ans_stat):
                                                        st.write('BOT : Did the patient have hypertension?')
                                                        hypertension = st.selectbox('Select the answer about hypertension', ('Select', 'Yes', 'No', 'No Idea'))
                                                        hypertension_val = 0
                                                        hypertension_ans_stat = False
                                                        if hypertension == 'Select':
                                                            st.empty()
                                                        elif hypertension == 'Yes':
                                                            hypertension_val = 1
                                                            hypertension_ans_stat = True
                                                            st.write('You : Yes')
                                                        elif hypertension == 'No':
                                                            hypertension_val = 2
                                                            hypertension_ans_stat = True
                                                            st.write('You : No')
                                                        else:
                                                            hypertension_val = 97
                                                            hypertension_ans_stat = True
                                                            st.write('You : No Idea')

                                                        if hypertension_ans_stat:
                                                            st.write('BOT : Did the patient has other disease?')
                                                            other_disease = st.selectbox('Select the answer about other disease', ('Select', 'Yes', 'No', 'No Idea'))
                                                            other_disease_val = 0
                                                            other_disease_ans_stat = False
                                                            if other_disease == 'Select':
                                                                st.empty()
                                                            elif other_disease == 'Yes':
                                                                other_disease_val = 1
                                                                other_disease_ans_stat = True
                                                                st.write('You : Yes')
                                                            elif other_disease == 'No':
                                                                other_disease_val = 2
                                                                other_disease_ans_stat = True
                                                                st.write('You : No')
                                                            else:
                                                                other_disease_val = 97
                                                                other_disease_ans_stat = True
                                                                st.write('You : No Idea')

                                                            if other_disease_ans_stat:
                                                                st.write('BOT : Did the patient has heart or blood vessels related disease?')
                                                                cardiovascular = st.selectbox('Select the answer about cardiovascular', ('Select', 'Yes', 'No', 'No Idea'))
                                                                cardiovascular_val = 0
                                                                cardiovascular_ans_stat = False
                                                                if cardiovascular == 'Select':
                                                                    st.empty()
                                                                elif cardiovascular == 'Yes':
                                                                    cardiovascular_val = 1
                                                                    cardiovascular_ans_stat = True
                                                                    st.write('You : Yes')
                                                                elif cardiovascular == 'No':
                                                                    cardiovascular_val = 2
                                                                    cardiovascular_ans_stat = True
                                                                    st.write('You : No')
                                                                else:
                                                                    cardiovascular_val = 97
                                                                    cardiovascular_ans_stat = True
                                                                    st.write('You : No Idea')

                                                                if cardiovascular_ans_stat:
                                                                    st.write('BOT : Did the patient obese?')
                                                                    obesity = st.selectbox('Select the answer about obesity', ('Select', 'Yes', 'No', 'No Idea'))
                                                                    obesity_val = 0
                                                                    obesity_ans_stat = False
                                                                    if obesity == 'Select':
                                                                        st.empty()
                                                                    elif obesity == 'Yes':
                                                                        obesity_val = 1
                                                                        obesity_ans_stat = True
                                                                        st.write('You : Yes')
                                                                    elif obesity == 'No':
                                                                        obesity_val = 2
                                                                        obesity_ans_stat = True
                                                                        st.write('You : No')
                                                                    else:
                                                                        obesity_val = 97
                                                                        obesity_ans_stat = True
                                                                        st.write('You : No Idea')

                                                                    if obesity_ans_stat:
                                                                        st.write('BOT : Did the patient has chronic renal disease?')
                                                                        renal_chronic = st.selectbox('Select the answer about chronic renal disease', ('Select', 'Yes', 'No', 'No Idea'))
                                                                        renal_chronic_val = 0
                                                                        renal_chronic_ans_stat = False
                                                                        if renal_chronic == 'Select':
                                                                            st.empty()
                                                                        elif renal_chronic == 'Yes':
                                                                            renal_chronic_val = 1
                                                                            renal_chronic_ans_stat = True
                                                                            st.write('You : Yes')
                                                                        elif renal_chronic == 'No':
                                                                            renal_chronic_val = 2
                                                                            renal_chronic_ans_stat = True
                                                                            st.write('You : No')
                                                                        else:
                                                                            renal_chronic_val = 97
                                                                            renal_chronic_ans_stat = True
                                                                            st.write('You : No Idea')

                                                                        if renal_chronic_ans_stat:
                                                                            st.write('BOT : Did the patient is a tobacco user?')
                                                                            tobacco = st.selectbox('Select the answer about use of tobacco', ('Select', 'Yes', 'No', 'No Idea'))
                                                                            tobacco_val = 0
                                                                            tobacco_ans_stat = False
                                                                            if tobacco == 'Select':
                                                                                st.empty()
                                                                            elif tobacco == 'Yes':
                                                                                tobacco_val = 1
                                                                                tobacco_ans_stat = True
                                                                                st.write('You : Yes')
                                                                            elif tobacco == 'No':
                                                                                tobacco_val = 2
                                                                                tobacco_ans_stat = True
                                                                                st.write('You : No')
                                                                            else:
                                                                                tobacco_val = 97
                                                                                tobacco_ans_stat = True
                                                                                st.write('You : No Idea')

                                                                            if tobacco_ans_stat:
                                                                                st.write('BOT : Did the patient had been admitted to an Intensive Care Unit?')
                                                                                icu = st.selectbox('Select the answer about ICU', ('Select', 'Yes', 'No', 'No Idea'))
                                                                                icu_val = 0
                                                                                icu_ans_stat = False
                                                                                if icu == 'Select':
                                                                                    st.empty()
                                                                                elif icu == 'Yes':
                                                                                    icu_val = 1
                                                                                    icu_ans_stat = True
                                                                                    st.write('You : Yes')
                                                                                elif icu == 'No':
                                                                                    icu_val = 2
                                                                                    icu_ans_stat = True
                                                                                    st.write('You : No')
                                                                                else:
                                                                                    icu_val = 0
                                                                                    icu_ans_stat = True
                                                                                    st.write('You : No')

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

                                                                                    if (covid_pred <= 3):
                                                                                        st.info(
                                                                                              'BOT : Based on the given data, The patient was diagnosed with covid in different degrees')
                                                                                        if st.button("Refresh"):
                                                                                            st.experimental_rerun()

                                                                                    elif (covid_pred >= 4):
                                                                                        st.info(
                                                                                              'BOT : Based on the given data, The patient is not a carrier of covid or that the test is inconclusive.')
                                                                                        if st.button("Refresh"):
                                                                                            st.experimental_rerun()



    with right:
        st.empty()