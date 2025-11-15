# """
# Plant Disease Detection Model Training Script
# Dataset: PlantVillage (54,000+ images, 38 classes)

# Run this script once to train and save the model:
# python smartcare/ml_model/train_model.py
# """

# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import layers # type: ignore
# from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
# from tensorflow.keras.applications import MobileNetV2 # type: ignore
# from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau # type: ignore
# import os
# import numpy as np
# import json

# # Configuration
# IMG_SIZE = 224
# BATCH_SIZE = 32
# EPOCHS = 50
# NUM_CLASSES = 38

# # Dataset path (download PlantVillage dataset first)
# DATASET_PATH = 'plant_disease_dataset'  # Update with your dataset path
# MODEL_SAVE_PATH = 'smartcare/ml_model/plant_disease_model.h5'
# CLASS_NAMES_PATH = 'smartcare/ml_model/class_names.json'

# # Class names for PlantVillage dataset
# CLASS_NAMES = [
#     'Apple___Apple_scab',
#     'Apple___Black_rot',
#     'Apple___Cedar_apple_rust',
#     'Apple___healthy',
#     'Blueberry___healthy',
#     'Cherry_(including_sour)___Powdery_mildew',
#     'Cherry_(including_sour)___healthy',
#     'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
#     'Corn_(maize)___Common_rust_',
#     'Corn_(maize)___Northern_Leaf_Blight',
#     'Corn_(maize)___healthy',
#     'Grape___Black_rot',
#     'Grape___Esca_(Black_Measles)',
#     'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
#     'Grape___healthy',
#     'Orange___Haunglongbing_(Citrus_greening)',
#     'Peach___Bacterial_spot',
#     'Peach___healthy',
#     'Pepper,_bell___Bacterial_spot',
#     'Pepper,_bell___healthy',
#     'Potato___Early_blight',
#     'Potato___Late_blight',
#     'Potato___healthy',
#     'Raspberry___healthy',
#     'Soybean___healthy',
#     'Squash___Powdery_mildew',
#     'Strawberry___Leaf_scorch',
#     'Strawberry___healthy',
#     'Tomato___Bacterial_spot',
#     'Tomato___Early_blight',
#     'Tomato___Late_blight',
#     'Tomato___Leaf_Mold',
#     'Tomato___Septoria_leaf_spot',
#     'Tomato___Spider_mites Two-spotted_spider_mite',
#     'Tomato___Target_Spot',
#     'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
#     'Tomato___Tomato_mosaic_virus',
#     'Tomato___healthy'
# ]


# def create_model():
#     """Create CNN model using MobileNetV2 with transfer learning"""
    
#     # Load pre-trained MobileNetV2
#     base_model = MobileNetV2(
#         input_shape=(IMG_SIZE, IMG_SIZE, 3),
#         include_top=False,
#         weights='imagenet'
#     )
    
#     # Freeze base model layers
#     base_model.trainable = False
    
#     # Create model
#     model = keras.Sequential([
#         base_model,
#         layers.GlobalAveragePooling2D(),
#         layers.BatchNormalization(),
#         layers.Dropout(0.5),
#         layers.Dense(512, activation='relu'),
#         layers.BatchNormalization(),
#         layers.Dropout(0.3),
#         layers.Dense(256, activation='relu'),
#         layers.BatchNormalization(),
#         layers.Dropout(0.2),
#         layers.Dense(NUM_CLASSES, activation='softmax')
#     ])
    
#     # Compile model
#     model.compile(
#         optimizer=keras.optimizers.Adam(learning_rate=0.001),
#         loss='categorical_crossentropy',
#         metrics=['accuracy', keras.metrics.TopKCategoricalAccuracy(k=3, name='top_3_accuracy')]
#     )
    
#     return model


# def prepare_data():
#     """Prepare data generators with augmentation"""
    
#     # Data augmentation for training
#     train_datagen = ImageDataGenerator(
#         rescale=1./255,
#         rotation_range=30,
#         width_shift_range=0.2,
#         height_shift_range=0.2,
#         shear_range=0.2,
#         zoom_range=0.2,
#         horizontal_flip=True,
#         vertical_flip=True,
#         fill_mode='nearest',
#         validation_split=0.2
#     )
    
#     # Only rescaling for validation
#     val_datagen = ImageDataGenerator(
#         rescale=1./255,
#         validation_split=0.2
#     )
    
