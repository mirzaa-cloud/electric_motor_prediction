import pandas as pd

def preprocess_input(features_dict, feature_names, scaler):
    # Arrange input in the correct order and scale it
    X = pd.DataFrame([features_dict], columns=feature_names)
    X_scaled = scaler.transform(X)
    return X_scaled
