#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Breast Cancer Survival Prediction GUI Application
Uses Logistic Regression to predict patient survival outcomes
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os

class BreastCancerPredictor:
    def __init__(self):
        """Initialize the predictor with model and encoders"""
        self.model = None
        self.encoders = {}
        self.feature_names = []
        self.train_model()

    def train_model(self):
        """Train the Logistic Regression model on breast cancer data"""
        # Load the dataset
        csv_path = os.path.join(os.path.dirname(__file__), 'Breast_Cancer.csv')
        df = pd.read_csv(csv_path)

        # Define feature columns (excluding target 'Status')
        self.feature_names = [col for col in df.columns if col != 'Status']

        # Separate features and target
        X = df[self.feature_names].copy()
        y = df['Status'].copy()

        # Encode categorical features
        categorical_features = ['Race', 'Marital Status', 'T Stage ', 'N Stage',
                               '6th Stage', 'differentiate', 'Grade', 'A Stage',
                               'Estrogen Status', 'Progesterone Status']

        for feature in categorical_features:
            if feature in X.columns:
                le = LabelEncoder()
                X[feature] = le.fit_transform(X[feature].astype(str))
                self.encoders[feature] = le

        # Encode target variable
        self.target_encoder = LabelEncoder()
        y_encoded = self.target_encoder.fit_transform(y)

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y_encoded, test_size=0.2, random_state=42
        )

        # Train Logistic Regression model
        self.model = LogisticRegression(max_iter=1000, random_state=42)
        self.model.fit(X_train, y_train)

        # Calculate and store accuracy
        self.accuracy = self.model.score(X_test, y_test)
        print(f"Model trained successfully! Accuracy: {self.accuracy:.2%}")

    def predict(self, input_data):
        """Make a prediction based on input data"""
        # Create DataFrame with input data
        df_input = pd.DataFrame([input_data])

        # Encode categorical features
        categorical_features = ['Race', 'Marital Status', 'T Stage ', 'N Stage',
                               '6th Stage', 'differentiate', 'Grade', 'A Stage',
                               'Estrogen Status', 'Progesterone Status']

        for feature in categorical_features:
            if feature in df_input.columns and feature in self.encoders:
                df_input[feature] = self.encoders[feature].transform(df_input[feature].astype(str))

        # Make prediction
        prediction = self.model.predict(df_input)
        prediction_proba = self.model.predict_proba(df_input)

        # Decode prediction
        result = self.target_encoder.inverse_transform(prediction)[0]
        confidence = np.max(prediction_proba) * 100

        return result, confidence

