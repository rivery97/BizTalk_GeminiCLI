# BizTone Converter 프로젝트 개요

## 프로젝트 요약
BizTone Converter는 신입사원이나 비즈니스 커뮤니케이션에 익숙하지 않은 사람들을 포함하여 개인이 일상적인 언어를 상사, 동료, 고객과 같은 다양한 대상에게 적합한 전문적인 비즈니스 톤으로 쉽고 빠르게 변환할 수 있도록 돕는 AI 기반 웹 솔루션입니다. 이 프로젝트의 목표는 커뮤니케이션 효율성을 높이고, 커뮤니케이션 품질을 표준화하며, 비즈니스 글쓰기 관련 교육 비용을 절감하는 것입니다.

## 아키텍처
이 프로젝트는 프론트엔드와 백엔드 구성 요소가 명확히 분리된 클라이언트-서버 아키텍처를 따릅니다.
-   **프론트엔드**: 직관적이고 반응성이 뛰어난 사용자 경험을 제공하기 위해 HTML, Tailwind CSS 및 JavaScript로 구축된 정적 웹 인터페이스입니다.
-   **백엔드**: RESTful API 역할을 하는 Python Flask 애플리케이션입니다. 프론트엔드의 요청을 처리하고, 텍스트 톤 변환을 위해 Groq AI API와 통신하며, 정적 프론트엔드 파일을 제공합니다.
-   **AI**: 페르소나별 프롬프트에 따라 텍스트 변환을 위해 `moonshotai/kimi-k2-instruct-0905` 모델과 함께 Groq AI API를 활용합니다.

## 사용된 기술
-   **프론트엔드**: HTML5, Tailwind CSS, JavaScript (ES6+), Fetch API
-   **백엔드**: Python, Flask, Flask-CORS, python-dotenv, Groq Python SDK
-   **AI**: Groq AI API (모델: `moonshotai/kimi-k2-instruct-0905`)
-   **개발 도구**: Git, GitHub
-   **배포 (예정)**: Vercel (정적 호스팅 및 서버리스 함수용)

## 빌드 및 실행

### 필수 구성 요소
-   Python 3.8+
-   `pip` (Python 패키지 설치 관리자)
-   Groq API 키

### 백엔드 설정 (Python Flask)

1.  **Python 가상 환경 생성**:
    프로젝트 종속성 관리를 위해 가상 환경을 생성하는 것이 좋습니다.
    ```bash
    python -m venv .venv
    ```

2.  **가상 환경 활성화**:
    *   **macOS/Linux**:
        ```bash
        source .venv/bin/activate
        ```
    *   **Windows**:
        ```bash
        .venv\Scripts\activate
        ```

3.  **종속성 설치**:
    `pip`를 사용하여 필요한 모든 Python 패키지를 설치합니다.
    ```bash
    pip install -r backend/requirements.txt
    ```

4.  **Groq API 키 구성**:
    프로젝트 루트 디렉토리 (`PRD.md` 옆)에 `.env` 파일을 생성하고 Groq API 키를 추가합니다.
    ```
    GROQ_API_KEY="your_groq_api_key_here"
    ```
    `"your_groq_api_key_here"`를 실제 Groq API 키로 교체하세요.

5.  **백엔드 서버 실행**:
    Flask 개발 서버를 시작합니다.
    ```bash
    python backend/app.py
    ```
    백엔드 서버는 일반적으로 `http://127.0.0.1:5000` (또는 `localhost:5000`)에서 실행됩니다.

### 프론트엔드
프론트엔드 파일 (`index.html`, `js/script.js`)은 Flask 백엔드에 의해 직접 제공됩니다. 백엔드 서버를 성공적으로 실행한 후 웹 브라우저를 열고 `http://127.00.1:5000`으로 이동하여 애플리케이션에 액세스합니다.

## 개발 규칙

### 코드 구조
-   프로젝트는 프론트엔드 (`frontend/`)와 백엔드 (`backend/`) 구성 요소를 별도의 디렉토리로 분리합니다.
-   프론트엔드는 표준 HTML, 스타일링을 위한 Tailwind CSS, 상호 작용을 위한 바닐라 JavaScript를 사용합니다.
-   백엔드는 라우팅 및 API 처리를 위해 Flask를 사용하며, `app.py`가 메인 진입점입니다.

### Git 워크플로우
-   PRD는 `feature -> develop -> main` 브랜치 전략을 제안합니다.

### 환경 변수
-   `GROQ_API_KEY`와 같은 민감한 정보는 `python-dotenv` 라이브러리를 통해 환경 변수로 관리되며 `.env` 파일에 저장됩니다. 이러한 변수들은 클라이언트 측에 노출되지 않습니다.

### 스타일링
-   프론트엔드는 직관성, 전문성, 효율성이라는 디자인 원칙을 준수하며, 깔끔하고 현대적이며 반응형 사용자 인터페이스를 위해 Tailwind CSS를 활용합니다.

## 이 컨텍스트를 사용하는 방법
이 `GEMINI.md` 파일은 Gemini CLI의 기본 컨텍스트 역할을 합니다. 이 프로젝트를 작업할 때 에이전트는 다음을 위해 이 문서를 참조해야 합니다.
-   전반적인 프로젝트 목표 및 기술 사양 이해
-   개발 환경 설정에 대한 지침
-   기존 아키텍처 및 기술 스택에 대한 지식
-   정의된 개발 규칙 및 스타일링 가이드라인 준수
