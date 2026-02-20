// 2단계: 프론트엔드 UI 개발 스크립트

document.addEventListener('DOMContentLoaded', () => {
    // DOM 요소 선택
    const inputText = document.getElementById('inputText');
    const currentCharCount = document.getElementById('currentCharCount');
    const targetSelection = document.querySelector('.target-selection');
    const convertButton = document.getElementById('convertButton');
    const outputText = document.getElementById('outputText');
    const copyButton = document.getElementById('copyButton');
    const feedbackHelpful = document.getElementById('feedbackHelpful');
    const feedbackNotHelpful = document.getElementById('feedbackNotHelpful');
    const messageArea = document.getElementById('messageArea');

    const API_ENDPOINT = '/api/convert'; // 백엔드 API 엔드포인트

    // --- 유틸리티 함수 ---

    function showMessage(message, type = 'info') {
        messageArea.textContent = message;
        messageArea.className = `message-area show ${type}`;
        // 메시지 3초 후 자동 숨김
        setTimeout(() => {
            messageArea.classList.remove('show');
            messageArea.textContent = '';
        }, 3000);
    }

    function enableButtons(enable) {
        convertButton.disabled = !enable;
        copyButton.disabled = !enable;
        feedbackHelpful.disabled = !enable;
        feedbackNotHelpful.disabled = !enable;
    }

    // --- 이벤트 핸들러 ---

    // 텍스트 입력 시 글자 수 업데이트
    inputText.addEventListener('input', () => {
        currentCharCount.textContent = inputText.value.length;
    });

    // '변환하기' 버튼 클릭 이벤트
    convertButton.addEventListener('click', async () => {
        const text = inputText.value.trim();
        const selectedTarget = targetSelection.querySelector('input[name="target"]:checked');
        
        if (!text) {
            showMessage('변환할 텍스트를 입력해주세요.', 'error');
            return;
        }
        if (!selectedTarget) {
            showMessage('변환 대상을 선택해주세요.', 'error');
            return;
        }

        const target = selectedTarget.value;
        enableButtons(false); // 버튼 비활성화
        convertButton.textContent = '변환 중...'; // 로딩 상태 표시
        outputText.value = ''; // 결과창 초기화

        try {
            const response = await fetch(API_ENDPOINT, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text, target }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            outputText.value = data.converted_text;
            showMessage('텍스트 변환 성공!', 'success');

        } catch (error) {
            console.error('변환 중 오류 발생:', error);
            showMessage(`오류 발생: ${error.message}. 잠시 후 다시 시도해주세요.`, 'error');
        } finally {
            enableButtons(true); // 버튼 다시 활성화
            convertButton.textContent = '변환하기'; // 버튼 텍스트 원상 복구
        }
    });

    // '복사하기' 버튼 클릭 이벤트
    copyButton.addEventListener('click', async () => {
        if (!outputText.value) {
            showMessage('변환된 텍스트가 없습니다.', 'error');
            return;
        }
        try {
            await navigator.clipboard.writeText(outputText.value);
            showMessage('변환된 텍스트가 클립보드에 복사되었습니다!', 'success');
        } catch (err) {
            console.error('클립보드 복사 실패:', err);
            showMessage('클립보드 복사 실패. 수동으로 복사해주세요.', 'error');
        }
    });

    // 피드백 버튼 클릭 이벤트 (간단히 메시지로 처리)
    feedbackHelpful.addEventListener('click', () => {
        showMessage('피드백 감사합니다! 서비스 개선에 반영하겠습니다.', 'success');
    });

    feedbackNotHelpful.addEventListener('click', () => {
        showMessage('더 나은 서비스를 위해 노력하겠습니다. 어떤 점이 부족했는지 알려주시면 감사하겠습니다.', 'info');
    });

    // 초기 글자 수 설정
    currentCharCount.textContent = inputText.value.length;
});
