from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from datetime import datetime
from app.error_codes import ErrorCode

class CustomException(Exception):
    def __init__(self, error_code):
        self.code = error_code[0]
        self.message = error_code[1]
        self.status_code = error_code[2]

# 명세서 1-4. 에러 응답 규격 준수
async def global_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "timestamp": datetime.now().isoformat(),
            "path": str(request.url.path),
            "status": exc.status_code,
            "code": "ERROR", # 필요시 세분화 가능 (e.g., USER_NOT_FOUND)
            "message": exc.detail,
            "details": {} 
        }
    )

async def custom_exception_handler(request: Request, exc: CustomException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "timestamp": datetime.now().isoformat(),
            "path": str(request.url.path),
            "status": exc.status_code,
            "code": exc.code,     # 예: A001, C002 ...
            "message": exc.message
        }
    )