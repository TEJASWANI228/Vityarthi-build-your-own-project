# Breast Cancer Survival Prediction

This model helps estimate a breast cancer patient’s survival likelihood to support better monitoring, clinical decision-making, and research.

---

## 📌 Table of Contents

- [Features](#features)  
- [Technologies / Tools Used](#technologies--tools-used)  
- [Steps to Install & Run the Project](#steps-to-install--run-the-project)  
- [Instructions for Testing the Model](#instructions-for-testing-the-model)  
- [Screenshots](#screenshots)  
- [Submission](#submission)

---

# Features  
<details>  
<summary><strong>Click to Expand Features</strong></summary><br>

### 1. Predicts Patient Survival  
Predicts whether a breast cancer patient is more likely to survive (Alive) or be at high risk (Dead) based on clinical and demographic features.

### 2. Uses a Machine Learning Classifier  
- Logistic Regression model for binary classification (Alive / Dead).  
- Trained on a real breast cancer dataset.

### 3. Handles Categorical Data Automatically  
Uses label encoding to convert text-based clinical features such as:  
- Race  
- Marital Status  
- Tumor Stage (T Stage, N Stage, 6th Stage)  
- Hormone receptor status (Estrogen / Progesterone Status)

### 4. Learns From Realistic Clinical Dataset  
Embedded CSV includes breast cancer records with features like:  
- Age  
- Race  
- Marital Status (Married / Single / Divorced / Widowed etc.)  
- Tumor stages (T, N, 6th Stage)  
- Tumor differentiation and Grade  
- Tumor Size  
- Estrogen & Progesterone Status  
- Lymph node information  
- Survival Months  
- Final Status (Alive / Dead – prediction target)

### 5. Train–Test Split for Fair Evaluation  
Uses `train_test_split` to separate training and testing data, reducing overfitting and enabling unbiased evaluation.

### 6. Predicts New Patient Outcome  
GUI accepts new patient details and instantly predicts:  
- Likely to recover / survive, or  
- High-risk (not likely to survive).

### 7. Input Validation  
- Checks numeric ranges (e.g., valid age, tumor size range).  
- Ensures no empty fields.  
- Ensures categorical values match the training dataset (via dropdowns).

### 8. GUI-Based Clinical Tool  
- Built with Tkinter.  
- Scrollable form for all features.  
- Predict button fixed at the bottom so it is always visible, even when resizing.

### 9. Patient-Friendly Interpretation  
Prediction message is written in clear language so non-technical users (patients, families) can understand the result.

### 10. Supports Real-World Use Cases  
Useful for:  
- Doctors and oncologists (as a decision-support aid).  
- Hospitals and clinics for demo / teaching.  
- Students and researchers learning medical ML and GUI development.

</details>

---

# Technologies / Tools Used  
<details>  
<summary><strong>Click to Expand Technologies Used</strong></summary><br>

### 1. Programming Language  
- Python 3

### 2. Machine Learning (Scikit-Learn)  
- Logistic Regression (binary classification)  
- LabelEncoder  
- Train-test split

### 3. Data Handling (Pandas & NumPy)  
- CSV data loading from embedded string  
- Data cleaning and preprocessing  
- Categorical and numerical feature processing

### 4. GUI Framework (Tkinter)  
- Labels, Entry fields, OptionMenus (dropdowns)  
- Scrollable frames, Message boxes

### 5. Development Environment  
- Jupyter Notebook / local Python IDE  
- Stand-alone `.py` script, no external CSV file needed

### 6. Documentation & Assets  
- README documentation  
- Screenshots of the GUI

### 7. ML Model  
- Logistic Regression model trained on embedded breast cancer survival dataset

### 8. Supporting Utilities  
- Label encoding  
- Input validation and range checking  

</details>

---

# Steps to Install & Run the Project  
<details>  
<summary><strong>Click to Expand Setup Steps</strong></summary><br>

### 1. Install Python 3  
Install Python 3 from the official website.

### 2. Install Required Libraries  
Run:  


### 3. Download the Project File  
Download the Python script file (e.g., `Breast_Cancer_Survival_GUI.py`).

### 4. Run the Project  
In your terminal or command prompt, run:  


### 5. Use the App  
Enter patient data and click “Predict Recovery & Cancer Status”.

</details>  

---

# Instructions for Testing the Model  
<details>  
<summary><strong>Click to Expand Instructions</strong></summary><br>

### 1. Run the Program  
Open the application window.

### 2. Read the Feature Descriptions  
Description of each clinical feature is shown at the top.

### 3. Enter Patient Data  
Use dropdowns for categorical fields and numeric entries for continuous data.

### 4. Get Prediction  
Click the button to see the estimated survival likelihood.

</details>

---

# Screenshots  
<details>  
<summary><strong>Click to Expand Screenshots</strong></summary><br>
<img width="1440" height="900" alt="Screenshot 2025-11-25 at 3 19 08 AM" src="https://github.com/user-attachments/assets/7a716031-323c-4bc8-b018-2af9b12f7d9e" />
<img width="1440" height="900" alt="Screenshot 2025-11-25 at 3 19 33 AM" src="https://github.com/user-attachments/assets/a5f0fdba-745b-4bf9-89c7-24077fb706ad" />
<img width="1440" height="900" alt="Screenshot 2025-11-25 at 3 19 52 AM" src="https://github.com/user-attachments/assets/6d301716-8184-4f3a-a5f6-139d25b82de9" />



</details>

---

### Submission  
VITYARTHI PROJECT  
BREAST CANCER SURVIVAL PREDICTION  
DONE BY Tejaswani yadav

---

