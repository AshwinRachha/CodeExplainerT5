from io import StringIO
import streamlit as st
import requests 
import json
import time



st.set_page_config(page_title="CATALYST", 
                   page_icon="https://endlessicons.com/wp-content/uploads/2012/12/fountain-pen-icon-614x460.png",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

def p_title(title):
    st.markdown(f'<h3 style="text-align: left; color:#F63366; font-size:28px;">{title}</h3>', unsafe_allow_html=True)

#########
#SIDEBAR
########

st.sidebar.header('CATALYST - I would like to :crystal_ball:')
nav = st.sidebar.radio('',['Go to homepage', 'Explain Code'])
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')
st.sidebar.write('')


if nav == 'Go to homepage':

    st.markdown("<h1 style='text-align: center; color: white; font-size:28px;'>Welcome to Catalyst!</h1>", unsafe_allow_html=True)
    #st.markdown("<h3 style='text-align: center; font-size:56px;'<p>&#129302;</p></h3>", unsafe_allow_html=True)
    #st.markdown("<img src="https://endlessicons.com/wp-content/uploads/2012/12/fountain-pen-icon-614x460.png" style="zoom: 50%;" />", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([6, 2, 6])
    col2.image("https://d1nhio0ox7pgb.cloudfront.net/_img/g_collection_png/standard/512x512/fountain_pen.png", width = 150)
    st.markdown("<h3 style='text-align: center; color: grey; font-size:20px;'>Dont know what an object is in Python or how list comprehensions work or even how fibonacci numbers are calculated in Python? Use our tool to write code and make it explain to you and learn better! !</h3>", unsafe_allow_html=True)

    st.markdown('___')
    st.write(':point_left: Use the menu at left to select a task (click on > if closed).')
    st.markdown('___')
    st.markdown("<h3 style='text-align: left; color:#F63366; font-size:18px;'><b>What is this App about?<b></h3>", unsafe_allow_html=True)
    st.write("")
    st.write("Python Code Explainer")     


if nav == 'Explain Code':    
    st.markdown("<h4 style='text-align: center; color:grey;'>Accelerate knowledge with Catalyst &#129302;</h4>", unsafe_allow_html=True)
    st.text('')
    p_title('Explain Code')
    st.text('')

    source = st.radio("How would you like to start? Choose an option below",
                          ("I want to input some text", "I want to upload a file"))
    st.text('')
    
    s_example = """
                class Solution(object):
                    def isValid(self, s):
                        stack = []
                        mapping = {")": "(", "}": "{", "]": "["}
                        for char in s:
                            if char in mapping:
                            top_element = stack.pop() if stack else '#'
                            if mapping[char] != top_element:
                                return False
                            else:
                                stack.append(char)
                        return not stack
                """
    if source == 'I want to input some text':
        input_su = st.text_area("Use the example below or input your own code with appropriate indentations)", value=s_example, max_chars=10000, height=330)
        if st.button('Explain Code'):
            with st.spinner('Processing...'):
                #time.sleep(2)
                st.markdown('___')
                st.write('Results Produces by CodeT5')
                    #convert string to json  
                response = requests.post("https://ashwinr-pythoncodeexplainer.hf.space/run/predict", json={
	                "data": [str(input_su),]}).json()
                
                data = response["data"]
                st.caption("Code explanation may not be taken upto full precision")
                st.success("".join(data))
                
                st.balloons()

    if source == 'I want to upload a file':
        file = st.file_uploader('Upload your file here',type=['txt'])
        if file is not None:
            with st.spinner('Processing...'):
                    time.sleep(2)
                    stringio = StringIO(file.getvalue().decode("utf-8"))
                    string_data = stringio.read()
                    time.sleep(2)
                    st.markdown('___')
                    st.write('Results Produces by CodeT5')
                    #convert string to json 
                    jsonfile = {
	                "data": [
                        string_data
	                        ]
                    }
                    response = requests.post("https://ashwinr-pythoncodeexplainer.hf.space/run/predict", json=jsonfile).json()
                    data = response["data"]
                    st.caption("Code explanation may not be taken upto full precision")
                    st.success(response)
                    st.balloons()
