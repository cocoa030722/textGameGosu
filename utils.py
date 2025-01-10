import json
import os

# JSON 파일 로드
def load_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def read_all_json(directory):
    json_data = {}
    try:
        # 디렉토리 내 모든 파일 탐색
        for filename in os.listdir(directory):
            if filename.endswith('.json'):  # JSON 파일만 선택
                file_path = os.path.join(directory, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    try:
                        data = json.load(file)  # JSON 파일 읽기
                        json_data[data["name"]] = (data)  # 데이터를 리스트에 추가
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in file {file_path}: {e}")
    except FileNotFoundError:
        print(f"Directory {directory} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return json_data
