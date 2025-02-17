# Powered By @Teams_devil @misterjack18

import os
from typing import List

import yaml

languages = {}
commands = {}


def get_command(value: str) -> List:
    return commands["command"][value]


def get_string(lang: str):
    return languages[lang]


for filename in os.listdir(r"./Devil/strings"):
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        commands[language_name] = yaml.safe_load(
            open(r"./Devil/strings/" + filename, encoding="utf8")
        )


for filename in os.listdir(r"./Devil/strings/langs/"):
    if "en" not in languages:
        languages["en"] = yaml.safe_load(
            open(r"./Devil/strings/langs/en.yml", encoding="utf8")
        )
    if filename.endswith(".yml"):
        language_name = filename[:-4]
        if language_name == "en":
            continue
        languages[language_name] = yaml.safe_load(
            open(r"./Devil/strings/langs/" + filename, encoding="utf8")
        )
        for item in languages["en"]:
            if item not in languages[language_name]:
                languages[language_name][item] = languages["en"][item]

