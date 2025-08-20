#!/bin/bash

# PythonAnywhere deployment script

echo "PythonAnywhere için deployment hazırlanıyor..."
echo "Bu script, PythonAnywhere'e manuel olarak deploy etmek için gerekli adımları içerir."

cat > pythonanywhere_deploy_steps.txt << EOL
PythonAnywhere Deployment Adımları:

1. PythonAnywhere'de bir hesap oluşturun (https://www.pythonanywhere.com)

2. Web sekmesine gidin ve "Add a new web app" butonuna tıklayın

3. Manuel yapılandırma seçin ve Python 3.9 sürümünü seçin

4. Kod dosyalarınızı yüklemek için:
   - Dashboard'da "Files" sekmesine gidin
   - "Upload a file" butonunu kullanarak tüm dosyalarınızı yükleyin
   - Veya GitHub/GitLab reponuzu klonlamak için bir Bash konsolu açın:
     git clone https://github.com/kullaniciadi/repo-adi.git

5. Sanal ortam oluşturun:
   - Bash konsolunda:
     mkvirtualenv --python=python3.9 predictz-venv
     workon predictz-venv
     pip install -r requirements.txt

6. WSGI yapılandırma dosyasını düzenleyin:
   - Web sekmesinde "WSGI configuration file" linkine tıklayın
   - Dosyayı aşağıdaki gibi düzenleyin:

```python
import sys
import os

path = '/home/KULLANICIADI/predictz-scraper'
if path not in sys.path:
    sys.path.append(path)

from api_server import app as application
```

7. Web uygulamasını yeniden başlatın
EOL

echo "pythonanywhere_deploy_steps.txt dosyası oluşturuldu."
echo "Bu dosyadaki adımları takip ederek PythonAnywhere'e deploy edebilirsiniz." 