import streamlit as st
import time
import datetime

# Set Streamlit app theme
st.set_page_config(page_title="Guideline",
                   page_icon="images/launchpad-icon.png", layout="centered")

# Display logo image
launchpad_icon = "images/launchpad-icon.png"
st.image(launchpad_icon, width=100)

# Set up app title
st.title("Guidelines and Standards")

# Display disclaimer message
st.write('This page offers concise and practical tips to enhance the effective utilization of various commonly used Streamlit components.')

st.divider()

# Input widget section start
st.markdown("""#### Input Widgets""")

# Text Input
with st.expander("💬 **TEXT INPUT**", expanded=False):

    st.text_input("Text input", help="""https://docs.streamlit.io/library/api-reference/widgets/st.text_input""",
                  placeholder="e.g. provide a clear and concise labels or examples to the user")
    st.divider()
    st.caption(
        """
            \n• Provide clear and concise labels for text input field.
            \n• Use consistent placeholder text to indicate the expected input format.
            \n• Use "e.g. example" when providing examples using the placeholder text.
            \n• Use tooltip help to provide additional guide to the user.
            \n• Use text input only if your expected input no longer than 1 line.""")

# Text Area
with st.expander("📝 **TEXT AREA**", expanded=False):

    st.text_area("Text area", help="""Provide a simple tooltip explanation to help user.""",
                 placeholder="e.g. provide a clear and concise labels or examples to the user", max_chars=1000)
    st.divider()
    st.caption(
        """• Provide clear and concise labels for text area field.
            \n• Use consistent placeholder text to indicate the expected input format.
            \n• Use "e.g. example" when providing examples using the placeholder text.
            \n• Use tooltip help to provide additional guide to the user.
            \n• Provide a reasonable height for the text area to accommodate the expected input.
            \n• Consider limiting the maximum character count if applicable.""")

# Selectbox
with st.expander("⏬ **SELECTBOX**", expanded=False):

    st.selectbox(
        'Selectbox',
        ('Option 1', 'Option 2', 'Option 3'), help="Provide a simple tooltip explanation to help user")
    st.divider()
    st.caption(
        """• Use meaningful and descriptive option labels for the selectbox.
            \n• Keep the list of options concise and relevant to the context of the application.
            \n• Ensure that the selectbox has default or pre-selected values that make sense in the context of the application, if applicable.
            \n• Use tooltip help to provide additional guide to the user.
            \n• Make sure the selectbox is wide enough to display the options without truncation or overflow.
            \n• If applicable, provide a "None" or "Not Applicable" option to account for scenarios where no specific option is suitable.""")

# MultiSelect
with st.expander("🌐 **MULTISELECT**", expanded=False):

    st.multiselect(
        'Multiselect',
        ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
        ['Option 1', 'Option 2'], help="Provide a simple tooltip explanation to help user")
    st.divider()
    st.caption(
        """• Clearly label the purpose of the multiselect to indicate that multiple options can be selected.
            \n• Keep the list of options concise and relevant to the context of the application.
            \n• Use tooltip help to provide additional guide to the user.
            \n• Ensure that the multiselect has default or pre-selected values that make sense in the context of the application, if applicable.
            \n• If applicable, provide a "None" or "Not Applicable" option to account for scenarios where no specific option is suitable.""")

# Checkbox
with st.expander("☑️ **CHECKBOX**", expanded=False):

    st.checkbox('Option1')
    st.checkbox('Option2')
    st.checkbox('Option3')
    st.divider()
    st.caption(
        """• Clearly label the purpose or action associated with the checkbox.
            \n• Always left-aligning checkboxes to create a clear visual association with the labels.
            \n• Avoid using too many checkboxes in a single group to prevent visual clutter and confusion.
            \n• Group related checkboxes together for better organization if necessary.""")

# Radio Button
with st.expander("◉ **RADIO BUTTON**", expanded=False):

    st.radio("Radio button",
             ('Option 1', 'Option 2', 'Option 3'), horizontal=True, help="Provide a simple tooltip explanation to help user")
    st.divider()
    st.caption(
        """• Clearly label the purpose of the radio button group to indicate the selection options.
            \n• Group related options together for better organization.
            \n• Ensure that only one option can be selected at a time.
            \n• Use tooltip help to provide additional guide to the user.
            \n• Avoid using too many radio buttons in a single group to prevent visual clutter and confusion.
            \n• Avoid using radio buttons when there are only two options; instead, consider using a checkbox for binary choices.""")

# Number Input
with st.expander("1️⃣ **NUMBER INPUT**", expanded=False):

    st.number_input('Number input', min_value=0, step=1,
                    help="Provide a simple tooltip explanation to help user")
    st.divider()
    st.caption(
        """• Clearly label the purpose or expected value for the number input.
            \n• Set appropriate boundaries (minimum and maximum values) if applicable.
            \n• Ensure that the number input accepts only valid numeric input.
            \n• Use consistent step values and formatting (e.g., decimal places, thousand separators) if needed.
            \n• Use tooltip help to provide additional guide to the user.
            \n• Provide default or pre-filled values when appropriate.""")

