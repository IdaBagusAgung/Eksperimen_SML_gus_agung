# SETUP GUIDE - Kriteria 1: Eksperimen SML
**Student**: gus_agung  
**Level Target**: Advanced (4/4 pts)  
**Repository**: https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung

---

## 📋 Struktur Folder Final

```
Eksperimen_SML_gus_agung/
├── .github/
│   └── workflows/
│       └── preprocessing.yml          # GitHub Actions workflow
├── .gitignore
├── hotel_bookings.csv                 # Raw dataset
├── README.md                          # Project documentation
├── SETUP.md                           # This file
└── preprocessing/
    ├── Eksperimen_gus_agung.ipynb    # Notebook eksperimen lengkap
    ├── automate_gus_agung.py         # Automation script
    └── hotel_bookings_preprocessed/   # Output folder (generated)
        ├── X_train.csv
        ├── X_test.csv
        ├── y_train.csv
        ├── y_test.csv
        ├── hotel_bookings_preprocessed.csv
        ├── scaler.pkl
        ├── label_encoders.pkl
        └── feature_names.pkl
```

---

## 🎯 Kriteria yang Dipenuhi

### ✅ Basic Level (2 pts)
- [x] Data loading pada notebook
- [x] EDA lengkap pada notebook
- [x] Preprocessing manual pada notebook

### ✅ Skilled Level (3 pts)
- [x] Semua basic terpenuhi
- [x] File `automate_gus_agung.py` untuk preprocessing otomatis
- [x] Konversi dari eksperimen notebook ke automation script
- [x] Fungsi preprocessing yang reusable

### ✅ Advanced Level (4 pts)
- [x] Semua skilled terpenuhi
- [x] GitHub Actions workflow di `.github/workflows/preprocessing.yml`
- [x] Automated preprocessing setiap push/PR
- [x] Dataset artifacts uploaded dan versioned
- [x] Complete CI/CD integration

---

## 🚀 Quick Start - Reproduksi Project

### Prerequisites

- Python 3.10+
- pip (Python package manager)
- Git
- GitHub account

### Step 1: Clone Repository

```bash
git clone https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung.git
cd Eksperimen_SML_gus_agung
```

### Step 2: Install Dependencies

```bash
pip install pandas numpy scikit-learn joblib matplotlib seaborn jupyter
```

### Step 3: Run Automation Script

```bash
cd preprocessing
python automate_gus_agung.py
```

**Expected Output:**
```
[INFO] Loading data from ../hotel_bookings.csv
[INFO] Data loaded successfully. Shape: (119390, 32)
==================================================
Starting Preprocessing Pipeline
==================================================
[INFO] Handling missing values...
[INFO] Missing values handled. Remaining NaN: 0
[INFO] Removing duplicates...
[INFO] Removed 32013 duplicate rows
[INFO] Engineering features...
[INFO] Feature engineering completed. New shape: (87377, 37)
[INFO] Handling outliers...
[INFO] Outliers handled
[INFO] Encoding categorical variables...
[INFO] Encoded 14 categorical columns
==================================================
Preprocessing Pipeline Completed
==================================================
[INFO] Scaling features...
[SUCCESS] Processed data saved to hotel_bookings_preprocessed/
[INFO] Training set: (69901, 36)
[INFO] Test set: (17476, 36)
==================================================
Preprocessing Summary
==================================================
Total features: 36
Training samples: 69901
Test samples: 17476
Target distribution (train): {0: 50682, 1: 19219}
==================================================
```

### Step 4: Verify Output Files

```bash
ls hotel_bookings_preprocessed/
```

**Expected Files:**
- `X_train.csv` - Training features (scaled)
- `X_test.csv` - Test features (scaled)
- `y_train.csv` - Training labels
- `y_test.csv` - Test labels
- `hotel_bookings_preprocessed.csv` - Full preprocessed dataset
- `scaler.pkl` - StandardScaler object
- `label_encoders.pkl` - Label encoders dictionary
- `feature_names.pkl` - Feature names list

### Step 5: Explore Notebook

```bash
jupyter notebook Eksperimen_gus_agung.ipynb
```

---

## 📊 Dataset Information

**Dataset**: Hotel Bookings  
**Source**: Kaggle / Public Dataset  
**Original Size**: 119,390 rows × 32 columns  
**After Preprocessing**: 87,377 rows × 39 columns

### Key Statistics:
- **Cancellation Rate**: ~37%
- **Missing Values**: 4 columns (handled)
- **Duplicates**: 32,013 rows (removed)
- **New Features**: 5 engineered features
- **Train/Test Split**: 80/20

---

