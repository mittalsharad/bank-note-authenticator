#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:18:48 2021

@author: sharad
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle 
import streamlit as st
from PIL import Image


pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome to Flask API"


def predict_note_auth(variance,skewness,curtosis,entropy):
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return prediction


def main():
    st.title("Bank Note Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance=st.text_input("Variance","Type Here")
    skewness=st.text_input("Skewness","Type Here")
    curtosis=st.text_input("Curtosis","Type Here")
    entropy=st.text_input("Entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=predict_note_auth(variance,skewness,curtosis,entropy)
    st.success('The Output is {}'.format(result))
    if st.button("About"):
        st.text("Learning Flask, Flasgger, Docker & Streamlit")
        st.text("API built with Streamlit")

                                                       
if __name__== '__main__':
    main()