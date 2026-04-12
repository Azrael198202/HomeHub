# HomeHub 3-Phase Family Test Cases For macOS

- Generated at: 2026-04-12T17:57
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

- Chinese Variants: 10
  - `你好`
  - `您好`
  - `嗨，你好`
  - `哈喽`
  - `HomeHub 你好`
  - `你好呀`
  - `早啊，你好`
  - `嘿，你好`
  - `在吗，你好`
  - `跟你打个招呼，你好`

- English Variants: 10
  - `Hello`
  - `Hi`
  - `Hello HomeHub`
  - `Hi there`
  - `Hey HomeHub`
  - `Good to see you`
  - `Hello there`
  - `Hi HomeHub`
  - `Hey there`
  - `Greetings`

- Japanese Variants: 10
  - `こんにちは`
  - `やあ、こんにちは`
  - `こんにちは HomeHub`
  - `どうも、こんにちは`
  - `お疲れさま、こんにちは`
  - `こんにちは、元気？`
  - `やあ HomeHub`
  - `こんにちは、お願いします`
  - `ちょっと挨拶です、こんにちは`
  - `もしもし、こんにちは`

### S1-02 本地问候 2

- Query: `你好啊 HomeHub`
- Expected: 返回自然问候。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `你好啊 HomeHub`
  - `HomeHub 你好呀`
  - `嗨 HomeHub`
  - `哈喽 HomeHub`
  - `HomeHub 在吗`
  - `HomeHub 你好`
  - `嘿 HomeHub 你好`
  - `跟你打个招呼 HomeHub`
  - `HomeHub 早上好`
  - `HomeHub 晚上好`

- English Variants: 10
  - `Hi HomeHub`
  - `Hello HomeHub`
  - `Hey HomeHub`
  - `Good to see you, HomeHub`
  - `Hi there, HomeHub`
  - `Hello there, HomeHub`
  - `Hey there, HomeHub`
  - `Morning, HomeHub`
  - `Good day, HomeHub`
  - `Greetings, HomeHub`

- Japanese Variants: 10
  - `こんにちは HomeHub`
  - `やあ HomeHub`
  - `HomeHub、こんにちは`
  - `どうも HomeHub`
  - `こんにちは、HomeHub さん`
  - `HomeHub、元気？`
  - `やあ、HomeHub`
  - `HomeHub に挨拶です`
  - `もしもし HomeHub`
  - `Hello HomeHub`

### S1-03 本地问候 3

- Query: `早上好`
- Expected: 返回自然问候。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `早上好`
  - `早安`
  - `早呀`
  - `早上好呀`
  - `早安 HomeHub`
  - `今天早上好`
  - `早，你好`
  - `早晨好`
  - `新的一天早上好`
  - `跟你说声早安`

- English Variants: 10
  - `Good morning`
  - `Morning`
  - `Good morning, HomeHub`
  - `Morning, HomeHub`
  - `Wishing you a good morning`
  - `Hope you're having a good morning`
  - `Hi, good morning`
  - `Hello this morning`
  - `Good morning there`
  - `Morning there`

- Japanese Variants: 10
  - `おはよう`
  - `おはようございます`
  - `おはよう HomeHub`
  - `朝の挨拶です、おはよう`
  - `今朝もおはよう`
  - `やあ、おはよう`
  - `おはようございます、HomeHub`
  - `朝ですね、おはよう`
  - `今日もおはよう`
  - `おはよう、元気？`

### S1-04 本地问候 4

- Query: `晚上好`
- Expected: 返回自然问候。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `晚上好`
  - `晚安前先打个招呼`
  - `晚上好呀`
  - `晚上好 HomeHub`
  - `今晚好`
  - `这个晚上好呀`
  - `晚上见，先问个好`
  - `晚上好，你在吗`
  - `跟你说声晚上好`
  - `今晚上好`

- English Variants: 10
  - `Good evening`
  - `Evening`
  - `Good evening, HomeHub`
  - `Evening, HomeHub`
  - `Hope you're having a good evening`
  - `Wishing you a pleasant evening`
  - `Hi, good evening`
  - `Hello this evening`
  - `Good evening there`
  - `Evening there`

- Japanese Variants: 10
  - `こんばんは`
  - `こんばんは HomeHub`
  - `今晩は`
  - `やあ、こんばんは`
  - `こんばんは、HomeHub さん`
  - `今夜もこんばんは`
  - `夜の挨拶です、こんばんは`
  - `こんばんは、元気？`
  - `お疲れさま、こんばんは`
  - `こんばんは、よろしくお願いします`

### S1-05 天气查询 1

- Query: `福冈今天的天气怎么样，最高温多少`
- Expected: 返回天气信息或明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查下福冈的天气`
  - `想知道福冈天气怎么样`
  - `看一下福冈天气情况`
  - `请告诉我福冈天气如何`
  - `查查福冈的天气预报`
  - `福冈最高温多少`
  - `帮我查一下福冈今天最高气温`
  - `请告诉我福冈今天会到多少度`
  - `福冈天气和最高温都告诉我`
  - `想知道福冈今天最热多少度`

- English Variants: 10
  - `What is the weather like in 福冈 today?`
  - `Can you check today's weather in 福冈?`
  - `Tell me the weather in 福冈 today.`
  - `How's the weather in 福冈 today?`
  - `Please give me today's forecast in 福冈.`
  - `What's the high temperature in 福冈 today?`
  - `Tell me today's high temperature in 福冈.`
  - `How warm will it get in 福冈 today?`
  - `Please check today's forecast and high temperature for 福冈.`
  - `I'd like today's weather and the high temperature in 福冈.`

- Japanese Variants: 10
  - `福冈の今日の天気を教えて`
  - `福冈は今日どんな天気か知りたい`
  - `福冈の今日の天気予報を見て`
  - `福冈の天気を確認して`
  - `福冈は今日はどんな天気？`
  - `福冈の今日の最高気温は何度？`
  - `福冈の天気と最高気温を教えて`
  - `福冈は今日何度まで上がる？`
  - `福冈の今日の一番高い気温を知りたい`
  - `福冈の今日の天気と最高気温を確認して`

### S1-06 天气查询 2

- Query: `东京今天气温多少`
- Expected: 返回天气信息或明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查下东京的天气`
  - `想知道东京天气怎么样`
  - `看一下东京天气情况`
  - `请告诉我东京天气如何`
  - `查查东京的天气预报`
  - `东京今天多少度`
  - `帮我查下东京今天气温`
  - `请告诉我东京今天温度`
  - `东京今天气温大概多少`
  - `我想知道东京今天有多热`

- English Variants: 10
  - `What is the weather like in 东京 today?`
  - `Can you check today's weather in 东京?`
  - `Tell me the weather in 东京 today.`
  - `How's the weather in 东京 today?`
  - `Please give me today's forecast in 东京.`
  - `What's today's temperature in 东京?`
  - `Tell me the temperature in 东京 today.`
  - `How many degrees is it in 东京 today?`
  - `Can you check today's temperature for 东京?`
  - `I'd like to know the current temperature in 东京 today.`

- Japanese Variants: 10
  - `东京の今日の天気を教えて`
  - `东京は今日どんな天気か知りたい`
  - `东京の今日の天気予報を見て`
  - `东京の天気を確認して`
  - `东京は今日はどんな天気？`
  - `东京の今日の気温は何度？`
  - `东京の今日の温度を教えて`
  - `东京は今日は何度くらい？`
  - `东京の今日の気温を確認して`
  - `东京の今日の温度が知りたい`

### S1-07 天气查询 3

- Query: `大阪今天会下雨吗`
- Expected: 返回天气信息或明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查下大阪的天气`
  - `想知道大阪天气怎么样`
  - `看一下大阪天气情况`
  - `请告诉我大阪天气如何`
  - `查查大阪的天气预报`
  - `大阪今天会不会下雨`
  - `帮我看下大阪今天有没有雨`
  - `请查一下大阪今天降雨情况`
  - `大阪今天下雨概率高吗`
  - `我想知道大阪今天是否有雨`

- English Variants: 10
  - `What is the weather like in 大阪 today?`
  - `Can you check today's weather in 大阪?`
  - `Tell me the weather in 大阪 today.`
  - `How's the weather in 大阪 today?`
  - `Please give me today's forecast in 大阪.`
  - `Will it rain in 大阪 today?`
  - `Can you check whether it's going to rain in 大阪 today?`
  - `Is rain expected in 大阪 today?`
  - `Tell me if I should expect rain in 大阪 today.`
  - `Please check today's rain chances in 大阪.`

- Japanese Variants: 10
  - `大阪の今日の天気を教えて`
  - `大阪は今日どんな天気か知りたい`
  - `大阪の今日の天気予報を見て`
  - `大阪の天気を確認して`
  - `大阪は今日はどんな天気？`
  - `大阪は今日雨が降る？`
  - `大阪の今日の降水状況を教えて`
  - `大阪で今日は雨の可能性がある？`
  - `大阪の今日の雨予報を確認して`
  - `大阪は今日は雨になるか見て`

### S1-08 天气查询 4

- Query: `请告诉我今天的天气，并告诉我最高温度`
- Expected: 返回天气信息或明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查下今天的天气`
  - `想知道今天天气怎么样`
  - `看一下今天天气情况`
  - `请告诉我今天天气如何`
  - `查查今天的天气预报`
  - `今天最高温多少`
  - `帮我查一下今天最高气温`
  - `请告诉我今天会到多少度`
  - `今天天气和最高温都告诉我`
  - `想知道今天最热多少度`

- English Variants: 10
  - `What is the weather like  today?`
  - `Can you check today's weather ?`
  - `Tell me the weather  today.`
  - `How's the weather  today?`
  - `Please give me today's forecast .`
  - `What's the high temperature in the area today?`
  - `Tell me today's high temperature .`
  - `How warm will it get  today?`
  - `Please check today's forecast and high temperature for today.`
  - `I'd like today's weather and the high temperature .`

- Japanese Variants: 10
  - `今日の今日の天気を教えて`
  - `今日は今日どんな天気か知りたい`
  - `今日の今日の天気予報を見て`
  - `今日の天気を確認して`
  - `今日は今日はどんな天気？`
  - `今日の今日の最高気温は何度？`
  - `今日の天気と最高気温を教えて`
  - `今日は今日何度まで上がる？`
  - `今日の今日の一番高い気温を知りたい`
  - `今日の今日の天気と最高気温を確認して`

### S1-09 列出家庭收件箱

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `查看 /tmp/homehub-family-suite/family-inbox 下面有哪些文件`
  - `帮我列出 /tmp/homehub-family-suite/family-inbox 下的文件`
  - `/tmp/homehub-family-suite/family-inbox 里都有什么文件`
  - `请看一下 /tmp/homehub-family-suite/family-inbox 的文件列表`
  - `我想知道 /tmp/homehub-family-suite/family-inbox 下面有哪些内容`
  - `打开 /tmp/homehub-family-suite/family-inbox 看看里面的文件`
  - `帮我确认 /tmp/homehub-family-suite/family-inbox 下都有哪些文件`
  - `列一下 /tmp/homehub-family-suite/family-inbox 里的文件`
  - `请检查 /tmp/homehub-family-suite/family-inbox 目录下的文件`
  - `看看 /tmp/homehub-family-suite/family-inbox 里面有什么`

- English Variants: 10
  - `Show me the files in /tmp/homehub-family-suite/family-inbox.`
  - `List the files under /tmp/homehub-family-suite/family-inbox.`
  - `What files are in /tmp/homehub-family-suite/family-inbox?`
  - `Can you check what files are inside /tmp/homehub-family-suite/family-inbox?`
  - `Please tell me what files are under /tmp/homehub-family-suite/family-inbox.`
  - `I want to see the contents of /tmp/homehub-family-suite/family-inbox.`
  - `Open /tmp/homehub-family-suite/family-inbox and list what's there.`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and show me the files.`
  - `Give me a file list for /tmp/homehub-family-suite/family-inbox.`
  - `Could you look in /tmp/homehub-family-suite/family-inbox and tell me what files are there?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて`
  - `/tmp/homehub-family-suite/family-inbox 配下のファイルを一覧にして`
  - `/tmp/homehub-family-suite/family-inbox の中に何のファイルがあるか教えて`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を確認したい`
  - `/tmp/homehub-family-suite/family-inbox の内容を見せてください`
  - `/tmp/homehub-family-suite/family-inbox に入っているファイルを表示して`
  - `/tmp/homehub-family-suite/family-inbox を開いて中身を確認して`
  - `/tmp/homehub-family-suite/family-inbox 配下のファイルを教えて`
  - `/tmp/homehub-family-suite/family-inbox に何があるかチェックして`
  - `/tmp/homehub-family-suite/family-inbox のファイル構成を見せて`

### S1-10 发送收件箱演示文稿

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，family_trip.pptx 文件发给我。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `看看 /tmp/homehub-family-suite/family-inbox 里有什么文件，再把 family_trip.pptx 发给我`
  - `帮我列出 /tmp/homehub-family-suite/family-inbox 下面的文件，并把 family_trip.pptx 传给我`
  - `查看一下 /tmp/homehub-family-suite/family-inbox 的文件列表，然后把 family_trip.pptx 给我`
  - `请检查 /tmp/homehub-family-suite/family-inbox 里有哪些文件，顺便发送 family_trip.pptx`
  - `我想看 /tmp/homehub-family-suite/family-inbox 下的文件，同时把 family_trip.pptx 发我`
  - `打开 /tmp/homehub-family-suite/family-inbox 看看文件情况，再把 family_trip.pptx 发过来`
  - `帮我确认 /tmp/homehub-family-suite/family-inbox 里有哪些内容，并发送文件 family_trip.pptx`
  - `列一下 /tmp/homehub-family-suite/family-inbox 里的文件，再把 family_trip.pptx 共享给我`
  - `看一下 /tmp/homehub-family-suite/family-inbox，并把其中的 family_trip.pptx 发给我`
  - `请先查看 /tmp/homehub-family-suite/family-inbox 下的文件，再发送 family_trip.pptx`

- English Variants: 10
  - `Show me the files in /tmp/homehub-family-suite/family-inbox, and send me family_trip.pptx.`
  - `List the files under /tmp/homehub-family-suite/family-inbox, then send over family_trip.pptx.`
  - `What's inside /tmp/homehub-family-suite/family-inbox? Please send me family_trip.pptx.`
  - `Can you check /tmp/homehub-family-suite/family-inbox and share family_trip.pptx with me?`
  - `Please look in /tmp/homehub-family-suite/family-inbox, list the files, and send family_trip.pptx.`
  - `I want to see the files in /tmp/homehub-family-suite/family-inbox; also send me family_trip.pptx.`
  - `Open /tmp/homehub-family-suite/family-inbox, tell me what files are there, and send family_trip.pptx.`
  - `Check the contents of /tmp/homehub-family-suite/family-inbox and forward family_trip.pptx to me.`
  - `Could you list the files in /tmp/homehub-family-suite/family-inbox and send me family_trip.pptx?`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and share the file family_trip.pptx.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて、そのあと family_trip.pptx を送って`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を出して、family_trip.pptx を送ってください`
  - `/tmp/homehub-family-suite/family-inbox に何があるか確認して、family_trip.pptx を共有して`
  - `/tmp/homehub-family-suite/family-inbox の中身を見せてから family_trip.pptx を送って`
  - `/tmp/homehub-family-suite/family-inbox を確認して、family_trip.pptx を私に渡して`
  - `/tmp/homehub-family-suite/family-inbox のファイルを一覧表示して、family_trip.pptx を送信して`
  - `/tmp/homehub-family-suite/family-inbox にあるものを教えて、family_trip.pptx も送って`
  - `/tmp/homehub-family-suite/family-inbox を開いてファイルを確認し、family_trip.pptx を送ってください`
  - `/tmp/homehub-family-suite/family-inbox の内容を見て、family_trip.pptx を共有してください`
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを確認したうえで family_trip.pptx を送って`

### S1-11 搜索预算文件

- Query: `搜索 /tmp/homehub-family-suite/family-inbox 下面的 budget 文件`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `搜索 /tmp/homehub-family-suite/family-inbox 下面和 budget 相关的文件`
  - `帮我在 /tmp/homehub-family-suite/family-inbox 里找 budget 文件`
  - `请查找 /tmp/homehub-family-suite/family-inbox 下包含 budget 的文件`
  - `看看 /tmp/homehub-family-suite/family-inbox 里面有没有 budget 相关文件`
  - `在 /tmp/homehub-family-suite/family-inbox 目录里搜索 budget`
  - `帮我检索 /tmp/homehub-family-suite/family-inbox 下的 budget 文件`
  - `请在 /tmp/homehub-family-suite/family-inbox 中查一下 budget 文件`
  - `找找 /tmp/homehub-family-suite/family-inbox 里面和 budget 有关的文件`
  - `查看 /tmp/homehub-family-suite/family-inbox 下是否有 budget 文件`
  - `在 /tmp/homehub-family-suite/family-inbox 里搜一下关键词 budget`

- English Variants: 10
  - `Search for files related to budget under /tmp/homehub-family-suite/family-inbox.`
  - `Find the budget files in /tmp/homehub-family-suite/family-inbox.`
  - `Please look through /tmp/homehub-family-suite/family-inbox for files matching budget.`
  - `Can you search /tmp/homehub-family-suite/family-inbox for any budget files?`
  - `Show me files about budget under /tmp/homehub-family-suite/family-inbox.`
  - `I need you to find budget-related files in /tmp/homehub-family-suite/family-inbox.`
  - `Please check /tmp/homehub-family-suite/family-inbox and search for budget files.`
  - `Look in /tmp/homehub-family-suite/family-inbox for anything named around budget.`
  - `Search the folder /tmp/homehub-family-suite/family-inbox for budget.`
  - `Could you find files connected to budget in /tmp/homehub-family-suite/family-inbox?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox で budget に関連するファイルを探して`
  - `/tmp/homehub-family-suite/family-inbox 配下の budget ファイルを検索して`
  - `/tmp/homehub-family-suite/family-inbox の中から budget に関係するファイルを見つけて`
  - `/tmp/homehub-family-suite/family-inbox で budget を含むファイルを探して`
  - `/tmp/homehub-family-suite/family-inbox の budget 関連ファイルを見たい`
  - `/tmp/homehub-family-suite/family-inbox を検索して budget ファイルを見つけて`
  - `/tmp/homehub-family-suite/family-inbox にある budget ファイルを確認して`
  - `/tmp/homehub-family-suite/family-inbox の中で budget に近いファイルを探して`
  - `/tmp/homehub-family-suite/family-inbox から budget ファイルを見つけてください`
  - `/tmp/homehub-family-suite/family-inbox 内の budget に関するファイルを検索して`

### S1-12 读取购物便签

- Query: `读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `读取一下 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `帮我打开并读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `看一下 /tmp/homehub-family-suite/family-reading/shopping-note.txt 里的内容`
  - `请读取文件 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `我想查看 /tmp/homehub-family-suite/family-reading/shopping-note.txt 的内容`
  - `打开 /tmp/homehub-family-suite/family-reading/shopping-note.txt 给我看看`
  - `帮我读一下 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `请展示 /tmp/homehub-family-suite/family-reading/shopping-note.txt 里的内容`
  - `查看并读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `把 /tmp/homehub-family-suite/family-reading/shopping-note.txt 打开读给我看`

- English Variants: 10
  - `Read /tmp/homehub-family-suite/family-reading/shopping-note.txt.`
  - `Please open and read /tmp/homehub-family-suite/family-reading/shopping-note.txt.`
  - `Show me the contents of /tmp/homehub-family-suite/family-reading/shopping-note.txt.`
  - `Can you read the file /tmp/homehub-family-suite/family-reading/shopping-note.txt?`
  - `I want to see what's inside /tmp/homehub-family-suite/family-reading/shopping-note.txt.`
  - `Please open /tmp/homehub-family-suite/family-reading/shopping-note.txt and tell me what's in it.`
  - `Check the contents of /tmp/homehub-family-suite/family-reading/shopping-note.txt for me.`
  - `Read through /tmp/homehub-family-suite/family-reading/shopping-note.txt and show it to me.`
  - `Could you display the contents of /tmp/homehub-family-suite/family-reading/shopping-note.txt?`
  - `Take a look at /tmp/homehub-family-suite/family-reading/shopping-note.txt and read it out.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読んで`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を開いて内容を見せて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の中身を確認して`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読み取ってください`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の内容を表示して`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を開いて読んでほしい`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のファイル内容を教えて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を確認して内容を見せて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読んで内容を共有して`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の中身を表示してください`

### S1-13 读取菜谱 JSON

- Query: `读取 /tmp/homehub-family-suite/family-reading/recipe.json`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `读取一下 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `帮我打开并读取 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `看一下 /tmp/homehub-family-suite/family-reading/recipe.json 里的内容`
  - `请读取文件 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `我想查看 /tmp/homehub-family-suite/family-reading/recipe.json 的内容`
  - `打开 /tmp/homehub-family-suite/family-reading/recipe.json 给我看看`
  - `帮我读一下 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `请展示 /tmp/homehub-family-suite/family-reading/recipe.json 里的内容`
  - `查看并读取 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `把 /tmp/homehub-family-suite/family-reading/recipe.json 打开读给我看`

- English Variants: 10
  - `Read /tmp/homehub-family-suite/family-reading/recipe.json.`
  - `Please open and read /tmp/homehub-family-suite/family-reading/recipe.json.`
  - `Show me the contents of /tmp/homehub-family-suite/family-reading/recipe.json.`
  - `Can you read the file /tmp/homehub-family-suite/family-reading/recipe.json?`
  - `I want to see what's inside /tmp/homehub-family-suite/family-reading/recipe.json.`
  - `Please open /tmp/homehub-family-suite/family-reading/recipe.json and tell me what's in it.`
  - `Check the contents of /tmp/homehub-family-suite/family-reading/recipe.json for me.`
  - `Read through /tmp/homehub-family-suite/family-reading/recipe.json and show it to me.`
  - `Could you display the contents of /tmp/homehub-family-suite/family-reading/recipe.json?`
  - `Take a look at /tmp/homehub-family-suite/family-reading/recipe.json and read it out.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読んで`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を開いて内容を見せて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の中身を確認して`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読み取ってください`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の内容を表示して`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を開いて読んでほしい`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のファイル内容を教えて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を確認して内容を見せて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読んで内容を共有して`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の中身を表示してください`

### S1-14 列出家庭资料库

- Query: `查看 /tmp/homehub-family-suite/family-library 下面有什么文件`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `查看 /tmp/homehub-family-suite/family-library 下面有哪些文件`
  - `帮我列出 /tmp/homehub-family-suite/family-library 下的文件`
  - `/tmp/homehub-family-suite/family-library 里都有什么文件`
  - `请看一下 /tmp/homehub-family-suite/family-library 的文件列表`
  - `我想知道 /tmp/homehub-family-suite/family-library 下面有哪些内容`
  - `打开 /tmp/homehub-family-suite/family-library 看看里面的文件`
  - `帮我确认 /tmp/homehub-family-suite/family-library 下都有哪些文件`
  - `列一下 /tmp/homehub-family-suite/family-library 里的文件`
  - `请检查 /tmp/homehub-family-suite/family-library 目录下的文件`
  - `看看 /tmp/homehub-family-suite/family-library 里面有什么`

- English Variants: 10
  - `Show me the files in /tmp/homehub-family-suite/family-library.`
  - `List the files under /tmp/homehub-family-suite/family-library.`
  - `What files are in /tmp/homehub-family-suite/family-library?`
  - `Can you check what files are inside /tmp/homehub-family-suite/family-library?`
  - `Please tell me what files are under /tmp/homehub-family-suite/family-library.`
  - `I want to see the contents of /tmp/homehub-family-suite/family-library.`
  - `Open /tmp/homehub-family-suite/family-library and list what's there.`
  - `Please inspect /tmp/homehub-family-suite/family-library and show me the files.`
  - `Give me a file list for /tmp/homehub-family-suite/family-library.`
  - `Could you look in /tmp/homehub-family-suite/family-library and tell me what files are there?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-library にあるファイルを見せて`
  - `/tmp/homehub-family-suite/family-library 配下のファイルを一覧にして`
  - `/tmp/homehub-family-suite/family-library の中に何のファイルがあるか教えて`
  - `/tmp/homehub-family-suite/family-library のファイル一覧を確認したい`
  - `/tmp/homehub-family-suite/family-library の内容を見せてください`
  - `/tmp/homehub-family-suite/family-library に入っているファイルを表示して`
  - `/tmp/homehub-family-suite/family-library を開いて中身を確認して`
  - `/tmp/homehub-family-suite/family-library 配下のファイルを教えて`
  - `/tmp/homehub-family-suite/family-library に何があるかチェックして`
  - `/tmp/homehub-family-suite/family-library のファイル構成を見せて`

### S1-15 发送 Documents 夹里的演示文稿

- Query: `查看 /Users/home/Documents 下面有什么文件，AI_Agent_Build2026 en.pptx 文件发给我。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `看看 /Users/home/Documents 里有什么文件，再把 AI_Agent_Build2026 en.pptx 发给我`
  - `帮我列出 /Users/home/Documents 下面的文件，并把 AI_Agent_Build2026 en.pptx 传给我`
  - `查看一下 /Users/home/Documents 的文件列表，然后把 AI_Agent_Build2026 en.pptx 给我`
  - `请检查 /Users/home/Documents 里有哪些文件，顺便发送 AI_Agent_Build2026 en.pptx`
  - `我想看 /Users/home/Documents 下的文件，同时把 AI_Agent_Build2026 en.pptx 发我`
  - `打开 /Users/home/Documents 看看文件情况，再把 AI_Agent_Build2026 en.pptx 发过来`
  - `帮我确认 /Users/home/Documents 里有哪些内容，并发送文件 AI_Agent_Build2026 en.pptx`
  - `列一下 /Users/home/Documents 里的文件，再把 AI_Agent_Build2026 en.pptx 共享给我`
  - `看一下 /Users/home/Documents，并把其中的 AI_Agent_Build2026 en.pptx 发给我`
  - `请先查看 /Users/home/Documents 下的文件，再发送 AI_Agent_Build2026 en.pptx`

- English Variants: 10
  - `Show me the files in /Users/home/Documents, and send me AI_Agent_Build2026 en.pptx.`
  - `List the files under /Users/home/Documents, then send over AI_Agent_Build2026 en.pptx.`
  - `What's inside /Users/home/Documents? Please send me AI_Agent_Build2026 en.pptx.`
  - `Can you check /Users/home/Documents and share AI_Agent_Build2026 en.pptx with me?`
  - `Please look in /Users/home/Documents, list the files, and send AI_Agent_Build2026 en.pptx.`
  - `I want to see the files in /Users/home/Documents; also send me AI_Agent_Build2026 en.pptx.`
  - `Open /Users/home/Documents, tell me what files are there, and send AI_Agent_Build2026 en.pptx.`
  - `Check the contents of /Users/home/Documents and forward AI_Agent_Build2026 en.pptx to me.`
  - `Could you list the files in /Users/home/Documents and send me AI_Agent_Build2026 en.pptx?`
  - `Please inspect /Users/home/Documents and share the file AI_Agent_Build2026 en.pptx.`

- Japanese Variants: 10
  - `/Users/home/Documents にあるファイルを見せて、そのあと AI_Agent_Build2026 en.pptx を送って`
  - `/Users/home/Documents のファイル一覧を出して、AI_Agent_Build2026 en.pptx を送ってください`
  - `/Users/home/Documents に何があるか確認して、AI_Agent_Build2026 en.pptx を共有して`
  - `/Users/home/Documents の中身を見せてから AI_Agent_Build2026 en.pptx を送って`
  - `/Users/home/Documents を確認して、AI_Agent_Build2026 en.pptx を私に渡して`
  - `/Users/home/Documents のファイルを一覧表示して、AI_Agent_Build2026 en.pptx を送信して`
  - `/Users/home/Documents にあるものを教えて、AI_Agent_Build2026 en.pptx も送って`
  - `/Users/home/Documents を開いてファイルを確認し、AI_Agent_Build2026 en.pptx を送ってください`
  - `/Users/home/Documents の内容を見て、AI_Agent_Build2026 en.pptx を共有してください`
  - `/Users/home/Documents にあるファイルを確認したうえで AI_Agent_Build2026 en.pptx を送って`

### S1-16 搜索照片

- Query: `搜索 /tmp/homehub-family-suite/family-library 下面的 photo 文件`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `搜索 /tmp/homehub-family-suite/family-library 下面和 photo 相关的文件`
  - `帮我在 /tmp/homehub-family-suite/family-library 里找 photo 文件`
  - `请查找 /tmp/homehub-family-suite/family-library 下包含 photo 的文件`
  - `看看 /tmp/homehub-family-suite/family-library 里面有没有 photo 相关文件`
  - `在 /tmp/homehub-family-suite/family-library 目录里搜索 photo`
  - `帮我检索 /tmp/homehub-family-suite/family-library 下的 photo 文件`
  - `请在 /tmp/homehub-family-suite/family-library 中查一下 photo 文件`
  - `找找 /tmp/homehub-family-suite/family-library 里面和 photo 有关的文件`
  - `查看 /tmp/homehub-family-suite/family-library 下是否有 photo 文件`
  - `在 /tmp/homehub-family-suite/family-library 里搜一下关键词 photo`

- English Variants: 10
  - `Search for files related to photo under /tmp/homehub-family-suite/family-library.`
  - `Find the photo files in /tmp/homehub-family-suite/family-library.`
  - `Please look through /tmp/homehub-family-suite/family-library for files matching photo.`
  - `Can you search /tmp/homehub-family-suite/family-library for any photo files?`
  - `Show me files about photo under /tmp/homehub-family-suite/family-library.`
  - `I need you to find photo-related files in /tmp/homehub-family-suite/family-library.`
  - `Please check /tmp/homehub-family-suite/family-library and search for photo files.`
  - `Look in /tmp/homehub-family-suite/family-library for anything named around photo.`
  - `Search the folder /tmp/homehub-family-suite/family-library for photo.`
  - `Could you find files connected to photo in /tmp/homehub-family-suite/family-library?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-library で photo に関連するファイルを探して`
  - `/tmp/homehub-family-suite/family-library 配下の photo ファイルを検索して`
  - `/tmp/homehub-family-suite/family-library の中から photo に関係するファイルを見つけて`
  - `/tmp/homehub-family-suite/family-library で photo を含むファイルを探して`
  - `/tmp/homehub-family-suite/family-library の photo 関連ファイルを見たい`
  - `/tmp/homehub-family-suite/family-library を検索して photo ファイルを見つけて`
  - `/tmp/homehub-family-suite/family-library にある photo ファイルを確認して`
  - `/tmp/homehub-family-suite/family-library の中で photo に近いファイルを探して`
  - `/tmp/homehub-family-suite/family-library から photo ファイルを見つけてください`
  - `/tmp/homehub-family-suite/family-library 内の photo に関するファイルを検索して`

### S1-17 分类 Alpha 目录

- Query: `将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹`

### S1-18 分类 Beta 目录

- Query: `将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹`

