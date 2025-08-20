#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import datetime
import os
import logging
import requests
from bs4 import BeautifulSoup
from predictz_scraper import PredictzScraper, Match

# Log yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger('predictz_api')

# Veri dosyasının yolu
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def get_league_names():
    """Predictz.com sitesinden lig isimlerini çeker"""
    # Cloudflare koruması nedeniyle manuel olarak lig isimlerini tanımlıyoruz
    leagues = [
        "Qatar Stars League Tips",
        "Uzbekistan Super League Tips",
        "Algeria Ligue 1 Tips",
        "Egypt Premier League Tips",
        "Europa League Tips",
        "Europa Conference League Tips",
        "Copa Libertadores Tips",
        "Copa Sudamericana Tips"
    ]
    
    for league in leagues:
        logger.info(f"Lig tanımlandı: {league}")
    
    return leagues

def create_json_file():
    """Predictz.com sitesinden veri çekip JSON dosyasına kaydeder"""
    logger.info("Veri çekme işlemi başlatılıyor...")
    
    try:
        # Önce lig isimlerini al
        leagues = get_league_names()
        if not leagues:
            logger.warning("Lig isimleri çekilemedi!")
        else:
            logger.info(f"Toplam {len(leagues)} lig bulundu: {', '.join(leagues)}")
        
        # Scraper'ı başlat
        scraper = PredictzScraper()
        matches = scraper.scrape()
        
        if not matches:
            logger.error("Veri çekilemedi!")
            return None
        
        # Bugünün tarihini al
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        
        # Dosya adını oluştur
        json_file = os.path.join(DATA_DIR, f"predictz_matches_{today}.json")
        
        # Maç nesnelerini sözlüklere dönüştür
        matches_dict = []
        for match in matches:
            # Eğer maçın ligi Europa League Tips ise, görüntüden gördüğümüz ligleri kontrol edelim
            league_name = match.league
            
            match_dict = {
                "date": match.date,
                "home_team": match.home_team,
                "away_team": match.away_team,
                "league": league_name,  # Lig ismi eklenmiş hali
                "prediction": match.prediction
            }
            matches_dict.append(match_dict)
        
        # JSON dosyasına kaydet
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(matches_dict, f, ensure_ascii=False, indent=4)
        
        logger.info(f"Veriler {json_file} dosyasına kaydedildi. Toplam {len(matches)} maç.")
        return json_file
    
    except Exception as e:
        logger.error(f"İşlem sırasında hata oluştu: {e}")
        return None

if __name__ == '__main__':
    # JSON dosyası oluştur
    result = create_json_file()
    
    if result:
        logger.info("İşlem başarıyla tamamlandı.")
    else:
        logger.error("İşlem başarısız oldu.") 