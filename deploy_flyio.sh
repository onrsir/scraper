#!/bin/bash

# Fly.io deployment script

echo "Fly.io için deployment hazırlanıyor..."

# Fly.io için gerekli Dockerfile oluştur
cat > Dockerfile << EOL
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "api_server.py"]
EOL

# Fly.io yapılandırma dosyası
cat > fly.toml << EOL
app = "predictz-api"
primary_region = "ams"

[build]
  dockerfile = "Dockerfile"

[http_service]
  internal_port = 5000
  force_https = true
  auto_stop_machines = true
  auto_start_machines = true
  min_machines_running = 0

[[vm]]
  cpu_kind = "shared"
  cpus = 1
  memory_mb = 256
EOL

echo "Dockerfile ve fly.toml dosyaları oluşturuldu."
echo "Fly.io CLI'yi yüklemek için: curl -L https://fly.io/install.sh | sh"
echo "Sonra şu komutları çalıştırın:"
echo "  flyctl auth login"
echo "  flyctl launch"
echo "  flyctl deploy" 