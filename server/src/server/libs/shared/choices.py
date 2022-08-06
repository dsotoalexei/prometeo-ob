from django.db import models


class ResponseStatusChoice(models.TextChoices):
    """Login status choices

    SELECT_CLIENT: It is necessary to select a client
    WRONG_CREDENTIALS: Invalid username or password
    MISSING_CREDENTIALS: Missing credential field
    LOGGED_IN: Successfully logged in
    INTERACTION_REQUIRED: Some kind of interactive login is required, could be a captcha or a security question
    ERROR = "error"
    LOGGED_OUT = "log_out"
    """
    SELECT_CLIENT = "select_client"
    WRONG_CREDENTIALS = "wrong_credentials"
    MISSING_CREDENTIALS = "missing_credentials"
    LOGGED_IN = "logged_in"
    INTERACTION_REQUIRED = "interaction_required"
    ERROR = "error"
    LOGGED_OUT = "logged_out"
