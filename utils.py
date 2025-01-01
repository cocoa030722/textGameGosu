import json

# JSON 파일 로드
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

