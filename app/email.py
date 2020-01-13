from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread

import boto3
from botocore.exceptions import ClientError
from flask import current_app


def _send_email(client, sender, recipients, msg):
    try:
        # Provide the contents of the email.
        response = client.send_raw_email(
            Source=sender,
            Destinations=recipients,
            RawMessage={"Data": msg.as_string(),},
        )
        # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response["Error"]["Message"])
    else:
        print("Email sent! Message ID:")
        print(response["MessageId"])


def send_async_email(app, client, sender, recipients, msg):
    with app.app_context():
        _send_email(client, sender, recipients, msg)


def send_email(
    subject, sender, recipients, text_body, html_body, attachments=None, sync=False,
):
    ses = boto3.client(
        "ses",
        region_name=current_app.config["SES_REGION_NAME"],
        aws_access_key_id=current_app.config["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=current_app.config["AWS_SECRET_ACCESS_KEY"],
    )

    if not sender:
        sender = current_app.config["SES_EMAIL_SOURCE"]

    # The full path to the file that will be attached to the email.
    # ATTACHMENT = "path/to/customers-to-contact.xlsx"

    # The character encoding for the email.
    CHARSET = "utf-8"

    # Create a multipart/mixed parent container.
    msg = MIMEMultipart("mixed")

    # Add subject, from and to lines.
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = ", ".join(recipients)

    # Create a multipart/alternative child container.
    msg_body = MIMEMultipart("alternative")

    # Encode the text and HTML content and set the character encoding. This step is
    # necessary if you're sending a message with characters outside the ASCII range.
    textpart = MIMEText(text_body.encode(CHARSET), "plain", CHARSET)
    htmlpart = MIMEText(html_body.encode(CHARSET), "html", CHARSET)

    # Add the text and HTML parts to the child container.
    msg_body.attach(textpart)
    msg_body.attach(htmlpart)

    # Attach the multipart/alternative child container to the multipart/mixed
    # parent container.
    msg.attach(msg_body)

    # Add the attachment to the parent container.
    if attachments:
        for idx, attachment in enumerate(attachments):
            data, mime_type = attachment
            part = MIMEApplication(data)
            part.add_header("Content-Disposition", "attachment", filename=f"posts.json")
            msg.attach(part)

    if sync:
        _send_email(ses, sender, recipients, msg)
    else:
        Thread(
            target=send_async_email,
            args=(current_app._get_current_object(), sender, recipients, msg),
        ).start()

    # Just a simple email - no attachments
    # ses.send_email(
    #     Source=sender,
    #     Destination={'ToAddresses': recipients},
    #     Message={
    #         'Subject': {'Data': subject},
    #         'Body': {
    #             'Text': {'Data': text_body},
    #             'Html': {'Data': html_body}
    #         }
    #     }
    # )
