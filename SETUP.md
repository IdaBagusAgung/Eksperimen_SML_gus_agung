# SETUP GUIDE - Kriteria 1: Eksperimen SML
**Student**: gus_agung
**Level Target**: Advanced (4 pts)

---

## 📋 Struktur Folder yang Harus Dibuat

```
Eksperimen_SML_gus_agung/
├── .github/
│   └── workflows/
│       └── preprocessing.yml
├── hotel_bookings.csv
├── preprocessing/
│   ├── Eksperimen_gus_agung.ipynb (move from Template_Eksperimen_MSML.ipynb)
│   ├── automate_gus_agung.py
│   └── hotel_bookings_preprocessed/
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_test.csv
│       ├── hotel_bookings_preprocessed.csv
│       ├── scaler.pkl
│       ├── label_encoders.pkl
│       └── feature_names.pkl
```

---

## 🎯 Requirements untuk Advanced Level

✅ **Basic Level (2 pts):**
- Data loading pada notebook
- EDA pada notebook
- Preprocessing pada notebook

✅ **Skilled Level (3 pts):**
- Semua basic terpenuhi
- File `automate_gus_agung.py` untuk preprocessing otomatis

✅ **Advanced Level (4 pts):**
- Semua skilled terpenuhi
- GitHub Actions workflow untuk preprocessing otomatis
- Automated data artifacts

---

## 🚀 Langkah-langkah Setup

### Step 1: Persiapan Repository

1. **Buat GitHub Repository Baru**
   ```powershell
   # Di terminal/command prompt
   cd "c:\Users\proda\OneDrive\Documents\Gus Agung\ACARA\ACARA AFTER LULUS\Mentor DBS 2026\SUBMISSION"
   
   # Rename folder
   Rename-Item "Experimen_SML_gus_agung" "Eksperimen_SML_gus_agung"
   
   cd Eksperimen_SML_gus_agung
   ```

2. **Initialize Git**
   ```powershell
   git init
   git branch -M main
   ```

3. **Create GitHub Repository**
   - Go to https://github.com/new
   - Repository name: `Eksperimen_SML_gus_agung`
   - Description: "Data Preprocessing Experiment for Hotel Bookings Dataset"
   - Public/Private: Your choice
   - Don't initialize with README

4. **Connect to GitHub**
   ```powershell
   git remote add origin https://github.com/gus_agung/Eksperimen_SML_gus_agung.git
   ```

---

### Step 2: Rename dan Organize Files

1. **Move Template to Preprocessing Folder**
   ```powershell
   Move-Item "Template_Eksperimen_MSML.ipynb" "preprocessing\Eksperimen_gus_agung.ipynb"
   ```

2. **Verify Structure**
   ```powershell
   tree /F
   ```

---

### Step 3: Install Dependencies

```powershell
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
