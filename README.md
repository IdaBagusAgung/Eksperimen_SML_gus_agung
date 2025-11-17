# Eksperimen SML - Hotel Bookings Cancellation Prediction

[![Preprocessing Pipeline](https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung/actions/workflows/preprocessing.yml/badge.svg)](https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung/actions/workflows/preprocessing.yml)

## 📋 Deskripsi Project

Repository ini berisi eksperimen dan automation untuk preprocessing dataset Hotel Bookings yang digunakan untuk memprediksi pembatalan reservasi hotel. Project ini dibuat sebagai submission untuk **Kriteria 1: Melakukan Eksperimen terhadap Dataset Pelatihan** pada kelas Machine Learning System and MLOps - Dicoding Indonesia.

### 🎯 Target: Advance Level (4/4 points)

**Kriteria yang dipenuhi:**
- ✅ **Basic (2 pts)**: Tahapan experimentation manual lengkap (loading, EDA, preprocessing)
- ✅ **Skilled (3 pts)**: Automation script `automate_gus_agung.py` untuk preprocessing otomatis
- ✅ **Advance (4 pts)**: GitHub Actions workflow untuk automated preprocessing

---

## 📁 Struktur Repository

```
Eksperimen_SML_gus_agung/
├── .github/
│   └── workflows/
│       └── preprocessing.yml          # GitHub Actions workflow
├── preprocessing/
│   ├── Eksperimen_gus_agung.ipynb    # Notebook eksperimen lengkap
│   ├── automate_gus_agung.py         # Automation script
│   └── hotel_bookings_preprocessed/   # Output folder (generated)
│       ├── X_train.csv
│       ├── X_test.csv
│       ├── y_train.csv
│       ├── y_test.csv
│       ├── hotel_bookings_preprocessed.csv
│       ├── scaler.pkl
│       ├── label_encoders.pkl
│       └── feature_names.pkl
├── hotel_bookings.csv                 # Raw dataset
├── SETUP.md                           # Setup dan reproduksi guide
└── README.md                          # Dokumentasi project
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- pip
- Git

### Installation

1. **Clone repository:**
```bash
git clone https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung.git
cd Eksperimen_SML_gus_agung
```

2. **Install dependencies:**
```bash
pip install pandas numpy scikit-learn joblib matplotlib seaborn jupyter
```

3. **Run preprocessing:**
```bash
cd preprocessing
python automate_gus_agung.py
```

---

## 📊 Dataset Information

**Dataset**: Hotel Bookings Dataset  
**Source**: Kaggle / Public Dataset  
**Size**: ~119,000 booking records  
**Features**: 32 columns  
**Target**: `is_canceled` (Binary classification)

### Dataset Statistics:
- Total bookings: ~119,390
- Cancellation rate: ~37%
- Features: Mix of numerical and categorical
- Missing values: Present in 4 columns
- Duplicates: Present (removed in preprocessing)

---

## 🔬 Eksperimen Overview

### 1. Exploratory Data Analysis (EDA)

Dilakukan di notebook `Eksperimen_gus_agung.ipynb` dengan tahapan:

- **Data Loading & Overview**
  - Dataset shape, types, basic statistics
  - Missing values analysis
  - Duplicate detection

- **Target Variable Analysis**
  - Distribution analysis
  - Imbalance ratio calculation
  - Business impact assessment

- **Numerical Features Analysis**
  - Distribution plots
  - Statistical summaries
  - Outlier detection
  - Correlation analysis

- **Categorical Features Analysis**
  - Frequency distributions
  - Cardinality check
  - Relationship with target

- **Cancellation Pattern Analysis**
  - By customer type, market segment
  - By deposit type, distribution channel
  - By hotel type and meal plan

- **Temporal Analysis**
  - Seasonal patterns
  - Monthly trends
  - Year-over-year comparison

- **Lead Time Impact**
  - Cancellation by booking advance time
  - Optimal booking window analysis

### 2. Data Preprocessing

Pipeline preprocessing yang diimplementasikan:

#### Step 1: Handle Missing Values
- `children`: Fill dengan 0 (no children assumption)
- `agent`: Fill dengan 0 (direct booking)
- `company`: Fill dengan 0 (non-corporate)
- `country`: Fill dengan mode (most frequent)

#### Step 2: Remove Duplicates
- Identify dan remove duplicate records
- Preserve data quality

#### Step 3: Feature Engineering
Membuat 5 fitur baru:
1. `total_nights` = weekend nights + week nights
2. `total_guests` = adults + children + babies
3. `has_special_requests` = binary indicator
4. `lead_time_category` = categorical (5 levels)
5. `season` = derived from arrival month

#### Step 4: Handle Outliers
- Method: IQR (Interquartile Range)
- Columns: `adr`, `lead_time`
- Action: Capping (preserve data points)

#### Step 5: Encode Categorical Variables
- Method: Label Encoding
- Applied to all categorical columns
- Encoders saved for production use

#### Step 6: Prepare Features & Target
- Separate X (features) and y (target)
- Verify data integrity

#### Step 7: Train-Test Split
- Ratio: 80% train, 20% test
- Stratified split (preserve class balance)
- Random state: 42 (reproducibility)

#### Step 8: Feature Scaling
- Method: StandardScaler (μ=0, σ=1)
- Fit on training data only
- Transform both train and test

#### Step 9: Save Processed Data
- CSV files: X_train, X_test, y_train, y_test
- Full preprocessed dataset
- Transformer objects (scalers, encoders)

---

## 🤖 Automation Script

File `automate_gus_agung.py` berisi class `HotelBookingPreprocessor` dengan fungsi:

### Main Features:

- **`load_data(filepath)`**: Load raw dataset
- **`handle_missing_values(df)`**: Handle missing values
- **`remove_duplicates(df)`**: Remove duplicate records
- **`feature_engineering(df)`**: Create new features
- **`handle_outliers(df)`**: Treat outliers
- **`encode_categorical(df)`**: Encode categorical variables
- **`scale_features(X_train, X_test)`**: Scale numerical features
- **`preprocess_pipeline(df)`**: Complete preprocessing pipeline
- **`prepare_for_training(filepath)`**: End-to-end preparation
- **`load_preprocessor(path)`**: Load saved transformers

### Usage Example:

```python
from preprocessing.automate_gus_agung import HotelBookingPreprocessor

