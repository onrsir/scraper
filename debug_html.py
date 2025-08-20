#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import os

def get_html_structure():
    """Web sayfasının HTML yapısını getir ve dosyaya kaydet"""
    url = "https://www.predictz.com/predictions/tomorrow/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print(f"Sayfa getiriliyor: {url}")
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        # HTML içeriğini kaydet
        with open("page_content.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("HTML içeriği 'page_content.html' dosyasına kaydedildi.")
        
        # BeautifulSoup ile parse et
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Lig başlıkları var mı kontrol et
        league_titles = soup.find_all('h2', class_='league-title')
        print(f"Bulunan lig başlıkları sayısı: {len(league_titles)}")
        
        if league_titles:
            for i, title in enumerate(league_titles[:3], 1):  # İlk 3 başlığı göster
                print(f"{i}. Lig başlığı: {title.text.strip()}")
                
                # Her lig başlığından sonraki tablo var mı?
                match_table = title.find_next('table')
                if match_table:
                    print(f"   - Bu lig için maç tablosu bulundu.")
                    match_rows = match_table.find_all('tr')
                    print(f"   - Bu ligde {len(match_rows)} satır var.")
                else:
                    print(f"   - Bu lig için maç tablosu bulunamadı.")
        else:
            print("Lig başlıkları bulunamadı. Farklı bir yapıyı analiz et:")
            
            # Alternatif yapı analizi
            print("\nSayfada bulunan bazı HTML öğeleri:")
            
            # Tüm tabloları kontrol et
            tables = soup.find_all('table')
            print(f"Toplam tablo sayısı: {len(tables)}")
            
            # Tüm h2 başlıklarını kontrol et
            h2_tags = soup.find_all('h2')
            print(f"Toplam h2 başlığı sayısı: {len(h2_tags)}")
            for i, h2 in enumerate(h2_tags[:5], 1):  # İlk 5 başlığı göster
                print(f"{i}. h2 başlığı: {h2.text.strip()}")
                print(f"   CSS sınıfları: {h2.get('class', 'sınıf yok')}")
            
            # Sayfa başlığını kontrol et
            title = soup.find('title')
            if title:
                print(f"\nSayfa başlığı: {title.text}")
            
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    get_html_structure() 