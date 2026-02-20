import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
# from groq import Groq

# .env 파일에서 환경 변수 로드
load_dotenv()

# Flask app 설정: frontend 폴더를 정적 파일의 루트로 지정
# static_folder: 정적 파일이 위치한 디렉토리 경로
# static_url_path: 웹에서 정적 파일에 접근할 때 사용될 URL 경로. ''로 설정 시 루트 경로(/)에서 접근 가능
app = Flask(__name__,
            static_folder='../frontend',
            static_url_path='')
# CORS 설정
CORS(app)

# Groq 클라이언트 초기화 (API 키는 환경 변수에서 가져옵니다)
# client = Groq(
#     api_key=os.environ.get("GROQ_API_KEY"),
# )

@app.route('/')
def index():
    """루트 URL 요청 시 frontend/index.html을 반환합니다."""
    # static_url_path가 ''로 설정되었으므로, send_static_file은
    # static_folder의 루트에서 파일을 찾습니다.
    return app.send_static_file('index.html')


@app.route('/api/convert', methods=['POST'])
def convert_tone():
    """
    사용자로부터 텍스트와 변환 대상을 받아, 더미 응답을 반환하는 API 엔드포인트입니다.
    Sprint 1 목표에 따라 초기 API 연동을 테스트하기 위한 구현입니다.
    """
    data = request.get_json()
    if not data or 'text' not in data or 'target' not in data:
        return jsonify({"error": "'text'와 'target' 필드가 필요합니다."}), 400

    user_text = data.get('text')
    target_persona = data.get('target')

    # Sprint 1: 실제 Groq API 호출 대신 더미 응답 반환
    dummy_response = {
        "original_text": user_text,
        "converted_text": f"'{user_text}'를 '{target_persona}' 대상으로 변환한 결과입니다. (이것은 더미 응답입니다.)",
        "target": target_persona
    }
    
    return jsonify(dummy_response)

if __name__ == '__main__':
    # 디버그 모드로 Flask 앱을 실행합니다.
    app.run(debug=True, port=5000)
