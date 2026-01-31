# -*- coding: utf-8 -*-
"""
Created on Sat Jan 31 20:43:06 2026

@author: boipe
"""

import streamlit as st





# Set page title
st.set_page_config(page_title="Student Profile", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Student Profile", "Academic record", "Qualifications", "Contact"],
)


# Sections based on menu selection
if menu == "Student Profile":
    st.title("Student Profile")
    st.sidebar.header("Profile Options")

    # Collect basic information
    name = "Boipelo Letwaba"
    qualification = "BCom specialising in Economics"
    current_studies = "Bcom Honours specialising in Business Analytics "
    institution = "University of the Free State"

    # Display basic profile information
    st.write(f"**Name:** {name}")
    st.write(f"**Qualification:** {qualification}")
    st.write(f"**Studing:**{studing}")
    st.write(f"**Institution:** {institution}")
    
    st.image(
    "C:\Users\boipe\OneDrive\Pictures\WhatsApp Image 2025-10-10 at 12.12.18_8757f497.jpg",
    caption=" B Letwaba"
)

elif menu == "Academic record":
    st.title("Academic record")
    st.sidebar.header("Upload and Filter")

    # Upload pdf file
    uploaded_file = st.file_uploader("Upload a PDF file ", type=["pdf"])
    if uploaded_file is not None:
        #read the file to bytes
        bytes_data =uploaded_file.getvalue()
        #display pdf
        st.write("File uploaded successfully")
     
    else:
        st.info("Please upload a PDF file")


elif menu == "Qualifications":
    st.title("Qualifications")
    st.sidebar.header("Qualifications")
    st.markdown(" NSC Bachelors pass Lyttelton Manor High School 2020")
    st.markdown("BCom Economics University of the Free State 2025")
 

elif menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "boipeloletwaba@outlook.come"
    st.write(f"You can reach me at {email}.")



