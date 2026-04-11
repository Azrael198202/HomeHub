# HomeHub 3-Phase Family Test Cases For macOS

- Generated at: 2026-04-11T21:45
- Project path: /Users/home/workspace/HomeHub
- Runtime command: `.venv/bin/python runtime/server.py`
- Documents fixture: /Users/home/Documents
- Temporary family fixtures: /tmp/homehub-family-suite
- Total cases: 174

## 阶段1

### S1-01 本地问候 1

- Query: `你好`
- Expected: 返回自然问候。
- Reset Before: Yes
- Setup Queries: 0

### S1-02 本地问候 2

- Query: `你好啊 HomeHub`
- Expected: 返回自然问候。
- Reset Before: Yes
- Setup Queries: 0

### S1-03 本地问候 3

- Query: `早上好`
- Expected: 返回自然问候。
- Reset Before: Yes
- Setup Queries: 0

### S1-04 本地问候 4

- Query: `晚上好`
- Expected: 返回自然问候。
- Reset Before: Yes
- Setup Queries: 0

### S1-05 天气查询 1

- Query: `福冈今天的天气怎么样，最高温多少`
- Expected: 返回天气信息或明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-06 天气查询 2

- Query: `东京今天气温多少`
- Expected: 返回天气信息或明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-07 天气查询 3

- Query: `大阪今天会下雨吗`
- Expected: 返回天气信息或明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-08 天气查询 4

- Query: `请告诉我今天的天气，并告诉我最高温度`
- Expected: 返回天气信息或明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-09 列出家庭收件箱

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-10 发送收件箱演示文稿

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，family_trip.pptx 文件发给我。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-11 搜索预算文件

- Query: `搜索 /tmp/homehub-family-suite/family-inbox 下面的 budget 文件`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-12 读取购物便签

- Query: `读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-13 读取菜谱 JSON

- Query: `读取 /tmp/homehub-family-suite/family-reading/recipe.json`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-14 列出家庭资料库

- Query: `查看 /tmp/homehub-family-suite/family-library 下面有什么文件`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-15 发送 Documents 夹里的演示文稿

- Query: `查看 /Users/home/Documents 下面有什么文件，AI_Agent_Build2026 en.pptx 文件发给我。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-16 搜索照片

- Query: `搜索 /tmp/homehub-family-suite/family-library 下面的 photo 文件`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-17 分类 Alpha 目录

- Query: `将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-18 分类 Beta 目录

- Query: `将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-19 家庭文档目录权限降级

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-20 发送 PDF 收据

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，receipt.pdf 文件发给我。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

### S1-21 孩子水壶提醒

- Query: `明天早上7点提醒我给孩子带水壶`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

### S1-22 阳台灯提醒

- Query: `后天晚上8点提醒我关阳台灯`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

### S1-23 水费提醒

- Query: `明天晚上9点提醒我交水费`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

### S1-24 提醒列表

- Query: `提醒列表`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 1

### S1-25 双提醒列表

- Query: `提醒列表`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 2

### S1-26 家庭会议日程

- Query: `明天下午3点安排家庭会议，并提前30分钟提醒我`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

### S1-27 家长会日程

- Query: `后天下午4点安排家长会，并提前30分钟提醒我`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

### S1-28 查看日程

- Query: `查看日程`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 1

### S1-29 奶奶吃药提醒

- Query: `明天早上8点提醒奶奶吃药`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

### S1-30 倒垃圾提醒

- Query: `明天晚上9点提醒我倒垃圾`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

### S1-31 学校接送日程

- Query: `明天下午5点安排接孩子放学，并提前30分钟提醒我`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

### S1-32 日程与提醒总览

- Query: `查看日程`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 1

## 阶段2

### S2-01 家庭账单 创建草稿

- Query: `创建智能体，名称为家庭账单。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

### S2-02 家庭账单 补充需求

- Query: `可以通过语音，文字，OCR进行账单的记录。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

### S2-03 家庭账单 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

### S2-04 家庭提醒 创建草稿

- Query: `创建智能体，名称为家庭提醒。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

### S2-05 家庭提醒 补充需求

- Query: `可以按时间、人物和提醒方式管理家庭提醒。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

### S2-06 家庭提醒 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

### S2-07 身体状况记录 创建草稿

- Query: `创建智能体，名称为身体状况记录。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

### S2-08 身体状况记录 补充需求

- Query: `用于记录家庭成员身体状况、体温和症状。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

