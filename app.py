# importing required libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# load the model
model = joblib.load('model.joblib')

# building the page

# container for title and logo
with st.container(border=False):

    # create two columns, one for logo and another for title
    logo_col, title_col = st.columns([.5, 2.5], border=False, vertical_alignment='center')

    # logo column
    with logo_col:

        # show logo image with 100 units width
        st.image('Images/logo.png', width=100)

    # title column
    with title_col:

        # title of the app
        st.write('# 🪪:blue[**Credit Card Approval**]💳')

# container for About the Project
with st.container(border=False):

    # expander for 'about the project' title
    with st.expander(':red[**ABOUT THE PROJECT**] 🚀', expanded=True):

        # about the project
        st.write(':green[**Credit Card Approval**] 🚀 is an :green[**Unsupervised Machine Learning**] project which decides whether an applicant can get a **:orange[Credit Card ✅ or Not] ❎**.')
        st.write(':blue[**K-Means**] clustering algorithm is used behind the development of this project.')

# container for input
with st.container(border=False):

    # creating two columns for input
    selectinp_col, enterinp_col = st.columns([2, 1], border=True)

    # under select input column
    with selectinp_col:

        # heading of the column
        st.write(':violet[**SELECT INPUTS**]')
        
        # cols for different inputs
        gender_inpcol, ownedcar_inpcol, ownedreal_inpcol = st.columns(3)

        # gender
        with gender_inpcol:
            gender = st.selectbox('**GENDER**', options=['Male', 'Female'])
            
            if gender == 'Male':
                gender = 'M'
            else:
                gender = 'F'
        
        # car owned
        with ownedcar_inpcol:
            car_owned = st.selectbox('**OWNED CAR**', options=['Yes', 'No'])

            if car_owned == 'Yes':
                car_owned = 'Y'
            else:
                car_owned = 'N'
            
        # reality owned
        with ownedreal_inpcol:
            reality_owned = st.selectbox('**OWNED REALITY**', options=['Yes', 'No'])

            if reality_owned == 'Yes':
                reality_owned = "Y"
            else:
                reality_owned = "N"
            
        # cols for some more selecting inputs
        incometype_inpcol, education_inpcol, housetype_inpcol = st.columns(3)

        # income type
        with incometype_inpcol:
            income_type = st.selectbox('**INCOME TYPE**', options=['Working', 'Com Associate', 'Pensioner', 'State Servant', 'Student'])

            if income_type == 'Com Associate':
                income_type = 'Commercial associate'
            elif income_type == 'State Servant':
                income_type = 'State servant'
            
        # education
        with education_inpcol:
            education = st.selectbox('**EDUCATION**', options=['Higher Ed', 'Secondary Ed', 'Incomplete Ed', 'Lower Sec Ed', 'Academic Degree'])

            if education == 'Higher Ed':
                education = 'Higher education'
            elif education == 'Secondary Ed':
                education = 'Secondary / secondary special'
            elif education == 'Incomplete Ed':
                education = 'Incomplete higher'
            elif education == 'Lower Sec Ed':
                education = 'Lower secondary'
            else:
                education = 'Academic degree'
            
        # house type
        with housetype_inpcol:
            house_type = st.selectbox('**HOUSE TYPE**', options=['Rented', 'House', 'Municipal','With Parents', 'Co-operative', 'Official'])

            if house_type == 'Rented':
                house_type = 'Rented apartment'
            elif house_type == 'House':
                house_type = 'House / apartment'
            elif house_type == 'Municipal':
                house_type = 'Municipal apartment'
            elif house_type == 'With Parents':
                house_type = 'With parents'
            elif house_type == 'Co-operative':
                house_type = 'Co-op apartment'
            else:
                house_type = 'Office apartment'
            
        # cols for more selecting inputs
        workingmobile_inpcol, havephone_inpcol, haveemail_inpcol = st.columns(3)

        # working mobile
        with workingmobile_inpcol:
            mobile_working = st.selectbox('**MOBILE WORKING**', options=['Yes', 'No'])

            if mobile_working == 'Yes':
                mobile_working = 1
            else:
                mobile_working = 0
            mobile_working = np.int64(mobile_working)

        # have phone
        with havephone_inpcol:
            have_phone = st.selectbox('**HAVE PHONE**', options=['Yes', 'No'])

            if have_phone == 'Yes':
                have_phone = 1
            else:
                have_phone = 0
            have_phone = np.int64(have_phone)
            
        # have email
        with haveemail_inpcol:
            have_email = st.selectbox('**HAVE EMAIL**', options=['Yes', 'No'])

            if have_email == 'Yes':
                have_email = 1
            else:
                have_email = 0
            have_email = np.int64(have_email)
            
        # lets some more columns
        occupation_inpcol, fammembers_inpcol, emptycol = st.columns(3)

        # occupation type
        with occupation_inpcol:
            occupation = st.selectbox('**OCCUPATION TYPE**', options=['Security', 'Sales', 'Accountants', 'Laborers',
       'Managers', 'Drivers', 'Core', 'High skill tech',
       'Cleaning', 'Private service', 'Cooking',
       'Low-skill', 'Medicine', 'Secretaries',
       'Waiters', 'HR', 'Realty agents', 'IT'])
            
            if occupation == 'Security':
                occupation = 'Security staff'
            elif occupation == 'Sales':
                occupation = 'Sales staff'
            elif occupation == 'Core':
                occupation = 'Core staff'
            elif occupation == 'High skill tech':
                occupation = 'High skill tech staff'
            elif occupation == 'Cleaning':
                occupation = 'Cleaning staff'
            elif occupation == 'Private service':
                occupation = 'Private service staff'
            elif occupation == 'Cooking':
                occupation = 'Cooking staff'
            elif occupation == 'Low-skill':
                occupation = 'Low-skill Laborers'
            elif occupation == 'Medicine':
                occupation = 'Medicine staff'
            elif occupation == 'Waiters':
                occupation = 'Waiters/barmen staff'
            elif occupation == 'HR':
                occupation = 'HR staff'
            elif occupation == 'IT':
                occupation = 'IT staff'
            
        # family members
        with fammembers_inpcol:
            family_members = st.selectbox('**FAMILY MEMBERS**', options=[1,2,3,4,5,6,7,8,9,11,14,15,20])
            family_members = np.float64(family_members)

    # under enter input column
    with enterinp_col:
        
        # heading of the column
        st.write(':violet[**ENTER INPUTS**]')

        # childrens
        childrens = st.slider('**CHILDRENS**', max_value=10, min_value=0)
        childrens = np.int64(childrens)
        
        # income
        min_income = 26100
        max_income = 6750000
        income = st.text_input('**INCOME**', placeholder=f'{min_income} to {max_income}')
        
        
        # days on earth
        min_days = 7489
        max_days = 25201
        days_on_earth = st.text_input('**DAYS ON EARTH**', placeholder=f'{min_days} to {max_days}')
        

        # employed days
        min_emp = 12
        max_emp = 365243
        employed_days = st.text_input('**EMPLOYED DAYS**', placeholder=f'{min_emp} to {max_emp}')
        
        if days_on_earth:
            days_on_earth = np.int64(days_on_earth)
        else:
            days_on_earth = 0

        if income:
            income = np.float64(income)
        else:
            income = 0
        
        if employed_days:
            employed_days = np.int64(employed_days)
        else:
            employed_days = 0
        
