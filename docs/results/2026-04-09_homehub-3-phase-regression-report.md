# HomeHub 3-Phase Regression Report

- Generated at: 2026-04-10T14:12
- Total cases: 23
- PASS: 9
- PARTIAL: 0
- FAIL: 14

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

- Status: `PASS`
- Query: `福冈今天的天气怎么样，温度多少。`
- Expected: 返回福冈当天天气与温度
- Actual: 今天福冈的天气预报显示白天和夜晚的情况可以在 The Weather Channel 和 Weather.com 上查看详细信息。另外，你也可以访问中国气象局网站查询福冈今日及未来一周的天气情况。具体温度数据需要在相关网站上获取。
来源：福冈县, 福冈县, 日本天气预报和情况 - The Weather Channel | Weather.com (weather.com)；【福冈天气】福冈天气预报,天气预报一周,天气预报15天查询 (weather.com.cn)

### 联网航班查询

- Status: `PASS`
- Query: `我要从日本去美国，帮我查询5月31号的所有去美国的飞机，时间和价格`
- Expected: 返回航班与价格信息
- Actual: 我已经查到可用的机票搜索来源，但它们目前提供的主要是搜索入口，还没有直接给出“日本全境到美国全境、5月31日”的完整航班时间和价格列表。这类查询范围太大，时间和价格会随出发城市、到达城市、是否直飞而变化。如果你补充出发城市和到达城市，例如“东京到洛杉矶”或“福冈到纽约”，我就可以继续按时间和价格帮你整理。
来源：Google 机票 (google.com)；【携程机票】飞机票查询,机票预订,机票价格查询,打折特价机票 (flights.ctrip.com)；Skyscanner | 以最快的速度找到最便宜的机票，节省您的时间和金钱！ (skyscanner.net)

### 本地文件查询与附件回传

- Status: `FAIL`
- Query: `查看 C:\Users\hy\OneDrive\ドキュメント 下面有什么文件，AI_Agent_Build2026 en.pptx文件发给我。`
- Expected: 在交流中返回可下载附件
- Actual: C:\Users\hy\OneDrive\ドキュメント 下面有这些内容：MATLAB、Office のカスタム テンプレート、Outlook ファイル、PowerShell、Tencent Files、WeChat Files、AI_Agent_Build2026 en.pptx、certification.pfx、Default.rdp、Tommy Hahn さんのノートブック.url、仕事.url、日本語学習.url
- Notes: Artifacts: []

## 阶段2

### 创建提醒智能体-起草

- Status: `FAIL`
- Query: `创建智能体，名称为提醒。`
- Expected: 追问功能
- Actual: 要创建一个名为“提醒”的智能体，你可以参考阿里云的Dify平台教程。访问该页面获取详细步骤：使用Dify平台手把手创建第一个Agent智能体-开发者社区-阿里云。关注阿里云公众号或下载阿里云APP，可以随时获取更多资讯。如果有任何问题，可以联系客服电话4008013260。
来源：使用Dify平台手把手创建第一个Agent智能体-开发者社区-阿里云 (developer.aliyun.com)

### 创建提醒智能体-补充功能

- Status: `FAIL`
- Query: `指定时间，人物，提醒方式，如邮件，短信，Homehub，到时见后发出提醒`
- Expected: 继续补充或提示确认创建
- Actual: 我还需要一个更具体的提醒时间。

### 创建提醒智能体-确认并生成feature

- Status: `FAIL`
- Query: `确认创建。`
- Expected: 创建完成并生成 feature 文件
- Actual: 确认创建智能体 已开始设计。这个智能体想叫什么名字？
- Notes: feature=E:\pw\HomeHub\runtime\features\customize\reminder_feature.py

### 创建家庭账单智能体-起草

- Status: `FAIL`
- Query: `创建智能体，名称为家庭账单。`
- Expected: 追问功能
- Actual: 还有其他要求吗？如果没有，回答“确认创建”。

### 创建家庭账单智能体-补充主功能

- Status: `PASS`
- Query: `可以通过语音，文字，QCR进行账单的记录。`
- Expected: 继续补充或提示确认创建
- Actual: 已经记录，还有其他要求吗？如果没有，回答“确认创建”。

### 创建家庭账单智能体-补充归类能力

- Status: `FAIL`
- Query: `补充，可以按照类别，时间进行归类汇总`
- Expected: 记录补充并提示确认创建
- Actual: 您是希望在智能体工作室中按照类别和时间进行归类汇总，还是需要其他方面的帮助？

### 创建家庭账单智能体-确认并生成feature

- Status: `FAIL`
- Query: `确认创建。`
- Expected: 创建完成并生成 feature 文件
- Actual: 账单记录助手 已正式创建完成。后面我会按照这个蓝图去提醒、记录和处理新输入。 已同时生成 feature 文件：E:\pw\HomeHub\runtime\features\customize\bills_feature.py。
- Notes: feature=E:\pw\HomeHub\runtime\features\customize\family_bills_feature.py

## 阶段3

### 账单图片导入

