
from datetime import datetime
from typing import Optional, List

from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field, Session, create_engine, select, col

DB_URL = "sqlite:///./kao.db"  # 프로젝트 폴더에 kao.db 생성
engine = create_engine(DB_URL, echo=False)

# ---------- Models ----------
class Idol(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    votes: int = Field(default=0)
    created_at: datetime = Field(default_factory=datetime.utcnow)

# ---------- App ----------
app = FastAPI(title="KAO Mini API (SQLite)")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

@app.get("/")
def index():
    return {"msg": "KAO API (SQLite) up ✅", "try": ["/docs", "/health", "/idol/{name}", "/vote/{name}", "/leaderboard"]}

@app.get("/health")
def health():
    return {"status": "OK"}

# 아이돌 생성 (이름 중복 방지)
@app.post("/idol/{name}")
def create_idol(name: str):
    name = name.strip()
    if not name:
        raise HTTPException(400, "name required")
    with Session(engine) as s:
        exists = s.exec(select(Idol).where(col(Idol.name) == name)).first()
        if exists:
            return {"msg": "이미 있음", "name": name, "id": exists.id, "votes": exists.votes}
        idol = Idol(name=name)
        s.add(idol)
        s.commit()
        s.refresh(idol)
        return {"msg": "생성", "id": idol.id, "name": idol.name, "votes": idol.votes}

# 투표 (없는 아이돌이면 오류)
@app.post("/vote/{name}")
def vote(name: str):
    with Session(engine) as s:
        idol = s.exec(select(Idol).where(col(Idol.name) == name)).first()
        if not idol:
            raise HTTPException(404, "없는 아이돌")
        idol.votes += 1
        s.add(idol)
        s.commit()
        s.refresh(idol)
        return {"name": idol.name, "votes": idol.votes}

# 리더보드 (득표수 내림차순 Top 50)
@app.get("/leaderboard")
def leaderboard(limit: int = 50):
    with Session(engine) as s:
        rows: List[Idol] = s.exec(
            select(Idol).order_by(Idol.votes.desc(), Idol.created_at.asc()).limit(limit)
        ).all()
        return [{"rank": i + 1, "name": r.name, "votes": r.votes} for i, r in enumerate(rows)]