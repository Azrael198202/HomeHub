# HomeHub 3-Phase Test Cases

- Generated at: 2026-04-10T17:48
- Project path: E:\pw\HomeHub
- Documents fixture: C:\Users\hy\OneDrive\ドキュメント
- Sample classification fixture: E:\sample documents

## 阶段1

### 1. 本地问候

- Query: `你好`
- Expected: 返回自然问候。

### 2. 城市天气查询

- Query: `请告诉我今天的天气，并告诉我最高温度。`
- Expected: 返回天气和温度信息。

### 3. 联网航班查询

- Query: `帮我查询今天从东京到上海的航班，5月1日有什么航班和价格`
- Expected: 返回航班或联网查询结果。

### 4. 本地文件查询与附件回传

- Query: `查看 C:\Users\hy\OneDrive\ドキュメント 下面有什么文件，AI_Agent_Build2026 en.pptx 文件发给我。`
- Expected: 返回目录内容并附带目标文件。

## 阶段2

### 5. 创建提醒智能体

- Query: `创建智能体，名称为提醒。`
- Expected: 进入提醒智能体创建流程。

### 6. 提醒智能体补充信息

- Query: `用于定时提醒家人，提醒内容包括家庭日程和账单。`
- Expected: 出现确认或继续补充提示。

### 7. 确认生成提醒 feature

- Query: `确认创建提醒智能体。`
- Expected: 生成 reminder feature 文件。

### 8. 创建家庭账单智能体

- Query: `创建智能体，名称为家庭账单。`
- Expected: 进入家庭账单智能体创建流程。

### 9. 家庭账单智能体补充信息

- Query: `可以通过 OCR 和文字记录家庭账单。`
- Expected: 出现确认或继续补充提示。

### 10. 确认生成账单 feature

- Query: `确认创建家庭账单智能体。`
- Expected: 生成 bills feature 文件。

## 阶段3

### 11. 消费记录 10:20

- Query: `记录今天10点20分消费2000日元`
- Expected: 调用家庭账单智能体记录消费。

### 12. 消费记录 12:00

- Query: `记录今天12点00分午饭消费800日元`
- Expected: 调用家庭账单智能体记录消费。

### 13. 消费记录 17:00

- Query: `记录今天17点00分购物消费5800日元`
- Expected: 调用家庭账单智能体记录消费。

### 14. 消费汇总与导出

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回汇总并导出 Excel。

### 15. 消费汇总与提醒

- Query: `到今天为止消费总额是多少，如果超过2000日元产生提醒，并把提醒发送到 homehub`
- Expected: 返回汇总，并在超阈值时触发提醒。

## 扩展

### 16. 样本文档分类

- Query: `将E:\sample documents下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并完成分类。
