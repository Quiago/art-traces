import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to, subject, message):
    # Configura los datos de la cuenta de correo electrónico desde la que enviarás el correo.
    smtp_server = 'smtp.gmail.com'  # Cambia esto al servidor SMTP que desees usar.
    smtp_port = 587  # Puerto SMTP del servidor.
    sender_email = 'arttraces5@gmail.com'  # Tu dirección de correo electrónico.
    sender_password = 'uejo wzbu vzyc nulq'  # Tu contraseña.

    # Configura el mensaje de correo.
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to
    msg['Subject'] = subject

    # Agrega el cuerpo del mensaje.
    msg.attach(MIMEText(message, 'plain'))

    # Inicia una conexión con el servidor SMTP.
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Envía el correo.
        server.sendmail(sender_email, to, msg.as_string())
        server.quit()
        return "Correo enviado exitosamente"

    except Exception as e:
        return {"message": f"Error al enviar el correo: {str(e)}"}
