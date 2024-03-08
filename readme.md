# Impact-Based Testing for Qt C++ Projects

## Requirements

1. Squish COCO v
2. QT Source codes
3. Git Bash
4. Python 3.11.5
5. CMD
6. MingW v
7. Chocolatey v

## Setup Steps

### 1. Install Squish COCO, Git, Python
### 2. Build QT Source Codes
   - Navigate to the QT source code folder, open CMD, and run the following command:
     ```bash
     make
     ```

### 3. Start Squish Server
   - In CMD, run the following commands:
     ```bash
     cd Squish for Qt X.X.X\bin 
     squishserver.exe # Run Squish server
     ```

### 4. Clone Repository and Set Up Tests
   - Open another CMD and run the following commands:
     ```bash
     git clone https://github.com/gowthamhegade/impact_qt_test.git # Clone impact_qt_test repo
     cd impact_qt_test
     ```
   - Copy the QT code folder inside the cloned repo.
   - Copy the `testsuite` folder inside the QT code folder.

### 5. Install Dependencies and Run Application
   - In the second CMD, run the following commands:
     ```bash
     pip install -r requirements.txt
     streamlit run app.py
     ```
