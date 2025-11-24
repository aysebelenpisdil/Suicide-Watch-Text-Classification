# Yapay Sinir Ağları Final Projesi - Suicide Watch Text Classification

## Proje Hakkında
Bu proje, Yapay Sinir Ağlarına Giriş dersi için hazırlanmıştır. Reddit'ten toplanan Suicide Watch veri seti kullanılarak, metin sınıflandırma problemi çözülmektedir.

### Veri Seti
- **Kaynak**: [Kaggle - Suicide Watch Dataset](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch)
- **Açıklama**: Reddit'in r/SuicideWatch ve r/teenagers subreddit'lerinden toplanan metin verileri
- **Sınıflar**:
  - 0: Non-suicide (İntihar riski yok)
  - 1: Suicide (İntihar riski var)

## Proje Yapısı

```
ysa-final/
│
├── data/                      # Veri setleri
│   ├── raw/                  # Ham veri (Kaggle'dan indirilen)
│   │   └── Suicide_Detection.csv
│   ├── processed/            # İşlenmiş veri
│   └── splits/              # Train/test/validation ayrımları
│
├── notebooks/                # Jupyter notebook'ları
│   ├── 01_veri_analizi.ipynb
│   ├── 02_veri_isleme.ipynb
│   ├── 03_model_egitim.ipynb
│   └── 04_sonuclar.ipynb
│
├── src/                      # Python kaynak kodları
│   ├── data_preprocessing.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── utils.py
│
├── models/                   # Eğitilmiş modeller
│   └── best_model.h5
│
├── outputs/                  # Çıktılar
│   ├── figures/             # Grafikler
│   ├── confusion_matrices/  # Karmaşıklık matrisleri
│   └── results/             # Test sonuçları
│
├── docs/                     # Dokümantasyon
│   └── final_rapor.docx
│
└── requirements.txt          # Python bağımlılıkları
```

## Kurulum

### 1. Veri Setini İndirme

#### Yöntem 1: Kaggle Web Sitesinden
1. [Kaggle Dataset Sayfası](https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch)'na gidin
2. "Download" butonuna tıklayın (Kaggle hesabı gerekli)
3. İndirilen `archive.zip` dosyasını açın
4. `Suicide_Detection.csv` dosyasını `data/raw/` klasörüne koyun

#### Yöntem 2: Kaggle API ile
```bash
# Kaggle API kurulumu
pip install kaggle

# API token'ınızı yerleştirin (~/.kaggle/kaggle.json)

# Veri setini indirin
kaggle datasets download -d nikhileswarkomati/suicide-watch -p data/raw/

# ZIP dosyasını açın
cd data/raw/
unzip suicide-watch.zip
```

### 2. Python Ortamını Hazırlama

```bash
# Virtual environment oluştur
python -m venv venv

# Aktif et (Windows)
venv\Scripts\activate

# Aktif et (Mac/Linux)
source venv/bin/activate

# Gereklilikleri yükle
pip install -r requirements.txt
```

## Veri Seti Bilgileri

- **Toplam Örnek Sayısı**: 232,074
- **Özellikler**:
  - `text`: Reddit gönderi metni
  - `class`: Sınıf etiketi (0 veya 1)
- **Sınıf Dağılımı**:
  - Non-suicide: ~116,000
  - Suicide: ~116,000

## Kullanılan Yöntemler

1. **Veri Ön İşleme**
   - Metin temizleme
   - Tokenization
   - Padding/Truncation
   - Word embedding

2. **Model Mimarisi**
   - LSTM/GRU tabanlı yapay sinir ağı
   - Embedding katmanı
   - Dense katmanlar

3. **Test Senaryoları**
   - Eğitim verisi üzerinde test
   - 5-fold cross validation
   - 10-fold cross validation
   - %75-%25 train-test split (5 farklı random split)

## İletişim
[Öğrenci Adı Soyadı]
[Öğrenci Numarası]