# -fabric-pattern-classifier

# 🧠 Pattern Sense: Classifying Fabric Patterns Using Deep Learning

**Pattern Sense** is a deep learning-based web application designed to classify various fabric patterns such as striped, checked, dotted, floral, and plain. This project combines a Convolutional Neural Network (CNN) model for image classification with a user-friendly Flask web interface.

---

## 👨‍💻 Team Details

* **Team ID:** LTVIP2025TMID39904
* **Team Members:**

  * M. Vaishnavi
  * Mangamuri Uma Devi
  * M. Jayasri
  * M. Vinod Naidu

**College:** G. Pullaiah College of Engineering and Technology

---

## 📌 Features

* Upload fabric images to identify their pattern type
* Uses a trained CNN model for classification
* User-friendly web interface (HTML, CSS, Flask)
* Instant classification results
* Screenshot/demo section to visualize outputs

---

## 🔍 Technologies Used

| Layer            | Technology        |
| ---------------- | ----------------- |
| Frontend         | HTML5, CSS3       |
| Backend          | Python, Flask     |
| Model Training   | TensorFlow, Keras |
| Image Processing | OpenCV, NumPy     |

---

## 🧠 Model Overview

The CNN model was trained on a dataset of fabric images representing five categories:

* **Striped**
* **Checked**
* **Dotted**
* **Floral**
* **Plain**

The model uses multiple convolutional and pooling layers followed by dense layers to output class probabilities. Accuracy was validated using a test dataset and fine-tuned for optimal performance.

---

## 🚀 How to Run the Project

### Prerequisites

Make sure the following are installed:

* Python 3.10+
* pip

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/vaishnavimalkar/fabric-pattern-classifier.git
cd fabric-pattern-classifier
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
python app.py
```

4. Open your browser and navigate to:
   `http://127.0.0.1:5000`



## 📂 Project Structure

```
fabric-pattern-classifier/
│
├── model/
│   └── fabric_model.h5           # Trained CNN model
│
├── static/
│   ├── css/
│   │   └── style.css             # Styling
│   ├── uploads/                  # Uploaded images
│   └── screenshots/              # Demo screenshots
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py                        # Main Flask application
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation



## 📈 Future Enhancements

* Add support for more pattern categories
* Improve model accuracy with a larger dataset
* Enable batch image uploads and classification
* Deploy the app on cloud platforms (e.g., Heroku, AWS)


