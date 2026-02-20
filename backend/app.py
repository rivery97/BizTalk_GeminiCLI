import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import groq

# .env 파일에서 환경 변수 로드
load_dotenv()

app = Flask(__name__)
# 모든 도메인에서 오는 요청을 허용하도록 CORS 설정
CORS(app)

# Groq API 클라이언트 설정 (실제 API 키는 .env 파일에 저장)
# 이 단계에서는 아직 API를 직접 호출하지 않으므로, 키가 없어도 서버는 동작합니다.
try:
    client = groq.Groq(api_key=os.environ.get("GROQ_API_KEY"))
except Exception as e:
    # API 키가 설정되지 않았을 경우를 대비한 예외 처리
    print(f"Groq API 클라이언트를 초기화하는 데 실패했습니다: {e}")
    client = None

@app.route('/api/convert', methods=['POST'])
def convert_text():
    """
    텍스트 변환을 위한 API 엔드포인트입니다.
    1단계에서는 실제 변환 로직 없이 더미 응답을 반환합니다.
    """
    # 요청으로부터 데이터 추출
    data = request.get_json()
    if not data or 'text' not in data or 'target' not in data:
        return jsonify({"error": "'text'와 'target' 필드가 필요합니다."}), 400

    original_text = data.get('text')
    target = data.get('target')

    # 더미 응답 생성
    dummy_response = f"'{original_text}'를 '{target}' 대상으로 변환한 결과입니다. (이것은 더미 응답입니다.)"
    
    return jsonify({
        "original_text": original_text,
        "converted_text": dummy_response,
        "target": target
    })

@app.route('/health', methods=['GET'])
def health_check():
    """
    서버의 상태를 확인하기 위한 헬스 체크 엔드포인트입니다.
    """
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    # 디버그 모드로 Flask 앱 실행
    # 실제 프로덕션 환경에서는 Gunicorn, uWSGI 등의 WSGI 서버를 사용해야 합니다.
    app.run(debug=True, port=5000)
