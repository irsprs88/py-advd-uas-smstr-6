"""
Soal 3: Dashboard Interaktif dengan Shiny for Python
Visualisasi data penjualan Q4 2024 dengan filter interaktif
"""

from shiny import App, render, ui, reactive
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data_sales.csv')

# UI Definition
app_ui = ui.page_sidebar(
    ui.sidebar(
        ui.h3("⚙️ Filter & Pengaturan"),
        ui.hr(),
        
        # Q1: Checkbox Group untuk Lokasi
        ui.input_checkbox_group(
            "lokasi_filter",
            "📍 Pilih Lokasi:",
            choices=["Jakarta", "Surabaya", "Bandung"],
            selected=["Jakarta", "Surabaya", "Bandung"]
        ),
        
        ui.hr(),
        
        # Q1: Radio Button untuk Metrik
        ui.input_radio_buttons(
            "metrik_pilihan",
            "📈 Pilih Metrik:",
            choices={
                "penjualan": "Total Penjualan (Rp)",
                "margin": "Margin Keuntungan (%)"
            },
            selected="penjualan"
        ),
        
        ui.hr(),
        
        # Info tambahan
        ui.div(
            ui.p("💡 ", ui.strong("Tips:")),
            ui.p("• Pilih lokasi untuk filter data"),
            ui.p("• Toggle metrik untuk analisis berbeda"),
            ui.p("• Chart akan update otomatis"),
            style="font-size: 0.85em; color: #666;"
        ),
    ),
    
    # MAIN CONTENT
    ui.h2("📊 Dashboard Penjualan Q4 2024"),
    
    # Summary Statistics
    ui.card(
        ui.card_header("📊 Ringkasan Data"),
        ui.output_text_verbatim("summary_stats"),
    ),
    
    ui.br(),
    
    # Main Plot - Grouped Bar Chart
    ui.card(
        ui.card_header("📈 Grouped Bar Chart - Perbandingan per Kategori Produk"),
        ui.output_plot("main_plot", height="500px"),
    ),
    
    ui.br(),
    
    # Q3: Analisis Visual
    ui.card(
        ui.card_header("💡 Analisis: Margin Elektronik vs Pakaian di Jakarta Q4"),
        ui.output_ui("analysis_text"),
    ),
    
    title="Dashboard Penjualan Q4 2024"
)

