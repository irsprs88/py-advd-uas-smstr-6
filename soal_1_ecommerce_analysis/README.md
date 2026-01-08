# Soal 1: Analisis E-commerce "Akselerasi Beli"

## 📋 Deskripsi

Menganalisis data transaksi E-commerce untuk mengidentifikasi faktor non-temporal yang paling dominan memengaruhi Total Pendapatan.

## 🎯 Tugas

1. **Identifikasi 2 faktor dominan** yang memengaruhi Total Pendapatan
2. **Dukung dengan perhitungan statistik** (rata-rata, korelasi)
3. **Buat visualisasi** untuk memvalidasi faktor pertama

## 🚀 Cara Menjalankan

### Terminal Visualization (Quick View)

```bash
python terminal_view.py
```

Akan menampilkan:
- Bar chart revenue per kategori (di terminal!)
- Scatter plot korelasi rating vs revenue
- Statistik deskriptif

### Jupyter Notebook (Detailed Analysis)

```bash
jupyter notebook analysis.ipynb
```

Berisi analisis lengkap dengan:
- Data exploration
- Perhitungan statistik
- Visualisasi interaktif
- Interpretasi hasil

## 📊 Data

File: `data_ecommerce.csv`

**Kolom:**
- ID_Transaksi
- Tanggal
- Kategori_Produk (Elektronik, Fesyen, Perabotan)
- Lokasi_Pengiriman (Jakarta, Surabaya, Bandung)
- Rating_Produk (1-5)
- Biaya_Promosi (Rp)
- Jumlah_Transaksi (Unit)
- Total_Pendapatan (Rp)

## 💡 Expected Output

1. **Faktor 1**: Kategori Produk (Elektronik punya revenue tertinggi)
2. **Faktor 2**: Rating Produk (Korelasi positif dengan revenue)
3. **Visualisasi**: Bar Chart atau Box Plot untuk revenue per kategori

## 📈 Rubrik Penilaian

- Identifikasi Faktor: 20 poin
- Dukungan Data/Statistik: 30 poin
- Pemilihan Visualisasi: 10 poin
- Kualitas Visualisasi & Kode: 30 poin
- Interpretasi Visual: 10 poin

**Total: 100 poin**

