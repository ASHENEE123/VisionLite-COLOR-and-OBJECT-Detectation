# VISIONLITE

**ColorDetectation** is an educational Python project designed as a learning experiment for exploring OpenCV and its core computer vision techniques. The project provides a hands-on approach to detecting both colors and objects in images, supporting real-time webcam input and image uploads via a simple Flask web interface. Users can analyze images, see how OpenCV processes them, and download the annotated results.

---

## 🚀 Features

- **Dual Input Modes**:  
  - **Real-Time Detection**: Detects colors and objects from live webcam video.
  - **Image Upload**: Users can upload images and analyze them interactively.

- **User-Driven Analysis**:  
  - Click or select regions in images or video to identify colors and objects at those points.

- **Color & Object Detection**:  
  - Detects objects using contour detection and identifies their dominant color.
  - Annotates detected objects with color and object labels.

- **Flask Web Backend**:  
  - Simple web UI for uploading images, viewing results, and downloading annotated images.

---

## 🛠️ Techniques & Libraries Used

- **OpenCV**:  
  - Core library for computer vision tasks.
  - Handles image loading, webcam streaming, color space conversion (BGR/HSV), and drawing.

- **Thresholding**:  
  - Separates objects from the background with binary/adaptive thresholding.

- **Contours & Contour Properties**:  
  - Uses `cv2.findContours` to detect object outlines.
  - Analyzes contour properties (area, centroid) and computes mean color within contours for labeling.

- **Color Detection**:  
  - Converts pixel/region color to HSV/RGB and maps them to basic color names.

- **Flask**:  
  - Provides the backend server for image upload, processing, and result download.

- **Image Download**:  
  - Lets users download processed images with all detected objects and color annotations.

---

## 📚 Educational Purpose

> **Note:**  
> This project is a trial model created to learn and experiment with OpenCV and its core techniques. It is intended for educational use, experimentation, and as a starting point for deeper exploration into computer vision.

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ASHENEE123/ColorDetectation.git
   cd ColorDetectation
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install requirements**
   ```bash
   pip install -r requirements.txt
   ```
   Or, if `requirements.txt` is missing:
   ```bash
   pip install numpy opencv-python flask
   ```

---

## ⚡ Usage

### 1. **Run the Web Application**

```bash
python color.py
```
or
```bash
flask run
```
- Visit `http://localhost:5000` in your browser.

### 2. **Analyze Images**

- **Webcam Mode:** Analyze live video feed for object and color detection.
- **Upload Mode:** Upload images, click to analyze regions, and download results.

---

## 🌈 Example

- Upload an image or use the webcam.
- Detected objects will be outlined and labeled with their dominant colors ranges in image and object type.
- Download the processed image from the browser.