# container for output
with st.container():

    input_df = pd.DataFrame(data=[[gender, car_owned, reality_owned, childrens,income,income_type,education,
                                  house_type,days_on_earth,employed_days,mobile_working,have_phone,have_email,
                                  occupation,family_members]], 
                            columns=['gender', 'car_owned', 'reality_owned', 'childrens', 'income',
       'income_type', 'education', 'house_type', 'days_on_earth',
       'employed_days', 'mobile_working', 'have_phone', 'have_email',
       'occupation_type', 'family_members'])
    
    prediction = model.predict(input_df)
    if prediction == 1:
        st.success('**APPLICANT APPROVED ✅**')
    elif prediction == 0:
        st.error('**APPLICANT REJECTED ❌**')
    
# Container for External Feature of the app
with st.container():

    # five more cols for linking app with other platforms
    youtube_col, hfspace_col, madee_col, repo_col, linkedIn_col = st.columns([1,1.2,1.08,1,1], gap='small')

    # Youtube link
    with youtube_col:
        st.link_button('**VIDEO**', icon=':material/slideshow:', url='https://youtu.be/joAhwfslXZ4', help='YOUTUBE')
    
    # Hugging Face Space link
    with hfspace_col:
        st.link_button('**HF SPACE**', icon=':material/sentiment_satisfied:', url='https://huggingface.co/spaces/madhav-pani/Credit_Card_Approval/tree/main', help='HUGGING FACE SPACE')

    # Madee Link
    with madee_col:
        st.button('**MADEE**', icon=':material/flight:', disabled=True, help='MADEE')

    # Repository Link
    with repo_col:
        st.link_button('**REPO**', icon=':material/code_blocks:', url='https://github.com/madhavpani/Credict_Card_Approval', help='GITHUB REPOSITORY')

    # LinkedIn link
    with linkedIn_col:
        st.link_button('**CONNECT**', icon=':material/connect_without_contact:', url='https://www.linkedin.com/in/madhavpani', help='LINKEDIN')