### S2-09 身体状况记录 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

### S2-10 体检报告 创建草稿

- Query: `创建智能体，名称为体检报告。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

### S2-11 体检报告 补充需求

- Query: `用于记录医院检查项目、结果和复查时间。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

### S2-12 体检报告 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

### S2-13 医院复查提醒 创建草稿

- Query: `创建智能体，名称为医院复查提醒。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

### S2-14 医院复查提醒 补充需求

- Query: `用于记录医院复查时间并提醒家人。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

### S2-15 医院复查提醒 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

### S2-16 孩子学习计划 创建草稿

- Query: `创建智能体，名称为孩子学习计划。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

### S2-17 孩子学习计划 补充需求

- Query: `用于记录孩子学习科目、作业和老师反馈。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

### S2-18 孩子学习计划 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

### S2-19 家庭活动安排 创建草稿

- Query: `创建智能体，名称为家庭活动安排。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

### S2-20 家庭活动安排 补充需求

- Query: `用于记录家庭活动时间、地点和参与成员。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

### S2-21 家庭活动安排 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

### S2-22 家庭日程安排 创建草稿

- Query: `创建智能体，名称为家庭日程安排。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

### S2-23 家庭日程安排 补充需求

- Query: `用于记录家庭日程时间、地点、参与成员和注意事项。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

### S2-24 家庭日程安排 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

### S2-25 买菜助理 创建草稿

- Query: `创建智能体，名称为买菜助理。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

### S2-26 买菜助理 补充需求

- Query: `用于记录买菜项目、数量和备注，并支持导出excel。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

### S2-27 买菜助理 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

## 阶段3

### S3-01 账单记录 1

- Query: `记录今日07点30分，早餐消费480日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: Yes
- Setup Queries: 3

### S3-02 账单记录 2

- Query: `记录今日08点20分，地铁消费220日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-03 账单记录 3

- Query: `记录今日10点20分，食材消费2000日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-04 账单记录 4

- Query: `记录今日12点00分，午餐消费800日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-05 账单记录 5

- Query: `记录今日14点10分，水果消费650日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-06 账单列表 5

- Query: `查看家庭账单有哪些记录`
- Expected: 返回当前账单记录列表。
- Reset Before: No
- Setup Queries: 0

### S3-07 账单导出 5

- Query: `导出家庭账单`
- Expected: 导出当前账单记录为 Excel。
- Reset Before: No
- Setup Queries: 0

### S3-08 账单汇总阈值 5

- Query: `到今天为止消费总额是多少，如果超过3000日元产生提醒，并把提醒发送到 homehub`
- Expected: 返回累计总额，并根据阈值给出提示。
- Reset Before: No
- Setup Queries: 0

### S3-09 账单汇总导出 5

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回累计总额并导出 Excel。
- Reset Before: No
- Setup Queries: 0

### S3-10 账单记录 6

- Query: `记录今日15点30分，纸巾消费320日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-11 账单记录 7

- Query: `记录今日17点00分，应酬消费5800日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-12 账单记录 8

- Query: `记录今日18点15分，牛奶消费260日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-13 账单记录 9

- Query: `记录今日19点40分，晚餐消费1500日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-14 账单记录 10

- Query: `记录今日20点10分，停车消费700日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-15 账单列表 10

- Query: `查看家庭账单有哪些记录`
- Expected: 返回当前账单记录列表。
- Reset Before: No
- Setup Queries: 0

### S3-16 账单导出 10

- Query: `导出家庭账单`
- Expected: 导出当前账单记录为 Excel。
- Reset Before: No
- Setup Queries: 0

### S3-17 账单汇总阈值 10

- Query: `到今天为止消费总额是多少，如果超过10000日元产生提醒，并把提醒发送到 homehub`
- Expected: 返回累计总额，并根据阈值给出提示。
- Reset Before: No
- Setup Queries: 0

### S3-18 账单汇总导出 10

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回累计总额并导出 Excel。
- Reset Before: No
- Setup Queries: 0

### S3-19 账单记录 11

- Query: `记录今日21点00分，药品消费980日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-20 账单记录 12

- Query: `记录今日21点20分，宠物粮消费2300日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-21 账单记录 13

- Query: `记录今日21点40分，网费消费4300日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-22 账单记录 14

- Query: `记录今日22点00分，水费消费3200日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-23 账单记录 15

