## Frontend

### node 版本
node 版本为 22
安装nvm 后，运行 `nvm use 22` 切换到 22 版本

### 运行
```bash
pnpm install
pnpm run dev
```

### 代理
vite 代理配置在 `vite.config.ts` 文件中


## Backend

### 运行


```bash
ssh qiaojun@devbox.mangotest.ai

cd ~/code/mangochat/backend
# 启动虚拟环境
source .venv/bin/activate
# 启动后端服务
sh dev.sh
```