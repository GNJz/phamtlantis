# PHAM-Pay (MVP v0.1)

KAO 경제권을 위한 **연방코인(PHAM) + 개인코인** 결제 시스템의 최소기능제품(MVP).
로컬 우선(local-first) 설계, 지갑/송금/스왑(모의) 기능부터 시작합니다.

---

## 0. 왜 PHAM-Pay인가
- **연방코인(PHAM)**: 공통 결제 단위
- **개인코인**: 크리에이터/개별 서비스 단위 토큰
- **목표**: 서버 없이도 동작 가능한 로컬 지갑을 기본으로, 필요 시 서버 동기화

---

## 1. MVP 범위 (v0.1)
- [x] 지갑 생성(모의), 잔고 조회
- [x] 토큰 전송(P2P, 모의 장부)
- [x] PHAM ↔ 개인토큰 스왑 **견적/모의 체결**
- [x] 트랜잭션 조회
- [ ] WebAuthn/디바이스 서명(다음 버전)
- [ ] 실제 체인 연동(테스트넷/사설체인)

---

## 2. 폴더 구조

phamPAY/  
├─ README.md  
├─ docs/  
│  └─ Pham-Pay_API_Spec_v0.1.md   # API 상세 스펙  
├─ src/  
│  └─ backend/  
│     └─ main.py                   # FastAPI 엔드포인트(모의 로직)  
└─ tests/                          # 추후 테스트 코드  

---

## 3. 빠른 시작 (로컬 실행)

### 의존성
```bash
pip install fastapi uvicorn
uvicorn phamPAY.src.backend.main:app --reload
문서/테스트
	•	OpenAPI: http://127.0.0.1:8000/docs
	•	헬스체크(추가 시): GET /healthz

⸻

4. 핵심 엔드포인트 (요약)

상세 파라미터와 응답 포맷은 docs/Pham-Pay_API_Spec_v0.1.md 참고
기능
메서드
경로
지갑 생성
POST
/api/v1/wallet/create
잔고 조회
GET
/api/v1/wallet/balance?address=0x...
토큰 전송
POST
/api/v1/token/transfer
연방코인 스왑(모의)
POST
/api/v1/federal/swap
트랜잭션 조회
GET
/api/v1/tx/{tx_id}

기능
메서드
경로
지갑 생성
POST
/api/v1/wallet/create
잔고 조회
GET
/api/v1/wallet/balance?address=0x...
토큰 전송
POST
/api/v1/token/transfer
연방코인 스왑(모의)
POST
/api/v1/federal/swap
트랜잭션 조회
GET
/api/v1/tx/{tx_id}
### 다음 액션
1) `phamPAY/README.md`를 위 내용으로 덮어쓰기  
2) `docs/Pham-Pay_API_Spec_v0.1.md`와 `src/backend/main.py`도 이어서 커밋하면 완성도가 확 올라가요.

