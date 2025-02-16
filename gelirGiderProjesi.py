import pandas as pd

# Şube isimleri
subeler = [f'Sube {i+1}' for i in range(10)]

# Gelirler (örnek veriler, her şube için artırılmış değerler)
gelirler = [49000, 59500, 71000, 69800, 80000, 89900, 70300, 90600, 70700, 50900]

# Giderler (örnek veriler, sabit tutulan)
giderler = {
    'Kasiyer Maas': [2800, 2800, 2800, 2800, 2800, 2800, 2800, 2800, 2800, 2800],
    'Paketci Maas': [3*3400, 3*3400, 3*3400, 3*3400, 3*3400, 3*3400, 3*3400, 3*3400, 3*3400, 3*3400],
    'Temizlikci Maas': [2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300, 2300],
    'Usta Maas': [2*3800, 2*3800, 2*3800, 2*3800, 2*3800, 2*3800, 2*3800, 2*3800, 2*3800, 2*3800],
    'Garson Maas': [2*2800, 2*2800, 2*2800, 2*2800, 2*2800, 2*2800, 2*2800, 2*2800, 2*2800, 2*2800],
    'Kira': [4800, 5000, 4900, 5100, 5200, 4800, 5000, 5100, 5200, 5300],
    'Yemek': [1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800, 1800],
    'Faturalar': [2700, 2800, 2900, 2700, 2800, 2900, 2700, 2800, 2900, 2800],
    'Primler': [450, 550, 500, 600, 550, 450, 550, 500, 600, 550]
}

df = pd.DataFrame(giderler, index=subeler)
df['Gelir'] = gelirler
df['Toplam Gider'] = df.drop(columns=['Gelir']).sum(axis=1)
df['Net Kazanc'] = df['Gelir'] - df['Toplam Gider']

# Vergi oranı
vergi_orani = 0.20
df['Vergi'] = df['Net Kazanc'] * vergi_orani
df['Vergi Sonrası Kazanç'] = df['Net Kazanc'] - df['Vergi']
print(df)
import matplotlib.pyplot as plt

# Şubelerin Gelir, Gider ve Vergi Sonrası Kazançları Tablosu
fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('tight')
ax.axis('off')
table_data = df[['Gelir', 'Toplam Gider', 'Net Kazanc', 'Vergi', 'Vergi Sonrası Kazanç']]
ax.table(cellText=table_data.values, colLabels=table_data.columns, rowLabels=table_data.index, cellLoc='center', loc='center')
plt.title('Şubelerin Gelir, Gider ve Vergi Sonrası Kazançları')
plt.show()
# Şubelerin Gider Kalemleri Tablosu
fig, ax = plt.subplots(figsize=(12, 5))
ax.axis('tight')
ax.axis('off')
table_data = df.drop(columns=['Gelir', 'Toplam Gider', 'Net Kazanc', 'Vergi', 'Vergi Sonrası Kazanç'])
ax.table(cellText=table_data.values, colLabels=table_data.columns, rowLabels=table_data.index, cellLoc='center', loc='center')
plt.title('Şubelerin Gider Kalemleri')
plt.show()
# Çalışan kategorilerine göre maaşları hesaplayalım
maaslar = {
    'Kasiyer': [2800] * 10,
    'Paketci': [3*3400] * 10,
    'Temizlikci': [2300] * 10,
    'Usta': [2*3800] * 10,
    'Garson': [2*2800] * 10
}

df_maaslar = pd.DataFrame(maaslar, index=subeler)
df_maaslar['Toplam Maas'] = df_maaslar.sum(axis=1)
print("\nÇalışan Kategorilerine Göre Maaşlar:")
print(df_maaslar)

# Çalışan Kategorilerine Göre Maaşlar Tablosu
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('tight')
ax.axis('off')
table_data = df_maaslar
ax.table(cellText=table_data.values, colLabels=table_data.columns, rowLabels=table_data.index, cellLoc='center', loc='center')
plt.title('Çalışan Kategorilerine Göre Maaşlar')
plt.show()
# Toplam gelir, gider, vergi ve net kazancı hesaplayalım
toplam_gelir = df['Gelir'].sum()
toplam_gider = df['Toplam Gider'].sum()
toplam_net_kazanc = df['Net Kazanc'].sum()
toplam_vergi = df['Vergi'].sum()
toplam_vergi_sonrasi_kazanc = df['Vergi Sonrası Kazanç'].sum()

print(f"Toplam Gelir: {toplam_gelir} TL")
print(f"Toplam Gider: {toplam_gider} TL")
print(f"Toplam Net Kazanç: {toplam_net_kazanc} TL")
print(f"Toplam Vergi: {toplam_vergi} TL")
print(f"Toplam Vergi Sonrası Kazanç: {toplam_vergi_sonrasi_kazanc} TL")

# Toplam Gelir, Gider, Vergi ve Vergi Sonrası Kazanç Tablosu
fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('tight')
ax.axis('off')
table_data = [['Toplam Gelir', toplam_gelir], ['Toplam Gider', toplam_gider], ['Toplam Net Kazanç', toplam_net_kazanc], ['Toplam Vergi', toplam_vergi], ['Toplam Vergi Sonrası Kazanç', toplam_vergi_sonrasi_kazanc]]
ax.table(cellText=table_data, colLabels=['Kalem', 'Tutar (TL)'], cellLoc='center', loc='center')
plt.title('Toplam Gelir, Gider, Vergi ve Vergi Sonrası Kazanç')
plt.show()

