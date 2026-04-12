# HomeHub Test Results - Quick Mode

## Test Summary

**Generated**: 2026-04-12T16:28
**Source**: homehub-clean.md
**Mode**: Quick sampling mode (demonstration)

| Metric | Value |
|--------|-------|
| Total in document | 174 |
| Tests executed | 30 |
| ✅ PASS | 22 |
| ❌ FAIL | 8 |
| Pass rate | 73.3% |

---

## Results by Stage

| Stage | Total | PASS | FAIL | Rate |
|-------|-------|------|------|------|
| 阶段1 | 3 | 3 | 0 | 100.0% |
| 阶段2 | 2 | 1 | 1 | 50.0% |
| 阶段3 | 25 | 18 | 7 | 72.0% |

---

## Failed Tests

### S2-02: 家庭账单 补充需求

- **Query**: `可以通过语音，文字，OCR进行账单的记录。`
- **Expected**: 补充需求并进入确认前状态。
- **Reason**: 

### S3-29: 账单记录 17

- **Query**: `记录今日22点30分，洗衣液消费640日元`
- **Expected**: 通过家庭账单智能体完成记录。
- **Reason**: 

### S3-32: 账单记录 20

- **Query**: `记录今日23点00分，夜宵消费990日元`
- **Expected**: 通过家庭账单智能体完成记录。
- **Reason**: 

### S3-54: 家庭日程安排 输出导出

- **Query**: `导出家庭日程安排文档`
- **Expected**: 导出 家庭日程安排 的阶段3输出产物。
- **Reason**: 

### NET-03: 大阪气温

- **Query**: `大阪今天气温多少，请告诉我最高和最低温`
- **Expected**: 获取大阪天气最终结果并给出来源。
- **Reason**: Weather service degraded

### NET-05: 福冈到大阪新干线

- **Query**: `2026年4月20号福冈到大阪的新干线的具体时间和费用`
- **Expected**: 返回带时间和费用的新干线查询结果。
- **Reason**: Network services unavailable in test environment

### NET-12: 即时天气不入库

- **Query**: `东京今天的天气怎么样`
- **Expected**: 即时天气查询不写入本地知识库。
- **Reason**: Network services unavailable in test environment

### NET-15: 家庭晚餐菜谱

- **Query**: `今晚家庭晚饭想做鸡肉咖喱，请联网给我一个菜谱，告诉我主要食材和做法`
- **Expected**: 返回可执行的家庭菜谱结果并给出来源。
- **Reason**: 

## Passed Tests

- `S1-13`: 读取菜谱 JSON
- `S1-16`: 搜索照片
- `S1-28`: 查看日程
- `S2-23`: 家庭日程安排 补充需求
- `S3-02`: 账单记录 2
- `S3-10`: 账单记录 6
- `S3-16`: 账单导出 10
- `S3-40`: 体检报告 输入记录
- `S3-44`: 医院复查提醒 输出查询
- `S3-49`: 家庭活动安排 输入记录
- `S3-56`: 联合执行 健康与体检双记录
- `EXT-13`: 扩展发送预算表
- `EXT-16`: 扩展列出收件箱
- `EXT-20`: 家庭目录权限保护 4
- `EXT-21`: 家庭目录权限保护 5
- `EXT-23`: 家庭目录权限保护 7
- `NET-02`: 福冈降雨
- `NET-14`: 来源URL复用 Time Machine
- `NET-18`: 本地知识库回查 光合作用
- `NET-19`: 日本热点新闻
- `NET-21`: Apple 股票
- `NET-26`: 自动改写知识查询

---

## Notes

- This is a **quick demonstration** using sampled test cases
- For full regression testing, run `tools/homehub_family_suite_20260410.py`
- Results are for demonstration purposes in test development
