import json

def parse_json_file(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def get_all_mp4_url(filepath):
    data = parse_json_file(filepath)
    return [item["mp4"] for item in data["videos"]]