import os
import json
import joblib
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Liver Disease Prediction",
    page_icon="🩺",
    layout="wide"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "notebook", "model")

MODEL_PATH = os.path.join(MODEL_DIR, "liver_model.pkl")
SCALER_PATH = os.path.join(MODEL_DIR, "scaler.pkl")
FEATURES_PATH = os.path.join(MODEL_DIR, "feature_names.json")
METADATA_PATH = os.path.join(MODEL_DIR, "model_metadata.json")


@st.cache_resource
def load_artifacts():
    missing_files = []

    for path in [MODEL_PATH, SCALER_PATH, FEATURES_PATH]:
        if not os.path.exists(path):
            missing_files.append(path)

    if missing_files:
        raise FileNotFoundError(
            "Missing required files:\n" + "\n".join(missing_files)
        )

    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    with open(FEATURES_PATH, "r") as f:
        feature_names = json.load(f)

    metadata = {}
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH, "r") as f:
            metadata = json.load(f)

    return model, scaler, feature_names, metadata


def build_input_df(
    age,
    gender,
    total_bilirubin,
    direct_bilirubin,
    alkaline_phosphotase,
    alamine_aminotransferase,
    aspartate_aminotransferase,
    total_proteins,
    albumin,
    albumin_and_globulin_ratio,
    feature_names
):
    gender_value = 1 if gender == "Male" else 0

    input_dict = {
        "Age": age,
        "Gender": gender_value,
        "Total_Bilirubin": total_bilirubin,
        "Direct_Bilirubin": direct_bilirubin,
        "Alkaline_Phosphotase": alkaline_phosphotase,
        "Alamine_Aminotransferase": alamine_aminotransferase,
        "Aspartate_Aminotransferase": aspartate_aminotransferase,
        "Total_Proteins": total_proteins,
        "Albumin": albumin,
        "Albumin_and_Globulin_Ratio": albumin_and_globulin_ratio
    }

    input_df = pd.DataFrame([input_dict])

    for col in feature_names:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[feature_names]
    return input_df


try:
    model, scaler, feature_names, metadata = load_artifacts()
except Exception as e:
    st.error("Model files could not be loaded.")
    st.exception(e)
    st.stop()


st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        font-weight: 700;
        color: #FF4B4B;
        margin-bottom: 6px;
    }
    .subtitle {
        font-size: 18px;
        color: #555555;
        margin-bottom: 25px;
    }
    .result-box {
        padding: 16px;
        border-radius: 12px;
        margin-top: 18px;
        font-size: 22px;
        font-weight: 700;
        text-align: center;
    }
    .positive {
        background-color: #fdeaea;
        color: #a61b1b;
        border: 1px solid #f3b9b9;
    }
    .negative {
        background-color: #eaf7ea;
        color: #1b5e20;
        border: 1px solid #b8dfb8;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🩺 Liver Disease Prediction App</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Enter patient details to predict liver disease risk.</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("About")
    st.write("This app predicts whether a patient is likely to have liver disease.")
    if metadata:
        st.write(f"**Best Model:** {metadata.get('best_model', 'N/A')}")
    st.write("**Model files location:**")
    st.code(MODEL_DIR)

with st.form("prediction_form"):
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=45)
        gender = st.selectbox("Gender", ["Male", "Female"])
        total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0, value=1.0, step=0.1)
        direct_bilirubin = st.number_input("Direct Bilirubin", min_value=0.0, value=0.3, step=0.1)

    with col2:
        alkaline_phosphotase = st.number_input("Alkaline Phosphotase", min_value=0.0, value=200.0, step=1.0)
        alamine_aminotransferase = st.number_input("Alamine Aminotransferase", min_value=0.0, value=30.0, step=1.0)
        aspartate_aminotransferase = st.number_input("Aspartate Aminotransferase", min_value=0.0, value=35.0, step=1.0)

    with col3:
        total_proteins = st.number_input("Total Proteins", min_value=0.0, value=6.5, step=0.1)
        albumin = st.number_input("Albumin", min_value=0.0, value=3.2, step=0.1)
        albumin_and_globulin_ratio = st.number_input(
            "Albumin and Globulin Ratio",
            min_value=0.0,
            value=0.9,
            step=0.1
        )

    submitted = st.form_submit_button("Predict")

if submitted:
    try:
        input_df = build_input_df(
            age,
            gender,
            total_bilirubin,
            direct_bilirubin,
            alkaline_phosphotase,
            alamine_aminotransferase,
            aspartate_aminotransferase,
            total_proteins,
            albumin,
            albumin_and_globulin_ratio,
            feature_names
        )

        scaled_input = scaler.transform(input_df)
        prediction = model.predict(scaled_input)[0]

        probability = None
        if hasattr(model, "predict_proba"):
            class_list = list(model.classes_)
            positive_index = class_list.index(1) if 1 in class_list else 0
            probability = model.predict_proba(scaled_input)[0][positive_index]

        st.subheader("Prediction Result")

        if prediction == 1:
            st.markdown(
                '<div class="result-box positive">⚠️ Liver Disease Detected</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                '<div class="result-box negative">✅ No Liver Disease Detected</div>',
                unsafe_allow_html=True
            )

        if probability is not None:
            st.metric("Probability of Liver Disease", f"{probability * 100:.2f}%")

        st.subheader("Input Summary")
        st.dataframe(input_df, use_container_width=True)

    except Exception as e:
        st.error("Prediction failed.")
        st.exception(e)
