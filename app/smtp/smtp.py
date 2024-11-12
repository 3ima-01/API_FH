import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from app.config import settings
from app.exceptions import SMTPException


async def send_confirmation_code(email: str, subject: str, message: str):
    try:
        msg = MIMEMultipart()
        msg["From"] = settings.SMTP_USER
        msg["To"] = email
        msg["Subject"] = subject

        html = f"""
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Код регистрации</title>
        </head>
        <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; height: 100vh;">
            <div class="email-container" style="background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); width: 100%; text-align: center;">
                <h1 style="color: #333;">Добро пожаловать!</h1>
                <p style="font-size: 16px; color: #555;">Для завершения регистрации, используйте следующий код:</p>
                <div class="code" style="font-size: 24px; font-weight: bold; color: #4CAF50; margin: 20px 0;">{message}</div>
                <p style="font-size: 16px; color: #555;">Введите этот код в соответствующее поле, чтобы продолжить процесс регистрации.</p>
                <p class="footer" style="font-size: 12px; color: #888; margin-top: 20px;">Если вы не запрашивали этот код, проигнорируйте это сообщение.</p>
            </div>
        </body>
        </html>
        """
        msg.attach(MIMEText(html, "html", "utf-8"))

        server = smtplib.SMTP_SSL("smtp.mail.ru", settings.SMTP_PORT)
        server.login(settings.SMTP_USER, settings.SMTP_PASS)
        server.send_message(msg)
        server.quit()

    except Exception as e:
        raise SMTPException
