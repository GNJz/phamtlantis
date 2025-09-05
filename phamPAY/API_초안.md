# PHAM-Pay (MVP v0.1)

KAO 경제권의 연방코인(PHAM) + 개인코인 결제 시스템.
익명 지갑(WebAuthn) 기반, 로컬-우선 설계, 서버/디바이스 API 연동.

## MVP 스코프
- 지갑 생성/복구 (로컬 키 보관)
- 잔고 조회 (PHAM, 개인토큰)
- 토큰 전송 (P2P)
- 연방코인↔개인토큰 스왑(모의)
- KAO API/Quarkka 디바이스 연동 훅

## 폴더
phamPAY/  
├─ README.md  
├─ docs/  
│  └─ Pham-Pay_API_Spec_v0.1.md  
├─ src/  
│  └─ backend/  
│     └─ main.py  
└─ tests/  
## 다음 액션
1) API 스펙 초안 고정 → 2) FastAPI 엔드포인트 스텁 생성 → 3) 도메인 로직 분리
2) 
