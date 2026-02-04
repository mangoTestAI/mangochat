# 启动虚拟环境
source .venv/bin/activate

# 导出数据库连接字符串
export DATABASE_URL=postgresql://postgres.ochxljmbwvlnsnyqcvbn:Qiaojun%40369@aws-1-ap-south-1.pooler.supabase.com:6543/postgres

# 导出 CORS 允许的来源
export CORS_ALLOW_ORIGIN="*"

PORT="${PORT:-8080}"
# 启动后端服务
uvicorn open_webui.main:app --port $PORT --host 0.0.0.0 --forwarded-allow-ips "*" --reload --reload-dir open_webui
