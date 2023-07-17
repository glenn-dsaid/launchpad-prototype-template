import streamlit as st
import time
import datetime

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

    # Generate the response section with temperature
    with st.expander("**RESPONSE**", True):
        st.info(response)
        st.caption("Temperature: 5.0 (Balanced)")

    # Generate the actual prompt section
    with st.expander("**ACTUAL PROMPT**", False):
        st.info(actual_prompt)


# Initiate the submit button status
if 'click_status' not in st.session_state:
    st.session_state.click_status = False

# Initiate the response msg button status
if 'response_msg' not in st.session_state:
    st.session_state.response_msg = ""

# Set Streamlit app theme
st.set_page_config(page_title="LaunchPad Prototype Template",
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

# Initial bot selection.
with st.expander("⚙️ **BOT SELECTION**", expanded=True):
    st.selectbox('Select your bot', ['Marketing',
                                     'Speech', 'Testimonial'], help="test")

# Text Input
with st.expander("⚙️ **TEXT INPUT**", expanded=False):

    st.text_input("Text input label", help="""https://docs.streamlit.io/library/api-reference/widgets/st.text_input""",
                  placeholder="e.g. provide a clear and concise labels or examples to the user")
    st.divider()
    st.caption(
        """
            \n• Provide clear and concise labels for text input field.
            \n• Use consistent placeholder text to indicate the expected input format.
            \n• Use "e.g. example" when providing examples using the placeholder text.
            \n• Use tooltip help to provide additional guide to the user.
            \n• Use text input only if your expected input no longer than 1 line.
            \nhttps://docs.streamlit.io/library/api-reference/widgets/st.text_input""")

# Text Area
with st.expander("⚙️ **TEXT AREA**", expanded=False):

    st.text_area("Text area label", help="""Provide a simple tooltip explanation to help user.""",
                 placeholder="e.g. provide a clear and concise labels or examples to the user", max_chars=1000)
    st.divider()
    st.caption(
        """• Provide clear and concise labels for text area field.
            \n• Use consistent placeholder text to indicate the expected input format.
            \n• Use "e.g. example" when providing examples using the placeholder text.
            \n• Use tooltip help to provide additional guide to the user.
            \n• Provide a reasonable height for the text area to accommodate the expected input.
            \n• Consider limiting the maximum character count if necessary.""")

# Configuration
with st.expander("⚙️ **CONFIGURATIONS**", expanded=False):

    # Text Input
    st.text_input("Text input2", help="Provide a simple tooltip explanation to help user",
                  placeholder="e.g. Give an example or instruction to guide user")

    # Text Area
    st.text_area("Text area2", help="Provide a simple tooltip explanation to help user",
                 placeholder="e.g. Give an example or instruction to guide user")

    # Selectbox
    st.selectbox(
        'Selectbox',
        ('Option 1', 'Option 2', 'Option 3'), help="Provide a simple tooltip explanation to help user")

    # Multiselect
    st.multiselect(
        'Multiselect',
        ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
        ['Option 1', 'Option 2'], help="Provide a simple tooltip explanation to help user")

    # Checkbox
    st.checkbox('Option1', 'Option2')

    # Radio Button
    st.radio("Radio button",
             ('Option 1', 'Option 2', 'Option 3'), horizontal=True, help="Provide a simple tooltip explanation to help user")

    # Number Input
    st.number_input('Number input', min_value=0, step=1,
                    help="Provide a simple tooltip explanation to help user")

    # Slider
    st.slider('Slider', 0, 100, 1,
              help="Provide a simple tooltip explanation to help user")

    # Date input
    st.date_input(
        "Date input",
        datetime.date(2023, 5, 6),
        help="Provide a simple tooltip explanation to help user")

    # Time input
    st.time_input('Time input', datetime.time(12, 00),
                  help="Provide a simple tooltip explanation to help user")

    # File uploader
    st.file_uploader(
        "File uploader", help="Provide a simple tooltip explanation to help user")


# Generate response & feedback.
actual_prompt = "The actual prompt will be shown here."

# to replace prompt with the actual response
response = "The response will be shown here."

if st.button("Submit", type="primary"):
    with st.spinner('Generating response...'):
        time.sleep(2)  # For testing purposes
        response_section()
        st.session_state.response_msg = response
        feedback_section()

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
