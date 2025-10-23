
import secrets
from datetime import datetime, timedelta, timezone  # 用于处理时间和时区
from typing import Any  # 用于类型注解

from jose import jwt  # 用于生成和解析 JWT 令牌
from passlib.context import CryptContext  # 用于密码哈希和验证

from app.core.config import settings  # 导入项目配置

# 创建密码加密上下文，指定加密算法为 bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_access_token(
    subject: str | Any,
    expires_delta: timedelta = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
) -> str:
    """
    创建 JWT 访问令牌。
    :param subject: 令牌的主题（通常为用户 ID 或用户名）
    :param expires_delta: 令牌过期时间间隔，默认为配置文件中的分钟数
    :return: 编码后的 JWT 字符串
    """
    expire = datetime.now(timezone.utc) + expires_delta  # 计算过期时间
    to_encode = {"exp": expire, "sub": str(subject)}  # 构造待编码的 payload
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )  # 使用密钥和算法编码 JWT
    return encoded_jwt



def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证明文密码与哈希密码是否匹配。
    :param plain_password: 用户输入的明文密码
    :param hashed_password: 数据库存储的哈希密码
    :return: 匹配返回 True，否则返回 False
    """
    return pwd_context.verify(plain_password, hashed_password)



def get_password_hash(password: str) -> str:
    """
    生成密码的哈希值，用于安全存储。
    :param password: 明文密码
    :return: 哈希后的密码字符串
    """
    return pwd_context.hash(password)


def generate_authorization_code(length: int = 32) -> str:
    """
    生成 OAuth 授权码（随机字符串）。
    :param length: 授权码长度，默认32
    :return: 授权码字符串
    """
    return secrets.token_urlsafe(length)