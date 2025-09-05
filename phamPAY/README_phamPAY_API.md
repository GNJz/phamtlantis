# Pham-Pay API 설계 초안

## 1. 개요
Pham-Pay는 **KAO 경제권 연동형 결제 시스템**의 MVP입니다.  
PHAM 코인을 기반으로 한 **연결형 개인 코인 시스템**을 지원합니다.

---

## 2. 핵심 기능
- **PHAM 코인 결제**: 기본 결제 단위
- **개인 코인 연계**: KAO 계정 지갑과 연결
- **익명 인증**: 개인정보 없이 지갑 인증
- **PHAM-Pay API**: 콘텐츠·아이템·서비스 구매 연동

---

## 3. API 엔드포인트 초안

### 3.1 사용자 인증
`POST /api/v1/auth`
- **설명**: 지갑 또는 개인 코인 키로 인증
- **Body 예시**
```json
{
  "wallet_id": "0x1234abcd...",
  "signature": "abcdef123456..."
}
```

### 3.2 결제 생성
`POST /api/v1/payment/create`
- **설명**: PHAM 또는 개인 코인 결제 생성
- **Body 예시**
```json
{
  "payer_id": "user123",
  "receiver_id": "pham_store_001",
  "amount": 15.75,
  "currency": "PHAM"
}
```

### 3.3 결제 상태 조회
`GET /api/v1/payment/:id`
- **설명**: 결제 트랜잭션 상태 조회

---

## 4. API 아키텍처
- **백엔드**: FastAPI + Python
- **DB**: PostgreSQL
- **토큰**: JWT 기반 인증
- **지갑 연동**: Web3 라이브러리 활용

---

## 5. 다음 단계
- [ ] API 스펙 세부 설계
- [ ] 테스트 지갑 및 PHAM 네트워크 구축
- [ ] MVP 백엔드 서버 배포
