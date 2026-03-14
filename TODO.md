> !! 请勿提交此文件 !!

# T0-share-viral · Phase 0

> 用户能够一键分享转换结果到社交媒体，并邀请好友获得额外转换次数奖励

## 上下文

- **依赖**: 无 - 这是 Phase 0 任务
- **边界**: 
  - 仅修改 apps/web 下的文件
  - 不涉及后端 API 改动（使用纯前端分享 SDK）
  - 不修改核心转换逻辑，只添加分享 UI

## Tasks

### 1. 设计并实现分享/邀请类型定义

- [ ] 创建 `apps/web/src/types/share.ts`
- **文件**: `apps/web/src/types/share.ts`（新建）
- **验收**: Given 用户点击分享, When 选择分享渠道, Then 类型定义支持所有渠道

```typescript
interface ShareOptions {
  title: string;
  description: string;
  url: string;
  imageUrl?: string;
}

type ShareChannel = 'twitter' | 'linkedin' | 'facebook' | 'wechat' | 'copy' | 'email';

interface ReferralInfo {
  referralCode: string;
  invitedCount: number;
  bonusCredits: number;
}
```

### 2. 实现 useShare Hook

- [ ] 创建 `apps/web/src/hooks/use-share.ts`
- **文件**: `apps/web/src/hooks/use-share.ts`（新建）
- **验收**: Given 用户选择分享渠道, When 调用 share, Then 正确打开对应分享窗口
- **测试**: 单元测试 · `should open Twitter share dialog when channel is twitter`
- **测试**: 单元测试 · `should copy link to clipboard when channel is copy`

功能需求：
- `share(channel, options)` - 执行分享
- `shareToTwitter(options)` - 分享到 Twitter/X
- `shareToLinkedIn(options)` - 分享到 LinkedIn
- `shareToFacebook(options)` - 分享到 Facebook
- `copyLink(url)` - 复制链接到剪贴板
- `shareViaEmail(options)` - 邮件分享

### 3. 实现 useReferral Hook (模拟)

- [ ] 创建 `apps/web/src/hooks/use-referral.ts`
- **文件**: `apps/web/src/hooks/use-referral.ts`（新建）
- **验收**: Given 用户访问页面, When 组件挂载, Then 生成或恢复推荐码

功能需求（纯前端模拟）：
- `getReferralCode()` - 获取当前用户的推荐码（基于 localStorage）
- `generateReferralLink()` - 生成带推荐码的分享链接
- `trackReferral(code)` - 模拟记录邀请（实际后端实现后替换）

### 4. 创建 ShareModal 组件

- [ ] 创建 `apps/web/src/app/components/share-modal.tsx`
- **文件**: `apps/web/src/app/components/share-modal.tsx`（新建）
- **验收**: Given 用户点击分享按钮, When 模态框打开, Then 显示所有分享选项
- **测试**: 组件测试 · `should render all share channels`
- **测试**: 组件测试 · `should close when clicking outside or close button`

UI 设计：
- 模态框标题："Share Your Conversion"
- 分享渠道图标网格（Twitter、LinkedIn、Facebook、复制链接、邮件）
- 每个渠道有对应图标和标签
- 关闭按钮和点击外部关闭
- 可选：转换结果预览缩略图

### 5. 创建 ReferralBanner 组件

- [ ] 创建 `apps/web/src/app/components/referral-banner.tsx`
- **文件**: `apps/web/src/app/components/referral-banner.tsx`（新建）
- **验收**: Given 用户查看页面, When 滚动到合适位置, Then 看到邀请好友横幅
- **测试**: 组件测试 · `should display referral code and copy button`

UI 设计：
- 横幅标题："Invite Friends, Get Free Credits"
- 推荐码展示（可复制）
- "Copy Link" 按钮
- 邀请进度显示（模拟）："You've invited X friends"
- 奖励说明："Each invite gives you +5 conversions"

### 6. 在 UploadSection 添加分享入口

- [ ] 修改转换成功后的 UI，添加分享按钮
- **文件**: `apps/web/src/app/sections/upload-section.tsx`（修改）
- **验收**: Given 转换成功完成, When 显示下载按钮, Then 同时显示分享按钮
- **测试**: 集成测试 · `should show share button after conversion success`

修改点：
- 在下载按钮旁边添加分享按钮
- 点击后打开 ShareModal

### 7. 在首页集成 ReferralBanner

- [ ] 修改 `apps/web/src/app/page.tsx` 添加邀请横幅
- **文件**: `apps/web/src/app/page.tsx`（修改）
- **验收**: Given 用户访问首页, When 页面加载, Then 在 Hero 区域下方看到邀请横幅
- **测试**: 集成测试 · `should render referral banner in page`

布局：
- 放在 Hero 和 UploadSection 之间
- 使用醒目的背景色（黄色/品牌色）
- 移动端适配

### 8. 创建 ShareSection（可选扩展）

- [ ] 创建 `apps/web/src/app/sections/share-section.tsx`
- **文件**: `apps/web/src/app/sections/share-section.tsx`（新建）
- **验收**: Given 用户滚动到分享区域, When 查看内容, Then 看到社交证明和分享 CTA

内容：
- 社交证明："Join 10,000+ users"
- 分享 CTA 按钮
- 用户评价/推荐语

## Done When

- [ ] 所有 Tasks checkbox 已勾选
- [ ] `npm run test` 全部通过
- [ ] `npm run build` 无报错
- [ ] 无 lint / type 错误
- [ ] 手动验证：
  - 转换成功后可以打开分享模态框
  - Twitter 分享链接正确
  - 复制链接功能可用
  - 推荐码生成和展示正常

---

### 测试规约

| 变更类型          | 要求                           |
| ----------------- | ------------------------------ |
| 工具函数 / 纯逻辑 | 单元测试：核心路径 + 边界 case |
| UI 组件           | 组件测试：渲染 + 交互 + 状态   |
| 跨模块 / API 交互 | 集成测试：模拟完整用户流程     |
| 合入 main 前      | 冒烟测试：构建 + 全量测试通过  |
