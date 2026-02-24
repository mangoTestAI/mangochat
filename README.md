## Frontend

### node 版本
node 版本为 22
安装nvm 后，运行 `nvm use 22` 切换到 22 版本

### 运行
```bash
pnpm install
pnpm run dev
```

### 后端地址
后端地址为 `http://localhost:8000`
可以在 `vite.config.ts` 中配置 `VITE_WEBUI_BASE_URL` 环境变量，来指定后端地址。
例如：
```bash
VITE_WEBUI_BASE_URL=http://devbox.mangotest.ai:8080 
```



## Backend

### 创建虚拟环境
在本地启动后端服务前，需要先创建虚拟环境。

python版本不低于3.11 推荐使用3.12
```bash
cd ~/code/mangochat/backend
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
source venv/bin/activate
```

### 本地启动
在本地启动后端服务，需要先安装依赖，然后运行 `dev.sh` 脚本。

```bash
cd ~/code/mangochat/backend
# 安装依赖
pip install -r requirements.txt
# 启动后端服务（临时）
sh dev.sh
# 启动后端服务（常驻）
sh dev-nohup.sh
```

### 远程开发
```bash
ssh qiaojun@devbox.mangotest.ai
cd ~/code/mangochat/backend
# 启动后端服务
sh dev.sh
```

### 切换环境
默认环境为 dev，切换到 prod 环境需要设置环境变量 `SG_ENV=prod`
```bash
export SG_ENV=prod
```

## 其他文档
### 项目文档
[项目文档](https://qiaojun-hk.jp.larksuite.com/wiki/OfKkwpwcfiNJibkiEsIjMzOmpkd?from=from_copylink)
