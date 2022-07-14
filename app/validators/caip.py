from marshmallow import Schema, fields, ValidationError, validate
from web3 import Web3
from app.constants import CAIP10

class Caip10(fields.Field):
    def _deserialize(self, value, attr, data, **kwargs):
        components = value.split(':')

        if len(components) != 3:
            raise ValidationError('CAIP-10 address must contain 3 components in the following format: <namespace:reference:account_id>')

        namespace, reference, account_address = components

        if namespace not in CAIP10.valid_chain_ids:
            raise ValidationError(f"Invalid namespace '{namespace}' must be one of {list(CAIP10.valid_chain_ids.keys())}")
        
        if reference not in CAIP10.valid_chain_ids[namespace]:
            raise ValidationError(f"Invalid reference '{reference}' for namespace '{namespace}' must be one of {list(CAIP10.valid_chain_ids[namespace])}")
        
        if namespace == "eip155":
            if not Web3.isAddress(account_address):
                raise ValidationError(f"Invalid account address '{account_address}'")
        
        return value