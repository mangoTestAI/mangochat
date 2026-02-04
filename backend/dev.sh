source .venv/bin/activate
export DATABASE_URL=postgresql://postgres.ochxljmbwvlnsnyqcvbn:Qiaojun%40369@aws-1-ap-south-1.pooler.supabase.com:6543/postgres
export CORS_ALLOW_ORIGIN="*"
PORT="${PORT:-8080}"
uvicorn open_webui.main:app --port $PORT --host 0.0.0.0 -- --forwarded-allow-ips '*' --reload --reload-exclude ".venv"
