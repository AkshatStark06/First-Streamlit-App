import streamlit as st

st.title('Title -> Welcome to Stark Page')
st.header('Header -> Welcome to Stark Page')
st.subheader('subheading -> Welcome to Stark Page')
st.text('Text -> Welcome to Stark Page')

st.markdown('# Hi -> h1 tag')              #h1 tag
st.markdown('## Hi -> h2 tag')             #h2
st.markdown('### Hi -> h3 tag')            #h3
st.markdown('#### Hi -> h4 tag')           #h4
st.markdown('##### Hi -> h5 tag')          #h5
st.markdown('Hi -> paragraph tag')                #p

st.markdown('**Akshat** is in Bold')                  #Bold
st.markdown('__Akshat__ is also in Bold')             #Bold

st.markdown('*Akshat* is in Italic')                  #Italic
st.markdown('_Akshat_ is also in Italic')             #Italic

st.markdown('***Akshat*** is in Bold & Italic')       # Bold + Italic
st.markdown('___Akshat___ is also in Bold & Italic')  # Bold + Italic


st.markdown('- Unordered Lists')                      #Unordered List
st.markdown('- Unordered Lists')                      #Unordered List

st.markdown('1. Ordered List')                        #Ordered List
st.markdown('2. Ordered List')                        #Ordered List

st.markdown('''3. 3.1. Multiple                      
            3.2. Line       
            3.3. List  
            3.4. with   
            3.5. Sub-points
            ''')                                     #Multiple Line List


st.subheader('Success & Warning msgs')
st.success('Task Successful')
st.info('This method shows given Information')
st.warning('Warning')
st.error('Error! Occured')
st.exception(ZeroDivisionError('Div by zero not possible'))

st.help(ZeroDivisionError)

st.write('range(1,10)')
st.write(range(1,10))
st.write(1*2*3)

st.subheader('Code-Writing')
st.code('x = 10\n'
        'for i in range(x):\n'
        '\tprint(i)')

st.subheader('Checkboxes')
st.checkbox('Student')
st.checkbox('Coder')

if(st.checkbox('Alive')):
    st.write("You're alive!")


st.subheader('RadioButton')
radiobutton= st.radio('Select your Gender : ',options= ('Male', 'Female', 'Other'),
                      help ='Choose your Gender',horizontal = True)

if(radiobutton =='Male'):
    st.write("You're a Male")
elif(radiobutton=='Female'):
    st.write("You're a Female")
elif(radiobutton=='Other'):
    st.write("You're an Other Gender")
    
st.subheader('Select Box')
selectBox= st.selectbox("Select your preffered domain : ", ['Data Analysis','Web Scraping','Machine Learning',
                                             'Deep Learning','Data Science',"Natural Language Processing",
                                             'Computer Vision','Image Processing',
                                             'Generative AI','Transformers'],
                                             help= 'You can only choose one domain')

st.write("You've selected : ",selectBox)

st.subheader("Multi-SelectBox")
multiSelect= st.multiselect("Select your domain interests : ", ['Data Analysis','Web Scraping',
                                                'Machine Learning','Deep Learning',
                                                'Natural Language Processing',
                                                'Computer Vision','Image Processing',
                                                'Generative AI','Data Science','Transformers'],
                                                help= 'Choose all domain with your interests or experiences',
                                                default= 'Data Science')

st.write("You've selected : ", len(multiSelect),'courses')

st.subheader('Button')
st.button('Click here')

if (st.button('Submit your response')):
    st.write('Your response is submitted')

st.subheader('Color Picker')
color= st.color_picker('Select your prefered color for the theme :','#F0F2F6')
st.write('Your selected color code is : ',color)

st.subheader('Toggle')
on= st.toggle('Activate Kill Mode')
if on :
    st.write('Kill Mode Activated')


st.subheader('Slider')
vol= st.slider('Select the volume',1,100,step=1)
st.write('Volume is:',vol)

st.subheader('Text Input')
name= st.text_input('Name : ')
if (name):
    st.write('Hi ',name)

st.subheader('Username & Password')
username= st.text_input('Username : ', value = 'MrStark21')
password= st.text_input('Password : ',type='password')

st.subheader('Text Area')
textArea= st.text_area('Write why we should get back to you in 20 words',
                       max_chars=20,value='Placeholder text',height= 100)

st.subheader("Input Number")
st.number_input('Select your age : ',18,110, value= 21)


from datetime import datetime
from dateutil.relativedelta import relativedelta

st.subheader('Input Date')
st.date_input('Date')

st.subheader('Input Time')
st.time_input('Time')

st.subheader("Date Input using Datetime library")
today= datetime.now().date()

date= st.date_input('Enter your birth date : ', value= today,
                     min_value= today.replace(year=today.year - 30), 
                     max_value= datetime.now().date())
st.write('You were born on : ', datetime.strftime(date,'%d/%m/%Y'))
st.write("Today's date is : ",datetime.now().date().strftime('%d/%m/%Y'))

age_old= relativedelta(today, date)
st.write(f"You are {age_old.years} years, {age_old.months} months & {age_old.days} days old")










