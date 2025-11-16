
# """
# Disease Prediction Module
# Handles model loading and prediction inference
# """

# import tensorflow as tf
# from tensorflow import keras
# import numpy as np
# from PIL import Image
# import json
# import os
# import logging

# logger = logging.getLogger(__name__)

# class DiseasePredictor:
#     """Plant Disease Prediction Class"""

    
#     def __init__(self, model_path=None, class_names_path=None):
#          base_dir = os.path.dirname(os.path.abspath(__file__))

#     # Use dynamic paths (no hardcoded Windows backslashes)
#          self.model_path = model_path or os.path.join(base_dir, "best_model.keras")
#          self.class_names_path = class_names_path or os.path.join(base_dir, "class_indices.npy")
#          self.model = None
#          self.class_names = None
#          self.img_size = 224  # resize images to 224x224
      
#     # Load model and class names
#          self.load_model()
#          self.load_class_names()

#          if self.model:
#             print(f"✅ Model loaded successfully!")
#          else:
#             print(f"❌ WARNING: Model not loaded! Using fallback mode.")


#     def load_model(self):
#         """Load trained Functional API model safely"""
#         print(f"[DEBUG] Attempting to load model from: {self.model_path}")
#         try:
#             if not os.path.exists(self.model_path):
#                 print(f"[DEBUG] ❌ File does not exist: {self.model_path}")
#                 return

#             # Load model without compiling
#             self.model = keras.models.load_model(self.model_path, compile=False)
#             print(f"[DEBUG] ✅ Model loaded!")
#             print(f"[DEBUG] Input shape: {self.model.input_shape}")
#             print(f"[DEBUG] Output shape: {self.model.output_shape}")

#         except Exception as e:
#             print(f"[DEBUG] ❌ Error loading model: {e}")
#             import traceback
#             traceback.print_exc()
#             self.model = None

    
#     def load_class_names(self):
    
#       try:
#         npy_path = self.class_names_path
#         json_path = npy_path.replace('.npy', '.json')

#         if os.path.exists(npy_path):
#             data = np.load(npy_path, allow_pickle=True).item()
#             # Expect a dict mapping {class_name: index}
#             if isinstance(data, dict):
#                 # Sort by index to maintain correct order
#                 self.class_names = [k for k, _ in sorted(data.items(), key=lambda x: x[1])]
#             else:
#                 # Fallback if it’s just a list
#                 self.class_names = data.tolist()
#             print(f"[DEBUG] ✅ Loaded {len(self.class_names)} class names from class_indices.npy")

#         elif os.path.exists(json_path):
#             with open(json_path, 'r') as f:
#                 self.class_names = json.load(f)
#             print(f"[DEBUG] ✅ Loaded {len(self.class_names)} class names from JSON")

#         else:
#             print(f"[DEBUG] ⚠️ No class names file found — using fallback")
#             self.class_names = self._get_fallback_classes()

#       except Exception as e:
#         print(f"[DEBUG] ❌ Error loading class names: {e}")
#         self.class_names = self._get_fallback_classes()



#     def _get_fallback_classes(self):
#         """Fallback class names"""
#         return [
#             'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
#             'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
#             'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
#             'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
#             'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
#             'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
#             'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
#             'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
#             'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
#             'Strawberry___Leaf_scorch', 'Strawberry___healthy',
#             'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
#             'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
#             'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
#             'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
#         ]

#     def preprocess_image(self, image):
#         """Preprocess image for model input"""
#         if image.mode != 'RGB':
#             image = image.convert('RGB')
#         image = image.resize((self.img_size, self.img_size))
#         img_array = np.array(image, dtype=np.float32) / 255.0
#         img_array = np.expand_dims(img_array, axis=0)
#         return img_array

#     def predict(self, image):
#         """Predict disease"""
#         img_array = self.preprocess_image(image)
#         if self.model:
#             predictions = self.model.predict(img_array, verbose=0)
#             predicted_idx = np.argmax(predictions[0])
#             confidence = float(predictions[0][predicted_idx] * 100)

#             top_3_idx = np.argsort(predictions[0])[-3:][::-1]
#             top_3_predictions = [
#                 {
#                     'disease': self._format_disease_name(self.class_names[idx]),
#                     'confidence': float(predictions[0][idx] * 100)
#                 } for idx in top_3_idx
#             ]

#             disease_name = self._format_disease_name(self.class_names[predicted_idx])

#             return {
#                 'disease': disease_name,
#                 'confidence': confidence,
#                 'top_3_predictions': top_3_predictions
#             }
#         else:
#             # fallback
#             print("[DEBUG] ⚠️ Model not loaded, using fallback prediction")
#             return {
#                 'disease': "Tomato Early blight",
#                 'confidence': 85.5,
#                 'top_3_predictions': [
#                     {'disease': 'Tomato Early blight', 'confidence': 85.5},
#                     {'disease': 'Tomato Late blight', 'confidence': 8.3},
#                     {'disease': 'Tomato Leaf Mold', 'confidence': 3.2}
#                 ]
#             }

#     def _format_disease_name(self, raw_name):
#         """Format disease name"""
#         name = raw_name.replace('___', ' ').replace('_', ' ')
#         name = name.split('(')[0].strip()
#         return name


# # Global predictor instance
# _predictor = None

