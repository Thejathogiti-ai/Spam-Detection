import pickle
import streamlit as st
model=pickle.load(open("MNB.pkl","rb"))

cv2=pickle.load(open("count_vectorizer.pkl","rb"))

st.title("Spam SMS Detection")

text=st.text_area("Enter SMS")

if st.button("predict"):
    vector=cv2.transform([text])
    predict=model.predict(vector)

    if predict[0]:
        st.error("spam")
    else:
        st.success("ham")