import pickle
import streamlit as st
from PIL import Image
from sklearn.feature_extraction.text import TfidfVectorizer

model_fraud = pickle.load(open('model_fraud.sav', 'rb'))

tfidf = TfidfVectorizer

loaded_vec = TfidfVectorizer(decode_error="replace", vocabulary=set(
    pickle.load(open("new_selected_feature_tf-idf.sav", "rb"))))


# Judul
st.title('DETEKSI REVIEWS')
st.subheader("Tugas UAS Business intelligence")
st.markdown("NENDA PUTRI SUCIATY")
st.markdown("191351065")

st.header("COBA REVIEWS")
clean_reviews = st.text_input('MASUKAN KATA :')

fraud_detection = ''
if st.button('HASIL REVIEWS'):
    predict_fraud = model_fraud.predict(
        loaded_vec.fit_transform([clean_reviews]))

    if (predict_fraud == 1):
        fraud_detection = 'INI REVIEWS POSITIF'
    else:
        fraud_detection = 'INI REVIEWS NEGATIF'
    st.success(fraud_detection)
