# HomeHub 3-Phase Test Cases

- Generated at: 2026-04-10T15:45
- Project path: E:\pw\HomeHub
- Documents fixture: C:\Users\hy\OneDrive\ドキュメント
- Sample classification fixture: E:\sample documents

## 阶段1

### 1. 本地问候

- Query: `你好。`
- Expected: 返回自然问候。

### 2. 城市天气查询

- Query: `福冈今天的天气怎么样，温度多少。`
- Expected: 返回天气或给出合理降级。

### 3. 联网航班查询

- Query: `我要从日本去美国，帮我查询5月31号的所有去美国的飞机，从东京出发到美国的旧金山，时间和价格`
- Expected: 返回航班信息或给出合理降级。

### 4. 本地文件查询与附件回传

- Query: `查看 C:\Users\hy\OneDrive\ドキュメント 下面有什么文件，AI_Agent_Build2026 en.pptx文件发给我。`
- Expected: 返回目录内容并附带目标文件。

## 阶段2

### 5. 创建提醒智能体-起草

- Query: `创建智能体，名称为提醒。`
- Expected: 进入提醒智能体的创建流。

### 6. 创建提醒智能体-补充功能

- Query: `指定时间，人物，提醒方式，如邮件，短信，Homehub，到时见后发出提醒`
- Expected: 继续收集或进入确认。

### 7. 创建提醒智能体-确认并生成feature

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。

### 8. 创建家庭账单智能体-起草

- Query: `创建智能体，名称为家庭账单。`
- Expected: 进入家庭账单智能体创建流。

### 9. 创建家庭账单智能体-补充功能

- Query: `可以通过语音，文字，QCR进行账单的记录。`
- Expected: 继续收集或进入确认。

### 10. 创建家庭账单智能体-确认并生成feature

- Query: `确认创建。`
- Expected: 完成家庭账单创建并生成 feature 文件。

## 阶段3

### 11. 消费记录

- Query: `记录今日10点20分，食材消费2000日元`
- Expected: 使用家庭账单智能体，记录消费记录情况。

### 12. 消费记录

- Query: `记录今日12点00分，午餐消费800日元`
- Expected: 使用家庭账单智能体，记录消费记录情况。

### 13. 消费记录

- Query: `记录今日17点00分，应酬消费5800日元`
- Expected: 使用家庭账单智能体，记录消费记录情况。

### 14. 消费汇总，导出

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回汇总并附带导出文件，或给出明确失败。

### 15. 消费汇总，提醒

- Query: `到今天为止消费总额是多少，如果超出2000日元产生提醒，发邮件给ying.hahn@gmail.com和再homehub的见面上提醒`
- Expected: 返回汇总，因超出指定的提醒价格，成功发送邮件和再homehub中立刻产生提醒信息。

## 扩展

### 16. 样本文档分类

- Query: `将E:\sample documents下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按文件类型创建分类文件夹。
