#!/bin/bash
echo "YSA Final Projesi Başlatılıyor..."
echo "=================================="
if [ ! -d "venv" ]; then
    echo "Virtual environment oluşturuluyor..."
    python3 -m venv venv
fi
source venv/bin/activate
echo "Gerekli paketler yükleniyor..."
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "Veri seti kontrol ediliyor..."
python3 setup_dataset.py
echo "=================================="
echo "Proje hazır! Jupyter Notebook başlatmak için: jupyter notebook"