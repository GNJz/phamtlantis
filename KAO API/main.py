from fastapi import FastAPI
from typing import List

app = FastAPI(title="KAO Mini API")

# 메모리(임시) 저장소 ─ 서버 재시작하면 초기화됨
IDOLS: List[str] = []
VOTES = {}  # {"아이돌명": 득표수}

@app.get("/")
def index():
    return {
        "msg": "KAO Mini API up ✅",
        "try": ["/docs", "/health", "/idol/{name}", "/vote/{name}", "/leaderboard"]
    }

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/idol/{name}")
def create_idol(name: str):
    """아이돌 등록 (이름만)"""
    if name in IDOLS:
        return {"msg": "이미 있음", "name": name}
    IDOLS.append(name)
    VOTES[name] = 0
    return {"msg": "생성", "name": name}

@app.post("/vote/{name}")
def vote(name: str):
    """특정 아이돌에 1표"""
    if name not in VOTES:
        return {"error": "없는 아이돌"}
    VOTES[name] += 1
    return {"name": name, "votes": VOTES[name]}

@app.get("/leaderboard")
def leaderboard():
    """득표 순위 조회"""
    ranks = sorted(VOTES.items(), key=lambda x: x[1], reverse=True)
    return [{"rank": i+1, "name": n, "votes": v} for i, (n, v) in enumerate(ranks)]