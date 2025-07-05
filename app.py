import bz2
import joblib
import numpy as np
import gradio as gr

# Load the compressed .pkl.bz2 model
try:
    with bz2.BZ2File("forecasting_co2_emmision.pkl.bz2", "rb") as f:
        model = joblib.load(f)
except Exception as e:
    model = None
    print("❌ Error loading model:", e)

# Prediction function
def predict(input_str):
    try:
        if model is None:
            return "Model not loaded."

        features = [float(x.strip()) for x in input_str.split(",")]
        input_array = np.array([features])
        prediction = model.predict(input_array)[0]
        return f"Predicted CO₂ Emission: {round(prediction, 2)} tons per capita"
    except Exception as e:
        return f"❌ Error during prediction: {e}"

# Gradio Interface
iface = gr.Interface(
    fn=predict,
    inputs=gr.Textbox(label="Input Features (Comma-separated)", placeholder="e.g., 45000, 3200, 78, 1400000000, 25, 0.26, 1.4"),
    outputs="text",
    title="🌍 CO₂ Emission Predictor",
    description="Enter 7 features separated by commas to predict CO₂ emissions (tons per capita).",
    theme="default"
)

# Launch the app locally and show the link in terminal
if __name__ == "__main__":
    iface.launch(share=False)
