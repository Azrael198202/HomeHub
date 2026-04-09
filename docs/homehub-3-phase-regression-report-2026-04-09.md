# HomeHub 3-Phase Regression Report

- Generated at: 2026-04-09T22:29
- Total cases: 23
- PASS: 21
- PARTIAL: 2
- FAIL: 0

## Overall Notes

- Stage 1 network-dependent weather and flight queries were exercised through the real HomeHub path.
- In this local execution environment, external weather/search providers did not return live results, so those cases are marked `PARTIAL` when HomeHub correctly understood the task and degraded gracefully.
- File-system, blueprint creation, OCR bill intake, reminder collaboration, and Excel export were executed end-to-end.

## 阶段1

### 本地问候

- Status: `PASS`
- Query: `你好。`
- Expected: 本地正常问候回复
- Actual: 你好，有什么可以帮忙的？

### 城市天气查询

- Status: `PARTIAL`
- Query: `福冈今天的天气怎么样，温度多少。`
- Expected: 返回福冈当天天气与温度
- Actual: 我已经理解成天气查询了，但当前外部天气服务没有返回可用结果。请稍后重试，或在浏览器允许定位后再查询。
- Notes: 当前测试环境下外部天气服务没有返回结果，因此这里只验证了正确降级，不算实时报文通过。

### 联网航班查询

- Status: `PARTIAL`
- Query: `我要从日本去美国，帮我查询5月31号的所有去美国的飞机，时间和价格`
- Expected: 返回航班与价格信息
- Actual: 我已经理解成航班与价格查询了，但当前外部检索没有返回可用结果。请稍后重试，或换成更具体的出发地、目的地和日期。
- Notes: 当前测试环境下外部检索没有返回结果，因此这里只验证了语义理解与正确降级，不算实时联网结果通过。

### 本地文件查询与附件回传

- Status: `PASS`
- Query: `查看 ~/Documents 下面有什么文件，AI_Agent_Build2026 en.pptx文件发给我。`
- Expected: 在交流中返回可下载附件
- Actual: 我已经找到并准备好了文件：AI_Agent_Build2026 en.pptx。你可以直接点击下面的附件下载。
- Notes: Artifacts: [{'kind': 'file', 'label': 'Local File', 'fileName': 'AI_Agent_Build2026 en.pptx', 'path': 'generated/local-files/20260409-222904-AI_Agent_Build2026-en.pptx', 'url': '/generated/local-files/20260409-222904-AI_Agent_Build2026-en.pptx', 'sourcePath': '/Users/home/Documents/AI_Agent_Build2026 en.pptx'}]

## 阶段2

### 创建提醒智能体-起草

- Status: `PASS`
- Query: `创建智能体，名称为提醒。`
- Expected: 追问功能
- Actual: 提醒 已开始设计。它长期要负责什么任务？

### 创建提醒智能体-补充功能

- Status: `PASS`
- Query: `指定时间，人物，提醒方式，如邮件，短信，Homehub，到时见后发出提醒`
- Expected: 继续补充或提示确认创建
- Actual: 还有其他要求吗？如果没有，回答“确认创建”。

### 创建提醒智能体-确认并生成feature

- Status: `PASS`
- Query: `确认创建。`
- Expected: 创建完成并生成 feature 文件
- Actual: 提醒 已正式创建完成。后面我会按照这个蓝图去提醒、记录和处理新输入。 已同时生成 feature 文件：/Users/home/workspace/HomeHub/runtime/features/customize/reminder_feature.py。
- Notes: feature=/Users/home/workspace/HomeHub/runtime/features/customize/reminder_feature.py

### 创建家庭账单智能体-起草

- Status: `PASS`
- Query: `创建智能体，名称为家庭账单。`
- Expected: 追问功能
- Actual: 家庭账单 已开始设计。它长期要负责什么任务？

### 创建家庭账单智能体-补充主功能