- Query: `记录今日22点10分，电费消费5100日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-24 账单列表 15

- Query: `查看家庭账单有哪些记录`
- Expected: 返回当前账单记录列表。
- Reset Before: No
- Setup Queries: 0

### S3-25 账单导出 15

- Query: `导出家庭账单`
- Expected: 导出当前账单记录为 Excel。
- Reset Before: No
- Setup Queries: 0

### S3-26 账单汇总阈值 15

- Query: `到今天为止消费总额是多少，如果超过20000日元产生提醒，并把提醒发送到 homehub`
- Expected: 返回累计总额，并根据阈值给出提示。
- Reset Before: No
- Setup Queries: 0

### S3-27 账单汇总导出 15

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回累计总额并导出 Excel。
- Reset Before: No
- Setup Queries: 0

### S3-28 账单记录 16

- Query: `记录今日22点20分，学用品消费890日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-29 账单记录 17

- Query: `记录今日22点30分，洗衣液消费640日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-30 账单记录 18

- Query: `记录今日22点40分，生日蛋糕消费2750日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-31 账单记录 19

- Query: `记录今日22点50分，咖啡消费450日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-32 账单记录 20

- Query: `记录今日23点00分，夜宵消费990日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

### S3-33 账单列表 20

- Query: `查看家庭账单有哪些记录`
- Expected: 返回当前账单记录列表。
- Reset Before: No
- Setup Queries: 0

### S3-34 账单导出 20

- Query: `导出家庭账单`
- Expected: 导出当前账单记录为 Excel。
- Reset Before: No
- Setup Queries: 0

### S3-35 账单汇总阈值 20

- Query: `到今天为止消费总额是多少，如果超过35000日元产生提醒，并把提醒发送到 homehub`
- Expected: 返回累计总额，并根据阈值给出提示。
- Reset Before: No
- Setup Queries: 0

### S3-36 账单汇总导出 20

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回累计总额并导出 Excel。
- Reset Before: No
- Setup Queries: 0

### S3-37 身体状况记录 输入记录

- Query: `请在身体状况记录中记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
- Expected: 将阶段3输入写入 身体状况记录，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

### S3-38 身体状况记录 输出查询

- Query: `查看身体状况记录有哪些记录`
- Expected: 返回 身体状况记录 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

### S3-39 身体状况记录 输出导出

- Query: `导出身体状况记录文档`
- Expected: 导出 身体状况记录 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

### S3-40 体检报告 输入记录

- Query: `请在体检报告中记录：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
- Expected: 将阶段3输入写入 体检报告，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

### S3-41 体检报告 输出查询

- Query: `查看体检报告有哪些记录`
- Expected: 返回 体检报告 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

### S3-42 体检报告 输出导出

- Query: `导出体检报告文档`
- Expected: 导出 体检报告 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

### S3-43 医院复查提醒 输入记录

- Query: `请在医院复查提醒中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
- Expected: 将阶段3输入写入 医院复查提醒，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

### S3-44 医院复查提醒 输出查询

- Query: `查看医院复查提醒有哪些记录`
- Expected: 返回 医院复查提醒 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

### S3-45 医院复查提醒 输出导出

- Query: `导出医院复查提醒文档`
- Expected: 导出 医院复查提醒 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

### S3-46 孩子学习计划 输入记录

- Query: `请在孩子学习计划中记录：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
- Expected: 将阶段3输入写入 孩子学习计划，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

### S3-47 孩子学习计划 输出查询

- Query: `查看孩子学习计划有哪些记录`
- Expected: 返回 孩子学习计划 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

### S3-48 孩子学习计划 输出导出

- Query: `导出孩子学习计划表格`
- Expected: 导出 孩子学习计划 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

### S3-49 家庭活动安排 输入记录

- Query: `请在家庭活动安排中记录：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
- Expected: 将阶段3输入写入 家庭活动安排，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

### S3-50 家庭活动安排 输出查询

- Query: `查看家庭活动安排有哪些记录`
- Expected: 返回 家庭活动安排 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

### S3-51 家庭活动安排 输出导出

- Query: `导出家庭活动安排文档`
- Expected: 导出 家庭活动安排 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

### S3-52 家庭日程安排 输入记录

- Query: `请在家庭日程安排中记录：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
- Expected: 将阶段3输入写入 家庭日程安排，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

### S3-53 家庭日程安排 输出查询

