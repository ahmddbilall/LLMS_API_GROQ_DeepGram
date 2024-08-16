import streamlit as st

st.title("About Me")

col1, col2 = st.columns([1, 2])  

with col1:
    st.image("image.jpeg", width=200)  

with col2:
    st.markdown("""
    <div style="text-align: justify;">
    I am currently pursuing a degree in Data Science at FAST National University, Lahore, where I have successfully completed two years of my academic journey. 

    <br><br>
    Prior to this, I completed my intermediate studies at Government College University, Lahore (GCU), where I developed a strong analytical and problem-solving mindset.
    
    </div>
    """, unsafe_allow_html=True)

st.write("### Skills:")
st.write("Python, C++, C#, SQL, Flutter, Data Analysis, Machine Learning, Deep Learning, Data Visualization, Web Development.")

st.write("### Tools:")
st.write("Jupyter Notebook, VS Code, Android Studio, Git, GitHub, Microsoft Office, visual studio, Adobe XD, Figma.")

st.write("### Languages:")
st.write("English, Urdu, Punjabi.")

st.write("----")

st.write("### Connect with Me:")
col1, col2, col3, col4,col5,col6,col7,col8 = st.columns(8)

with col1:
    st.markdown(
        '<a href="https://github.com/ahmddbilall" target="_blank"><img src="https://img.icons8.com/ios-filled/30/000000/github.png" alt="GitHub"/></a>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<a href="https://www.linkedin.com/in/ahmddbilall/" target="_blank"><img src="https://img.icons8.com/ios-filled/30/000000/linkedin.png" alt="LinkedIn"/></a>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<a href="https://leetcode.com/ahmddbilall/" target="_blank"><img src="https://img.icons8.com/external-tal-revivo-filled-tal-revivo/30/000000/external-level-up-your-coding-skills-and-quickly-land-a-job-logo-filled-tal-revivo.png" alt="LeetCode"/></a>',
        unsafe_allow_html=True
    )

with col4:
    st.markdown(
        '<a href="https://www.kaggle.com/ahmddbilall" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Kaggle_logo.png" width="50" alt="Kaggle"/></a>',
        unsafe_allow_html=True
    )

