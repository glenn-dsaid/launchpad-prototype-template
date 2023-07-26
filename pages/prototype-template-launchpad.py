import streamlit as st
import time
from utils import feedback_logger

# ------------ TEMPLATE HEADER START (EDIT ONLY RELEVANT FIELDS) ------------


def feedback_section():  # Define feedback section content
    st.session_state.click_status = False

    # Feedback section
    feedback_logger.insert_feedback_form()


def form_callback():  # Define feedback callback
    st.session_state.click_status = True
    # To do something with the feedback. To be implemented


def response_disclaimer():
    # Display response disclaimer message (Edit where necessary)
    st.warning("""
            ***Reminder**: Please check the output above for inaccuracy or hallucination. When in doubt, do not use the AI's response. Avoid putting any Personal Identifiable Information (PII) in the prompts.*""")


def response_section():  # Define response section
    st.divider()
    st.subheader("Response")
    st.info(response)
    response_disclaimer()


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

# Display disclaimer message (Edit where necessary)
st.warning("""**Please read the following before proceeding:**
        *• This application is currently in **Beta version** and supports data classified up to **Restricted and Sensitive (Normal)**. 
        • **DO NOT** put Personal Identifiable Information (PII) within this application.
        • This application is under active testing and your prompts will be logged to improve your experience.
        • By using this application, you acknowledge that you recognise the possibility of AI generating inaccurate or wrong responses, and you take full responsibility over how you use the generated output.*""")

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
                                 'Bulk Output'], help="Provide a simple tooltip explanation to help user.", format_func=str)

# Context Input section (For all context related fields - to populate accordingly)
with st.expander("📖 **CONTEXT**", True):

    st.text_input("Context 01",
                  placeholder="provide a clear and concise explanation or examples to user", help="Provide a simple tooltip explanation to help user.")

    st.text_area("Context 02", help="""Provide a simple tooltip explanation to help user.""",
                 placeholder="provide a clear and concise explanation or examples to user", max_chars=1000)

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
            ('Low', 'Balanced', 'High'), help="Creativity regulates the randomness of the response. A higher creativity value typically makes the output more diverse but might also increase its likelihood of straying from the context.", index=1)


# FOR TESTING PURPOSES ONLY. To replace with actual reponse.
response = "The response will be shown here."

# Submit button with dummy spinner
if st.button("Submit", type="primary"):
    with st.spinner('Generating response...'):
        time.sleep(2)  # FOR TESTING PURPOSES ONLY. Remove when using template.
        response_section()
        st.session_state.response_msg = response
        feedback_section()

# To show response, disclaimer and thank you message when user click on feedback submit button
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

# Display application built from launchpad message
st.caption(
    "🛠️ Built from [LaunchPad](https://go.gov.sg/launchpad)")

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
