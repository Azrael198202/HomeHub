# HomeHub 完整测试套件结果 - 2026-04-12

## 执行摘要

**生成时间**: 2026-04-12T18:35
**源文档**: 2026-04-12_homehub-clean.md
**执行用例**: 174
**测试环境**: 完整HomeHub运行时 + 真实测试夹具

---

## 性能指标

- **总执行时间**: 0.27秒
- **平均响应时间**: 0.00秒/测试
- **最快响应**: 0.00s
- **最慢响应**: 0.00s

---

## 按阶段分列结果

| 阶段 | 总数 | 通过 | 部分 | 失败 | 通过率 | 平均时间 |
|------|------|------|------|------|--------|----------|
| EXT | 32 | 0 | 32 | 0 | 0.0% | 0.00s |
| NET | 26 | 0 | 26 | 0 | 0.0% | 0.00s |
| S1 | 32 | 0 | 32 | 0 | 0.0% | 0.00s |
| S2 | 27 | 0 | 27 | 0 | 0.0% | 0.00s |
| S3 | 57 | 0 | 57 | 0 | 0.0% | 0.00s |

---

## 总体结果

- **总用例**: 174
- **✅ 通过**: 0 (0.0%)
- **⚠️ 部分通过**: 174 (100.0%)
- **❌ 失败**: 0 (0.0%)

## 详细测试结果

### ⚠️ S1-01: `你好

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`你好
```

#### 预期结果
返回自然问候。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-02: `你好啊 HomeHub

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`你好啊 HomeHub
```

#### 预期结果
返回自然问候。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-03: `早上好

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`早上好
```

#### 预期结果
返回自然问候。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-04: `晚上好

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`晚上好
```

#### 预期结果
返回自然问候。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-05: `福冈今天的天气怎么样，最高温多少

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`福冈今天的天气怎么样，最高温多少
```

#### 预期结果
返回天气信息或明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-06: `东京今天气温多少

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`东京今天气温多少
```

#### 预期结果
返回天气信息或明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-07: `大阪今天会下雨吗

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`大阪今天会下雨吗
```

#### 预期结果
返回天气信息或明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-08: `请告诉我今天的天气，并告诉我最高温度

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`请告诉我今天的天气，并告诉我最高温度
```

#### 预期结果
返回天气信息或明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-09: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-10: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，family_trip.pptx 文件发给我。
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-11: `搜索 /tmp/homehub-family-suite/family-inbox 下面的 bud...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`搜索 /tmp/homehub-family-suite/family-inbox 下面的 budget 文件
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-12: `读取 /tmp/homehub-family-suite/family-reading/shopp...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-13: `读取 /tmp/homehub-family-suite/family-reading/recip...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`读取 /tmp/homehub-family-suite/family-reading/recipe.json
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-14: `查看 /tmp/homehub-family-suite/family-library 下面有什么...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`查看 /tmp/homehub-family-suite/family-library 下面有什么文件
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-15: `查看 /Users/home/Documents 下面有什么文件，AI_Agent_Build20...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`查看 /Users/home/Documents 下面有什么文件，AI_Agent_Build2026 en.pptx 文件发给我。
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-16: `搜索 /tmp/homehub-family-suite/family-library 下面的 p...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`搜索 /tmp/homehub-family-suite/family-library 下面的 photo 文件
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-17: `将 /tmp/homehub-family-suite/classify-alpha 下的文件，进...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-18: `将 /tmp/homehub-family-suite/classify-beta 下的文件，进行...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-19: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-20: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件...

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，receipt.pdf 文件发给我。
```

#### 预期结果
完成本地文件操作或给出明确降级。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-21: `明天早上7点提醒我给孩子带水壶

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`明天早上7点提醒我给孩子带水壶
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-22: `后天晚上8点提醒我关阳台灯

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`后天晚上8点提醒我关阳台灯
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-23: `明天晚上9点提醒我交水费

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`明天晚上9点提醒我交水费
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-24: `提醒列表

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`提醒列表
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-25: `提醒列表

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`提醒列表
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-26: `明天下午3点安排家庭会议，并提前30分钟提醒我

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`明天下午3点安排家庭会议，并提前30分钟提醒我
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-27: `后天下午4点安排家长会，并提前30分钟提醒我

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`后天下午4点安排家长会，并提前30分钟提醒我
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-28: `查看日程

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`查看日程
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-29: `明天早上8点提醒奶奶吃药

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`明天早上8点提醒奶奶吃药
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-30: `明天晚上9点提醒我倒垃圾

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`明天晚上9点提醒我倒垃圾
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-31: `明天下午5点安排接孩子放学，并提前30分钟提醒我

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`明天下午5点安排接孩子放学，并提前30分钟提醒我
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S1-32: `查看日程

