import streamlit as st
import pandas as pd
import joblib
import pickle

# ==========================
# Load Files
# ==========================

model = joblib.load("model.pkl")

scaler = joblib.load("scaler.pkl")

with open("features.pkl", "rb") as f:
    features = pickle.load(f)

with open("feature_means.pkl", "rb") as f:
    feature_means = pickle.load(f)




# ==========================
# Streamlit UI
# ==========================

st.set_page_config(page_title="FIFA Player Performance Predictor")

st.title("⚽ FIFA Player Performance Predictor")

st.write("Predict whether a player will be a High Performer.")

# ==========================
# Player Information
# ==========================

st.header("Player Information")

age = st.number_input("Age", 16, 45, 25)

height_cm = st.number_input("Height (cm)", 150, 220, 180)

weight_kg = st.number_input("Weight (kg)", 50, 120, 75)

preferred_foot = st.selectbox(
    "Preferred Foot",
    ["Left", "Right"]
)

position = st.selectbox(
    "Position",
    ["Forward", "Midfielder", "Goalkeeper"]
)

# ==========================
# Match Information
# ==========================

st.header("Match Information")

teams = [
    "Argentina", "Australia", "Austria", "Belgium",
    "Brazil", "Cameroon", "Canada", "Chile",
    "Colombia", "Costa Rica", "Croatia", "Denmark",
    "Ecuador", "Egypt", "England", "France",
    "Germany", "Ghana", "Iran", "Iraq",
    "Italy", "Jamaica", "Japan", "Mexico",
    "Morocco", "Netherlands", "Nigeria", "Panama",
    "Peru", "Poland", "Portugal", "Qatar",
    "Saudi Arabia", "Scotland", "Senegal", "Serbia",
    "South Africa", "South Korea", "Spain", "Sweden",
    "Switzerland", "Tunisia", "Turkey", "Ukraine",
    "United States", "Uruguay", "Uzbekistan"
]

team = st.selectbox(
    "Team",
    teams,
    index=4  # Brazil
)

opponent_team = st.selectbox(
    "Opponent Team",
    teams,
    index=0  # Argentina
)

tournament_stage = st.selectbox(
    "Tournament Stage",
    [
        "Group Stage",
        "Round of 32",
        "Round of 16",
        "Quarter Finals",
        "Semi Finals",
        "Third Place Match"
    ]
)

match_result = st.selectbox(
    "Match Result",
    ["Win", "Draw", "Loss"]
)

# ==========================
# Performance Stats
# ==========================

st.header("Performance Statistics")

minutes_played = st.slider(
    "Minutes Played",
    0,
    120,
    90
)

goals = st.number_input(
    "Goals",
    0,
    10,
    0
)

assists = st.number_input(
    "Assists",
    0,
    10,
    0
)

shots = st.number_input(
    "Shots",
    0,
    20,
    3
)

shots_on_target = st.number_input(
    "Shots on Target",
    0,
    20,
    1
)

pass_accuracy = st.slider(
    "Pass Accuracy (%)",
    0.0,
    100.0,
    80.0
)

tackles = st.number_input(
    "Tackles",
    0,
    20,
    2
)

interceptions = st.number_input(
    "Interceptions",
    0,
    20,
    1
)

recoveries = st.number_input(
    "Recoveries",
    0,
    50,
    5
)

distance_covered_km = st.number_input(
    "Distance Covered (km)",
    0.0,
    20.0,
    10.0
)

top_speed_kmh = st.number_input(
    "Top Speed (km/h)",
    0.0,
    45.0,
    30.0
)

stamina_score = st.slider(
    "Stamina Score",
    0.0,
    100.0,
    75.0
)

# ==========================
# Prediction
# ==========================

if st.button("Predict"):

    # Start with mean values
    input_dict = feature_means.copy()

    # Numerical Inputs
    input_dict["age"] = age
    input_dict["height_cm"] = height_cm
    input_dict["weight_kg"] = weight_kg

    input_dict["minutes_played"] = minutes_played
    input_dict["goals"] = goals
    input_dict["assists"] = assists

    input_dict["shots"] = shots
    input_dict["shots_on_target"] = shots_on_target

    input_dict["pass_accuracy"] = pass_accuracy

    input_dict["tackles"] = tackles
    input_dict["interceptions"] = interceptions
    input_dict["recoveries"] = recoveries

    input_dict["distance_covered_km"] = distance_covered_km
    input_dict["top_speed_kmh"] = top_speed_kmh

    input_dict["stamina_score"] = stamina_score

    # Preferred Foot
    input_dict["preferred_foot"] = 1 if preferred_foot == "Right" else 0

    # One-Hot Encoding

    position_col = f"position_{position}"
    if position_col in input_dict:
        input_dict[position_col] = 1

    team_col = f"team_{team}"
    if team_col in input_dict:
        input_dict[team_col] = 1

    opponent_col = f"opponent_team_{opponent_team}"
    if opponent_col in input_dict:
        input_dict[opponent_col] = 1

    stage_col = f"tournament_stage_{tournament_stage}"
    if stage_col in input_dict:
        input_dict[stage_col] = 1

    if match_result == "Win":
        input_dict["match_result_W"] = 1

    elif match_result == "Loss":
        input_dict["match_result_L"] = 1

    # Create DataFrame
    input_df = pd.DataFrame([input_dict])

    # Ensure exact column order
    input_df = input_df[features]

    # Scale
    input_scaled = scaler.transform(input_df)

    # Prediction
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.success("🏆 High Performer")
    else:
        st.error("❌ Not a High Performer")