# Server Logic
def server(input, output, session):
    
    # Q2: Reactive data filtering berdasarkan lokasi
    @reactive.Calc
    def data_filtered():
        # Filter berdasarkan lokasi yang dipilih
        if len(input.lokasi_filter()) > 0:
            filtered = df[df['Lokasi'].isin(input.lokasi_filter())].copy()
        else:
            filtered = df.copy()
        
        return filtered
    
    # Q2: Reactive data aggregation untuk visualisasi
    @reactive.Calc
    def data_aggregated():
        filtered = data_filtered()
        metrik = input.metrik_pilihan()
        
        if metrik == "penjualan":
            # Aggregasi: SUM untuk Total Penjualan
            agg_data = filtered.groupby(['Kategori_Produk', 'Lokasi'])['Total_Penjualan'].sum().reset_index()
            agg_data.columns = ['Kategori_Produk', 'Lokasi', 'Nilai']
        else:
            # Aggregasi: MEAN untuk Margin Keuntungan
            agg_data = filtered.groupby(['Kategori_Produk', 'Lokasi'])['Margin_Keuntungan'].mean().reset_index()
            agg_data.columns = ['Kategori_Produk', 'Lokasi', 'Nilai']
            # Convert to percentage
            agg_data['Nilai'] = agg_data['Nilai'] * 100
        
        return agg_data, metrik
    
    # Output: Summary Statistics
    @output
    @render.text
    def summary_stats():
        filtered = data_filtered()
        metrik = input.metrik_pilihan()
        
        total_rows = len(filtered)
        lokasi_count = filtered['Lokasi'].nunique()
        kategori_count = filtered['Kategori_Produk'].nunique()
        
        if metrik == "penjualan":
            total_value = filtered['Total_Penjualan'].sum()
            avg_value = filtered['Total_Penjualan'].mean()
            metric_name = "Total Penjualan"
            format_str = "Rp {:,.0f}"
        else:
            total_value = filtered['Margin_Keuntungan'].mean() * 100
            avg_value = filtered['Margin_Keuntungan'].mean() * 100
            metric_name = "Rata-rata Margin"
            format_str = "{:.2f}%"
        
        stats = f"""
Data yang Ditampilkan:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Total Baris Data: {total_rows}
• Jumlah Lokasi: {lokasi_count}
• Jumlah Kategori: {kategori_count}
• Lokasi Terpilih: {', '.join(input.lokasi_filter()) if input.lokasi_filter() else 'Tidak ada'}
• Metrik: {metric_name}

"""
        if metrik == "penjualan":
            stats += f"• Total Keseluruhan: {format_str.format(total_value)}\n"
            stats += f"• Rata-rata per Transaksi: {format_str.format(avg_value)}"
        else:
            stats += f"• {metric_name}: {format_str.format(avg_value)}"
        
        return stats
    
    # Q2 & Q3: Main Plot - Grouped Bar Chart
    @output
    @render.plot
    def main_plot():
        agg_data, metrik = data_aggregated()
        
        if agg_data.empty:
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.text(0.5, 0.5, 'Tidak ada data untuk ditampilkan\nSilakan pilih lokasi', 
                   ha='center', va='center', fontsize=14, color='red')
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            ax.axis('off')
            return fig
        
        # Create grouped bar chart
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Pivot data untuk grouped bar chart
        pivot_data = agg_data.pivot(index='Kategori_Produk', columns='Lokasi', values='Nilai')
        
        # Plot dengan seaborn
        pivot_data.plot(kind='bar', ax=ax, width=0.8, edgecolor='black', linewidth=1.2)
        
        # Styling
        if metrik == "penjualan":
            title = "Total Penjualan per Kategori Produk (Berdasarkan Lokasi)"
            ylabel = "Total Penjualan (Rp)"
            format_func = lambda x: f'Rp {x:,.0f}'
        else:
            title = "Margin Keuntungan per Kategori Produk (Berdasarkan Lokasi)"
            ylabel = "Margin Keuntungan (%)"
            format_func = lambda x: f'{x:.1f}%'
        
        ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel('Kategori Produk', fontsize=12, fontweight='bold')
        ax.set_ylabel(ylabel, fontsize=12, fontweight='bold')
        ax.legend(title='Lokasi', title_fontsize=11, fontsize=10, loc='upper right')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_xticklabels(ax.get_xticklabels(), rotation=0, ha='center')
        
        # Tambahkan nilai di atas bar
        for container in ax.containers:
            labels = [format_func(v) if v > 0 else '' for v in container.datavalues]
            ax.bar_label(container, labels=labels, fontsize=9, padding=3)
        
        plt.tight_layout()
        return fig
    
    # Q3: Analisis Visual Output
    @output
    @render.ui
    def analysis_text():
        # Filter data Jakarta saja
        jakarta_data = df[df['Lokasi'] == 'Jakarta'].copy()
        
        # Hitung rata-rata margin per kategori
        margin_elektronik = jakarta_data[jakarta_data['Kategori_Produk'] == 'Elektronik']['Margin_Keuntungan'].mean() * 100
        margin_pakaian = jakarta_data[jakarta_data['Kategori_Produk'] == 'Pakaian']['Margin_Keuntungan'].mean() * 100
        
        # Hitung total penjualan per kategori
        sales_elektronik = jakarta_data[jakarta_data['Kategori_Produk'] == 'Elektronik']['Total_Penjualan'].sum()
        sales_pakaian = jakarta_data[jakarta_data['Kategori_Produk'] == 'Pakaian']['Total_Penjualan'].sum()
        
        perbedaan_margin = margin_pakaian - margin_elektronik
        rasio_margin = margin_pakaian / margin_elektronik if margin_elektronik > 0 else 0
        
        return ui.div(
            ui.h4("📊 Hasil Analisis Margin - Jakarta Q4 2024", style="color: #2c3e50;"),
            ui.hr(),
            
            ui.div(
                ui.h5("📈 Data Margin Keuntungan:", style="color: #16a085;"),
                ui.tags.ul(
                    ui.tags.li(f"Elektronik: {margin_elektronik:.2f}%", style="font-size: 1.1em;"),
                    ui.tags.li(f"Pakaian: {margin_pakaian:.2f}%", style="font-size: 1.1em; font-weight: bold; color: #27ae60;"),
                    ui.tags.li(f"Perbedaan: {perbedaan_margin:.2f}% (Pakaian lebih tinggi)", style="font-size: 1.1em;"),
                ),
                style="background-color: #ecf0f1; padding: 15px; border-radius: 5px; margin-bottom: 15px;"
            ),
            
            ui.div(
                ui.h5("💰 Data Total Penjualan:", style="color: #d35400;"),
                ui.tags.ul(
                    ui.tags.li(f"Elektronik: Rp {sales_elektronik:,.0f}", style="font-size: 1.1em; font-weight: bold;"),
                    ui.tags.li(f"Pakaian: Rp {sales_pakaian:,.0f}", style="font-size: 1.1em;"),
                ),
                style="background-color: #fef5e7; padding: 15px; border-radius: 5px; margin-bottom: 15px;"
            ),
            
            ui.div(
                ui.h5("🎯 Insight Kritis:", style="color: #c0392b;"),
                ui.p(
                    f"Berdasarkan visualisasi grouped bar chart untuk Jakarta Q4 2024, terlihat bahwa:",
                    style="font-size: 1.05em;"
                ),
                ui.tags.ul(
                    ui.tags.li(
                        ui.strong("Margin Pakaian lebih tinggi {:.1f}x lipat".format(rasio_margin)),
                        f" dibanding Elektronik ({margin_pakaian:.2f}% vs {margin_elektronik:.2f}%)",
                        style="font-size: 1.05em; margin-bottom: 10px;"
                    ),
                    ui.tags.li(
                        ui.strong("Elektronik memiliki volume penjualan lebih besar"),
                        f" (Rp {sales_elektronik:,.0f}) namun margin lebih rendah",
                        style="font-size: 1.05em; margin-bottom: 10px;"
                    ),
                    ui.tags.li(
                        ui.strong("Implikasi Bisnis: "),
                        "Pakaian lebih profitable per unit. Strategi sebaiknya: ",
                        "fokus pada peningkatan volume Pakaian atau improve margin Elektronik melalui efisiensi operasional.",
                        style="font-size: 1.05em; margin-bottom: 10px;"
                    ),
                ),
                style="background-color: #fadbd8; padding: 15px; border-radius: 5px;"
            ),
            
            ui.hr(),
            ui.p(
                "💡 Gunakan filter lokasi di sidebar untuk melihat perbandingan di kota lain!",
                style="font-style: italic; color: #7f8c8d; text-align: center;"
            )
        )

# Create app
app = App(app_ui, server)