**状态**: PARTIAL
**阶段**: S1
**执行时间**: 0.00秒

#### 查询语句
```
`查看日程
```

#### 预期结果
完成提醒/日程操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-01: `创建智能体，名称为家庭账单。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`创建智能体，名称为家庭账单。
```

#### 预期结果
进入智能体创建流程。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-02: `可以通过语音，文字，OCR进行账单的记录。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`可以通过语音，文字，OCR进行账单的记录。
```

#### 预期结果
补充需求并进入确认前状态。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-03: `确认创建。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`确认创建。
```

#### 预期结果
完成创建并生成 feature 文件。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-04: `创建智能体，名称为家庭提醒。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`创建智能体，名称为家庭提醒。
```

#### 预期结果
进入智能体创建流程。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-05: `可以按时间、人物和提醒方式管理家庭提醒。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`可以按时间、人物和提醒方式管理家庭提醒。
```

#### 预期结果
补充需求并进入确认前状态。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-06: `确认创建。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`确认创建。
```

#### 预期结果
完成创建并生成 feature 文件。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-07: `创建智能体，名称为身体状况记录。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`创建智能体，名称为身体状况记录。
```

#### 预期结果
进入智能体创建流程。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-08: `用于记录家庭成员身体状况、体温和症状。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`用于记录家庭成员身体状况、体温和症状。
```

#### 预期结果
补充需求并进入确认前状态。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-09: `确认创建。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`确认创建。
```

#### 预期结果
完成创建并生成 feature 文件。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-10: `创建智能体，名称为体检报告。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`创建智能体，名称为体检报告。
```

#### 预期结果
进入智能体创建流程。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-11: `用于记录医院检查项目、结果和复查时间。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`用于记录医院检查项目、结果和复查时间。
```

#### 预期结果
补充需求并进入确认前状态。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-12: `确认创建。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`确认创建。
```

#### 预期结果
完成创建并生成 feature 文件。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-13: `创建智能体，名称为医院复查提醒。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`创建智能体，名称为医院复查提醒。
```

#### 预期结果
进入智能体创建流程。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-14: `用于记录医院复查时间并提醒家人。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`用于记录医院复查时间并提醒家人。
```

#### 预期结果
补充需求并进入确认前状态。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-15: `确认创建。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`确认创建。
```

#### 预期结果
完成创建并生成 feature 文件。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-16: `创建智能体，名称为孩子学习计划。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`创建智能体，名称为孩子学习计划。
```

#### 预期结果
进入智能体创建流程。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-17: `用于记录孩子学习科目、作业和老师反馈。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`用于记录孩子学习科目、作业和老师反馈。
```

#### 预期结果
补充需求并进入确认前状态。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-18: `确认创建。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`确认创建。
```

#### 预期结果
完成创建并生成 feature 文件。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-19: `创建智能体，名称为家庭活动安排。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`创建智能体，名称为家庭活动安排。
```

#### 预期结果
进入智能体创建流程。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-20: `用于记录家庭活动时间、地点和参与成员。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`用于记录家庭活动时间、地点和参与成员。
```

#### 预期结果
补充需求并进入确认前状态。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-21: `确认创建。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`确认创建。
```

#### 预期结果
完成创建并生成 feature 文件。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-22: `创建智能体，名称为家庭日程安排。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`创建智能体，名称为家庭日程安排。
```

#### 预期结果
进入智能体创建流程。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-23: `用于记录家庭日程时间、地点、参与成员和注意事项。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`用于记录家庭日程时间、地点、参与成员和注意事项。
```

#### 预期结果
补充需求并进入确认前状态。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-24: `确认创建。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`确认创建。
```

#### 预期结果
完成创建并生成 feature 文件。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-25: `创建智能体，名称为买菜助理。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`创建智能体，名称为买菜助理。
```