- Query: `查看家庭日程安排有哪些记录`
- Expected: 返回 家庭日程安排 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

### S3-54 家庭日程安排 输出导出

- Query: `导出家庭日程安排文档`
- Expected: 导出 家庭日程安排 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

### S3-55 联合执行 账单与提醒阈值联动

- Query: `到今天为止消费总额是多少，如果超出2000日元产生提醒，并把提醒发送到 homehub`
- Expected: 家庭账单与家庭提醒智能体联合执行，输出总额并触发提醒联动。
- Reset Before: Yes
- Setup Queries: 9

### S3-56 联合执行 健康与体检双记录

- Query: `查看体检报告有哪些记录`
- Expected: 身体状况记录与体检报告智能体在同一家庭场景下连续执行，输出体检记录。
- Reset Before: Yes
- Setup Queries: 8

### S3-57 联合执行 学习与活动双场景

- Query: `导出孩子学习计划表格`
- Expected: 孩子学习计划与家庭活动安排在同一家庭周末场景下联合执行，输出学习表格。
- Reset Before: Yes
- Setup Queries: 8

## 扩展

### EXT-01 ext-school 分类

- Query: `将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

### EXT-02 ext-bills 分类

- Query: `将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

### EXT-03 ext-photos 分类

- Query: `将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

### EXT-04 ext-recipes 分类

- Query: `将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

### EXT-05 ext-mixed 分类

- Query: `将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

### EXT-06 ext-visitors 分类

- Query: `将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

### EXT-07 ext-pet 分类

- Query: `将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

### EXT-08 ext-health 分类

- Query: `将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

### EXT-09 扩展读取账单备注

- Query: `读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

### EXT-10 扩展读取菜单

- Query: `读取 /tmp/homehub-family-suite/family-library/meal-plan.md`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

### EXT-11 扩展读取 JSON

- Query: `读取 /tmp/homehub-family-suite/family-reading/recipe.json`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

### EXT-12 扩展发送收据

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，receipt.pdf 文件发给我。`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