## 🔧 Automation Script Details

### File: `automate_gus_agung.py`

**Main Class**: `HotelBookingPreprocessor`

**Key Methods:**
1. `load_data(filepath)` - Load raw dataset
2. `handle_missing_values(df)` - Handle missing data
3. `remove_duplicates(df)` - Remove duplicate records
4. `feature_engineering(df)` - Create new features
5. `handle_outliers(df)` - Treat outliers using IQR
6. `encode_categorical(df)` - Label encoding
7. `scale_features(X_train, X_test)` - StandardScaler
8. `preprocess_pipeline(df)` - Complete pipeline
9. `prepare_for_training(filepath)` - End-to-end preparation

**Usage Example:**

```python
from automate_gus_agung import HotelBookingPreprocessor

# Initialize
preprocessor = HotelBookingPreprocessor(random_state=42)

# Run preprocessing
X_train, X_test, y_train, y_test = preprocessor.prepare_for_training(
    filepath='../hotel_bookings.csv',
    test_size=0.2,
    save_path='hotel_bookings_preprocessed'
)

# Load saved preprocessor
preprocessor.load_preprocessor('hotel_bookings_preprocessed')
```

---

## ⚙️ GitHub Actions Workflow

### File: `.github/workflows/preprocessing.yml`

**Triggers:**
- Push to `main` or `master` branch
- Pull requests to main branches
- Manual workflow dispatch
- Changes to dataset or preprocessing files

**Pipeline Steps:**

1. ✅ Checkout repository
2. ✅ Setup Python 3.10
3. ✅ Install dependencies (pandas, numpy, scikit-learn, joblib)
4. ✅ Display dataset information
5. ✅ Run `automate_gus_agung.py`
6. ✅ Verify preprocessed output
7. ✅ Upload artifacts (90 days retention)
8. ✅ Create preprocessing summary
9. ✅ Commit results back to repo (optional)
10. ✅ Success notification

**Artifacts Generated:**
- `preprocessed-hotel-bookings-run-{NUMBER}` - All CSV and PKL files
- `preprocessing-summary-run-{NUMBER}` - Processing report

**View Workflow Runs:**
https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung/actions

---

## 🧪 Testing & Verification

### Test Automation Locally

```bash
cd preprocessing
python automate_gus_agung.py
```

### Verify Output

```python
import pandas as pd

# Load preprocessed data
X_train = pd.read_csv('hotel_bookings_preprocessed/X_train.csv')
X_test = pd.read_csv('hotel_bookings_preprocessed/X_test.csv')
y_train = pd.read_csv('hotel_bookings_preprocessed/y_train.csv')
y_test = pd.read_csv('hotel_bookings_preprocessed/y_test.csv')

print(f"X_train shape: {X_train.shape}")
print(f"X_test shape: {X_test.shape}")
print(f"y_train shape: {y_train.shape}")
print(f"y_test shape: {y_test.shape}")

# Check for missing values
print(f"\nMissing values in X_train: {X_train.isnull().sum().sum()}")
print(f"Missing values in X_test: {X_test.isnull().sum().sum()}")

# Check scaling (mean should be ~0, std ~1)
print(f"\nX_train mean: {X_train.mean().mean():.6f}")
print(f"X_train std: {X_train.std().mean():.6f}")
```

### Test GitHub Actions

**Method 1: Make a Change**
```bash
# Edit README.md or add a comment
git add .
git commit -m "Test GitHub Actions workflow"
git push origin main
```

**Method 2: Manual Trigger**
1. Go to: https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung/actions
2. Click on "Automated Data Preprocessing - Hotel Bookings"
3. Click "Run workflow" button
4. Select branch and run

---

## 📝 Preprocessing Pipeline Details

### Step 1: Handle Missing Values
- `children`: Fill with 0 (assume no children)
- `agent`: Fill with 0 (direct booking)
- `company`: Fill with 0 (non-corporate)
- `country`: Fill with mode (most frequent)

### Step 2: Remove Duplicates
- Identify and remove exact duplicate rows
- Preserves data quality

### Step 3: Feature Engineering
Create 5 new features:
1. **total_nights** = weekend nights + week nights
2. **total_guests** = adults + children + babies
3. **has_special_requests** = binary (0 or 1)
4. **lead_time_category** = categorical (5 levels)
5. **season** = derived from arrival_date_month

### Step 4: Handle Outliers
- **Method**: IQR (Interquartile Range)
- **Columns**: `adr`, `lead_time`
- **Action**: Capping (not removal)
- **Formula**: 
  - Lower bound = Q1 - 1.5 × IQR
  - Upper bound = Q3 + 1.5 × IQR

