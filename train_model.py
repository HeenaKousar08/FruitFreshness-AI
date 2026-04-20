import os
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

# Configuration
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
DATASET_DIR = 'dataset'
MODEL_NAME = "freshness_model.h5"

def train():
    if not os.path.exists(DATASET_DIR):
        print(f"ERROR: '{DATASET_DIR}' directory not found. Please create it and add 'Fresh', 'Ripe', 'Rotten' folders.")
        return

    # Data Augmentation
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=0.2,
        rotation_range=30,
        width_shift_range=0.2,
        height_shift_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    print("Loading Training Data...")
    try:
        train_data = train_datagen.flow_from_directory(
            DATASET_DIR,
            target_size=IMG_SIZE,
            batch_size=BATCH_SIZE,
            class_mode='categorical',
            subset='training'
        )

        val_data = train_datagen.flow_from_directory(
            DATASET_DIR,
            target_size=IMG_SIZE,
            batch_size=BATCH_SIZE,
            class_mode='categorical',
            subset='validation'
        )
    except Exception as e:
        print(f"Error loading data: {e}")
        print("Make sure you have images in dataset/Fresh, dataset/Ripe, and dataset/Rotten")
        return

    # Load MobileNetV2
    base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    for layer in base_model.layers:
        layer.trainable = False

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.3)(x)
    predictions = Dense(3, activation='softmax')(x)

    model = Model(inputs=base_model.input, outputs=predictions)

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    checkpoint = ModelCheckpoint(MODEL_NAME, monitor='val_accuracy', save_best_only=True, verbose=1)
    early_stop = EarlyStopping(monitor='val_loss', patience=3, verbose=1)

    print("Starting Training...")
    history = model.fit(
        train_data,
        validation_data=val_data,
        epochs=10,
        callbacks=[checkpoint, early_stop]
    )

    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.legend()
    plt.title('Training Results')
    plt.savefig('training_plot.png')
    print(f"Training Complete. Model saved as {MODEL_NAME}")

if __name__ == '__main__':
    train()
