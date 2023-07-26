import streamlit as st

st.set_page_config(page_title="LaunchPad Prototype Template",
                   page_icon="images/launchpad-icon.png", layout="centered")

launchpad_icon = "images/launchpad-icon.png"
st.image(launchpad_icon, width=100)

st.title("LaunchPad Prototype Template")

st.write("Welcome to the LaunchPad Prototype Template. ")

st.divider()

st.subheader("Guidelines & Standards")
st.write("The \"Guidelines and Standards\" section offers concise and practical tips to enhance the effective utilization of various commonly used Streamlit components.")

st.subheader("Generic Template")
st.write("The Generic Template is designed to be used by external agencies when creating prototypes. "
         "The template includes a generic icon and disclaimer prominently displayed in the header. Aside from these differences, the remaining content and structure of the template remain identical to the LaunchPad version.")
st.write(
    "[Download Generic Template](https://github.com/glenn-dsaid/launchpad-prototype-template/tree/main/template/generic)")

st.subheader("LaunchPad Template")
st.write("The LaunchPad Template is designed for internal team use when creating prototypes. "
         "The template includes a distinctive LaunchPad icon and a disclaimer prominently displayed in the header. Aside from these differences, the remaining content and structure of the template remain identical to the generic version.")
st.write(
    "[Download LaunchPad Template](https://github.com/glenn-dsaid/launchpad-prototype-template/tree/main/template/launchpad)")

st.divider()

# Changelog
changelog_text = """
##### Changelog

###### Version 1.0.1 (26 July 2023)
- Updated Generic and LaunchPad template with new disclaimer text.
- Added a utility function to send data as a log file to s3 bucket. 
- Updated the feedback form in `prototype-template-launchpad` template that use the utility function. \
  Refer to the docstring in `utils/feedback_logger.py` for more details, such as requirements and usage.

###### Version 1.0.0 (21 July 2023)
- Added template for Generic and Launchpad versions.
- Added a guideline page for usage of commonly used components on Streamlit.

"""

st.markdown(changelog_text)

# ------------ CONTENT AREA END (ADD CODE BEFORE HERE) ------------


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