### S1-19 家庭文档目录权限降级

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### S1-20 发送 PDF 收据

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，receipt.pdf 文件发给我。`
- Expected: 完成本地文件操作或给出明确降级。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `看看 /tmp/homehub-family-suite/family-inbox 里有什么文件，再把 receipt.pdf 发给我`
  - `帮我列出 /tmp/homehub-family-suite/family-inbox 下面的文件，并把 receipt.pdf 传给我`
  - `查看一下 /tmp/homehub-family-suite/family-inbox 的文件列表，然后把 receipt.pdf 给我`
  - `请检查 /tmp/homehub-family-suite/family-inbox 里有哪些文件，顺便发送 receipt.pdf`
  - `我想看 /tmp/homehub-family-suite/family-inbox 下的文件，同时把 receipt.pdf 发我`
  - `打开 /tmp/homehub-family-suite/family-inbox 看看文件情况，再把 receipt.pdf 发过来`
  - `帮我确认 /tmp/homehub-family-suite/family-inbox 里有哪些内容，并发送文件 receipt.pdf`
  - `列一下 /tmp/homehub-family-suite/family-inbox 里的文件，再把 receipt.pdf 共享给我`
  - `看一下 /tmp/homehub-family-suite/family-inbox，并把其中的 receipt.pdf 发给我`
  - `请先查看 /tmp/homehub-family-suite/family-inbox 下的文件，再发送 receipt.pdf`

- English Variants: 10
  - `Show me the files in /tmp/homehub-family-suite/family-inbox, and send me receipt.pdf.`
  - `List the files under /tmp/homehub-family-suite/family-inbox, then send over receipt.pdf.`
  - `What's inside /tmp/homehub-family-suite/family-inbox? Please send me receipt.pdf.`
  - `Can you check /tmp/homehub-family-suite/family-inbox and share receipt.pdf with me?`
  - `Please look in /tmp/homehub-family-suite/family-inbox, list the files, and send receipt.pdf.`
  - `I want to see the files in /tmp/homehub-family-suite/family-inbox; also send me receipt.pdf.`
  - `Open /tmp/homehub-family-suite/family-inbox, tell me what files are there, and send receipt.pdf.`
  - `Check the contents of /tmp/homehub-family-suite/family-inbox and forward receipt.pdf to me.`
  - `Could you list the files in /tmp/homehub-family-suite/family-inbox and send me receipt.pdf?`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and share the file receipt.pdf.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて、そのあと receipt.pdf を送って`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を出して、receipt.pdf を送ってください`
  - `/tmp/homehub-family-suite/family-inbox に何があるか確認して、receipt.pdf を共有して`
  - `/tmp/homehub-family-suite/family-inbox の中身を見せてから receipt.pdf を送って`
  - `/tmp/homehub-family-suite/family-inbox を確認して、receipt.pdf を私に渡して`
  - `/tmp/homehub-family-suite/family-inbox のファイルを一覧表示して、receipt.pdf を送信して`
  - `/tmp/homehub-family-suite/family-inbox にあるものを教えて、receipt.pdf も送って`
  - `/tmp/homehub-family-suite/family-inbox を開いてファイルを確認し、receipt.pdf を送ってください`
  - `/tmp/homehub-family-suite/family-inbox の内容を見て、receipt.pdf を共有してください`
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを確認したうえで receipt.pdf を送って`

### S1-21 孩子水壶提醒

- Query: `明天早上7点提醒我给孩子带水壶`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `明天早上7点提醒我我给孩子带水壶`
  - `帮我设置一个提醒，明天早上7点我给孩子带水壶`
  - `请在明天早上7点提醒我去我给孩子带水壶`
  - `到明天早上7点记得提醒我我给孩子带水壶`
  - `我想在明天早上7点收到提醒：我给孩子带水壶`
  - `请给我设一个明天早上7点的提醒，内容是我给孩子带水壶`
  - `明天早上7点帮我提醒一下我给孩子带水壶`
  - `记得在明天早上7点提醒我我给孩子带水壶`
  - `请添加提醒：明天早上7点我给孩子带水壶`
  - `到明天早上7点通知我我给孩子带水壶`

- English Variants: 10
  - `Remind me 明天早上7点 to 我给孩子带水壶.`
  - `Set a reminder 明天早上7点 for me to 我给孩子带水壶.`
  - `Please remind me 明天早上7点 that I need to 我给孩子带水壶.`
  - `Can you create a reminder 明天早上7点 for 我给孩子带水壶?`
  - `I need a reminder 明天早上7点 to 我给孩子带水壶.`
  - `Put in a reminder for 明天早上7点: 我给孩子带水壶.`
  - `Schedule a reminder 明天早上7点 so I remember to 我给孩子带水壶.`
  - `Please alert me 明天早上7点 to 我给孩子带水壶.`
  - `Set me a 明天早上7点 reminder to 我给孩子带水壶.`
  - `Create a reminder telling me 明天早上7点 to 我给孩子带水壶.`

- Japanese Variants: 10
  - `明天早上7点に我给孩子带水壶とリマインドして`
  - `明天早上7点に我给孩子带水壶ことを知らせて`
  - `明天早上7点用に「我给孩子带水壶」のリマインダーを設定して`
  - `明天早上7点になったら我给孩子带水壶と通知して`
  - `明天早上7点のリマインダーとして我给孩子带水壶を登録して`
  - `明天早上7点に我给孩子带水壶の通知を入れて`
  - `明天早上7点に我给孩子带水壶ことを忘れないよう知らせて`
  - `明天早上7点の時刻で我给孩子带水壶をリマインドして`
  - `明天早上7点に私へ我给孩子带水壶と伝えて`
  - `明天早上7点用に我给孩子带水壶の通知を作って`

### S1-22 阳台灯提醒

- Query: `后天晚上8点提醒我关阳台灯`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `后天晚上8点提醒我我关阳台灯`
  - `帮我设置一个提醒，后天晚上8点我关阳台灯`
  - `请在后天晚上8点提醒我去我关阳台灯`
  - `到后天晚上8点记得提醒我我关阳台灯`
  - `我想在后天晚上8点收到提醒：我关阳台灯`
  - `请给我设一个后天晚上8点的提醒，内容是我关阳台灯`
  - `后天晚上8点帮我提醒一下我关阳台灯`
  - `记得在后天晚上8点提醒我我关阳台灯`
  - `请添加提醒：后天晚上8点我关阳台灯`
  - `到后天晚上8点通知我我关阳台灯`

- English Variants: 10
  - `Remind me 后天晚上8点 to 我关阳台灯.`
  - `Set a reminder 后天晚上8点 for me to 我关阳台灯.`
  - `Please remind me 后天晚上8点 that I need to 我关阳台灯.`
  - `Can you create a reminder 后天晚上8点 for 我关阳台灯?`
  - `I need a reminder 后天晚上8点 to 我关阳台灯.`
  - `Put in a reminder for 后天晚上8点: 我关阳台灯.`
  - `Schedule a reminder 后天晚上8点 so I remember to 我关阳台灯.`
  - `Please alert me 后天晚上8点 to 我关阳台灯.`
  - `Set me a 后天晚上8点 reminder to 我关阳台灯.`
  - `Create a reminder telling me 后天晚上8点 to 我关阳台灯.`

- Japanese Variants: 10
  - `后天晚上8点に我关阳台灯とリマインドして`
  - `后天晚上8点に我关阳台灯ことを知らせて`
  - `后天晚上8点用に「我关阳台灯」のリマインダーを設定して`
  - `后天晚上8点になったら我关阳台灯と通知して`
  - `后天晚上8点のリマインダーとして我关阳台灯を登録して`
  - `后天晚上8点に我关阳台灯の通知を入れて`
  - `后天晚上8点に我关阳台灯ことを忘れないよう知らせて`
  - `后天晚上8点の時刻で我关阳台灯をリマインドして`
  - `后天晚上8点に私へ我关阳台灯と伝えて`
  - `后天晚上8点用に我关阳台灯の通知を作って`

### S1-23 水费提醒

- Query: `明天晚上9点提醒我交水费`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `明天晚上9点提醒我我交水费`
  - `帮我设置一个提醒，明天晚上9点我交水费`
  - `请在明天晚上9点提醒我去我交水费`
  - `到明天晚上9点记得提醒我我交水费`
  - `我想在明天晚上9点收到提醒：我交水费`
  - `请给我设一个明天晚上9点的提醒，内容是我交水费`
  - `明天晚上9点帮我提醒一下我交水费`
  - `记得在明天晚上9点提醒我我交水费`
  - `请添加提醒：明天晚上9点我交水费`
  - `到明天晚上9点通知我我交水费`

- English Variants: 10
  - `Remind me 明天晚上9点 to 我交水费.`
  - `Set a reminder 明天晚上9点 for me to 我交水费.`
  - `Please remind me 明天晚上9点 that I need to 我交水费.`
  - `Can you create a reminder 明天晚上9点 for 我交水费?`
  - `I need a reminder 明天晚上9点 to 我交水费.`
  - `Put in a reminder for 明天晚上9点: 我交水费.`
  - `Schedule a reminder 明天晚上9点 so I remember to 我交水费.`
  - `Please alert me 明天晚上9点 to 我交水费.`
  - `Set me a 明天晚上9点 reminder to 我交水费.`
  - `Create a reminder telling me 明天晚上9点 to 我交水费.`

- Japanese Variants: 10
  - `明天晚上9点に我交水费とリマインドして`
  - `明天晚上9点に我交水费ことを知らせて`
  - `明天晚上9点用に「我交水费」のリマインダーを設定して`
  - `明天晚上9点になったら我交水费と通知して`
  - `明天晚上9点のリマインダーとして我交水费を登録して`
  - `明天晚上9点に我交水费の通知を入れて`
  - `明天晚上9点に我交水费ことを忘れないよう知らせて`
  - `明天晚上9点の時刻で我交水费をリマインドして`
  - `明天晚上9点に私へ我交水费と伝えて`
  - `明天晚上9点用に我交水费の通知を作って`

### S1-24 提醒列表

- Query: `提醒列表`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `提醒列表`
  - `查看提醒列表`
  - `把提醒列表给我看看`
  - `显示一下当前提醒`
  - `我想看提醒事项`
  - `列出所有提醒`
  - `帮我打开提醒列表`
  - `看看有哪些提醒`
  - `现在的提醒都有什么`
  - `把我的提醒展示一下`

- English Variants: 10
  - `Show me my reminder list.`
  - `List all reminders.`
  - `What reminders do I have?`
  - `Can you display my reminders?`
  - `Please show the current reminders.`
  - `I want to check my reminder list.`
  - `Open the reminder list for me.`
  - `Please tell me all active reminders.`
  - `What is on my reminders list?`
  - `Let me see the reminders.`

- Japanese Variants: 10
  - `リマインダー一覧を見せて`
  - `今のリマインダーを表示して`
  - `リマインダーのリストを確認したい`
  - `登録済みのリマインダーを教えて`
  - `リマインダー一覧を開いて`
  - `いま入っているリマインダーを見たい`
  - `リマインダーを全部表示して`
  - `現在の通知予定を見せて`
  - `リマインダー内容を確認して`
  - `登録中のリマインダー一覧を出して`

### S1-25 双提醒列表

- Query: `提醒列表`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `提醒列表`
  - `查看提醒列表`
  - `把提醒列表给我看看`
  - `显示一下当前提醒`
  - `我想看提醒事项`
  - `列出所有提醒`
  - `帮我打开提醒列表`
  - `看看有哪些提醒`
  - `现在的提醒都有什么`
  - `把我的提醒展示一下`

- English Variants: 10
  - `Show me my reminder list.`
  - `List all reminders.`
  - `What reminders do I have?`
  - `Can you display my reminders?`
  - `Please show the current reminders.`
  - `I want to check my reminder list.`
  - `Open the reminder list for me.`
  - `Please tell me all active reminders.`
  - `What is on my reminders list?`
  - `Let me see the reminders.`

- Japanese Variants: 10
  - `リマインダー一覧を見せて`
  - `今のリマインダーを表示して`
  - `リマインダーのリストを確認したい`
  - `登録済みのリマインダーを教えて`
  - `リマインダー一覧を開いて`
  - `いま入っているリマインダーを見たい`
  - `リマインダーを全部表示して`
  - `現在の通知予定を見せて`
  - `リマインダー内容を確認して`
  - `登録中のリマインダー一覧を出して`

### S1-26 家庭会议日程

- Query: `明天下午3点安排家庭会议，并提前30分钟提醒我`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `明天下午3点安排家庭会议，提前30分钟提醒我`
  - `帮我把家庭会议安排在明天下午3点，并提前30分钟提醒`
  - `请在明天下午3点安排家庭会议，记得提前30分钟通知我`
  - `把家庭会议加到明天下午3点的日程里，并在前30分钟提醒我`
  - `我想在明天下午3点安排家庭会议，提前30分钟给我提醒`
  - `请帮我预约明天下午3点的家庭会议，并提前30分钟提醒`
  - `在明天下午3点创建家庭会议日程，提前30分钟通知我`
  - `把家庭会议定在明天下午3点，并设置提前30分钟提醒`
  - `请安排明天下午3点的家庭会议，到时前30分钟提醒我`
  - `帮我新增家庭会议这个安排，时间是明天下午3点，提醒提前30分钟`

- English Variants: 10
  - `Schedule 家庭会议 明天下午3点 and remind me 30 minutes early.`
  - `Please add 家庭会议 for 明天下午3点, with a reminder 30 minutes before.`
  - `Set up 家庭会议 明天下午3点 and alert me 30 minutes in advance.`
  - `Can you schedule 家庭会议 明天下午3点 and remind me 30 minutes ahead of time?`
  - `Put 家庭会议 on the schedule for 明天下午3点 and send a 30-minute early reminder.`
  - `Arrange 家庭会议 明天下午3点, and make sure I get a reminder 30 minutes before.`
  - `Create a schedule entry for 家庭会议 明天下午3点 with a 30-minute advance reminder.`
  - `Please add 家庭会议 at 明天下午3点 and notify me 30 minutes beforehand.`
  - `Book 家庭会议 for 明天下午3点 and remind me 30 minutes before it starts.`
  - `Set 家庭会议 for 明天下午3点 and give me an alert 30 minutes early.`

- Japanese Variants: 10
  - `明天下午3点に家庭会议を予定に入れて、30分前に知らせて`
  - `明天下午3点の家庭会议を登録して、30分前にリマインドして`
  - `明天下午3点に家庭会议を設定し、30分前に通知して`
  - `明天下午3点の予定として家庭会议を追加して、30分前に教えて`
  - `家庭会议を明天下午3点に入れて、30分前に知らせてください`
  - `明天下午3点の家庭会议をスケジュールして、30分前に通知して`
  - `明天下午3点に家庭会议を登録して、事前に30分前で知らせて`
  - `明天下午3点の家庭会议を予定表に入れ、30分前にリマインドして`
  - `家庭会议を明天下午3点に追加して、30分前の通知を設定して`
  - `明天下午3点に家庭会议を予定登録し、30分前に教えて`

### S1-27 家长会日程

- Query: `后天下午4点安排家长会，并提前30分钟提醒我`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `后天下午4点安排家长会，提前30分钟提醒我`
  - `帮我把家长会安排在后天下午4点，并提前30分钟提醒`
  - `请在后天下午4点安排家长会，记得提前30分钟通知我`
  - `把家长会加到后天下午4点的日程里，并在前30分钟提醒我`
  - `我想在后天下午4点安排家长会，提前30分钟给我提醒`
  - `请帮我预约后天下午4点的家长会，并提前30分钟提醒`
  - `在后天下午4点创建家长会日程，提前30分钟通知我`
  - `把家长会定在后天下午4点，并设置提前30分钟提醒`
  - `请安排后天下午4点的家长会，到时前30分钟提醒我`
  - `帮我新增家长会这个安排，时间是后天下午4点，提醒提前30分钟`

- English Variants: 10
  - `Schedule 家长会 后天下午4点 and remind me 30 minutes early.`
  - `Please add 家长会 for 后天下午4点, with a reminder 30 minutes before.`
  - `Set up 家长会 后天下午4点 and alert me 30 minutes in advance.`
  - `Can you schedule 家长会 后天下午4点 and remind me 30 minutes ahead of time?`
  - `Put 家长会 on the schedule for 后天下午4点 and send a 30-minute early reminder.`
  - `Arrange 家长会 后天下午4点, and make sure I get a reminder 30 minutes before.`
  - `Create a schedule entry for 家长会 后天下午4点 with a 30-minute advance reminder.`
  - `Please add 家长会 at 后天下午4点 and notify me 30 minutes beforehand.`
  - `Book 家长会 for 后天下午4点 and remind me 30 minutes before it starts.`
  - `Set 家长会 for 后天下午4点 and give me an alert 30 minutes early.`

- Japanese Variants: 10
  - `后天下午4点に家长会を予定に入れて、30分前に知らせて`
  - `后天下午4点の家长会を登録して、30分前にリマインドして`
  - `后天下午4点に家长会を設定し、30分前に通知して`
  - `后天下午4点の予定として家长会を追加して、30分前に教えて`
  - `家长会を后天下午4点に入れて、30分前に知らせてください`
  - `后天下午4点の家长会をスケジュールして、30分前に通知して`
  - `后天下午4点に家长会を登録して、事前に30分前で知らせて`
  - `后天下午4点の家长会を予定表に入れ、30分前にリマインドして`
  - `家长会を后天下午4点に追加して、30分前の通知を設定して`
  - `后天下午4点に家长会を予定登録し、30分前に教えて`

### S1-28 查看日程

- Query: `查看日程`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `查看日程`
  - `看一下日程安排`
  - `帮我打开日程`
  - `显示一下日程`
  - `我想看今天的日程`
  - `列出当前日程`
  - `把日程安排给我看看`
  - `查看一下日历安排`
  - `看看接下来的安排`
  - `帮我展示日程表`

- English Variants: 10
  - `Show me the schedule.`
  - `Open my schedule.`
  - `Let me see today's schedule.`
  - `Can you display the calendar?`
  - `Please show the agenda.`
  - `I want to check the schedule.`
  - `What's on the calendar?`
  - `Please pull up the schedule.`
  - `Show the upcoming schedule.`
  - `Let me look at the agenda.`

- Japanese Variants: 10
  - `予定を見せて`
  - `スケジュールを開いて`
  - `日程を確認したい`
  - `今の予定表を表示して`
  - `カレンダー予定を見せて`
  - `予定一覧を出して`
  - `これからの予定を確認して`
  - `スケジュール内容を教えて`
  - `日程表を見たい`
  - `登録されている予定を表示して`

### S1-29 奶奶吃药提醒

- Query: `明天早上8点提醒奶奶吃药`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `明天早上8点提醒我奶奶吃药`
  - `帮我设置一个提醒，明天早上8点奶奶吃药`
  - `请在明天早上8点提醒我去奶奶吃药`
  - `到明天早上8点记得提醒我奶奶吃药`
  - `我想在明天早上8点收到提醒：奶奶吃药`
  - `请给我设一个明天早上8点的提醒，内容是奶奶吃药`
  - `明天早上8点帮我提醒一下奶奶吃药`
  - `记得在明天早上8点提醒我奶奶吃药`
  - `请添加提醒：明天早上8点奶奶吃药`
  - `到明天早上8点通知我奶奶吃药`

- English Variants: 10
  - `Remind me 明天早上8点 to 奶奶吃药.`
  - `Set a reminder 明天早上8点 for me to 奶奶吃药.`
  - `Please remind me 明天早上8点 that I need to 奶奶吃药.`
  - `Can you create a reminder 明天早上8点 for 奶奶吃药?`
  - `I need a reminder 明天早上8点 to 奶奶吃药.`
  - `Put in a reminder for 明天早上8点: 奶奶吃药.`
  - `Schedule a reminder 明天早上8点 so I remember to 奶奶吃药.`
  - `Please alert me 明天早上8点 to 奶奶吃药.`
  - `Set me a 明天早上8点 reminder to 奶奶吃药.`
  - `Create a reminder telling me 明天早上8点 to 奶奶吃药.`

- Japanese Variants: 10
  - `明天早上8点に奶奶吃药とリマインドして`
  - `明天早上8点に奶奶吃药ことを知らせて`
  - `明天早上8点用に「奶奶吃药」のリマインダーを設定して`
  - `明天早上8点になったら奶奶吃药と通知して`
  - `明天早上8点のリマインダーとして奶奶吃药を登録して`
  - `明天早上8点に奶奶吃药の通知を入れて`
  - `明天早上8点に奶奶吃药ことを忘れないよう知らせて`
  - `明天早上8点の時刻で奶奶吃药をリマインドして`
  - `明天早上8点に私へ奶奶吃药と伝えて`
  - `明天早上8点用に奶奶吃药の通知を作って`

### S1-30 倒垃圾提醒

- Query: `明天晚上9点提醒我倒垃圾`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `明天晚上9点提醒我我倒垃圾`
  - `帮我设置一个提醒，明天晚上9点我倒垃圾`
  - `请在明天晚上9点提醒我去我倒垃圾`
  - `到明天晚上9点记得提醒我我倒垃圾`
  - `我想在明天晚上9点收到提醒：我倒垃圾`
  - `请给我设一个明天晚上9点的提醒，内容是我倒垃圾`
  - `明天晚上9点帮我提醒一下我倒垃圾`
  - `记得在明天晚上9点提醒我我倒垃圾`
  - `请添加提醒：明天晚上9点我倒垃圾`
  - `到明天晚上9点通知我我倒垃圾`

- English Variants: 10
  - `Remind me 明天晚上9点 to 我倒垃圾.`
  - `Set a reminder 明天晚上9点 for me to 我倒垃圾.`
  - `Please remind me 明天晚上9点 that I need to 我倒垃圾.`
  - `Can you create a reminder 明天晚上9点 for 我倒垃圾?`
  - `I need a reminder 明天晚上9点 to 我倒垃圾.`
  - `Put in a reminder for 明天晚上9点: 我倒垃圾.`
  - `Schedule a reminder 明天晚上9点 so I remember to 我倒垃圾.`
  - `Please alert me 明天晚上9点 to 我倒垃圾.`
  - `Set me a 明天晚上9点 reminder to 我倒垃圾.`
  - `Create a reminder telling me 明天晚上9点 to 我倒垃圾.`

- Japanese Variants: 10
  - `明天晚上9点に我倒垃圾とリマインドして`
  - `明天晚上9点に我倒垃圾ことを知らせて`
  - `明天晚上9点用に「我倒垃圾」のリマインダーを設定して`
  - `明天晚上9点になったら我倒垃圾と通知して`
  - `明天晚上9点のリマインダーとして我倒垃圾を登録して`
  - `明天晚上9点に我倒垃圾の通知を入れて`
  - `明天晚上9点に我倒垃圾ことを忘れないよう知らせて`
  - `明天晚上9点の時刻で我倒垃圾をリマインドして`
  - `明天晚上9点に私へ我倒垃圾と伝えて`
  - `明天晚上9点用に我倒垃圾の通知を作って`

### S1-31 学校接送日程

- Query: `明天下午5点安排接孩子放学，并提前30分钟提醒我`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `明天下午5点安排接孩子放学，提前30分钟提醒我`
  - `帮我把接孩子放学安排在明天下午5点，并提前30分钟提醒`
  - `请在明天下午5点安排接孩子放学，记得提前30分钟通知我`
  - `把接孩子放学加到明天下午5点的日程里，并在前30分钟提醒我`
  - `我想在明天下午5点安排接孩子放学，提前30分钟给我提醒`
  - `请帮我预约明天下午5点的接孩子放学，并提前30分钟提醒`
  - `在明天下午5点创建接孩子放学日程，提前30分钟通知我`
  - `把接孩子放学定在明天下午5点，并设置提前30分钟提醒`
  - `请安排明天下午5点的接孩子放学，到时前30分钟提醒我`
  - `帮我新增接孩子放学这个安排，时间是明天下午5点，提醒提前30分钟`

- English Variants: 10
  - `Schedule 接孩子放学 明天下午5点 and remind me 30 minutes early.`
  - `Please add 接孩子放学 for 明天下午5点, with a reminder 30 minutes before.`
  - `Set up 接孩子放学 明天下午5点 and alert me 30 minutes in advance.`
  - `Can you schedule 接孩子放学 明天下午5点 and remind me 30 minutes ahead of time?`
  - `Put 接孩子放学 on the schedule for 明天下午5点 and send a 30-minute early reminder.`
  - `Arrange 接孩子放学 明天下午5点, and make sure I get a reminder 30 minutes before.`
  - `Create a schedule entry for 接孩子放学 明天下午5点 with a 30-minute advance reminder.`
  - `Please add 接孩子放学 at 明天下午5点 and notify me 30 minutes beforehand.`
  - `Book 接孩子放学 for 明天下午5点 and remind me 30 minutes before it starts.`
  - `Set 接孩子放学 for 明天下午5点 and give me an alert 30 minutes early.`

- Japanese Variants: 10
  - `明天下午5点に接孩子放学を予定に入れて、30分前に知らせて`
  - `明天下午5点の接孩子放学を登録して、30分前にリマインドして`
  - `明天下午5点に接孩子放学を設定し、30分前に通知して`
  - `明天下午5点の予定として接孩子放学を追加して、30分前に教えて`
  - `接孩子放学を明天下午5点に入れて、30分前に知らせてください`
  - `明天下午5点の接孩子放学をスケジュールして、30分前に通知して`
  - `明天下午5点に接孩子放学を登録して、事前に30分前で知らせて`
  - `明天下午5点の接孩子放学を予定表に入れ、30分前にリマインドして`
  - `接孩子放学を明天下午5点に追加して、30分前の通知を設定して`
  - `明天下午5点に接孩子放学を予定登録し、30分前に教えて`

### S1-32 日程与提醒总览

- Query: `查看日程`
- Expected: 完成提醒/日程操作。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `查看日程`
  - `看一下日程安排`
  - `帮我打开日程`
  - `显示一下日程`
  - `我想看今天的日程`
  - `列出当前日程`
  - `把日程安排给我看看`
  - `查看一下日历安排`
  - `看看接下来的安排`
  - `帮我展示日程表`

- English Variants: 10
  - `Show me the schedule.`
  - `Open my schedule.`
  - `Let me see today's schedule.`
  - `Can you display the calendar?`
  - `Please show the agenda.`
  - `I want to check the schedule.`
  - `What's on the calendar?`
  - `Please pull up the schedule.`
  - `Show the upcoming schedule.`
  - `Let me look at the agenda.`

- Japanese Variants: 10
  - `予定を見せて`
  - `スケジュールを開いて`
  - `日程を確認したい`
  - `今の予定表を表示して`
  - `カレンダー予定を見せて`
  - `予定一覧を出して`
  - `これからの予定を確認して`
  - `スケジュール内容を教えて`
  - `日程表を見たい`
  - `登録されている予定を表示して`

## 阶段2

### S2-01 家庭账单 创建草稿

- Query: `创建智能体，名称为家庭账单。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `创建一个名为家庭账单的智能体`
  - `帮我新建智能体，名字叫家庭账单`
  - `请创建智能体 家庭账单`
  - `我想创建一个叫家庭账单的智能体`
  - `新增智能体，名称设为家庭账单`
  - `请帮我建立名为家庭账单的智能体`
  - `创建新的自定义智能体：家庭账单`
  - `把智能体名称设成家庭账单并创建`
  - `帮我做一个家庭账单智能体`
  - `新建智能体，叫做家庭账单`

- English Variants: 10
  - `Create an agent named 家庭账单.`
  - `Please create a new agent called 家庭账单.`
  - `I want to make an agent named 家庭账单.`
  - `Set up an agent with the name 家庭账单.`
  - `Can you create the agent 家庭账单?`
  - `Please add a new agent named 家庭账单.`
  - `Create a custom agent called 家庭账单.`
  - `Help me create an agent named 家庭账单.`
  - `Make a new agent and name it 家庭账单.`
  - `Start creating an agent called 家庭账单.`

- Japanese Variants: 10
  - `家庭账单 という名前のエージェントを作って`
  - `家庭账单 というエージェントを新規作成して`
  - `家庭账单 名義でエージェントを作成して`
  - `家庭账单 というカスタムエージェントを作って`
  - `家庭账单 のエージェントを作りたい`
  - `家庭账单 を名前にしてエージェントを作って`
  - `家庭账单 という新しいエージェントを追加して`
  - `家庭账单 という名称で作成してください`
  - `家庭账单 のエージェントを立ち上げて`
  - `家庭账单 を名前とするエージェントを設定して`

### S2-02 家庭账单 补充需求

- Query: `可以通过语音，文字，OCR进行账单的记录。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `可以通过语音，文字，OCR进行账单的记录`
  - `它需要支持这样的能力：可以通过语音，文字，OCR进行账单的记录`
  - `请把这个能力加进去：可以通过语音，文字，OCR进行账单的记录`
  - `这个智能体要能做到：可以通过语音，文字，OCR进行账单的记录`
  - `我希望它具备这个功能：可以通过语音，文字，OCR进行账单的记录`
  - `请按这个用途来配置：可以通过语音，文字，OCR进行账单的记录`
  - `它的主要功能应该是：可以通过语音，文字，OCR进行账单的记录`
  - `请让它支持以下场景：可以通过语音，文字，OCR进行账单的记录`
  - `这个智能体的目标是：可以通过语音，文字，OCR进行账单的记录`
  - `能力要求如下：可以通过语音，文字，OCR进行账单的记录`

- English Variants: 10
  - `It should support this: 可以通过语音，文字，OCR进行账单的记录`
  - `Please make sure it can do the following: 可以通过语音，文字，OCR进行账单的记录`
  - `The agent needs this capability: 可以通过语音，文字，OCR进行账单的记录`
  - `This is the function I want it to have: 可以通过语音，文字，OCR进行账单的记录`
  - `It should be able to handle this: 可以通过语音，文字，OCR进行账单的记录`
  - `Please configure it for this use: 可以通过语音，文字，OCR进行账单的记录`
  - `I need the agent to cover this requirement: 可以通过语音，文字，OCR进行账单的记录`
  - `The intended capability is: 可以通过语音，文字，OCR进行账单的记录`
  - `Make it support the following scenario: 可以通过语音，文字，OCR进行账单的记录`
  - `This should be part of the agent behavior: 可以通过语音，文字，OCR进行账单的记录`

- Japanese Variants: 10
  - `可以通过语音，文字，OCR进行账单的记录`
  - `この機能を持たせてください: 可以通过语音，文字，OCR进行账单的记录`
  - `次の用途に対応できるようにして: 可以通过语音，文字，OCR进行账单的记录`
  - `このエージェントには次の役割が必要です: 可以通过语音，文字，OCR进行账单的记录`
  - `以下の機能をサポートしてほしいです: 可以通过语音，文字，OCR进行账单的记录`
  - `この用途で使えるように設定してください: 可以通过语音，文字，OCR进行账单的记录`
  - `次の内容に対応するエージェントにして: 可以通过语音，文字，OCR进行账单的记录`
  - `この能力を含めてください: 可以通过语音，文字，OCR进行账单的记录`
  - `想定している機能はこれです: 可以通过语音，文字，OCR进行账单的记录`
  - `この要件を満たすようにしてください: 可以通过语音，文字，OCR进行账单的记录`

### S2-03 家庭账单 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `确认创建`
  - `请确认创建`
  - `好的，创建吧`
  - `可以，开始创建`
  - `没问题，确认生成`
  - `继续创建`
  - `就按这个创建`
  - `确认并完成创建`
  - `请直接创建`
  - `可以，执行创建`

- English Variants: 10
  - `Confirm the creation.`
  - `Please go ahead and create it.`
  - `Yes, confirm creation.`
  - `That's good, create it now.`
  - `Proceed with the creation.`
  - `Please confirm and finish creating it.`
  - `Go ahead with creating it.`
  - `I confirm, please create it.`
  - `Create it as discussed.`
  - `Finalize the creation.`

- Japanese Variants: 10
  - `作成を確定して`
  - `この内容で作成して`
  - `はい、作成を進めて`
  - `そのまま作成して`
  - `問題ないので作成して`
  - `作成を確定してください`
  - `この設定で完成させて`
  - `その内容で作って`
  - `では作成を続けて`
  - `確定して作成して`

### S2-04 家庭提醒 创建草稿

- Query: `创建智能体，名称为家庭提醒。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `创建一个名为家庭提醒的智能体`
  - `帮我新建智能体，名字叫家庭提醒`
  - `请创建智能体 家庭提醒`
  - `我想创建一个叫家庭提醒的智能体`
  - `新增智能体，名称设为家庭提醒`
  - `请帮我建立名为家庭提醒的智能体`
  - `创建新的自定义智能体：家庭提醒`
  - `把智能体名称设成家庭提醒并创建`
  - `帮我做一个家庭提醒智能体`
  - `新建智能体，叫做家庭提醒`

- English Variants: 10
  - `Create an agent named 家庭提醒.`
  - `Please create a new agent called 家庭提醒.`
  - `I want to make an agent named 家庭提醒.`
  - `Set up an agent with the name 家庭提醒.`
  - `Can you create the agent 家庭提醒?`
  - `Please add a new agent named 家庭提醒.`
  - `Create a custom agent called 家庭提醒.`
  - `Help me create an agent named 家庭提醒.`
  - `Make a new agent and name it 家庭提醒.`
  - `Start creating an agent called 家庭提醒.`

- Japanese Variants: 10
  - `家庭提醒 という名前のエージェントを作って`
  - `家庭提醒 というエージェントを新規作成して`
  - `家庭提醒 名義でエージェントを作成して`
  - `家庭提醒 というカスタムエージェントを作って`
  - `家庭提醒 のエージェントを作りたい`
  - `家庭提醒 を名前にしてエージェントを作って`
  - `家庭提醒 という新しいエージェントを追加して`
  - `家庭提醒 という名称で作成してください`
  - `家庭提醒 のエージェントを立ち上げて`
  - `家庭提醒 を名前とするエージェントを設定して`

### S2-05 家庭提醒 补充需求

- Query: `可以按时间、人物和提醒方式管理家庭提醒。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `可以按时间、人物和提醒我方式管理家庭提醒`
  - `帮我设置一个提醒，可以按时间、人物和方式管理家庭提醒`
  - `请在可以按时间、人物和提醒我去方式管理家庭提醒`
  - `到可以按时间、人物和记得提醒我方式管理家庭提醒`
  - `我想在可以按时间、人物和收到提醒：方式管理家庭提醒`
  - `请给我设一个可以按时间、人物和的提醒，内容是方式管理家庭提醒`
  - `可以按时间、人物和帮我提醒一下方式管理家庭提醒`
  - `记得在可以按时间、人物和提醒我方式管理家庭提醒`
  - `请添加提醒：可以按时间、人物和方式管理家庭提醒`
  - `到可以按时间、人物和通知我方式管理家庭提醒`

- English Variants: 10
  - `Remind me 可以按时间、人物和 to 方式管理家庭提醒.`
  - `Set a reminder 可以按时间、人物和 for me to 方式管理家庭提醒.`
  - `Please remind me 可以按时间、人物和 that I need to 方式管理家庭提醒.`
  - `Can you create a reminder 可以按时间、人物和 for 方式管理家庭提醒?`
  - `I need a reminder 可以按时间、人物和 to 方式管理家庭提醒.`
  - `Put in a reminder for 可以按时间、人物和: 方式管理家庭提醒.`
  - `Schedule a reminder 可以按时间、人物和 so I remember to 方式管理家庭提醒.`
  - `Please alert me 可以按时间、人物和 to 方式管理家庭提醒.`
  - `Set me a 可以按时间、人物和 reminder to 方式管理家庭提醒.`
  - `Create a reminder telling me 可以按时间、人物和 to 方式管理家庭提醒.`

- Japanese Variants: 10
  - `可以按时间、人物和に方式管理家庭提醒とリマインドして`
  - `可以按时间、人物和に方式管理家庭提醒ことを知らせて`
  - `可以按时间、人物和用に「方式管理家庭提醒」のリマインダーを設定して`
  - `可以按时间、人物和になったら方式管理家庭提醒と通知して`
  - `可以按时间、人物和のリマインダーとして方式管理家庭提醒を登録して`
  - `可以按时间、人物和に方式管理家庭提醒の通知を入れて`
  - `可以按时间、人物和に方式管理家庭提醒ことを忘れないよう知らせて`
  - `可以按时间、人物和の時刻で方式管理家庭提醒をリマインドして`
  - `可以按时间、人物和に私へ方式管理家庭提醒と伝えて`
  - `可以按时间、人物和用に方式管理家庭提醒の通知を作って`

### S2-06 家庭提醒 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `确认创建`
  - `请确认创建`
  - `好的，创建吧`
  - `可以，开始创建`
  - `没问题，确认生成`
  - `继续创建`
  - `就按这个创建`
  - `确认并完成创建`
  - `请直接创建`
  - `可以，执行创建`

- English Variants: 10
  - `Confirm the creation.`
  - `Please go ahead and create it.`
  - `Yes, confirm creation.`
  - `That's good, create it now.`
  - `Proceed with the creation.`
  - `Please confirm and finish creating it.`
  - `Go ahead with creating it.`
  - `I confirm, please create it.`
  - `Create it as discussed.`
  - `Finalize the creation.`

- Japanese Variants: 10
  - `作成を確定して`
  - `この内容で作成して`
  - `はい、作成を進めて`
  - `そのまま作成して`
  - `問題ないので作成して`
  - `作成を確定してください`
  - `この設定で完成させて`
  - `その内容で作って`
  - `では作成を続けて`
  - `確定して作成して`

### S2-07 身体状况记录 创建草稿

- Query: `创建智能体，名称为身体状况记录。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `创建一个名为身体状况记录的智能体`
  - `帮我新建智能体，名字叫身体状况记录`
  - `请创建智能体 身体状况记录`
  - `我想创建一个叫身体状况记录的智能体`
  - `新增智能体，名称设为身体状况记录`
  - `请帮我建立名为身体状况记录的智能体`
  - `创建新的自定义智能体：身体状况记录`
  - `把智能体名称设成身体状况记录并创建`
  - `帮我做一个身体状况记录智能体`
  - `新建智能体，叫做身体状况记录`

- English Variants: 10
  - `Create an agent named 身体状况记录.`
  - `Please create a new agent called 身体状况记录.`
  - `I want to make an agent named 身体状况记录.`
  - `Set up an agent with the name 身体状况记录.`
  - `Can you create the agent 身体状况记录?`
  - `Please add a new agent named 身体状况记录.`
  - `Create a custom agent called 身体状况记录.`
  - `Help me create an agent named 身体状况记录.`
  - `Make a new agent and name it 身体状况记录.`
  - `Start creating an agent called 身体状况记录.`

- Japanese Variants: 10
  - `身体状况记录 という名前のエージェントを作って`
  - `身体状况记录 というエージェントを新規作成して`
  - `身体状况记录 名義でエージェントを作成して`
  - `身体状况记录 というカスタムエージェントを作って`
  - `身体状况记录 のエージェントを作りたい`
  - `身体状况记录 を名前にしてエージェントを作って`
  - `身体状况记录 という新しいエージェントを追加して`
  - `身体状况记录 という名称で作成してください`
  - `身体状况记录 のエージェントを立ち上げて`
  - `身体状况记录 を名前とするエージェントを設定して`

### S2-08 身体状况记录 补充需求

- Query: `用于记录家庭成员身体状况、体温和症状。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `用于记录家庭成员身体状况、体温和症状`
  - `它需要支持这样的能力：用于记录家庭成员身体状况、体温和症状`
  - `请把这个能力加进去：用于记录家庭成员身体状况、体温和症状`
  - `这个智能体要能做到：用于记录家庭成员身体状况、体温和症状`
  - `我希望它具备这个功能：用于记录家庭成员身体状况、体温和症状`
  - `请按这个用途来配置：用于记录家庭成员身体状况、体温和症状`
  - `它的主要功能应该是：用于记录家庭成员身体状况、体温和症状`
  - `请让它支持以下场景：用于记录家庭成员身体状况、体温和症状`
  - `这个智能体的目标是：用于记录家庭成员身体状况、体温和症状`
  - `能力要求如下：用于记录家庭成员身体状况、体温和症状`

- English Variants: 10
  - `It should support this: 用于记录家庭成员身体状况、体温和症状`
  - `Please make sure it can do the following: 用于记录家庭成员身体状况、体温和症状`
  - `The agent needs this capability: 用于记录家庭成员身体状况、体温和症状`
  - `This is the function I want it to have: 用于记录家庭成员身体状况、体温和症状`
  - `It should be able to handle this: 用于记录家庭成员身体状况、体温和症状`
  - `Please configure it for this use: 用于记录家庭成员身体状况、体温和症状`
  - `I need the agent to cover this requirement: 用于记录家庭成员身体状况、体温和症状`
  - `The intended capability is: 用于记录家庭成员身体状况、体温和症状`
  - `Make it support the following scenario: 用于记录家庭成员身体状况、体温和症状`
  - `This should be part of the agent behavior: 用于记录家庭成员身体状况、体温和症状`

- Japanese Variants: 10
  - `用于记录家庭成员身体状况、体温和症状`
  - `この機能を持たせてください: 用于记录家庭成员身体状况、体温和症状`
  - `次の用途に対応できるようにして: 用于记录家庭成员身体状况、体温和症状`
  - `このエージェントには次の役割が必要です: 用于记录家庭成员身体状况、体温和症状`
  - `以下の機能をサポートしてほしいです: 用于记录家庭成员身体状况、体温和症状`
  - `この用途で使えるように設定してください: 用于记录家庭成员身体状况、体温和症状`
  - `次の内容に対応するエージェントにして: 用于记录家庭成员身体状况、体温和症状`
  - `この能力を含めてください: 用于记录家庭成员身体状况、体温和症状`
  - `想定している機能はこれです: 用于记录家庭成员身体状况、体温和症状`
  - `この要件を満たすようにしてください: 用于记录家庭成员身体状况、体温和症状`

### S2-09 身体状况记录 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `确认创建`
  - `请确认创建`
  - `好的，创建吧`
  - `可以，开始创建`
  - `没问题，确认生成`
  - `继续创建`
  - `就按这个创建`
  - `确认并完成创建`
  - `请直接创建`
  - `可以，执行创建`

- English Variants: 10
  - `Confirm the creation.`
  - `Please go ahead and create it.`
  - `Yes, confirm creation.`
  - `That's good, create it now.`
  - `Proceed with the creation.`
  - `Please confirm and finish creating it.`
  - `Go ahead with creating it.`
  - `I confirm, please create it.`
  - `Create it as discussed.`
  - `Finalize the creation.`

- Japanese Variants: 10
  - `作成を確定して`
  - `この内容で作成して`
  - `はい、作成を進めて`
  - `そのまま作成して`
  - `問題ないので作成して`
  - `作成を確定してください`
  - `この設定で完成させて`
  - `その内容で作って`
  - `では作成を続けて`
  - `確定して作成して`

### S2-10 体检报告 创建草稿

