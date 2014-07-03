# -*- coding: utf8 -*-
# author: Gonzalo Chacaltana @gchacaltanab
import mailer

sender = mailer.Mailer(
        host='smtp.domain.org',
        port=587,
        use_tls=True,
        usr='postmaster@domain.org',
        pwd='**********'
    )

email_subject = "Mensaje de Prueba"
email_to = "gchacaltanab@outlook.com"
email_from = "noreply@domain.org"
email_body = ""
email_html = "<h1>Mensaje enviado con Python</h1>"

message = mailer.Message(
        Subject= email_subject.encode('utf-8'),
        To=email_to,
        From=email_from,
        Body=email_body,
        Html=email_html
    )

sender.send(message)
