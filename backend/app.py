import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from groq import Groq

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
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

@app.route('/')
def index():
    """루트 URL 요청 시 frontend/index.html을 반환합니다."""
    # static_url_path가 ''로 설정되었으므로, send_static_file은
    # static_folder의 루트에서 파일을 찾습니다.
    return app.send_static_file('index.html')


@app.route('/api/convert', methods=['POST'])
def convert_tone():
    """
    사용자로부터 텍스트와 변환 대상을 받아, Groq API를 호출하여 말투를 변환합니다.
    """
    data = request.get_json()
    if not data or 'text' not in data or 'target' not in data:
        return jsonify({"error": "'text'와 'target' 필드가 필요합니다."}), 400

    user_text = data.get('text')
    target_persona = data.get('target')

    # 대상별 프롬프트 선택
    system_prompt = ""
    if target_persona == "상사":
        system_prompt = "주어진 텍스트를 상사에게 보고하는 형식의 정중하고 격식 있는 말투로 변환해 주세요. 핵심 내용을 명확하게 전달하고 보고 형식에 맞춰주세요."
    elif target_persona == "타팀 동료":
        system_prompt = "주어진 텍스트를 타팀 동료에게 협업을 요청하는 친절하고 상호 존중하는 말투로 변환해 주세요. 요청 사항과 필요 기한을 명확히 포함시켜 주세요."
    elif target_persona == "고객":
        system_prompt = "주어진 텍스트를 고객에게 안내하는 극존칭을 사용한 전문적이고 신뢰감 있는 말투로 변환해 주세요. 서비스 마인드를 강조하고 목적에 부합하는 형식으로 작성해 주세요."
    else:
        return jsonify({"error": "유효하지 않은 대상입니다."}), 400

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": system_prompt,
                },
                {
                    "role": "user",
                    "content": user_text,
                }
            ],
            model="moonshotai/kimi-k2-instruct-0905",
            temperature=0.7,
            max_tokens=500,
        )
        converted_text = chat_completion.choices[0].message.content
        return jsonify({"converted_text": converted_text})

    except Exception as e:
        app.logger.error(f"Groq API 호출 오류: {e}")
        return jsonify({"error": f"텍스트 변환 중 오류가 발생했습니다: {str(e)}"}), 500

if __name__ == '__main__':
    # 디버그 모드로 Flask 앱을 실행합니다.
    app.run(debug=True, port=5000)