- Query: `创建智能体，名称为体检报告。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `创建一个名为体检报告的智能体`
  - `帮我新建智能体，名字叫体检报告`
  - `请创建智能体 体检报告`
  - `我想创建一个叫体检报告的智能体`
  - `新增智能体，名称设为体检报告`
  - `请帮我建立名为体检报告的智能体`
  - `创建新的自定义智能体：体检报告`
  - `把智能体名称设成体检报告并创建`
  - `帮我做一个体检报告智能体`
  - `新建智能体，叫做体检报告`

- English Variants: 10
  - `Create an agent named 体检报告.`
  - `Please create a new agent called 体检报告.`
  - `I want to make an agent named 体检报告.`
  - `Set up an agent with the name 体检报告.`
  - `Can you create the agent 体检报告?`
  - `Please add a new agent named 体检报告.`
  - `Create a custom agent called 体检报告.`
  - `Help me create an agent named 体检报告.`
  - `Make a new agent and name it 体检报告.`
  - `Start creating an agent called 体检报告.`

- Japanese Variants: 10
  - `体检报告 という名前のエージェントを作って`
  - `体检报告 というエージェントを新規作成して`
  - `体检报告 名義でエージェントを作成して`
  - `体检报告 というカスタムエージェントを作って`
  - `体检报告 のエージェントを作りたい`
  - `体检报告 を名前にしてエージェントを作って`
  - `体检报告 という新しいエージェントを追加して`
  - `体检报告 という名称で作成してください`
  - `体检报告 のエージェントを立ち上げて`
  - `体检报告 を名前とするエージェントを設定して`

### S2-11 体检报告 补充需求

- Query: `用于记录医院检查项目、结果和复查时间。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `用于记录医院检查项目、结果和复查时间`
  - `它需要支持这样的能力：用于记录医院检查项目、结果和复查时间`
  - `请把这个能力加进去：用于记录医院检查项目、结果和复查时间`
  - `这个智能体要能做到：用于记录医院检查项目、结果和复查时间`
  - `我希望它具备这个功能：用于记录医院检查项目、结果和复查时间`
  - `请按这个用途来配置：用于记录医院检查项目、结果和复查时间`
  - `它的主要功能应该是：用于记录医院检查项目、结果和复查时间`
  - `请让它支持以下场景：用于记录医院检查项目、结果和复查时间`
  - `这个智能体的目标是：用于记录医院检查项目、结果和复查时间`
  - `能力要求如下：用于记录医院检查项目、结果和复查时间`

- English Variants: 10
  - `It should support this: 用于记录医院检查项目、结果和复查时间`
  - `Please make sure it can do the following: 用于记录医院检查项目、结果和复查时间`
  - `The agent needs this capability: 用于记录医院检查项目、结果和复查时间`
  - `This is the function I want it to have: 用于记录医院检查项目、结果和复查时间`
  - `It should be able to handle this: 用于记录医院检查项目、结果和复查时间`
  - `Please configure it for this use: 用于记录医院检查项目、结果和复查时间`
  - `I need the agent to cover this requirement: 用于记录医院检查项目、结果和复查时间`
  - `The intended capability is: 用于记录医院检查项目、结果和复查时间`
  - `Make it support the following scenario: 用于记录医院检查项目、结果和复查时间`
  - `This should be part of the agent behavior: 用于记录医院检查项目、结果和复查时间`

- Japanese Variants: 10
  - `用于记录医院检查项目、结果和复查时间`
  - `この機能を持たせてください: 用于记录医院检查项目、结果和复查时间`
  - `次の用途に対応できるようにして: 用于记录医院检查项目、结果和复查时间`
  - `このエージェントには次の役割が必要です: 用于记录医院检查项目、结果和复查时间`
  - `以下の機能をサポートしてほしいです: 用于记录医院检查项目、结果和复查时间`
  - `この用途で使えるように設定してください: 用于记录医院检查项目、结果和复查时间`
  - `次の内容に対応するエージェントにして: 用于记录医院检查项目、结果和复查时间`
  - `この能力を含めてください: 用于记录医院检查项目、结果和复查时间`
  - `想定している機能はこれです: 用于记录医院检查项目、结果和复查时间`
  - `この要件を満たすようにしてください: 用于记录医院检查项目、结果和复查时间`

### S2-12 体检报告 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `确认创建`
  - `请确认创建`
  - `好的，创建吧`
  - `可以，开始创建`
  - `没问题，确认生成`
  - `继续创建`
  - `就按这个创建`
  - `确认并完成创建`
  - `请直接创建`
  - `可以，执行创建`

- English Variants: 10
  - `Confirm the creation.`
  - `Please go ahead and create it.`
  - `Yes, confirm creation.`
  - `That's good, create it now.`
  - `Proceed with the creation.`
  - `Please confirm and finish creating it.`
  - `Go ahead with creating it.`
  - `I confirm, please create it.`
  - `Create it as discussed.`
  - `Finalize the creation.`

- Japanese Variants: 10
  - `作成を確定して`
  - `この内容で作成して`
  - `はい、作成を進めて`
  - `そのまま作成して`
  - `問題ないので作成して`
  - `作成を確定してください`
  - `この設定で完成させて`
  - `その内容で作って`
  - `では作成を続けて`
  - `確定して作成して`

### S2-13 医院复查提醒 创建草稿

- Query: `创建智能体，名称为医院复查提醒。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `创建一个名为医院复查提醒的智能体`
  - `帮我新建智能体，名字叫医院复查提醒`
  - `请创建智能体 医院复查提醒`
  - `我想创建一个叫医院复查提醒的智能体`
  - `新增智能体，名称设为医院复查提醒`
  - `请帮我建立名为医院复查提醒的智能体`
  - `创建新的自定义智能体：医院复查提醒`
  - `把智能体名称设成医院复查提醒并创建`
  - `帮我做一个医院复查提醒智能体`
  - `新建智能体，叫做医院复查提醒`

- English Variants: 10
  - `Create an agent named 医院复查提醒.`
  - `Please create a new agent called 医院复查提醒.`
  - `I want to make an agent named 医院复查提醒.`
  - `Set up an agent with the name 医院复查提醒.`
  - `Can you create the agent 医院复查提醒?`
  - `Please add a new agent named 医院复查提醒.`
  - `Create a custom agent called 医院复查提醒.`
  - `Help me create an agent named 医院复查提醒.`
  - `Make a new agent and name it 医院复查提醒.`
  - `Start creating an agent called 医院复查提醒.`

- Japanese Variants: 10
  - `医院复查提醒 という名前のエージェントを作って`
  - `医院复查提醒 というエージェントを新規作成して`
  - `医院复查提醒 名義でエージェントを作成して`
  - `医院复查提醒 というカスタムエージェントを作って`
  - `医院复查提醒 のエージェントを作りたい`
  - `医院复查提醒 を名前にしてエージェントを作って`
  - `医院复查提醒 という新しいエージェントを追加して`
  - `医院复查提醒 という名称で作成してください`
  - `医院复查提醒 のエージェントを立ち上げて`
  - `医院复查提醒 を名前とするエージェントを設定して`

### S2-14 医院复查提醒 补充需求

- Query: `用于记录医院复查时间并提醒家人。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `用于记录医院复查时间并提醒我家人`
  - `帮我设置一个提醒，用于记录医院复查时间并家人`
  - `请在用于记录医院复查时间并提醒我去家人`
  - `到用于记录医院复查时间并记得提醒我家人`
  - `我想在用于记录医院复查时间并收到提醒：家人`
  - `请给我设一个用于记录医院复查时间并的提醒，内容是家人`
  - `用于记录医院复查时间并帮我提醒一下家人`
  - `记得在用于记录医院复查时间并提醒我家人`
  - `请添加提醒：用于记录医院复查时间并家人`
  - `到用于记录医院复查时间并通知我家人`

- English Variants: 10
  - `Remind me 用于记录医院复查时间并 to 家人.`
  - `Set a reminder 用于记录医院复查时间并 for me to 家人.`
  - `Please remind me 用于记录医院复查时间并 that I need to 家人.`
  - `Can you create a reminder 用于记录医院复查时间并 for 家人?`
  - `I need a reminder 用于记录医院复查时间并 to 家人.`
  - `Put in a reminder for 用于记录医院复查时间并: 家人.`
  - `Schedule a reminder 用于记录医院复查时间并 so I remember to 家人.`
  - `Please alert me 用于记录医院复查时间并 to 家人.`
  - `Set me a 用于记录医院复查时间并 reminder to 家人.`
  - `Create a reminder telling me 用于记录医院复查时间并 to 家人.`

- Japanese Variants: 10
  - `用于记录医院复查时间并に家人とリマインドして`
  - `用于记录医院复查时间并に家人ことを知らせて`
  - `用于记录医院复查时间并用に「家人」のリマインダーを設定して`
  - `用于记录医院复查时间并になったら家人と通知して`
  - `用于记录医院复查时间并のリマインダーとして家人を登録して`
  - `用于记录医院复查时间并に家人の通知を入れて`
  - `用于记录医院复查时间并に家人ことを忘れないよう知らせて`
  - `用于记录医院复查时间并の時刻で家人をリマインドして`
  - `用于记录医院复查时间并に私へ家人と伝えて`
  - `用于记录医院复查时间并用に家人の通知を作って`

### S2-15 医院复查提醒 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `确认创建`
  - `请确认创建`
  - `好的，创建吧`
  - `可以，开始创建`
  - `没问题，确认生成`
  - `继续创建`
  - `就按这个创建`
  - `确认并完成创建`
  - `请直接创建`
  - `可以，执行创建`

- English Variants: 10
  - `Confirm the creation.`
  - `Please go ahead and create it.`
  - `Yes, confirm creation.`
  - `That's good, create it now.`
  - `Proceed with the creation.`
  - `Please confirm and finish creating it.`
  - `Go ahead with creating it.`
  - `I confirm, please create it.`
  - `Create it as discussed.`
  - `Finalize the creation.`

- Japanese Variants: 10
  - `作成を確定して`
  - `この内容で作成して`
  - `はい、作成を進めて`
  - `そのまま作成して`
  - `問題ないので作成して`
  - `作成を確定してください`
  - `この設定で完成させて`
  - `その内容で作って`
  - `では作成を続けて`
  - `確定して作成して`

### S2-16 孩子学习计划 创建草稿

- Query: `创建智能体，名称为孩子学习计划。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `创建一个名为孩子学习计划的智能体`
  - `帮我新建智能体，名字叫孩子学习计划`
  - `请创建智能体 孩子学习计划`
  - `我想创建一个叫孩子学习计划的智能体`
  - `新增智能体，名称设为孩子学习计划`
  - `请帮我建立名为孩子学习计划的智能体`
  - `创建新的自定义智能体：孩子学习计划`
  - `把智能体名称设成孩子学习计划并创建`
  - `帮我做一个孩子学习计划智能体`
  - `新建智能体，叫做孩子学习计划`

- English Variants: 10
  - `Create an agent named 孩子学习计划.`
  - `Please create a new agent called 孩子学习计划.`
  - `I want to make an agent named 孩子学习计划.`
  - `Set up an agent with the name 孩子学习计划.`
  - `Can you create the agent 孩子学习计划?`
  - `Please add a new agent named 孩子学习计划.`
  - `Create a custom agent called 孩子学习计划.`
  - `Help me create an agent named 孩子学习计划.`
  - `Make a new agent and name it 孩子学习计划.`
  - `Start creating an agent called 孩子学习计划.`

- Japanese Variants: 10
  - `孩子学习计划 という名前のエージェントを作って`
  - `孩子学习计划 というエージェントを新規作成して`
  - `孩子学习计划 名義でエージェントを作成して`
  - `孩子学习计划 というカスタムエージェントを作って`
  - `孩子学习计划 のエージェントを作りたい`
  - `孩子学习计划 を名前にしてエージェントを作って`
  - `孩子学习计划 という新しいエージェントを追加して`
  - `孩子学习计划 という名称で作成してください`
  - `孩子学习计划 のエージェントを立ち上げて`
  - `孩子学习计划 を名前とするエージェントを設定して`

### S2-17 孩子学习计划 补充需求

- Query: `用于记录孩子学习科目、作业和老师反馈。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `用于记录孩子学习科目、作业和老师反馈`
  - `它需要支持这样的能力：用于记录孩子学习科目、作业和老师反馈`
  - `请把这个能力加进去：用于记录孩子学习科目、作业和老师反馈`
  - `这个智能体要能做到：用于记录孩子学习科目、作业和老师反馈`
  - `我希望它具备这个功能：用于记录孩子学习科目、作业和老师反馈`
  - `请按这个用途来配置：用于记录孩子学习科目、作业和老师反馈`
  - `它的主要功能应该是：用于记录孩子学习科目、作业和老师反馈`
  - `请让它支持以下场景：用于记录孩子学习科目、作业和老师反馈`
  - `这个智能体的目标是：用于记录孩子学习科目、作业和老师反馈`
  - `能力要求如下：用于记录孩子学习科目、作业和老师反馈`

- English Variants: 10
  - `It should support this: 用于记录孩子学习科目、作业和老师反馈`
  - `Please make sure it can do the following: 用于记录孩子学习科目、作业和老师反馈`
  - `The agent needs this capability: 用于记录孩子学习科目、作业和老师反馈`
  - `This is the function I want it to have: 用于记录孩子学习科目、作业和老师反馈`
  - `It should be able to handle this: 用于记录孩子学习科目、作业和老师反馈`
  - `Please configure it for this use: 用于记录孩子学习科目、作业和老师反馈`
  - `I need the agent to cover this requirement: 用于记录孩子学习科目、作业和老师反馈`
  - `The intended capability is: 用于记录孩子学习科目、作业和老师反馈`
  - `Make it support the following scenario: 用于记录孩子学习科目、作业和老师反馈`
  - `This should be part of the agent behavior: 用于记录孩子学习科目、作业和老师反馈`

- Japanese Variants: 10
  - `用于记录孩子学习科目、作业和老师反馈`
  - `この機能を持たせてください: 用于记录孩子学习科目、作业和老师反馈`
  - `次の用途に対応できるようにして: 用于记录孩子学习科目、作业和老师反馈`
  - `このエージェントには次の役割が必要です: 用于记录孩子学习科目、作业和老师反馈`
  - `以下の機能をサポートしてほしいです: 用于记录孩子学习科目、作业和老师反馈`
  - `この用途で使えるように設定してください: 用于记录孩子学习科目、作业和老师反馈`
  - `次の内容に対応するエージェントにして: 用于记录孩子学习科目、作业和老师反馈`
  - `この能力を含めてください: 用于记录孩子学习科目、作业和老师反馈`
  - `想定している機能はこれです: 用于记录孩子学习科目、作业和老师反馈`
  - `この要件を満たすようにしてください: 用于记录孩子学习科目、作业和老师反馈`

### S2-18 孩子学习计划 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `确认创建`
  - `请确认创建`
  - `好的，创建吧`
  - `可以，开始创建`
  - `没问题，确认生成`
  - `继续创建`
  - `就按这个创建`
  - `确认并完成创建`
  - `请直接创建`
  - `可以，执行创建`

- English Variants: 10
  - `Confirm the creation.`
  - `Please go ahead and create it.`
  - `Yes, confirm creation.`
  - `That's good, create it now.`
  - `Proceed with the creation.`
  - `Please confirm and finish creating it.`
  - `Go ahead with creating it.`
  - `I confirm, please create it.`
  - `Create it as discussed.`
  - `Finalize the creation.`

- Japanese Variants: 10
  - `作成を確定して`
  - `この内容で作成して`
  - `はい、作成を進めて`
  - `そのまま作成して`
  - `問題ないので作成して`
  - `作成を確定してください`
  - `この設定で完成させて`
  - `その内容で作って`
  - `では作成を続けて`
  - `確定して作成して`

### S2-19 家庭活动安排 创建草稿

- Query: `创建智能体，名称为家庭活动安排。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `创建一个名为家庭活动安排的智能体`
  - `帮我新建智能体，名字叫家庭活动安排`
  - `请创建智能体 家庭活动安排`
  - `我想创建一个叫家庭活动安排的智能体`
  - `新增智能体，名称设为家庭活动安排`
  - `请帮我建立名为家庭活动安排的智能体`
  - `创建新的自定义智能体：家庭活动安排`
  - `把智能体名称设成家庭活动安排并创建`
  - `帮我做一个家庭活动安排智能体`
  - `新建智能体，叫做家庭活动安排`

- English Variants: 10
  - `Create an agent named 家庭活动安排.`
  - `Please create a new agent called 家庭活动安排.`
  - `I want to make an agent named 家庭活动安排.`
  - `Set up an agent with the name 家庭活动安排.`
  - `Can you create the agent 家庭活动安排?`
  - `Please add a new agent named 家庭活动安排.`
  - `Create a custom agent called 家庭活动安排.`
  - `Help me create an agent named 家庭活动安排.`
  - `Make a new agent and name it 家庭活动安排.`
  - `Start creating an agent called 家庭活动安排.`

- Japanese Variants: 10
  - `家庭活动安排 という名前のエージェントを作って`
  - `家庭活动安排 というエージェントを新規作成して`
  - `家庭活动安排 名義でエージェントを作成して`
  - `家庭活动安排 というカスタムエージェントを作って`
  - `家庭活动安排 のエージェントを作りたい`
  - `家庭活动安排 を名前にしてエージェントを作って`
  - `家庭活动安排 という新しいエージェントを追加して`
  - `家庭活动安排 という名称で作成してください`
  - `家庭活动安排 のエージェントを立ち上げて`
  - `家庭活动安排 を名前とするエージェントを設定して`

### S2-20 家庭活动安排 补充需求

- Query: `用于记录家庭活动时间、地点和参与成员。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `用于记录家庭活动时间、地点和参与成员`
  - `它需要支持这样的能力：用于记录家庭活动时间、地点和参与成员`
  - `请把这个能力加进去：用于记录家庭活动时间、地点和参与成员`
  - `这个智能体要能做到：用于记录家庭活动时间、地点和参与成员`
  - `我希望它具备这个功能：用于记录家庭活动时间、地点和参与成员`
  - `请按这个用途来配置：用于记录家庭活动时间、地点和参与成员`
  - `它的主要功能应该是：用于记录家庭活动时间、地点和参与成员`
  - `请让它支持以下场景：用于记录家庭活动时间、地点和参与成员`
  - `这个智能体的目标是：用于记录家庭活动时间、地点和参与成员`
  - `能力要求如下：用于记录家庭活动时间、地点和参与成员`

- English Variants: 10
  - `It should support this: 用于记录家庭活动时间、地点和参与成员`
  - `Please make sure it can do the following: 用于记录家庭活动时间、地点和参与成员`
  - `The agent needs this capability: 用于记录家庭活动时间、地点和参与成员`
  - `This is the function I want it to have: 用于记录家庭活动时间、地点和参与成员`
  - `It should be able to handle this: 用于记录家庭活动时间、地点和参与成员`
  - `Please configure it for this use: 用于记录家庭活动时间、地点和参与成员`
  - `I need the agent to cover this requirement: 用于记录家庭活动时间、地点和参与成员`
  - `The intended capability is: 用于记录家庭活动时间、地点和参与成员`
  - `Make it support the following scenario: 用于记录家庭活动时间、地点和参与成员`
  - `This should be part of the agent behavior: 用于记录家庭活动时间、地点和参与成员`

- Japanese Variants: 10
  - `用于记录家庭活动时间、地点和参与成员`
  - `この機能を持たせてください: 用于记录家庭活动时间、地点和参与成员`
  - `次の用途に対応できるようにして: 用于记录家庭活动时间、地点和参与成员`
  - `このエージェントには次の役割が必要です: 用于记录家庭活动时间、地点和参与成员`
  - `以下の機能をサポートしてほしいです: 用于记录家庭活动时间、地点和参与成员`
  - `この用途で使えるように設定してください: 用于记录家庭活动时间、地点和参与成员`
  - `次の内容に対応するエージェントにして: 用于记录家庭活动时间、地点和参与成员`
  - `この能力を含めてください: 用于记录家庭活动时间、地点和参与成员`
  - `想定している機能はこれです: 用于记录家庭活动时间、地点和参与成员`
  - `この要件を満たすようにしてください: 用于记录家庭活动时间、地点和参与成员`

### S2-21 家庭活动安排 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `确认创建`
  - `请确认创建`
  - `好的，创建吧`
  - `可以，开始创建`
  - `没问题，确认生成`
  - `继续创建`
  - `就按这个创建`
  - `确认并完成创建`
  - `请直接创建`
  - `可以，执行创建`

- English Variants: 10
  - `Confirm the creation.`
  - `Please go ahead and create it.`
  - `Yes, confirm creation.`
  - `That's good, create it now.`
  - `Proceed with the creation.`
  - `Please confirm and finish creating it.`
  - `Go ahead with creating it.`
  - `I confirm, please create it.`
  - `Create it as discussed.`
  - `Finalize the creation.`

- Japanese Variants: 10
  - `作成を確定して`
  - `この内容で作成して`
  - `はい、作成を進めて`
  - `そのまま作成して`
  - `問題ないので作成して`
  - `作成を確定してください`
  - `この設定で完成させて`
  - `その内容で作って`
  - `では作成を続けて`
  - `確定して作成して`

### S2-22 家庭日程安排 创建草稿

- Query: `创建智能体，名称为家庭日程安排。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `创建一个名为家庭日程安排的智能体`
  - `帮我新建智能体，名字叫家庭日程安排`
  - `请创建智能体 家庭日程安排`
  - `我想创建一个叫家庭日程安排的智能体`
  - `新增智能体，名称设为家庭日程安排`
  - `请帮我建立名为家庭日程安排的智能体`
  - `创建新的自定义智能体：家庭日程安排`
  - `把智能体名称设成家庭日程安排并创建`
  - `帮我做一个家庭日程安排智能体`
  - `新建智能体，叫做家庭日程安排`

- English Variants: 10
  - `Create an agent named 家庭日程安排.`
  - `Please create a new agent called 家庭日程安排.`
  - `I want to make an agent named 家庭日程安排.`
  - `Set up an agent with the name 家庭日程安排.`
  - `Can you create the agent 家庭日程安排?`
  - `Please add a new agent named 家庭日程安排.`
  - `Create a custom agent called 家庭日程安排.`
  - `Help me create an agent named 家庭日程安排.`
  - `Make a new agent and name it 家庭日程安排.`
  - `Start creating an agent called 家庭日程安排.`

- Japanese Variants: 10
  - `家庭日程安排 という名前のエージェントを作って`
  - `家庭日程安排 というエージェントを新規作成して`
  - `家庭日程安排 名義でエージェントを作成して`
  - `家庭日程安排 というカスタムエージェントを作って`
  - `家庭日程安排 のエージェントを作りたい`
  - `家庭日程安排 を名前にしてエージェントを作って`
  - `家庭日程安排 という新しいエージェントを追加して`
  - `家庭日程安排 という名称で作成してください`
  - `家庭日程安排 のエージェントを立ち上げて`
  - `家庭日程安排 を名前とするエージェントを設定して`

### S2-23 家庭日程安排 补充需求

- Query: `用于记录家庭日程时间、地点、参与成员和注意事项。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `用于记录家庭日程时间、地点、参与成员和注意事项`
  - `它需要支持这样的能力：用于记录家庭日程时间、地点、参与成员和注意事项`
  - `请把这个能力加进去：用于记录家庭日程时间、地点、参与成员和注意事项`
  - `这个智能体要能做到：用于记录家庭日程时间、地点、参与成员和注意事项`
  - `我希望它具备这个功能：用于记录家庭日程时间、地点、参与成员和注意事项`
  - `请按这个用途来配置：用于记录家庭日程时间、地点、参与成员和注意事项`
  - `它的主要功能应该是：用于记录家庭日程时间、地点、参与成员和注意事项`
  - `请让它支持以下场景：用于记录家庭日程时间、地点、参与成员和注意事项`
  - `这个智能体的目标是：用于记录家庭日程时间、地点、参与成员和注意事项`
  - `能力要求如下：用于记录家庭日程时间、地点、参与成员和注意事项`

- English Variants: 10
  - `It should support this: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `Please make sure it can do the following: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `The agent needs this capability: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `This is the function I want it to have: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `It should be able to handle this: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `Please configure it for this use: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `I need the agent to cover this requirement: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `The intended capability is: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `Make it support the following scenario: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `This should be part of the agent behavior: 用于记录家庭日程时间、地点、参与成员和注意事项`

- Japanese Variants: 10
  - `用于记录家庭日程时间、地点、参与成员和注意事项`
  - `この機能を持たせてください: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `次の用途に対応できるようにして: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `このエージェントには次の役割が必要です: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `以下の機能をサポートしてほしいです: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `この用途で使えるように設定してください: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `次の内容に対応するエージェントにして: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `この能力を含めてください: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `想定している機能はこれです: 用于记录家庭日程时间、地点、参与成员和注意事项`
  - `この要件を満たすようにしてください: 用于记录家庭日程时间、地点、参与成员和注意事项`

### S2-24 家庭日程安排 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `确认创建`
  - `请确认创建`
  - `好的，创建吧`
  - `可以，开始创建`
  - `没问题，确认生成`
  - `继续创建`
  - `就按这个创建`
  - `确认并完成创建`
  - `请直接创建`
  - `可以，执行创建`

- English Variants: 10
  - `Confirm the creation.`
  - `Please go ahead and create it.`
  - `Yes, confirm creation.`
  - `That's good, create it now.`
  - `Proceed with the creation.`
  - `Please confirm and finish creating it.`
  - `Go ahead with creating it.`
  - `I confirm, please create it.`
  - `Create it as discussed.`
  - `Finalize the creation.`

- Japanese Variants: 10
  - `作成を確定して`
  - `この内容で作成して`
  - `はい、作成を進めて`
  - `そのまま作成して`
  - `問題ないので作成して`
  - `作成を確定してください`
  - `この設定で完成させて`
  - `その内容で作って`
  - `では作成を続けて`
  - `確定して作成して`

### S2-25 买菜助理 创建草稿

- Query: `创建智能体，名称为买菜助理。`
- Expected: 进入智能体创建流程。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `创建一个名为买菜助理的智能体`
  - `帮我新建智能体，名字叫买菜助理`
  - `请创建智能体 买菜助理`
  - `我想创建一个叫买菜助理的智能体`
  - `新增智能体，名称设为买菜助理`
  - `请帮我建立名为买菜助理的智能体`
  - `创建新的自定义智能体：买菜助理`
  - `把智能体名称设成买菜助理并创建`
  - `帮我做一个买菜助理智能体`
  - `新建智能体，叫做买菜助理`

- English Variants: 10
  - `Create an agent named 买菜助理.`
  - `Please create a new agent called 买菜助理.`
  - `I want to make an agent named 买菜助理.`
  - `Set up an agent with the name 买菜助理.`
  - `Can you create the agent 买菜助理?`
  - `Please add a new agent named 买菜助理.`
  - `Create a custom agent called 买菜助理.`
  - `Help me create an agent named 买菜助理.`
  - `Make a new agent and name it 买菜助理.`
  - `Start creating an agent called 买菜助理.`

- Japanese Variants: 10
  - `买菜助理 という名前のエージェントを作って`
  - `买菜助理 というエージェントを新規作成して`
  - `买菜助理 名義でエージェントを作成して`
  - `买菜助理 というカスタムエージェントを作って`
  - `买菜助理 のエージェントを作りたい`
  - `买菜助理 を名前にしてエージェントを作って`
  - `买菜助理 という新しいエージェントを追加して`
  - `买菜助理 という名称で作成してください`
  - `买菜助理 のエージェントを立ち上げて`
  - `买菜助理 を名前とするエージェントを設定して`

### S2-26 买菜助理 补充需求

- Query: `用于记录买菜项目、数量和备注，并支持导出excel。`
- Expected: 补充需求并进入确认前状态。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `用于记录买菜项目、数量和备注，并支持导出excel`
  - `它需要支持这样的能力：用于记录买菜项目、数量和备注，并支持导出excel`
  - `请把这个能力加进去：用于记录买菜项目、数量和备注，并支持导出excel`
  - `这个智能体要能做到：用于记录买菜项目、数量和备注，并支持导出excel`
  - `我希望它具备这个功能：用于记录买菜项目、数量和备注，并支持导出excel`
  - `请按这个用途来配置：用于记录买菜项目、数量和备注，并支持导出excel`
  - `它的主要功能应该是：用于记录买菜项目、数量和备注，并支持导出excel`
  - `请让它支持以下场景：用于记录买菜项目、数量和备注，并支持导出excel`
  - `这个智能体的目标是：用于记录买菜项目、数量和备注，并支持导出excel`
  - `能力要求如下：用于记录买菜项目、数量和备注，并支持导出excel`

- English Variants: 10
  - `It should support this: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `Please make sure it can do the following: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `The agent needs this capability: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `This is the function I want it to have: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `It should be able to handle this: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `Please configure it for this use: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `I need the agent to cover this requirement: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `The intended capability is: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `Make it support the following scenario: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `This should be part of the agent behavior: 用于记录买菜项目、数量和备注，并支持导出excel`

- Japanese Variants: 10
  - `用于记录买菜项目、数量和备注，并支持导出excel`
  - `この機能を持たせてください: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `次の用途に対応できるようにして: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `このエージェントには次の役割が必要です: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `以下の機能をサポートしてほしいです: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `この用途で使えるように設定してください: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `次の内容に対応するエージェントにして: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `この能力を含めてください: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `想定している機能はこれです: 用于记录买菜项目、数量和备注，并支持导出excel`
  - `この要件を満たすようにしてください: 用于记录买菜项目、数量和备注，并支持导出excel`

### S2-27 买菜助理 确认创建

- Query: `确认创建。`
- Expected: 完成创建并生成 feature 文件。
- Reset Before: Yes
- Setup Queries: 2

- Chinese Variants: 10
  - `确认创建`
  - `请确认创建`
  - `好的，创建吧`
  - `可以，开始创建`
  - `没问题，确认生成`
  - `继续创建`
  - `就按这个创建`
  - `确认并完成创建`
  - `请直接创建`
  - `可以，执行创建`

- English Variants: 10
  - `Confirm the creation.`
  - `Please go ahead and create it.`
  - `Yes, confirm creation.`
  - `That's good, create it now.`
  - `Proceed with the creation.`
  - `Please confirm and finish creating it.`
  - `Go ahead with creating it.`
  - `I confirm, please create it.`
  - `Create it as discussed.`
  - `Finalize the creation.`

- Japanese Variants: 10
  - `作成を確定して`
  - `この内容で作成して`
  - `はい、作成を進めて`
  - `そのまま作成して`
  - `問題ないので作成して`
  - `作成を確定してください`
  - `この設定で完成させて`
  - `その内容で作って`
  - `では作成を続けて`
  - `確定して作成して`

## 阶段3

### S3-01 账单记录 1

- Query: `记录今日07点30分，早餐消费480日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: Yes
- Setup Queries: 3

- Chinese Variants: 10
  - `记录今天07点30分早餐消费480日元`
  - `帮我登记今日07点30分的早餐支出480日元`
  - `请记录今天07点30分花了480日元买早餐`
  - `把今天07点30分早餐这笔480日元记下来`
  - `新增一条消费记录：今日07点30分，早餐，480日元`
  - `今天07点30分早餐花费480日元，请帮我记录`
  - `请登记07点30分这笔早餐消费，金额480日元`
  - `把今日07点30分的早餐支出480日元录入账单`
  - `记录一下今天07点30分早餐用了480日元`
  - `帮我添加消费：07点30分 早餐 480日元`

- English Variants: 10
  - `Record an expense of 480 yen for 早餐 at 07点30分 today.`
  - `Please log 早餐 costing 480 yen at 07点30分 today.`
  - `Add a spending record for 早餐: 480 yen at 07点30分 today.`
  - `Track 480 yen spent on 早餐 at 07点30分 today.`
  - `Please record today's 07点30分 expense: 早餐, 480 yen.`
  - `Log that I spent 480 yen on 早餐 at 07点30分 today.`
  - `Enter an expense for 早餐 at 07点30分 today, amount 480 yen.`
  - `Add today's 07点30分 purchase of 早餐 for 480 yen.`
  - `Please save a bill entry for 早餐 costing 480 yen at 07点30分.`
  - `Record today's 早餐 expense of 480 yen at 07点30分.`

- Japanese Variants: 10
  - `今日の07点30分に早餐で480円使った記録を追加して`
  - `07点30分の早餐 480円を支出として記録して`
  - `今日07点30分の早餐代480円を登録して`
  - `07点30分に使った早餐 480円を家計に記録して`
  - `今日07点30分の支出として早餐 480円を保存して`
  - `早餐に480円使ったので、今日07点30分の記録に入れて`
  - `今日の07点30分、早餐で480円使ったことを記録して`
  - `07点30分の早餐購入 480円を登録して`
  - `今日07点30分の早餐支出480円を追加して`
  - `家計記録に07点30分の早餐 480円を入れて`

### S3-02 账单记录 2

- Query: `记录今日08点20分，地铁消费220日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天08点20分地铁消费220日元`
  - `帮我登记今日08点20分的地铁支出220日元`
  - `请记录今天08点20分花了220日元买地铁`
  - `把今天08点20分地铁这笔220日元记下来`
  - `新增一条消费记录：今日08点20分，地铁，220日元`
  - `今天08点20分地铁花费220日元，请帮我记录`
  - `请登记08点20分这笔地铁消费，金额220日元`
  - `把今日08点20分的地铁支出220日元录入账单`
  - `记录一下今天08点20分地铁用了220日元`
  - `帮我添加消费：08点20分 地铁 220日元`

- English Variants: 10
  - `Record an expense of 220 yen for 地铁 at 08点20分 today.`
  - `Please log 地铁 costing 220 yen at 08点20分 today.`
  - `Add a spending record for 地铁: 220 yen at 08点20分 today.`
  - `Track 220 yen spent on 地铁 at 08点20分 today.`
  - `Please record today's 08点20分 expense: 地铁, 220 yen.`
  - `Log that I spent 220 yen on 地铁 at 08点20分 today.`
  - `Enter an expense for 地铁 at 08点20分 today, amount 220 yen.`
  - `Add today's 08点20分 purchase of 地铁 for 220 yen.`
  - `Please save a bill entry for 地铁 costing 220 yen at 08点20分.`
  - `Record today's 地铁 expense of 220 yen at 08点20分.`

- Japanese Variants: 10
  - `今日の08点20分に地铁で220円使った記録を追加して`
  - `08点20分の地铁 220円を支出として記録して`
  - `今日08点20分の地铁代220円を登録して`
  - `08点20分に使った地铁 220円を家計に記録して`
  - `今日08点20分の支出として地铁 220円を保存して`
  - `地铁に220円使ったので、今日08点20分の記録に入れて`
  - `今日の08点20分、地铁で220円使ったことを記録して`
  - `08点20分の地铁購入 220円を登録して`
  - `今日08点20分の地铁支出220円を追加して`
  - `家計記録に08点20分の地铁 220円を入れて`

### S3-03 账单记录 3

- Query: `记录今日10点20分，食材消费2000日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天10点20分食材消费2000日元`
  - `帮我登记今日10点20分的食材支出2000日元`
  - `请记录今天10点20分花了2000日元买食材`
  - `把今天10点20分食材这笔2000日元记下来`
  - `新增一条消费记录：今日10点20分，食材，2000日元`
  - `今天10点20分食材花费2000日元，请帮我记录`
  - `请登记10点20分这笔食材消费，金额2000日元`
  - `把今日10点20分的食材支出2000日元录入账单`
  - `记录一下今天10点20分食材用了2000日元`
  - `帮我添加消费：10点20分 食材 2000日元`

- English Variants: 10
  - `Record an expense of 2000 yen for 食材 at 10点20分 today.`
  - `Please log 食材 costing 2000 yen at 10点20分 today.`
  - `Add a spending record for 食材: 2000 yen at 10点20分 today.`
  - `Track 2000 yen spent on 食材 at 10点20分 today.`
  - `Please record today's 10点20分 expense: 食材, 2000 yen.`
  - `Log that I spent 2000 yen on 食材 at 10点20分 today.`
  - `Enter an expense for 食材 at 10点20分 today, amount 2000 yen.`
  - `Add today's 10点20分 purchase of 食材 for 2000 yen.`
  - `Please save a bill entry for 食材 costing 2000 yen at 10点20分.`
  - `Record today's 食材 expense of 2000 yen at 10点20分.`

- Japanese Variants: 10
  - `今日の10点20分に食材で2000円使った記録を追加して`
  - `10点20分の食材 2000円を支出として記録して`
  - `今日10点20分の食材代2000円を登録して`
  - `10点20分に使った食材 2000円を家計に記録して`
  - `今日10点20分の支出として食材 2000円を保存して`
  - `食材に2000円使ったので、今日10点20分の記録に入れて`
  - `今日の10点20分、食材で2000円使ったことを記録して`
  - `10点20分の食材購入 2000円を登録して`
  - `今日10点20分の食材支出2000円を追加して`
  - `家計記録に10点20分の食材 2000円を入れて`

### S3-04 账单记录 4

