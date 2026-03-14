> !! 请勿提交此文件 !!

# T0-cicd · Phase 0

> 建立Git仓库、GitHub Actions CI/CD流水线，实现自动化测试和部署

## 上下文

- **依赖**: 无（本Track是基础设施设置）
- **边界**: 不修改业务代码，只添加CI/CD配置和仓库设置

**当前状态:**
- 本地git仓库已初始化
- 尚未推送到GitHub
- 无CI/CD配置
- 前端：Next.js 15 + React 19，部署目标Vercel
- 后端：Python FastAPI，部署目标Railway/Fly.io

## Tasks

### 1. 创建GitHub仓库并推送代码

- [ ] 在GitHub创建edit-banana仓库（public）
- [ ] 添加README.md（项目介绍、技术栈、快速开始）
- [ ] 配置.gitignore（确保node_modules, __pycache__, .env等被忽略）
- [ ] 推送代码到main分支
- **文件**: `README.md`（新建/更新）, `.gitignore`（更新）
- **验收**: Given GitHub仓库创建, When 推送完成, Then main分支包含完整代码
- **测试**: 手动验证 · `should see code on GitHub main branch`

### 2. 设置前端CI/CD (GitHub Actions)

- [ ] 创建前端构建和测试workflow
- [ ] 配置Vercel自动部署（或使用GitHub Actions部署到Vercel）
- [ ] 添加类型检查、lint检查、构建验证
- **文件**: `.github/workflows/frontend.yml`（新建）
- **验收**: Given PR创建, When 推送到分支, Then GitHub Actions运行测试和构建
- **测试**: 手动验证 · `should see green checks on PR`

### 3. 设置后端CI/CD (GitHub Actions)

- [ ] 创建后端测试和构建workflow
- [ ] 配置Python环境、依赖安装
- [ ] 添加代码质量检查（black, ruff, mypy）
- [ ] 配置Docker构建（如需要）
- **文件**: `.github/workflows/backend.yml`（新建）
- **验收**: Given PR修改后端代码, When 推送到分支, Then 后端workflow运行测试
- **测试**: 手动验证 · `should see backend checks on PR`

### 4. 配置部署流水线

- [ ] 配置Vercel部署（前端）- 可设置VERCEL_TOKEN
- [ ] 配置后端部署配置（Railway或Fly.io）
- [ ] 添加部署状态通知
- [ ] 创建部署文档
- **文件**: `.github/workflows/deploy.yml`（新建）, `docs/deployment.md`（新建）
- **验收**: Given 合并到main分支, When CI通过, Then 自动部署到生产环境
- **测试**: 手动验证 · `should auto-deploy on main merge`

### 5. 设置分支保护和PR模板

- [ ] 配置分支保护规则（需要PR、需要review、需要CI通过）
- [ ] 创建PR模板
- [ ] 创建Issue模板
- **文件**: `.github/pull_request_template.md`（新建）, `.github/ISSUE_TEMPLATE/`（新建目录）
- **验收**: Given 尝试直接推送到main, When 推送, Then 被拒绝，需要走PR流程
- **测试**: 手动验证 · `should enforce PR workflow`

实现好后需要使用code-simplifier agent进行代码优化。

## Done When

- [ ] 所有 Tasks checkbox 已勾选
- [ ] GitHub仓库可见，代码已推送
- [ ] GitHub Actions工作流正常运行
- [ ] PR创建时有自动化检查
- [ ] 合并到main后自动部署
- [ ] 分支保护规则生效

---

### 测试规约

| 变更类型          | 要求                           |
| ----------------- | ------------------------------ |
| CI/CD配置         | 手动测试：创建测试PR验证流水线  |
| 部署脚本          | 手动测试：验证部署命令可执行    |
| 文档              | 人工review：步骤清晰可复现      |

- **文件位置**: 与源文件同目录
- **Case 命名**: `should {预期行为} when {条件}`
