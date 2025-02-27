import pandas as pd

# Veri setini yükleme
data = pd.read_csv("train.csv")

# İlk beş satırı görüntüleme
print(data.head())

# Veri hakkında genel bilgi
print(data.info())

# İstatistiksel özet
print(data.describe())
# Sayısal sütunlardaki eksik değerleri medyan ile doldurma
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_columns:
    data[col] = data[col].fillna(data[col].median())  # inplace=True yerine doğrudan atama

# Kategorik sütunlardaki eksik değerleri "None" ile doldurma
categorical_columns = data.select_dtypes(include=['object']).columns
for col in categorical_columns:
    data[col] = data[col].fillna("None")  # inplace=True yerine doğrudan atama
# Kategorik verileri dönüştürme (One-Hot Encoding)
data = pd.get_dummies(data, drop_first=True)
# Özellikler ve hedef değişkeni ayırma
X = data.drop("SalePrice", axis=1)  # Bağımsız değişkenler
y = data["SalePrice"]  # Bağımlı değişken
print(data.head())

from sklearn.model_selection import train_test_split

# Veriyi eğitim ve test setlerine bölme
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.preprocessing import StandardScaler

# Veriyi ölçeklendirme
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

import tensorflow as tf

# Model oluşturma
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # Çıktı katmanı (regresyon için tek bir nöron)
])

# Modeli derleme
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Modeli eğitme
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_split=0.2)

from sklearn.metrics import mean_squared_error

# Test seti üzerinde tahmin yapma
y_pred = model.predict(X_test)

# Hata metriklerini hesaplama
mse = mean_squared_error(y_test, y_pred)
rmse = mse**0.5
print(f"Root Mean Squared Error (RMSE): {rmse}")

import matplotlib.pyplot as plt

# Eğitim ve doğrulama kaybını görselleştirme
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Loss Over Epochs')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

# Gerçek ve tahmin edilen değerleri karşılaştırma
plt.scatter(y_test, y_pred)
plt.xlabel('Gerçek Fiyatlar')
plt.ylabel('Tahmin Edilen Fiyatlar')
plt.title('Gerçek vs Tahmin Edilen Fiyatlar')
plt.show()