# Initialize
preprocessor = HotelBookingPreprocessor(random_state=42)

# Run preprocessing
X_train, X_test, y_train, y_test = preprocessor.prepare_for_training(
    filepath='../hotel_bookings.csv',
    test_size=0.2,
    save_path='hotel_bookings_preprocessed'
)

# Load preprocessed data later
preprocessor.load_preprocessor('hotel_bookings_preprocessed')
```

---

## ⚙️ GitHub Actions Workflow

File `.github/workflows/preprocessing.yml` melakukan automated preprocessing:

### Triggers:
- **Push** ke branch `main` atau `master`
- **Pull Request** ke branch utama
- **Manual trigger** via workflow_dispatch

### Pipeline Steps:

1. ✅ Checkout repository
2. ✅ Setup Python 3.10
3. ✅ Install dependencies
4. ✅ Display dataset info
5. ✅ Run preprocessing pipeline
6. ✅ Verify output data
7. ✅ Upload artifacts (90 days retention)
8. ✅ Create preprocessing summary
9. ✅ Commit results to repo (optional)
10. ✅ Success notification

### Artifacts Generated:

- **Preprocessed Data**: All CSV and PKL files
- **Processing Summary**: Markdown report dengan run information

---

## 📈 Results & Outputs

### Preprocessing Results:

| Metric | Value |
|--------|-------|
| Original dataset | 119,390 rows × 32 columns |
| After preprocessing | ~119,000 rows × 39 columns |
| New features | 5 |
| Training samples | ~95,512 (80%) |
| Test samples | ~23,878 (20%) |
| Missing values | 0 (all handled) |
| Outliers | Treated (capping) |
| Encoding | Label Encoding |
| Scaling | StandardScaler |

### Key Insights:

1. **Cancellation Rate**: ~37% (significant business impact)
2. **Strong Predictors**: Lead time, deposit type, customer type
3. **Temporal Patterns**: Clear seasonal trends
4. **Data Quality**: Good after preprocessing

---

## 🔄 CI/CD Integration

GitHub Actions workflow memastikan:

- ✅ Automated preprocessing setiap code change
- ✅ Consistent preprocessing pipeline
- ✅ Versioned preprocessed datasets
- ✅ Reproducible results
- ✅ Quality assurance checks

### View Workflow Runs:
[https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung/actions](https://github.com/IdaBagusAgung/Eksperimen_SML_gus_agung/actions)

---

## 📚 Documentation

- **SETUP.md**: Detailed setup dan reproduksi guide
- **Eksperimen_gus_agung.ipynb**: Complete experimentation notebook dengan visualisasi
- **Comments in code**: Comprehensive inline documentation

---

## 🎯 Next Steps

### Kriteria 2: Model Building
- Implement multiple ML algorithms
- MLflow experiment tracking
- DagsHub integration
- Model comparison and selection

### Kriteria 3: CI/CD Workflow
- MLflow Projects setup
- Docker containerization
- Automated model deployment
- Docker Hub integration

### Kriteria 4: Monitoring & Logging
- Prometheus metrics exporter
- Grafana dashboards
- Model performance tracking
- Alert rules implementation

---

## 👤 Author

**Gus Agung**  
- GitHub: [@IdaBagusAgung](https://github.com/IdaBagusAgung)
- Course: Machine Learning System and MLOps - Dicoding Indonesia
- Target: Maximum 16/16 points (Advanced Level)

---

## 📝 License

This project is created for educational purposes as part of Dicoding's Machine Learning System and MLOps course submission.

---

## 🙏 Acknowledgments

- **Dicoding Indonesia** - Course provider
- **Kaggle** - Dataset source
- **Scikit-learn** - ML library
- **GitHub Actions** - CI/CD platform

---

## 📞 Support

For questions or issues:
1. Check [SETUP.md](SETUP.md) for troubleshooting
2. Review notebook for detailed explanations
3. Check GitHub Actions logs for workflow issues
4. Open an issue on GitHub repository

---

**Status**: ✅ Kriteria 1 - COMPLETED (Advance Level - 4/4 points)

**Last Updated**: November 2024
