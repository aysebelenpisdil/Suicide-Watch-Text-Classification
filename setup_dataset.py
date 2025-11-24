import os
import zipfile
import pandas as pd
from pathlib import Path

def setup_kaggle_credentials():
    kaggle_dir = Path.home() / '.kaggle'
    kaggle_json = kaggle_dir / 'kaggle.json'
    if not kaggle_json.exists():
        print("\n⚠️  Kaggle API anahtarı bulunamadı!")
        print("\nKaggle API anahtarını ayarlamak için:")
        print("1. https://www.kaggle.com/account adresine gidin")
        print("2. 'Create New API Token' butonuna tıklayın")
        print("3. İndirilen kaggle.json dosyasını ~/.kaggle/ klasörüne koyun")
        print("4. chmod 600 ~/.kaggle/kaggle.json komutunu çalıştırın (Linux/Mac)")
        return False
    return True

def download_dataset():
    if not setup_kaggle_credentials():
        return False
    try:
        import kaggle
        print("\n📥 Veri seti indiriliyor...")
        kaggle.api.dataset_download_files(
            'nikhileswarkomati/suicide-watch',
            path='data/raw',
            unzip=True
        )
        print("✅ Veri seti başarıyla indirildi!")
        return True
    except Exception as e:
        print(f"❌ Hata: {e}")
        print("\nAlternatif olarak:")
        print("1. https://www.kaggle.com/datasets/nikhileswarkomati/suicide-watch adresine gidin")
        print("2. 'Download' butonuna tıklayın")
        print("3. İndirilen CSV dosyasını data/raw/ klasörüne koyun")
        return False

def check_dataset():
    dataset_path = Path('data/raw/Suicide_Detection.csv')
    if not dataset_path.exists():
        print("\n⚠️  Veri seti dosyası bulunamadı!")
        print(f"Beklenen konum: {dataset_path.absolute()}")
        return False
    print("\n📊 Veri seti bilgileri:")
    df = pd.read_csv(dataset_path)
    print(f"- Toplam örnek sayısı: {len(df):,}")
    print(f"- Sütunlar: {', '.join(df.columns)}")
    print(f"\n- Sınıf dağılımı:")
    class_counts = df['class'].value_counts()
    for class_name, count in class_counts.items():
        label = "Non-suicide" if class_name == 0 else "Suicide"
        print(f"  {label} (class={class_name}): {count:,} ({count/len(df)*100:.1f}%)")
    print(f"\n- İlk 3 örnek:")
    for i in range(min(3, len(df))):
        text = df.iloc[i]['text'][:100] + "..." if len(df.iloc[i]['text']) > 100 else df.iloc[i]['text']
        print(f"  {i+1}. Class={df.iloc[i]['class']}: {text}")
    return True

def main():
    print("=" * 60)
    print("SUICIDE WATCH VERİ SETİ KURULUM")
    print("=" * 60)
    data_dirs = ['data/raw', 'data/processed', 'data/splits']
    for dir_path in data_dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)
    if not check_dataset():
        if download_dataset():
            check_dataset()
        else:
            print("\n❌ Veri seti indirilemedi. Lütfen manuel olarak indirin.")
            return
    print("\n✅ Veri seti hazır!")
    print("\nSonraki adımlar:")
    print("1. notebooks/01_veri_analizi.ipynb ile veri keşfi yapın")
    print("2. src/data_preprocessing.py ile veri ön işleme yapın")
    print("3. Model eğitimi için notebooks/03_model_egitim.ipynb kullanın")

if __name__ == "__main__":
    main()