from flask import request
from flask_restful import abort
from marshmallow import ValidationError
from app.validators.fields import Caip10

def validate_json():
    data = request.get_json(force=True, silent=True)
    if not data: abort(400, message='Invalid JSON body')
    return data

def load_schema(SchemaClass, data):
    try:
        return SchemaClass().load(data)
    except ValidationError as error:
        abort(400, errors=error.messages)

def dump_schema(SchemaClass, obj):
    return SchemaClass().dump(obj)

def validate_schema(SchemaClass, data):
    errors = SchemaClass().validate(data)
    if errors: abort(400, errors=errors)

def validate_caip(caip):
    try:
        Caip10().deserialize(caip)
    except ValidationError as error:
        abort(400, errors=error.messages)