"""This module defines the EmailMailer interface.
"""

# Author: Ling Thio <ling.thio@gmail.com>
# Copyright (c) 2013 Ling Thio

from __future__ import print_function

from flask_user import ConfigError


class EmailMailerInterface(object):
    """ Define the EmailMailer interface to send emails through specific email mailers."""

    def __init__(self, app):
        """
        Args:
            app(Flask): The Flask application instance.
        """
        self.sender_name = app.config.get('USER_EMAIL_SENDER_NAME', None)
        self.sender_email = app.config.get('USER_EMAIL_SENDER_EMAIL', None)

    def send_email_message(self, recipient, subject, html_message, text_message):
        """ Send email message via an email mailer.

        Args:
            recipient: Email address or tuple of (Name, Email-address).
            subject: Subject line.
            html_message: The message body in HTML.
            text_message: The message body in plain text.
        """
        raise NotImplementedError