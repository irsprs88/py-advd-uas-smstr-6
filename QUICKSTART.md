# 🚀 QUICK START GUIDE

Panduan cepat untuk menjalankan project UAS Analitik dan Visualisasi Data

---

## ⚡ Setup Cepat (5 Menit)

### 1. Install Dependencies

```bash
# Pastikan Anda berada di root directory project
cd /Users/icadic88/repository/UNDIRA/UAS-advd-smst-6

# Install semua dependencies
pip install -r requirements.txt
```

### 2. Verifikasi Installation

```bash
# Test Python dan libraries
python -c "import pandas, plotext, shiny; print('✅ All libraries installed!')"
```

---

## 📊 Menjalankan Project

### SOAL 1: E-commerce Analysis

#### Option A: Terminal Visualization (QUICK)

```bash
cd soal_1_ecommerce_analysis
python terminal_view.py
```

**Output**: ASCII charts langsung di terminal! 🎨

#### Option B: Jupyter Notebook (DETAILED)

```bash
cd soal_1_ecommerce_analysis
jupyter notebook analysis.ipynb
```

Kemudian run semua cells dengan `Cell > Run All`

---

### SOAL 2: Retention Analysis

#### Option A: Terminal Visualization (QUICK)

```bash
cd soal_2_retention_analysis
python terminal_view.py
```

#### Option B: Jupyter Notebook (DETAILED)

```bash
cd soal_2_retention_analysis
jupyter notebook analysis.ipynb
```

---

### SOAL 3: Shiny Dashboard

```bash
cd soal_3_shiny_dashboard
shiny run app.py --reload
```

**Buka browser**: http://localhost:8000

**Tips**:
- Pilih lokasi dengan checkbox ✅
- Toggle metrik dengan radio button 🔘
- Chart akan auto-update! ⚡

**Stop server**: Tekan `Ctrl + C` di terminal

---
### 1. Record Video

**Tools Recommended**:
- **macOS**: QuickTime Player (free) atau ScreenFlow
- **Windows**: OBS Studio (free)
- **Online**: Loom

**Format**:
- Resolution: 1080p minimal
- Duration: 10-15 menit
- Audio: Clear & jelas

### 2. Upload ke YouTube

1. Login dengan email UNDIRA
2. Upload video
3. Copy template dari `youtube_description.txt`
4. Paste & edit sesuai info Anda
5. Set visibility: **Public**
6. Copy link video

### 3. Update Report

```bash
# Edit report_template.md
# Isi semua bagian [ISI ...] dengan info Anda
# Terutama link YouTube video!
```

---

## 🔍 Troubleshooting

### Error: "Module not found"

```bash
# Re-install dependencies
pip install -r requirements.txt --upgrade
```

### Error: "Permission denied" saat run Python

```bash
# Tambahkan execute permission
chmod +x soal_1_ecommerce_analysis/terminal_view.py
chmod +x soal_2_retention_analysis/terminal_view.py
```

### Jupyter tidak bisa import module

```bash
# Install ipykernel
pip install ipykernel
python -m ipykernel install --user --name=venv
```

### Shiny app tidak bisa jalan

```bash
# Check shiny version
pip show shiny

# Re-install jika perlu
pip install --upgrade shiny
```

### Visualisasi folder tidak ada

```bash
# Create visualizations folders
mkdir -p soal_1_ecommerce_analysis/visualizations
mkdir -p soal_2_retention_analysis/visualizations
```

---

## 📝 Checklist Before Submission

### ✅ Technical Checklist

- [ ] Semua dependencies terinstall
- [ ] Soal 1 terminal_view.py berjalan tanpa error
- [ ] Soal 1 Jupyter notebook run completely
- [ ] Soal 2 terminal_view.py berjalan tanpa error
- [ ] Soal 2 Jupyter notebook run completely
- [ ] Soal 3 Shiny app bisa dibuka di browser
- [ ] Soal 3 semua filters berfungsi
- [ ] Visualizations tersimpan di folder masing-masing

### ✅ Presentation Checklist

- [ ] Video terekam dengan kualitas baik
- [ ] Audio jelas & tidak ada noise
- [ ] Semua soal dijelaskan
- [ ] Demo berjalan smooth
- [ ] Duration 10-15 menit
- [ ] Upload ke YouTube channel UNDIRA email
- [ ] Set visibility: Public
- [ ] Description lengkap dengan semua hashtags
- [ ] Link video sudah dicopy

### ✅ Documentation Checklist

- [ ] Laporan template sudah diisi lengkap
- [ ] Nama & NIM sudah diisi
- [ ] Link YouTube sudah dimasukkan
- [ ] Screenshot dashboard disertakan
- [ ] Semua perhitungan dijelaskan
- [ ] Insight & rekomendasi ditulis

## 🎓 Good Luck!

You got this! Project ini sudah lengkap dan siap dijalankan. 

Tinggal:
1. ✅ Install dependencies
2. ✅ Run & test semua components
3. ✅ Record video presentasi
4. ✅ Complete laporan
5. ✅ Submit!

**Remember**: Quality > Speed. Take your time to understand the analysis!

---

**© 2025 - Teknik Informatika UNDIRA**

**Last Updated**: January 8, 2025