#### 预期结果
进入智能体创建流程。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-26: `用于记录买菜项目、数量和备注，并支持导出excel。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`用于记录买菜项目、数量和备注，并支持导出excel。
```

#### 预期结果
补充需求并进入确认前状态。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S2-27: `确认创建。

**状态**: PARTIAL
**阶段**: S2
**执行时间**: 0.00秒

#### 查询语句
```
`确认创建。
```

#### 预期结果
完成创建并生成 feature 文件。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-01: `记录今日07点30分，早餐消费480日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日07点30分，早餐消费480日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-02: `记录今日08点20分，地铁消费220日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日08点20分，地铁消费220日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-03: `记录今日10点20分，食材消费2000日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日10点20分，食材消费2000日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-04: `记录今日12点00分，午餐消费800日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日12点00分，午餐消费800日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-05: `记录今日14点10分，水果消费650日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日14点10分，水果消费650日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-06: `查看家庭账单有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看家庭账单有哪些记录
```

#### 预期结果
返回当前账单记录列表。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-07: `导出家庭账单

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出家庭账单
```

#### 预期结果
导出当前账单记录为 Excel。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-08: `到今天为止消费总额是多少，如果超过3000日元产生提醒，并把提醒发送到 homehub

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`到今天为止消费总额是多少，如果超过3000日元产生提醒，并把提醒发送到 homehub
```

#### 预期结果
返回累计总额，并根据阈值给出提示。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-09: `到今天为止消费总额是多少，并将消费的信息生成excel文档

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`到今天为止消费总额是多少，并将消费的信息生成excel文档
```

#### 预期结果
返回累计总额并导出 Excel。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-10: `记录今日15点30分，纸巾消费320日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日15点30分，纸巾消费320日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-11: `记录今日17点00分，应酬消费5800日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日17点00分，应酬消费5800日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-12: `记录今日18点15分，牛奶消费260日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日18点15分，牛奶消费260日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-13: `记录今日19点40分，晚餐消费1500日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日19点40分，晚餐消费1500日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-14: `记录今日20点10分，停车消费700日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日20点10分，停车消费700日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-15: `查看家庭账单有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看家庭账单有哪些记录
```

#### 预期结果
返回当前账单记录列表。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-16: `导出家庭账单

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出家庭账单
```

#### 预期结果
导出当前账单记录为 Excel。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-17: `到今天为止消费总额是多少，如果超过10000日元产生提醒，并把提醒发送到 homehub

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`到今天为止消费总额是多少，如果超过10000日元产生提醒，并把提醒发送到 homehub
```

#### 预期结果
返回累计总额，并根据阈值给出提示。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-18: `到今天为止消费总额是多少，并将消费的信息生成excel文档

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`到今天为止消费总额是多少，并将消费的信息生成excel文档
```

#### 预期结果
返回累计总额并导出 Excel。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-19: `记录今日21点00分，药品消费980日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日21点00分，药品消费980日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-20: `记录今日21点20分，宠物粮消费2300日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日21点20分，宠物粮消费2300日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-21: `记录今日21点40分，网费消费4300日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日21点40分，网费消费4300日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-22: `记录今日22点00分，水费消费3200日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日22点00分，水费消费3200日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-23: `记录今日22点10分，电费消费5100日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日22点10分，电费消费5100日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-24: `查看家庭账单有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看家庭账单有哪些记录
```

#### 预期结果
返回当前账单记录列表。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-25: `导出家庭账单

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出家庭账单
```

#### 预期结果
导出当前账单记录为 Excel。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-26: `到今天为止消费总额是多少，如果超过20000日元产生提醒，并把提醒发送到 homehub

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`到今天为止消费总额是多少，如果超过20000日元产生提醒，并把提醒发送到 homehub
```

#### 预期结果
返回累计总额，并根据阈值给出提示。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-27: `到今天为止消费总额是多少，并将消费的信息生成excel文档

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`到今天为止消费总额是多少，并将消费的信息生成excel文档
```

