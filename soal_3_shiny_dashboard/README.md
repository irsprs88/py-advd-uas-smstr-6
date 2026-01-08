# Soal 3: Dashboard Interaktif dengan Shiny

## 📋 Deskripsi

Membangun aplikasi dashboard interaktif menggunakan Shiny for Python untuk visualisasi data penjualan Q4 2024.

## 🎯 Tugas

1. **Sidebar Input**:
   - Checkbox Group untuk filter lokasi (Jakarta, Surabaya, Bandung)
   - Radio Button untuk memilih metrik (Total Penjualan atau Margin Keuntungan)

2. **Main Panel**:
   - Grouped Bar Chart yang menampilkan data per kategori produk
   - Chart harus responsive terhadap filter yang dipilih

3. **Analisis**:
   - Jelaskan insight perbandingan margin Elektronik vs Pakaian di Jakarta Q4

## 🚀 Cara Menjalankan

```bash
shiny run app.py --reload
```

Kemudian buka browser ke: **http://localhost:8000**

### Fitur Dashboard:

- ✅ Filter lokasi multiple selection
- ✅ Toggle antara Total Penjualan dan Margin Keuntungan
- ✅ Grouped bar chart interaktif
- ✅ Auto-refresh saat input berubah

## 📊 Data

File: `data_sales.csv`

**Kolom:**
- Kategori_Produk (Elektronik, Pakaian, Makanan)
- Lokasi (Jakarta, Surabaya, Bandung)
- Bulan (Oktober, November, Desember)
- Total_Penjualan (Rp)
- Margin_Keuntungan (%)

## 💡 Expected Insight

**Perbandingan Margin Jakarta Q4:**
- Pakaian: Margin lebih tinggi (~26.67%)
- Elektronik: Margin lebih rendah (~12%)
- **Insight**: Meskipun Elektronik punya volume penjualan lebih tinggi, Pakaian lebih profitable (margin 2x lipat)

## 📈 Rubrik Penilaian

- Fungsionalitas Input UI: 25 poin
- Implementasi Server & Data Processing: 25 poin
- Kualitas Visualisasi (Grouped Bar Chart): 30 poin
- Analisis Visual: 20 poin

**Total: 100 poin**

## 🎨 Screenshot

Dashboard akan menampilkan:
- Sidebar kiri dengan controls
- Main panel dengan grouped bar chart
- Summary statistics

