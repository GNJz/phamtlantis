# Pham‑Pay API — MVP README

> **목표:** KAO 경제권 기반의 **연합 코인(₱PHAM)** + **개인 코인(Px)** 결제/정산을 위한 최소기능 제품(MVP) API.
> - 로컬 우선(Local‑first) 지갑/키 보관
> - JWT 인증 게이트(Cloudflare/JWT) 연동
> - 간편 결제 링크/QR, 연합코인 스왑, 연동 로그
> - FastAPI 백엔드 + SQLite(임시 원장) + uWSGI/uvicorn 실행

---

## 1) 설계 원칙

- **Local‑first:** 키/서명/지갑 데이터는 사용자 디바이스 보관, 서버는 동기화와 기록 백업만 수행
- **모듈화:** 네트워크, 지갑, 원장, 스왑, 게이트 분리
- **확장성:** 이후 WebAuthn, 온체인(이더리움 계열/솔라나 등) 브릿지, 콘텐츠 상점/테스트넷 연동

---

## 2) 디렉터리 구조(제안)

```
phamPAY/
 ├─ docs/
 │   └─ Pham‑Pay_API_Spec_v0.1.md         # API 상세 스펙
 ├─ src/
 │   └─ backend/
 │       ├─ main.py                        # FastAPI 엔트리
 │       ├─ routers/
 │       │   ├─ wallet.py                  # 지갑/계정
 │       │   ├─ payments.py                # 결제
 │       │   ├─ tokens.py                  # 토큰 전송
 │       │   └─ ledger.py                  # 원장/트랜잭션 조회
 │       ├─ models/
 │       │   └─ db.py                      # SQLite 모델/세션
 │       └─ security/
 │           └─ jwt.py                     # JWT 발급/검증
 ├─ README.md                              # 이 파일
 └─ requirements.txt
```

---

## 3) 빠른 시작 (로컬 개발)

```bash
# (선택) 새 가상환경
python3 -m venv .venv && source .venv/bin/activate

# 의존성
pip install fastapi uvicorn "pydantic<3" python-jose[cryptography] passlib[bcrypt] sqlmodel

# 실행
uvicorn phamPAY.src.backend.main:app --reload

# 문서
#  OpenAPI:  http://127.0.0.1:8000/docs
#  헬스체크: GET /healthz
```

---

## 4) 핵심 엔드포인트 (요약)

**지갑**
- `POST  /api/v1/wallet/create` — 지갑/계정 생성
- `GET   /api/v1/wallet/balance?address=0x...` — 잔고 조회

**결제/정산**
- `POST  /api/v1/api/pay` — 결제 생성 및 전송
- `GET   /api/v1/tx/{tx_id}` — 트랜잭션 조회

**토큰 전송/연합**
- `POST  /api/v1/token/transfer` — 토큰 전송
- `POST  /api/v1/federal/swap` — 연합코인 스왑(모의)

> 파라미터/응답 상세 포맷은 `docs/Pham‑Pay_API_Spec_v0.1.md` 참고.

---

## 5) 요청/응답 예시

**결제 생성**
```http
POST /api/v1/api/pay
Content-Type: application/json

{
  "from": "0xUSER1",
  "to":   "0xMERCHANT1",
  "amount": 12.50,
  "currency": "PHAM",
  "note": "ice-latte x2",
  "nonce": "client-ts-1736140000"
}
```
**응답**
```json
{
  "tx_id": "ppay_9d8f3e...",
  "status": "PENDING",
  "amount": 12.5,
  "fee": 0.01,
  "created_at": "2025-09-05T10:20:31Z"
}
```

**잔고 조회**
```http
GET /api/v1/wallet/balance?address=0xUSER1
```
**응답**
```json
{ "address": "0xUSER1", "PHAM": 128.75, "Px": 4000 }
```

---

## 6) 보안/인증(요약)

- **JWT 게이트**: 로그인 또는 장치 서명 성공 시 액세스 토큰 발급 → API 헤더 `Authorization: Bearer <jwt>` 사용
- **서명 정책**: 중요한 전송/결제는 **디바이스 비밀키**로 서명 후 서버에 전달(서버는 서명 검증만)
- **레이트 리밋/방화벽**: Cloudflare 또는 Nginx 레이트 리밋, IP 허용 목록
- **로그**: 모든 결제/전송/스왑 호출은 원장(Log DB)에 저장

---

## 7) 향후 로드맵

- [ ] WebAuthn 로그인
- [ ] 온체인 브릿지(테스트넷 ERC‑20 <-> PHAM)
- [ ] 결제 링크/QR 생성 API
- [ ] 상점용 대시보드(통계/정산)
- [ ] 모바일 SDK(안드/IOS) 및 라즈베리파이 샘플 앱
