"Predict one delivery, from the command line."

import pandas as pd

from delivery import load_model


def main():
    # Load the trained model
    model = load_model("model.joblib")

    # Create the required order
    order = pd.DataFrame([{
        "distance_km": 7.0,
        "prep_time_min": 25,
        "traffic_level": 3,
        "rain": 0
    }])

    # Make the prediction
    minutes = model.predict(order)[0]

    # Print the prediction
    print(f"PREDICTION: {minutes:.1f}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
