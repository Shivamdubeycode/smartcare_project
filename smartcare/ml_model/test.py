from tensorflow.keras.models import load_model
import numpy as np

try:
    # Load the model
    model = load_model("smartcare/ml_model/best_model.keras")
    print("✅ Model loaded successfully")

    # Load class mapping
    class_indices = np.load("smartcare/ml_model/class_indices.npy", allow_pickle=True).item()
    print("✅ Class mapping loaded")
    print("Classes:", list(class_indices.keys()))

    # Optional: show model summary
    model.summary()

except Exception as e:
    print("❌ Error loading model or class mapping:")
    print(e)