import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ==========================================
# KONFIGURACJA NADACU I SERWERA SMTP
# ==========================================
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # Port dla SSL
SENDER_EMAIL = "twoj_email@gmail.com"
SENDER_PASSWORD = "twoje_haslo_aplikacji"  # Hasło aplikacji Gmail (App Password)

# ==========================================
# LISTA ODBIORCÓW
# ==========================================
RECIPIENTS = [
    {"name": "Jan", "email": "jan.kowalski@example.com"},
    {"name": "Anna", "email": "anna.nowak@example.com"}
]

# ==========================================
# SZABLON MAILA (HTML)
# ==========================================
def generate_html_newsletter(name):
    return f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gorąca promocja w Domino's Pizza!</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: 20px auto;
                background-color: #ffffff;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }}
            .header {{
                background-color: #006491;
                color: #ffffff;
                text-align: center;
                padding: 20px;
            }}
            .header h1 {{
                margin: 0;
                font-size: 28px;
                letter-spacing: 1px;
            }}
            .content {{
                padding: 30px 20px;
                color: #333333;
                line-height: 1.6;
            }}
            .promo-box {{
                background-color: #e21836;
                color: #ffffff;
                text-align: center;
                padding: 20px;
                border-radius: 6px;
                margin: 20px 0;
            }}
            .promo-box h2 {{
                margin: 0 0 10px 0;
                font-size: 24px;
            }}
            .code {{
                display: inline-block;
                background-color: #ffffff;
                color: #e21836;
                font-weight: bold;
                font-size: 22px;
                padding: 10px 20px;
                border-radius: 4px;
                letter-spacing: 2px;
                margin-top: 10px;
            }}
            .button-container {{
                text-align: center;
                margin-top: 25px;
            }}
            .btn {{
                background-color: #006491;
                color: #ffffff !important;
                padding: 14px 28px;
                text-decoration: none;
                font-weight: bold;
                border-radius: 5px;
                display: inline-block;
            }}
            .footer {{
                background-color: #f8f9fa;
                padding: 15px;
                text-align: center;
                font-size: 12px;
                color: #777777;
                border-top: 1px solid #eeeeee;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Domino's Pizza</h1>
            </div>
            <div class="content">
                <p>Cześć <strong>{name}</strong>!</p>
                <p>Masz ochotę na coś pysznego? Mamy dla Ciebie specjalną okazję na ten tydzień!</p>
                
                <div class="promo-box">
                    <h2>DRUGA PIZZA -50%</h2>
                    <p>Zamów dowolną dużą pizzę, a drugą otrzymasz za połowę ceny!</p>
                    <div class="code">KOD: PIZZA50</div>
                </div>

                <p>Oferta obowiązuje przy zamówieniach online na dostawę oraz z odbiorem osobistym.</p>
                
                <div class="button-container">
                    <a href="https://www.dominospizza.pl" class="btn">ZAMÓW TERAZ</a>
                </div>
            </div>
            <div class="footer">
                <p>Otrzymujesz ten e-mail, ponieważ zapisano Cię do newslettera Domino's Pizza.</p>
                <p>Jeśli nie chcesz otrzymywać więcej wiadomości, kliknij tutaj, aby zrezygnować.</p>
            </div>
        </div>
    </body>
    </html>
    """

# ==========================================
# LOGIKA WYSYŁANIA E-MAILI
# ==========================================
def send_newsletter():
    context = ssl.create_default_context()

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print("Pomyślnie zalogowano do serwera SMTP.")

            for recipient in RECIPIENTS:
                message = MIMEMultipart("alternative")
                message["Subject"] = "🍕 Twój kod rabatowy na pizzę w Domino's!"
                message["From"] = f"Domino's Pizza <{SENDER_EMAIL}>"
                message["To"] = recipient["email"]

                html_content = generate_html_newsletter(recipient["name"])
                message.attach(MIMEText(html_content, "html"))

                server.sendmail(SENDER_EMAIL, recipient["email"], message.as_string())
                print(f"Wysłano newsletter do: {recipient['name']} ({recipient['email']})")

    except Exception as e:
        print(f"Błąd podczas wysyłania wiadomości: {e}")

if __name__ == "__main__":
    send_newsletter()
