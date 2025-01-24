"""
코드 내에서 많이 쓰이는 스니펫들의 모음입니다.
"""
import json
import os
import inspect

# JSON 파일 로드
def load_json(file_path:str) -> dict:
    """
    하나의 json을 딕셔너리로 반환합니다.
    """
    with open(file_path, "r", encoding='utf-8') as file:
        return json.load(file)

def read_all_json(directory:str) -> dict:
    """
    특정 디렉토리 내의 모든 json을 읽어들이고, 각 json에서 나온 딕셔너리를 하나의 딕셔너리에 담아 반환합니다.
    """
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
def load_json(file_path: str) -> Union[FocusTree, ItemDict, Boss]:
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
