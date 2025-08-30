# 🧮 BMI Calculator (Tkinter GUI)

A simple and user-friendly **BMI (Body Mass Index) Calculator** built with Python's Tkinter library.  
It allows users to enter their weight and height, validates the input, and displays their BMI along with a health classification.

---

## 📌 Features
- **Interactive GUI** built using Tkinter.
- **Real-time input validation** — only allows numeric values with a single decimal point.
- **Instant BMI calculation** with a simple button click.
- **Health classification** based on WHO BMI ranges:
  - Underweight
  - Healthy weight
  - Overweight
  - Obese
- **Color-coded results** for easy understanding.
- **Error handling** for missing or invalid inputs.

---

## 📷 Preview
<img width="342" height="482" alt="image" src="https://github.com/user-attachments/assets/3ee644a0-f901-45bd-b457-de3964611aae" />
<img width="342" height="482" alt="image" src="https://github.com/user-attachments/assets/21bad810-a140-4c3c-b469-5b58fe6799c0" />


---

## 📂 Installation
1. Make sure you have Python 3 installed.
2. Clone this repository:
   ```bash
   git clone https://github.com/Harsh-Pendhari/BMI-Calculator.git
    ```
3. Navigate to the project folder:
    ```bash
    cd BMI-Calculator
    ```

4. Run the script:
    ```bash
    python BMI_Calculator.py
    ```

## 🛠 How It Works

1. Enter your weight in kilograms.

2. Enter your height in centimeters.

3. Click Calculate.

4. The application will:

    - Compute your BMI using the formula:
    ```ini
        BMI = weight / (height_in_meters)^2
    ```

    - Display your BMI value.

    - Show your health classification.

## 📊 BMI Classification Table
---------------------------

| BMI Range   | Classification  | Color Indicator |
|-------------|-----------------|-----------------|
| < 18.5      | Underweight     | 🔴 Red          |
| 18.5 – 24.9 | Healthy Weight  | 🟢 Green        |
| 25 – 29.9   | Overweight      | 🟡 Yellow       |
| ≥ 30        | Obese           | 🔴 Red          |

## 💡 Example

Input:
    Weight: 70 kg
    Height: 175 cm


Output:
    Your BMI is 22.86
    You have Healthy Weight!

## 📜 License

This project is open-source and available under the MIT License.
