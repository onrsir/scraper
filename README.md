# Predictz.com Maç Tahminleri Scraper ve API

Bu proje, [Predictz.com](https://www.predictz.com/predictions/tomorrow/) web sitesinden yarınki futbol maç tahminlerini çeken bir web scraper ve mobil uygulamalar için API sunucusu içerir.

## Özellikler

- Yarınki futbol maçlarının verilerini çeker
- Maçların ev sahibi ve deplasman takımlarını, oranlarını, form bilgilerini ve tahminleri toplar
- Verileri CSV ve JSON dosyasına kaydeder
- Mobil uygulamalar için REST API sunucusu
- Hata yakalama ve günlük tutma özellikleri
- Otomatik veri yenileme için cron job

## Kurulum

1. Gereksinimleri yükleyin:
```
pip install -r requirements.txt
```

## Kullanım

### Scraper'ı çalıştırmak için:
```
python predictz_scraper.py
```

Bu komut, maç verilerini çekecek ve günün tarihi ile bir CSV ve JSON dosyasına kaydedecektir (örn: `predictz_matches_2023-09-13.csv` ve `predictz_matches_2023-09-13.json`).

### API Sunucusunu çalıştırmak için:
```
python api_server.py
```

Bu komut, API sunucusunu 5000 portunda başlatacaktır.

### API Sunucusunu Yönetmek İçin:

Sunucuyu arka planda başlatmak için:
```
./start_api_server.sh
```

Sunucuyu durdurmak için:
```
./stop_api_server.sh
```

### Verileri Manuel Olarak Yenilemek İçin:
```
./refresh_data.sh
```

## API Endpoints

- **GET /api/matches**: Tüm maçları getir
- **GET /api/matches/{league}**: Belirli bir lige ait maçları getir (örn: `/api/matches/Europa League Tips`)
- **GET /api/leagues**: Mevcut tüm ligleri getir
- **GET /api/refresh**: Verileri yenile (scraper'ı çalıştır)

## Ücretsiz Bulut Platformlarına Deploy Etme

Bu API'yi ücretsiz bulut platformlarında çalıştırabilirsiniz. Aşağıdaki seçenekler mevcuttur:

### 1. Render.com

Render.com'da ücretsiz olarak deploy etmek için:

```bash
./deploy_render.sh
```

Bu script, Render.com için gerekli yapılandırma dosyasını oluşturacaktır. Sonrasında:
1. https://dashboard.render.com adresine gidin
2. GitHub/GitLab hesabınızı bağlayın
3. "New Web Service" seçeneği ile repoyu deploy edin

### 2. PythonAnywhere

PythonAnywhere'e deploy etmek için:

```bash
./deploy_pythonanywhere.sh
```

Bu script, PythonAnywhere'e deploy etmek için gerekli adımları içeren bir kılavuz oluşturacaktır.

### 3. Fly.io

Fly.io'ya deploy etmek için:

```bash
./deploy_flyio.sh
```

Bu script, Fly.io için gerekli Dockerfile ve yapılandırma dosyalarını oluşturacaktır. Sonrasında Fly.io CLI'yi kullanarak deploy edebilirsiniz.

## Mobil Uygulama Entegrasyonu

Mobil uygulamanızı API sunucusuna bağlamak için:

### iOS (Swift) Örneği:
```swift
import Foundation

func fetchMatches(completion: @escaping ([Match]?, Error?) -> Void) {
    let url = URL(string: "http://your-server-ip:5000/api/matches")!
    
    URLSession.shared.dataTask(with: url) { data, response, error in
        if let error = error {
            completion(nil, error)
            return
        }
        
        guard let data = data else {
            completion(nil, NSError(domain: "", code: 0, userInfo: [NSLocalizedDescriptionKey: "No data"]))
            return
        }
        
        do {
            let matches = try JSONDecoder().decode([Match].self, from: data)
            completion(matches, nil)
        } catch {
            completion(nil, error)
        }
    }.resume()
}
```

### Android (Kotlin) Örneği:
```kotlin
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response
import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

interface ApiService {
    @GET("matches")
    fun getMatches(): Call<List<Match>>
}

val retrofit = Retrofit.Builder()
    .baseUrl("http://your-server-ip:5000/api/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val service = retrofit.create(ApiService::class.java)

fun fetchMatches() {
    service.getMatches().enqueue(object : Callback<List<Match>> {
        override fun onResponse(call: Call<List<Match>>, response: Response<List<Match>>) {
            if (response.isSuccessful) {
                val matches = response.body()
                // Verileri işle
            }
        }
        
        override fun onFailure(call: Call<List<Match>>, t: Throwable) {
            // Hata durumunu işle
        }
    })
}
```

## Çıktı

API aşağıdaki bilgileri içeren JSON formatında veri döndürür:

- Tarih
- Ev sahibi takım
- Deplasman takımı
- Lig
- Ev sahibi oranları
- Beraberlik oranları
- Deplasman oranları
- Ev sahibi form
- Deplasman form
- Tahmin

## Otomatik Veri Yenileme

Verilerin güncel kalması için bir cron job ayarlanmıştır. Bu job her gün gece yarısı (00:00) çalışır ve verileri yeniler.

Mevcut cron job ayarını görmek için:
```
crontab -l
```

Cron job ayarını değiştirmek için:
```
crontab -e
```

## Sunucu Kurulumu

API sunucusunu sürekli çalışır durumda tutmak için:

### Linux/macOS (systemd):
```
[Unit]
Description=Predictz API Server
After=network.target

[Service]
User=yourusername
WorkingDirectory=/path/to/scraper
ExecStart=/usr/bin/python3 /path/to/scraper/api_server.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Bu dosyayı `/etc/systemd/system/predictz-api.service` olarak kaydedip, aşağıdaki komutları çalıştırın:

```
sudo systemctl daemon-reload
sudo systemctl enable predictz-api
sudo systemctl start predictz-api
``` 