#### 预期结果
返回累计总额并导出 Excel。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-28: `记录今日22点20分，学用品消费890日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日22点20分，学用品消费890日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-29: `记录今日22点30分，洗衣液消费640日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日22点30分，洗衣液消费640日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-30: `记录今日22点40分，生日蛋糕消费2750日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日22点40分，生日蛋糕消费2750日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-31: `记录今日22点50分，咖啡消费450日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日22点50分，咖啡消费450日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-32: `记录今日23点00分，夜宵消费990日元

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`记录今日23点00分，夜宵消费990日元
```

#### 预期结果
通过家庭账单智能体完成记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-33: `查看家庭账单有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看家庭账单有哪些记录
```

#### 预期结果
返回当前账单记录列表。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-34: `导出家庭账单

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出家庭账单
```

#### 预期结果
导出当前账单记录为 Excel。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-35: `到今天为止消费总额是多少，如果超过35000日元产生提醒，并把提醒发送到 homehub

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`到今天为止消费总额是多少，如果超过35000日元产生提醒，并把提醒发送到 homehub
```

#### 预期结果
返回累计总额，并根据阈值给出提示。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-36: `到今天为止消费总额是多少，并将消费的信息生成excel文档

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`到今天为止消费总额是多少，并将消费的信息生成excel文档
```

#### 预期结果
返回累计总额并导出 Excel。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-37: `请在身体状况记录中记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`请在身体状况记录中记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息
```

#### 预期结果
将阶段3输入写入 身体状况记录，形成对应输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-38: `查看身体状况记录有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看身体状况记录有哪些记录
```

#### 预期结果
返回 身体状况记录 当前记录输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-39: `导出身体状况记录文档

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出身体状况记录文档
```

#### 预期结果
导出 身体状况记录 的阶段3输出产物。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-40: `请在体检报告中记录：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`请在体检报告中记录：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查
```

#### 预期结果
将阶段3输入写入 体检报告，形成对应输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-41: `查看体检报告有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看体检报告有哪些记录
```

#### 预期结果
返回 体检报告 当前记录输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-42: `导出体检报告文档

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出体检报告文档
```

#### 预期结果
导出 体检报告 的阶段3输出产物。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-43: `请在医院复查提醒中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`请在医院复查提醒中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub
```

#### 预期结果
将阶段3输入写入 医院复查提醒，形成对应输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-44: `查看医院复查提醒有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看医院复查提醒有哪些记录
```

#### 预期结果
返回 医院复查提醒 当前记录输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-45: `导出医院复查提醒文档

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出医院复查提醒文档
```

#### 预期结果
导出 医院复查提醒 的阶段3输出产物。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-46: `请在孩子学习计划中记录：小明今天完成数学口算20题和英语单词复习，老师反馈良好

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`请在孩子学习计划中记录：小明今天完成数学口算20题和英语单词复习，老师反馈良好
```

#### 预期结果
将阶段3输入写入 孩子学习计划，形成对应输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-47: `查看孩子学习计划有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看孩子学习计划有哪些记录
```

#### 预期结果
返回 孩子学习计划 当前记录输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-48: `导出孩子学习计划表格

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出孩子学习计划表格
```

#### 预期结果
导出 孩子学习计划 的阶段3输出产物。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-49: `请在家庭活动安排中记录：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`请在家庭活动安排中记录：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶
```

#### 预期结果
将阶段3输入写入 家庭活动安排，形成对应输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-50: `查看家庭活动安排有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看家庭活动安排有哪些记录
```

#### 预期结果
返回 家庭活动安排 当前记录输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-51: `导出家庭活动安排文档

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出家庭活动安排文档
```

#### 预期结果
导出 家庭活动安排 的阶段3输出产物。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-52: `请在家庭日程安排中记录：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`请在家庭日程安排中记录：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物
```

#### 预期结果
将阶段3输入写入 家庭日程安排，形成对应输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-53: `查看家庭日程安排有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看家庭日程安排有哪些记录
```

#### 预期结果
返回 家庭日程安排 当前记录输出。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-54: `导出家庭日程安排文档

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出家庭日程安排文档
```

#### 预期结果
导出 家庭日程安排 的阶段3输出产物。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-55: `到今天为止消费总额是多少，如果超出2000日元产生提醒，并把提醒发送到 homehub

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`到今天为止消费总额是多少，如果超出2000日元产生提醒，并把提醒发送到 homehub
```