class BreastCancerGUI:
    def __init__(self, root):
        """Initialize the GUI application"""
        self.root = root
        self.root.title("Breast Cancer Survival Prediction System")
        self.root.geometry("800x700")

        # Initialize predictor
        self.predictor = BreastCancerPredictor()

        # Input variables
        self.input_vars = {}

        # Create GUI
        self.create_widgets()

    def create_widgets(self):
        """Create all GUI widgets"""
        # Main container with scrollbar
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas and scrollbar
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Title
        title_label = ttk.Label(
            scrollable_frame,
            text="Breast Cancer Survival Prediction",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=10)

        # Description
        desc_text = """This tool predicts breast cancer patient survival outcomes based on clinical and demographic features.
Please enter patient information below and click 'Predict' to get an estimated prognosis."""

        desc_label = ttk.Label(
            scrollable_frame,
            text=desc_text,
            wraplength=750,
            justify=tk.CENTER
        )
        desc_label.pack(pady=5)

        # Input form frame
        form_frame = ttk.Frame(scrollable_frame)
        form_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)

        # Define input fields with their types and options
        fields = [
            ("Age", "numeric", "40-90", None),
            ("Race", "dropdown", None, ["White", "Black", "Other", "Asian"]),
            ("Marital Status", "dropdown", None, ["Married", "Single", "Divorced", "Widowed", "Separated"]),
            ("T Stage ", "dropdown", None, ["T1", "T2", "T3", "T4"]),
            ("N Stage", "dropdown", None, ["N1", "N2", "N3"]),
            ("6th Stage", "dropdown", None, ["IIA", "IIB", "IIIA", "IIIB", "IIIC"]),
            ("differentiate", "dropdown", None, ["Poorly differentiated", "Moderately differentiated", "Well differentiated", "Undifferentiated"]),
            ("Grade", "dropdown", None, ["1", "2", "3", " anaplastic; Grade IV"]),
            ("A Stage", "dropdown", None, ["Regional", "Distant"]),
            ("Tumor Size", "numeric", "1-140", None),
            ("Estrogen Status", "dropdown", None, ["Positive", "Negative"]),
            ("Progesterone Status", "dropdown", None, ["Positive", "Negative"]),
            ("Regional Node Examined", "numeric", "1-61", None),
            ("Reginol Node Positive", "numeric", "1-46", None),
            ("Survival Months", "numeric", "1-107", None),
        ]

        # Create input fields
        row = 0
        for field_name, field_type, hint, options in fields:
            # Label
            label_text = field_name
            if hint:
                label_text += f" ({hint})"

            label = ttk.Label(form_frame, text=label_text + ":", font=("Arial", 10))
            label.grid(row=row, column=0, sticky=tk.W, pady=5, padx=5)

            # Input widget
            if field_type == "numeric":
                var = tk.StringVar()
                entry = ttk.Entry(form_frame, textvariable=var, width=30)
                entry.grid(row=row, column=1, pady=5, padx=5)
                self.input_vars[field_name] = var

            elif field_type == "dropdown":
                var = tk.StringVar()
                if options:
                    var.set(options[0])
                dropdown = ttk.Combobox(form_frame, textvariable=var, values=options,
                                       width=28, state="readonly")
                dropdown.grid(row=row, column=1, pady=5, padx=5)
                self.input_vars[field_name] = var

            row += 1

        # Button frame (fixed at bottom)
        button_frame = ttk.Frame(self.root)
        button_frame.pack(side=tk.BOTTOM, pady=10)

        # Predict button
        predict_btn = ttk.Button(
            button_frame,
            text="Predict Recovery & Cancer Status",
            command=self.make_prediction,
            style="Accent.TButton"
        )
        predict_btn.pack(pady=5)

        # Pack canvas and scrollbar
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Enable mouse wheel scrolling
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def make_prediction(self):
        """Collect input data and make prediction"""
        try:
            # Collect input data
            input_data = {}

            for field_name, var in self.input_vars.items():
                value = var.get().strip()

                # Validate non-empty
                if not value:
                    messagebox.showerror("Input Error", f"Please enter a value for {field_name}")
                    return

                # Convert numeric fields to appropriate type
                if field_name in ["Age", "Tumor Size", "Regional Node Examined",
                                 "Reginol Node Positive", "Survival Months"]:
                    try:
                        value = float(value)
                    except ValueError:
                        messagebox.showerror("Input Error", f"{field_name} must be a number")
                        return

                input_data[field_name] = value

            # Make prediction
            result, confidence = self.predictor.predict(input_data)

            # Display result
            if result == "Alive":
                message = f"✓ Prediction: Patient is likely to SURVIVE\n\n"
                message += f"Confidence: {confidence:.1f}%\n\n"
                message += "This patient shows favorable indicators for survival. "
                message += "Continue with recommended treatment and monitoring protocols."
                messagebox.showinfo("Prediction Result", message)
            else:
                message = f"⚠ Prediction: Patient is at HIGH RISK\n\n"
                message += f"Confidence: {confidence:.1f}%\n\n"
                message += "This patient shows concerning indicators. "
                message += "Recommend intensive treatment, close monitoring, and specialist consultation."
                messagebox.showwarning("Prediction Result", message)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during prediction:\n{str(e)}")

def main():
    """Main entry point for the application"""
    root = tk.Tk()
    app = BreastCancerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
