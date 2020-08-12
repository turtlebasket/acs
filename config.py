from json import load as json_load
with open("config.json", "r") as cfg_file:
    cfg = json_load(cfg_file)