### Step 5: Encode Categorical Variables
- **Method**: Label Encoding
- **Reason**: Efficient for tree-based models
- **Applied to**: All categorical columns (14 columns)
- **Saved**: Encoders saved for production use

### Step 6: Prepare Features & Target
- Separate X (features) and y (target)
- Verify data integrity
- Store feature names

### Step 7: Train-Test Split
- **Ratio**: 80% train, 20% test
- **Method**: Stratified split (preserve class balance)
- **Random State**: 42 (reproducibility)

### Step 8: Feature Scaling
- **Method**: StandardScaler
- **Formula**: z = (x - μ) / σ
- **Result**: Mean = 0, Std = 1
- **Important**: Fit only on training data (prevent data leakage)

### Step 9: Save Processed Data
- CSV files for easy access
- PKL files for transformers (scaler, encoders)
- Timestamped versions for tracking

---

## 🐛 Troubleshooting

### Issue: File not found error

**Solution:**
```bash
# Check current directory
pwd

# Ensure you're in the right folder
cd preprocessing

# Verify file exists
ls ../hotel_bookings.csv
```

### Issue: Module not found

**Solution:**
```bash
pip install pandas numpy scikit-learn joblib
```

### Issue: GitHub Actions fails

**Checklist:**
- [ ] Repository is public or Actions enabled for private
- [ ] Workflow file is in `.github/workflows/`
- [ ] YAML syntax is correct
- [ ] Dataset file exists in repository
- [ ] Python dependencies are correctly specified

**View Logs:**
Go to Actions tab → Click on failed workflow → View logs

### Issue: Permission denied when pushing

**Solution:**
```bash
# Configure Git credentials
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Re-authenticate with GitHub
# Use Personal Access Token instead of password
```

---

## 📚 Additional Resources

### Documentation
- **README.md**: Project overview and features
- **SETUP.md**: This file - setup and reproduction guide
- **Eksperimen_gus_agung.ipynb**: Detailed experimentation notebook

### Links
- Repository: https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung
- Actions: https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung/actions
- Issues: https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung/issues

### References
- Scikit-learn Documentation: https://scikit-learn.org/
- Pandas Documentation: https://pandas.pydata.org/
- GitHub Actions Docs: https://docs.github.com/en/actions

---

## ✅ Completion Checklist

### Kriteria 1 - Advanced Level

- [x] Repository created: `Eksperimen_SML_gus_agung`
- [x] Raw dataset included: `hotel_bookings.csv`
- [x] Notebook eksperimen: `preprocessing/Eksperimen_gus_agung.ipynb`
- [x] Automation script: `preprocessing/automate_gus_agung.py`
- [x] GitHub Actions workflow: `.github/workflows/preprocessing.yml`
- [x] Preprocessed data folder: `preprocessing/hotel_bookings_preprocessed/`
- [x] Documentation: `README.md` dan `SETUP.md`
- [x] Git initialized and pushed to GitHub
- [x] Workflow runs successfully
- [x] Artifacts uploaded correctly

### Verification

```bash
# 1. Repository structure
tree /F

# 2. Run automation
cd preprocessing
python automate_gus_agung.py

# 3. Check output
ls hotel_bookings_preprocessed/

# 4. GitHub Actions status
# Visit: https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung/actions
```

---

## 🎯 Next Steps

### Kriteria 2: Model Building
- Implement multiple ML algorithms
- MLflow experiment tracking
- DagsHub integration
- Model comparison

### Kriteria 3: CI/CD Workflow
- MLflow Projects setup
- Docker containerization
- Automated deployment

### Kriteria 4: Monitoring & Logging
- Prometheus integration
- Grafana dashboards
- Alert rules

---

## 👤 Author

