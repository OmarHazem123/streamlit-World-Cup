import streamlit as st

# Set page configuration
st.set_page_config(page_title='World Cup', page_icon="https://iconape.com/wp-content/files/qp/332288/png/332288.png")
# Function to add background image
def add_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://i.ytimg.com/vi/EXXe-G-_lxI/hq720.jpg?sqp=-oaymwEXCK4FEIIDSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLBkSIwwBv8CrafQQBbhNmjdVuSV5A");
            background-attachment: fixed;
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to add the background
add_background()

