from flask import Flask
import json
import requests
import re

app = Flask(__name__)

@app.route('/character_list')
def home():
    base_url = "https://github.com/yuanyan3060/Arknights-Bot-Resource/raw/main/gamedata/excel/character_table.json"
    character_table = requests.get(base_url).json()
    char_list = {}
    for key in character_table.keys():
        if re.match("notchar",character_table[key]["subProfessionId"]) is False:
            char_list[key] = character_table[key]["name"]
    response = json.dumps(char_list)
    return response,200,{"Content-Type":"application/json"}

@app.route('/about')
def about():
    return 'About'