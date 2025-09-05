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

## 3) `phamPAY/src/backend/main.py` (FastAPI 스켈레톤)
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict
import uuid
from datetime import datetime

app = FastAPI(title="PHAM-Pay API", version="0.1")

# ---- Models ----
class CreateWalletReq(BaseModel):
    label: Optional[str] = None

class TransferReq(BaseModel):
    from_: str
    to: str
    symbol: str
    amount: str
    memo: Optional[str] = ""

class SwapReq(BaseModel):
    from_symbol: str
    to_symbol: str
    amount: str

# ---- In-memory store (MVP mock) ----
WALLETS: Dict[str, Dict] = {}
BALANCES: Dict[str, Dict[str, float]] = {}
TXS: Dict[str, Dict] = {}

# ---- Helpers ----
def new_addr() -> str:
    return "0x" + uuid.uuid4().hex[:40]

# ---- Routes ----
@app.post("/api/v1/wallet/create")
def create_wallet(req: CreateWalletReq):
    wid = "w_" + uuid.uuid4().hex[:8]
    addr = new_addr()
    WALLETS[wid] = {"wallet_id": wid, "address": addr, "label": req.label, "created_at": datetime.utcnow().isoformat()}
    BALANCES.setdefault(addr, {"PHAM": 100.0})  # faucet for MVP
    return WALLETS[wid]

@app.get("/api/v1/wallet/balance")
def get_balance(address: str):
    if address not in BALANCES:
        raise HTTPException(404, "wallet not found")
    return {"address": address, "balances": BALANCES[address]}

@app.post("/api/v1/token/transfer")
def transfer(req: TransferReq):
    if req.from_ not in BALANCES or req.to not in BALANCES:
        raise HTTPException(404, "address not found")
    amt = float(req.amount)
    if BALANCES[req.from_].get(req.symbol, 0.0) < amt:
        raise HTTPException(400, "insufficient funds")
    BALANCES[req.from_][req.symbol] -= amt
    BALANCES[req.to][req.symbol] = BALANCES[req.to].get(req.symbol, 0.0) + amt
    tx_id = "tx_" + uuid.uuid4().hex[:10]
    TXS[tx_id] = {"tx_id": tx_id, "status": "confirmed", "memo": req.memo}
    return {"tx_id": tx_id, "status": "pending"}

@app.post("/api/v1/federal/swap")
def swap(req: SwapReq):
    # mock: 고정 레이트 0.95
    rate = 0.95
    received = float(req.amount) * rate
    return {"quote_rate": str(rate), "received": f"{received:.6f}"}

@app.get("/api/v1/tx/{tx_id}")
def get_tx(tx_id: str):
    if tx_id not in TXS:
        raise HTTPException(404, "tx not found")
    return TXS[tx_id]
