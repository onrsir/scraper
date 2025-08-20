# Predictz.com Maç Tahminleri Scraper

Bu proje, [Predictz.com](https://www.predictz.com/predictions/tomorrow/) web sitesinden yarınki futbol maç tahminlerini çeken bir web scraper içerir.

## Özellikler

- Yarınki futbol maçlarının verilerini çeker
- Maçların ev sahibi ve deplasman takımlarını ve tahminleri toplar
- Verileri JSON dosyasına kaydeder

## Kurulum

1. Gereksinimleri yükleyin:
```
pip install -r requirements.txt
```

## Kullanım

### Scraper'ı çalıştırmak için:
```
python api_server.py
```

Bu komut, maç verilerini çekecek ve günün tarihi ile bir JSON dosyasına kaydedecektir (örn: `predictz_matches_2023-09-13.json`).

## Çıktı

JSON dosyası aşağıdaki bilgileri içerir:

- Tarih
- Ev sahibi takım
- Deplasman takımı
- Tahmin 