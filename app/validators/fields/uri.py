from marshmallow import fields
from app.constants import Web

class Uri(fields.Url):
    def __init__(self, *, relative: bool = False, require_tld: bool = True, **kwargs):
        super().__init__(relative=relative, schemes=Web.valid_schemes, require_tld=require_tld, **kwargs)