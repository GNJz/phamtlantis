
# 🪙 PHAM-Pay MVP

**PHAM-Pay**는 **KAO 경제권** 기반의 **연방 코인 + 개인 코인** 결제 시스템을 구축하기 위한 MVP 프로젝트입니다.  
PHAM 및 PHAMTLANTIS 생태계에서 디지털 콘텐츠 결제, 토큰화, API 연동을 위한 핵심 인프라 역할을 합니다.

---

## 📌 프로젝트 개요
- **프로젝트명**: PHAM-Pay
- **목표**: KAO 세계관 기반 디지털 콘텐츠 결제 및 코인 거래 시스템 구축
- **스코프**:
  1. 연방 코인(PHAM) 발행 및 관리
  2. 개인 코인(Px) 연계 및 지갑 구조 설계
  3. 웹/앱 기반 간편 결제 API 제공
  4. Cloudflare 보안 및 JWT 인증 게이트 적용

---

## 🛠️ 초기 MVP 설계

### 1) 시스템 구조
```
[사용자] → [PHAM-Pay API] → [결제 게이트] → [KAO Ledger] → [콘텐츠 제공]
```

### 2) 핵심 기능
- **지갑 시스템**: PHAM 및 개인 코인(Px) 보관 및 전송
- **JWT 인증 게이트**: 퍼즐 기반 게이트 통과 후 액세스 토큰 발급
- **결제 API**: 웹/앱/쿼카 디바이스와 연동 가능한 RESTful API 설계
- **로그 & 대시보드**: 거래 기록, 통계, 사용자 활동 모니터링

---

## 📡 API 초안

> ⚠️ 아래는 **초안**입니다. 실제 구현 시 `docs/Pham-Pay_API_Spec_v0.1.md` 에서 파라미터·에러코드 확정.

### [POST] `/api/pay`
- **설명**: 결제 생성 및 전송 처리
- **Request**
```json
{
  "payer": "user_pham_id",
  "receiver": "merchant_pham_id",
  "amount": 120,
  "token": "PHAM"
}
```
- **Response**
```json
{
  "status": "success",
  "tx_hash": "0xabc123def456"
}
```

### [GET] `/api/wallet/{id}`
- **설명**: 지갑 잔액 및 코인 정보 조회
- **Response**
```json
{
  "wallet_id": "user_pham_id",
  "balance": {
    "PHAM": 420,
    "Px": 88
  }
}
```

### [POST] `/api/auth/puzzle`
- **설명**: 퍼즐 검증 후 JWT 발급
- **Response**
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## 📂 폴더 구조 (초안)
```
phamPAY/
├── README.md                 # 프로젝트 설명 (본 파일)
├── docs/
│   ├── PHAM_Research_Income_Strategy.docx
│   └── Pham-Pay_설계초안_v0.1.docx
├── src/
│   ├── backend/
│   │   ├── main.py           # FastAPI 엔트리포인트
│   │   ├── routers/
│   │   │   ├── pay.py
│   │   │   ├── wallet.py
│   │   │   └── auth.py
│   │   ├── services/
│   │   │   ├── ledger.py
│   │   │   └── jwt_gate.py
│   │   └── db/
│   │       └── sqlite.py
│   └── frontend/ (선택)
│       └── web/
└── tests/
    └── api_test.py
```

---

## 🧪 로컬 실행 (예시)
```bash
pip install fastapi uvicorn pydantic "python-jose[cryptography]" sqlite-utils
uvicorn src.backend.main:app --reload
# OpenAPI: http://127.0.0.1:8000/docs
# Health:   GET /healthz
```

---

## ✅ 체크리스트 (MVP)
- [ ] API 스펙 v0.1 확정
- [ ] `/api/pay`, `/api/wallet`, `/api/auth` 구현
- [ ] JWT 게이트 퍼즐 로직/토큰발급 연결
- [ ] SQLite 임시 원장 + 마이그레이션 스크립트
- [ ] 로그/메트릭 수집 (간단 버전)

---

## 📄 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.
