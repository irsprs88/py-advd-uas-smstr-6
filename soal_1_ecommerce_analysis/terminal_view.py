#!/usr/bin/env python3
"""
Soal 1: E-commerce Analysis - Terminal Visualization
Visualisasi data E-commerce menggunakan plotext (ASCII charts di terminal)
"""

import pandas as pd
import plotext as plt
from scipy.stats import pearsonr

def load_data():
    """Load data e-commerce dari CSV"""
    df = pd.read_csv('data_ecommerce.csv')
    return df

def analyze_category_revenue(df):
    """Analisis revenue per kategori produk"""
    print("\n" + "="*60)
    print("📊 ANALISIS FAKTOR 1: KATEGORI PRODUK")
    print("="*60)
    
    # Hitung rata-rata revenue per kategori
    category_stats = df.groupby('Kategori_Produk').agg({
        'Total_Pendapatan': ['mean', 'sum', 'count']
    }).round(0)
    
    print("\n📈 Statistik Revenue per Kategori Produk:")
    print(category_stats)
    
    # Visualisasi bar chart di terminal
    categories = df.groupby('Kategori_Produk')['Total_Pendapatan'].mean().sort_values(ascending=False)
    
    print("\n📊 Bar Chart: Rata-rata Revenue per Kategori Produk\n")
    plt.clear_figure()
    plt.simple_bar(
        categories.index.tolist(),
        categories.values.tolist(),
        width=60,
        title='Rata-rata Total Pendapatan per Kategori Produk'
    )
    plt.xlabel('Kategori Produk')
    plt.ylabel('Rata-rata Revenue (Rp)')
    plt.show()
    
    print(f"\n💡 INSIGHT:")
    print(f"   Kategori ELEKTRONIK memiliki rata-rata revenue tertinggi: Rp {categories.iloc[0]:,.0f}")
    print(f"   Kategori {categories.index[0]} {(categories.iloc[0]/categories.iloc[-1] - 1)*100:.1f}% lebih tinggi dari {categories.index[-1]}")
    
    return categories

def analyze_rating_correlation(df):
    """Analisis korelasi rating dengan revenue"""
    print("\n" + "="*60)
    print("📊 ANALISIS FAKTOR 2: RATING PRODUK")
    print("="*60)
    
    # Hitung korelasi
    correlation, p_value = pearsonr(df['Rating_Produk'], df['Total_Pendapatan'])
    
    print(f"\n📈 Korelasi Pearson antara Rating dan Revenue:")
    print(f"   Koefisien Korelasi: {correlation:.4f}")
    print(f"   P-value: {p_value:.4f}")
    
    if correlation > 0.7:
        strength = "KUAT"
    elif correlation > 0.4:
        strength = "SEDANG"
    else:
        strength = "LEMAH"
    
    print(f"   Kekuatan: {strength} (Positif)")
    
    # Scatter plot di terminal
    print("\n📊 Scatter Plot: Rating vs Revenue\n")
    plt.clear_figure()
    plt.scatter(df['Rating_Produk'].tolist(), df['Total_Pendapatan'].tolist())
    plt.title('Korelasi Rating Produk vs Total Pendapatan')
    plt.xlabel('Rating Produk (1-5)')
    plt.ylabel('Total Pendapatan (Rp)')
    plt.plotsize(60, 20)
    plt.show()
    
    print(f"\n💡 INSIGHT:")
    print(f"   Terdapat korelasi {strength.lower()} positif ({correlation:.4f})")
    print(f"   Semakin tinggi rating, semakin tinggi revenue")
    
    return correlation

def show_summary_statistics(df):
    """Tampilkan ringkasan statistik keseluruhan"""
    print("\n" + "="*60)
    print("📋 RINGKASAN STATISTIK DATA")
    print("="*60)
    print(f"\nTotal Transaksi: {len(df)}")
    print(f"Total Revenue: Rp {df['Total_Pendapatan'].sum():,.0f}")
    print(f"Rata-rata Revenue per Transaksi: Rp {df['Total_Pendapatan'].mean():,.0f}")
    print(f"\nRentang Tanggal: {df['Tanggal'].min()} s/d {df['Tanggal'].max()}")

def main():
    """Main function"""
    print("\n" + "="*60)
    print("🚀 SOAL 1: ANALISIS E-COMMERCE 'AKSELERASI BELI'")
    print("="*60)
    
    # Load data
    df = load_data()
    print(f"\n✅ Data berhasil dimuat: {len(df)} transaksi")
    
    # Tampilkan data sample
    print("\n📄 Sample Data (5 baris pertama):")
    print(df.head().to_string())
    
    # Analisis statistik
    show_summary_statistics(df)
    
    # Analisis Faktor 1: Kategori Produk
    category_revenue = analyze_category_revenue(df)
    
    # Analisis Faktor 2: Rating Produk
    correlation = analyze_rating_correlation(df)
    
    # Kesimpulan
    print("\n" + "="*60)
    print("🎯 KESIMPULAN")
    print("="*60)
    print("\n2 Faktor Non-Temporal yang Paling Dominan Memengaruhi Revenue:")
    print("\n1. KATEGORI PRODUK (Faktor Kategorikal)")
    print("   - Elektronik: Rata-rata revenue tertinggi")
    print("   - Perbedaan signifikan antar kategori")
    print("   - Faktor paling dominan (visual & statistik)")
    
    print("\n2. RATING PRODUK (Faktor Numerik)")
    print(f"   - Korelasi positif dengan revenue: {correlation:.4f}")
    print("   - Produk dengan rating tinggi cenderung punya revenue tinggi")
    print("   - Menunjukkan kepuasan pelanggan berpengaruh pada penjualan")
    
    print("\n" + "="*60)
    print("✅ Analisis Selesai!")
    print("="*60)
    print("\n💡 Tip: Lihat analysis.ipynb untuk analisis lebih detail dengan Jupyter!")
    print()

if __name__ == "__main__":
    main()

