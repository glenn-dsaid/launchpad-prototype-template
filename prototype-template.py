import streamlit as st

# --------------------- TEMPLATE HEADER START (DO NOT EDIT) ------------------------------

# Set Streamlit app theme
st.set_page_config(page_title="LaunchPad Prototype",
                   page_icon="images/launchpad-icon.png", layout="centered")

# Display logo image
launchpad_icon = "images/launchpad-icon.png"
st.image(launchpad_icon, width=100)

# Set up app title
st.title("Application Title")

# Display app information
st.warning('**This application is in Alpha version**. You should avoid using it for general fact-finding and information retrieval and must never trust the responses completely.')

# Add information section
with st.expander("Application Title", False):
    st.write('Application description here. Keep it to within 5 liners.')

st.divider()

# --------------------- TEMPLATE HEADER END (DO NOT EDIT) ------------------------------


# --------------------- CONTENT AREA START (ADD YOUR CODE AFTER HERE) ------------------

# Text area example. To provide tooltip and placeholder example where applicable to guide user.
prompt = st.text_area("Text area",
                      height=200, help="Provide a simple tooltip explanation to help user", placeholder="Give an example or instruction to guide user")

# Generate response example. To provide error using st.error and st.success as the response.
if st.button("Submit"):
    if prompt != "":
        with st.spinner('Generating response...'):
            st.divider()
            st.subheader("The response is:")
        st.success(prompt)
    else:
        st.error("You must input a prompt to get started")

# --------------------- CONTENT AREA END (ADD YOUR CODE BEFORE HERE) ----------------------


# --------------------- TEMPLATE FOOTER START (DO NOT EDIT) -------------------------------

st.divider()

# Display feedback message
st.info(
    "💬 Help us improve the application by sharing your [feedback with us](http://go.gov.sg/launchpad-gpt-feedback).")

# Hide streamlit footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ---------------------- TEMPLATE FOOTER END  (DO NOT EDIT) -------------------------------
