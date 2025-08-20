#!/bin/bash

# Render.com deployment script

echo "Render.com için deployment hazırlanıyor..."

# Render.com için gerekli dosyayı oluştur
cat > render.yaml << EOL
services:
  - type: web
    name: predictz-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python api_server.py
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.0
EOL

echo "render.yaml dosyası oluşturuldu."
echo "Şimdi https://dashboard.render.com adresine gidip GitHub/GitLab hesabınızı bağlayın."
echo "Sonra 'New Web Service' seçeneğini kullanarak bu repoyu deploy edebilirsiniz." 