- Query: `记录今日12点00分，午餐消费800日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天12点00分午餐消费800日元`
  - `帮我登记今日12点00分的午餐支出800日元`
  - `请记录今天12点00分花了800日元买午餐`
  - `把今天12点00分午餐这笔800日元记下来`
  - `新增一条消费记录：今日12点00分，午餐，800日元`
  - `今天12点00分午餐花费800日元，请帮我记录`
  - `请登记12点00分这笔午餐消费，金额800日元`
  - `把今日12点00分的午餐支出800日元录入账单`
  - `记录一下今天12点00分午餐用了800日元`
  - `帮我添加消费：12点00分 午餐 800日元`

- English Variants: 10
  - `Record an expense of 800 yen for 午餐 at 12点00分 today.`
  - `Please log 午餐 costing 800 yen at 12点00分 today.`
  - `Add a spending record for 午餐: 800 yen at 12点00分 today.`
  - `Track 800 yen spent on 午餐 at 12点00分 today.`
  - `Please record today's 12点00分 expense: 午餐, 800 yen.`
  - `Log that I spent 800 yen on 午餐 at 12点00分 today.`
  - `Enter an expense for 午餐 at 12点00分 today, amount 800 yen.`
  - `Add today's 12点00分 purchase of 午餐 for 800 yen.`
  - `Please save a bill entry for 午餐 costing 800 yen at 12点00分.`
  - `Record today's 午餐 expense of 800 yen at 12点00分.`

- Japanese Variants: 10
  - `今日の12点00分に午餐で800円使った記録を追加して`
  - `12点00分の午餐 800円を支出として記録して`
  - `今日12点00分の午餐代800円を登録して`
  - `12点00分に使った午餐 800円を家計に記録して`
  - `今日12点00分の支出として午餐 800円を保存して`
  - `午餐に800円使ったので、今日12点00分の記録に入れて`
  - `今日の12点00分、午餐で800円使ったことを記録して`
  - `12点00分の午餐購入 800円を登録して`
  - `今日12点00分の午餐支出800円を追加して`
  - `家計記録に12点00分の午餐 800円を入れて`

### S3-05 账单记录 5

- Query: `记录今日14点10分，水果消费650日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天14点10分水果消费650日元`
  - `帮我登记今日14点10分的水果支出650日元`
  - `请记录今天14点10分花了650日元买水果`
  - `把今天14点10分水果这笔650日元记下来`
  - `新增一条消费记录：今日14点10分，水果，650日元`
  - `今天14点10分水果花费650日元，请帮我记录`
  - `请登记14点10分这笔水果消费，金额650日元`
  - `把今日14点10分的水果支出650日元录入账单`
  - `记录一下今天14点10分水果用了650日元`
  - `帮我添加消费：14点10分 水果 650日元`

- English Variants: 10
  - `Record an expense of 650 yen for 水果 at 14点10分 today.`
  - `Please log 水果 costing 650 yen at 14点10分 today.`
  - `Add a spending record for 水果: 650 yen at 14点10分 today.`
  - `Track 650 yen spent on 水果 at 14点10分 today.`
  - `Please record today's 14点10分 expense: 水果, 650 yen.`
  - `Log that I spent 650 yen on 水果 at 14点10分 today.`
  - `Enter an expense for 水果 at 14点10分 today, amount 650 yen.`
  - `Add today's 14点10分 purchase of 水果 for 650 yen.`
  - `Please save a bill entry for 水果 costing 650 yen at 14点10分.`
  - `Record today's 水果 expense of 650 yen at 14点10分.`

- Japanese Variants: 10
  - `今日の14点10分に水果で650円使った記録を追加して`
  - `14点10分の水果 650円を支出として記録して`
  - `今日14点10分の水果代650円を登録して`
  - `14点10分に使った水果 650円を家計に記録して`
  - `今日14点10分の支出として水果 650円を保存して`
  - `水果に650円使ったので、今日14点10分の記録に入れて`
  - `今日の14点10分、水果で650円使ったことを記録して`
  - `14点10分の水果購入 650円を登録して`
  - `今日14点10分の水果支出650円を追加して`
  - `家計記録に14点10分の水果 650円を入れて`

### S3-06 账单列表 5

- Query: `查看家庭账单有哪些记录`
- Expected: 返回当前账单记录列表。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `查看家庭账单里的记录`
  - `帮我列出家庭账单有哪些记录`
  - `家庭账单目前都记录了什么`
  - `请显示家庭账单的全部记录`
  - `我想看一下家庭账单里的内容`
  - `把家庭账单的记录给我看看`
  - `查看一下家庭账单都有哪些条目`
  - `帮我打开家庭账单记录`
  - `列出家庭账单目前的记录`
  - `请展示家庭账单中的所有记录`

- English Variants: 10
  - `Show me the records in 家庭账单.`
  - `What records are in 家庭账单?`
  - `Please list the entries under 家庭账单.`
  - `Can you display all records in 家庭账单?`
  - `I want to check the records for 家庭账单.`
  - `Let me see what has been recorded in 家庭账单.`
  - `Please open 家庭账单 and show the entries.`
  - `List everything recorded in 家庭账单.`
  - `Could you pull up the records from 家庭账单?`
  - `Show all entries stored in 家庭账单.`

- Japanese Variants: 10
  - `家庭账单 の記録を見せて`
  - `家庭账单 にある記録一覧を表示して`
  - `家庭账单 の登録内容を確認したい`
  - `家庭账单 の記録を全部見たい`
  - `家庭账单 に入っている情報を見せて`
  - `家庭账单 の内容を一覧表示して`
  - `家庭账单 の記録を教えて`
  - `家庭账单 のエントリーを確認して`
  - `家庭账单 の登録データを開いて`
  - `家庭账单 に何が記録されているか見せて`

### S3-07 账单导出 5

- Query: `导出家庭账单`
- Expected: 导出当前账单记录为 Excel。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `导出家庭账单`
  - `把家庭账单导出来`
  - `请帮我导出家庭账单`
  - `生成家庭账单的导出文件`
  - `我想导出家庭账单的数据`
  - `请把家庭账单内容输出成文件`
  - `帮我准备家庭账单的导出结果`
  - `导出一下家庭账单相关内容`
  - `请生成家庭账单的可导出文件`
  - `把家庭账单做成导出文档`

- English Variants: 10
  - `Export 家庭账单.`
  - `Please export 家庭账单.`
  - `I need an export of 家庭账单.`
  - `Can you export the data export for 家庭账单?`
  - `Generate an export for 家庭账单.`
  - `Please create an export file for 家庭账单.`
  - `Export the data from 家庭账单.`
  - `Could you prepare an export for 家庭账单?`
  - `I want to download the exported data export for 家庭账单.`
  - `Please output 家庭账单 as an export file.`

- Japanese Variants: 10
  - `家庭账单 をエクスポートして`
  - `家庭账单 のデータを出力して`
  - `家庭账单 を書き出してください`
  - `家庭账单 の内容をエクスポートしたい`
  - `家庭账单 のエクスポートファイルを作って`
  - `家庭账单 を外部出力して`
  - `家庭账单 の記録をファイルで出して`
  - `家庭账单 のデータを出力形式にして`
  - `家庭账单 をダウンロードできる形で出して`
  - `家庭账单 のエクスポートを準備して`

### S3-08 账单汇总阈值 5

- Query: `到今天为止消费总额是多少，如果超过3000日元产生提醒，并把提醒发送到 homehub`
- Expected: 返回累计总额，并根据阈值给出提示。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `到今天为止消费总额是多少，如果超过3000日元产生提醒我，并把提醒发送到 homehub`
  - `帮我设置一个提醒，到今天为止消费总额是多少，如果超过3000日元产生，并把提醒发送到 homehub`
  - `请在到今天为止消费总额是多少，如果超过3000日元产生提醒我去，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超过3000日元产生记得提醒我，并把提醒发送到 homehub`
  - `我想在到今天为止消费总额是多少，如果超过3000日元产生收到提醒：，并把提醒发送到 homehub`
  - `请给我设一个到今天为止消费总额是多少，如果超过3000日元产生的提醒，内容是，并把提醒发送到 homehub`
  - `到今天为止消费总额是多少，如果超过3000日元产生帮我提醒一下，并把提醒发送到 homehub`
  - `记得在到今天为止消费总额是多少，如果超过3000日元产生提醒我，并把提醒发送到 homehub`
  - `请添加提醒：到今天为止消费总额是多少，如果超过3000日元产生，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超过3000日元产生通知我，并把提醒发送到 homehub`

- English Variants: 10
  - `Remind me 到今天为止消费总额是多少，如果超过3000日元产生 to ，并把提醒发送到 homehub.`
  - `Set a reminder 到今天为止消费总额是多少，如果超过3000日元产生 for me to ，并把提醒发送到 homehub.`
  - `Please remind me 到今天为止消费总额是多少，如果超过3000日元产生 that I need to ，并把提醒发送到 homehub.`
  - `Can you create a reminder 到今天为止消费总额是多少，如果超过3000日元产生 for ，并把提醒发送到 homehub?`
  - `I need a reminder 到今天为止消费总额是多少，如果超过3000日元产生 to ，并把提醒发送到 homehub.`
  - `Put in a reminder for 到今天为止消费总额是多少，如果超过3000日元产生: ，并把提醒发送到 homehub.`
  - `Schedule a reminder 到今天为止消费总额是多少，如果超过3000日元产生 so I remember to ，并把提醒发送到 homehub.`
  - `Please alert me 到今天为止消费总额是多少，如果超过3000日元产生 to ，并把提醒发送到 homehub.`
  - `Set me a 到今天为止消费总额是多少，如果超过3000日元产生 reminder to ，并把提醒发送到 homehub.`
  - `Create a reminder telling me 到今天为止消费总额是多少，如果超过3000日元产生 to ，并把提醒发送到 homehub.`

- Japanese Variants: 10
  - `到今天为止消费总额是多少，如果超过3000日元产生に，并把提醒发送到 homehubとリマインドして`
  - `到今天为止消费总额是多少，如果超过3000日元产生に，并把提醒发送到 homehubことを知らせて`
  - `到今天为止消费总额是多少，如果超过3000日元产生用に「，并把提醒发送到 homehub」のリマインダーを設定して`
  - `到今天为止消费总额是多少，如果超过3000日元产生になったら，并把提醒发送到 homehubと通知して`
  - `到今天为止消费总额是多少，如果超过3000日元产生のリマインダーとして，并把提醒发送到 homehubを登録して`
  - `到今天为止消费总额是多少，如果超过3000日元产生に，并把提醒发送到 homehubの通知を入れて`
  - `到今天为止消费总额是多少，如果超过3000日元产生に，并把提醒发送到 homehubことを忘れないよう知らせて`
  - `到今天为止消费总额是多少，如果超过3000日元产生の時刻で，并把提醒发送到 homehubをリマインドして`
  - `到今天为止消费总额是多少，如果超过3000日元产生に私へ，并把提醒发送到 homehubと伝えて`
  - `到今天为止消费总额是多少，如果超过3000日元产生用に，并把提醒发送到 homehubの通知を作って`

### S3-09 账单汇总导出 5

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回累计总额并导出 Excel。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `统计到今天为止的消费总额，并把消费信息生成 Excel 文档`
  - `帮我算一下当前消费总额，再导出 Excel 明细`
  - `请汇总截至今天的消费，并生成一份 Excel 文件`
  - `到今天为止一共花了多少？顺便把消费信息做成 Excel`
  - `我想看累计消费总额，并导出消费 Excel 文档`
  - `请统计总支出，同时生成消费明细的 Excel`
  - `帮我把消费总额算出来，并把记录导出成 Excel`
  - `请生成截至今天的消费汇总和 Excel 文档`
  - `看一下当前总消费，再输出一份 Excel 表格`
  - `把到今天的消费合计出来，并生成 Excel 文件`

- English Variants: 10
  - `What's the total spending up to today, and generate an Excel file with the expense details.`
  - `Please calculate total spending through today and create an Excel document of the expenses.`
  - `Show me the total spent so far today, and export the spending data to Excel.`
  - `Tell me the total expenses up to today and make an Excel file with the details.`
  - `I want today's cumulative spending and an Excel export of the expense information.`
  - `Please total the spending so far and generate an Excel sheet of all expense records.`
  - `How much have we spent up to today? Also create an Excel file of the spending details.`
  - `Calculate the total spending through today and output the expense data as Excel.`
  - `Give me the spending total so far and build an Excel document from the expense info.`
  - `Please provide today's total expense amount and export the expense details into Excel.`

- Japanese Variants: 10
  - `今日までの支出総額を出して、支出情報を Excel にまとめて`
  - `ここまでの支出合計を計算して、Excel 文書を作って`
  - `今日時点の消費総額を確認し、Excel ファイルも生成して`
  - `支出合計を出して、明細を Excel にしてほしい`
  - `累計支出とその内容を Excel で出力して`
  - `今日までの出費を集計して、Excel 形式でまとめて`
  - `支出の合計を教えて、その情報を Excel にして`
  - `現在までの消費額を計算し、Excel ファイルを作成して`
  - `ここまでの支出情報を Excel 文書として出して`
  - `支出合計の確認と、Excel への書き出しをお願い`

### S3-10 账单记录 6

- Query: `记录今日15点30分，纸巾消费320日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天15点30分纸巾消费320日元`
  - `帮我登记今日15点30分的纸巾支出320日元`
  - `请记录今天15点30分花了320日元买纸巾`
  - `把今天15点30分纸巾这笔320日元记下来`
  - `新增一条消费记录：今日15点30分，纸巾，320日元`
  - `今天15点30分纸巾花费320日元，请帮我记录`
  - `请登记15点30分这笔纸巾消费，金额320日元`
  - `把今日15点30分的纸巾支出320日元录入账单`
  - `记录一下今天15点30分纸巾用了320日元`
  - `帮我添加消费：15点30分 纸巾 320日元`

- English Variants: 10
  - `Record an expense of 320 yen for 纸巾 at 15点30分 today.`
  - `Please log 纸巾 costing 320 yen at 15点30分 today.`
  - `Add a spending record for 纸巾: 320 yen at 15点30分 today.`
  - `Track 320 yen spent on 纸巾 at 15点30分 today.`
  - `Please record today's 15点30分 expense: 纸巾, 320 yen.`
  - `Log that I spent 320 yen on 纸巾 at 15点30分 today.`
  - `Enter an expense for 纸巾 at 15点30分 today, amount 320 yen.`
  - `Add today's 15点30分 purchase of 纸巾 for 320 yen.`
  - `Please save a bill entry for 纸巾 costing 320 yen at 15点30分.`
  - `Record today's 纸巾 expense of 320 yen at 15点30分.`

- Japanese Variants: 10
  - `今日の15点30分に纸巾で320円使った記録を追加して`
  - `15点30分の纸巾 320円を支出として記録して`
  - `今日15点30分の纸巾代320円を登録して`
  - `15点30分に使った纸巾 320円を家計に記録して`
  - `今日15点30分の支出として纸巾 320円を保存して`
  - `纸巾に320円使ったので、今日15点30分の記録に入れて`
  - `今日の15点30分、纸巾で320円使ったことを記録して`
  - `15点30分の纸巾購入 320円を登録して`
  - `今日15点30分の纸巾支出320円を追加して`
  - `家計記録に15点30分の纸巾 320円を入れて`

### S3-11 账单记录 7

- Query: `记录今日17点00分，应酬消费5800日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天17点00分应酬消费5800日元`
  - `帮我登记今日17点00分的应酬支出5800日元`
  - `请记录今天17点00分花了5800日元买应酬`
  - `把今天17点00分应酬这笔5800日元记下来`
  - `新增一条消费记录：今日17点00分，应酬，5800日元`
  - `今天17点00分应酬花费5800日元，请帮我记录`
  - `请登记17点00分这笔应酬消费，金额5800日元`
  - `把今日17点00分的应酬支出5800日元录入账单`
  - `记录一下今天17点00分应酬用了5800日元`
  - `帮我添加消费：17点00分 应酬 5800日元`

- English Variants: 10
  - `Record an expense of 5800 yen for 应酬 at 17点00分 today.`
  - `Please log 应酬 costing 5800 yen at 17点00分 today.`
  - `Add a spending record for 应酬: 5800 yen at 17点00分 today.`
  - `Track 5800 yen spent on 应酬 at 17点00分 today.`
  - `Please record today's 17点00分 expense: 应酬, 5800 yen.`
  - `Log that I spent 5800 yen on 应酬 at 17点00分 today.`
  - `Enter an expense for 应酬 at 17点00分 today, amount 5800 yen.`
  - `Add today's 17点00分 purchase of 应酬 for 5800 yen.`
  - `Please save a bill entry for 应酬 costing 5800 yen at 17点00分.`
  - `Record today's 应酬 expense of 5800 yen at 17点00分.`

- Japanese Variants: 10
  - `今日の17点00分に应酬で5800円使った記録を追加して`
  - `17点00分の应酬 5800円を支出として記録して`
  - `今日17点00分の应酬代5800円を登録して`
  - `17点00分に使った应酬 5800円を家計に記録して`
  - `今日17点00分の支出として应酬 5800円を保存して`
  - `应酬に5800円使ったので、今日17点00分の記録に入れて`
  - `今日の17点00分、应酬で5800円使ったことを記録して`
  - `17点00分の应酬購入 5800円を登録して`
  - `今日17点00分の应酬支出5800円を追加して`
  - `家計記録に17点00分の应酬 5800円を入れて`

### S3-12 账单记录 8

- Query: `记录今日18点15分，牛奶消费260日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天18点15分牛奶消费260日元`
  - `帮我登记今日18点15分的牛奶支出260日元`
  - `请记录今天18点15分花了260日元买牛奶`
  - `把今天18点15分牛奶这笔260日元记下来`
  - `新增一条消费记录：今日18点15分，牛奶，260日元`
  - `今天18点15分牛奶花费260日元，请帮我记录`
  - `请登记18点15分这笔牛奶消费，金额260日元`
  - `把今日18点15分的牛奶支出260日元录入账单`
  - `记录一下今天18点15分牛奶用了260日元`
  - `帮我添加消费：18点15分 牛奶 260日元`

- English Variants: 10
  - `Record an expense of 260 yen for 牛奶 at 18点15分 today.`
  - `Please log 牛奶 costing 260 yen at 18点15分 today.`
  - `Add a spending record for 牛奶: 260 yen at 18点15分 today.`
  - `Track 260 yen spent on 牛奶 at 18点15分 today.`
  - `Please record today's 18点15分 expense: 牛奶, 260 yen.`
  - `Log that I spent 260 yen on 牛奶 at 18点15分 today.`
  - `Enter an expense for 牛奶 at 18点15分 today, amount 260 yen.`
  - `Add today's 18点15分 purchase of 牛奶 for 260 yen.`
  - `Please save a bill entry for 牛奶 costing 260 yen at 18点15分.`
  - `Record today's 牛奶 expense of 260 yen at 18点15分.`

- Japanese Variants: 10
  - `今日の18点15分に牛奶で260円使った記録を追加して`
  - `18点15分の牛奶 260円を支出として記録して`
  - `今日18点15分の牛奶代260円を登録して`
  - `18点15分に使った牛奶 260円を家計に記録して`
  - `今日18点15分の支出として牛奶 260円を保存して`
  - `牛奶に260円使ったので、今日18点15分の記録に入れて`
  - `今日の18点15分、牛奶で260円使ったことを記録して`
  - `18点15分の牛奶購入 260円を登録して`
  - `今日18点15分の牛奶支出260円を追加して`
  - `家計記録に18点15分の牛奶 260円を入れて`

### S3-13 账单记录 9

- Query: `记录今日19点40分，晚餐消费1500日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天19点40分晚餐消费1500日元`
  - `帮我登记今日19点40分的晚餐支出1500日元`
  - `请记录今天19点40分花了1500日元买晚餐`
  - `把今天19点40分晚餐这笔1500日元记下来`
  - `新增一条消费记录：今日19点40分，晚餐，1500日元`
  - `今天19点40分晚餐花费1500日元，请帮我记录`
  - `请登记19点40分这笔晚餐消费，金额1500日元`
  - `把今日19点40分的晚餐支出1500日元录入账单`
  - `记录一下今天19点40分晚餐用了1500日元`
  - `帮我添加消费：19点40分 晚餐 1500日元`

- English Variants: 10
  - `Record an expense of 1500 yen for 晚餐 at 19点40分 today.`
  - `Please log 晚餐 costing 1500 yen at 19点40分 today.`
  - `Add a spending record for 晚餐: 1500 yen at 19点40分 today.`
  - `Track 1500 yen spent on 晚餐 at 19点40分 today.`
  - `Please record today's 19点40分 expense: 晚餐, 1500 yen.`
  - `Log that I spent 1500 yen on 晚餐 at 19点40分 today.`
  - `Enter an expense for 晚餐 at 19点40分 today, amount 1500 yen.`
  - `Add today's 19点40分 purchase of 晚餐 for 1500 yen.`
  - `Please save a bill entry for 晚餐 costing 1500 yen at 19点40分.`
  - `Record today's 晚餐 expense of 1500 yen at 19点40分.`

- Japanese Variants: 10
  - `今日の19点40分に晚餐で1500円使った記録を追加して`
  - `19点40分の晚餐 1500円を支出として記録して`
  - `今日19点40分の晚餐代1500円を登録して`
  - `19点40分に使った晚餐 1500円を家計に記録して`
  - `今日19点40分の支出として晚餐 1500円を保存して`
  - `晚餐に1500円使ったので、今日19点40分の記録に入れて`
  - `今日の19点40分、晚餐で1500円使ったことを記録して`
  - `19点40分の晚餐購入 1500円を登録して`
  - `今日19点40分の晚餐支出1500円を追加して`
  - `家計記録に19点40分の晚餐 1500円を入れて`

### S3-14 账单记录 10

- Query: `记录今日20点10分，停车消费700日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天20点10分停车消费700日元`
  - `帮我登记今日20点10分的停车支出700日元`
  - `请记录今天20点10分花了700日元买停车`
  - `把今天20点10分停车这笔700日元记下来`
  - `新增一条消费记录：今日20点10分，停车，700日元`
  - `今天20点10分停车花费700日元，请帮我记录`
  - `请登记20点10分这笔停车消费，金额700日元`
  - `把今日20点10分的停车支出700日元录入账单`
  - `记录一下今天20点10分停车用了700日元`
  - `帮我添加消费：20点10分 停车 700日元`

- English Variants: 10
  - `Record an expense of 700 yen for 停车 at 20点10分 today.`
  - `Please log 停车 costing 700 yen at 20点10分 today.`
  - `Add a spending record for 停车: 700 yen at 20点10分 today.`
  - `Track 700 yen spent on 停车 at 20点10分 today.`
  - `Please record today's 20点10分 expense: 停车, 700 yen.`
  - `Log that I spent 700 yen on 停车 at 20点10分 today.`
  - `Enter an expense for 停车 at 20点10分 today, amount 700 yen.`
  - `Add today's 20点10分 purchase of 停车 for 700 yen.`
  - `Please save a bill entry for 停车 costing 700 yen at 20点10分.`
  - `Record today's 停车 expense of 700 yen at 20点10分.`

- Japanese Variants: 10
  - `今日の20点10分に停车で700円使った記録を追加して`
  - `20点10分の停车 700円を支出として記録して`
  - `今日20点10分の停车代700円を登録して`
  - `20点10分に使った停车 700円を家計に記録して`
  - `今日20点10分の支出として停车 700円を保存して`
  - `停车に700円使ったので、今日20点10分の記録に入れて`
  - `今日の20点10分、停车で700円使ったことを記録して`
  - `20点10分の停车購入 700円を登録して`
  - `今日20点10分の停车支出700円を追加して`
  - `家計記録に20点10分の停车 700円を入れて`

### S3-15 账单列表 10

- Query: `查看家庭账单有哪些记录`
- Expected: 返回当前账单记录列表。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `查看家庭账单里的记录`
  - `帮我列出家庭账单有哪些记录`
  - `家庭账单目前都记录了什么`
  - `请显示家庭账单的全部记录`
  - `我想看一下家庭账单里的内容`
  - `把家庭账单的记录给我看看`
  - `查看一下家庭账单都有哪些条目`
  - `帮我打开家庭账单记录`
  - `列出家庭账单目前的记录`
  - `请展示家庭账单中的所有记录`

- English Variants: 10
  - `Show me the records in 家庭账单.`
  - `What records are in 家庭账单?`
  - `Please list the entries under 家庭账单.`
  - `Can you display all records in 家庭账单?`
  - `I want to check the records for 家庭账单.`
  - `Let me see what has been recorded in 家庭账单.`
  - `Please open 家庭账单 and show the entries.`
  - `List everything recorded in 家庭账单.`
  - `Could you pull up the records from 家庭账单?`
  - `Show all entries stored in 家庭账单.`

- Japanese Variants: 10
  - `家庭账单 の記録を見せて`
  - `家庭账单 にある記録一覧を表示して`
  - `家庭账单 の登録内容を確認したい`
  - `家庭账单 の記録を全部見たい`
  - `家庭账单 に入っている情報を見せて`
  - `家庭账单 の内容を一覧表示して`
  - `家庭账单 の記録を教えて`
  - `家庭账单 のエントリーを確認して`
  - `家庭账单 の登録データを開いて`
  - `家庭账单 に何が記録されているか見せて`

### S3-16 账单导出 10

- Query: `导出家庭账单`
- Expected: 导出当前账单记录为 Excel。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `导出家庭账单`
  - `把家庭账单导出来`
  - `请帮我导出家庭账单`
  - `生成家庭账单的导出文件`
  - `我想导出家庭账单的数据`
  - `请把家庭账单内容输出成文件`
  - `帮我准备家庭账单的导出结果`
  - `导出一下家庭账单相关内容`
  - `请生成家庭账单的可导出文件`
  - `把家庭账单做成导出文档`

- English Variants: 10
  - `Export 家庭账单.`
  - `Please export 家庭账单.`
  - `I need an export of 家庭账单.`
  - `Can you export the data export for 家庭账单?`
  - `Generate an export for 家庭账单.`
  - `Please create an export file for 家庭账单.`
  - `Export the data from 家庭账单.`
  - `Could you prepare an export for 家庭账单?`
  - `I want to download the exported data export for 家庭账单.`
  - `Please output 家庭账单 as an export file.`

- Japanese Variants: 10
  - `家庭账单 をエクスポートして`
  - `家庭账单 のデータを出力して`
  - `家庭账单 を書き出してください`
  - `家庭账单 の内容をエクスポートしたい`
  - `家庭账单 のエクスポートファイルを作って`
  - `家庭账单 を外部出力して`
  - `家庭账单 の記録をファイルで出して`
  - `家庭账单 のデータを出力形式にして`
  - `家庭账单 をダウンロードできる形で出して`
  - `家庭账单 のエクスポートを準備して`

### S3-17 账单汇总阈值 10

- Query: `到今天为止消费总额是多少，如果超过10000日元产生提醒，并把提醒发送到 homehub`
- Expected: 返回累计总额，并根据阈值给出提示。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `到今天为止消费总额是多少，如果超过10000日元产生提醒我，并把提醒发送到 homehub`
  - `帮我设置一个提醒，到今天为止消费总额是多少，如果超过10000日元产生，并把提醒发送到 homehub`
  - `请在到今天为止消费总额是多少，如果超过10000日元产生提醒我去，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超过10000日元产生记得提醒我，并把提醒发送到 homehub`
  - `我想在到今天为止消费总额是多少，如果超过10000日元产生收到提醒：，并把提醒发送到 homehub`
  - `请给我设一个到今天为止消费总额是多少，如果超过10000日元产生的提醒，内容是，并把提醒发送到 homehub`
  - `到今天为止消费总额是多少，如果超过10000日元产生帮我提醒一下，并把提醒发送到 homehub`
  - `记得在到今天为止消费总额是多少，如果超过10000日元产生提醒我，并把提醒发送到 homehub`
  - `请添加提醒：到今天为止消费总额是多少，如果超过10000日元产生，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超过10000日元产生通知我，并把提醒发送到 homehub`

- English Variants: 10
  - `Remind me 到今天为止消费总额是多少，如果超过10000日元产生 to ，并把提醒发送到 homehub.`
  - `Set a reminder 到今天为止消费总额是多少，如果超过10000日元产生 for me to ，并把提醒发送到 homehub.`
  - `Please remind me 到今天为止消费总额是多少，如果超过10000日元产生 that I need to ，并把提醒发送到 homehub.`
  - `Can you create a reminder 到今天为止消费总额是多少，如果超过10000日元产生 for ，并把提醒发送到 homehub?`
  - `I need a reminder 到今天为止消费总额是多少，如果超过10000日元产生 to ，并把提醒发送到 homehub.`
  - `Put in a reminder for 到今天为止消费总额是多少，如果超过10000日元产生: ，并把提醒发送到 homehub.`
  - `Schedule a reminder 到今天为止消费总额是多少，如果超过10000日元产生 so I remember to ，并把提醒发送到 homehub.`
  - `Please alert me 到今天为止消费总额是多少，如果超过10000日元产生 to ，并把提醒发送到 homehub.`
  - `Set me a 到今天为止消费总额是多少，如果超过10000日元产生 reminder to ，并把提醒发送到 homehub.`
  - `Create a reminder telling me 到今天为止消费总额是多少，如果超过10000日元产生 to ，并把提醒发送到 homehub.`

- Japanese Variants: 10
  - `到今天为止消费总额是多少，如果超过10000日元产生に，并把提醒发送到 homehubとリマインドして`
  - `到今天为止消费总额是多少，如果超过10000日元产生に，并把提醒发送到 homehubことを知らせて`
  - `到今天为止消费总额是多少，如果超过10000日元产生用に「，并把提醒发送到 homehub」のリマインダーを設定して`
  - `到今天为止消费总额是多少，如果超过10000日元产生になったら，并把提醒发送到 homehubと通知して`
  - `到今天为止消费总额是多少，如果超过10000日元产生のリマインダーとして，并把提醒发送到 homehubを登録して`
  - `到今天为止消费总额是多少，如果超过10000日元产生に，并把提醒发送到 homehubの通知を入れて`
  - `到今天为止消费总额是多少，如果超过10000日元产生に，并把提醒发送到 homehubことを忘れないよう知らせて`
  - `到今天为止消费总额是多少，如果超过10000日元产生の時刻で，并把提醒发送到 homehubをリマインドして`
  - `到今天为止消费总额是多少，如果超过10000日元产生に私へ，并把提醒发送到 homehubと伝えて`
  - `到今天为止消费总额是多少，如果超过10000日元产生用に，并把提醒发送到 homehubの通知を作って`

### S3-18 账单汇总导出 10

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回累计总额并导出 Excel。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `统计到今天为止的消费总额，并把消费信息生成 Excel 文档`
  - `帮我算一下当前消费总额，再导出 Excel 明细`
  - `请汇总截至今天的消费，并生成一份 Excel 文件`
  - `到今天为止一共花了多少？顺便把消费信息做成 Excel`
  - `我想看累计消费总额，并导出消费 Excel 文档`
  - `请统计总支出，同时生成消费明细的 Excel`
  - `帮我把消费总额算出来，并把记录导出成 Excel`
  - `请生成截至今天的消费汇总和 Excel 文档`
  - `看一下当前总消费，再输出一份 Excel 表格`
  - `把到今天的消费合计出来，并生成 Excel 文件`

- English Variants: 10
  - `What's the total spending up to today, and generate an Excel file with the expense details.`
  - `Please calculate total spending through today and create an Excel document of the expenses.`
  - `Show me the total spent so far today, and export the spending data to Excel.`
  - `Tell me the total expenses up to today and make an Excel file with the details.`
  - `I want today's cumulative spending and an Excel export of the expense information.`
  - `Please total the spending so far and generate an Excel sheet of all expense records.`
  - `How much have we spent up to today? Also create an Excel file of the spending details.`
  - `Calculate the total spending through today and output the expense data as Excel.`
  - `Give me the spending total so far and build an Excel document from the expense info.`
  - `Please provide today's total expense amount and export the expense details into Excel.`

- Japanese Variants: 10
  - `今日までの支出総額を出して、支出情報を Excel にまとめて`
  - `ここまでの支出合計を計算して、Excel 文書を作って`
  - `今日時点の消費総額を確認し、Excel ファイルも生成して`
  - `支出合計を出して、明細を Excel にしてほしい`
  - `累計支出とその内容を Excel で出力して`
  - `今日までの出費を集計して、Excel 形式でまとめて`
  - `支出の合計を教えて、その情報を Excel にして`
  - `現在までの消費額を計算し、Excel ファイルを作成して`
  - `ここまでの支出情報を Excel 文書として出して`
  - `支出合計の確認と、Excel への書き出しをお願い`

### S3-19 账单记录 11

- Query: `记录今日21点00分，药品消费980日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天21点00分药品消费980日元`
  - `帮我登记今日21点00分的药品支出980日元`
  - `请记录今天21点00分花了980日元买药品`
  - `把今天21点00分药品这笔980日元记下来`
  - `新增一条消费记录：今日21点00分，药品，980日元`
  - `今天21点00分药品花费980日元，请帮我记录`
  - `请登记21点00分这笔药品消费，金额980日元`
  - `把今日21点00分的药品支出980日元录入账单`
  - `记录一下今天21点00分药品用了980日元`
  - `帮我添加消费：21点00分 药品 980日元`

- English Variants: 10
  - `Record an expense of 980 yen for 药品 at 21点00分 today.`
  - `Please log 药品 costing 980 yen at 21点00分 today.`
  - `Add a spending record for 药品: 980 yen at 21点00分 today.`
  - `Track 980 yen spent on 药品 at 21点00分 today.`
  - `Please record today's 21点00分 expense: 药品, 980 yen.`
  - `Log that I spent 980 yen on 药品 at 21点00分 today.`
  - `Enter an expense for 药品 at 21点00分 today, amount 980 yen.`
  - `Add today's 21点00分 purchase of 药品 for 980 yen.`
  - `Please save a bill entry for 药品 costing 980 yen at 21点00分.`
  - `Record today's 药品 expense of 980 yen at 21点00分.`

- Japanese Variants: 10
  - `今日の21点00分に药品で980円使った記録を追加して`
  - `21点00分の药品 980円を支出として記録して`
  - `今日21点00分の药品代980円を登録して`
  - `21点00分に使った药品 980円を家計に記録して`
  - `今日21点00分の支出として药品 980円を保存して`
  - `药品に980円使ったので、今日21点00分の記録に入れて`
  - `今日の21点00分、药品で980円使ったことを記録して`
  - `21点00分の药品購入 980円を登録して`
  - `今日21点00分の药品支出980円を追加して`
  - `家計記録に21点00分の药品 980円を入れて`

### S3-20 账单记录 12

- Query: `记录今日21点20分，宠物粮消费2300日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天21点20分宠物粮消费2300日元`
  - `帮我登记今日21点20分的宠物粮支出2300日元`
  - `请记录今天21点20分花了2300日元买宠物粮`
  - `把今天21点20分宠物粮这笔2300日元记下来`
  - `新增一条消费记录：今日21点20分，宠物粮，2300日元`
  - `今天21点20分宠物粮花费2300日元，请帮我记录`
  - `请登记21点20分这笔宠物粮消费，金额2300日元`
  - `把今日21点20分的宠物粮支出2300日元录入账单`
  - `记录一下今天21点20分宠物粮用了2300日元`
  - `帮我添加消费：21点20分 宠物粮 2300日元`

- English Variants: 10
  - `Record an expense of 2300 yen for 宠物粮 at 21点20分 today.`
  - `Please log 宠物粮 costing 2300 yen at 21点20分 today.`
  - `Add a spending record for 宠物粮: 2300 yen at 21点20分 today.`
  - `Track 2300 yen spent on 宠物粮 at 21点20分 today.`
  - `Please record today's 21点20分 expense: 宠物粮, 2300 yen.`
  - `Log that I spent 2300 yen on 宠物粮 at 21点20分 today.`
  - `Enter an expense for 宠物粮 at 21点20分 today, amount 2300 yen.`
  - `Add today's 21点20分 purchase of 宠物粮 for 2300 yen.`
  - `Please save a bill entry for 宠物粮 costing 2300 yen at 21点20分.`
  - `Record today's 宠物粮 expense of 2300 yen at 21点20分.`

- Japanese Variants: 10
  - `今日の21点20分に宠物粮で2300円使った記録を追加して`
  - `21点20分の宠物粮 2300円を支出として記録して`
  - `今日21点20分の宠物粮代2300円を登録して`
  - `21点20分に使った宠物粮 2300円を家計に記録して`
  - `今日21点20分の支出として宠物粮 2300円を保存して`
  - `宠物粮に2300円使ったので、今日21点20分の記録に入れて`
  - `今日の21点20分、宠物粮で2300円使ったことを記録して`
  - `21点20分の宠物粮購入 2300円を登録して`
  - `今日21点20分の宠物粮支出2300円を追加して`
  - `家計記録に21点20分の宠物粮 2300円を入れて`

### S3-21 账单记录 13

