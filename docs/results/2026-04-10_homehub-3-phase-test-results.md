# HomeHub 3-Phase Test Results

- Generated at: 2026-04-10T17:45
- Total cases: 12
- PASS: 0
- FAIL: 12

## 阶段1

### 本地问候

- Status: `FAIL`
- Query: `你好啊`
- Expected: 返回自然问候。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]

### 城市天气查询

- Status: `FAIL`
- Query: `请告诉我今天天气，并且告诉我最高温度。`
- Expected: 返回天气与温度信息。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]

### 联网航班查询

- Status: `FAIL`
- Query: `帮我查询今天从东京到上海的航班，5月1日有什么航班和价格`
- Expected: 返回航班或联网查询结果。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]

### 本地文件查询与附件回传

- Status: `FAIL`
- Query: `查看 C:\Users\hy\OneDrive\ドキュメント 下面有什么文件，AI_Agent_Build2026 en.pptx文件发给我。`
- Expected: 返回目录内容，并附带目标文件。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]

## 阶段2

### 创建提醒智能体

- Status: `FAIL`
- Query: `创建智能体，名称为提醒。`
- Expected: 进入提醒智能体创建流程。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]

### 提醒智能体补充确认

- Status: `FAIL`
- Query: `用于定时提醒家人和 HomeHub，提醒内容包括账单和日程。`
- Expected: 出现确认或继续补充提示。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]

### 确认后生成提醒 feature

- Status: `FAIL`
- Query: `确认创建。`
- Expected: 生成 reminder feature 文件。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]; feature=E:\pw\HomeHub\runtime\features\customize\reminder_feature.py

### 创建家庭账单智能体

- Status: `FAIL`
- Query: `创建智能体，名称为家庭账单。`
- Expected: 进入家庭账单智能体创建流程。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]

### 家庭账单补充确认

- Status: `FAIL`
- Query: `可以通过文字和 OCR 记录账单。`
- Expected: 出现确认或继续补充提示。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]

### 确认后生成账单 feature

- Status: `FAIL`
- Query: `确认创建。`
- Expected: 生成 bills feature 文件。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]; generated=[]

## 阶段3

### 消费汇总与导出

- Status: `FAIL`
- Query: `到今天为止消费总额是多少，如果超出2000产生提醒，并将消费的信息生成excel文档`
- Expected: 返回汇总并附带导出文件，或给出明确失败。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]

## 扩展

### 样本文档分类

- Status: `FAIL`
- Query: `将E:\sample documents下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并完成分类。
- Actual: TIMEOUT after 30s
- Notes: route=timeout; artifacts=[]; sample_dirs=[]