#     # Create generators
#     train_generator = train_datagen.flow_from_directory(
#         DATASET_PATH,
#         target_size=(IMG_SIZE, IMG_SIZE),
#         batch_size=BATCH_SIZE,
#         class_mode='categorical',
#         subset='training',
#         shuffle=True
#     )
    
#     validation_generator = val_datagen.flow_from_directory(
#         DATASET_PATH,
#         target_size=(IMG_SIZE, IMG_SIZE),
#         batch_size=BATCH_SIZE,
#         class_mode='categorical',
#         subset='validation',
#         shuffle=False
#     )
    
#     return train_generator, validation_generator


# def train_model():
#     """Train the model"""
    
#     print("Creating model...")
#     model = create_model()
#     model.summary()
    
#     print("\nPreparing data...")
#     train_gen, val_gen = prepare_data()
    
#     print(f"\nTraining samples: {train_gen.samples}")
#     print(f"Validation samples: {val_gen.samples}")
#     print(f"Classes: {NUM_CLASSES}")
    
#     # Callbacks
#     callbacks = [
#         ModelCheckpoint(
#             MODEL_SAVE_PATH,
#             monitor='val_accuracy',
#             save_best_only=True,
#             mode='max',
#             verbose=1
#         ),
#         EarlyStopping(
#             monitor='val_loss',
#             patience=10,
#             restore_best_weights=True,
#             verbose=1
#         ),
#         ReduceLROnPlateau(
#             monitor='val_loss',
#             factor=0.5,
#             patience=5,
#             min_lr=1e-7,
#             verbose=1
#         )
#     ]
    
#     # Train model
#     print("\nStarting training...")
#     history = model.fit(
#         train_gen,
#         validation_data=val_gen,
#         epochs=EPOCHS,
#         callbacks=callbacks,
#         verbose=1
#     )
    
#     # Save class names
#     with open(CLASS_NAMES_PATH, 'w') as f:
#         json.dump(CLASS_NAMES, f)
    
#     print(f"\nModel saved to: {MODEL_SAVE_PATH}")
#     print(f"Class names saved to: {CLASS_NAMES_PATH}")
    
#     # Final evaluation
#     print("\nFinal evaluation:")
#     val_loss, val_acc, val_top3 = model.evaluate(val_gen)
#     print(f"Validation Loss: {val_loss:.4f}")
#     print(f"Validation Accuracy: {val_acc:.4f}")
#     print(f"Top-3 Accuracy: {val_top3:.4f}")
    
#     return model, history


# def fine_tune_model(model, train_gen, val_gen):
#     """Fine-tune the model by unfreezing some layers"""
    
#     print("\nFine-tuning model...")
    
#     # Unfreeze the last 30 layers of base model
#     base_model = model.layers[0]
#     base_model.trainable = True
    
#     for layer in base_model.layers[:-30]:
#         layer.trainable = False
    
#     # Recompile with lower learning rate
#     model.compile(
#         optimizer=keras.optimizers.Adam(learning_rate=1e-5),
#         loss='categorical_crossentropy',
#         metrics=['accuracy', keras.metrics.TopKCategoricalAccuracy(k=3)]
#     )
    
#     # Train again
#     callbacks = [
#         ModelCheckpoint(
#             MODEL_SAVE_PATH.replace('.h5', '_finetuned.h5'),
#             monitor='val_accuracy',
#             save_best_only=True,
#             mode='max'
#         ),
#         EarlyStopping(
#             monitor='val_loss',
#             patience=7,
#             restore_best_weights=True
#         )
#     ]
    
#     history_fine = model.fit(
#         train_gen,
#         validation_data=val_gen,
#         epochs=20,
#         callbacks=callbacks
#     )
    
#     return model, history_fine


# if __name__ == "__main__":
#     print("=" * 50)
#     print("Plant Disease Detection Model Training")
#     print("=" * 50)
    
#     # Create necessary directories
#     os.makedirs('smartcare/ml_model', exist_ok=True)
    
#     # Train model
#     model, history = train_model()
    
#     # Optional: Fine-tune
#     fine_tune = input("\nDo you want to fine-tune the model? (y/n): ")
#     if fine_tune.lower() == 'y':
#         train_gen, val_gen = prepare_data()
#         model, history_fine = fine_tune_model(model, train_gen, val_gen)
    
#     print("\nTraining complete!")
#     print(f"Model saved at: {MODEL_SAVE_PATH}")
#     print("\nYou can now use this model in your Django application.")