- Status: `PASS`
- Query: `可以通过语音，文字，QCR进行账单的记录。`
- Expected: 继续补充或提示确认创建
- Actual: 还有其他要求吗？如果没有，回答“确认创建”。

### 创建家庭账单智能体-补充归类能力

- Status: `PASS`
- Query: `补充，可以按照类别，时间进行归类汇总`
- Expected: 记录补充并提示确认创建
- Actual: 已经记录，还有其他要求吗？如果没有，回答“确认创建”。

### 创建家庭账单智能体-确认并生成feature

- Status: `PASS`
- Query: `确认创建。`
- Expected: 创建完成并生成 feature 文件
- Actual: 家庭账单 已正式创建完成。后面我会按照这个蓝图去提醒、记录和处理新输入。 已同时生成 feature 文件：/Users/home/workspace/HomeHub/runtime/features/customize/family_bills_feature.py。
- Notes: feature=/Users/home/workspace/HomeHub/runtime/features/customize/family_bills_feature.py

## 阶段3

### 账单图片导入

- Status: `PASS`
- Query: `上传图片，并语言提示，将账单记录到家庭账单中`
- Expected: 完成账单记录
- Actual: 已记录 1 条账单。
- Notes: analysis={'summary': 'FAMILY MART', 'contentType': 'receipt', 'relevantFacts': ['FAMILY MART', '2026-04-09', 'Milk 480 JPY', 'Bread 620 JPY', 'Total 2100 JPY'], 'suggestedAction': '', 'recommendedAction': 'record_expense', 'followUpQuestion': '', 'confidence': 0.0, 'requiresUserReview': False, 'currency': 'JPY', 'merchant': 'FAMILY MART', 'detectedDate': '2026-04-09', 'paymentMethod': '', 'ocrText': 'FAMILY MART\n2026-04-09\nMilk 480 JPY\nBread 620 JPY\nTotal 2100 JPY', 'totalAmount': 2100, 'subtotal': 0, 'taxAmount': 0, 'documentLanguage': 'en-US', 'detectedExpenses': [{'amount': 2100, 'category': 'receipt', 'content': 'FAMILY MART', 'note': '2026-04-09', 'merchant': 'FAMILY MART', 'purchaseDate': '2026-04-09', 'paymentMethod': '', 'taxAmount': 0}], 'provider': 'rapidocr', 'model': 'rapidocr_onnxruntime'}

### 消费总额、提醒联动与Excel导出

- Status: `PASS`
- Query: `到今天为止消费总额是多少，如果超出2000产生提醒，并将消费的信息生成excel文档`
- Expected: 返回总额、阈值提醒，并生成 Excel 导出
- Actual: 到今天为止，家庭账单 累计记录 1 条，消费总额约为 2100。 已经超过你设定的 2000 阈值，我会触发提醒。 我也已经导出了消费明细文件：20260409-222908-family-bills.xlsx。 我也已经联动提醒智能体“提醒”发出超额提醒。
- Notes: artifacts=[{'kind': 'document', 'label': '家庭账单 records', 'fileName': '20260409-222908-family-bills.xlsx', 'path': 'generated/family_bills/20260409-222908-family-bills.xlsx', 'url': '/generated/family_bills/20260409-222908-family-bills.xlsx', 'count': 1}]

## 扩展回归

### 扩展1

- Status: `PASS`
- Query: `下午好。`
- Expected: 本地问候仍保持正常
- Actual: 你好，有什么可以帮忙的？
- Notes: artifacts=[]

### 扩展2

- Status: `PASS`
- Query: `查看 ~/Documents 下面有什么文件。`
- Expected: 返回目录内容
- Actual: /Users/home/Documents 下面有这些内容：Playground、.DS_Store、.localized、AI_Agent_Build2026 en.pptx、AI_Agent_Build2026.pptx、Image_20260409210423_7_2.jpg、secrets.local.json、simplespeech-14a250bf7ba5.json、中日佛教文化交流平台报价0409 update.xlsx、在当前以人工智能为核心驱动力的技术变革背景下.docx、日本語版&English.docx
- Notes: artifacts=[]

