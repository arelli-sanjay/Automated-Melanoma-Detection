# Automated Melanoma Detection using Deep Learning and Convolutional Neural Networks

## Overview

The Automated Melanoma Detection system is a healthcare application that uses Artificial Intelligence to find melanoma in skin lesion images. This system uses Deep Learning and something called Convolutional Neural Networks to look at the images. It uses something called transfer learning with models that are already trained like VGG16 and EfficientNet to figure out if a skin lesion is **Benign** or **Malignant**. By doing the analysis the system helps doctors find skin cancer early so they can do something about it sooner. This also helps healthcare professionals make a diagnosis faster.

## Features

- The system uses Artificial Intelligence to detect melanoma from skin lesion images.
- You can upload pictures of skin lesions. Get an answer right away.
- The system says if a skin lesion is **Benign** or **Malignant**.
- It uses transfer learning with VGG16 and EfficientNet models.
- The system makes the pictures the right size and normalizes them.
- You get a confidence score with the answer.
- The website is easy to use.
- The system helps doctors find skin cancer by using Deep Learning.

## Tech Stack

### Programming Language
- Python

### Deep Learning
- TensorFlow
- Keras

### Computer Vision
- OpenCV
- NumPy

### Deep Learning Models
- Convolutional Neural Networks (CNN)
- VGG16
- EfficientNet
- Transfer Learning

### Dataset
- ISIC Skin Lesion Dataset
- Kaggle Skin Cancer Dataset

### Web Development
- Flask
- HTML
- CSS
- JavaScript

## How It Works

1. The system gets pictures of skin lesions from places like ISIC and Kaggle.
2. The pictures are made smaller to **224 × 224 pixels**. The colors are normalized.
3. The pictures are split into two groups, one for training and one for testing.
4. The system uses transfer learning with pretrained **VGG16** and **EfficientNet** models.
5. The Convolutional Neural Network finds things in each picture.
6. The trained model says if the lesion is **Benign** or **Malignant**.
7. The answer and confidence score are shown on the website.

## Screenshots

### Home Page

<img width="1877" height="908" alt="Screenshot 2026-07-21 232816" src="https://github.com/user-attachments/assets/b27493b9-161d-407a-9be1-672aaf28d0d9" />

### Admin Login

<img width="1871" height="897" alt="Screenshot 2026-07-21 232958" src="https://github.com/user-attachments/assets/581d31c2-e709-4cd3-b971-fc6bb2855cca" />

### Preview Page

<img width="1871" height="892" alt="Screenshot 2026-07-21 233027" src="https://github.com/user-attachments/assets/4b78695b-b34a-4a47-b3f6-ec61cdf19475" />

### Prediction Result

<img width="1847" height="907" alt="Screenshot 2026-07-21 233051" src="https://github.com/user-attachments/assets/cb61555d-f8f9-45b3-bbe7-43899a8652ac" />

### Performance Analysis Page

<img width="1846" height="896" alt="Screenshot 2026-07-21 233117" src="https://github.com/user-attachments/assets/52431ad8-e50a-431d-b06e-4bf71095d610" />

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Automated-Melanoma-Detection.git

cd Automated-Melanoma-Detection
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

## Live Demo

https://automated-melanoma-detection.onrender.com

##  Publication

This project has been published in the **International Journal of Advanced Research in Education and Technology (IJARETY)**.

**Title:** Automated Melanoma Detection using Deep Learning and Convolutional Neural Networks

**Journal:** International Journal of Advanced Research in Education and Technology (IJARETY)

**DOI:** https://doi.org/10.15680/IJARETY.2026.1303083

**Article:** https://www.ijarety.in/article/Automated-Melanoma-Detection-using-Deep-Learning-and-Convolutional-Neural-Networks-2312

## What I Learned

- I built a system that uses Deep Learning to look at medical pictures.
- I used transfer learning with pretrained VGG16 and EfficientNet models.
- I learned how to get pictures ready for Convolutional Neural Networks.
- How to test Deep Learning models using TensorFlow and Keras.
- I put the Artificial Intelligence models into a Flask web application.
- I got experience, with computer vision and healthcare Artificial Intelligence.
- I understood better how to use Artificial Intelligence to solve problems.

## Author

**ARELLI SANJAY**
- GitHub: https://github.com/arelli-sanjay
- Linkedin: https://www.linkedin.com/in/sanjay-arelli-2b0970383/

## Support
If you like Automated Melanoma Detection using Deep Learning and Convolutional Neural Networks consider giving it a star, on GitHub.
