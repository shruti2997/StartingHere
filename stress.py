import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Sample dataset
data = {
    'HRV': [70, 65, 50, 45, 80, 60, 40, 30, 75, 55, 35, 25, 65, 45, 55],
    'SpO2': [98, 97, 95, 92, 99, 96, 91, 90, 98, 95, 89, 88, 97, 93, 94],
    'GSR': [0.15, 0.20, 0.35, 0.40, 0.10, 0.25, 0.45, 0.50, 0.12, 0.30, 0.48, 0.55, 0.22, 0.38, 0.28],
    'Heart_Rate': [70, 75, 90, 95, 65, 85, 100, 105, 68, 88, 98, 110, 80, 92, 78],
    'Respiration_Rate': [12, 14, 18, 20, 11, 16, 22, 24, 13, 17, 21, 25, 15, 19, 16],
    'Skin_Temperature': [33, 32, 30, 29, 34, 31, 28, 27, 33, 30, 29, 26, 31, 28, 30],
    'Stress': [0, 0, 1, 2, 0, 1, 2, 2, 0, 1, 2, 2, 1, 2, 1]
}

df = pd.DataFrame(data)

X = df[['HRV', 'SpO2', 'GSR', 'Heart_Rate', 'Respiration_Rate', 'Skin_Temperature']].values
y = df['Stress'].values

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train SVM model
model = SVC(kernel='rbf', C=1.0, gamma='scale', random_state=42)
model.fit(X_train_scaled, y_train)

# Evaluate model
y_pred = model.predict(X_test_scaled)
print("Model Evaluation:")
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

thresholds = {
    'HRV': {'low': 40, 'medium': 60},
    'SpO2': {'low': 90},
    'GSR': {'medium': 0.25, 'high': 0.40},
    'Heart_Rate': {'medium': 85, 'high': 100},
    'Respiration_Rate': {'medium': 16, 'high': 22},
    'Skin_Temperature': {'low': 29, 'medium': 31}
}

def parameter_based_stress(hrv, spo2, gsr, hr, rr, skin_temp):
    stress_score = 0
    if hrv < thresholds['HRV']['low']:
        stress_score += 2
    elif hrv < thresholds['HRV']['medium']:
        stress_score += 1
    if spo2 < thresholds['SpO2']['low']:
        stress_score += 2
    if gsr > thresholds['GSR']['high']:
        stress_score += 2
    elif gsr > thresholds['GSR']['medium']:
        stress_score += 1
    if hr > thresholds['Heart_Rate']['high']:
        stress_score += 2
    elif hr > thresholds['Heart_Rate']['medium']:
        stress_score += 1
    if rr > thresholds['Respiration_Rate']['high']:
        stress_score += 2
    elif rr > thresholds['Respiration_Rate']['medium']:
        stress_score += 1
    if skin_temp < thresholds['Skin_Temperature']['low']:
        stress_score += 2
    elif skin_temp < thresholds['Skin_Temperature']['medium']:
        stress_score += 1
    if stress_score >= 7:
        return "High Stress"
    elif stress_score >= 3:
        return "Medium Stress"
    else:
        return "Low Stress"

def combined_stress_prediction(hrv, spo2, gsr, hr, rr, skin_temp):
    features = np.array([[hrv, spo2, gsr, hr, rr, skin_temp]])
    features_scaled = scaler.transform(features)
    ml_prediction = model.predict(features_scaled)[0]
    threshold_prediction = parameter_based_stress(hrv, spo2, gsr, hr, rr, skin_temp)
    ml_map = {0: "Low Stress", 1: "Medium Stress", 2: "High Stress"}
    # Prioritize High Stress if either method detects it
    if ml_map[ml_prediction] == "High Stress" or threshold_prediction == "High Stress":
        return "High Stress"
    elif ml_map[ml_prediction] == "Medium Stress" or threshold_prediction == "Medium Stress":
        return "Medium Stress"
    else:
        return "Low Stress"

def get_user_input():
    print("\nEnter test subject data. Type 'done' as the name when finished.\n")
    records = []
    while True:
        name = input("Enter test subject name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        try:
            hrv = float(input("HRV (ms): "))
            spo2 = float(input("SpO2 (%): "))
            gsr = float(input("GSR (microsiemens): "))
            hr = float(input("Heart Rate (bpm): "))
            rr = float(input("Respiration Rate (breaths/min): "))
            skin_temp = float(input("Skin Temperature (°C): "))
        except ValueError:
            print("Invalid input, please enter numeric values.")
            continue

        stress_level = combined_stress_prediction(hrv, spo2, gsr, hr, rr, skin_temp)
        records.append({
            "Name": name,
            "HRV": hrv,
            "SpO2": spo2,
            "GSR": gsr,
            "Heart Rate": hr,
            "Respiration Rate": rr,
            "Skin Temperature": skin_temp,
            "Stress Level": stress_level
        })
        print(f"Recorded {name}: {stress_level}\n")

    return records

def display_sorted_records(records):
    if not records:
        print("No data entered.")
        return
    df_records = pd.DataFrame(records)
    # Map stress levels to numeric for sorting
    stress_order = {"Low Stress": 0, "Medium Stress": 1, "High Stress": 2}
    df_records['StressOrder'] = df_records['Stress Level'].map(stress_order)
    df_sorted = df_records.sort_values('StressOrder')
    df_sorted = df_sorted.drop(columns='StressOrder')
    print("\nSorted Stress Level Records:")
    print(df_sorted.to_string(index=False))

if __name__ == "_main_":
    all_records = get_user_input()
    display_sorted_records(all_records)