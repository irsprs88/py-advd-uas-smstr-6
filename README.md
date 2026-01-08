# UAS Analitik dan Visualisasi Data - Semester 6

**Mata Kuliah**: 412563403 - Analitik dan Visualisasi Data  
**Dosen**: M. Iqbal Habibie, S.Kom, MT, Ph.D  
**Tanggal**: 8 Januari 2025

## 📋 Struktur Project

```
UAS-advd-smst-6/
├── requirements.txt                  # Dependencies Python
├── README.md                         # File ini
├── soal_1_ecommerce_analysis/       # Soal 1: Analisis E-commerce
│   ├── data_ecommerce.csv           # Data transaksi
│   ├── analysis.ipynb               # Jupyter notebook analisis
│   ├── terminal_view.py             # Visualisasi di terminal
│   └── README.md                    # Panduan soal 1
├── soal_2_retention_analysis/       # Soal 2: Analisis Retensi
│   ├── data_subscribers.csv         # Data pelanggan
│   ├── analysis.ipynb               # Jupyter notebook analisis
│   ├── terminal_view.py             # Visualisasi di terminal
│   └── README.md                    # Panduan soal 2
├── soal_3_shiny_dashboard/          # Soal 3: Dashboard Interaktif
│   ├── app.py                       # Shiny app
│   ├── data_sales.csv               # Data penjualan Q4
│   └── README.md                    # Panduan soal 3
```

## 🚀 Cara Instalasi

### 1. Setup Virtual Environment (Recommended)

```bash
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Untuk macOS/Linux:
source venv/bin/activate
# Untuk Windows:
# venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 📊 Cara Menjalankan

### Soal 1: E-commerce Analysis

```bash
# Lihat visualisasi di terminal
cd soal_1_ecommerce_analysis
python terminal_view.py

# Atau buka Jupyter notebook untuk analisis detail
jupyter notebook analysis.ipynb
```

### Soal 2: Retention Analysis

```bash
# Lihat visualisasi di terminal
cd soal_2_retention_analysis
python terminal_view.py

# Atau buka Jupyter notebook untuk analisis detail
jupyter notebook analysis.ipynb
```

### Soal 3: Shiny Dashboard

```bash
cd soal_3_shiny_dashboard
shiny run app.py --reload
```

Buka browser ke: `http://localhost:8000`

## 📝 Ringkasan Soal

### Soal 1 (25%): Analisis Faktor Revenue E-commerce
- Identifikasi 2 faktor non-temporal yang dominan
- Perhitungan statistik (rata-rata, korelasi)
- Visualisasi untuk validasi

### Soal 2 (25%): Analisis Retensi Pelanggan
- Hitung Churn Rate & Retention Rate
- Cohort Analysis
- Identifikasi bulan dengan retensi terbaik/terburuk

### Soal 3 (25%): Dashboard Interaktif
- Filter lokasi (checkbox)
- Pilih metrik (radio button)
- Grouped bar chart
- Analisis margin Jakarta

### Soal 4 (25%): Presentasi & Laporan
- Script presentasi video
- Template laporand
- Hashtags YouTube

## 🎥 Video Presentation Requirementsc

Video harus di-upload ke YouTube dengan hashtags:
- #TeknikInformatikaUNDIRA
- #SemangatBerkarya
- #NetworkEngineering
- #SoftwareEngineering
- #UNDIRABersinergi
- #InformatikaUntukBangsa
- #ExploreInnovasiDigital
- #MahasiswaProduktif
- #GenerasiTeknologi
- #FutureTechLeaders
- #KolaborasiTeknikInformatika
- #TeknologiUntukMasaDepan
- #GrowWithUNDIRA
- #DigitalTransformationHeroes

## 👨‍💻 Author

**Nama Mahasiswa**: Irsyad
**NIM**: 411222059

