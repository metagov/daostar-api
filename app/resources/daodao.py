from flask import Flask, jsonify, request
from app.constants import DaoDao
import requests

def fetch_juno_daos():
    limit = request.args.get('limit', '500')  # Default limit to 500 if not specified
    url = f"{DaoDao.JUNO_URL}?limit={limit}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DaoDao.API_KEY}"
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json()), response.status_code

def fetch_osmosis_daos():
    limit = request.args.get('limit', '500')  # Default limit to 500 if not specified
    url = f"{DaoDao.OSMOSIS_URL}?limit={limit}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DaoDao.API_KEY}"
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json()), response.status_code

def fetch_stargaze_daos():
    limit = request.args.get('limit', '500')  # Default limit to 500 if not specified
    url = f"{DaoDao.STARGAZE_URL}&limit={limit}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DaoDao.SEARCH_API_KEY}"
    }
    response = requests.get(url, headers=headers)
    return jsonify(response.json()), response.status_code


