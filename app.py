# -*- coding: utf-8 -*-
"""
Created on Tue Jan 27 17:32:56 2026

@author: BBarsch
"""

import streamlit as st

st.write("CSS2026 :)")

st.title("Would you love me if i was a worm and if so by how much")

st.write("Hello !")

st.header("Number selection")

number = st.slider("Pick a number", 1, 3000)
st.write(f"You picked: {number}")

#mark down - paragraphs and texts as ell as emoji

st.markdown(" Thank you ")