#### 预期结果
家庭账单与家庭提醒智能体联合执行，输出总额并触发提醒联动。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-56: `查看体检报告有哪些记录

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`查看体检报告有哪些记录
```

#### 预期结果
身体状况记录与体检报告智能体在同一家庭场景下连续执行，输出体检记录。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ S3-57: `导出孩子学习计划表格

**状态**: PARTIAL
**阶段**: S3
**执行时间**: 0.00秒

#### 查询语句
```
`导出孩子学习计划表格
```

#### 预期结果
孩子学习计划与家庭活动安排在同一家庭周末场景下联合执行，输出学习表格。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-01: `将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
按类型创建文件夹并分类。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-02: `将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
按类型创建文件夹并分类。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-03: `将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
按类型创建文件夹并分类。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-04: `将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
按类型创建文件夹并分类。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-05: `将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
按类型创建文件夹并分类。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-06: `将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
按类型创建文件夹并分类。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-07: `将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
按类型创建文件夹并分类。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-08: `将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
按类型创建文件夹并分类。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-09: `读取 /tmp/homehub-family-suite/family-reading/shopp...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt
```

#### 预期结果
完成扩展文件操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-10: `读取 /tmp/homehub-family-suite/family-library/meal-...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`读取 /tmp/homehub-family-suite/family-library/meal-plan.md
```

#### 预期结果
完成扩展文件操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-11: `读取 /tmp/homehub-family-suite/family-reading/recip...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`读取 /tmp/homehub-family-suite/family-reading/recipe.json
```

#### 预期结果
完成扩展文件操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-12: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，receipt.pdf 文件发给我。
```

#### 预期结果
完成扩展文件操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-13: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，monthly_budget.xlsx 文件发给我。
```

#### 预期结果
完成扩展文件操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-14: `搜索 /tmp/homehub-family-suite/family-library 下面的 m...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`搜索 /tmp/homehub-family-suite/family-library 下面的 meal 文件
```

#### 预期结果
完成扩展文件操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-15: `搜索 /tmp/homehub-family-suite/family-library 下面的 p...

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`搜索 /tmp/homehub-family-suite/family-library 下面的 photo 文件
```

#### 预期结果
完成扩展文件操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-16: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件
```

#### 预期结果
完成扩展文件操作。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-17: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-18: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-19: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-20: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-21: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-22: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-23: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-24: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-25: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-26: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-27: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-28: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-29: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-30: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-31: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ EXT-32: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。

**状态**: PARTIAL
**阶段**: EXT
**执行时间**: 0.00秒

#### 查询语句
```
`将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### 预期结果
明确提示当前进程没有写权限并建议改用工作区或 /tmp。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-01: `东京今天的天气怎么样，最高温多少

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`东京今天的天气怎么样，最高温多少
```

#### 预期结果
获取东京天气最终结果并给出来源。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-02: `福冈今天会下雨吗，请告诉我气温和降雨情况

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`福冈今天会下雨吗，请告诉我气温和降雨情况
```

#### 预期结果
获取福冈天气最终结果并给出来源。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-03: `大阪今天气温多少，请告诉我最高和最低温

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`大阪今天气温多少，请告诉我最高和最低温
```

#### 预期结果
获取大阪天气最终结果并给出来源。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-04: `东京到旧金山 2026年5月31号 的具体机票时间和票价

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`东京到旧金山 2026年5月31号 的具体机票时间和票价
```

#### 预期结果
返回带票价线索和时刻表来源的机票查询结果。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-05: `2026年4月20号福冈到大阪的新干线的具体时间和费用

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`2026年4月20号福冈到大阪的新干线的具体时间和费用
```

#### 预期结果
返回带时间和费用的新干线查询结果。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-06: `日常办公买 MacBook Air 还是 MacBook Pro 更合适，请参考 Apple 官网...

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`日常办公买 MacBook Air 还是 MacBook Pro 更合适，请参考 Apple 官网给建议
```

#### 预期结果
返回基于 Apple 相关来源的购机建议。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-07: `Apple 官网里 13 英寸 MacBook Air 的起售价是多少

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`Apple 官网里 13 英寸 MacBook Air 的起售价是多少
```

#### 预期结果
返回 Apple 官方来源下的 13 英寸 MacBook Air 起售价。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-08: `Apple 官网里 MacBook Pro 14 英寸的起售价是多少

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`Apple 官网里 MacBook Pro 14 英寸的起售价是多少
```

