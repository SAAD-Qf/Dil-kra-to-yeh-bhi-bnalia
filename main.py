import streamlit as st  # Streamlit library import kar rahe hain

# Function jo user ke input ke mutabiq response dega
def check_status(num):
    if num in ['Only Muslim', 'Muslim', 'Musalman']:  # Agar user sirf Muslim likhta hai
        return 'Wow Masallah You Are a Real Muslim 🦾'
    elif num == 'Im Barelvi':  # Agar user Barelvi hai
        return 'Mere Nabi (SAW) sa hai e koi nhi tere sare babay te shay e koi nhi 👆'
    elif num == 'Im Deobandi':  # Agar user Deobandi hai
        return 'Mian Log Kia Kahen ge (LGBTQ) 😘😋'
    elif num == 'Im Shia':  # Agar user Shia hai
        return 'You Are Rafidi 😂😂😂'
    elif num == 'Im Ehlehadis':  # Agar user Ehlehadis hai
        return '2812'
    elif num == 'Im Wahabi':  # Agar user Wahabi hai
        return 'You Are Nasbi (6229) Parh beta 😂😂😂🤣🤣'
    else:  # Agar user ne koi valid option select nahi kiya
        return 'Please Enter Valid Muslim Status'

# Streamlit ka UI part
st.title('Muslim Status Checker')  # App ka title set kar rahe hain

# Dropdown menu jo user se identity choose karne ko kahega
user_input = st.selectbox("Select your identity:", ['Only Muslim', 'Muslim', 'Musalman', 'Im Barelvi', 'Im Deobandi', 'Im Shia', 'Im Ehlehadis', 'Im Wahabi'])

# Button jab click hoga tab function call hoga
if st.button('Check Status'):
    result = check_status(user_input)  # Function ko call kar ke result store kar rahe hain
    st.success(result)  # Output ko Streamlit pe show kar rahe hain