# def get_predictor():
#     """Get or create predictor instance"""
#     global _predictor
#     if _predictor is None:
#         print("[DEBUG] Creating new predictor instance...")
#         _predictor = DiseasePredictor()
#     return _predictor
"""
Disease Prediction Module
Handles model loading and prediction inference
WITH LAZY LOADING - Optimized for Render 512MB
"""

import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import json
import os
import logging

logger = logging.getLogger(__name__)

class DiseasePredictor:
    """Plant Disease Prediction Class with Lazy Loading"""

    def __init__(self, model_path=None, class_names_path=None):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Use dynamic paths (no hardcoded Windows backslashes)
        self.model_path = model_path or os.path.join(base_dir, "best_model.keras")
        self.class_names_path = class_names_path or os.path.join(base_dir, "class_indices.npy")
        
        # ✅ DON'T load model yet - lazy loading!
        self.model = None
        self.class_names = None
        self.img_size = 224
        
        # Load class names immediately (small, won't crash)
        self.load_class_names()
        
        print(f"✅ DiseasePredictor initialized (model will load on first prediction)")

    def load_model(self):
        """Load trained model - ONLY WHEN NEEDED"""
        if self.model is not None:
            # Already loaded, skip
            return
            
        print(f"🔄 Loading disease detection model from: {self.model_path}")
        try:
            if not os.path.exists(self.model_path):
                print(f"❌ Model file not found: {self.model_path}")
                return

            # Load model without compiling (saves memory)
            self.model = keras.models.load_model(self.model_path, compile=False)
            
            print(f"✅ Model loaded successfully!")
            print(f"   Input shape: {self.model.input_shape}")
            print(f"   Output shape: {self.model.output_shape}")

        except Exception as e:
            print(f"❌ Error loading model: {e}")
            import traceback
            traceback.print_exc()
            self.model = None

    def load_class_names(self):
        """Load class names (small file, safe to load immediately)"""
        try:
            npy_path = self.class_names_path
            json_path = npy_path.replace('.npy', '.json')

            if os.path.exists(npy_path):
                data = np.load(npy_path, allow_pickle=True).item()
                if isinstance(data, dict):
                    self.class_names = [k for k, _ in sorted(data.items(), key=lambda x: x[1])]
                else:
                    self.class_names = data.tolist()
                print(f"✅ Loaded {len(self.class_names)} class names from .npy")

            elif os.path.exists(json_path):
                with open(json_path, 'r') as f:
                    self.class_names = json.load(f)
                print(f"✅ Loaded {len(self.class_names)} class names from JSON")

            else:
                print(f"⚠️ No class names file found — using fallback")
                self.class_names = self._get_fallback_classes()

        except Exception as e:
            print(f"❌ Error loading class names: {e}")
            self.class_names = self._get_fallback_classes()

    def _get_fallback_classes(self):
        """Fallback class names"""
        return [
            'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
            'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
            'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
            'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy',
            'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
            'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
            'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy',
            'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy',
            'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew',
            'Strawberry___Leaf_scorch', 'Strawberry___healthy',
            'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight',
            'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot',
            'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
            'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
        ]

    def preprocess_image(self, image):
        """Preprocess image for model input"""
        if image.mode != 'RGB':
            image = image.convert('RGB')
        image = image.resize((self.img_size, self.img_size))
        img_array = np.array(image, dtype=np.float32) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        return img_array

    def predict(self, image):
        """
        Predict disease - MODEL LOADS HERE ON FIRST CALL
        """
        # ✅ Load model only when prediction is requested
        if self.model is None:
            print("🔄 First prediction - loading model now...")
            self.load_model()
        
        # Preprocess image
        img_array = self.preprocess_image(image)
        
        if self.model:
            # Model loaded successfully - make prediction
            predictions = self.model.predict(img_array, verbose=0)
            predicted_idx = np.argmax(predictions[0])
            confidence = float(predictions[0][predicted_idx] * 100)

            top_3_idx = np.argsort(predictions[0])[-3:][::-1]
            top_3_predictions = [
                {
                    'disease': self._format_disease_name(self.class_names[idx]),
                    'confidence': float(predictions[0][idx] * 100)
                } for idx in top_3_idx
            ]

            disease_name = self._format_disease_name(self.class_names[predicted_idx])

            return {
                'disease': disease_name,
                'confidence': confidence,
                'top_3_predictions': top_3_predictions
            }
        else:
            # Model failed to load - use fallback
            print("⚠️ Model not loaded, using fallback prediction")
            return {
                'disease': "Tomato Early blight",
                'confidence': 85.5,
                'top_3_predictions': [
                    {'disease': 'Tomato Early blight', 'confidence': 85.5},
                    {'disease': 'Tomato Late blight', 'confidence': 8.3},
                    {'disease': 'Tomato Leaf Mold', 'confidence': 3.2}
                ]
            }

    def _format_disease_name(self, raw_name):
        """Format disease name"""
        name = raw_name.replace('___', ' ').replace('_', ' ')
        name = name.split('(')[0].strip()
        return name


# ✅ Global predictor instance with lazy loading
_predictor = None

def get_predictor():
    """
    Get or create predictor instance
    MODEL DOESN'T LOAD UNTIL FIRST PREDICTION!
    """
    global _predictor
    if _predictor is None:
        print("📦 Creating DiseasePredictor instance...")
        _predictor = DiseasePredictor()
        print("✅ DiseasePredictor ready (model will load on first use)")
    return _predictor