### EXT-13 扩展发送预算表

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，monthly_budget.xlsx 文件发给我。`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

### EXT-14 扩展搜索菜谱

- Query: `搜索 /tmp/homehub-family-suite/family-library 下面的 meal 文件`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

### EXT-15 扩展搜索照片

- Query: `搜索 /tmp/homehub-family-suite/family-library 下面的 photo 文件`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

### EXT-16 扩展列出收件箱

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

### EXT-17 家庭目录权限保护 1

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-18 家庭目录权限保护 2

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-19 家庭目录权限保护 3

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-20 家庭目录权限保护 4

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-21 家庭目录权限保护 5

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-22 家庭目录权限保护 6

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-23 家庭目录权限保护 7

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-24 家庭目录权限保护 8

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-25 家庭目录权限保护 9

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-26 家庭目录权限保护 10

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-27 家庭目录权限保护 11

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-28 家庭目录权限保护 12

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-29 家庭目录权限保护 13

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-30 家庭目录权限保护 14

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-31 家庭目录权限保护 15

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

### EXT-32 家庭目录权限保护 16

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

## 联网查询

### NET-01 东京天气

- Query: `东京今天的天气怎么样，最高温多少`
- Expected: 获取东京天气最终结果并给出来源。
- Reset Before: Yes
- Setup Queries: 0

### NET-02 福冈降雨

- Query: `福冈今天会下雨吗，请告诉我气温和降雨情况`
- Expected: 获取福冈天气最终结果并给出来源。
- Reset Before: Yes
- Setup Queries: 0

### NET-03 大阪气温

- Query: `大阪今天气温多少，请告诉我最高和最低温`
- Expected: 获取大阪天气最终结果并给出来源。
- Reset Before: Yes
- Setup Queries: 0

### NET-04 东京到旧金山机票

- Query: `东京到旧金山 2026年5月31号 的具体机票时间和票价`
- Expected: 返回带票价线索和时刻表来源的机票查询结果。
- Reset Before: Yes
- Setup Queries: 0

### NET-05 福冈到大阪新干线

- Query: `2026年4月20号福冈到大阪的新干线的具体时间和费用`
- Expected: 返回带时间和费用的新干线查询结果。
- Reset Before: Yes
- Setup Queries: 0

### NET-06 购机推荐

- Query: `日常办公买 MacBook Air 还是 MacBook Pro 更合适，请参考 Apple 官网给建议`
- Expected: 返回基于 Apple 相关来源的购机建议。
- Reset Before: Yes
- Setup Queries: 0

### NET-07 MacBook Air 价格

- Query: `Apple 官网里 13 英寸 MacBook Air 的起售价是多少`
- Expected: 返回 Apple 官方来源下的 13 英寸 MacBook Air 起售价。
- Reset Before: Yes
- Setup Queries: 0

### NET-08 MacBook Pro 价格

- Query: `Apple 官网里 MacBook Pro 14 英寸的起售价是多少`
- Expected: 返回 Apple 官方来源下的 MacBook Pro 14 英寸起售价。
- Reset Before: Yes
- Setup Queries: 0

### NET-09 Time Machine 网络知识

- Query: `请联网搜索 Time Machine 是什么，有什么作用`
- Expected: 返回稳定网络知识，并写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

### NET-10 Liquid Retina 网络知识

- Query: `请联网搜索 Liquid Retina 显示屏是什么`
- Expected: 返回稳定网络知识，并写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

### NET-11 本地知识库回查 Time Machine

- Query: `根据本地知识库，Time Machine 是什么`
- Expected: 直接从本地知识库回答。
- Reset Before: Yes
- Setup Queries: 1

### NET-12 即时天气不入库

- Query: `东京今天的天气怎么样`
- Expected: 即时天气查询不写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

### NET-13 天气来源URL写入

- Query: `东京今天会下雨吗`
- Expected: 联网天气查询会把来源 URL 写入本地来源记忆。
- Reset Before: Yes
- Setup Queries: 0

### NET-14 来源URL复用 Time Machine

- Query: `Time Machine 主要是做什么的`
- Expected: 相似问题优先复用已记录来源 URL，再返回带来源的结果。
- Reset Before: Yes
- Setup Queries: 1

### NET-15 家庭晚餐菜谱

- Query: `今晚家庭晚饭想做鸡肉咖喱，请联网给我一个菜谱，告诉我主要食材和做法`
- Expected: 返回可执行的家庭菜谱结果并给出来源。
- Reset Before: Yes
- Setup Queries: 0

### NET-16 孩子早餐菜谱

- Query: `适合小学生上学前吃的简单早餐菜谱，给我食材和步骤`
- Expected: 返回适合家庭场景的早餐菜谱并给出来源。
- Reset Before: Yes
- Setup Queries: 0

### NET-17 光合作用网络知识

- Query: `请联网搜索 光合作用 是什么`
- Expected: 返回稳定知识并写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

### NET-18 本地知识库回查 光合作用

- Query: `根据本地知识库，光合作用是什么`
- Expected: 直接从本地知识库回答光合作用。
- Reset Before: Yes
- Setup Queries: 1

### NET-19 日本热点新闻

- Query: `今天日本有什么热点新闻，请给我两条摘要`
- Expected: 返回热点新闻摘要和来源。
- Reset Before: Yes
- Setup Queries: 0

### NET-20 家庭关注股票

- Query: `英伟达今天的股价是多少，涨跌情况如何`
- Expected: 返回实时股票信息和来源。
- Reset Before: Yes
- Setup Queries: 0

### NET-21 Apple 股票

- Query: `苹果公司今天的股价是多少`
- Expected: 返回 Apple 实时股票信息和来源。
- Reset Before: Yes
- Setup Queries: 0

### NET-22 孩子学习知识点

- Query: `请联网搜索 分数为什么要通分，用孩子能听懂的话解释`
- Expected: 返回稳定知识并写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

### NET-23 本地知识库回查 通分

- Query: `根据本地知识库，分数为什么要通分`
- Expected: 直接从本地知识库回答通分。
- Reset Before: Yes
- Setup Queries: 1

### NET-24 家庭火车票信息

- Query: `东京到大阪明天的火车票时间和票价`
- Expected: 返回火车票时间和票价来源。
- Reset Before: Yes
- Setup Queries: 0

### NET-25 自动改写机票查询

- Query: `帮我查一下月底从东京飞旧金山的大概航班时间和价格，尽量给我靠谱来源`
- Expected: 触发自动改写或多轮检索，并返回来源结果。
- Reset Before: Yes
- Setup Queries: 0

### NET-26 自动改写知识查询

- Query: `给孩子讲讲为什么白天能看到彩虹，用容易理解的话`
- Expected: 触发自动改写或多轮检索，并把稳定知识写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0
