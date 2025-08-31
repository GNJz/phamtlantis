
# 🌐 KAO Mini API (Open Collaboration)

> **누구나 함께 만드는 아이돌 투표·리더보드 API**  
> MVP 단계부터 전 세계 기여자와 함께 개발하며, 첫 1년 수익을 기여 지분에 따라 분배합니다.

---

## 📌 프로젝트 개요
KAO Mini API는 간단한 아이돌 생성, 투표, 리더보드 기능을 제공하는 **FastAPI 기반 오픈소스 백엔드**입니다.  
이 프로젝트는 오픈 콜라보레이션으로 개발되며, 서비스가 상용화되면 **첫 1년 순수익의 일부를 기여자에게 분배**합니다.

---

## 🚀 기능 (MVP)
- **아이돌 생성**: `/idol/{name}`
- **투표하기**: `/vote/{name}`
- **리더보드 조회**: `/leaderboard`
- **상태 체크**: `/health`
- **홈 인덱스**: `/`

---

## 🛠 빠른 시작

### 로컬 실행
```bash
# 저장소 클론
git clone https://github.com/<your-id>/kao-open.git
cd kao-open

# 의존성 설치
python3 -m pip install -r requirements.txt

# 서버 실행
uvicorn main:app --reload