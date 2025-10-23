from typing import Optional, Dict, Any

from fastapi import APIRouter, HTTPException, Query, Form, Request
from fastapi.templating import Jinja2Templates

from app.core.security import create_access_token

templates = Jinja2Templates(directory="static/templates")

# 配置
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 访问令牌有效期1小时
REFRESH_TOKEN_EXPIRE_DAYS = 7     # 刷新令牌有效期7天
AUTH_CODE_EXPIRE_MINUTES = 10     # 授权码有效期10秒
CLIENTS_COLLECTION_NAME = "oauth_clients" # 客户端存储集合名称

# ---------------------- 模拟数据存储（生产环境需替换为数据库） ----------------------
# 1. 已注册的客户端
registered_clients: Dict[str, Dict] = {
    "VCoder": {
        "client_name": 'VCoder',
        "client_secret": "vcoder-secret",  # 机密客户端需验证密钥
        "redirect_uris": ["http://localhost:8080/oauth/callback"],  # 允许的回调地址
    }
}

# 2. 临时存储授权码（authorization_code: {client_id, redirect_uri, scope, expires_at}）
auth_codes: Dict[str, Dict] = {}

# 3. 临时存储访问令牌（access_token: {client_id, scope, expires_at}）
access_tokens: Dict[str, Dict] = {}

# 初始化 router
router = APIRouter(tags=["OAuth2"])

# 验证授权参数
@router.get("/authorize")
async def authorize(
    *,
    response_type: str = Query(..., description="必须为 'code' 表示使用授权码模式"),
    client_id: str = Query(..., description="客户端ID"),
    redirect_uri: Optional[str] = Query(None, description="重定向URI"),
    scope: Optional[str] = Query(None, description="请求的权限范围，空格分隔"),
    state: Optional[str] = Query(None, description="客户端生成的随机字符串，用于防CSRF")
):
    # 1. 验证客户端
    client = registered_clients.get(client_id)
    if not client:
        raise HTTPException(status_code=400, detail="Invalid client_id")

    # 2. 验证 redirect_uri 是否在允许列表中
    if redirect_uri not in client.get("redirect_uris", []):
        raise HTTPException(status_code=400, detail="Invalid redirect_uri")

    # 3. 验证 response_type (只支持 'code')
    if response_type != "code":
        raise HTTPException(status_code=400, detail="Unsupported response_type")
    
    # TODO: 返回登录页面或授权页面

@router.post("/token")
async def token(
    grant_type: str = Form(..., description="授权类型，只支持 'authorization_code'"),
    code: str = Form(None, description="授权码，当grant_type为authorization_code时必填"),
    client_id: str = Form(..., description="客户端ID"),
    # client_secret: str = Form(..., description="客户端密钥")
):
    # 验证客户端身份
    if not client_id:
        raise HTTPException(status_code=401, detail="无效的客户端身份验证信息")
    
    if grant_type != "authorization_code":
        raise HTTPException(status_code=400, detail="只支持授权码模式")
    
    # 处理授权码模式
    if not code:
        raise HTTPException(status_code=400, detail="缺少授权码")
    
    # 检查授权码是否存在
    code_key = f"auth_code:{code}"
    code_data: Any = auth_codes.get(code_key)
    if not code_data:
        raise HTTPException(status_code=400, detail="无效的授权码或授权码已过期")
    
    # 验证 client_id 是否匹配
    if code_data.get("client_id") != client_id:
        raise HTTPException(status_code=400, detail="客户端ID与授权码不匹配")
    
    # 删除授权码
    auth_codes.pop(code_key, None)
    
    # 准备JWT数据
    user_id = code_data["user_id"]
    scope = code_data["scope"]
    
    # 生成访问令牌
    access_token = create_access_token(user_id)
    
    # 返回令牌响应（不返回 refresh_token）
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        "scope": scope
    }

@router.get("/template")
async def read_root(request: Request):
    # 传递给模板的数据（键值对形式）
    context = {
        "request": request,  # 必须传递 request 对象（Jinja2 要求）
    }
    # 渲染 templates/index.html 模板，并返回
    return templates.TemplateResponse("index.html", context)