- Query: `记录今日21点40分，网费消费4300日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天21点40分网费消费4300日元`
  - `帮我登记今日21点40分的网费支出4300日元`
  - `请记录今天21点40分花了4300日元买网费`
  - `把今天21点40分网费这笔4300日元记下来`
  - `新增一条消费记录：今日21点40分，网费，4300日元`
  - `今天21点40分网费花费4300日元，请帮我记录`
  - `请登记21点40分这笔网费消费，金额4300日元`
  - `把今日21点40分的网费支出4300日元录入账单`
  - `记录一下今天21点40分网费用了4300日元`
  - `帮我添加消费：21点40分 网费 4300日元`

- English Variants: 10
  - `Record an expense of 4300 yen for 网费 at 21点40分 today.`
  - `Please log 网费 costing 4300 yen at 21点40分 today.`
  - `Add a spending record for 网费: 4300 yen at 21点40分 today.`
  - `Track 4300 yen spent on 网费 at 21点40分 today.`
  - `Please record today's 21点40分 expense: 网费, 4300 yen.`
  - `Log that I spent 4300 yen on 网费 at 21点40分 today.`
  - `Enter an expense for 网费 at 21点40分 today, amount 4300 yen.`
  - `Add today's 21点40分 purchase of 网费 for 4300 yen.`
  - `Please save a bill entry for 网费 costing 4300 yen at 21点40分.`
  - `Record today's 网费 expense of 4300 yen at 21点40分.`

- Japanese Variants: 10
  - `今日の21点40分に网费で4300円使った記録を追加して`
  - `21点40分の网费 4300円を支出として記録して`
  - `今日21点40分の网费代4300円を登録して`
  - `21点40分に使った网费 4300円を家計に記録して`
  - `今日21点40分の支出として网费 4300円を保存して`
  - `网费に4300円使ったので、今日21点40分の記録に入れて`
  - `今日の21点40分、网费で4300円使ったことを記録して`
  - `21点40分の网费購入 4300円を登録して`
  - `今日21点40分の网费支出4300円を追加して`
  - `家計記録に21点40分の网费 4300円を入れて`

### S3-22 账单记录 14

- Query: `记录今日22点00分，水费消费3200日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天22点00分水费消费3200日元`
  - `帮我登记今日22点00分的水费支出3200日元`
  - `请记录今天22点00分花了3200日元买水费`
  - `把今天22点00分水费这笔3200日元记下来`
  - `新增一条消费记录：今日22点00分，水费，3200日元`
  - `今天22点00分水费花费3200日元，请帮我记录`
  - `请登记22点00分这笔水费消费，金额3200日元`
  - `把今日22点00分的水费支出3200日元录入账单`
  - `记录一下今天22点00分水费用了3200日元`
  - `帮我添加消费：22点00分 水费 3200日元`

- English Variants: 10
  - `Record an expense of 3200 yen for 水费 at 22点00分 today.`
  - `Please log 水费 costing 3200 yen at 22点00分 today.`
  - `Add a spending record for 水费: 3200 yen at 22点00分 today.`
  - `Track 3200 yen spent on 水费 at 22点00分 today.`
  - `Please record today's 22点00分 expense: 水费, 3200 yen.`
  - `Log that I spent 3200 yen on 水费 at 22点00分 today.`
  - `Enter an expense for 水费 at 22点00分 today, amount 3200 yen.`
  - `Add today's 22点00分 purchase of 水费 for 3200 yen.`
  - `Please save a bill entry for 水费 costing 3200 yen at 22点00分.`
  - `Record today's 水费 expense of 3200 yen at 22点00分.`

- Japanese Variants: 10
  - `今日の22点00分に水费で3200円使った記録を追加して`
  - `22点00分の水费 3200円を支出として記録して`
  - `今日22点00分の水费代3200円を登録して`
  - `22点00分に使った水费 3200円を家計に記録して`
  - `今日22点00分の支出として水费 3200円を保存して`
  - `水费に3200円使ったので、今日22点00分の記録に入れて`
  - `今日の22点00分、水费で3200円使ったことを記録して`
  - `22点00分の水费購入 3200円を登録して`
  - `今日22点00分の水费支出3200円を追加して`
  - `家計記録に22点00分の水费 3200円を入れて`

### S3-23 账单记录 15

- Query: `记录今日22点10分，电费消费5100日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天22点10分电费消费5100日元`
  - `帮我登记今日22点10分的电费支出5100日元`
  - `请记录今天22点10分花了5100日元买电费`
  - `把今天22点10分电费这笔5100日元记下来`
  - `新增一条消费记录：今日22点10分，电费，5100日元`
  - `今天22点10分电费花费5100日元，请帮我记录`
  - `请登记22点10分这笔电费消费，金额5100日元`
  - `把今日22点10分的电费支出5100日元录入账单`
  - `记录一下今天22点10分电费用了5100日元`
  - `帮我添加消费：22点10分 电费 5100日元`

- English Variants: 10
  - `Record an expense of 5100 yen for 电费 at 22点10分 today.`
  - `Please log 电费 costing 5100 yen at 22点10分 today.`
  - `Add a spending record for 电费: 5100 yen at 22点10分 today.`
  - `Track 5100 yen spent on 电费 at 22点10分 today.`
  - `Please record today's 22点10分 expense: 电费, 5100 yen.`
  - `Log that I spent 5100 yen on 电费 at 22点10分 today.`
  - `Enter an expense for 电费 at 22点10分 today, amount 5100 yen.`
  - `Add today's 22点10分 purchase of 电费 for 5100 yen.`
  - `Please save a bill entry for 电费 costing 5100 yen at 22点10分.`
  - `Record today's 电费 expense of 5100 yen at 22点10分.`

- Japanese Variants: 10
  - `今日の22点10分に电费で5100円使った記録を追加して`
  - `22点10分の电费 5100円を支出として記録して`
  - `今日22点10分の电费代5100円を登録して`
  - `22点10分に使った电费 5100円を家計に記録して`
  - `今日22点10分の支出として电费 5100円を保存して`
  - `电费に5100円使ったので、今日22点10分の記録に入れて`
  - `今日の22点10分、电费で5100円使ったことを記録して`
  - `22点10分の电费購入 5100円を登録して`
  - `今日22点10分の电费支出5100円を追加して`
  - `家計記録に22点10分の电费 5100円を入れて`

### S3-24 账单列表 15

- Query: `查看家庭账单有哪些记录`
- Expected: 返回当前账单记录列表。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `查看家庭账单里的记录`
  - `帮我列出家庭账单有哪些记录`
  - `家庭账单目前都记录了什么`
  - `请显示家庭账单的全部记录`
  - `我想看一下家庭账单里的内容`
  - `把家庭账单的记录给我看看`
  - `查看一下家庭账单都有哪些条目`
  - `帮我打开家庭账单记录`
  - `列出家庭账单目前的记录`
  - `请展示家庭账单中的所有记录`

- English Variants: 10
  - `Show me the records in 家庭账单.`
  - `What records are in 家庭账单?`
  - `Please list the entries under 家庭账单.`
  - `Can you display all records in 家庭账单?`
  - `I want to check the records for 家庭账单.`
  - `Let me see what has been recorded in 家庭账单.`
  - `Please open 家庭账单 and show the entries.`
  - `List everything recorded in 家庭账单.`
  - `Could you pull up the records from 家庭账单?`
  - `Show all entries stored in 家庭账单.`

- Japanese Variants: 10
  - `家庭账单 の記録を見せて`
  - `家庭账单 にある記録一覧を表示して`
  - `家庭账单 の登録内容を確認したい`
  - `家庭账单 の記録を全部見たい`
  - `家庭账单 に入っている情報を見せて`
  - `家庭账单 の内容を一覧表示して`
  - `家庭账单 の記録を教えて`
  - `家庭账单 のエントリーを確認して`
  - `家庭账单 の登録データを開いて`
  - `家庭账单 に何が記録されているか見せて`

### S3-25 账单导出 15

- Query: `导出家庭账单`
- Expected: 导出当前账单记录为 Excel。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `导出家庭账单`
  - `把家庭账单导出来`
  - `请帮我导出家庭账单`
  - `生成家庭账单的导出文件`
  - `我想导出家庭账单的数据`
  - `请把家庭账单内容输出成文件`
  - `帮我准备家庭账单的导出结果`
  - `导出一下家庭账单相关内容`
  - `请生成家庭账单的可导出文件`
  - `把家庭账单做成导出文档`

- English Variants: 10
  - `Export 家庭账单.`
  - `Please export 家庭账单.`
  - `I need an export of 家庭账单.`
  - `Can you export the data export for 家庭账单?`
  - `Generate an export for 家庭账单.`
  - `Please create an export file for 家庭账单.`
  - `Export the data from 家庭账单.`
  - `Could you prepare an export for 家庭账单?`
  - `I want to download the exported data export for 家庭账单.`
  - `Please output 家庭账单 as an export file.`

- Japanese Variants: 10
  - `家庭账单 をエクスポートして`
  - `家庭账单 のデータを出力して`
  - `家庭账单 を書き出してください`
  - `家庭账单 の内容をエクスポートしたい`
  - `家庭账单 のエクスポートファイルを作って`
  - `家庭账单 を外部出力して`
  - `家庭账单 の記録をファイルで出して`
  - `家庭账单 のデータを出力形式にして`
  - `家庭账单 をダウンロードできる形で出して`
  - `家庭账单 のエクスポートを準備して`

### S3-26 账单汇总阈值 15

- Query: `到今天为止消费总额是多少，如果超过20000日元产生提醒，并把提醒发送到 homehub`
- Expected: 返回累计总额，并根据阈值给出提示。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `到今天为止消费总额是多少，如果超过20000日元产生提醒我，并把提醒发送到 homehub`
  - `帮我设置一个提醒，到今天为止消费总额是多少，如果超过20000日元产生，并把提醒发送到 homehub`
  - `请在到今天为止消费总额是多少，如果超过20000日元产生提醒我去，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超过20000日元产生记得提醒我，并把提醒发送到 homehub`
  - `我想在到今天为止消费总额是多少，如果超过20000日元产生收到提醒：，并把提醒发送到 homehub`
  - `请给我设一个到今天为止消费总额是多少，如果超过20000日元产生的提醒，内容是，并把提醒发送到 homehub`
  - `到今天为止消费总额是多少，如果超过20000日元产生帮我提醒一下，并把提醒发送到 homehub`
  - `记得在到今天为止消费总额是多少，如果超过20000日元产生提醒我，并把提醒发送到 homehub`
  - `请添加提醒：到今天为止消费总额是多少，如果超过20000日元产生，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超过20000日元产生通知我，并把提醒发送到 homehub`

- English Variants: 10
  - `Remind me 到今天为止消费总额是多少，如果超过20000日元产生 to ，并把提醒发送到 homehub.`
  - `Set a reminder 到今天为止消费总额是多少，如果超过20000日元产生 for me to ，并把提醒发送到 homehub.`
  - `Please remind me 到今天为止消费总额是多少，如果超过20000日元产生 that I need to ，并把提醒发送到 homehub.`
  - `Can you create a reminder 到今天为止消费总额是多少，如果超过20000日元产生 for ，并把提醒发送到 homehub?`
  - `I need a reminder 到今天为止消费总额是多少，如果超过20000日元产生 to ，并把提醒发送到 homehub.`
  - `Put in a reminder for 到今天为止消费总额是多少，如果超过20000日元产生: ，并把提醒发送到 homehub.`
  - `Schedule a reminder 到今天为止消费总额是多少，如果超过20000日元产生 so I remember to ，并把提醒发送到 homehub.`
  - `Please alert me 到今天为止消费总额是多少，如果超过20000日元产生 to ，并把提醒发送到 homehub.`
  - `Set me a 到今天为止消费总额是多少，如果超过20000日元产生 reminder to ，并把提醒发送到 homehub.`
  - `Create a reminder telling me 到今天为止消费总额是多少，如果超过20000日元产生 to ，并把提醒发送到 homehub.`

- Japanese Variants: 10
  - `到今天为止消费总额是多少，如果超过20000日元产生に，并把提醒发送到 homehubとリマインドして`
  - `到今天为止消费总额是多少，如果超过20000日元产生に，并把提醒发送到 homehubことを知らせて`
  - `到今天为止消费总额是多少，如果超过20000日元产生用に「，并把提醒发送到 homehub」のリマインダーを設定して`
  - `到今天为止消费总额是多少，如果超过20000日元产生になったら，并把提醒发送到 homehubと通知して`
  - `到今天为止消费总额是多少，如果超过20000日元产生のリマインダーとして，并把提醒发送到 homehubを登録して`
  - `到今天为止消费总额是多少，如果超过20000日元产生に，并把提醒发送到 homehubの通知を入れて`
  - `到今天为止消费总额是多少，如果超过20000日元产生に，并把提醒发送到 homehubことを忘れないよう知らせて`
  - `到今天为止消费总额是多少，如果超过20000日元产生の時刻で，并把提醒发送到 homehubをリマインドして`
  - `到今天为止消费总额是多少，如果超过20000日元产生に私へ，并把提醒发送到 homehubと伝えて`
  - `到今天为止消费总额是多少，如果超过20000日元产生用に，并把提醒发送到 homehubの通知を作って`

### S3-27 账单汇总导出 15

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回累计总额并导出 Excel。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `统计到今天为止的消费总额，并把消费信息生成 Excel 文档`
  - `帮我算一下当前消费总额，再导出 Excel 明细`
  - `请汇总截至今天的消费，并生成一份 Excel 文件`
  - `到今天为止一共花了多少？顺便把消费信息做成 Excel`
  - `我想看累计消费总额，并导出消费 Excel 文档`
  - `请统计总支出，同时生成消费明细的 Excel`
  - `帮我把消费总额算出来，并把记录导出成 Excel`
  - `请生成截至今天的消费汇总和 Excel 文档`
  - `看一下当前总消费，再输出一份 Excel 表格`
  - `把到今天的消费合计出来，并生成 Excel 文件`

- English Variants: 10
  - `What's the total spending up to today, and generate an Excel file with the expense details.`
  - `Please calculate total spending through today and create an Excel document of the expenses.`
  - `Show me the total spent so far today, and export the spending data to Excel.`
  - `Tell me the total expenses up to today and make an Excel file with the details.`
  - `I want today's cumulative spending and an Excel export of the expense information.`
  - `Please total the spending so far and generate an Excel sheet of all expense records.`
  - `How much have we spent up to today? Also create an Excel file of the spending details.`
  - `Calculate the total spending through today and output the expense data as Excel.`
  - `Give me the spending total so far and build an Excel document from the expense info.`
  - `Please provide today's total expense amount and export the expense details into Excel.`

- Japanese Variants: 10
  - `今日までの支出総額を出して、支出情報を Excel にまとめて`
  - `ここまでの支出合計を計算して、Excel 文書を作って`
  - `今日時点の消費総額を確認し、Excel ファイルも生成して`
  - `支出合計を出して、明細を Excel にしてほしい`
  - `累計支出とその内容を Excel で出力して`
  - `今日までの出費を集計して、Excel 形式でまとめて`
  - `支出の合計を教えて、その情報を Excel にして`
  - `現在までの消費額を計算し、Excel ファイルを作成して`
  - `ここまでの支出情報を Excel 文書として出して`
  - `支出合計の確認と、Excel への書き出しをお願い`

### S3-28 账单记录 16

- Query: `记录今日22点20分，学用品消费890日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天22点20分学用品消费890日元`
  - `帮我登记今日22点20分的学用品支出890日元`
  - `请记录今天22点20分花了890日元买学用品`
  - `把今天22点20分学用品这笔890日元记下来`
  - `新增一条消费记录：今日22点20分，学用品，890日元`
  - `今天22点20分学用品花费890日元，请帮我记录`
  - `请登记22点20分这笔学用品消费，金额890日元`
  - `把今日22点20分的学用品支出890日元录入账单`
  - `记录一下今天22点20分学用品用了890日元`
  - `帮我添加消费：22点20分 学用品 890日元`

- English Variants: 10
  - `Record an expense of 890 yen for 学用品 at 22点20分 today.`
  - `Please log 学用品 costing 890 yen at 22点20分 today.`
  - `Add a spending record for 学用品: 890 yen at 22点20分 today.`
  - `Track 890 yen spent on 学用品 at 22点20分 today.`
  - `Please record today's 22点20分 expense: 学用品, 890 yen.`
  - `Log that I spent 890 yen on 学用品 at 22点20分 today.`
  - `Enter an expense for 学用品 at 22点20分 today, amount 890 yen.`
  - `Add today's 22点20分 purchase of 学用品 for 890 yen.`
  - `Please save a bill entry for 学用品 costing 890 yen at 22点20分.`
  - `Record today's 学用品 expense of 890 yen at 22点20分.`

- Japanese Variants: 10
  - `今日の22点20分に学用品で890円使った記録を追加して`
  - `22点20分の学用品 890円を支出として記録して`
  - `今日22点20分の学用品代890円を登録して`
  - `22点20分に使った学用品 890円を家計に記録して`
  - `今日22点20分の支出として学用品 890円を保存して`
  - `学用品に890円使ったので、今日22点20分の記録に入れて`
  - `今日の22点20分、学用品で890円使ったことを記録して`
  - `22点20分の学用品購入 890円を登録して`
  - `今日22点20分の学用品支出890円を追加して`
  - `家計記録に22点20分の学用品 890円を入れて`

### S3-29 账单记录 17

- Query: `记录今日22点30分，洗衣液消费640日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天22点30分洗衣液消费640日元`
  - `帮我登记今日22点30分的洗衣液支出640日元`
  - `请记录今天22点30分花了640日元买洗衣液`
  - `把今天22点30分洗衣液这笔640日元记下来`
  - `新增一条消费记录：今日22点30分，洗衣液，640日元`
  - `今天22点30分洗衣液花费640日元，请帮我记录`
  - `请登记22点30分这笔洗衣液消费，金额640日元`
  - `把今日22点30分的洗衣液支出640日元录入账单`
  - `记录一下今天22点30分洗衣液用了640日元`
  - `帮我添加消费：22点30分 洗衣液 640日元`

- English Variants: 10
  - `Record an expense of 640 yen for 洗衣液 at 22点30分 today.`
  - `Please log 洗衣液 costing 640 yen at 22点30分 today.`
  - `Add a spending record for 洗衣液: 640 yen at 22点30分 today.`
  - `Track 640 yen spent on 洗衣液 at 22点30分 today.`
  - `Please record today's 22点30分 expense: 洗衣液, 640 yen.`
  - `Log that I spent 640 yen on 洗衣液 at 22点30分 today.`
  - `Enter an expense for 洗衣液 at 22点30分 today, amount 640 yen.`
  - `Add today's 22点30分 purchase of 洗衣液 for 640 yen.`
  - `Please save a bill entry for 洗衣液 costing 640 yen at 22点30分.`
  - `Record today's 洗衣液 expense of 640 yen at 22点30分.`

- Japanese Variants: 10
  - `今日の22点30分に洗衣液で640円使った記録を追加して`
  - `22点30分の洗衣液 640円を支出として記録して`
  - `今日22点30分の洗衣液代640円を登録して`
  - `22点30分に使った洗衣液 640円を家計に記録して`
  - `今日22点30分の支出として洗衣液 640円を保存して`
  - `洗衣液に640円使ったので、今日22点30分の記録に入れて`
  - `今日の22点30分、洗衣液で640円使ったことを記録して`
  - `22点30分の洗衣液購入 640円を登録して`
  - `今日22点30分の洗衣液支出640円を追加して`
  - `家計記録に22点30分の洗衣液 640円を入れて`

### S3-30 账单记录 18

- Query: `记录今日22点40分，生日蛋糕消费2750日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天22点40分生日蛋糕消费2750日元`
  - `帮我登记今日22点40分的生日蛋糕支出2750日元`
  - `请记录今天22点40分花了2750日元买生日蛋糕`
  - `把今天22点40分生日蛋糕这笔2750日元记下来`
  - `新增一条消费记录：今日22点40分，生日蛋糕，2750日元`
  - `今天22点40分生日蛋糕花费2750日元，请帮我记录`
  - `请登记22点40分这笔生日蛋糕消费，金额2750日元`
  - `把今日22点40分的生日蛋糕支出2750日元录入账单`
  - `记录一下今天22点40分生日蛋糕用了2750日元`
  - `帮我添加消费：22点40分 生日蛋糕 2750日元`

- English Variants: 10
  - `Record an expense of 2750 yen for 生日蛋糕 at 22点40分 today.`
  - `Please log 生日蛋糕 costing 2750 yen at 22点40分 today.`
  - `Add a spending record for 生日蛋糕: 2750 yen at 22点40分 today.`
  - `Track 2750 yen spent on 生日蛋糕 at 22点40分 today.`
  - `Please record today's 22点40分 expense: 生日蛋糕, 2750 yen.`
  - `Log that I spent 2750 yen on 生日蛋糕 at 22点40分 today.`
  - `Enter an expense for 生日蛋糕 at 22点40分 today, amount 2750 yen.`
  - `Add today's 22点40分 purchase of 生日蛋糕 for 2750 yen.`
  - `Please save a bill entry for 生日蛋糕 costing 2750 yen at 22点40分.`
  - `Record today's 生日蛋糕 expense of 2750 yen at 22点40分.`

- Japanese Variants: 10
  - `今日の22点40分に生日蛋糕で2750円使った記録を追加して`
  - `22点40分の生日蛋糕 2750円を支出として記録して`
  - `今日22点40分の生日蛋糕代2750円を登録して`
  - `22点40分に使った生日蛋糕 2750円を家計に記録して`
  - `今日22点40分の支出として生日蛋糕 2750円を保存して`
  - `生日蛋糕に2750円使ったので、今日22点40分の記録に入れて`
  - `今日の22点40分、生日蛋糕で2750円使ったことを記録して`
  - `22点40分の生日蛋糕購入 2750円を登録して`
  - `今日22点40分の生日蛋糕支出2750円を追加して`
  - `家計記録に22点40分の生日蛋糕 2750円を入れて`

### S3-31 账单记录 19

- Query: `记录今日22点50分，咖啡消费450日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天22点50分咖啡消费450日元`
  - `帮我登记今日22点50分的咖啡支出450日元`
  - `请记录今天22点50分花了450日元买咖啡`
  - `把今天22点50分咖啡这笔450日元记下来`
  - `新增一条消费记录：今日22点50分，咖啡，450日元`
  - `今天22点50分咖啡花费450日元，请帮我记录`
  - `请登记22点50分这笔咖啡消费，金额450日元`
  - `把今日22点50分的咖啡支出450日元录入账单`
  - `记录一下今天22点50分咖啡用了450日元`
  - `帮我添加消费：22点50分 咖啡 450日元`

- English Variants: 10
  - `Record an expense of 450 yen for 咖啡 at 22点50分 today.`
  - `Please log 咖啡 costing 450 yen at 22点50分 today.`
  - `Add a spending record for 咖啡: 450 yen at 22点50分 today.`
  - `Track 450 yen spent on 咖啡 at 22点50分 today.`
  - `Please record today's 22点50分 expense: 咖啡, 450 yen.`
  - `Log that I spent 450 yen on 咖啡 at 22点50分 today.`
  - `Enter an expense for 咖啡 at 22点50分 today, amount 450 yen.`
  - `Add today's 22点50分 purchase of 咖啡 for 450 yen.`
  - `Please save a bill entry for 咖啡 costing 450 yen at 22点50分.`
  - `Record today's 咖啡 expense of 450 yen at 22点50分.`

- Japanese Variants: 10
  - `今日の22点50分に咖啡で450円使った記録を追加して`
  - `22点50分の咖啡 450円を支出として記録して`
  - `今日22点50分の咖啡代450円を登録して`
  - `22点50分に使った咖啡 450円を家計に記録して`
  - `今日22点50分の支出として咖啡 450円を保存して`
  - `咖啡に450円使ったので、今日22点50分の記録に入れて`
  - `今日の22点50分、咖啡で450円使ったことを記録して`
  - `22点50分の咖啡購入 450円を登録して`
  - `今日22点50分の咖啡支出450円を追加して`
  - `家計記録に22点50分の咖啡 450円を入れて`

### S3-32 账单记录 20

- Query: `记录今日23点00分，夜宵消费990日元`
- Expected: 通过家庭账单智能体完成记录。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `记录今天23点00分夜宵消费990日元`
  - `帮我登记今日23点00分的夜宵支出990日元`
  - `请记录今天23点00分花了990日元买夜宵`
  - `把今天23点00分夜宵这笔990日元记下来`
  - `新增一条消费记录：今日23点00分，夜宵，990日元`
  - `今天23点00分夜宵花费990日元，请帮我记录`
  - `请登记23点00分这笔夜宵消费，金额990日元`
  - `把今日23点00分的夜宵支出990日元录入账单`
  - `记录一下今天23点00分夜宵用了990日元`
  - `帮我添加消费：23点00分 夜宵 990日元`

- English Variants: 10
  - `Record an expense of 990 yen for 夜宵 at 23点00分 today.`
  - `Please log 夜宵 costing 990 yen at 23点00分 today.`
  - `Add a spending record for 夜宵: 990 yen at 23点00分 today.`
  - `Track 990 yen spent on 夜宵 at 23点00分 today.`
  - `Please record today's 23点00分 expense: 夜宵, 990 yen.`
  - `Log that I spent 990 yen on 夜宵 at 23点00分 today.`
  - `Enter an expense for 夜宵 at 23点00分 today, amount 990 yen.`
  - `Add today's 23点00分 purchase of 夜宵 for 990 yen.`
  - `Please save a bill entry for 夜宵 costing 990 yen at 23点00分.`
  - `Record today's 夜宵 expense of 990 yen at 23点00分.`

- Japanese Variants: 10
  - `今日の23点00分に夜宵で990円使った記録を追加して`
  - `23点00分の夜宵 990円を支出として記録して`
  - `今日23点00分の夜宵代990円を登録して`
  - `23点00分に使った夜宵 990円を家計に記録して`
  - `今日23点00分の支出として夜宵 990円を保存して`
  - `夜宵に990円使ったので、今日23点00分の記録に入れて`
  - `今日の23点00分、夜宵で990円使ったことを記録して`
  - `23点00分の夜宵購入 990円を登録して`
  - `今日23点00分の夜宵支出990円を追加して`
  - `家計記録に23点00分の夜宵 990円を入れて`

### S3-33 账单列表 20

- Query: `查看家庭账单有哪些记录`
- Expected: 返回当前账单记录列表。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `查看家庭账单里的记录`
  - `帮我列出家庭账单有哪些记录`
  - `家庭账单目前都记录了什么`
  - `请显示家庭账单的全部记录`
  - `我想看一下家庭账单里的内容`
  - `把家庭账单的记录给我看看`
  - `查看一下家庭账单都有哪些条目`
  - `帮我打开家庭账单记录`
  - `列出家庭账单目前的记录`
  - `请展示家庭账单中的所有记录`

- English Variants: 10
  - `Show me the records in 家庭账单.`
  - `What records are in 家庭账单?`
  - `Please list the entries under 家庭账单.`
  - `Can you display all records in 家庭账单?`
  - `I want to check the records for 家庭账单.`
  - `Let me see what has been recorded in 家庭账单.`
  - `Please open 家庭账单 and show the entries.`
  - `List everything recorded in 家庭账单.`
  - `Could you pull up the records from 家庭账单?`
  - `Show all entries stored in 家庭账单.`

- Japanese Variants: 10
  - `家庭账单 の記録を見せて`
  - `家庭账单 にある記録一覧を表示して`
  - `家庭账单 の登録内容を確認したい`
  - `家庭账单 の記録を全部見たい`
  - `家庭账单 に入っている情報を見せて`
  - `家庭账单 の内容を一覧表示して`
  - `家庭账单 の記録を教えて`
  - `家庭账单 のエントリーを確認して`
  - `家庭账单 の登録データを開いて`
  - `家庭账单 に何が記録されているか見せて`

### S3-34 账单导出 20

- Query: `导出家庭账单`
- Expected: 导出当前账单记录为 Excel。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `导出家庭账单`
  - `把家庭账单导出来`
  - `请帮我导出家庭账单`
  - `生成家庭账单的导出文件`
  - `我想导出家庭账单的数据`
  - `请把家庭账单内容输出成文件`
  - `帮我准备家庭账单的导出结果`
  - `导出一下家庭账单相关内容`
  - `请生成家庭账单的可导出文件`
  - `把家庭账单做成导出文档`

- English Variants: 10
  - `Export 家庭账单.`
  - `Please export 家庭账单.`
  - `I need an export of 家庭账单.`
  - `Can you export the data export for 家庭账单?`
  - `Generate an export for 家庭账单.`
  - `Please create an export file for 家庭账单.`
  - `Export the data from 家庭账单.`
  - `Could you prepare an export for 家庭账单?`
  - `I want to download the exported data export for 家庭账单.`
  - `Please output 家庭账单 as an export file.`

- Japanese Variants: 10
  - `家庭账单 をエクスポートして`
  - `家庭账单 のデータを出力して`
  - `家庭账单 を書き出してください`
  - `家庭账单 の内容をエクスポートしたい`
  - `家庭账单 のエクスポートファイルを作って`
  - `家庭账单 を外部出力して`
  - `家庭账单 の記録をファイルで出して`
  - `家庭账单 のデータを出力形式にして`
  - `家庭账单 をダウンロードできる形で出して`
  - `家庭账单 のエクスポートを準備して`

### S3-35 账单汇总阈值 20

- Query: `到今天为止消费总额是多少，如果超过35000日元产生提醒，并把提醒发送到 homehub`
- Expected: 返回累计总额，并根据阈值给出提示。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `到今天为止消费总额是多少，如果超过35000日元产生提醒我，并把提醒发送到 homehub`
  - `帮我设置一个提醒，到今天为止消费总额是多少，如果超过35000日元产生，并把提醒发送到 homehub`
  - `请在到今天为止消费总额是多少，如果超过35000日元产生提醒我去，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超过35000日元产生记得提醒我，并把提醒发送到 homehub`
  - `我想在到今天为止消费总额是多少，如果超过35000日元产生收到提醒：，并把提醒发送到 homehub`
  - `请给我设一个到今天为止消费总额是多少，如果超过35000日元产生的提醒，内容是，并把提醒发送到 homehub`
  - `到今天为止消费总额是多少，如果超过35000日元产生帮我提醒一下，并把提醒发送到 homehub`
  - `记得在到今天为止消费总额是多少，如果超过35000日元产生提醒我，并把提醒发送到 homehub`
  - `请添加提醒：到今天为止消费总额是多少，如果超过35000日元产生，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超过35000日元产生通知我，并把提醒发送到 homehub`

- English Variants: 10
  - `Remind me 到今天为止消费总额是多少，如果超过35000日元产生 to ，并把提醒发送到 homehub.`
  - `Set a reminder 到今天为止消费总额是多少，如果超过35000日元产生 for me to ，并把提醒发送到 homehub.`
  - `Please remind me 到今天为止消费总额是多少，如果超过35000日元产生 that I need to ，并把提醒发送到 homehub.`
  - `Can you create a reminder 到今天为止消费总额是多少，如果超过35000日元产生 for ，并把提醒发送到 homehub?`
  - `I need a reminder 到今天为止消费总额是多少，如果超过35000日元产生 to ，并把提醒发送到 homehub.`
  - `Put in a reminder for 到今天为止消费总额是多少，如果超过35000日元产生: ，并把提醒发送到 homehub.`
  - `Schedule a reminder 到今天为止消费总额是多少，如果超过35000日元产生 so I remember to ，并把提醒发送到 homehub.`
  - `Please alert me 到今天为止消费总额是多少，如果超过35000日元产生 to ，并把提醒发送到 homehub.`
  - `Set me a 到今天为止消费总额是多少，如果超过35000日元产生 reminder to ，并把提醒发送到 homehub.`
  - `Create a reminder telling me 到今天为止消费总额是多少，如果超过35000日元产生 to ，并把提醒发送到 homehub.`

- Japanese Variants: 10
  - `到今天为止消费总额是多少，如果超过35000日元产生に，并把提醒发送到 homehubとリマインドして`
  - `到今天为止消费总额是多少，如果超过35000日元产生に，并把提醒发送到 homehubことを知らせて`
  - `到今天为止消费总额是多少，如果超过35000日元产生用に「，并把提醒发送到 homehub」のリマインダーを設定して`
  - `到今天为止消费总额是多少，如果超过35000日元产生になったら，并把提醒发送到 homehubと通知して`
  - `到今天为止消费总额是多少，如果超过35000日元产生のリマインダーとして，并把提醒发送到 homehubを登録して`
  - `到今天为止消费总额是多少，如果超过35000日元产生に，并把提醒发送到 homehubの通知を入れて`
  - `到今天为止消费总额是多少，如果超过35000日元产生に，并把提醒发送到 homehubことを忘れないよう知らせて`
  - `到今天为止消费总额是多少，如果超过35000日元产生の時刻で，并把提醒发送到 homehubをリマインドして`
  - `到今天为止消费总额是多少，如果超过35000日元产生に私へ，并把提醒发送到 homehubと伝えて`
  - `到今天为止消费总额是多少，如果超过35000日元产生用に，并把提醒发送到 homehubの通知を作って`

### S3-36 账单汇总导出 20

- Query: `到今天为止消费总额是多少，并将消费的信息生成excel文档`
- Expected: 返回累计总额并导出 Excel。
- Reset Before: No
- Setup Queries: 0

- Chinese Variants: 10
  - `统计到今天为止的消费总额，并把消费信息生成 Excel 文档`
  - `帮我算一下当前消费总额，再导出 Excel 明细`
  - `请汇总截至今天的消费，并生成一份 Excel 文件`
  - `到今天为止一共花了多少？顺便把消费信息做成 Excel`
  - `我想看累计消费总额，并导出消费 Excel 文档`
  - `请统计总支出，同时生成消费明细的 Excel`
  - `帮我把消费总额算出来，并把记录导出成 Excel`
  - `请生成截至今天的消费汇总和 Excel 文档`
  - `看一下当前总消费，再输出一份 Excel 表格`
  - `把到今天的消费合计出来，并生成 Excel 文件`

- English Variants: 10
  - `What's the total spending up to today, and generate an Excel file with the expense details.`
  - `Please calculate total spending through today and create an Excel document of the expenses.`
  - `Show me the total spent so far today, and export the spending data to Excel.`
  - `Tell me the total expenses up to today and make an Excel file with the details.`
  - `I want today's cumulative spending and an Excel export of the expense information.`
  - `Please total the spending so far and generate an Excel sheet of all expense records.`
  - `How much have we spent up to today? Also create an Excel file of the spending details.`
  - `Calculate the total spending through today and output the expense data as Excel.`
  - `Give me the spending total so far and build an Excel document from the expense info.`
  - `Please provide today's total expense amount and export the expense details into Excel.`

- Japanese Variants: 10
  - `今日までの支出総額を出して、支出情報を Excel にまとめて`
  - `ここまでの支出合計を計算して、Excel 文書を作って`
  - `今日時点の消費総額を確認し、Excel ファイルも生成して`
  - `支出合計を出して、明細を Excel にしてほしい`
  - `累計支出とその内容を Excel で出力して`
  - `今日までの出費を集計して、Excel 形式でまとめて`
  - `支出の合計を教えて、その情報を Excel にして`
  - `現在までの消費額を計算し、Excel ファイルを作成して`
  - `ここまでの支出情報を Excel 文書として出して`
  - `支出合計の確認と、Excel への書き出しをお願い`

### S3-37 身体状况记录 输入记录

- Query: `请在身体状况记录中记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
- Expected: 将阶段3输入写入 身体状况记录，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

- Chinese Variants: 10
  - `请在身体状况记录中新增记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `帮我把这条内容记到身体状况记录里：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `把以下信息记录到身体状况记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `请将奶奶今天体温37.5度，轻微咳嗽，已喝水休息录入到身体状况记录`
  - `在身体状况记录里添加这条记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `帮我往身体状况记录中写入：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `请保存到身体状况记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `将这条信息登记到身体状况记录：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `请在身体状况记录里面记录下：奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `把奶奶今天体温37.5度，轻微咳嗽，已喝水休息这条内容存到身体状况记录`

- English Variants: 10
  - `Please add this record to 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `Record the following in 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `Can you save this entry in 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `Log this information under 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `Please create a new record in 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `Put this into 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `Add this content to 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `Save the following note in 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `Enter this record for 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `Please store this in 身体状况记录: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`

