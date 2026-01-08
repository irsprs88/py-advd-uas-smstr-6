#!/usr/bin/env python3
"""
Soal 2: Retention Analysis - Terminal Visualization
Analisis Churn Rate, Retention Rate, dan Cohort Analysis untuk layanan streaming
"""

import pandas as pd
import plotext as plt

def load_data():
    """Load data subscribers dari CSV"""
    df = pd.read_csv('data_subscribers.csv')
    return df

def calculate_churn_retention(df):
    """Hitung Churn Rate dan Retention Rate"""
    print("\n" + "="*70)
    print("📊 PERHITUNGAN CHURN RATE & RETENTION RATE")
    print("="*70)
    
    # Prepare data untuk perhitungan
    df['Pelanggan_Baru'] = df['Pelanggan_Baru'].fillna(0).astype(int)
    
    results = []
    
    for i in range(1, len(df)):
        bulan = df.iloc[i]['Bulan']
        pelanggan_bulan_ini = df.iloc[i]['Total_Pelanggan_Aktif']
        pelanggan_baru = df.iloc[i]['Pelanggan_Baru']
        pelanggan_bulan_lalu = df.iloc[i-1]['Total_Pelanggan_Aktif']
        
        # Hitung pelanggan yang retained dari bulan lalu
        pelanggan_retained = pelanggan_bulan_ini - pelanggan_baru
        
        # Hitung pelanggan yang churn
        pelanggan_churn = pelanggan_bulan_lalu - pelanggan_retained
        
        # Hitung Churn Rate
        churn_rate = (pelanggan_churn / pelanggan_bulan_lalu) * 100
        
        # Hitung Retention Rate
        retention_rate = 100 - churn_rate
        
        results.append({
            'Bulan': bulan,
            'Pelanggan_Awal': pelanggan_bulan_lalu,
            'Pelanggan_Baru': pelanggan_baru,
            'Pelanggan_Akhir': pelanggan_bulan_ini,
            'Pelanggan_Retained': pelanggan_retained,
            'Pelanggan_Churn': pelanggan_churn,
            'Churn_Rate': churn_rate,
            'Retention_Rate': retention_rate
        })
    
    results_df = pd.DataFrame(results)
    
    print("\n📈 Detail Perhitungan:")
    print(results_df.to_string(index=False))
    
    return results_df

def show_specific_months(results_df):
    """Tampilkan hasil untuk bulan yang diminta"""
    print("\n" + "="*70)
    print("🎯 HASIL UNTUK BULAN YANG DIMINTA")
    print("="*70)
    
    # April 2025 - Churn Rate
    april = results_df[results_df['Bulan'].str.contains('April')].iloc[0]
    print(f"\n📌 APRIL 2025 - Churn Rate")
    print(f"   Pelanggan Bulan Lalu (Maret): {april['Pelanggan_Awal']}")
    print(f"   Pelanggan Baru April: {april['Pelanggan_Baru']}")
    print(f"   Pelanggan Retained: {april['Pelanggan_Retained']}")
    print(f"   Pelanggan Churn: {april['Pelanggan_Churn']}")
    print(f"   ➡️  CHURN RATE = {april['Churn_Rate']:.2f}%")
    
    # Juni 2025 - Churn Rate
    juni = results_df[results_df['Bulan'].str.contains('Juni')].iloc[0]
    print(f"\n📌 JUNI 2025 - Churn Rate")
    print(f"   Pelanggan Bulan Lalu (Mei): {juni['Pelanggan_Awal']}")
    print(f"   Pelanggan Baru Juni: {juni['Pelanggan_Baru']}")
    print(f"   Pelanggan Retained: {juni['Pelanggan_Retained']}")
    print(f"   Pelanggan Churn: {juni['Pelanggan_Churn']}")
    print(f"   ➡️  CHURN RATE = {juni['Churn_Rate']:.2f}%")
    
    # Mei 2025 - Retention Rate
    mei = results_df[results_df['Bulan'].str.contains('Mei')].iloc[0]
    print(f"\n📌 MEI 2025 - Retention Rate")
    print(f"   Churn Rate: {mei['Churn_Rate']:.2f}%")
    print(f"   ➡️  RETENTION RATE = {mei['Retention_Rate']:.2f}%")
    
    # Juli 2025 - Retention Rate
    juli = results_df[results_df['Bulan'].str.contains('Juli')].iloc[0]
    print(f"\n📌 JULI 2025 - Retention Rate")
    print(f"   Churn Rate: {juli['Churn_Rate']:.2f}%")
    print(f"   ➡️  RETENTION RATE = {juli['Retention_Rate']:.2f}%")

