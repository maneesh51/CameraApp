# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:06:42 2022

@author: yadav
"""

import cv2
import streamlit as st

st.title("Webcam Application")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
cam = cv2.VideoCapture(1)

while run:
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
else:
    st.write('Stopped')