- Japanese Variants: 10
  - `身体状况记录 に次の内容を記録して: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `身体状况记录 へこの情報を追加して: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `身体状况记录 にこの記録を保存して: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `身体状况记录 に 奶奶今天体温37.5度，轻微咳嗽，已喝水休息 を登録して`
  - `身体状况记录 の記録として 奶奶今天体温37.5度，轻微咳嗽，已喝水休息 を入れて`
  - `身体状况记录 に以下を記録してください: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `身体状况记录 へこの内容を書き込んで: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `身体状况记录 に新しい記録を追加: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`
  - `奶奶今天体温37.5度，轻微咳嗽，已喝水休息 を 身体状况记录 に保存して`
  - `身体状况记录 にこの内容を残して: 奶奶今天体温37.5度，轻微咳嗽，已喝水休息`

### S3-38 身体状况记录 输出查询

- Query: `查看身体状况记录有哪些记录`
- Expected: 返回 身体状况记录 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `查看身体状况记录里的记录`
  - `帮我列出身体状况记录有哪些记录`
  - `身体状况记录目前都记录了什么`
  - `请显示身体状况记录的全部记录`
  - `我想看一下身体状况记录里的内容`
  - `把身体状况记录的记录给我看看`
  - `查看一下身体状况记录都有哪些条目`
  - `帮我打开身体状况记录记录`
  - `列出身体状况记录目前的记录`
  - `请展示身体状况记录中的所有记录`

- English Variants: 10
  - `Show me the records in 身体状况记录.`
  - `What records are in 身体状况记录?`
  - `Please list the entries under 身体状况记录.`
  - `Can you display all records in 身体状况记录?`
  - `I want to check the records for 身体状况记录.`
  - `Let me see what has been recorded in 身体状况记录.`
  - `Please open 身体状况记录 and show the entries.`
  - `List everything recorded in 身体状况记录.`
  - `Could you pull up the records from 身体状况记录?`
  - `Show all entries stored in 身体状况记录.`

- Japanese Variants: 10
  - `身体状况记录 の記録を見せて`
  - `身体状况记录 にある記録一覧を表示して`
  - `身体状况记录 の登録内容を確認したい`
  - `身体状况记录 の記録を全部見たい`
  - `身体状况记录 に入っている情報を見せて`
  - `身体状况记录 の内容を一覧表示して`
  - `身体状况记录 の記録を教えて`
  - `身体状况记录 のエントリーを確認して`
  - `身体状况记录 の登録データを開いて`
  - `身体状况记录 に何が記録されているか見せて`

### S3-39 身体状况记录 输出导出

- Query: `导出身体状况记录文档`
- Expected: 导出 身体状况记录 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `导出身体状况记录`
  - `把身体状况记录导出来`
  - `请帮我导出身体状况记录`
  - `生成身体状况记录的导出文件`
  - `我想导出身体状况记录的数据`
  - `请把身体状况记录内容输出成文件`
  - `帮我准备身体状况记录的导出结果`
  - `导出一下身体状况记录相关内容`
  - `请生成身体状况记录的可导出文件`
  - `把身体状况记录做成导出文档`

- English Variants: 10
  - `Export 身体状况记录.`
  - `Please export 身体状况记录.`
  - `I need an export of 身体状况记录.`
  - `Can you export the document for 身体状况记录?`
  - `Generate an export for 身体状况记录.`
  - `Please create an export file for 身体状况记录.`
  - `Export the data from 身体状况记录.`
  - `Could you prepare an export for 身体状况记录?`
  - `I want to download the exported document for 身体状况记录.`
  - `Please output 身体状况记录 as an export file.`

- Japanese Variants: 10
  - `身体状况记录 をエクスポートして`
  - `身体状况记录 のデータを出力して`
  - `身体状况记录 を書き出してください`
  - `身体状况记录 の内容をエクスポートしたい`
  - `身体状况记录 のエクスポートファイルを作って`
  - `身体状况记录 を外部出力して`
  - `身体状况记录 の記録をファイルで出して`
  - `身体状况记录 のデータを出力形式にして`
  - `身体状况记录 をダウンロードできる形で出して`
  - `身体状况记录 のエクスポートを準備して`

### S3-40 体检报告 输入记录

- Query: `请在体检报告中记录：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
- Expected: 将阶段3输入写入 体检报告，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

- Chinese Variants: 10
  - `请在体检报告中新增记录：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `帮我把这条内容记到体检报告里：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `把以下信息记录到体检报告：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `请将妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查录入到体检报告`
  - `在体检报告里添加这条记录：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `帮我往体检报告中写入：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `请保存到体检报告：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `将这条信息登记到体检报告：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `请在体检报告里面记录下：妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `把妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查这条内容存到体检报告`

- English Variants: 10
  - `Please add this record to 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `Record the following in 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `Can you save this entry in 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `Log this information under 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `Please create a new record in 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `Put this into 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `Add this content to 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `Save the following note in 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `Enter this record for 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `Please store this in 体检报告: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`

- Japanese Variants: 10
  - `体检报告 に次の内容を記録して: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `体检报告 へこの情報を追加して: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `体检报告 にこの記録を保存して: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `体检报告 に 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查 を登録して`
  - `体检报告 の記録として 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查 を入れて`
  - `体检报告 に以下を記録してください: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `体检报告 へこの内容を書き込んで: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `体检报告 に新しい記録を追加: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`
  - `妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查 を 体检报告 に保存して`
  - `体检报告 にこの内容を残して: 妈妈4月20日做血液检查，结果维生素D偏低，一个月后复查`

### S3-41 体检报告 输出查询

- Query: `查看体检报告有哪些记录`
- Expected: 返回 体检报告 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `查看体检报告里的记录`
  - `帮我列出体检报告有哪些记录`
  - `体检报告目前都记录了什么`
  - `请显示体检报告的全部记录`
  - `我想看一下体检报告里的内容`
  - `把体检报告的记录给我看看`
  - `查看一下体检报告都有哪些条目`
  - `帮我打开体检报告记录`
  - `列出体检报告目前的记录`
  - `请展示体检报告中的所有记录`

- English Variants: 10
  - `Show me the records in 体检报告.`
  - `What records are in 体检报告?`
  - `Please list the entries under 体检报告.`
  - `Can you display all records in 体检报告?`
  - `I want to check the records for 体检报告.`
  - `Let me see what has been recorded in 体检报告.`
  - `Please open 体检报告 and show the entries.`
  - `List everything recorded in 体检报告.`
  - `Could you pull up the records from 体检报告?`
  - `Show all entries stored in 体检报告.`

- Japanese Variants: 10
  - `体检报告 の記録を見せて`
  - `体检报告 にある記録一覧を表示して`
  - `体检报告 の登録内容を確認したい`
  - `体检报告 の記録を全部見たい`
  - `体检报告 に入っている情報を見せて`
  - `体检报告 の内容を一覧表示して`
  - `体检报告 の記録を教えて`
  - `体检报告 のエントリーを確認して`
  - `体检报告 の登録データを開いて`
  - `体检报告 に何が記録されているか見せて`

### S3-42 体检报告 输出导出

- Query: `导出体检报告文档`
- Expected: 导出 体检报告 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `导出体检报告`
  - `把体检报告导出来`
  - `请帮我导出体检报告`
  - `生成体检报告的导出文件`
  - `我想导出体检报告的数据`
  - `请把体检报告内容输出成文件`
  - `帮我准备体检报告的导出结果`
  - `导出一下体检报告相关内容`
  - `请生成体检报告的可导出文件`
  - `把体检报告做成导出文档`

- English Variants: 10
  - `Export 体检报告.`
  - `Please export 体检报告.`
  - `I need an export of 体检报告.`
  - `Can you export the document for 体检报告?`
  - `Generate an export for 体检报告.`
  - `Please create an export file for 体检报告.`
  - `Export the data from 体检报告.`
  - `Could you prepare an export for 体检报告?`
  - `I want to download the exported document for 体检报告.`
  - `Please output 体检报告 as an export file.`

- Japanese Variants: 10
  - `体检报告 をエクスポートして`
  - `体检报告 のデータを出力して`
  - `体检报告 を書き出してください`
  - `体检报告 の内容をエクスポートしたい`
  - `体检报告 のエクスポートファイルを作って`
  - `体检报告 を外部出力して`
  - `体检报告 の記録をファイルで出して`
  - `体检报告 のデータを出力形式にして`
  - `体检报告 をダウンロードできる形で出して`
  - `体检报告 のエクスポートを準備して`

### S3-43 医院复查提醒 输入记录

- Query: `请在医院复查提醒中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
- Expected: 将阶段3输入写入 医院复查提醒，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

- Chinese Variants: 10
  - `请在医院复查提醒我中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
  - `帮我设置一个提醒，请在医院复查中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
  - `请在请在医院复查提醒我去中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
  - `到请在医院复查记得提醒我中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
  - `我想在请在医院复查收到提醒：中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
  - `请给我设一个请在医院复查的提醒，内容是中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
  - `请在医院复查帮我提醒一下中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
  - `记得在请在医院复查提醒我中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
  - `请添加提醒：请在医院复查中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`
  - `到请在医院复查通知我中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub`

- English Variants: 10
  - `Remind me 请在医院复查 to 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub.`
  - `Set a reminder 请在医院复查 for me to 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub.`
  - `Please remind me 请在医院复查 that I need to 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub.`
  - `Can you create a reminder 请在医院复查 for 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub?`
  - `I need a reminder 请在医院复查 to 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub.`
  - `Put in a reminder for 请在医院复查: 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub.`
  - `Schedule a reminder 请在医院复查 so I remember to 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub.`
  - `Please alert me 请在医院复查 to 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub.`
  - `Set me a 请在医院复查 reminder to 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub.`
  - `Create a reminder telling me 请在医院复查 to 中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub.`

- Japanese Variants: 10
  - `请在医院复查に中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHubとリマインドして`
  - `请在医院复查に中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHubことを知らせて`
  - `请在医院复查用に「中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHub」のリマインダーを設定して`
  - `请在医院复查になったら中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHubと通知して`
  - `请在医院复查のリマインダーとして中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHubを登録して`
  - `请在医院复查に中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHubの通知を入れて`
  - `请在医院复查に中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHubことを忘れないよう知らせて`
  - `请在医院复查の時刻で中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHubをリマインドして`
  - `请在医院复查に私へ中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHubと伝えて`
  - `请在医院复查用に中记录：爸爸4月18日上午9点心内科复查，提醒方式HomeHubの通知を作って`

### S3-44 医院复查提醒 输出查询

- Query: `查看医院复查提醒有哪些记录`
- Expected: 返回 医院复查提醒 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `查看医院复查提醒我有哪些记录`
  - `帮我设置一个提醒，查看医院复查有哪些记录`
  - `请在查看医院复查提醒我去有哪些记录`
  - `到查看医院复查记得提醒我有哪些记录`
  - `我想在查看医院复查收到提醒：有哪些记录`
  - `请给我设一个查看医院复查的提醒，内容是有哪些记录`
  - `查看医院复查帮我提醒一下有哪些记录`
  - `记得在查看医院复查提醒我有哪些记录`
  - `请添加提醒：查看医院复查有哪些记录`
  - `到查看医院复查通知我有哪些记录`

- English Variants: 10
  - `Remind me 查看医院复查 to 有哪些记录.`
  - `Set a reminder 查看医院复查 for me to 有哪些记录.`
  - `Please remind me 查看医院复查 that I need to 有哪些记录.`
  - `Can you create a reminder 查看医院复查 for 有哪些记录?`
  - `I need a reminder 查看医院复查 to 有哪些记录.`
  - `Put in a reminder for 查看医院复查: 有哪些记录.`
  - `Schedule a reminder 查看医院复查 so I remember to 有哪些记录.`
  - `Please alert me 查看医院复查 to 有哪些记录.`
  - `Set me a 查看医院复查 reminder to 有哪些记录.`
  - `Create a reminder telling me 查看医院复查 to 有哪些记录.`

- Japanese Variants: 10
  - `查看医院复查に有哪些记录とリマインドして`
  - `查看医院复查に有哪些记录ことを知らせて`
  - `查看医院复查用に「有哪些记录」のリマインダーを設定して`
  - `查看医院复查になったら有哪些记录と通知して`
  - `查看医院复查のリマインダーとして有哪些记录を登録して`
  - `查看医院复查に有哪些记录の通知を入れて`
  - `查看医院复查に有哪些记录ことを忘れないよう知らせて`
  - `查看医院复查の時刻で有哪些记录をリマインドして`
  - `查看医院复查に私へ有哪些记录と伝えて`
  - `查看医院复查用に有哪些记录の通知を作って`

### S3-45 医院复查提醒 输出导出

- Query: `导出医院复查提醒文档`
- Expected: 导出 医院复查提醒 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `导出医院复查提醒我文档`
  - `帮我设置一个提醒，导出医院复查文档`
  - `请在导出医院复查提醒我去文档`
  - `到导出医院复查记得提醒我文档`
  - `我想在导出医院复查收到提醒：文档`
  - `请给我设一个导出医院复查的提醒，内容是文档`
  - `导出医院复查帮我提醒一下文档`
  - `记得在导出医院复查提醒我文档`
  - `请添加提醒：导出医院复查文档`
  - `到导出医院复查通知我文档`

- English Variants: 10
  - `Remind me 导出医院复查 to 文档.`
  - `Set a reminder 导出医院复查 for me to 文档.`
  - `Please remind me 导出医院复查 that I need to 文档.`
  - `Can you create a reminder 导出医院复查 for 文档?`
  - `I need a reminder 导出医院复查 to 文档.`
  - `Put in a reminder for 导出医院复查: 文档.`
  - `Schedule a reminder 导出医院复查 so I remember to 文档.`
  - `Please alert me 导出医院复查 to 文档.`
  - `Set me a 导出医院复查 reminder to 文档.`
  - `Create a reminder telling me 导出医院复查 to 文档.`

- Japanese Variants: 10
  - `导出医院复查に文档とリマインドして`
  - `导出医院复查に文档ことを知らせて`
  - `导出医院复查用に「文档」のリマインダーを設定して`
  - `导出医院复查になったら文档と通知して`
  - `导出医院复查のリマインダーとして文档を登録して`
  - `导出医院复查に文档の通知を入れて`
  - `导出医院复查に文档ことを忘れないよう知らせて`
  - `导出医院复查の時刻で文档をリマインドして`
  - `导出医院复查に私へ文档と伝えて`
  - `导出医院复查用に文档の通知を作って`

### S3-46 孩子学习计划 输入记录

- Query: `请在孩子学习计划中记录：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
- Expected: 将阶段3输入写入 孩子学习计划，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

- Chinese Variants: 10
  - `请在孩子学习计划中新增记录：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `帮我把这条内容记到孩子学习计划里：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `把以下信息记录到孩子学习计划：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `请将小明今天完成数学口算20题和英语单词复习，老师反馈良好录入到孩子学习计划`
  - `在孩子学习计划里添加这条记录：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `帮我往孩子学习计划中写入：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `请保存到孩子学习计划：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `将这条信息登记到孩子学习计划：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `请在孩子学习计划里面记录下：小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `把小明今天完成数学口算20题和英语单词复习，老师反馈良好这条内容存到孩子学习计划`

- English Variants: 10
  - `Please add this record to 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `Record the following in 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `Can you save this entry in 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `Log this information under 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `Please create a new record in 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `Put this into 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `Add this content to 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `Save the following note in 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `Enter this record for 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `Please store this in 孩子学习计划: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`

- Japanese Variants: 10
  - `孩子学习计划 に次の内容を記録して: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `孩子学习计划 へこの情報を追加して: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `孩子学习计划 にこの記録を保存して: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `孩子学习计划 に 小明今天完成数学口算20题和英语单词复习，老师反馈良好 を登録して`
  - `孩子学习计划 の記録として 小明今天完成数学口算20题和英语单词复习，老师反馈良好 を入れて`
  - `孩子学习计划 に以下を記録してください: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `孩子学习计划 へこの内容を書き込んで: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `孩子学习计划 に新しい記録を追加: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`
  - `小明今天完成数学口算20题和英语单词复习，老师反馈良好 を 孩子学习计划 に保存して`
  - `孩子学习计划 にこの内容を残して: 小明今天完成数学口算20题和英语单词复习，老师反馈良好`

### S3-47 孩子学习计划 输出查询

- Query: `查看孩子学习计划有哪些记录`
- Expected: 返回 孩子学习计划 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `查看孩子学习计划里的记录`
  - `帮我列出孩子学习计划有哪些记录`
  - `孩子学习计划目前都记录了什么`
  - `请显示孩子学习计划的全部记录`
  - `我想看一下孩子学习计划里的内容`
  - `把孩子学习计划的记录给我看看`
  - `查看一下孩子学习计划都有哪些条目`
  - `帮我打开孩子学习计划记录`
  - `列出孩子学习计划目前的记录`
  - `请展示孩子学习计划中的所有记录`

- English Variants: 10
  - `Show me the records in 孩子学习计划.`
  - `What records are in 孩子学习计划?`
  - `Please list the entries under 孩子学习计划.`
  - `Can you display all records in 孩子学习计划?`
  - `I want to check the records for 孩子学习计划.`
  - `Let me see what has been recorded in 孩子学习计划.`
  - `Please open 孩子学习计划 and show the entries.`
  - `List everything recorded in 孩子学习计划.`
  - `Could you pull up the records from 孩子学习计划?`
  - `Show all entries stored in 孩子学习计划.`

- Japanese Variants: 10
  - `孩子学习计划 の記録を見せて`
  - `孩子学习计划 にある記録一覧を表示して`
  - `孩子学习计划 の登録内容を確認したい`
  - `孩子学习计划 の記録を全部見たい`
  - `孩子学习计划 に入っている情報を見せて`
  - `孩子学习计划 の内容を一覧表示して`
  - `孩子学习计划 の記録を教えて`
  - `孩子学习计划 のエントリーを確認して`
  - `孩子学习计划 の登録データを開いて`
  - `孩子学习计划 に何が記録されているか見せて`

### S3-48 孩子学习计划 输出导出

- Query: `导出孩子学习计划表格`
- Expected: 导出 孩子学习计划 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `导出孩子学习计划`
  - `把孩子学习计划导出来`
  - `请帮我导出孩子学习计划`
  - `生成孩子学习计划的导出文件`
  - `我想导出孩子学习计划的数据`
  - `请把孩子学习计划内容输出成文件`
  - `帮我准备孩子学习计划的导出结果`
  - `导出一下孩子学习计划相关内容`
  - `请生成孩子学习计划的可导出文件`
  - `把孩子学习计划做成导出文档`

- English Variants: 10
  - `Export 孩子学习计划.`
  - `Please export 孩子学习计划.`
  - `I need an export of 孩子学习计划.`
  - `Can you export the table for 孩子学习计划?`
  - `Generate an export for 孩子学习计划.`
  - `Please create an export file for 孩子学习计划.`
  - `Export the data from 孩子学习计划.`
  - `Could you prepare an export for 孩子学习计划?`
  - `I want to download the exported table for 孩子学习计划.`
  - `Please output 孩子学习计划 as an export file.`

- Japanese Variants: 10
  - `孩子学习计划 をエクスポートして`
  - `孩子学习计划 のデータを出力して`
  - `孩子学习计划 を書き出してください`
  - `孩子学习计划 の内容をエクスポートしたい`
  - `孩子学习计划 のエクスポートファイルを作って`
  - `孩子学习计划 を外部出力して`
  - `孩子学习计划 の記録をファイルで出して`
  - `孩子学习计划 のデータを出力形式にして`
  - `孩子学习计划 をダウンロードできる形で出して`
  - `孩子学习计划 のエクスポートを準備して`

### S3-49 家庭活动安排 输入记录

- Query: `请在家庭活动安排中记录：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
- Expected: 将阶段3输入写入 家庭活动安排，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

- Chinese Variants: 10
  - `请在家庭活动安排中新增记录：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `帮我把这条内容记到家庭活动安排里：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `把以下信息记录到家庭活动安排：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `请将周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶录入到家庭活动安排`
  - `在家庭活动安排里添加这条记录：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `帮我往家庭活动安排中写入：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `请保存到家庭活动安排：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `将这条信息登记到家庭活动安排：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `请在家庭活动安排里面记录下：周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `把周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶这条内容存到家庭活动安排`

- English Variants: 10
  - `Please add this record to 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `Record the following in 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `Can you save this entry in 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `Log this information under 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `Please create a new record in 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `Put this into 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `Add this content to 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `Save the following note in 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `Enter this record for 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `Please store this in 家庭活动安排: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`

- Japanese Variants: 10
  - `家庭活动安排 に次の内容を記録して: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `家庭活动安排 へこの情報を追加して: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `家庭活动安排 にこの記録を保存して: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `家庭活动安排 に 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶 を登録して`
  - `家庭活动安排 の記録として 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶 を入れて`
  - `家庭活动安排 に以下を記録してください: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `家庭活动安排 へこの内容を書き込んで: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `家庭活动安排 に新しい記録を追加: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`
  - `周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶 を 家庭活动安排 に保存して`
  - `家庭活动安排 にこの内容を残して: 周日去上野公园野餐，参加成员爸爸妈妈和小明，注意带水壶`

### S3-50 家庭活动安排 输出查询

- Query: `查看家庭活动安排有哪些记录`
- Expected: 返回 家庭活动安排 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `查看家庭活动安排里的记录`
  - `帮我列出家庭活动安排有哪些记录`
  - `家庭活动安排目前都记录了什么`
  - `请显示家庭活动安排的全部记录`
  - `我想看一下家庭活动安排里的内容`
  - `把家庭活动安排的记录给我看看`
  - `查看一下家庭活动安排都有哪些条目`
  - `帮我打开家庭活动安排记录`
  - `列出家庭活动安排目前的记录`
  - `请展示家庭活动安排中的所有记录`

- English Variants: 10
  - `Show me the records in 家庭活动安排.`
  - `What records are in 家庭活动安排?`
  - `Please list the entries under 家庭活动安排.`
  - `Can you display all records in 家庭活动安排?`
  - `I want to check the records for 家庭活动安排.`
  - `Let me see what has been recorded in 家庭活动安排.`
  - `Please open 家庭活动安排 and show the entries.`
  - `List everything recorded in 家庭活动安排.`
  - `Could you pull up the records from 家庭活动安排?`
  - `Show all entries stored in 家庭活动安排.`

- Japanese Variants: 10
  - `家庭活动安排 の記録を見せて`
  - `家庭活动安排 にある記録一覧を表示して`
  - `家庭活动安排 の登録内容を確認したい`
  - `家庭活动安排 の記録を全部見たい`
  - `家庭活动安排 に入っている情報を見せて`
  - `家庭活动安排 の内容を一覧表示して`
  - `家庭活动安排 の記録を教えて`
  - `家庭活动安排 のエントリーを確認して`
  - `家庭活动安排 の登録データを開いて`
  - `家庭活动安排 に何が記録されているか見せて`

### S3-51 家庭活动安排 输出导出

- Query: `导出家庭活动安排文档`
- Expected: 导出 家庭活动安排 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `导出家庭活动安排`
  - `把家庭活动安排导出来`
  - `请帮我导出家庭活动安排`
  - `生成家庭活动安排的导出文件`
  - `我想导出家庭活动安排的数据`
  - `请把家庭活动安排内容输出成文件`
  - `帮我准备家庭活动安排的导出结果`
  - `导出一下家庭活动安排相关内容`
  - `请生成家庭活动安排的可导出文件`
  - `把家庭活动安排做成导出文档`

- English Variants: 10
  - `Export 家庭活动安排.`
  - `Please export 家庭活动安排.`
  - `I need an export of 家庭活动安排.`
  - `Can you export the document for 家庭活动安排?`
  - `Generate an export for 家庭活动安排.`
  - `Please create an export file for 家庭活动安排.`
  - `Export the data from 家庭活动安排.`
  - `Could you prepare an export for 家庭活动安排?`
  - `I want to download the exported document for 家庭活动安排.`
  - `Please output 家庭活动安排 as an export file.`

- Japanese Variants: 10
  - `家庭活动安排 をエクスポートして`
  - `家庭活动安排 のデータを出力して`
  - `家庭活动安排 を書き出してください`
  - `家庭活动安排 の内容をエクスポートしたい`
  - `家庭活动安排 のエクスポートファイルを作って`
  - `家庭活动安排 を外部出力して`
  - `家庭活动安排 の記録をファイルで出して`
  - `家庭活动安排 のデータを出力形式にして`
  - `家庭活动安排 をダウンロードできる形で出して`
  - `家庭活动安排 のエクスポートを準備して`

### S3-52 家庭日程安排 输入记录

- Query: `请在家庭日程安排中记录：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
- Expected: 将阶段3输入写入 家庭日程安排，形成对应输出。
- Reset Before: Yes
- Setup Queries: 3

- Chinese Variants: 10
  - `请在家庭日程安排中新增记录：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `帮我把这条内容记到家庭日程安排里：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `把以下信息记录到家庭日程安排：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `请将周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物录入到家庭日程安排`
  - `在家庭日程安排里添加这条记录：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `帮我往家庭日程安排中写入：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `请保存到家庭日程安排：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `将这条信息登记到家庭日程安排：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `请在家庭日程安排里面记录下：周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `把周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物这条内容存到家庭日程安排`

- English Variants: 10
  - `Please add this record to 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `Record the following in 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `Can you save this entry in 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `Log this information under 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `Please create a new record in 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `Put this into 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `Add this content to 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `Save the following note in 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `Enter this record for 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `Please store this in 家庭日程安排: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`

- Japanese Variants: 10
  - `家庭日程安排 に次の内容を記録して: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `家庭日程安排 へこの情報を追加して: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `家庭日程安排 にこの記録を保存して: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `家庭日程安排 に 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物 を登録して`
  - `家庭日程安排 の記録として 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物 を入れて`
  - `家庭日程安排 に以下を記録してください: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `家庭日程安排 へこの内容を書き込んで: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `家庭日程安排 に新しい記録を追加: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`
  - `周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物 を 家庭日程安排 に保存して`
  - `家庭日程安排 にこの内容を残して: 周六下午2点家庭聚会在奶奶家，参加成员全家，注意带礼物`

### S3-53 家庭日程安排 输出查询

- Query: `查看家庭日程安排有哪些记录`
- Expected: 返回 家庭日程安排 当前记录输出。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `查看家庭日程安排里的记录`
  - `帮我列出家庭日程安排有哪些记录`
  - `家庭日程安排目前都记录了什么`
  - `请显示家庭日程安排的全部记录`
  - `我想看一下家庭日程安排里的内容`
  - `把家庭日程安排的记录给我看看`
  - `查看一下家庭日程安排都有哪些条目`
  - `帮我打开家庭日程安排记录`
  - `列出家庭日程安排目前的记录`
  - `请展示家庭日程安排中的所有记录`

- English Variants: 10
  - `Show me the records in 家庭日程安排.`
  - `What records are in 家庭日程安排?`
  - `Please list the entries under 家庭日程安排.`
  - `Can you display all records in 家庭日程安排?`
  - `I want to check the records for 家庭日程安排.`
  - `Let me see what has been recorded in 家庭日程安排.`
  - `Please open 家庭日程安排 and show the entries.`
  - `List everything recorded in 家庭日程安排.`
  - `Could you pull up the records from 家庭日程安排?`
  - `Show all entries stored in 家庭日程安排.`

- Japanese Variants: 10
  - `家庭日程安排 の記録を見せて`
  - `家庭日程安排 にある記録一覧を表示して`
  - `家庭日程安排 の登録内容を確認したい`
  - `家庭日程安排 の記録を全部見たい`
  - `家庭日程安排 に入っている情報を見せて`
  - `家庭日程安排 の内容を一覧表示して`
  - `家庭日程安排 の記録を教えて`
  - `家庭日程安排 のエントリーを確認して`
  - `家庭日程安排 の登録データを開いて`
  - `家庭日程安排 に何が記録されているか見せて`

### S3-54 家庭日程安排 输出导出

- Query: `导出家庭日程安排文档`
- Expected: 导出 家庭日程安排 的阶段3输出产物。
- Reset Before: Yes
- Setup Queries: 4

- Chinese Variants: 10
  - `导出家庭日程安排`
  - `把家庭日程安排导出来`
  - `请帮我导出家庭日程安排`
  - `生成家庭日程安排的导出文件`
  - `我想导出家庭日程安排的数据`
  - `请把家庭日程安排内容输出成文件`
  - `帮我准备家庭日程安排的导出结果`
  - `导出一下家庭日程安排相关内容`
  - `请生成家庭日程安排的可导出文件`
  - `把家庭日程安排做成导出文档`

- English Variants: 10
  - `Export 家庭日程安排.`
  - `Please export 家庭日程安排.`
  - `I need an export of 家庭日程安排.`
  - `Can you export the document for 家庭日程安排?`
  - `Generate an export for 家庭日程安排.`
  - `Please create an export file for 家庭日程安排.`
  - `Export the data from 家庭日程安排.`
  - `Could you prepare an export for 家庭日程安排?`
  - `I want to download the exported document for 家庭日程安排.`
  - `Please output 家庭日程安排 as an export file.`

- Japanese Variants: 10
  - `家庭日程安排 をエクスポートして`
  - `家庭日程安排 のデータを出力して`
  - `家庭日程安排 を書き出してください`
  - `家庭日程安排 の内容をエクスポートしたい`
  - `家庭日程安排 のエクスポートファイルを作って`
  - `家庭日程安排 を外部出力して`
  - `家庭日程安排 の記録をファイルで出して`
  - `家庭日程安排 のデータを出力形式にして`
  - `家庭日程安排 をダウンロードできる形で出して`
  - `家庭日程安排 のエクスポートを準備して`

### S3-55 联合执行 账单与提醒阈值联动

- Query: `到今天为止消费总额是多少，如果超出2000日元产生提醒，并把提醒发送到 homehub`
- Expected: 家庭账单与家庭提醒智能体联合执行，输出总额并触发提醒联动。
- Reset Before: Yes
- Setup Queries: 9

- Chinese Variants: 10
  - `到今天为止消费总额是多少，如果超出2000日元产生提醒我，并把提醒发送到 homehub`
  - `帮我设置一个提醒，到今天为止消费总额是多少，如果超出2000日元产生，并把提醒发送到 homehub`
  - `请在到今天为止消费总额是多少，如果超出2000日元产生提醒我去，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超出2000日元产生记得提醒我，并把提醒发送到 homehub`
  - `我想在到今天为止消费总额是多少，如果超出2000日元产生收到提醒：，并把提醒发送到 homehub`
  - `请给我设一个到今天为止消费总额是多少，如果超出2000日元产生的提醒，内容是，并把提醒发送到 homehub`
  - `到今天为止消费总额是多少，如果超出2000日元产生帮我提醒一下，并把提醒发送到 homehub`
  - `记得在到今天为止消费总额是多少，如果超出2000日元产生提醒我，并把提醒发送到 homehub`
  - `请添加提醒：到今天为止消费总额是多少，如果超出2000日元产生，并把提醒发送到 homehub`
  - `到到今天为止消费总额是多少，如果超出2000日元产生通知我，并把提醒发送到 homehub`

- English Variants: 10
  - `Remind me 到今天为止消费总额是多少，如果超出2000日元产生 to ，并把提醒发送到 homehub.`
  - `Set a reminder 到今天为止消费总额是多少，如果超出2000日元产生 for me to ，并把提醒发送到 homehub.`
  - `Please remind me 到今天为止消费总额是多少，如果超出2000日元产生 that I need to ，并把提醒发送到 homehub.`
  - `Can you create a reminder 到今天为止消费总额是多少，如果超出2000日元产生 for ，并把提醒发送到 homehub?`
  - `I need a reminder 到今天为止消费总额是多少，如果超出2000日元产生 to ，并把提醒发送到 homehub.`
  - `Put in a reminder for 到今天为止消费总额是多少，如果超出2000日元产生: ，并把提醒发送到 homehub.`
  - `Schedule a reminder 到今天为止消费总额是多少，如果超出2000日元产生 so I remember to ，并把提醒发送到 homehub.`
  - `Please alert me 到今天为止消费总额是多少，如果超出2000日元产生 to ，并把提醒发送到 homehub.`
  - `Set me a 到今天为止消费总额是多少，如果超出2000日元产生 reminder to ，并把提醒发送到 homehub.`
  - `Create a reminder telling me 到今天为止消费总额是多少，如果超出2000日元产生 to ，并把提醒发送到 homehub.`

- Japanese Variants: 10
  - `到今天为止消费总额是多少，如果超出2000日元产生に，并把提醒发送到 homehubとリマインドして`
  - `到今天为止消费总额是多少，如果超出2000日元产生に，并把提醒发送到 homehubことを知らせて`
  - `到今天为止消费总额是多少，如果超出2000日元产生用に「，并把提醒发送到 homehub」のリマインダーを設定して`
  - `到今天为止消费总额是多少，如果超出2000日元产生になったら，并把提醒发送到 homehubと通知して`
  - `到今天为止消费总额是多少，如果超出2000日元产生のリマインダーとして，并把提醒发送到 homehubを登録して`
  - `到今天为止消费总额是多少，如果超出2000日元产生に，并把提醒发送到 homehubの通知を入れて`
  - `到今天为止消费总额是多少，如果超出2000日元产生に，并把提醒发送到 homehubことを忘れないよう知らせて`
  - `到今天为止消费总额是多少，如果超出2000日元产生の時刻で，并把提醒发送到 homehubをリマインドして`
  - `到今天为止消费总额是多少，如果超出2000日元产生に私へ，并把提醒发送到 homehubと伝えて`
  - `到今天为止消费总额是多少，如果超出2000日元产生用に，并把提醒发送到 homehubの通知を作って`

### S3-56 联合执行 健康与体检双记录

- Query: `查看体检报告有哪些记录`
- Expected: 身体状况记录与体检报告智能体在同一家庭场景下连续执行，输出体检记录。
- Reset Before: Yes
- Setup Queries: 8

- Chinese Variants: 10
  - `查看体检报告里的记录`
  - `帮我列出体检报告有哪些记录`
  - `体检报告目前都记录了什么`
  - `请显示体检报告的全部记录`
  - `我想看一下体检报告里的内容`
  - `把体检报告的记录给我看看`
  - `查看一下体检报告都有哪些条目`
  - `帮我打开体检报告记录`
  - `列出体检报告目前的记录`
  - `请展示体检报告中的所有记录`

- English Variants: 10
  - `Show me the records in 体检报告.`
  - `What records are in 体检报告?`
  - `Please list the entries under 体检报告.`
  - `Can you display all records in 体检报告?`
  - `I want to check the records for 体检报告.`
  - `Let me see what has been recorded in 体检报告.`
  - `Please open 体检报告 and show the entries.`
  - `List everything recorded in 体检报告.`
  - `Could you pull up the records from 体检报告?`
  - `Show all entries stored in 体检报告.`

- Japanese Variants: 10
  - `体检报告 の記録を見せて`
  - `体检报告 にある記録一覧を表示して`
  - `体检报告 の登録内容を確認したい`
  - `体检报告 の記録を全部見たい`
  - `体检报告 に入っている情報を見せて`
  - `体检报告 の内容を一覧表示して`
  - `体检报告 の記録を教えて`
  - `体检报告 のエントリーを確認して`
  - `体检报告 の登録データを開いて`
  - `体检报告 に何が記録されているか見せて`

### S3-57 联合执行 学习与活动双场景

- Query: `导出孩子学习计划表格`
- Expected: 孩子学习计划与家庭活动安排在同一家庭周末场景下联合执行，输出学习表格。
- Reset Before: Yes
- Setup Queries: 8

- Chinese Variants: 10
  - `导出孩子学习计划`
  - `把孩子学习计划导出来`
  - `请帮我导出孩子学习计划`
  - `生成孩子学习计划的导出文件`
  - `我想导出孩子学习计划的数据`
  - `请把孩子学习计划内容输出成文件`
  - `帮我准备孩子学习计划的导出结果`
  - `导出一下孩子学习计划相关内容`
  - `请生成孩子学习计划的可导出文件`
  - `把孩子学习计划做成导出文档`

- English Variants: 10
  - `Export 孩子学习计划.`
  - `Please export 孩子学习计划.`
  - `I need an export of 孩子学习计划.`
  - `Can you export the table for 孩子学习计划?`
  - `Generate an export for 孩子学习计划.`
  - `Please create an export file for 孩子学习计划.`
  - `Export the data from 孩子学习计划.`
  - `Could you prepare an export for 孩子学习计划?`
  - `I want to download the exported table for 孩子学习计划.`
  - `Please output 孩子学习计划 as an export file.`

- Japanese Variants: 10
  - `孩子学习计划 をエクスポートして`
  - `孩子学习计划 のデータを出力して`
  - `孩子学习计划 を書き出してください`
  - `孩子学习计划 の内容をエクスポートしたい`
  - `孩子学习计划 のエクスポートファイルを作って`
  - `孩子学习计划 を外部出力して`
  - `孩子学习计划 の記録をファイルで出して`
  - `孩子学习计划 のデータを出力形式にして`
  - `孩子学习计划 をダウンロードできる形で出して`
  - `孩子学习计划 のエクスポートを準備して`

## 扩展

### EXT-01 ext-school 分类

- Query: `将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/ext-school 下的文件，进行分类。类型创建新的文件夹`

### EXT-02 ext-bills 分类

- Query: `将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/ext-bills 下的文件，进行分类。类型创建新的文件夹`

### EXT-03 ext-photos 分类

- Query: `将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/ext-photos 下的文件，进行分类。类型创建新的文件夹`

### EXT-04 ext-recipes 分类

- Query: `将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/ext-recipes 下的文件，进行分类。类型创建新的文件夹`

