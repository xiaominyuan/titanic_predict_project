import joblib
import os

import numpy as np
from sklearn.preprocessing import LabelEncoder

import logging

logger = logging.getLogger("titanic_project.model")


def load_model():
    current_dir = os.path.dirname(__file__)

    model_path = os.path.join(current_dir, '..', 'model', 'model.pkl')

    model = joblib.load(model_path)
    return model


def preprocess_data(data):
    label_encoder = LabelEncoder()

    if 'Sex' in data:
        data['Sex'] = label_encoder.fit_transform([data['Sex']])[0]

    if 'Embarked' in data:
        data['Embarked'] = label_encoder.fit_transform([data['Embarked']])[0]

    return np.array([[data['Pclass'], data['Sex'], data['Age'], data['SibSp'], data['Parch'], data['Fare'], data['Embarked']]])


def predict(data):
    model = load_model()
    processed_data = preprocess_data(data)
    prediction_proba = model.predict(processed_data, raw_score=False)

    survival_probability = prediction_proba[0]

    logger.info(f"Prediction survival_probability: {survival_probability}")
    return {
        'probability': survival_probability
    }