# Soal 2: Analisis Retensi "Irama Kita"

## 📋 Deskripsi

Menganalisis data pelanggan layanan streaming musik untuk menghitung metrik retensi (Churn Rate & Retention Rate) dan melakukan Cohort Analysis.

## 🎯 Tugas

1. **Hitung Churn Rate** untuk bulan April dan Juni 2025
2. **Hitung Retention Rate** untuk bulan Mei dan Juli 2025
3. **Lakukan Cohort Analysis** untuk identifikasi bulan dengan retensi terbaik/terburuk

## 🚀 Cara Menjalankan

### Terminal Visualization (Quick View)

```bash
python terminal_view.py
```

Akan menampilkan:
- Tabel perhitungan Churn & Retention Rate
- Visualisasi trend pelanggan di terminal
- Hasil Cohort Analysis

### Jupyter Notebook (Detailed Analysis)

```bash
jupyter notebook analysis.ipynb
```

Berisi analisis lengkap dengan:
- Perhitungan step-by-step
- Visualisasi interaktif
- Cohort matrix
- Interpretasi hasil

## 📊 Data

File: `data_subscribers.csv`

**Kolom:**
- Bulan
- Total_Pelanggan_Aktif (akhir bulan)
- Pelanggan_Baru (akuisisi bulan ini)

## 📐 Rumus

### Churn Rate
```
Churn Rate = (Pelanggan Bulan Lalu - (Pelanggan Bulan Ini - Pelanggan Baru)) / Pelanggan Bulan Lalu × 100%
```

### Retention Rate
```
Retention Rate = 100% - Churn Rate
```

## 💡 Expected Output

- **Churn Rate April**: ~4.17%
- **Churn Rate Juni**: ~3.57%
- **Retention Rate Mei**: ~96.30%
- **Retention Rate Juli**: ~96.77%
- **Bulan Terbaik**: Juli (retensi tertinggi)
- **Bulan Terburuk**: April (churn tertinggi)

## 📈 Rubrik Penilaian

- Perhitungan Churn Rate: 25 poin
- Perhitungan Retention Rate: 25 poin
- Cohort Analysis: 30 poin
- Interpretasi & Rekomendasi: 20 poin

**Total: 100 poin**