### EXT-05 ext-mixed 分类

- Query: `将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/ext-mixed 下的文件，进行分类。类型创建新的文件夹`

### EXT-06 ext-visitors 分类

- Query: `将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/ext-visitors 下的文件，进行分类。类型创建新的文件夹`

### EXT-07 ext-pet 分类

- Query: `将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/ext-pet 下的文件，进行分类。类型创建新的文件夹`

### EXT-08 ext-health 分类

- Query: `将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 按类型创建文件夹并分类。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /tmp/homehub-family-suite/ext-health 下的文件，进行分类。类型创建新的文件夹`

### EXT-09 扩展读取账单备注

- Query: `读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `读取一下 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `帮我打开并读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `看一下 /tmp/homehub-family-suite/family-reading/shopping-note.txt 里的内容`
  - `请读取文件 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `我想查看 /tmp/homehub-family-suite/family-reading/shopping-note.txt 的内容`
  - `打开 /tmp/homehub-family-suite/family-reading/shopping-note.txt 给我看看`
  - `帮我读一下 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `请展示 /tmp/homehub-family-suite/family-reading/shopping-note.txt 里的内容`
  - `查看并读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt`
  - `把 /tmp/homehub-family-suite/family-reading/shopping-note.txt 打开读给我看`

- English Variants: 10
  - `Read /tmp/homehub-family-suite/family-reading/shopping-note.txt.`
  - `Please open and read /tmp/homehub-family-suite/family-reading/shopping-note.txt.`
  - `Show me the contents of /tmp/homehub-family-suite/family-reading/shopping-note.txt.`
  - `Can you read the file /tmp/homehub-family-suite/family-reading/shopping-note.txt?`
  - `I want to see what's inside /tmp/homehub-family-suite/family-reading/shopping-note.txt.`
  - `Please open /tmp/homehub-family-suite/family-reading/shopping-note.txt and tell me what's in it.`
  - `Check the contents of /tmp/homehub-family-suite/family-reading/shopping-note.txt for me.`
  - `Read through /tmp/homehub-family-suite/family-reading/shopping-note.txt and show it to me.`
  - `Could you display the contents of /tmp/homehub-family-suite/family-reading/shopping-note.txt?`
  - `Take a look at /tmp/homehub-family-suite/family-reading/shopping-note.txt and read it out.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読んで`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を開いて内容を見せて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の中身を確認して`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読み取ってください`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の内容を表示して`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を開いて読んでほしい`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のファイル内容を教えて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を確認して内容を見せて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読んで内容を共有して`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の中身を表示してください`

### EXT-10 扩展读取菜单

- Query: `读取 /tmp/homehub-family-suite/family-library/meal-plan.md`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `读取一下 /tmp/homehub-family-suite/family-library/meal-plan.md`
  - `帮我打开并读取 /tmp/homehub-family-suite/family-library/meal-plan.md`
  - `看一下 /tmp/homehub-family-suite/family-library/meal-plan.md 里的内容`
  - `请读取文件 /tmp/homehub-family-suite/family-library/meal-plan.md`
  - `我想查看 /tmp/homehub-family-suite/family-library/meal-plan.md 的内容`
  - `打开 /tmp/homehub-family-suite/family-library/meal-plan.md 给我看看`
  - `帮我读一下 /tmp/homehub-family-suite/family-library/meal-plan.md`
  - `请展示 /tmp/homehub-family-suite/family-library/meal-plan.md 里的内容`
  - `查看并读取 /tmp/homehub-family-suite/family-library/meal-plan.md`
  - `把 /tmp/homehub-family-suite/family-library/meal-plan.md 打开读给我看`

- English Variants: 10
  - `Read /tmp/homehub-family-suite/family-library/meal-plan.md.`
  - `Please open and read /tmp/homehub-family-suite/family-library/meal-plan.md.`
  - `Show me the contents of /tmp/homehub-family-suite/family-library/meal-plan.md.`
  - `Can you read the file /tmp/homehub-family-suite/family-library/meal-plan.md?`
  - `I want to see what's inside /tmp/homehub-family-suite/family-library/meal-plan.md.`
  - `Please open /tmp/homehub-family-suite/family-library/meal-plan.md and tell me what's in it.`
  - `Check the contents of /tmp/homehub-family-suite/family-library/meal-plan.md for me.`
  - `Read through /tmp/homehub-family-suite/family-library/meal-plan.md and show it to me.`
  - `Could you display the contents of /tmp/homehub-family-suite/family-library/meal-plan.md?`
  - `Take a look at /tmp/homehub-family-suite/family-library/meal-plan.md and read it out.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を読んで`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を開いて内容を見せて`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md の中身を確認して`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を読み取ってください`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md の内容を表示して`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を開いて読んでほしい`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md のファイル内容を教えて`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を確認して内容を見せて`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を読んで内容を共有して`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md の中身を表示してください`

### EXT-11 扩展读取 JSON

- Query: `读取 /tmp/homehub-family-suite/family-reading/recipe.json`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `读取一下 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `帮我打开并读取 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `看一下 /tmp/homehub-family-suite/family-reading/recipe.json 里的内容`
  - `请读取文件 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `我想查看 /tmp/homehub-family-suite/family-reading/recipe.json 的内容`
  - `打开 /tmp/homehub-family-suite/family-reading/recipe.json 给我看看`
  - `帮我读一下 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `请展示 /tmp/homehub-family-suite/family-reading/recipe.json 里的内容`
  - `查看并读取 /tmp/homehub-family-suite/family-reading/recipe.json`
  - `把 /tmp/homehub-family-suite/family-reading/recipe.json 打开读给我看`

- English Variants: 10
  - `Read /tmp/homehub-family-suite/family-reading/recipe.json.`
  - `Please open and read /tmp/homehub-family-suite/family-reading/recipe.json.`
  - `Show me the contents of /tmp/homehub-family-suite/family-reading/recipe.json.`
  - `Can you read the file /tmp/homehub-family-suite/family-reading/recipe.json?`
  - `I want to see what's inside /tmp/homehub-family-suite/family-reading/recipe.json.`
  - `Please open /tmp/homehub-family-suite/family-reading/recipe.json and tell me what's in it.`
  - `Check the contents of /tmp/homehub-family-suite/family-reading/recipe.json for me.`
  - `Read through /tmp/homehub-family-suite/family-reading/recipe.json and show it to me.`
  - `Could you display the contents of /tmp/homehub-family-suite/family-reading/recipe.json?`
  - `Take a look at /tmp/homehub-family-suite/family-reading/recipe.json and read it out.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読んで`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を開いて内容を見せて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の中身を確認して`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読み取ってください`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の内容を表示して`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を開いて読んでほしい`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のファイル内容を教えて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を確認して内容を見せて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読んで内容を共有して`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の中身を表示してください`

### EXT-12 扩展发送收据

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，receipt.pdf 文件发给我。`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `看看 /tmp/homehub-family-suite/family-inbox 里有什么文件，再把 receipt.pdf 发给我`
  - `帮我列出 /tmp/homehub-family-suite/family-inbox 下面的文件，并把 receipt.pdf 传给我`
  - `查看一下 /tmp/homehub-family-suite/family-inbox 的文件列表，然后把 receipt.pdf 给我`
  - `请检查 /tmp/homehub-family-suite/family-inbox 里有哪些文件，顺便发送 receipt.pdf`
  - `我想看 /tmp/homehub-family-suite/family-inbox 下的文件，同时把 receipt.pdf 发我`
  - `打开 /tmp/homehub-family-suite/family-inbox 看看文件情况，再把 receipt.pdf 发过来`
  - `帮我确认 /tmp/homehub-family-suite/family-inbox 里有哪些内容，并发送文件 receipt.pdf`
  - `列一下 /tmp/homehub-family-suite/family-inbox 里的文件，再把 receipt.pdf 共享给我`
  - `看一下 /tmp/homehub-family-suite/family-inbox，并把其中的 receipt.pdf 发给我`
  - `请先查看 /tmp/homehub-family-suite/family-inbox 下的文件，再发送 receipt.pdf`

- English Variants: 10
  - `Show me the files in /tmp/homehub-family-suite/family-inbox, and send me receipt.pdf.`
  - `List the files under /tmp/homehub-family-suite/family-inbox, then send over receipt.pdf.`
  - `What's inside /tmp/homehub-family-suite/family-inbox? Please send me receipt.pdf.`
  - `Can you check /tmp/homehub-family-suite/family-inbox and share receipt.pdf with me?`
  - `Please look in /tmp/homehub-family-suite/family-inbox, list the files, and send receipt.pdf.`
  - `I want to see the files in /tmp/homehub-family-suite/family-inbox; also send me receipt.pdf.`
  - `Open /tmp/homehub-family-suite/family-inbox, tell me what files are there, and send receipt.pdf.`
  - `Check the contents of /tmp/homehub-family-suite/family-inbox and forward receipt.pdf to me.`
  - `Could you list the files in /tmp/homehub-family-suite/family-inbox and send me receipt.pdf?`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and share the file receipt.pdf.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて、そのあと receipt.pdf を送って`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を出して、receipt.pdf を送ってください`
  - `/tmp/homehub-family-suite/family-inbox に何があるか確認して、receipt.pdf を共有して`
  - `/tmp/homehub-family-suite/family-inbox の中身を見せてから receipt.pdf を送って`
  - `/tmp/homehub-family-suite/family-inbox を確認して、receipt.pdf を私に渡して`
  - `/tmp/homehub-family-suite/family-inbox のファイルを一覧表示して、receipt.pdf を送信して`
  - `/tmp/homehub-family-suite/family-inbox にあるものを教えて、receipt.pdf も送って`
  - `/tmp/homehub-family-suite/family-inbox を開いてファイルを確認し、receipt.pdf を送ってください`
  - `/tmp/homehub-family-suite/family-inbox の内容を見て、receipt.pdf を共有してください`
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを確認したうえで receipt.pdf を送って`

### EXT-13 扩展发送预算表

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，monthly_budget.xlsx 文件发给我。`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `看看 /tmp/homehub-family-suite/family-inbox 里有什么文件，再把 monthly_budget.xlsx 发给我`
  - `帮我列出 /tmp/homehub-family-suite/family-inbox 下面的文件，并把 monthly_budget.xlsx 传给我`
  - `查看一下 /tmp/homehub-family-suite/family-inbox 的文件列表，然后把 monthly_budget.xlsx 给我`
  - `请检查 /tmp/homehub-family-suite/family-inbox 里有哪些文件，顺便发送 monthly_budget.xlsx`
  - `我想看 /tmp/homehub-family-suite/family-inbox 下的文件，同时把 monthly_budget.xlsx 发我`
  - `打开 /tmp/homehub-family-suite/family-inbox 看看文件情况，再把 monthly_budget.xlsx 发过来`
  - `帮我确认 /tmp/homehub-family-suite/family-inbox 里有哪些内容，并发送文件 monthly_budget.xlsx`
  - `列一下 /tmp/homehub-family-suite/family-inbox 里的文件，再把 monthly_budget.xlsx 共享给我`
  - `看一下 /tmp/homehub-family-suite/family-inbox，并把其中的 monthly_budget.xlsx 发给我`
  - `请先查看 /tmp/homehub-family-suite/family-inbox 下的文件，再发送 monthly_budget.xlsx`

- English Variants: 10
  - `Show me the files in /tmp/homehub-family-suite/family-inbox, and send me monthly_budget.xlsx.`
  - `List the files under /tmp/homehub-family-suite/family-inbox, then send over monthly_budget.xlsx.`
  - `What's inside /tmp/homehub-family-suite/family-inbox? Please send me monthly_budget.xlsx.`
  - `Can you check /tmp/homehub-family-suite/family-inbox and share monthly_budget.xlsx with me?`
  - `Please look in /tmp/homehub-family-suite/family-inbox, list the files, and send monthly_budget.xlsx.`
  - `I want to see the files in /tmp/homehub-family-suite/family-inbox; also send me monthly_budget.xlsx.`
  - `Open /tmp/homehub-family-suite/family-inbox, tell me what files are there, and send monthly_budget.xlsx.`
  - `Check the contents of /tmp/homehub-family-suite/family-inbox and forward monthly_budget.xlsx to me.`
  - `Could you list the files in /tmp/homehub-family-suite/family-inbox and send me monthly_budget.xlsx?`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and share the file monthly_budget.xlsx.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて、そのあと monthly_budget.xlsx を送って`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を出して、monthly_budget.xlsx を送ってください`
  - `/tmp/homehub-family-suite/family-inbox に何があるか確認して、monthly_budget.xlsx を共有して`
  - `/tmp/homehub-family-suite/family-inbox の中身を見せてから monthly_budget.xlsx を送って`
  - `/tmp/homehub-family-suite/family-inbox を確認して、monthly_budget.xlsx を私に渡して`
  - `/tmp/homehub-family-suite/family-inbox のファイルを一覧表示して、monthly_budget.xlsx を送信して`
  - `/tmp/homehub-family-suite/family-inbox にあるものを教えて、monthly_budget.xlsx も送って`
  - `/tmp/homehub-family-suite/family-inbox を開いてファイルを確認し、monthly_budget.xlsx を送ってください`
  - `/tmp/homehub-family-suite/family-inbox の内容を見て、monthly_budget.xlsx を共有してください`
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを確認したうえで monthly_budget.xlsx を送って`

### EXT-14 扩展搜索菜谱

- Query: `搜索 /tmp/homehub-family-suite/family-library 下面的 meal 文件`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `搜索 /tmp/homehub-family-suite/family-library 下面和 meal 相关的文件`
  - `帮我在 /tmp/homehub-family-suite/family-library 里找 meal 文件`
  - `请查找 /tmp/homehub-family-suite/family-library 下包含 meal 的文件`
  - `看看 /tmp/homehub-family-suite/family-library 里面有没有 meal 相关文件`
  - `在 /tmp/homehub-family-suite/family-library 目录里搜索 meal`
  - `帮我检索 /tmp/homehub-family-suite/family-library 下的 meal 文件`
  - `请在 /tmp/homehub-family-suite/family-library 中查一下 meal 文件`
  - `找找 /tmp/homehub-family-suite/family-library 里面和 meal 有关的文件`
  - `查看 /tmp/homehub-family-suite/family-library 下是否有 meal 文件`
  - `在 /tmp/homehub-family-suite/family-library 里搜一下关键词 meal`

- English Variants: 10
  - `Search for files related to meal under /tmp/homehub-family-suite/family-library.`
  - `Find the meal files in /tmp/homehub-family-suite/family-library.`
  - `Please look through /tmp/homehub-family-suite/family-library for files matching meal.`
  - `Can you search /tmp/homehub-family-suite/family-library for any meal files?`
  - `Show me files about meal under /tmp/homehub-family-suite/family-library.`
  - `I need you to find meal-related files in /tmp/homehub-family-suite/family-library.`
  - `Please check /tmp/homehub-family-suite/family-library and search for meal files.`
  - `Look in /tmp/homehub-family-suite/family-library for anything named around meal.`
  - `Search the folder /tmp/homehub-family-suite/family-library for meal.`
  - `Could you find files connected to meal in /tmp/homehub-family-suite/family-library?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-library で meal に関連するファイルを探して`
  - `/tmp/homehub-family-suite/family-library 配下の meal ファイルを検索して`
  - `/tmp/homehub-family-suite/family-library の中から meal に関係するファイルを見つけて`
  - `/tmp/homehub-family-suite/family-library で meal を含むファイルを探して`
  - `/tmp/homehub-family-suite/family-library の meal 関連ファイルを見たい`
  - `/tmp/homehub-family-suite/family-library を検索して meal ファイルを見つけて`
  - `/tmp/homehub-family-suite/family-library にある meal ファイルを確認して`
  - `/tmp/homehub-family-suite/family-library の中で meal に近いファイルを探して`
  - `/tmp/homehub-family-suite/family-library から meal ファイルを見つけてください`
  - `/tmp/homehub-family-suite/family-library 内の meal に関するファイルを検索して`

### EXT-15 扩展搜索照片

- Query: `搜索 /tmp/homehub-family-suite/family-library 下面的 photo 文件`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `搜索 /tmp/homehub-family-suite/family-library 下面和 photo 相关的文件`
  - `帮我在 /tmp/homehub-family-suite/family-library 里找 photo 文件`
  - `请查找 /tmp/homehub-family-suite/family-library 下包含 photo 的文件`
  - `看看 /tmp/homehub-family-suite/family-library 里面有没有 photo 相关文件`
  - `在 /tmp/homehub-family-suite/family-library 目录里搜索 photo`
  - `帮我检索 /tmp/homehub-family-suite/family-library 下的 photo 文件`
  - `请在 /tmp/homehub-family-suite/family-library 中查一下 photo 文件`
  - `找找 /tmp/homehub-family-suite/family-library 里面和 photo 有关的文件`
  - `查看 /tmp/homehub-family-suite/family-library 下是否有 photo 文件`
  - `在 /tmp/homehub-family-suite/family-library 里搜一下关键词 photo`

- English Variants: 10
  - `Search for files related to photo under /tmp/homehub-family-suite/family-library.`
  - `Find the photo files in /tmp/homehub-family-suite/family-library.`
  - `Please look through /tmp/homehub-family-suite/family-library for files matching photo.`
  - `Can you search /tmp/homehub-family-suite/family-library for any photo files?`
  - `Show me files about photo under /tmp/homehub-family-suite/family-library.`
  - `I need you to find photo-related files in /tmp/homehub-family-suite/family-library.`
  - `Please check /tmp/homehub-family-suite/family-library and search for photo files.`
  - `Look in /tmp/homehub-family-suite/family-library for anything named around photo.`
  - `Search the folder /tmp/homehub-family-suite/family-library for photo.`
  - `Could you find files connected to photo in /tmp/homehub-family-suite/family-library?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-library で photo に関連するファイルを探して`
  - `/tmp/homehub-family-suite/family-library 配下の photo ファイルを検索して`
  - `/tmp/homehub-family-suite/family-library の中から photo に関係するファイルを見つけて`
  - `/tmp/homehub-family-suite/family-library で photo を含むファイルを探して`
  - `/tmp/homehub-family-suite/family-library の photo 関連ファイルを見たい`
  - `/tmp/homehub-family-suite/family-library を検索して photo ファイルを見つけて`
  - `/tmp/homehub-family-suite/family-library にある photo ファイルを確認して`
  - `/tmp/homehub-family-suite/family-library の中で photo に近いファイルを探して`
  - `/tmp/homehub-family-suite/family-library から photo ファイルを見つけてください`
  - `/tmp/homehub-family-suite/family-library 内の photo に関するファイルを検索して`

### EXT-16 扩展列出收件箱

- Query: `查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件`
- Expected: 完成扩展文件操作。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `查看 /tmp/homehub-family-suite/family-inbox 下面有哪些文件`
  - `帮我列出 /tmp/homehub-family-suite/family-inbox 下的文件`
  - `/tmp/homehub-family-suite/family-inbox 里都有什么文件`
  - `请看一下 /tmp/homehub-family-suite/family-inbox 的文件列表`
  - `我想知道 /tmp/homehub-family-suite/family-inbox 下面有哪些内容`
  - `打开 /tmp/homehub-family-suite/family-inbox 看看里面的文件`
  - `帮我确认 /tmp/homehub-family-suite/family-inbox 下都有哪些文件`
  - `列一下 /tmp/homehub-family-suite/family-inbox 里的文件`
  - `请检查 /tmp/homehub-family-suite/family-inbox 目录下的文件`
  - `看看 /tmp/homehub-family-suite/family-inbox 里面有什么`

- English Variants: 10
  - `Show me the files in /tmp/homehub-family-suite/family-inbox.`
  - `List the files under /tmp/homehub-family-suite/family-inbox.`
  - `What files are in /tmp/homehub-family-suite/family-inbox?`
  - `Can you check what files are inside /tmp/homehub-family-suite/family-inbox?`
  - `Please tell me what files are under /tmp/homehub-family-suite/family-inbox.`
  - `I want to see the contents of /tmp/homehub-family-suite/family-inbox.`
  - `Open /tmp/homehub-family-suite/family-inbox and list what's there.`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and show me the files.`
  - `Give me a file list for /tmp/homehub-family-suite/family-inbox.`
  - `Could you look in /tmp/homehub-family-suite/family-inbox and tell me what files are there?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて`
  - `/tmp/homehub-family-suite/family-inbox 配下のファイルを一覧にして`
  - `/tmp/homehub-family-suite/family-inbox の中に何のファイルがあるか教えて`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を確認したい`
  - `/tmp/homehub-family-suite/family-inbox の内容を見せてください`
  - `/tmp/homehub-family-suite/family-inbox に入っているファイルを表示して`
  - `/tmp/homehub-family-suite/family-inbox を開いて中身を確認して`
  - `/tmp/homehub-family-suite/family-inbox 配下のファイルを教えて`
  - `/tmp/homehub-family-suite/family-inbox に何があるかチェックして`
  - `/tmp/homehub-family-suite/family-inbox のファイル構成を見せて`

### EXT-17 家庭目录权限保护 1

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-18 家庭目录权限保护 2

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-19 家庭目录权限保护 3

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-20 家庭目录权限保护 4

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-21 家庭目录权限保护 5

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-22 家庭目录权限保护 6

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-23 家庭目录权限保护 7

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-24 家庭目录权限保护 8

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-25 家庭目录权限保护 9

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-26 家庭目录权限保护 10

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-27 家庭目录权限保护 11

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-28 家庭目录权限保护 12

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-29 家庭目录权限保护 13

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-30 家庭目录权限保护 14

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-31 家庭目录权限保护 15

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

### EXT-32 家庭目录权限保护 16

- Query: `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。`
- Expected: 明确提示当前进程没有写权限并建议改用工作区或 /tmp。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请帮我处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦你帮我办这件事：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `换个说法就是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `我想表达的是：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请按照这个意思来做：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `帮我看一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请直接处理这个需求：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `麻烦执行一下：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `请根据这句话处理：将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- English Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please help me with this: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Can you handle this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I want to ask this another way: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please work on the following: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Could you take care of this for me: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please treat this as the request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `What I need is: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `Please respond to this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `I'd like help with this request: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

- Japanese Variants: 10
  - `将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この依頼をお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次の内容で対応してください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `言い換えるとこういう依頼です: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この件を進めてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `以下の内容を対応してほしいです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この指示として扱ってください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `私の意図は次のとおりです: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `次のリクエストに答えてください: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`
  - `この内容でお願いします: 将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹`

## 联网查询

### NET-01 东京天气

- Query: `东京今天的天气怎么样，最高温多少`
- Expected: 获取东京天气最终结果并给出来源。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查下东京的天气`
  - `想知道东京天气怎么样`
  - `看一下东京天气情况`
  - `请告诉我东京天气如何`
  - `查查东京的天气预报`
  - `东京最高温多少`
  - `帮我查一下东京今天最高气温`
  - `请告诉我东京今天会到多少度`
  - `东京天气和最高温都告诉我`
  - `想知道东京今天最热多少度`

- English Variants: 10
  - `What is the weather like in 东京 today?`
  - `Can you check today's weather in 东京?`
  - `Tell me the weather in 东京 today.`
  - `How's the weather in 东京 today?`
  - `Please give me today's forecast in 东京.`
  - `What's the high temperature in 东京 today?`
  - `Tell me today's high temperature in 东京.`
  - `How warm will it get in 东京 today?`
  - `Please check today's forecast and high temperature for 东京.`
  - `I'd like today's weather and the high temperature in 东京.`

- Japanese Variants: 10
  - `东京の今日の天気を教えて`
  - `东京は今日どんな天気か知りたい`
  - `东京の今日の天気予報を見て`
  - `东京の天気を確認して`
  - `东京は今日はどんな天気？`
  - `东京の今日の最高気温は何度？`
  - `东京の天気と最高気温を教えて`
  - `东京は今日何度まで上がる？`
  - `东京の今日の一番高い気温を知りたい`
  - `东京の今日の天気と最高気温を確認して`

### NET-02 福冈降雨

- Query: `福冈今天会下雨吗，请告诉我气温和降雨情况`
- Expected: 获取福冈天气最终结果并给出来源。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查下福冈的天气`
  - `想知道福冈天气怎么样`
  - `看一下福冈天气情况`
  - `请告诉我福冈天气如何`
  - `查查福冈的天气预报`
  - `福冈今天会不会下雨`
  - `帮我看下福冈今天有没有雨`
  - `请查一下福冈今天降雨情况`
  - `福冈今天下雨概率高吗`
  - `我想知道福冈今天是否有雨`

- English Variants: 10
  - `What is the weather like in 福冈 today?`
  - `Can you check today's weather in 福冈?`
  - `Tell me the weather in 福冈 today.`
  - `How's the weather in 福冈 today?`
  - `Please give me today's forecast in 福冈.`
  - `Will it rain in 福冈 today?`
  - `Can you check whether it's going to rain in 福冈 today?`
  - `Is rain expected in 福冈 today?`
  - `Tell me if I should expect rain in 福冈 today.`
  - `Please check today's rain chances in 福冈.`

- Japanese Variants: 10
  - `福冈の今日の天気を教えて`
  - `福冈は今日どんな天気か知りたい`
  - `福冈の今日の天気予報を見て`
  - `福冈の天気を確認して`
  - `福冈は今日はどんな天気？`
  - `福冈は今日雨が降る？`
  - `福冈の今日の降水状況を教えて`
  - `福冈で今日は雨の可能性がある？`
  - `福冈の今日の雨予報を確認して`
  - `福冈は今日は雨になるか見て`

### NET-03 大阪气温

- Query: `大阪今天气温多少，请告诉我最高和最低温`
- Expected: 获取大阪天气最终结果并给出来源。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查下大阪的天气`
  - `想知道大阪天气怎么样`
  - `看一下大阪天气情况`
  - `请告诉我大阪天气如何`
  - `查查大阪的天气预报`
  - `大阪今天多少度`
  - `帮我查下大阪今天气温`
  - `请告诉我大阪今天温度`
  - `大阪今天气温大概多少`
  - `我想知道大阪今天有多热`

- English Variants: 10
  - `What is the weather like in 大阪 today?`
  - `Can you check today's weather in 大阪?`
  - `Tell me the weather in 大阪 today.`
  - `How's the weather in 大阪 today?`
  - `Please give me today's forecast in 大阪.`
  - `What's today's temperature in 大阪?`
  - `Tell me the temperature in 大阪 today.`
  - `How many degrees is it in 大阪 today?`
  - `Can you check today's temperature for 大阪?`
  - `I'd like to know the current temperature in 大阪 today.`

- Japanese Variants: 10
  - `大阪の今日の天気を教えて`
  - `大阪は今日どんな天気か知りたい`
  - `大阪の今日の天気予報を見て`
  - `大阪の天気を確認して`
  - `大阪は今日はどんな天気？`
  - `大阪の今日の気温は何度？`
  - `大阪の今日の温度を教えて`
  - `大阪は今日は何度くらい？`
  - `大阪の今日の気温を確認して`
  - `大阪の今日の温度が知りたい`

### NET-04 东京到旧金山机票

- Query: `东京到旧金山 2026年5月31号 的具体机票时间和票价`
- Expected: 返回带票价线索和时刻表来源的机票查询结果。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查一下对应航线的航班时间和票价`
  - `请看一下这趟航班的大概时间和价格`
  - `我想知道这条航线的具体机票时间与票价`
  - `查查这次出行的航班班次和费用`
  - `请帮我找一下相关航班时刻和价格信息`
  - `看看这趟飞机什么时候飞、票价多少`
  - `帮我检索这条航线的时间和机票价格`
  - `请查询对应日期的航班安排和票价`
  - `我需要这次飞行的大概时间和费用`
  - `请给我这条航线的靠谱航班时间和价格`

- English Variants: 10
  - `Please check the flight times and fares for Tokyo to San Francisco on 2026年5月31号.`
  - `Find me the flight schedule and ticket prices from Tokyo to San Francisco for the requested date.`
  - `I want the flight times and fares for Tokyo to San Francisco on that date.`
  - `Can you look up the specific flight schedule and pricing from Tokyo to San Francisco?`
  - `Please check flights from Tokyo to San Francisco and tell me the times and prices.`
  - `Show me the available Tokyo to San Francisco flights and ticket prices for the requested date.`
  - `Help me find flight times and fares from Tokyo to San Francisco.`
  - `I need the detailed flight schedule and pricing for Tokyo to San Francisco.`
  - `Please look up airfare and departure times from Tokyo to San Francisco.`
  - `Check reliable flight options from Tokyo to San Francisco and tell me the prices.`

- Japanese Variants: 10
  - `この条件のフライト時間と料金を調べて`
  - `対象の便のスケジュールと価格を確認して`
  - `この移動の航空券の時間と値段を知りたい`
  - `該当するフライトの時刻と料金を見て`
  - `この路線の航空券情報を調べて`
  - `便の出発時間と価格を確認してほしい`
  - `このフライトの具体的な時間と運賃を探して`
  - `対象日の航空券スケジュールと料金を見せて`
  - `この旅程のフライト時刻と価格を調べて`
  - `信頼できる情報源でフライト時間と料金を確認して`

### NET-05 福冈到大阪新干线

- Query: `2026年4月20号福冈到大阪的新干线的具体时间和费用`
- Expected: 返回带时间和费用的新干线查询结果。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查一下这趟列车的时间和票价`
  - `请查询对应路线的车次时间和费用`
  - `我想知道这段行程的列车班次和价格`
  - `看看这条线路什么时候有车、票价多少`
  - `帮我找一下这趟车的时刻表和费用`
  - `请查这段路程的火车时间和票价`
  - `帮我检索对应日期的车票时间和价格`
  - `我需要这次铁路出行的具体时间和费用`
  - `请看一下可选列车和票价信息`
  - `查询一下这趟旅程的时刻和票价`

- English Variants: 10
  - `Please check the train schedule and fares for the requested trip.`
  - `Find the train times and ticket prices for that route.`
  - `I want the available train departures and fares for that trip.`
  - `Can you look up the train timetable and cost for the requested route?`
  - `Show me the train options, times, and prices for that trip.`
  - `Please tell me the train schedule and fare information for the route.`
  - `Help me find train times and ticket prices for the requested date.`
  - `I need the timetable and fare details for that train trip.`
  - `Please check rail departures and pricing for the requested journey.`
  - `Look up the train schedule and fare details for me.`

- Japanese Variants: 10
  - `この区間の列車時刻と料金を調べて`
  - `該当ルートの電車の時間と運賃を確認して`
  - `この移動の列車スケジュールと価格を知りたい`
  - `対象日の列車時刻表と料金を見て`
  - `この区間の乗車時間と値段を調べて`
  - `電車の発車時刻と料金を確認してほしい`
  - `この旅程の列車情報を調べて`
  - `該当する鉄道の時間と価格を見せて`
  - `このルートの時刻表と運賃を確認して`
  - `列車の所要時間と料金情報を探して`

### NET-06 购机推荐

- Query: `日常办公买 MacBook Air 还是 MacBook Pro 更合适，请参考 Apple 官网给建议`
- Expected: 返回基于 Apple 相关来源的购机建议。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `日常办公更适合买 MacBook Air 还是 MacBook Pro，请参考 Apple 官网`
  - `请基于 Apple 官网，给我建议日常办公选 Air 还是 Pro`
  - `平时办公用的话，MacBook Air 和 MacBook Pro 哪个更合适？参考 Apple 官网`
  - `帮我对比一下 MacBook Air 和 MacBook Pro，看看办公场景选哪个更好`
  - `想买办公电脑，Air 和 Pro 哪个更值得，麻烦参考 Apple 官方信息`
  - `请结合 Apple 官网内容，判断办公使用更推荐 Air 还是 Pro`
  - `普通办公场景下，MacBook Air 和 MacBook Pro 怎么选，请参考官网`
  - `帮我按照 Apple 官网信息，分析 Air 和 Pro 哪个适合办公`
  - `如果是日常办公，Apple 官网里 Air 和 Pro 哪个更匹配`
  - `请参考 Apple 官方网站，推荐一款更适合办公的 MacBook`

- English Variants: 10
  - `For everyday office work, which is a better fit: MacBook Air or MacBook Pro? Please use Apple's website as the reference.`
  - `Please compare MacBook Air and MacBook Pro for normal office use based on Apple's official site.`
  - `Which should I buy for daily office work, a MacBook Air or a MacBook Pro? Reference Apple.com.`
  - `Using Apple's official information, tell me whether MacBook Air or MacBook Pro is more suitable for office tasks.`
  - `I need advice on MacBook Air versus MacBook Pro for regular work, based on Apple's website.`
  - `Please use Apple's official site to recommend either MacBook Air or MacBook Pro for office use.`
  - `For standard work tasks, is MacBook Air or MacBook Pro the better choice? Refer to Apple.`
  - `Check Apple's website and advise me on MacBook Air versus MacBook Pro for everyday work.`
  - `Based on Apple's official info, which laptop is more appropriate for office work: Air or Pro?`
  - `Help me decide between MacBook Air and MacBook Pro for office use using Apple's site.`

- Japanese Variants: 10
  - `普段の事務作業なら MacBook Air と MacBook Pro のどちらが向いているか、Apple 公式を参考に教えて`
  - `Apple 公式サイトを参考に、日常業務には Air と Pro のどちらが合うか教えて`
  - `通常のオフィスワーク用に MacBook Air と Pro を比べてほしい`
  - `Apple 公式情報ベースで、仕事用なら Air と Pro のどちらがよいか知りたい`
  - `日常的な業務向けに Air と Pro のおすすめを Apple 公式を見て教えて`
  - `MacBook Air と Pro のどちらが普段の仕事に適しているか見てほしい`
  - `Apple の公式サイトを参考に、事務作業向けのおすすめを教えて`
  - `仕事用として Air と Pro のどちらを選ぶべきか Apple 公式基準で教えて`
  - `オフィス用途なら Air と Pro のどちらが向いているか知りたい`
  - `Apple 公式を参考に MacBook Air と Pro を比較してアドバイスして`

### NET-07 MacBook Air 价格

- Query: `Apple 官网里 13 英寸 MacBook Air 的起售价是多少`
- Expected: 返回 Apple 官方来源下的 13 英寸 MacBook Air 起售价。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `Apple 官网里 13 英寸 MacBook Air 多少钱起`
  - `帮我查一下 Apple 官网 13 英寸 MacBook Air 的起步价`
  - `请告诉我 Apple 官网 13 英寸 MacBook Air 的起售价`
  - `13 英寸 MacBook Air 在 Apple 官方网站上的最低价格是多少`
  - `我想知道 Apple 官网 13 英寸 MacBook Air 的入门价格`
  - `查查 Apple 网站上 13 英寸 MacBook Air 的起始价格`
  - `请看一下 13 英寸 MacBook Air 在 Apple 官网卖多少钱起`
  - `Apple 官方网站里 13 英寸 MacBook Air 起价多少`
  - `帮我确认 13 英寸 MacBook Air 的官方起售价`
  - `请查询 Apple 官网 13 英寸 MacBook Air 的基础售价`

- English Variants: 10
  - `What is the starting price of the 13-inch MacBook Air on Apple's website?`
  - `Please check Apple's site for the base price of the 13-inch MacBook Air.`
  - `How much does the 13-inch MacBook Air start at on Apple.com?`
  - `Tell me the official starting price for Apple's 13-inch MacBook Air.`
  - `I want the entry price of the 13-inch MacBook Air from Apple's site.`
  - `Can you look up the starting price of the 13-inch MacBook Air on the Apple website?`
  - `Please find the listed base price for the 13-inch MacBook Air on Apple.com.`
  - `What's the official entry-level price of the 13-inch MacBook Air at Apple?`
  - `Check Apple's website and tell me the starting price for the 13-inch MacBook Air.`
  - `Show me the Apple website price that the 13-inch MacBook Air starts from.`

- Japanese Variants: 10
  - `Apple 公式サイトで 13 インチ MacBook Air の開始価格はいくら？`
  - `13 インチ MacBook Air のApple公式価格の最安構成を教えて`
  - `Apple 公式で 13 インチ MacBook Air はいくらから？`
  - `13 インチ MacBook Air の公式な開始価格を確認して`
  - `Apple サイトの 13 インチ MacBook Air の最低価格を知りたい`
  - `13 インチ MacBook Air のベース価格を Apple 公式で調べて`
  - `Apple 公式ページで 13 インチ MacBook Air の価格を見て`
  - `13 インチ MacBook Air のスタート価格はいくらか教えて`
  - `Apple の 13 インチ MacBook Air の初期価格を確認して`
  - `Apple 公式サイトで 13 インチ MacBook Air の価格帯の入口を教えて`

### NET-08 MacBook Pro 价格

