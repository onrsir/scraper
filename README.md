# Predictz.com Maç Tahminleri Scraper

Bu proje, [Predictz.com](https://www.predictz.com/predictions/tomorrow/) web sitesinden yarınki futbol maç tahminlerini çeken bir web scraper içerir.

## Özellikler

- Yarınki futbol maçlarının verilerini çeker
- Maçların ev sahibi ve deplasman takımlarını, oranlarını, form bilgilerini ve tahminleri toplar
- Verileri CSV dosyasına kaydeder
- Hata yakalama ve günlük tutma özellikleri

## Kurulum

1. Gereksinimleri yükleyin:
```
pip install -r requirements.txt
```

## Kullanım

Scripti çalıştırmak için:
```
python predictz_scraper.py
```

Bu komut, maç verilerini çekecek ve günün tarihi ile bir CSV dosyasına kaydedecektir (örn: `predictz_matches_2023-09-13.csv`).

## Çıktı

Script aşağıdaki bilgileri içeren bir CSV dosyası oluşturur:

- Tarih
- Ev sahibi takım
- Deplasman takımı
- Lig
- Ev sahibi oranları
- Beraberlik oranları
- Deplasman oranları
- Ev sahibi takımın form bilgisi (son 5 maç)
- Deplasman takımının form bilgisi (son 5 maç)
- Tahmin 