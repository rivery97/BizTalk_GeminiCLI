# Backend (백엔드) GEMINI.md

## 백엔드 개요
이 디렉토리에는 BizTone Converter 애플리케이션의 백엔드 서비스가 포함되어 있습니다. Python Flask 프레임워크를 기반으로 구축되었으며, 주요 역할은 다음과 같습니다:
-   프론트엔드로부터 텍스트 변환 요청을 수신합니다.
-   Groq AI API를 호출하여 입력 텍스트를 대상 페르소나(상사, 타팀 동료, 고객)에 맞춰 변환합니다.
-   변환된 텍스트를 프론트엔드로 반환합니다.
-   정적 프론트엔드 파일(HTML, CSS, JS)을 제공하여 웹 애플리케이션을 호스팅합니다.

## 주요 파일
-   `app.py`: Flask 애플리케이션의 메인 엔트리 포인트입니다.
    -   `/` (루트) 경로 요청 시 `frontend/index.html`을 제공합니다.
    -   `/api/convert` API 엔드포인트를 처리하여 텍스트 변환 로직(Groq API 호출 포함)을 수행합니다.
    -   대상 페르소나에 따른 프롬프트 엔지니어링 로직이 포함되어 있습니다.
-   `requirements.txt`: 이 백엔드 서비스가 의존하는 모든 Python 패키지 목록을 포함합니다.

## 사용된 기술
-   **언어**: Python
-   **웹 프레임워크**: Flask
-   **API 클라이언트**: Groq Python SDK
-   **환경 변수 관리**: `python-dotenv`
-   **CORS**: `Flask-CORS` (프론트엔드와의 교차 출처 리소스 공유를 허용)

## API 엔드포인트

### `POST /api/convert`
-   **설명**: 사용자로부터 원문 텍스트와 변환 대상을 받아, Groq AI를 통해 텍스트의 말투를 변환합니다.
-   **메서드**: `POST`
-   **요청 본문 (JSON)**:
    ```json
    {
        "text": "변환하고자 하는 원문 텍스트",
        "target": "변환 대상 (예: 상사, 타팀 동료, 고객)"
    }
    ```
-   **응답 본문 (JSON)**:
    -   **성공 (200 OK)**:
        ```json
        {
            "converted_text": "변환된 텍스트"
        }
        ```
    -   **클라이언트 오류 (400 Bad Request)**:
        `'text'와 'target' 필드가 필요합니다.` 또는 `유효하지 않은 대상입니다.`
    -   **서버 오류 (500 Internal Server Error)**:
        `텍스트 변환 중 오류가 발생했습니다: [오류 메시지]`

## 백엔드 설정 및 실행

### 필수 구성 요소
-   Python 3.8+
-   `pip` (Python 패키지 설치 관리자)
-   Groq API 키

### 단계별 설정
1.  **가상 환경 생성 및 활성화**:
    프로젝트 루트 디렉토리에서 가상 환경을 생성하고 활성화합니다.
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

2.  **종속성 설치**:
    `backend/requirements.txt`에 명시된 모든 Python 패키지를 설치합니다.
    ```bash
    pip install -r backend/requirements.txt
    ```

3.  **Groq API 키 구성**:
    프로젝트 루트 디렉토리에 `.env` 파일을 생성하고 `GROQ_API_KEY`를 설정합니다.
    ```
    GROQ_API_KEY="your_groq_api_key_here"
    ```
    `"your_groq_api_key_here"`를 실제 Groq API 키로 교체하세요.

4.  **백엔드 서버 실행**:
    Flask 개발 서버를 시작합니다.
    ```bash
    python backend/app.py
    ```
    서버는 `http://127.0.0.1:5000`에서 수신 대기하며, 프론트엔드 파일도 이 주소를 통해 제공됩니다.

## 개발 규칙 및 고려사항
-   **환경 변수**: 민감한 API 키는 `.env` 파일을 통해 환경 변수로 관리됩니다.
-   **오류 처리**: API 요청 시 유효성 검사 및 Groq API 호출 중 발생하는 예외에 대한 기본적인 오류 처리가 구현되어 있습니다.
-   **로깅**: `app.logger.error`를 사용하여 서버 측 오류를 기록합니다.

## 이 컨텍스트를 사용하는 방법
이 `backend/GEMINI.md` 파일은 Gemini CLI가 `backend/` 디렉토리에서 작업할 때 필요한 특정 컨텍스트를 제공합니다. 백엔드 관련 작업을 수행할 때 이 문서를 참조하여 다음 사항을 파악할 수 있습니다:
-   백엔드 서비스의 기능 및 책임
-   백엔드 코드 구조 및 주요 파일
-   백엔드 설정 및 실행 방법
-   사용 가능한 API 엔드포인트 및 통신 방식
-   개발 시 고려해야 할 규칙 및 모범 사례
