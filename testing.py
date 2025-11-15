"""
Quick test script to verify:
✅ Model loads correctly
✅ Prediction runs successfully
✅ Remedy lookup works properly
"""

import os
from PIL import Image
from smartcare.ml_model.disease_predictor import get_predictor
from smartcare.ml_model.disease_remedies import get_remedy, format_remedy_text

# --- CONFIG ---
# Path to any test leaf image from your dataset (JPG or PNG)
TEST_IMAGE = "media/disease_images/small-corn-plant-farm-natural-nepal-small-corn-plant-farm-natural-nepal-_Mb0pJJw.webp"

def test_prediction_and_remedy():
    print("🔍 Loading predictor...")
    predictor = get_predictor()

    # Check model and classes
    if predictor.model is None:
        print("❌ Model failed to load. Check path in disease_predictor.py")
        return

    print("✅ Model loaded successfully!")
    print(f"Total classes: {len(predictor.class_names)}")

    # --- Test Image ---
    if not os.path.exists(TEST_IMAGE):
        print(f"❌ Test image not found: {TEST_IMAGE}")
        return

    print(f"🖼️ Loading test image: {TEST_IMAGE}")
    img = Image.open(TEST_IMAGE)

    # --- Make Prediction ---
    print("🧠 Making prediction...")
    result = predictor.predict(img)

    disease = result["disease"]
    confidence = result["confidence"]
    print(f"\n✅ Predicted disease: {disease}")
    print(f"   Confidence: {confidence:.2f}%")

    print("\nTop 3 predictions:")
    for p in result["top_3_predictions"]:
        print(f"  - {p['disease']}: {p['confidence']:.2f}%")

    # --- Remedy lookup ---
    print("\n🌿 Fetching remedy info...")
    remedy_info = get_remedy(disease)
    remedy_text = format_remedy_text(disease, remedy_info)
    print("\nRemedy details:")
    print(remedy_text)

if __name__ == "__main__":
    test_prediction_and_remedy()
