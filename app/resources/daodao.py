from flask import Flask, jsonify
from app.constants import DaoDao
import requests

def fetch_juno_daos():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DaoDao.API_KEY}"
    }
    response = requests.get(DaoDao.JUNO_URL, headers=headers)
    return jsonify(response.json()), response.status_code

def fetch_osmosis_daos():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DaoDao.API_KEY}"
    }
    response = requests.get(DaoDao.OSMOSIS_URL, headers=headers)
    return jsonify(response.json()), response.status_code

def fetch_stargaze_daos():
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DaoDao.SEARCH_API_KEY}"
    }
    response = requests.get(DaoDao.STARGAZE_URL, headers=headers)
    return jsonify(response.json()), response.status_code