- Query: `Apple 官网里 MacBook Pro 14 英寸的起售价是多少`
- Expected: 返回 Apple 官方来源下的 MacBook Pro 14 英寸起售价。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `Apple 官网里 14 英寸 MacBook Pro 多少钱起`
  - `帮我查一下 Apple 官网 14 英寸 MacBook Pro 的起步价`
  - `请告诉我 Apple 官网 14 英寸 MacBook Pro 的起售价`
  - `14 英寸 MacBook Pro 在 Apple 官方网站上的最低价格是多少`
  - `我想知道 Apple 官网 14 英寸 MacBook Pro 的入门价格`
  - `查查 Apple 网站上 14 英寸 MacBook Pro 的起始价格`
  - `请看一下 14 英寸 MacBook Pro 在 Apple 官网卖多少钱起`
  - `Apple 官方网站里 14 英寸 MacBook Pro 起价多少`
  - `帮我确认 14 英寸 MacBook Pro 的官方起售价`
  - `请查询 Apple 官网 14 英寸 MacBook Pro 的基础售价`

- English Variants: 10
  - `What is the starting price of the 14-inch MacBook Pro on Apple's website?`
  - `Please check Apple's site for the base price of the 14-inch MacBook Pro.`
  - `How much does the 14-inch MacBook Pro start at on Apple.com?`
  - `Tell me the official starting price for Apple's 14-inch MacBook Pro.`
  - `I want the entry price of the 14-inch MacBook Pro from Apple's site.`
  - `Can you look up the starting price of the 14-inch MacBook Pro on the Apple website?`
  - `Please find the listed base price for the 14-inch MacBook Pro on Apple.com.`
  - `What's the official entry-level price of the 14-inch MacBook Pro at Apple?`
  - `Check Apple's website and tell me the starting price for the 14-inch MacBook Pro.`
  - `Show me the Apple website price that the 14-inch MacBook Pro starts from.`

- Japanese Variants: 10
  - `Apple 公式サイトで 14 インチ MacBook Pro の開始価格はいくら？`
  - `14 インチ MacBook Pro のApple公式価格の最安構成を教えて`
  - `Apple 公式で 14 インチ MacBook Pro はいくらから？`
  - `14 インチ MacBook Pro の公式な開始価格を確認して`
  - `Apple サイトの 14 インチ MacBook Pro の最低価格を知りたい`
  - `14 インチ MacBook Pro のベース価格を Apple 公式で調べて`
  - `Apple 公式ページで 14 インチ MacBook Pro の価格を見て`
  - `14 インチ MacBook Pro のスタート価格はいくらか教えて`
  - `Apple の 14 インチ MacBook Pro の初期価格を確認して`
  - `Apple 公式サイトで 14 インチ MacBook Pro の価格帯の入口を教えて`

### NET-09 Time Machine 网络知识

- Query: `请联网搜索 Time Machine 是什么，有什么作用`
- Expected: 返回稳定网络知识，并写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `Time Machine 是什么，有什么作用是什么`
  - `请解释一下Time Machine 是什么，有什么作用`
  - `我想知道Time Machine 是什么，有什么作用的意思`
  - `帮我讲讲Time Machine 是什么，有什么作用`
  - `请介绍一下Time Machine 是什么，有什么作用`
  - `Time Machine 是什么，有什么作用主要是干什么的`
  - `告诉我Time Machine 是什么，有什么作用有什么作用`
  - `能不能说明一下Time Machine 是什么，有什么作用`
  - `请简单解释Time Machine 是什么，有什么作用`
  - `我想了解Time Machine 是什么，有什么作用到底是什么`

- English Variants: 10
  - `What is Time Machine 是什么，有什么作用?`
  - `Please explain what Time Machine 是什么，有什么作用 is.`
  - `I'd like to know what Time Machine 是什么，有什么作用 means.`
  - `Can you tell me what Time Machine 是什么，有什么作用 is?`
  - `Give me an explanation of Time Machine 是什么，有什么作用.`
  - `Help me understand Time Machine 是什么，有什么作用.`
  - `Please introduce Time Machine 是什么，有什么作用 in simple terms.`
  - `What does Time Machine 是什么，有什么作用 do?`
  - `Could you explain the purpose of Time Machine 是什么，有什么作用?`
  - `Tell me the main idea behind Time Machine 是什么，有什么作用.`

- Japanese Variants: 10
  - `Time Machine 是什么，有什么作用 とは何か教えて`
  - `Time Machine 是什么，有什么作用 について説明して`
  - `Time Machine 是什么，有什么作用 の意味を知りたい`
  - `Time Machine 是什么，有什么作用 が何なのか教えて`
  - `Time Machine 是什么，有什么作用 を簡単に説明して`
  - `Time Machine 是什么，有什么作用 の役割を教えて`
  - `Time Machine 是什么，有什么作用 って何？`
  - `Time Machine 是什么，有什么作用 についてわかりやすく教えて`
  - `Time Machine 是什么，有什么作用 の主な用途を知りたい`
  - `Time Machine 是什么，有什么作用 がどんなものか説明して`

### NET-10 Liquid Retina 网络知识

- Query: `请联网搜索 Liquid Retina 显示屏是什么`
- Expected: 返回稳定网络知识，并写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `Liquid Retina 显示屏是什么是什么`
  - `请解释一下Liquid Retina 显示屏是什么`
  - `我想知道Liquid Retina 显示屏是什么的意思`
  - `帮我讲讲Liquid Retina 显示屏是什么`
  - `请介绍一下Liquid Retina 显示屏是什么`
  - `Liquid Retina 显示屏是什么主要是干什么的`
  - `告诉我Liquid Retina 显示屏是什么有什么作用`
  - `能不能说明一下Liquid Retina 显示屏是什么`
  - `请简单解释Liquid Retina 显示屏是什么`
  - `我想了解Liquid Retina 显示屏是什么到底是什么`

- English Variants: 10
  - `What is Liquid Retina 显示屏是什么?`
  - `Please explain what Liquid Retina 显示屏是什么 is.`
  - `I'd like to know what Liquid Retina 显示屏是什么 means.`
  - `Can you tell me what Liquid Retina 显示屏是什么 is?`
  - `Give me an explanation of Liquid Retina 显示屏是什么.`
  - `Help me understand Liquid Retina 显示屏是什么.`
  - `Please introduce Liquid Retina 显示屏是什么 in simple terms.`
  - `What does Liquid Retina 显示屏是什么 do?`
  - `Could you explain the purpose of Liquid Retina 显示屏是什么?`
  - `Tell me the main idea behind Liquid Retina 显示屏是什么.`

- Japanese Variants: 10
  - `Liquid Retina 显示屏是什么 とは何か教えて`
  - `Liquid Retina 显示屏是什么 について説明して`
  - `Liquid Retina 显示屏是什么 の意味を知りたい`
  - `Liquid Retina 显示屏是什么 が何なのか教えて`
  - `Liquid Retina 显示屏是什么 を簡単に説明して`
  - `Liquid Retina 显示屏是什么 の役割を教えて`
  - `Liquid Retina 显示屏是什么 って何？`
  - `Liquid Retina 显示屏是什么 についてわかりやすく教えて`
  - `Liquid Retina 显示屏是什么 の主な用途を知りたい`
  - `Liquid Retina 显示屏是什么 がどんなものか説明して`

### NET-11 本地知识库回查 Time Machine

- Query: `根据本地知识库，Time Machine 是什么`
- Expected: 直接从本地知识库回答。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `Time Machine 是什么是什么`
  - `请解释一下Time Machine 是什么`
  - `我想知道Time Machine 是什么的意思`
  - `帮我讲讲Time Machine 是什么`
  - `请介绍一下Time Machine 是什么`
  - `Time Machine 是什么主要是干什么的`
  - `告诉我Time Machine 是什么有什么作用`
  - `能不能说明一下Time Machine 是什么`
  - `请简单解释Time Machine 是什么`
  - `我想了解Time Machine 是什么到底是什么`

- English Variants: 10
  - `What is Time Machine 是什么?`
  - `Please explain what Time Machine 是什么 is.`
  - `I'd like to know what Time Machine 是什么 means.`
  - `Can you tell me what Time Machine 是什么 is?`
  - `Give me an explanation of Time Machine 是什么.`
  - `Help me understand Time Machine 是什么.`
  - `Please introduce Time Machine 是什么 in simple terms.`
  - `What does Time Machine 是什么 do?`
  - `Could you explain the purpose of Time Machine 是什么?`
  - `Tell me the main idea behind Time Machine 是什么.`

- Japanese Variants: 10
  - `Time Machine 是什么 とは何か教えて`
  - `Time Machine 是什么 について説明して`
  - `Time Machine 是什么 の意味を知りたい`
  - `Time Machine 是什么 が何なのか教えて`
  - `Time Machine 是什么 を簡単に説明して`
  - `Time Machine 是什么 の役割を教えて`
  - `Time Machine 是什么 って何？`
  - `Time Machine 是什么 についてわかりやすく教えて`
  - `Time Machine 是什么 の主な用途を知りたい`
  - `Time Machine 是什么 がどんなものか説明して`

### NET-12 即时天气不入库

- Query: `东京今天的天气怎么样`
- Expected: 即时天气查询不写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查下东京的天气`
  - `想知道东京天气怎么样`
  - `看一下东京天气情况`
  - `请告诉我东京天气如何`
  - `查查东京的天气预报`
  - `东京今天多少度`
  - `帮我查下东京今天气温`
  - `请告诉我东京今天温度`
  - `东京今天气温大概多少`
  - `我想知道东京今天有多热`

- English Variants: 10
  - `What is the weather like in 东京 today?`
  - `Can you check today's weather in 东京?`
  - `Tell me the weather in 东京 today.`
  - `How's the weather in 东京 today?`
  - `Please give me today's forecast in 东京.`
  - `What's today's temperature in 东京?`
  - `Tell me the temperature in 东京 today.`
  - `How many degrees is it in 东京 today?`
  - `Can you check today's temperature for 东京?`
  - `I'd like to know the current temperature in 东京 today.`

- Japanese Variants: 10
  - `东京の今日の天気を教えて`
  - `东京は今日どんな天気か知りたい`
  - `东京の今日の天気予報を見て`
  - `东京の天気を確認して`
  - `东京は今日はどんな天気？`
  - `东京の今日の気温は何度？`
  - `东京の今日の温度を教えて`
  - `东京は今日は何度くらい？`
  - `东京の今日の気温を確認して`
  - `东京の今日の温度が知りたい`

### NET-13 天气来源URL写入

- Query: `东京今天会下雨吗`
- Expected: 联网天气查询会把来源 URL 写入本地来源记忆。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查下东京的天气`
  - `想知道东京天气怎么样`
  - `看一下东京天气情况`
  - `请告诉我东京天气如何`
  - `查查东京的天气预报`
  - `东京今天会不会下雨`
  - `帮我看下东京今天有没有雨`
  - `请查一下东京今天降雨情况`
  - `东京今天下雨概率高吗`
  - `我想知道东京今天是否有雨`

- English Variants: 10
  - `What is the weather like in 东京 today?`
  - `Can you check today's weather in 东京?`
  - `Tell me the weather in 东京 today.`
  - `How's the weather in 东京 today?`
  - `Please give me today's forecast in 东京.`
  - `Will it rain in 东京 today?`
  - `Can you check whether it's going to rain in 东京 today?`
  - `Is rain expected in 东京 today?`
  - `Tell me if I should expect rain in 东京 today.`
  - `Please check today's rain chances in 东京.`

- Japanese Variants: 10
  - `东京の今日の天気を教えて`
  - `东京は今日どんな天気か知りたい`
  - `东京の今日の天気予報を見て`
  - `东京の天気を確認して`
  - `东京は今日はどんな天気？`
  - `东京は今日雨が降る？`
  - `东京の今日の降水状況を教えて`
  - `东京で今日は雨の可能性がある？`
  - `东京の今日の雨予報を確認して`
  - `东京は今日は雨になるか見て`

### NET-14 来源URL复用 Time Machine

- Query: `Time Machine 主要是做什么的`
- Expected: 相似问题优先复用已记录来源 URL，再返回带来源的结果。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `Time Machine 主要是做什么的是什么`
  - `请解释一下Time Machine 主要是做什么的`
  - `我想知道Time Machine 主要是做什么的的意思`
  - `帮我讲讲Time Machine 主要是做什么的`
  - `请介绍一下Time Machine 主要是做什么的`
  - `Time Machine 主要是做什么的主要是干什么的`
  - `告诉我Time Machine 主要是做什么的有什么作用`
  - `能不能说明一下Time Machine 主要是做什么的`
  - `请简单解释Time Machine 主要是做什么的`
  - `我想了解Time Machine 主要是做什么的到底是什么`

- English Variants: 10
  - `What is Time Machine 主要是做什么的?`
  - `Please explain what Time Machine 主要是做什么的 is.`
  - `I'd like to know what Time Machine 主要是做什么的 means.`
  - `Can you tell me what Time Machine 主要是做什么的 is?`
  - `Give me an explanation of Time Machine 主要是做什么的.`
  - `Help me understand Time Machine 主要是做什么的.`
  - `Please introduce Time Machine 主要是做什么的 in simple terms.`
  - `What does Time Machine 主要是做什么的 do?`
  - `Could you explain the purpose of Time Machine 主要是做什么的?`
  - `Tell me the main idea behind Time Machine 主要是做什么的.`

- Japanese Variants: 10
  - `Time Machine 主要是做什么的 とは何か教えて`
  - `Time Machine 主要是做什么的 について説明して`
  - `Time Machine 主要是做什么的 の意味を知りたい`
  - `Time Machine 主要是做什么的 が何なのか教えて`
  - `Time Machine 主要是做什么的 を簡単に説明して`
  - `Time Machine 主要是做什么的 の役割を教えて`
  - `Time Machine 主要是做什么的 って何？`
  - `Time Machine 主要是做什么的 についてわかりやすく教えて`
  - `Time Machine 主要是做什么的 の主な用途を知りたい`
  - `Time Machine 主要是做什么的 がどんなものか説明して`

### NET-15 家庭晚餐菜谱

- Query: `今晚家庭晚饭想做鸡肉咖喱，请联网给我一个菜谱，告诉我主要食材和做法`
- Expected: 返回可执行的家庭菜谱结果并给出来源。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `今晚家庭晚饭想做鸡肉咖喱，请联网给我一个菜谱，告诉我主要食材和做法`
  - `帮我找一个合适的菜谱，并告诉我主要食材和步骤`
  - `请给我这个菜的做法，顺便列出食材`
  - `我想做这道菜，麻烦给我菜谱和步骤`
  - `帮我查一下相关菜谱，告诉我怎么做`
  - `请提供这道菜的食材清单和做法`
  - `给我一个适合的做法，并说明主要材料`
  - `我需要这道菜的菜谱、食材和步骤`
  - `请帮我整理一个简单可做的菜谱`
  - `查一下这类菜适合的做法和所需食材`

- English Variants: 10
  - `Please find me a recipe for this meal and tell me the key ingredients and steps.`
  - `I need a recipe for this dish, including the main ingredients and how to make it.`
  - `Can you look up a recipe and give me the ingredients and method?`
  - `Please suggest a recipe for this and include the ingredient list and instructions.`
  - `Find a good recipe for this meal and explain the main ingredients and steps.`
  - `I want the recipe, the essential ingredients, and the cooking method.`
  - `Please search for a recipe and summarize the ingredients and directions.`
  - `Help me cook this by giving me a recipe with ingredients and steps.`
  - `Can you provide a recipe and walk me through the main steps?`
  - `Please tell me what ingredients I need and how to make this dish.`

- Japanese Variants: 10
  - `今晚家庭晚饭想做鸡肉咖喱，请联网给我一个菜谱，告诉我主要食材和做法`
  - `この料理のレシピと主な材料、作り方を教えて`
  - `作り方と必要な材料を含めたレシピを知りたい`
  - `この料理に合うレシピを探して、手順も教えて`
  - `材料と手順つきでレシピを教えて`
  - `このメニューの作り方を簡単にまとめて`
  - `主な食材と調理手順を教えてほしい`
  - `レシピを探して、材料と流れを説明して`
  - `この料理を作るための材料と手順を知りたい`
  - `家庭で作りやすいレシピを教えて`

### NET-16 孩子早餐菜谱

- Query: `适合小学生上学前吃的简单早餐菜谱，给我食材和步骤`
- Expected: 返回适合家庭场景的早餐菜谱并给出来源。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `适合小学生上学前吃的简单早餐菜谱，给我食材和步骤`
  - `帮我找一个合适的菜谱，并告诉我主要食材和步骤`
  - `请给我这个菜的做法，顺便列出食材`
  - `我想做这道菜，麻烦给我菜谱和步骤`
  - `帮我查一下相关菜谱，告诉我怎么做`
  - `请提供这道菜的食材清单和做法`
  - `给我一个适合的做法，并说明主要材料`
  - `我需要这道菜的菜谱、食材和步骤`
  - `请帮我整理一个简单可做的菜谱`
  - `查一下这类菜适合的做法和所需食材`

- English Variants: 10
  - `Please find me a recipe for this meal and tell me the key ingredients and steps.`
  - `I need a recipe for this dish, including the main ingredients and how to make it.`
  - `Can you look up a recipe and give me the ingredients and method?`
  - `Please suggest a recipe for this and include the ingredient list and instructions.`
  - `Find a good recipe for this meal and explain the main ingredients and steps.`
  - `I want the recipe, the essential ingredients, and the cooking method.`
  - `Please search for a recipe and summarize the ingredients and directions.`
  - `Help me cook this by giving me a recipe with ingredients and steps.`
  - `Can you provide a recipe and walk me through the main steps?`
  - `Please tell me what ingredients I need and how to make this dish.`

- Japanese Variants: 10
  - `适合小学生上学前吃的简单早餐菜谱，给我食材和步骤`
  - `この料理のレシピと主な材料、作り方を教えて`
  - `作り方と必要な材料を含めたレシピを知りたい`
  - `この料理に合うレシピを探して、手順も教えて`
  - `材料と手順つきでレシピを教えて`
  - `このメニューの作り方を簡単にまとめて`
  - `主な食材と調理手順を教えてほしい`
  - `レシピを探して、材料と流れを説明して`
  - `この料理を作るための材料と手順を知りたい`
  - `家庭で作りやすいレシピを教えて`

### NET-17 光合作用网络知识

- Query: `请联网搜索 光合作用 是什么`
- Expected: 返回稳定知识并写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `光合作用 是什么是什么`
  - `请解释一下光合作用 是什么`
  - `我想知道光合作用 是什么的意思`
  - `帮我讲讲光合作用 是什么`
  - `请介绍一下光合作用 是什么`
  - `光合作用 是什么主要是干什么的`
  - `告诉我光合作用 是什么有什么作用`
  - `能不能说明一下光合作用 是什么`
  - `请简单解释光合作用 是什么`
  - `我想了解光合作用 是什么到底是什么`

- English Variants: 10
  - `What is 光合作用 是什么?`
  - `Please explain what 光合作用 是什么 is.`
  - `I'd like to know what 光合作用 是什么 means.`
  - `Can you tell me what 光合作用 是什么 is?`
  - `Give me an explanation of 光合作用 是什么.`
  - `Help me understand 光合作用 是什么.`
  - `Please introduce 光合作用 是什么 in simple terms.`
  - `What does 光合作用 是什么 do?`
  - `Could you explain the purpose of 光合作用 是什么?`
  - `Tell me the main idea behind 光合作用 是什么.`

- Japanese Variants: 10
  - `光合作用 是什么 とは何か教えて`
  - `光合作用 是什么 について説明して`
  - `光合作用 是什么 の意味を知りたい`
  - `光合作用 是什么 が何なのか教えて`
  - `光合作用 是什么 を簡単に説明して`
  - `光合作用 是什么 の役割を教えて`
  - `光合作用 是什么 って何？`
  - `光合作用 是什么 についてわかりやすく教えて`
  - `光合作用 是什么 の主な用途を知りたい`
  - `光合作用 是什么 がどんなものか説明して`

### NET-18 本地知识库回查 光合作用

- Query: `根据本地知识库，光合作用是什么`
- Expected: 直接从本地知识库回答光合作用。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `光合作用是什么是什么`
  - `请解释一下光合作用是什么`
  - `我想知道光合作用是什么的意思`
  - `帮我讲讲光合作用是什么`
  - `请介绍一下光合作用是什么`
  - `光合作用是什么主要是干什么的`
  - `告诉我光合作用是什么有什么作用`
  - `能不能说明一下光合作用是什么`
  - `请简单解释光合作用是什么`
  - `我想了解光合作用是什么到底是什么`

- English Variants: 10
  - `What is 光合作用是什么?`
  - `Please explain what 光合作用是什么 is.`
  - `I'd like to know what 光合作用是什么 means.`
  - `Can you tell me what 光合作用是什么 is?`
  - `Give me an explanation of 光合作用是什么.`
  - `Help me understand 光合作用是什么.`
  - `Please introduce 光合作用是什么 in simple terms.`
  - `What does 光合作用是什么 do?`
  - `Could you explain the purpose of 光合作用是什么?`
  - `Tell me the main idea behind 光合作用是什么.`

- Japanese Variants: 10
  - `光合作用是什么 とは何か教えて`
  - `光合作用是什么 について説明して`
  - `光合作用是什么 の意味を知りたい`
  - `光合作用是什么 が何なのか教えて`
  - `光合作用是什么 を簡単に説明して`
  - `光合作用是什么 の役割を教えて`
  - `光合作用是什么 って何？`
  - `光合作用是什么 についてわかりやすく教えて`
  - `光合作用是什么 の主な用途を知りたい`
  - `光合作用是什么 がどんなものか説明して`

### NET-19 日本热点新闻

- Query: `今天日本有什么热点新闻，请给我两条摘要`
- Expected: 返回热点新闻摘要和来源。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `今天日本有哪些热点新闻，给我两条摘要`
  - `帮我看下日本今天的热门新闻，并总结两条`
  - `请给我两条今天日本热点新闻的简要摘要`
  - `我想知道今天日本有什么大新闻，麻烦总结两条`
  - `查一下今天日本的新闻热点，给我两条简介`
  - `请整理两条今天日本的热门新闻摘要`
  - `今天日本上了哪些新闻热点，给我概括两条`
  - `帮我筛两条今天日本的重点新闻并总结`
  - `请提供两条今天日本热点新闻的简短概述`
  - `看看今天日本有什么值得关注的新闻，给我两条摘要`

- English Variants: 10
  - `What are the top news stories in Japan today? Please give me two short summaries.`
  - `Please find today's trending news in Japan and provide two summaries.`
  - `Show me two brief summaries of today's major news in Japan.`
  - `Can you tell me two hot news topics in Japan today with short summaries?`
  - `I want two concise summaries of today's biggest news in Japan.`
  - `Please check the latest hot news in Japan today and summarize two items.`
  - `Give me two short summaries of what's making headlines in Japan today.`
  - `What is trending in Japan today? Please summarize two news items.`
  - `Please provide two brief summaries of current hot topics in Japan today.`
  - `Find two important Japanese news stories from today and summarize them.`

- Japanese Variants: 10
  - `今日の日本の注目ニュースを2件、要約付きで教えて`
  - `日本で今日話題のニュースを2つ要約して`
  - `今日の日本のホットニュースを2件まとめて`
  - `日本の今日の主要ニュースを2つ短く要約して`
  - `今日の日本の話題を2件だけ概要で教えて`
  - `日本の最新ニュースから注目記事を2つ要約して`
  - `今日の日本で大きなニュースを2件まとめてほしい`
  - `日本の本日のトレンドニュースを2件教えて`
  - `今日の日本ニュースの要点を2つだけ知りたい`
  - `日本の今日の見出しニュースを2件要約して`

### NET-20 家庭关注股票

- Query: `英伟达今天的股价是多少，涨跌情况如何`
- Expected: 返回实时股票信息和来源。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `英伟达今天的股价是多少`
  - `帮我查一下英伟达今日股价`
  - `请告诉我英伟达今天股价`
  - `英伟达今天股票价格多少`
  - `我想知道英伟达当前股价`
  - `英伟达今天股价多少，涨跌怎么样`
  - `帮我看下英伟达今日股价和涨跌幅`
  - `请查一下英伟达今天的股价表现`
  - `英伟达今天股票价格和涨跌情况告诉我`
  - `我想了解英伟达今天股价及涨跌变化`

- English Variants: 10
  - `What is NVIDIA's stock price today?`
  - `Please check NVIDIA's share price for today.`
  - `How much is NVIDIA stock trading at today?`
  - `Tell me today's stock price for NVIDIA.`
  - `I want today's market price for NVIDIA stock.`
  - `What's NVIDIA's stock price today, and how much is it up or down?`
  - `Please give me today's NVIDIA share price and price change.`
  - `How is NVIDIA stock moving today? Include the current price.`
  - `Tell me NVIDIA's stock price and today's gain or loss.`
  - `Check today's NVIDIA stock price together with the daily change.`

- Japanese Variants: 10
  - `NVIDIA の今日の株価はいくら？`
  - `NVIDIA の本日の株価を教えて`
  - `NVIDIA 株は今日いくらで取引されている？`
  - `NVIDIA の今日の株価を確認して`
  - `NVIDIA の現在の株価を知りたい`
  - `NVIDIA の今日の株価と値動きを教えて`
  - `NVIDIA の本日の株価と上げ下げを確認して`
  - `NVIDIA 株は今日はどう動いている？価格も教えて`
  - `NVIDIA の今日の株価と騰落状況を見たい`
  - `NVIDIA の株価と本日の変動幅を教えて`

### NET-21 Apple 股票

- Query: `苹果公司今天的股价是多少`
- Expected: 返回 Apple 实时股票信息和来源。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `苹果公司今天的股价是多少`
  - `帮我查一下苹果公司今日股价`
  - `请告诉我苹果公司今天股价`
  - `苹果公司今天股票价格多少`
  - `我想知道苹果公司当前股价`
  - `帮我看看苹果公司今天股价多少`
  - `请查询苹果公司今日市场价格`
  - `苹果公司今天每股多少钱`
  - `看一下苹果公司股票今天报价`
  - `请告诉我苹果公司目前的股票价格`

- English Variants: 10
  - `What is Apple's stock price today?`
  - `Please check Apple's share price for today.`
  - `How much is Apple stock trading at today?`
  - `Tell me today's stock price for Apple.`
  - `I want today's market price for Apple stock.`
  - `Can you look up the current stock price of Apple today?`
  - `Please tell me the latest Apple stock price today.`
  - `Show me how much Apple stock costs today.`
  - `I'd like to know today's quoted price for Apple.`
  - `Check the current share price of Apple for me today.`

- Japanese Variants: 10
  - `Apple の今日の株価はいくら？`
  - `Apple の本日の株価を教えて`
  - `Apple 株は今日いくらで取引されている？`
  - `Apple の今日の株価を確認して`
  - `Apple の現在の株価を知りたい`
  - `Apple の株価を今日時点で見せて`
  - `Apple の本日の市場価格を確認して`
  - `Apple 株の今日の価格を教えて`
  - `Apple の現在値を見たい`
  - `Apple の今日の売買価格をチェックして`

### NET-22 孩子学习知识点

- Query: `请联网搜索 分数为什么要通分，用孩子能听懂的话解释`
- Expected: 返回稳定知识并写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `分数为什么要通分，用孩子能听懂的话解释是什么`
  - `请解释一下分数为什么要通分，用孩子能听懂的话解释`
  - `我想知道分数为什么要通分，用孩子能听懂的话解释的意思`
  - `帮我讲讲分数为什么要通分，用孩子能听懂的话解释`
  - `请介绍一下分数为什么要通分，用孩子能听懂的话解释`
  - `分数为什么要通分，用孩子能听懂的话解释主要是干什么的`
  - `告诉我分数为什么要通分，用孩子能听懂的话解释有什么作用`
  - `能不能说明一下分数为什么要通分，用孩子能听懂的话解释`
  - `请简单解释分数为什么要通分，用孩子能听懂的话解释`
  - `我想了解分数为什么要通分，用孩子能听懂的话解释到底是什么`

- English Variants: 10
  - `What is 分数为什么要通分，用孩子能听懂的话解释?`
  - `Please explain what 分数为什么要通分，用孩子能听懂的话解释 is.`
  - `I'd like to know what 分数为什么要通分，用孩子能听懂的话解释 means.`
  - `Can you tell me what 分数为什么要通分，用孩子能听懂的话解释 is?`
  - `Give me an explanation of 分数为什么要通分，用孩子能听懂的话解释.`
  - `Help me understand 分数为什么要通分，用孩子能听懂的话解释.`
  - `Please introduce 分数为什么要通分，用孩子能听懂的话解释 in simple terms.`
  - `What does 分数为什么要通分，用孩子能听懂的话解释 do?`
  - `Could you explain the purpose of 分数为什么要通分，用孩子能听懂的话解释?`
  - `Tell me the main idea behind 分数为什么要通分，用孩子能听懂的话解释.`

- Japanese Variants: 10
  - `分数为什么要通分，用孩子能听懂的话解释 とは何か教えて`
  - `分数为什么要通分，用孩子能听懂的话解释 について説明して`
  - `分数为什么要通分，用孩子能听懂的话解释 の意味を知りたい`
  - `分数为什么要通分，用孩子能听懂的话解释 が何なのか教えて`
  - `分数为什么要通分，用孩子能听懂的话解释 を簡単に説明して`
  - `分数为什么要通分，用孩子能听懂的话解释 の役割を教えて`
  - `分数为什么要通分，用孩子能听懂的话解释 って何？`
  - `分数为什么要通分，用孩子能听懂的话解释 についてわかりやすく教えて`
  - `分数为什么要通分，用孩子能听懂的话解释 の主な用途を知りたい`
  - `分数为什么要通分，用孩子能听懂的话解释 がどんなものか説明して`

### NET-23 本地知识库回查 通分

- Query: `根据本地知识库，分数为什么要通分`
- Expected: 直接从本地知识库回答通分。
- Reset Before: Yes
- Setup Queries: 1

- Chinese Variants: 10
  - `分数为什么要通分是什么`
  - `请解释一下分数为什么要通分`
  - `我想知道分数为什么要通分的意思`
  - `帮我讲讲分数为什么要通分`
  - `请介绍一下分数为什么要通分`
  - `分数为什么要通分主要是干什么的`
  - `告诉我分数为什么要通分有什么作用`
  - `能不能说明一下分数为什么要通分`
  - `请简单解释分数为什么要通分`
  - `我想了解分数为什么要通分到底是什么`

- English Variants: 10
  - `What is 分数为什么要通分?`
  - `Please explain what 分数为什么要通分 is.`
  - `I'd like to know what 分数为什么要通分 means.`
  - `Can you tell me what 分数为什么要通分 is?`
  - `Give me an explanation of 分数为什么要通分.`
  - `Help me understand 分数为什么要通分.`
  - `Please introduce 分数为什么要通分 in simple terms.`
  - `What does 分数为什么要通分 do?`
  - `Could you explain the purpose of 分数为什么要通分?`
  - `Tell me the main idea behind 分数为什么要通分.`

- Japanese Variants: 10
  - `分数为什么要通分 とは何か教えて`
  - `分数为什么要通分 について説明して`
  - `分数为什么要通分 の意味を知りたい`
  - `分数为什么要通分 が何なのか教えて`
  - `分数为什么要通分 を簡単に説明して`
  - `分数为什么要通分 の役割を教えて`
  - `分数为什么要通分 って何？`
  - `分数为什么要通分 についてわかりやすく教えて`
  - `分数为什么要通分 の主な用途を知りたい`
  - `分数为什么要通分 がどんなものか説明して`

### NET-24 家庭火车票信息

- Query: `东京到大阪明天的火车票时间和票价`
- Expected: 返回火车票时间和票价来源。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查一下这趟列车的时间和票价`
  - `请查询对应路线的车次时间和费用`
  - `我想知道这段行程的列车班次和价格`
  - `看看这条线路什么时候有车、票价多少`
  - `帮我找一下这趟车的时刻表和费用`
  - `请查这段路程的火车时间和票价`
  - `帮我检索对应日期的车票时间和价格`
  - `我需要这次铁路出行的具体时间和费用`
  - `请看一下可选列车和票价信息`
  - `查询一下这趟旅程的时刻和票价`

- English Variants: 10
  - `Please check the train schedule and fares for the requested trip.`
  - `Find the train times and ticket prices for that route.`
  - `I want the available train departures and fares for that trip.`
  - `Can you look up the train timetable and cost for the requested route?`
  - `Show me the train options, times, and prices for that trip.`
  - `Please tell me the train schedule and fare information for the route.`
  - `Help me find train times and ticket prices for the requested date.`
  - `I need the timetable and fare details for that train trip.`
  - `Please check rail departures and pricing for the requested journey.`
  - `Look up the train schedule and fare details for me.`

- Japanese Variants: 10
  - `この区間の列車時刻と料金を調べて`
  - `該当ルートの電車の時間と運賃を確認して`
  - `この移動の列車スケジュールと価格を知りたい`
  - `対象日の列車時刻表と料金を見て`
  - `この区間の乗車時間と値段を調べて`
  - `電車の発車時刻と料金を確認してほしい`
  - `この旅程の列車情報を調べて`
  - `該当する鉄道の時間と価格を見せて`
  - `このルートの時刻表と運賃を確認して`
  - `列車の所要時間と料金情報を探して`

### NET-25 自动改写机票查询

- Query: `帮我查一下月底从东京飞旧金山的大概航班时间和价格，尽量给我靠谱来源`
- Expected: 触发自动改写或多轮检索，并返回来源结果。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `帮我查一下对应航线的航班时间和票价`
  - `请看一下这趟航班的大概时间和价格`
  - `我想知道这条航线的具体机票时间与票价`
  - `查查这次出行的航班班次和费用`
  - `请帮我找一下相关航班时刻和价格信息`
  - `看看这趟飞机什么时候飞、票价多少`
  - `帮我检索这条航线的时间和机票价格`
  - `请查询对应日期的航班安排和票价`
  - `我需要这次飞行的大概时间和费用`
  - `请给我这条航线的靠谱航班时间和价格`

- English Variants: 10
  - `Please check the flight times and fares for 帮我查一下月底从东京飞旧金山的大概航班时间和价格，尽量给我靠谱来源.`
  - `Find me the flight schedule and ticket prices from Tokyo to San Francisco for the requested date.`
  - `I want the flight times and fares for Tokyo to San Francisco on that date.`
  - `Can you look up the specific flight schedule and pricing from Tokyo to San Francisco?`
  - `Please check flights from Tokyo to San Francisco and tell me the times and prices.`
  - `Show me the available Tokyo to San Francisco flights and ticket prices for the requested date.`
  - `Help me find flight times and fares from Tokyo to San Francisco.`
  - `I need the detailed flight schedule and pricing for Tokyo to San Francisco.`
  - `Please look up airfare and departure times from Tokyo to San Francisco.`
  - `Check reliable flight options from Tokyo to San Francisco and tell me the prices.`

- Japanese Variants: 10
  - `この条件のフライト時間と料金を調べて`
  - `対象の便のスケジュールと価格を確認して`
  - `この移動の航空券の時間と値段を知りたい`
  - `該当するフライトの時刻と料金を見て`
  - `この路線の航空券情報を調べて`
  - `便の出発時間と価格を確認してほしい`
  - `このフライトの具体的な時間と運賃を探して`
  - `対象日の航空券スケジュールと料金を見せて`
  - `この旅程のフライト時刻と価格を調べて`
  - `信頼できる情報源でフライト時間と料金を確認して`

### NET-26 自动改写知识查询

- Query: `给孩子讲讲为什么白天能看到彩虹，用容易理解的话`
- Expected: 触发自动改写或多轮检索，并把稳定知识写入本地知识库。
- Reset Before: Yes
- Setup Queries: 0

- Chinese Variants: 10
  - `给孩子讲讲为什么白天能看到彩虹，用容易理解的话`
  - `请用孩子容易理解的话解释一下`
  - `帮我用小朋友能听懂的方式讲讲这个`
  - `请把这个内容讲得简单一点，适合孩子听`
  - `我想让孩子听懂，麻烦通俗解释`
  - `请用很简单的话说明这个问题`
  - `帮我做一个儿童版解释`
  - `请像给小学生讲课一样解释`
  - `换成适合孩子理解的说法告诉我`
  - `请用生活化的例子给孩子讲讲`

- English Variants: 10
  - `Please explain this in a way a child can easily understand.`
  - `Can you describe this in simple words for a child?`
  - `I want a kid-friendly explanation of this topic.`
  - `Please explain this simply enough for a child to follow.`
  - `Help me explain this to a child in easy language.`
  - `Can you make this explanation easy for kids?`
  - `Please give me a child-friendly version of the explanation.`
  - `Explain this in simple everyday language for a child.`
  - `I need a very easy explanation that a child can understand.`
  - `Please teach this topic in a child-friendly way.`

- Japanese Variants: 10
  - `给孩子讲讲为什么白天能看到彩虹，用容易理解的话`
  - `子どもにもわかる言い方で説明して`
  - `小学生向けにやさしく教えて`
  - `子どもが理解しやすい言葉で話して`
  - `できるだけ簡単に説明して`
  - `子ども向けのやさしい説明にして`
  - `身近な例でわかりやすく教えて`
  - `難しい言葉を使わずに説明して`
  - `子どもに話すようにやさしく説明して`
  - `かみ砕いてわかりやすく教えて`
