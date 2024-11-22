#이전 수업 시간에 만들었던 이미지 분류 pkl 파일을 바탕으로 한 이미지 분류 모델을 Streamlit에 올리는 예제 코드
#파일 이름 streamlit_app.py

import streamlit as st
from fastai.vision.all import *
from PIL import Image
import gdown

    # 클래스별 확률을 HTML과 CSS로 시각화
    st.markdown("<h3>클래스별 확률:</h3>", unsafe_allow_html=True)

    if prediction == labels[0]:
         st.write("중냉 꿋굿")
    elif prediction == labels[1]:
         st.write("짜장면은 굿")
    elif prediction == labels[2]:
         st.write("짬뽕은 맵지만 맛있어!!")

    for label, prob in zip(labels, probs):
        # HTML 및 CSS로 확률을 시각화
        st.markdown(f"""
            <div style="background-color: #f0f0f0; border-radius: 5px; padding: 5px; margin: 5px 0;">
                <strong style="color: #333;">{label}:</strong>
                <div style="background-color: #d3d3d3; border-radius: 5px; width: 100%; padding: 2px;">
                    <div style="background-color: #4CAF50; width: {prob*100}%; padding: 5px 0; border-radius: 5px; text-align: center; color: white;">
                        {prob:.4f}
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)


