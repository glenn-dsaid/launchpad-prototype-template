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
    # To do something with the feedback. Not yet implemented


def response_section():  # Define response section
    st.divider()
    st.subheader("Response")
    st.info(response)


# Initiate the submit button status
if 'click_status' not in st.session_state:
    st.session_state.click_status = False

# Initiate the response msg button status
if 'response_msg' not in st.session_state:
    st.session_state.response_msg = ""

# Set Streamlit app theme
st.set_page_config(page_title="LaunchPad Prototype Template",
                   page_icon="images/launchpad-icon.png", layout="centered")  # USER TO EDIT PAGE TITLE

# Display logo image
launchpad_icon = "images/launchpad-icon.png"
st.image(launchpad_icon, width=100)

# Set up app title
st.title("Application Title")  # USER TO EDIT TITLE

# Display disclaimer message
st.warning('**This application is in Alpha version**. You should avoid using it for general fact-finding and information retrieval and must never trust the responses completely.')

# Display information section
with st.expander("**DESCRIPTION**", False):
    # EDIT DESCRIPTION
    st.write('Application description here. Keep it to within 5 liners.')

st.divider()

# ------------ TEMPLATE HEADER END (EDIT ONLY RELEVANT FIELDS) ------------


# ------------ CONTENT AREA START (ADD CODE AFTER HERE) ------------

# Mode selection section (Remove if not needed)
with st.expander("🔘 **MODE SELECTION**", expanded=True):
    st.selectbox('Select mode', ['Single Output',
                                 'Bulk Output'], help="Provide a simple tooltip explanation to help user.")

# Context Input section (For all context related fields - to populate accordingly)
with st.expander("📖 **CONTEXT**", True):

    st.text_input("Context 01",
                  placeholder="e.g. provide a clear and concise labels or examples to the user", help="Provide a simple tooltip explanation to help user.")

    st.text_area("Context 02", help="""Provide a simple tooltip explanation to help user.""",
                 placeholder="e.g. provide a clear and concise labels or examples to the user", max_chars=1000)

# Configurations section (For all CO-STAR related fields)
with st.expander("⚙️ **CONFIGURATIONS**", True):

    st.text_input("Target audience",
                  placeholder="e.g. general, parents, educators")

    col1, col2 = st.columns(2)

    with col1:
        st.text_input("Style of response",
                      placeholder="e.g. formal, informative, casual")

    with col2:
        st.text_input("Tone of response",
                      placeholder="e.g. friendly, professional, humorous")

    with col1:
        st.number_input('Length of response', min_value=0, step=25, value=100)

    with col2:
        st.selectbox(
            'Creativity',
            ('Low (Focused & Precise)', 'Balanced (Diverse & Coherent)', 'High (Creative & Surprising)'), help="Creativity regulates the randomness of the response.", index=1)


# FOR TESTING PURPOSES ONLY. To replace with actual reponse.
response = "The response will be shown here."

# Submit button with dummy spinner
if st.button("Submit", type="primary"):
    with st.spinner('Generating response...'):
        time.sleep(2)  # FOR TESTING PURPOSES ONLY. Remove when using template.
        response_section()
        st.session_state.response_msg = response
        feedback_section()

# To show response and thank you message when user click on feedback submit button
if st.session_state.click_status:
    response_section()
    st.success("Thank you for your feedback!")

# Actual prompt section
with st.expander("📝 **ACTUAL PROMPT**", False):
    st.markdown(
        """
        ```
        
        Please provide detailed information about the specific prompt that was utilized for the task. 
        Include all relevant details such as the input format, context, and any other important parameters 
        or settings used during the language model's execution. 
        
        ```
        """)

# ------------ CONTENT AREA END (ADD CODE BEFORE HERE) ------------


# ------------ TEMPLATE FOOTER START (EDIT ONLY RELEVANT FIELDS) ------------

st.divider()

# Display feedback message
st.info(
    "💬 Help us improve the application by [sharing your feedback with us](http://go.gov.sg/launchpad-gpt-feedback).")

# Hide streamlit footer
hide_streamlit_style = """
                <style>
                footer {display: none;}
                .stAlert {white-space:pre-wrap;}
                .st-bk,[role="alert"],input[type]:not([type="number"]),
                [data-baseweb="input"]:not(:has([type="number"])),
                [data-baseweb="textarea"],button[kind],
                [data-testid="stForm"], .focused.focused {
                    border-radius: 8px;
                }
                [data-baseweb="input"]:has([type="number"]) {
                    border-top-left-radius: 8px;
                    border-bottom-left-radius: 8px;
                }
                button.step-up.step-up {
                    border-top-right-radius: 8px;
                    border-bottom-right-radius: 8px;
                }
                [role="tab"] {
                    border-radius: 8px;
                    padding: 0 16px;
                    height: 30px;
                    margin-bottom: 4px;
                }

                [role="tab"].st-da,[role="tab"]:focus { background-color: #f1f2ff;  }
                .st-d2 { gap: 0.5rem }
                </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# ------------ TEMPLATE FOOTER END (EDIT ONLY RELEVANT FIELDS) ------------