# Slider
with st.expander("🎛️ **SLIDER**", expanded=False):

    st.slider('Slider', 0, 100, 1,
              help="Provide a simple tooltip explanation to help user")
    st.divider()
    st.caption(
        """• Clearly label the purpose or range of the slider.
            \n• Set appropriate minimum and maximum values for the slider.
            \n• Use a consistent step or increment value to control the granularity of the slider.
            \n• If applicable, consider using a range slider (with two draggable handles) for scenarios where a range of values needs to be selected.
            \n• Provide default or pre-selected values when applicable to assist users in quickly selecting a value.
            \n• Consider using a logarithmic scale for the slider if the values span a wide range to improve user experience.""")

# Date Input
with st.expander("📅 **DATE INPUT**", expanded=False):

    st.date_input(
        "Date input",
        datetime.date(2023, 5, 6),
        help="Provide a simple tooltip explanation to help user")
    st.divider()
    st.caption(
        """• Clearly label the purpose or expected format(yyyy/mm/dd) for the date input. 
            \n• Consider setting appropriate date boundaries (minimum and maximum dates) if the input is limited to a specific range.
            \n• If relevant, allow users to manually input dates in addition to using the date picker.
            \n• If the date input is optional, consider providing a default value that makes sense in the context of the application.
            \n• Validate and provide error messages for incorrect or invalid date formats.""")

# Time Input
with st.expander("⌚ **TIME INPUT**", expanded=False):

    st.time_input('Time input', datetime.time(12, 00),
                  help="Provide a simple tooltip explanation to help user")
    st.divider()
    st.caption(
        """• Clearly label the purpose of the time input to indicate the expected time format (e.g., 24-hour format or AM/PM). If applicable, provide examples of the expected time format to guide users.
            \n• Consider setting appropriate time boundaries (minimum and maximum time) if the input is limited to a specific range.
            \n• If relevant, allow users to manually input times in addition to using the time picker.
            \n• If the time input is optional, consider providing a default value that makes sense in the context of the application.""")

# File Uploader
with st.expander("📂 **FILE UPLOADER**", expanded=False):

    st.file_uploader(
        "File uploader", accept_multiple_files=True,  type='txt, docx, pdf', help="Provide a simple tooltip explanation to help user")
    st.divider()
    st.caption(
        """• Clearly indicate the accepted file types for the uploader.
            \n• Limit the accepted file types to only what is necessary for the application to prevent irrelevant or unsupported files from being uploaded.
            \n• Specify the maximum file size that the uploader can handle.""")

# Button
with st.expander("📥 **BUTTON**", expanded=False):

    st.button("Primary Button", type='primary')
    st.button("Secondary Button", type='secondary')
    st.divider()
    st.caption(
        """• Use primary button for main action and accompany with secondary button if you need 2 buttons for different actions. Do not use 2 primary buttons alongside one another.
            \n• Clearly label the purpose of the button to indicate the action it performs. Consider using action-oriented labels like "Submit," "Save," "Apply," or "Search".
            \n• If the button performs a time-consuming action, provide feedback(st.spinner) to indicate that the action is in progress.
            \n• Disable the button when the action it triggers is not applicable or during processes that require completion before triggering the action again.
            """)

# Status elements section start
st.divider()
st.markdown("""#### Status Elements""")

# Info Status
with st.expander("ℹ️ **INFO STATUS**", expanded=False):

    st.info('Info Status')
    st.divider()
    st.caption(
        """• Utilize info messages to explain features, provide instructions, or share tips with users.
            \n• Keep info messages brief and informative to assist users without overwhelming them.""")


# Error Status
with st.expander("❌ **ERROR STATUS**", expanded=False):

    st.error('Error Status')
    st.divider()
    st.caption(
        """• Use error messages to inform users about critical errors that prevent the application from functioning correctly.
            \n• Provide clear and concise error messages that help users understand the problem and suggest possible solutions.
            \n• Avoid using error messages for non-critical issues or situations that users can easily recover from.""")

# Warning Status
with st.expander("⚠️ **WARNING STATUS**", expanded=False):

    st.warning('Warning Status')
    st.divider()
    st.caption(
        """• Utilize warning messages for situations that require user attention or action.
            \n• Keep warning messages concise and clear to communicate the message effectively.
            \n• Use warning messages sparingly to avoid overwhelming users with too many alerts.""")

# Success Status
with st.expander("✅ **SUCCESS STATUS**", expanded=False):

    st.success('Success Status')
    st.divider()
    st.caption(
        """• Provide positive feedback to users after they successfully complete an action.
            \n• Keep success messages short and to the point to reinforce the accomplishment.
            \n• Use success messages to create a positive user experience.""")


# Spinner
with st.expander("🌀 **SPINNERS**", expanded=False):

    def recursive_spinner():
        st.spinner("Use this for time-consuming action..")
        time.sleep(0.5)
        recursive_spinner()

    with st.spinner():
        recursive_spinner()

    st.divider()
    st.caption(
        """• Use the spinner for time-consuming action to indicate that the action is in progress.
        \n• Provide an error if the spinner takes too long to load. Do not let the user wait for too long for the action to take place. Provide a clear time indication if it will take long.
            """)


# ------------ TEMPLATE FOOTER START (EDIT ONLY RELEVANT FIELDS) ------------

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
