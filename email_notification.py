import smtplib
import os

# Email variables definition
sender = '‘example @ gmail.com’'
receiver = ['svirahonda@gmail.com']  # replace this by the owner's email address
smtp_provider = 'smtp.gmail.com'  # replace this by your STMP provider
smtp_port = 587
smtp_account = '‘example @ gmail.com’'
smtp_password = '‘your_password’'

def training_result(result, model_acc):
    if result == 'ok':
        message = 'The model reached ' + str(model_acc) + ', It has been saved to GCS.'
    if result == 'failed':
        message = "None of the models reached an acceptable accuracy, training execution had to be forcefully ended."
    message = 'Subject: {}\n\n{}'.format('An automatic training job has ended recently', message)
    try:
        server = smtplib.SMTP(smtp_provider, smtp_port)
        server.starttls()
        server.login(smtp_account, smtp_password)
        server.sendmail(sender, receiver, message)
        return
    except Exception as e:
        print('Something went wrong. Unable to send email: ' + str(e), flush=True)
        return


def exception(e_message):
    try:
        message = 'Subject: {}\n\n{}'.format('An automatic training job has failed.', e_message)
        server = smtplib.SMTP(smtp_provider, smtp_port)
        server.starttls()
        server.login(smtp_account, smtp_password)
        server.sendmail(sender, receiver, message)
        return
    except Exception as e:
        print('Something went wrong. Unable to send email: ' + str(e), flush=True)
        return