- Status: `PASS`
- Query: `上传图片，并语言提示，将账单记录到家庭账单中`
- Expected: 完成账单记录
- Actual: 已记录 1 条账单。
- Notes: analysis={'summary': 'FAMILY MART', 'contentType': 'receipt', 'relevantFacts': ['FAMILY MART', '2026-04-09', 'Milk 480 JPY', 'Bread 620 JPY', 'Total 2100 JPY'], 'suggestedAction': '', 'recommendedAction': 'record_expense', 'followUpQuestion': '', 'confidence': 0.0, 'requiresUserReview': False, 'currency': 'JPY', 'merchant': 'FAMILY MART', 'detectedDate': '2026-04-09', 'paymentMethod': '', 'ocrText': 'FAMILY MART\n2026-04-09\nMilk 480 JPY\nBread 620 JPY\nTotal 2100 JPY', 'totalAmount': 2100, 'subtotal': 0, 'taxAmount': 0, 'documentLanguage': 'en-US', 'detectedExpenses': [{'amount': 2100, 'category': 'receipt', 'content': 'FAMILY MART', 'note': '2026-04-09', 'merchant': 'FAMILY MART', 'purchaseDate': '2026-04-09', 'paymentMethod': '', 'taxAmount': 0}], 'provider': 'rapidocr', 'model': 'rapidocr_onnxruntime'}

### 消费总额、提醒联动与Excel导出

- Status: `FAIL`
- Query: `到今天为止消费总额是多少，如果超出2000产生提醒，并将消费的信息生成excel文档`
- Expected: 返回总额、阈值提醒，并生成 Excel 导出
- Actual: 路径不可用：path_not_found
- Notes: artifacts=[]

## 扩展回归

### 扩展1

- Status: `PASS`
- Query: `下午好。`
- Expected: 本地问候仍保持正常
- Actual: 你好，有什么可以帮忙的？
- Notes: artifacts=[]

### 扩展2

- Status: `PASS`
- Query: `查看 C:\Users\hy\OneDrive\ドキュメント 下面有什么文件。`
- Expected: 返回目录内容
- Actual: C:\Users\hy\OneDrive\ドキュメント 下面有这些内容：MATLAB、Office のカスタム テンプレート、Outlook ファイル、PowerShell、Tencent Files、WeChat Files、AI_Agent_Build2026 en.pptx、certification.pfx、Default.rdp、Tommy Hahn さんのノートブック.url、仕事.url、日本語学習.url
- Notes: artifacts=[]

### 扩展3

- Status: `FAIL`
- Query: `在 C:\Users\hy\OneDrive\ドキュメント 搜索 AI_Agent_Build2026 en.pptx`
- Expected: 返回文件搜索结果
- Actual: 好的，请稍等一下。我正在搜索文件...
- Notes: artifacts=[]

### 扩展4

- Status: `FAIL`
- Query: `查看 C:\Users\hy\OneDrive\ドキュメント 下面有什么文件，AI_Agent_Build2026 en.pptx文件发给我。`
- Expected: 返回下载附件
- Actual: C:\Users\hy\OneDrive\ドキュメント 下面有这些内容：MATLAB、Office のカスタム テンプレート、Outlook ファイル、PowerShell、Tencent Files、WeChat Files、AI_Agent_Build2026 en.pptx、certification.pfx、Default.rdp、Tommy Hahn さんのノートブック.url、仕事.url、日本語学習.url
- Notes: artifacts=[]

### 扩展5

- Status: `FAIL`
- Query: `家庭账单现在有多少条记录`
- Expected: 返回账单记录数量
- Actual: 本地日程里暂时没有新的安排或提醒。
- Notes: artifacts=[]

### 扩展6

- Status: `FAIL`
- Query: `导出家庭账单的记录文件`
- Expected: 返回账单导出文件
- Actual: 路径不可用：path_not_found
- Notes: artifacts=[]

### 扩展7

- Status: `PASS`
- Query: `把 C:\Users\hy\OneDrive\ドキュメント\AI_Agent_Build2026 en.pptx 发给我`
- Expected: 直接返回附件
- Actual: 我已经找到并准备好了文件：AI_Agent_Build2026 en.pptx。你可以直接点击下面的附件下载。
- Notes: artifacts=[{'kind': 'file', 'label': 'Local File', 'fileName': 'AI_Agent_Build2026 en.pptx', 'path': 'generated\\local-files\\20260410-140843-AI_Agent_Build2026-en.pptx', 'url': '/generated/local-files/20260410-140843-AI_Agent_Build2026-en.pptx', 'sourcePath': 'C:\\Users\\hy\\OneDrive\\ドキュメント\\AI_Agent_Build2026 en.pptx'}]

### 扩展8

- Status: `PASS`
- Query: `到目前为止消费总额多少`
- Expected: 返回累计消费
- Actual: 到今天为止，账单记录助手 累计记录 1 条，消费总额约为 2100。
- Notes: artifacts=[]

### 扩展9

- Status: `FAIL`
- Query: `如果超过3000就提醒我，并导出账单表格`
- Expected: 不超阈值时也应导出表格
- Actual: 我还需要一个更具体的提醒时间。
- Notes: artifacts=[]

### 扩展10

- Status: `FAIL`
- Query: `删除家庭账单里名为 FAMILY MART 的记录`
- Expected: 删除指定记录
- Actual: feature_missing
- Notes: artifacts=[]