**Gus Agung**  
- GitHub: [@IdaBagusAgung](https://github.com/IdaBagusAgung)
- Course: Machine Learning System and MLOps - Dicoding Indonesia
- Target: 16/16 points (Advanced Level all criteria)

---

## 📅 Timeline

- **Kriteria 1**: ✅ Completed - Advanced Level (4/4 pts)
- **Kriteria 2**: 🔄 In Progress
- **Kriteria 3**: ⏳ Planned
- **Kriteria 4**: ⏳ Planned

---

**Last Updated**: November 17, 2025  
**Status**: ✅ Kriteria 1 COMPLETED - Ready for Review
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install packages
pip install pandas numpy matplotlib seaborn scikit-learn joblib jupyter
```

---

### Step 4: Run Experiment Notebook

1. **Start Jupyter**
   ```powershell
   cd preprocessing
   jupyter notebook
   ```

2. **Open Eksperimen_gus_agung.ipynb**
   - Run all cells sequentially
   - Verify:
     - Data loads successfully
     - EDA visualizations appear
     - Preprocessing completes
     - Files saved to `hotel_bookings_preprocessed/`

3. **Expected Output:**
   ```
   ✓ X_train.csv
   ✓ X_test.csv
   ✓ y_train.csv
   ✓ y_test.csv
   ✓ hotel_bookings_preprocessed.csv
   ```

---

### Step 5: Test Automation Script

```powershell
cd preprocessing
python automate_gus_agung.py
```

**Expected Output:**
```
==================================================
Starting Preprocessing Pipeline
==================================================
[INFO] Loading data from ../hotel_bookings.csv
[INFO] Data loaded successfully. Shape: (119390, 32)
...
[SUCCESS] Processed data saved to hotel_bookings_preprocessed/
```

**Verify Files Created:**
- Check `hotel_bookings_preprocessed/` folder
- Confirm all CSV and PKL files exist

---

### Step 6: Setup GitHub Actions (Advanced Level)

1. **Add .gitignore**
   ```powershell
   # Create .gitignore in project root
   @"
   venv/
   __pycache__/
   *.pyc
   .ipynb_checkpoints/
   .DS_Store
   "@ | Out-File -FilePath ..\.gitignore -Encoding utf8
   ```

2. **Commit Files**
   ```powershell
   cd ..
   git add .
   git commit -m "Initial commit: Experiment notebook and automation script"
   git push -u origin main
   ```

3. **Verify GitHub Actions**
   - Go to your GitHub repo
   - Click "Actions" tab
   - Workflow should trigger automatically
   - Wait for workflow to complete (green checkmark)

4. **Check Artifacts**
   - In Actions, click on the completed workflow run
   - Scroll to "Artifacts" section
   - Download `preprocessed-data-{run_number}`
   - Verify contents

---

### Step 7: Trigger Manual Workflow

```powershell
# Make a change to trigger workflow
cd preprocessing
echo "# Updated" >> automate_gus_agung.py

git add .
git commit -m "Update preprocessing script"
git push
```

Watch Actions tab - workflow should trigger again!

---

## ✅ Kriteria Checklist

### Basic Level ✓
- [x] Data loading pada notebook
- [x] EDA dengan visualisasi
- [x] Preprocessing pada notebook
- [x] Data tersimpan

### Skilled Level ✓
- [x] File `automate_gus_agung.py` exists
- [x] Script berjalan tanpa error
- [x] Menghasilkan data yang sama dengan notebook
- [x] Preprocessing terotomatisasi

### Advanced Level ✓
- [x] `.github/workflows/preprocessing.yml` exists
- [x] Workflow trigger on push
- [x] Preprocessing berjalan di GitHub Actions
- [x] Artifacts tersimpan
- [x] Automated commit (optional)

---

## 🐛 Troubleshooting

### Issue 1: Import Error
```
ModuleNotFoundError: No module named 'pandas'
```
**Solution:**
```powershell
pip install -r requirements.txt
```

### Issue 2: File Not Found
```
FileNotFoundError: hotel_bookings.csv not found
```
**Solution:**
- Ensure you're running from correct directory
- Check relative path in script
- Verify file exists: `Test-Path hotel_bookings.csv`

### Issue 3: GitHub Actions Fails
**Solution:**
- Check workflow logs in Actions tab
- Common issues:
  - Missing dependencies in workflow
  - Wrong paths
  - Insufficient permissions

---

## 📸 Screenshots untuk Submission

Ambil screenshot berikut:

1. **Notebook Execution**: All cells run successfully
2. **Preprocessing Output**: Terminal showing successful preprocessing
3. **GitHub Actions**: Workflow completed successfully (green checkmark)
4. **Artifacts**: Downloaded artifacts from GitHub Actions
5. **Folder Structure**: Tree view showing complete structure

---

## 🎓 Tips untuk Advanced Level

1. **Test Locally First**: Always test automation script before pushing
2. **Check Workflow Logs**: If fails, read logs carefully
3. **Incremental Commits**: Commit frequently with clear messages
4. **Document Everything**: Add comments in code
5. **Verify Outputs**: Always check generated files

---

## 📚 Resources

- GitHub Actions: https://docs.github.com/en/actions
- Pandas Documentation: https://pandas.pydata.org/docs/
- Scikit-learn: https://scikit-learn.org/stable/

---

**Status**: ✅ Ready for Kriteria 1 Advanced Level Submission
**Author**: gus_agung
**Last Updated**: November 2025
