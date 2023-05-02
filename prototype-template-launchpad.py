import streamlit as st
import time

# ------------ TEMPLATE HEADER START (EDIT ONLY RELEVANT FIELDS) ------------


def feedback_section():  # Define feedback section content
    st.session_state.click_status = False

    # Feedback section
    with st.form("feedback_form"):
        feedback = st.radio(
            "How would you rate this response?", ("👍", "👎"), horizontal=True)
        comment = st.text_input("Additional comments (optional)")
        click_feedback = st.form_submit_button(
            label='Send feedback', on_click=form_callback)


def form_callback():  # Define feedback callback
    st.session_state.click_status = True
    # Do something with the feedback


def response_section():
    st.divider()
    st.subheader("Output")
    # Generate the actual prompt section
    with st.expander("**ACTUAL PROMPT**", False):
        st.write(actual_prompt)
    # Generate the response section with temperature
    with st.expander("**RESPONSE**", True):
        st.write(response)
        st.caption("Temperature: 5.0 (Balanced)")


# Initiate the submit button status
if 'click_status' not in st.session_state:
    st.session_state.click_status = False

# Initiate the response msg button status
if 'response_msg' not in st.session_state:
    st.session_state.response_msg = ""

# Set Streamlit app theme
st.set_page_config(page_title="LaunchPad Prototype",
                   page_icon="images/launchpad-icon.png", layout="centered")  # EDIT PAGE TITLE

# Display logo image
launchpad_icon = "images/launchpad-icon.png"
st.image(launchpad_icon, width=100)

# Set up app title
st.title("Application Title")  # EDIT TITLE

# Display disclaimer message
st.warning('**This application is in Alpha version**. You should avoid using it for general fact-finding and information retrieval and must never trust the responses completely.')

# Display information section
with st.expander("**APPLICATION TITLE**", False):   # EDIT TITLE
    # EDIT DESCRIPTION
    st.write('Application description here. Keep it to within 5 liners.')

st.divider()

# ------------ TEMPLATE HEADER END (EDIT ONLY RELEVANT FIELDS) ------------


# ------------ CONTENT AREA START (ADD CODE AFTER HERE) ------------

# (CAN DELETE) Content example. Always provide tooltip and placeholder example where applicable to guide user.
prompt = st.text_area("Text area", help="Provide a simple tooltip explanation to help user",
                      placeholder="Give an example or instruction to guide user")

# Generate response & feedback.
actual_prompt = "The actual prompt will be shown here."

# to replace prompt with the actual response
response = "The response will be shown here."


if st.button("Submit"):
    if prompt != "":  # check that prompt isn't empty
        with st.spinner('Generating response...'):
            time.sleep(2)  # For testing purposes
            response_section()
            st.session_state.response_msg = response
            feedback_section()
    else:
        st.error("You must input a prompt to get started")


if st.session_state.click_status:
    response_section()
    st.success("Thank you for your feedback!")

# ------------ CONTENT AREA END (ADD CODE BEFORE HERE) ------------


# ------------ TEMPLATE FOOTER START (EDIT ONLY RELEVANT FIELDS) ------------

st.divider()

# Display feedback message
st.info(
    "💬 Help us improve the application by [sharing your feedback with us](http://go.gov.sg/launchpad-gpt-feedback).")

# Hide streamlit footer
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ------------ TEMPLATE FOOTER END (EDIT ONLY RELEVANT FIELDS) ------------
