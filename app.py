from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="tr">
    <head>
        <meta charset="UTF-8">
        <title>Ahmet Utku Can - Kimsebaşgöz</title>
        <style>
            body {
                margin: 0;
                padding: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-image: url('https://raw.githubusercontent.com/kbgyazilim46/Yenisite/main/background.jpg'); /* Burayı kendi fotoğraf URL’inle değiştir */
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
                color: #fff;
            }
            .overlay {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 30px;
                max-width: 800px;
                margin: 50px auto;
                border-radius: 12px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.5);
            }
            h1, h3 {
                color: #ffcc00;
                text-align: center;
                text-shadow: 1px 1px 4px #000;
            }
            p, li {
                font-size: 18px;
                line-height: 1.6;
                font-weight: 500;
                text-shadow: 1px 1px 2px #000;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                background: rgba(255, 255, 255, 0.1);
                padding: 10px;
                margin: 6px 0;
                border-radius: 6px;
            }
            .contact {
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="overlay">
            <h1>Ahmet Utku Can</h1>
            <p><strong>Bilgi:</strong><br>
            Ahmet Utku Can, yani sanal adıyla <strong>Kimsebaşgöz</strong>, 2016 yılında sanala giriş yapmıştır.
            Şu anda <strong>Kimsebaşgöz</strong> ve <strong>Pars Family</strong> kurucusu olarak sanalda gezmektedir.</p>

            <h3>İlgi Alanları</h3>
            <ul>
                <li>Sanal Yaşam</li>
                <li>Topluluk Yönetimi</li>
                <li>Kimlik ve Rol Geliştirme</li>
            </ul>

            <h3>İletişim</h3>
            <div class="contact">
                <p><strong>Instagram:</strong></p>
                <ul>
                    <li>@_pars.bas.krc.kimsebasgoz</li>
                    <li>@_kimsebasgoz.her.da1m_</li>
                </ul>
                <p><strong>WhatsApp:</strong> +639092363984</p>
                <p><strong>E-posta:</strong> kimsebasgozedemez@gmail.com</p>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run()