def visualize_trends(df, results_df):
    """Visualisasi trend pelanggan"""
    print("\n" + "="*70)
    print("📊 VISUALISASI TREND PELANGGAN")
    print("="*70)
    
    # Plot total pelanggan aktif
    print("\n📈 Trend Total Pelanggan Aktif\n")
    plt.clear_figure()
    
    months = [m.split()[0] for m in df['Bulan'].tolist()]
    values = df['Total_Pelanggan_Aktif'].tolist()
    
    # Use numeric indices instead of month names to avoid date parsing
    x_indices = list(range(len(months)))
    plt.plot(x_indices, values, marker='braille')
    plt.title('Total Pelanggan Aktif per Bulan')
    plt.xlabel('Bulan: ' + ' -> '.join(months))
    plt.ylabel('Jumlah Pelanggan')
    plt.plotsize(60, 15)
    plt.show()
    
    # Plot churn rate
    print("\n📉 Trend Churn Rate per Bulan\n")
    plt.clear_figure()
    
    months_result = [m.split()[0] for m in results_df['Bulan'].tolist()]
    churn_values = results_df['Churn_Rate'].tolist()
    
    # Use numeric indices instead of month names
    x_indices_result = list(range(len(months_result)))
    plt.plot(x_indices_result, churn_values, marker='braille')
    plt.title('Churn Rate per Bulan (%)')
    plt.xlabel('Bulan: ' + ' -> '.join(months_result))
    plt.ylabel('Churn Rate (%)')
    plt.plotsize(60, 15)
    plt.show()

def cohort_analysis(results_df):
    """Lakukan Cohort Analysis sederhana"""
    print("\n" + "="*70)
    print("📊 COHORT ANALYSIS")
    print("="*70)
    
    print("\n📋 Retention Rate per Bulan Akuisisi:")
    print(results_df[['Bulan', 'Retention_Rate', 'Churn_Rate']].to_string(index=False))
    
    # Identifikasi bulan terbaik dan terburuk
    best_month = results_df.loc[results_df['Retention_Rate'].idxmax()]
    worst_month = results_df.loc[results_df['Churn_Rate'].idxmax()]
    
    print(f"\n🏆 BULAN DENGAN RETENSI TERBAIK:")
    print(f"   {best_month['Bulan']}")
    print(f"   Retention Rate: {best_month['Retention_Rate']:.2f}%")
    print(f"   Churn Rate: {best_month['Churn_Rate']:.2f}%")
    
    print(f"\n⚠️  BULAN DENGAN RETENSI TERBURUK:")
    print(f"   {worst_month['Bulan']}")
    print(f"   Retention Rate: {worst_month['Retention_Rate']:.2f}%")
    print(f"   Churn Rate: {worst_month['Churn_Rate']:.2f}%")
    
    return best_month, worst_month

def main():
    """Main function"""
    print("\n" + "="*70)
    print("🚀 SOAL 2: ANALISIS RETENSI 'IRAMA KITA'")
    print("="*70)
    
    # Load data
    df = load_data()
    print(f"\n✅ Data berhasil dimuat: {len(df)} bulan")
    
    print("\n📄 Data Pelanggan:")
    print(df.to_string(index=False))
    
    # Hitung Churn & Retention Rate
    results_df = calculate_churn_retention(df)
    
    # Tampilkan hasil bulan yang diminta
    show_specific_months(results_df)
    
    # Visualisasi
    visualize_trends(df, results_df)
    
    # Cohort Analysis
    best_month, worst_month = cohort_analysis(results_df)
    
    # Kesimpulan
    print("\n" + "="*70)
    print("🎯 KESIMPULAN & REKOMENDASI")
    print("="*70)
    
    print("\n1. TREND RETENSI:")
    print("   - Churn Rate cenderung menurun dari Maret ke Juli (POSITIF)")
    print("   - Retention Rate meningkat seiring waktu (BAIK)")
    print("   - Pertumbuhan pelanggan konsisten positif")
    
    print("\n2. PERFORMA BULANAN:")
    print(f"   - Bulan Terbaik: {best_month['Bulan']} ({best_month['Retention_Rate']:.2f}%)")
    print(f"   - Bulan Terburuk: {worst_month['Bulan']} ({worst_month['Churn_Rate']:.2f}% churn)")
    
    print("\n3. REKOMENDASI:")
    print("   - Investigate faktor di bulan April (churn tertinggi)")
    print("   - Replikasi strategi bulan Juli (retensi terbaik)")
    print("   - Focus on onboarding pelanggan baru untuk improve retention")
    print("   - Monitor churn rate < 5% untuk maintain kesehatan bisnis")
    
    print("\n" + "="*70)
    print("✅ Analisis Selesai!")
    print("="*70)
    print("\n💡 Tip: Lihat analysis.ipynb untuk analisis lebih detail dengan Jupyter!")
    print()

if __name__ == "__main__":
    main()