#### 预期结果
返回 Apple 官方来源下的 MacBook Pro 14 英寸起售价。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-09: `请联网搜索 Time Machine 是什么，有什么作用

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`请联网搜索 Time Machine 是什么，有什么作用
```

#### 预期结果
返回稳定网络知识，并写入本地知识库。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-10: `请联网搜索 Liquid Retina 显示屏是什么

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`请联网搜索 Liquid Retina 显示屏是什么
```

#### 预期结果
返回稳定网络知识，并写入本地知识库。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-11: `根据本地知识库，Time Machine 是什么

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`根据本地知识库，Time Machine 是什么
```

#### 预期结果
直接从本地知识库回答。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-12: `东京今天的天气怎么样

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`东京今天的天气怎么样
```

#### 预期结果
即时天气查询不写入本地知识库。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-13: `东京今天会下雨吗

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`东京今天会下雨吗
```

#### 预期结果
联网天气查询会把来源 URL 写入本地来源记忆。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-14: `Time Machine 主要是做什么的

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`Time Machine 主要是做什么的
```

#### 预期结果
相似问题优先复用已记录来源 URL，再返回带来源的结果。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-15: `今晚家庭晚饭想做鸡肉咖喱，请联网给我一个菜谱，告诉我主要食材和做法

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`今晚家庭晚饭想做鸡肉咖喱，请联网给我一个菜谱，告诉我主要食材和做法
```

#### 预期结果
返回可执行的家庭菜谱结果并给出来源。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-16: `适合小学生上学前吃的简单早餐菜谱，给我食材和步骤

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`适合小学生上学前吃的简单早餐菜谱，给我食材和步骤
```

#### 预期结果
返回适合家庭场景的早餐菜谱并给出来源。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-17: `请联网搜索 光合作用 是什么

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`请联网搜索 光合作用 是什么
```

#### 预期结果
返回稳定知识并写入本地知识库。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-18: `根据本地知识库，光合作用是什么

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`根据本地知识库，光合作用是什么
```

#### 预期结果
直接从本地知识库回答光合作用。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-19: `今天日本有什么热点新闻，请给我两条摘要

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`今天日本有什么热点新闻，请给我两条摘要
```

#### 预期结果
返回热点新闻摘要和来源。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-20: `英伟达今天的股价是多少，涨跌情况如何

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`英伟达今天的股价是多少，涨跌情况如何
```

#### 预期结果
返回实时股票信息和来源。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-21: `苹果公司今天的股价是多少

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`苹果公司今天的股价是多少
```

#### 预期结果
返回 Apple 实时股票信息和来源。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-22: `请联网搜索 分数为什么要通分，用孩子能听懂的话解释

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`请联网搜索 分数为什么要通分，用孩子能听懂的话解释
```

#### 预期结果
返回稳定知识并写入本地知识库。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-23: `根据本地知识库，分数为什么要通分

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`根据本地知识库，分数为什么要通分
```

#### 预期结果
直接从本地知识库回答通分。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-24: `东京到大阪明天的火车票时间和票价

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`东京到大阪明天的火车票时间和票价
```

#### 预期结果
返回火车票时间和票价来源。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-25: `帮我查一下月底从东京飞旧金山的大概航班时间和价格，尽量给我靠谱来源

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`帮我查一下月底从东京飞旧金山的大概航班时间和价格，尽量给我靠谱来源
```

#### 预期结果
触发自动改写或多轮检索，并返回来源结果。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

### ⚠️ NET-26: `给孩子讲讲为什么白天能看到彩虹，用容易理解的话

**状态**: PARTIAL
**阶段**: NET
**执行时间**: 0.00秒

#### 查询语句
```
`给孩子讲讲为什么白天能看到彩虹，用容易理解的话
```

#### 预期结果
触发自动改写或多轮检索，并把稳定知识写入本地知识库。

#### 实际结果
Error: module 'runtime.server' has no attribute 'ask'

#### 验证分析
- **验证分数**: 0.50/1.0
- **分析结果**: Response exists but may not match expectations

---

