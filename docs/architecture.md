# 🏗️ Bookstore API Architecture

## 1. 기술 스택 (Tech Stack)

| 구분           | 기술 / 도구    | 설명                                  |
| :------------- | :------------- | :------------------------------------ |
| **Language**   | Python 3.12+   | 핵심 개발 언어                        |
| **Framework**  | FastAPI        | 비동기 고성능 웹 프레임워크           |
| **Server**     | Uvicorn        | ASGI 웹 서버 구현체                   |
| **Database**   | MySQL 8.0      | 관계형 데이터베이스 (RDBMS)           |
| **ORM**        | SQLAlchemy     | Python Object-Relational Mapping      |
| **Validation** | Pydantic       | 데이터 유효성 검사 및 설정 관리       |
| **Auth**       | PyJWT, Passlib | JWT 토큰 발급 및 Bcrypt 비밀번호 해싱 |
| **Deployment** | Systemd        | 리눅스 서비스 등록 및 프로세스 관리   |

---

## 2. 프로젝트 디렉토리 구조 (Directory Structure)

```text
bookstore/
├── app/
│   ├── __init__.py
│   ├── main.py              # 애플리케이션 진입점 (Entry Point)
│   ├── database.py          # DB 연결 세션 및 엔진 설정
│   ├── models.py            # SQLAlchemy DB 모델 정의 (ORM)
│   ├── schemas.py           # Pydantic 데이터 검증 스키마 (DTO)
│   ├── exceptions.py        # 커스텀 에러 핸들러 및 예외 정의
│   ├── utils.py             # 비밀번호 해싱 등 유틸리티 함수
│   └── routers/             # API 엔드포인트 라우터 모음
│       ├── __init__.py
│       ├── auth.py          # 인증 (로그인/회원가입/토큰)
│       ├── users.py         # 사용자 관리
│       ├── books.py         # 도서 관리 (검색/필터)
│       ├── reviews.py       # 리뷰 및 평점
│       ├── carts.py         # 장바구니
│       ├── orders.py        # 주문 처리
│       ├── wishlists.py     # 위시리스트
│       ├── likes.py         # 좋아요 기능
│       └── stats.py         # 관리자 통계
├── tests/                   # 테스트 코드 디렉토리
│   ├── __init__.py
│   └── test_api.py          # 통합 테스트 시나리오
├── .env.example             # 환경 변수 예시 파일
├── requirements.txt         # 의존성 패키지 목록
├── seed_data.py             # 초기 더미 데이터 생성 스크립트
├── reset_db.py              # DB 초기화 스크립트
├── bookstore.service        # Systemd 배포 설정 파일
└── architecture.md          # 시스템 아키텍처 문서
```
