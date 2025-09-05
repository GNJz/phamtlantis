# Pham-Pay API Spec v0.1 (MVP)

## 공통
- Base URL: `/api/v1`
- Content-Type: `application/json`
- Auth: `Bearer <token>` (이후 WebAuthn/장치서명으로 대체)

## 1. 지갑
### POST /api/v1/wallet/create
- req: `{ "label": "optional" }`
- res: `{ "wallet_id": "w_...", "address": "0x...", "created_at": "..." }`

### GET /api/v1/wallet/balance?address=0x...
- res: `{ "address": "0x...", "balances": { "PHAM": "123.45", "JJZ": "10.0" } }`

## 2. 토큰
### POST /api/v1/token/transfer
- req: `{ "from":"0x...", "to":"0x...", "symbol":"PHAM", "amount":"1.5", "memo":"" }`
- res: `{ "tx_id":"tx_...", "status":"pending" }`

### POST /api/v1/token/mint (개인코인 발행 - 개발자용)
- req: `{ "symbol":"JJZ", "supply":"1000000" }`
- res: `{ "symbol":"JJZ", "total_supply":"1000000" }`

## 3. 연방코인 스왑(모의)
### POST /api/v1/federal/swap
- req: `{ "from_symbol":"PHAM", "to_symbol":"JJZ", "amount":"10.0" }`
- res: `{ "quote_rate":"0.95", "received":"9.5" }`

## 4. 영수증/조회
### GET /api/v1/tx/{tx_id}
- res: `{ "tx_id":"tx_...", "status":"confirmed", "block_time":"..." }`

## 에러 포맷
```json
{ "error": { "code":"INVALID_INPUT", "message":"..." } }
