import cv2
import numpy as np
import sqlite3
import os
from flask import Flask, render_template, Response, request
from tensorflow.keras.models import load_model

from logic import predict_shelf_life
from database import save_to_db, init_db

app = Flask(__name__)

# ✅ LOAD MODEL HERE (VERY IMPORTANT)
model = load_model("freshness_model.h5")

# Initialize DB
init_db()

# Load TensorFlow Model
model = load_model("freshness_model.h5")

# Classes for your model
classes = ["Fresh", "Ripe", "Rotten"]

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# 🔮 Prediction Function
def predict_image(img):
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    class_index = np.argmax(pred)

    return classes[class_index]


# 🏠 MAIN PAGE
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')

        base_price = float(request.form.get('base_price') or 0)
        cost_price = float(request.form.get('cost_price') or 0)

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            img = cv2.imread(filepath)

            # Predict freshness
            status = predict_image(img)

            # Shelf life logic
            label = "Fruit/Vegetable"
            days = predict_shelf_life(label, status)

            # Convert days safely
            try:
                days_val = int(str(days).split()[0])
            except:
                days_val = 5

            # Pricing logic
            discount = 0.20 if days_val < 3 else 0.0
            final_price = base_price * (1 - discount)
            profit_loss = final_price - cost_price

            # Save to DB
            save_to_db(label, status, days, base_price, cost_price, final_price, profit_loss)

            results = [{
                'label': label,
                'status': status,
                'days': days,
                'price': round(final_price, 2),
                'pl': round(profit_loss, 2)
            }]

            return render_template('index.html', results=results, message="Analysis Complete!")

    return render_template('index.html')


# 📷 CAMERA STREAM
def generate_frames():
    camera = cv2.VideoCapture(0)
    frame_count = 0

    while True:
        success, frame = camera.read()
        if not success:
            break

        frame_count += 1

        # Predict freshness
        status = predict_image(frame)
        label = "Live Item"
        days = predict_shelf_life(label, status)

        # Save every 60 frames
        if frame_count % 60 == 0:
            save_to_db(label, status, days, 0.0, 0.0, 0.0, 0.0)

        # Show on screen
        cv2.putText(frame, f"{status} ({days})", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# 📊 HISTORY PAGE
@app.route('/history')
def history():
    conn = sqlite3.connect('fruit_data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM scan_history ORDER BY timestamp DESC")
    data = cursor.fetchall()

    conn.close()

    return render_template('history.html', scans=data)


# 📷 CAMERA PAGE
@app.route('/camera')
def camera_page():
    return render_template('camera.html')


# 🚀 RUN
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)