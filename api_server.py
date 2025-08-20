#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
import os
import json
import datetime
import logging
from predictz_scraper import PredictzScraper

# Log yapılandırması
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger('predictz_api')

app = Flask(__name__)

# Veri dosyasının yolu
DATA_DIR = os.path.dirname(os.path.abspath(__file__))

def get_latest_data_file():
    """En son oluşturulan JSON veri dosyasını bul"""
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    json_file = os.path.join(DATA_DIR, f"predictz_matches_{today}.json")
    
    # Eğer bugünün dosyası yoksa, scraper'ı çalıştır
    if not os.path.exists(json_file):
        logger.info(f"Bugünün veri dosyası bulunamadı. Scraper çalıştırılıyor...")
        scraper = PredictzScraper()
        matches = scraper.scrape()
        if matches:
            json_file = scraper.save_to_json()
            logger.info(f"Yeni veri dosyası oluşturuldu: {json_file}")
        else:
            logger.error("Veri çekilemedi!")
            return None
    
    return json_file

def load_data():
    """En son veri dosyasını yükle"""
    json_file = get_latest_data_file()
    if not json_file or not os.path.exists(json_file):
        logger.error(f"Veri dosyası bulunamadı: {json_file}")
        return []
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        logger.error(f"Veri dosyası yüklenirken hata: {e}")
        return []

@app.route('/')
def index():
    """Ana sayfa"""
    return "Predictz API - Kullanılabilir endpointler: /api/matches, /api/matches/<league>, /api/leagues, /api/refresh"

@app.route('/api/matches', methods=['GET'])
def get_matches():
    """Tüm maçları getir"""
    data = load_data()
    return jsonify(data)

@app.route('/api/matches/<league>', methods=['GET'])
def get_matches_by_league(league):
    """Belirli bir lige ait maçları getir"""
    data = load_data()
    filtered_data = [match for match in data if match['league'].lower() == league.lower()]
    return jsonify(filtered_data)

@app.route('/api/leagues', methods=['GET'])
def get_leagues():
    """Mevcut tüm ligleri getir"""
    data = load_data()
    leagues = list(set(match['league'] for match in data))
    return jsonify(leagues)

@app.route('/api/refresh', methods=['GET'])
def refresh_data():
    """Verileri yenile"""
    scraper = PredictzScraper()
    matches = scraper.scrape()
    
    if matches:
        json_file = scraper.save_to_json()
        logger.info(f"Veriler yenilendi: {json_file}")
        return jsonify({"status": "success", "message": f"Veriler yenilendi: {len(matches)} maç"})
    else:
        return jsonify({"status": "error", "message": "Veri çekilemedi!"})

if __name__ == '__main__':
    # API sunucusunu başlat
    app.run(host='0.0.0.0', port=5000) 