### 扩展3

- Status: `PASS`
- Query: `在 ~/Documents 搜索 AI_Agent_Build2026 en.pptx`
- Expected: 返回文件搜索结果
- Actual: 搜索结果：/Users/home/Documents/AI_Agent_Build2026 en.pptx
- Notes: artifacts=[]

### 扩展4

- Status: `PASS`
- Query: `查看 ~/Documents 下面有什么文件，AI_Agent_Build2026 en.pptx文件发给我。`
- Expected: 返回下载附件
- Actual: 我已经找到并准备好了文件：AI_Agent_Build2026 en.pptx。你可以直接点击下面的附件下载。
- Notes: artifacts=[{'kind': 'file', 'label': 'Local File', 'fileName': 'AI_Agent_Build2026 en.pptx', 'path': 'generated/local-files/20260409-222910-AI_Agent_Build2026-en.pptx', 'url': '/generated/local-files/20260409-222910-AI_Agent_Build2026-en.pptx', 'sourcePath': '/Users/home/Documents/AI_Agent_Build2026 en.pptx'}]

### 扩展5

- Status: `PASS`
- Query: `家庭账单现在有多少条记录`
- Expected: 返回账单记录数量
- Actual: 家庭账单 当前有 1 条记录。最近几条是：FAMILY MART：账单截图: 2100 / category: receipt / content: FAMILY MART / note: 2026-04-09
- Notes: artifacts=[]

### 扩展6

- Status: `PASS`
- Query: `导出家庭账单的记录文件`
- Expected: 返回账单导出文件
- Actual: 已导出 1 条记录。
- Notes: artifacts=[{'kind': 'document', 'label': '家庭账单 records', 'fileName': '20260409-222911-family-bills.xlsx', 'path': 'generated/family_bills/20260409-222911-family-bills.xlsx', 'url': '/generated/family_bills/20260409-222911-family-bills.xlsx', 'count': 1}]

### 扩展7

- Status: `PASS`
- Query: `把 ~/Documents/AI_Agent_Build2026 en.pptx 发给我`
- Expected: 直接返回附件
- Actual: 我已经找到并准备好了文件：AI_Agent_Build2026 en.pptx。你可以直接点击下面的附件下载。
- Notes: artifacts=[{'kind': 'file', 'label': 'Local File', 'fileName': 'AI_Agent_Build2026 en.pptx', 'path': 'generated/local-files/20260409-222911-AI_Agent_Build2026-en.pptx', 'url': '/generated/local-files/20260409-222911-AI_Agent_Build2026-en.pptx', 'sourcePath': '/Users/home/Documents/AI_Agent_Build2026 en.pptx'}]

### 扩展8

- Status: `PASS`
- Query: `到目前为止消费总额多少`
- Expected: 返回累计消费
- Actual: 到今天为止，家庭账单 累计记录 1 条，消费总额约为 2100。
- Notes: artifacts=[]

### 扩展9

- Status: `PASS`
- Query: `如果超过3000就提醒我，并导出账单表格`
- Expected: 不超阈值时也应导出表格
- Actual: 到今天为止，家庭账单 累计记录 1 条，消费总额约为 2100。 目前还没有超过你设定的 3000 阈值。 我也已经导出了消费明细文件：20260409-222912-family-bills.xlsx。
- Notes: artifacts=[{'kind': 'document', 'label': '家庭账单 records', 'fileName': '20260409-222912-family-bills.xlsx', 'path': 'generated/family_bills/20260409-222912-family-bills.xlsx', 'url': '/generated/family_bills/20260409-222912-family-bills.xlsx', 'count': 1}]

### 扩展10

- Status: `PASS`
- Query: `删除家庭账单里名为 FAMILY MART 的记录`
- Expected: 删除指定记录
- Actual: 已删除记录：FAMILY MART。
- Notes: artifacts=[]
