#!/usr/bin/env python
import os
import sys
import io
import json
import boto3
import logging
import streamlit as st
from dotenv import load_dotenv
from datetime import datetime
import pytz

__all__ = ["insert_feedback_form", "dictionary_to_log_on_s3"]

"""
This module contains functions to log data to S3.
There are two main methods:

1. insert_feedback_form(appdata_to_capture: dict = None)
    - This method renders the streamlit component for feedback form.
    - It takes a dictionary and combine the data in the feedback form.
    - It then sends the combined dictionary to S3 as a log

2. dictionary_to_log_on_s3(feedback_dictionary: dict = None) 
    - This method takes a dictionary and sends it to S3 as a log.
    - It can be used to send default logs, all inputs and the response, every time the "submit" button is clicked.
    - Suggest to use a different folder (than the one for feedback form) to collect the default logs.

Requirements:
- Create a S3 bucket and a IAM role with access to the bucket.
- Create a .env file with the following variables based on the IAM role:
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - REGION_NAME
- Install the dependencies in requirements.txt file
- Change the BUCKET_NAME variable to the name of your bucket.
"""

# Setup logging
logging.basicConfig(level=logging.INFO)

load_dotenv('.env')

# Specify the bucket name
BUCKET_NAME = 'YOUR_BUCKET_NAME'

# Create a high-level S3 resource object with your access keys
try:
    s3 = boto3.resource(
        's3',
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("REGION_NAME"),
    )
except Exception as e:
    logging.warning(f"Error creating S3 resource: {e}")
    raise e


def dictionary_to_log_on_s3(feedback_dictionary: dict = None):
    # Get the current datetime, convert to SGT and format it as a string to use in the filename
    timestamp = datetime.now()
    sgt = pytz.timezone('Asia/Singapore')
    timestamp = timestamp.astimezone(sgt)
    year_month = timestamp.strftime('%Y-%m')
    timestamp = timestamp.strftime('%Y-%m-%d_%H-%M-%S')

    # Use the timestamp as part of the filename, organize by year-month
    file_name = f'{year_month}/my_log_{timestamp}.json'

    try:
        # Convert the Python dictionary to a JSON string
        data_json = json.dumps(feedback_dictionary)

        # Create an in-memory text stream
        str_io = io.StringIO(data_json)

        # Upload the file
        s3.Object(BUCKET_NAME, file_name).put(Body=str_io.getvalue())
        logging.info(f"Successfully uploaded {file_name} to {BUCKET_NAME}.")
        return True
    except Exception as e:
        logging.warning(f"Error uploading to S3: {e}")
        return False


def insert_feedback_form(appdata_to_capture: dict = None) -> None:
    """
    Inserts a feedback form into the app.
    This method receives a dictionary of data to capture.
    Data to capture include the input prompt, configurations, and the response.
    The data will be combined with the feedback data and sent to S3 as a log.

    :param appdata_to_capture: dict. dictionary of data to capture. If None, a new dictionary will be created. \
    If not None, only the feedback_thumbs_updown, feedback_text, and feedback_email will be added to the dictionary and send as a log. \


    :return:
    """
    with st.expander("📨 **FEEDBACK ON THE RESPONSE**", expanded=False):
        with st.container():
            st.markdown('---')
            with st.form(key="feedback_form"):
                feedback_thumbs_updown = st.radio("How would you rate this particular response?",
                                                  ("positive", "negative"),
                                                  format_func=lambda x: "👍🏽" if x == "positive" else "👎🏽",
                                                  horizontal=True)
                st.write("")
                feedback_text = st.text_area("Please share your feedback with us", value="", height=150, max_chars=2500)
                feedback_email = st.text_input("Your email address (if you would like us to follow up with you)")
                st.write("")

                feedback_data = {
                    "feedback_thumbs_updown": feedback_thumbs_updown,
                    "feedback_text": feedback_text,
                    "feedback_email": feedback_email,
                }

                if appdata_to_capture:
                    appdata_to_capture.update(feedback_data)
                else:
                    appdata_to_capture = feedback_data

                st.markdown("<small>By submitting the form, I understand and agree that information for the current session "
                            "will be sent together with my feedback to developers for improving the application.</small>",
                            unsafe_allow_html=True)

                if st.form_submit_button("Submit"):
                    response = dictionary_to_log_on_s3(feedback_data)
                    if response:
                        st.success("Thank you for your feedback!")
                    else:
                        st.error("Oops! Something went wrong. Please try again later.")


if __name__ == "__main__":
    logging.warning("This script is not meant to be run directly.")
    sys.exit()