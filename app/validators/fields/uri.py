from marshmallow import fields
from app.constants import Web

# alias for fields.Url, sets schemes to those defined in constants
class Uri(fields.Url):
    default_error_messages = {"invalid": "Not a valid URI."}

    def __init__(self, **kwargs):
        super().__init__(relative=False, schemes=Web.valid_schemes, require_tld=False, **kwargs)