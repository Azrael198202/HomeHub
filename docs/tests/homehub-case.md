# HomeHub 3-Phase Family Test Cases For macOS

- Generated at: 2026-04-12T15:24
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
  - `Hello, HomeHub`
  - `Hi there`
  - `Hey`
  - `Hey, HomeHub`
  - `Hello there`
  - `Hi, HomeHub`
  - `Hey there`
  - `Greetings`

- Japanese Variants: 10
  - `こんにちは`
  - `やあ、こんにちは`
  - `こんにちは、HomeHub`
  - `どうも、こんにちは`
  - `やあ`
  - `こんにちは、元気？`
  - `やあ、HomeHub`
  - `こんにちは、いる？`
  - `もしもし`
  - `こんにちは！`
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
  - `Hi, HomeHub`
  - `Hello, HomeHub`
  - `Hey, HomeHub`
  - `Hi there, HomeHub`
  - `Hello there, HomeHub`
  - `Hey there, HomeHub`
  - `Good morning, HomeHub`
  - `Good evening, HomeHub`
  - `Greetings, HomeHub`
  - `HomeHub, are you there?`

- Japanese Variants: 10
  - `こんにちは、HomeHub`
  - `やあ、HomeHub`
  - `HomeHub、こんにちは`
  - `どうも、HomeHub`
  - `こんにちは、HomeHubさん`
  - `やあ、HomeHub`
  - `HomeHub、いる？`
  - `もしもし、HomeHub`
  - `おはよう、HomeHub`
  - `こんばんは、HomeHub`
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
  - `Hi, good morning`
  - `Hello, good morning`
  - `Good morning there`
  - `Morning there`
  - `Hope you're having a good morning`
  - `Wishing you a good morning`

- Japanese Variants: 10
  - `おはよう`
  - `おはようございます`
  - `おはよう、HomeHub`
  - `やあ、おはよう`
  - `おはようございます、HomeHub`
  - `おはよう、元気？`
  - `おはよう、いる？`
  - `やあ、HomeHub`
  - `今日もよろしく`
  - `おはよう！`
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
  - `Hi, good evening`
  - `Hello, good evening`
  - `Good evening there`
  - `Evening there`
  - `Hope you're having a good evening`
  - `Wishing you a pleasant evening`

- Japanese Variants: 10
  - `こんばんは`
  - `こんばんは、HomeHub`
  - `やあ、こんばんは`
  - `こんばんは、HomeHubさん`
  - `こんばんは、元気？`
  - `こんばんは、いる？`
  - `やあ、HomeHub`
  - `今日もお疲れさま`
  - `こんばんは！`
  - `もしもし、こんばんは`
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
  - `What is the weather like in Fukuoka today?`
  - `Can you check today's weather in Fukuoka?`
  - `Tell me today's temperature in Fukuoka.`
  - `How's the weather in Fukuoka today?`
  - `Please give me today's forecast for Fukuoka.`
  - `What's the high temperature in Fukuoka today?`
  - `Tell me today's high and low temperatures in Fukuoka.`
  - `How warm will it get in Fukuoka today?`
  - `Please check today's forecast and temperatures for Fukuoka.`
  - `I'd like today's weather and temperature details for Fukuoka.`

- Japanese Variants: 10
  - `福岡の今日の天気を教えてください。`
  - `福岡の今日の天気を確認してください。`
  - `福岡の今日の気温を教えてください。`
  - `福岡の今日の天気はどうですか。`
  - `福岡の今日の天気予報を教えてください。`
  - `福岡の今日の最高気温は何度ですか。`
  - `福岡の今日の最高気温と最低気温を教えてください。`
  - `福岡は今日どれくらい暖かくなりますか。`
  - `福岡の今日の予報と気温を確認してください。`
  - `福岡の今日の天気と気温の詳細を知りたいです。`
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
  - `What is the weather like in Tokyo today?`
  - `Can you check today's weather in Tokyo?`
  - `Tell me today's temperature in Tokyo.`
  - `How's the weather in Tokyo today?`
  - `Please give me today's forecast for Tokyo.`
  - `What's the high temperature in Tokyo today?`
  - `Tell me today's high and low temperatures in Tokyo.`
  - `How warm will it get in Tokyo today?`
  - `Please check today's forecast and temperatures for Tokyo.`
  - `I'd like today's weather and temperature details for Tokyo.`

- Japanese Variants: 10
  - `東京の今日の天気を教えてください。`
  - `東京の今日の天気を確認してください。`
  - `東京の今日の気温を教えてください。`
  - `東京の今日の天気はどうですか。`
  - `東京の今日の天気予報を教えてください。`
  - `東京の今日の最高気温は何度ですか。`
  - `東京の今日の最高気温と最低気温を教えてください。`
  - `東京は今日どれくらい暖かくなりますか。`
  - `東京の今日の予報と気温を確認してください。`
  - `東京の今日の天気と気温の詳細を知りたいです。`
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
  - `Will it rain in Osaka today?`
  - `Can you check whether it will rain in Osaka today?`
  - `Please tell me today's weather in Osaka and whether rain is expected.`
  - `Show me today's forecast for Osaka, including the chance of rain.`
  - `Is rain expected in Osaka today?`
  - `Tell me the temperature and rain forecast for Osaka today.`
  - `Please check today's weather in Osaka, especially the rain forecast.`
  - `What will the weather be like in Osaka today? Will it rain?`
  - `I'd like today's weather and rain information for Osaka.`
  - `Can you give me today's forecast for Osaka, including rain and temperature?`

- Japanese Variants: 10
  - `大阪は今日、雨が降りますか。`
  - `大阪の今日の雨予報を確認してください。`
  - `大阪の今日の天気と雨の情報を教えてください。`
  - `大阪の今日の降水確率を見せてください。`
  - `大阪では今日、雨の予報がありますか。`
  - `大阪の今日の気温と雨予報を教えてください。`
  - `大阪の今日の天気を、雨を中心に確認してください。`
  - `大阪の今日の天気はどうですか。雨は降りますか。`
  - `大阪の今日の天気と降雨情報を知りたいです。`
  - `大阪の今日の予報を、気温と雨を含めて教えてください。`
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
  - `What is the weather like today?`
  - `Can you check today's weather?`
  - `Tell me today's weather.`
  - `How's the weather today?`
  - `Please give me today's forecast.`
  - `What's today's high temperature?`
  - `Tell me today's temperature.`
  - `How warm will it get today?`
  - `Please check today's forecast and high temperature.`
  - `I'd like today's weather and temperature details.`

- Japanese Variants: 10
  - `今日の天気を教えてください。`
  - `今日の天気を確認してください。`
  - `今日の天気を教えて。`
  - `今日の天気はどうですか。`
  - `今日の天気予報を教えてください。`
  - `今日の最高気温は何度ですか。`
  - `今日の気温を教えてください。`
  - `今日はどれくらい暖かくなりますか。`
  - `今日の予報と最高気温を確認してください。`
  - `今日の天気と気温の詳細を知りたいです。`
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
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-inbox の下にあるファイルを一覧にしてください。`
  - `/tmp/homehub-family-suite/family-inbox にはどんなファイルがありますか。`
  - `/tmp/homehub-family-suite/family-inbox の中にあるファイルを確認してください。`
  - `/tmp/homehub-family-suite/family-inbox の下にあるファイルを教えてください。`
  - `/tmp/homehub-family-suite/family-inbox の内容を見たいです。`
  - `/tmp/homehub-family-suite/family-inbox を開いて中のファイルを一覧表示してください。`
  - `/tmp/homehub-family-suite/family-inbox を確認してファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧をください。`
  - `/tmp/homehub-family-suite/family-inbox の中にどんなファイルがあるか教えてください。`
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
  - `List the files under /tmp/homehub-family-suite/family-inbox, then send me family_trip.pptx.`
  - `What files are in /tmp/homehub-family-suite/family-inbox? Please send me family_trip.pptx.`
  - `Can you check /tmp/homehub-family-suite/family-inbox and share family_trip.pptx with me?`
  - `Please look in /tmp/homehub-family-suite/family-inbox, list the files, and send me family_trip.pptx.`
  - `I want to see the files in /tmp/homehub-family-suite/family-inbox; also send me family_trip.pptx.`
  - `Open /tmp/homehub-family-suite/family-inbox, tell me what files are there, and send family_trip.pptx.`
  - `Check the contents of /tmp/homehub-family-suite/family-inbox and forward family_trip.pptx to me.`
  - `Could you list the files in /tmp/homehub-family-suite/family-inbox and send me family_trip.pptx?`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and share the file family_trip.pptx.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて、そのあと family_trip.pptx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox の下にあるファイルを一覧表示してから、family_trip.pptx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox にどんなファイルがあるか教えてください。あわせて family_trip.pptx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox を確認して、family_trip.pptx を共有してください。`
  - `/tmp/homehub-family-suite/family-inbox を見てファイル一覧を出し、そのうえで family_trip.pptx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox のファイルを見たいです。あわせて family_trip.pptx も送ってください。`
  - `/tmp/homehub-family-suite/family-inbox を開いて中のファイルを教え、そのあと family_trip.pptx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox の内容を確認して、family_trip.pptx を転送してください。`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を出して、family_trip.pptx を送ってもらえますか。`
  - `/tmp/homehub-family-suite/family-inbox を確認して、ファイル family_trip.pptx を共有してください。`
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
  - `Search for budget files under /tmp/homehub-family-suite/family-inbox.`
  - `Find the budget files in /tmp/homehub-family-suite/family-inbox.`
  - `Please look through /tmp/homehub-family-suite/family-inbox for files matching budget.`
  - `Can you search /tmp/homehub-family-suite/family-inbox for any budget files?`
  - `Show me files related to budget under /tmp/homehub-family-suite/family-inbox.`
  - `I need you to find budget-related files in /tmp/homehub-family-suite/family-inbox.`
  - `Please check /tmp/homehub-family-suite/family-inbox and search for budget files.`
  - `Look in /tmp/homehub-family-suite/family-inbox for anything named budget.`
  - `Search the folder /tmp/homehub-family-suite/family-inbox for budget.`
  - `Could you find files connected to budget in /tmp/homehub-family-suite/family-inbox?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox の下で budget ファイルを検索してください。`
  - `/tmp/homehub-family-suite/family-inbox で budget ファイルを探してください。`
  - `/tmp/homehub-family-suite/family-inbox の中から budget に一致するファイルを探してください。`
  - `/tmp/homehub-family-suite/family-inbox に budget ファイルがあるか検索してください。`
  - `/tmp/homehub-family-suite/family-inbox の下にある budget 関連のファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-inbox の中で budget に関係するファイルを見つけてください。`
  - `/tmp/homehub-family-suite/family-inbox を確認して budget ファイルを検索してください。`
  - `/tmp/homehub-family-suite/family-inbox で名前に budget を含むものを探してください。`
  - `フォルダ /tmp/homehub-family-suite/family-inbox で budget を検索してください。`
  - `/tmp/homehub-family-suite/family-inbox の中で budget に関連するファイルを見つけてもらえますか。`
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
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読んでください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を開いて読んでください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の内容を見せてください。`
  - `ファイル /tmp/homehub-family-suite/family-reading/shopping-note.txt を読めますか。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の中身を見たいです。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を開いて内容を教えてください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の内容を確認してください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読んで見せてください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の内容を表示してもらえますか。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を見て読み上げてください。`
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
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読んでください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を開いて読んでください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の内容を見せてください。`
  - `ファイル /tmp/homehub-family-suite/family-reading/recipe.json を読めますか。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の中身を見たいです。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を開いて内容を教えてください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の内容を確認してください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読んで見せてください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の内容を表示してもらえますか。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を見て読み上げてください。`
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
  - `/tmp/homehub-family-suite/family-library にあるファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-library の下にあるファイルを一覧にしてください。`
  - `/tmp/homehub-family-suite/family-library にはどんなファイルがありますか。`
  - `/tmp/homehub-family-suite/family-library の中にあるファイルを確認してください。`
  - `/tmp/homehub-family-suite/family-library の下にあるファイルを教えてください。`
  - `/tmp/homehub-family-suite/family-library の内容を見たいです。`
  - `/tmp/homehub-family-suite/family-library を開いて中のファイルを一覧表示してください。`
  - `/tmp/homehub-family-suite/family-library を確認してファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-library のファイル一覧をください。`
  - `/tmp/homehub-family-suite/family-library の中にどんなファイルがあるか教えてください。`
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
  - `List the files under /Users/home/Documents, then send me AI_Agent_Build2026 en.pptx.`
  - `What files are in /Users/home/Documents? Please send me AI_Agent_Build2026 en.pptx.`
  - `Can you check /Users/home/Documents and share AI_Agent_Build2026 en.pptx with me?`
  - `Please look in /Users/home/Documents, list the files, and send me AI_Agent_Build2026 en.pptx.`
  - `I want to see the files in /Users/home/Documents; also send me AI_Agent_Build2026 en.pptx.`
  - `Open /Users/home/Documents, tell me what files are there, and send AI_Agent_Build2026 en.pptx.`
  - `Check the contents of /Users/home/Documents and forward AI_Agent_Build2026 en.pptx to me.`
  - `Could you list the files in /Users/home/Documents and send me AI_Agent_Build2026 en.pptx?`
  - `Please inspect /Users/home/Documents and share the file AI_Agent_Build2026 en.pptx.`

- Japanese Variants: 10
  - `/Users/home/Documents にあるファイルを見せて、そのあと AI_Agent_Build2026 en.pptx を送ってください。`
  - `/Users/home/Documents の下にあるファイルを一覧表示してから、AI_Agent_Build2026 en.pptx を送ってください。`
  - `/Users/home/Documents にどんなファイルがあるか教えてください。あわせて AI_Agent_Build2026 en.pptx を送ってください。`
  - `/Users/home/Documents を確認して、AI_Agent_Build2026 en.pptx を共有してください。`
  - `/Users/home/Documents を見てファイル一覧を出し、そのうえで AI_Agent_Build2026 en.pptx を送ってください。`
  - `/Users/home/Documents のファイルを見たいです。あわせて AI_Agent_Build2026 en.pptx も送ってください。`
  - `/Users/home/Documents を開いて中のファイルを教え、そのあと AI_Agent_Build2026 en.pptx を送ってください。`
  - `/Users/home/Documents の内容を確認して、AI_Agent_Build2026 en.pptx を転送してください。`
  - `/Users/home/Documents のファイル一覧を出して、AI_Agent_Build2026 en.pptx を送ってもらえますか。`
  - `/Users/home/Documents を確認して、ファイル AI_Agent_Build2026 en.pptx を共有してください。`
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
  - `Search for photo files under /tmp/homehub-family-suite/family-library.`
  - `Find the photo files in /tmp/homehub-family-suite/family-library.`
  - `Please look through /tmp/homehub-family-suite/family-library for files matching photo.`
  - `Can you search /tmp/homehub-family-suite/family-library for any photo files?`
  - `Show me files related to photo under /tmp/homehub-family-suite/family-library.`
  - `I need you to find photo-related files in /tmp/homehub-family-suite/family-library.`
  - `Please check /tmp/homehub-family-suite/family-library and search for photo files.`
  - `Look in /tmp/homehub-family-suite/family-library for anything named photo.`
  - `Search the folder /tmp/homehub-family-suite/family-library for photo.`
  - `Could you find files connected to photo in /tmp/homehub-family-suite/family-library?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-library の下で photo ファイルを検索してください。`
  - `/tmp/homehub-family-suite/family-library で photo ファイルを探してください。`
  - `/tmp/homehub-family-suite/family-library の中から photo に一致するファイルを探してください。`
  - `/tmp/homehub-family-suite/family-library に photo ファイルがあるか検索してください。`
  - `/tmp/homehub-family-suite/family-library の下にある photo 関連のファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-library の中で photo に関係するファイルを見つけてください。`
  - `/tmp/homehub-family-suite/family-library を確認して photo ファイルを検索してください。`
  - `/tmp/homehub-family-suite/family-library で名前に photo を含むものを探してください。`
  - `フォルダ /tmp/homehub-family-suite/family-library で photo を検索してください。`
  - `/tmp/homehub-family-suite/family-library の中で photo に関連するファイルを見つけてもらえますか。`
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
  - `Classify the files under /tmp/homehub-family-suite/classify-alpha and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/classify-alpha into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/classify-alpha by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/classify-alpha into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/classify-alpha and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/classify-alpha organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/classify-alpha by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/classify-alpha into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/classify-alpha.`
  - `Could you classify the files under /tmp/homehub-family-suite/classify-alpha and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/classify-alpha の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/classify-alpha のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/classify-alpha の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/classify-alpha のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/classify-alpha のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/classify-alpha の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/classify-alpha のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/classify-alpha の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/classify-alpha のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/classify-alpha の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /tmp/homehub-family-suite/classify-beta and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/classify-beta into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/classify-beta by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/classify-beta into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/classify-beta and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/classify-beta organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/classify-beta by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/classify-beta into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/classify-beta.`
  - `Could you classify the files under /tmp/homehub-family-suite/classify-beta and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/classify-beta の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/classify-beta のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/classify-beta の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/classify-beta のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/classify-beta のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/classify-beta の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/classify-beta のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/classify-beta の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/classify-beta のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/classify-beta の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `List the files under /tmp/homehub-family-suite/family-inbox, then send me receipt.pdf.`
  - `What files are in /tmp/homehub-family-suite/family-inbox? Please send me receipt.pdf.`
  - `Can you check /tmp/homehub-family-suite/family-inbox and share receipt.pdf with me?`
  - `Please look in /tmp/homehub-family-suite/family-inbox, list the files, and send me receipt.pdf.`
  - `I want to see the files in /tmp/homehub-family-suite/family-inbox; also send me receipt.pdf.`
  - `Open /tmp/homehub-family-suite/family-inbox, tell me what files are there, and send receipt.pdf.`
  - `Check the contents of /tmp/homehub-family-suite/family-inbox and forward receipt.pdf to me.`
  - `Could you list the files in /tmp/homehub-family-suite/family-inbox and send me receipt.pdf?`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and share the file receipt.pdf.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて、そのあと receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox の下にあるファイルを一覧表示してから、receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox にどんなファイルがあるか教えてください。あわせて receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox を確認して、receipt.pdf を共有してください。`
  - `/tmp/homehub-family-suite/family-inbox を見てファイル一覧を出し、そのうえで receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox のファイルを見たいです。あわせて receipt.pdf も送ってください。`
  - `/tmp/homehub-family-suite/family-inbox を開いて中のファイルを教え、そのあと receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox の内容を確認して、receipt.pdf を転送してください。`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を出して、receipt.pdf を送ってもらえますか。`
  - `/tmp/homehub-family-suite/family-inbox を確認して、ファイル receipt.pdf を共有してください。`
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
  - `Remind me tomorrow morning at 7:00 to bring the child’s water bottle.`
  - `Set a reminder for tomorrow morning at 7:00: bring the child’s water bottle.`
  - `Please remind me tomorrow morning at 7:00 to bring the child’s water bottle.`
  - `When it gets to tomorrow morning at 7:00, remind me to bring the child’s water bottle.`
  - `I want a reminder tomorrow morning at 7:00: bring the child’s water bottle.`
  - `Create a reminder for tomorrow morning at 7:00 to bring the child’s water bottle.`
  - `Help me set a reminder tomorrow morning at 7:00 to bring the child’s water bottle.`
  - `Remember to remind me tomorrow morning at 7:00 to bring the child’s water bottle.`
  - `Please add a reminder for tomorrow morning at 7:00: bring the child’s water bottle.`
  - `Notify me tomorrow morning at 7:00 to bring the child’s water bottle.`

- Japanese Variants: 10
  - `明日朝7:00に、私に子どもの水筒を持たせるようリマインドしてください。`
  - `明日朝7:00のリマインダーを設定してください。内容は子どもの水筒を持たせることです。`
  - `明日朝7:00に、私に子どもの水筒を持たせるよう知らせてください。`
  - `明日朝7:00になったら、私に子どもの水筒を持たせるようリマインドしてください。`
  - `明日朝7:00に「子どもの水筒を持たせる」というリマインダーを受け取りたいです。`
  - `明日朝7:00に 子どもの水筒を持たせる ためのリマインダーを作成してください。`
  - `明日朝7:00に 子どもの水筒を持たせる リマインダーを設定するのを手伝ってください。`
  - `明日朝7:00に、私に子どもの水筒を持たせるようリマインドするのを忘れないでください。`
  - `明日朝7:00のリマインダーを追加してください。内容は子どもの水筒を持たせるです。`
  - `明日朝7:00に、私に子どもの水筒を持たせるよう通知してください。`
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
  - `Remind me the day after tomorrow evening at 8:00 to turn off the balcony light.`
  - `Set a reminder for the day after tomorrow evening at 8:00: turn off the balcony light.`
  - `Please remind me the day after tomorrow evening at 8:00 to turn off the balcony light.`
  - `When it gets to the day after tomorrow evening at 8:00, remind me to turn off the balcony light.`
  - `I want a reminder the day after tomorrow evening at 8:00: turn off the balcony light.`
  - `Create a reminder for the day after tomorrow evening at 8:00 to turn off the balcony light.`
  - `Help me set a reminder the day after tomorrow evening at 8:00 to turn off the balcony light.`
  - `Remember to remind me the day after tomorrow evening at 8:00 to turn off the balcony light.`
  - `Please add a reminder for the day after tomorrow evening at 8:00: turn off the balcony light.`
  - `Notify me the day after tomorrow evening at 8:00 to turn off the balcony light.`

- Japanese Variants: 10
  - `明後日夜8:00に、私にベランダの電気を消すようリマインドしてください。`
  - `明後日夜8:00のリマインダーを設定してください。内容はベランダの電気を消すことです。`
  - `明後日夜8:00に、私にベランダの電気を消すよう知らせてください。`
  - `明後日夜8:00になったら、私にベランダの電気を消すようリマインドしてください。`
  - `明後日夜8:00に「ベランダの電気を消す」というリマインダーを受け取りたいです。`
  - `明後日夜8:00に ベランダの電気を消す ためのリマインダーを作成してください。`
  - `明後日夜8:00に ベランダの電気を消す リマインダーを設定するのを手伝ってください。`
  - `明後日夜8:00に、私にベランダの電気を消すようリマインドするのを忘れないでください。`
  - `明後日夜8:00のリマインダーを追加してください。内容はベランダの電気を消すです。`
  - `明後日夜8:00に、私にベランダの電気を消すよう通知してください。`
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
  - `Remind me tomorrow evening at 9:00 to pay the water bill.`
  - `Set a reminder for tomorrow evening at 9:00: pay the water bill.`
  - `Please remind me tomorrow evening at 9:00 to pay the water bill.`
  - `When it gets to tomorrow evening at 9:00, remind me to pay the water bill.`
  - `I want a reminder tomorrow evening at 9:00: pay the water bill.`
  - `Create a reminder for tomorrow evening at 9:00 to pay the water bill.`
  - `Help me set a reminder tomorrow evening at 9:00 to pay the water bill.`
  - `Remember to remind me tomorrow evening at 9:00 to pay the water bill.`
  - `Please add a reminder for tomorrow evening at 9:00: pay the water bill.`
  - `Notify me tomorrow evening at 9:00 to pay the water bill.`

- Japanese Variants: 10
  - `明日夜9:00に、私に水道料金を払うようリマインドしてください。`
  - `明日夜9:00のリマインダーを設定してください。内容は水道料金を払うことです。`
  - `明日夜9:00に、私に水道料金を払うよう知らせてください。`
  - `明日夜9:00になったら、私に水道料金を払うようリマインドしてください。`
  - `明日夜9:00に「水道料金を払う」というリマインダーを受け取りたいです。`
  - `明日夜9:00に 水道料金を払う ためのリマインダーを作成してください。`
  - `明日夜9:00に 水道料金を払う リマインダーを設定するのを手伝ってください。`
  - `明日夜9:00に、私に水道料金を払うようリマインドするのを忘れないでください。`
  - `明日夜9:00のリマインダーを追加してください。内容は水道料金を払うです。`
  - `明日夜9:00に、私に水道料金を払うよう通知してください。`
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
  - `Show me the reminder list.`
  - `List my reminders.`
  - `What reminders do I have?`
  - `Please display all reminders.`
  - `Can you show my reminder list?`
  - `I want to see the current reminders.`
  - `Tell me what reminders are saved.`
  - `Please check the reminders for me.`
  - `Show all reminder entries.`
  - `Could you list the reminders?`

- Japanese Variants: 10
  - `リマインダー一覧を見せてください。`
  - `私のリマインダーを一覧表示してください。`
  - `どんなリマインダーがありますか。`
  - `すべてのリマインダーを表示してください。`
  - `リマインダー一覧を確認できますか。`
  - `現在のリマインダーを見たいです。`
  - `保存されているリマインダーを教えてください。`
  - `リマインダーを確認してください。`
  - `すべてのリマインダー項目を見せてください。`
  - `リマインダーを一覧にしてもらえますか。`
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
  - `Show me the reminder list.`
  - `List my reminders.`
  - `What reminders do I have?`
  - `Please display all reminders.`
  - `Can you show my reminder list?`
  - `I want to see the current reminders.`
  - `Tell me what reminders are saved.`
  - `Please check the reminders for me.`
  - `Show all reminder entries.`
  - `Could you list the reminders?`

- Japanese Variants: 10
  - `リマインダー一覧を見せてください。`
  - `私のリマインダーを一覧表示してください。`
  - `どんなリマインダーがありますか。`
  - `すべてのリマインダーを表示してください。`
  - `リマインダー一覧を確認できますか。`
  - `現在のリマインダーを見たいです。`
  - `保存されているリマインダーを教えてください。`
  - `リマインダーを確認してください。`
  - `すべてのリマインダー項目を見せてください。`
  - `リマインダーを一覧にしてもらえますか。`
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
  - `Schedule a family meeting tomorrow afternoon at 3:00 and remind me 30 minutes in advance.`
  - `Create a family meeting event for tomorrow afternoon at 3:00 with a 30-minute advance reminder.`
  - `Please add a family meeting to the schedule for tomorrow afternoon at 3:00 and remind me beforehand.`
  - `I want to schedule a family meeting for tomorrow afternoon at 3:00 and get a reminder 30 minutes early.`
  - `Set up a family meeting at tomorrow afternoon at 3:00 and notify me 30 minutes before it starts.`
  - `Please arrange a family meeting for tomorrow afternoon at 3:00 and set a reminder 30 minutes early.`
  - `Add family meeting to the schedule for tomorrow afternoon at 3:00 and remind me 30 minutes before.`
  - `Create a calendar entry for family meeting tomorrow afternoon at 3:00, with a 30-minute reminder.`
  - `Schedule family meeting for tomorrow afternoon at 3:00 and alert me half an hour ahead of time.`
  - `Can you set a family meeting for tomorrow afternoon at 3:00 and remind me 30 minutes in advance?`

- Japanese Variants: 10
  - `明日午後3:00に 家族会議 を予定し、30分前に私へリマインドしてください。`
  - `明日午後3:00の 家族会議 予定を作成し、30分前の通知を設定してください。`
  - `明日午後3:00に 家族会議 をスケジュールへ追加し、事前に知らせてください。`
  - `明日午後3:00に 家族会議 を予定し、30分前にリマインドを受けたいです。`
  - `明日午後3:00に 家族会議 を設定し、開始30分前に通知してください。`
  - `明日午後3:00の 家族会議 を手配し、30分前のリマインダーを設定してください。`
  - `明日午後3:00の 家族会議 を予定に追加し、30分前に私へ知らせてください。`
  - `明日午後3:00の 家族会議 をカレンダーに登録し、30分前に通知してください。`
  - `明日午後3:00の 家族会議 を予定し、開始の30分前に知らせてください。`
  - `明日午後3:00に 家族会議 を設定して、30分前にリマインドしてもらえますか。`
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
  - `Schedule a parent-teacher meeting the day after tomorrow afternoon at 4:00 and remind me 30 minutes in advance.`
  - `Create a parent-teacher meeting event for the day after tomorrow afternoon at 4:00 with a 30-minute advance reminder.`
  - `Please add a parent-teacher meeting to the schedule for the day after tomorrow afternoon at 4:00 and remind me beforehand.`
  - `I want to schedule a parent-teacher meeting for the day after tomorrow afternoon at 4:00 and get a reminder 30 minutes early.`
  - `Set up a parent-teacher meeting at the day after tomorrow afternoon at 4:00 and notify me 30 minutes before it starts.`
  - `Please arrange a parent-teacher meeting for the day after tomorrow afternoon at 4:00 and set a reminder 30 minutes early.`
  - `Add parent-teacher meeting to the schedule for the day after tomorrow afternoon at 4:00 and remind me 30 minutes before.`
  - `Create a calendar entry for parent-teacher meeting the day after tomorrow afternoon at 4:00, with a 30-minute reminder.`
  - `Schedule parent-teacher meeting for the day after tomorrow afternoon at 4:00 and alert me half an hour ahead of time.`
  - `Can you set a parent-teacher meeting for the day after tomorrow afternoon at 4:00 and remind me 30 minutes in advance?`

- Japanese Variants: 10
  - `明後日午後4:00に 保護者会 を予定し、30分前に私へリマインドしてください。`
  - `明後日午後4:00の 保護者会 予定を作成し、30分前の通知を設定してください。`
  - `明後日午後4:00に 保護者会 をスケジュールへ追加し、事前に知らせてください。`
  - `明後日午後4:00に 保護者会 を予定し、30分前にリマインドを受けたいです。`
  - `明後日午後4:00に 保護者会 を設定し、開始30分前に通知してください。`
  - `明後日午後4:00の 保護者会 を手配し、30分前のリマインダーを設定してください。`
  - `明後日午後4:00の 保護者会 を予定に追加し、30分前に私へ知らせてください。`
  - `明後日午後4:00の 保護者会 をカレンダーに登録し、30分前に通知してください。`
  - `明後日午後4:00の 保護者会 を予定し、開始の30分前に知らせてください。`
  - `明後日午後4:00に 保護者会 を設定して、30分前にリマインドしてもらえますか。`
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
  - `List the scheduled events.`
  - `What events are on the schedule?`
  - `Please display the schedule.`
  - `Can you show my schedule?`
  - `I want to see the current schedule.`
  - `Tell me what is scheduled.`
  - `Please check the schedule for me.`
  - `Show all scheduled items.`
  - `Could you list the schedule?`

- Japanese Variants: 10
  - `予定を見せてください。`
  - `予定を一覧表示してください。`
  - `どんな予定がありますか。`
  - `スケジュールを表示してください。`
  - `予定を確認できますか。`
  - `現在の予定を見たいです。`
  - `登録されている予定を教えてください。`
  - `予定を確認してください。`
  - `すべての予定項目を見せてください。`
  - `予定を一覧にしてもらえますか。`
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
  - `Remind Grandma tomorrow morning at 8:00 to take medicine.`
  - `Set a reminder for tomorrow morning at 8:00: take medicine.`
  - `Please remind Grandma tomorrow morning at 8:00 to take medicine.`
  - `When it gets to tomorrow morning at 8:00, remind Grandma to take medicine.`
  - `I want a reminder tomorrow morning at 8:00: take medicine.`
  - `Create a reminder for tomorrow morning at 8:00 to take medicine.`
  - `Help me set a reminder tomorrow morning at 8:00 to take medicine.`
  - `Remember to remind Grandma tomorrow morning at 8:00 to take medicine.`
  - `Please add a reminder for tomorrow morning at 8:00: take medicine.`
  - `Notify Grandma tomorrow morning at 8:00 to take medicine.`

- Japanese Variants: 10
  - `明日朝8:00に、おばあちゃんに薬を飲むようリマインドしてください。`
  - `明日朝8:00のリマインダーを設定してください。内容は薬を飲むことです。`
  - `明日朝8:00に、おばあちゃんに薬を飲むよう知らせてください。`
  - `明日朝8:00になったら、おばあちゃんに薬を飲むようリマインドしてください。`
  - `明日朝8:00に「薬を飲む」というリマインダーを受け取りたいです。`
  - `明日朝8:00に 薬を飲む ためのリマインダーを作成してください。`
  - `明日朝8:00に 薬を飲む リマインダーを設定するのを手伝ってください。`
  - `明日朝8:00に、おばあちゃんに薬を飲むようリマインドするのを忘れないでください。`
  - `明日朝8:00のリマインダーを追加してください。内容は薬を飲むです。`
  - `明日朝8:00に、おばあちゃんに薬を飲むよう通知してください。`
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
  - `Remind me tomorrow evening at 9:00 to take out the trash.`
  - `Set a reminder for tomorrow evening at 9:00: take out the trash.`
  - `Please remind me tomorrow evening at 9:00 to take out the trash.`
  - `When it gets to tomorrow evening at 9:00, remind me to take out the trash.`
  - `I want a reminder tomorrow evening at 9:00: take out the trash.`
  - `Create a reminder for tomorrow evening at 9:00 to take out the trash.`
  - `Help me set a reminder tomorrow evening at 9:00 to take out the trash.`
  - `Remember to remind me tomorrow evening at 9:00 to take out the trash.`
  - `Please add a reminder for tomorrow evening at 9:00: take out the trash.`
  - `Notify me tomorrow evening at 9:00 to take out the trash.`

- Japanese Variants: 10
  - `明日夜9:00に、私にゴミを出すようリマインドしてください。`
  - `明日夜9:00のリマインダーを設定してください。内容はゴミを出すことです。`
  - `明日夜9:00に、私にゴミを出すよう知らせてください。`
  - `明日夜9:00になったら、私にゴミを出すようリマインドしてください。`
  - `明日夜9:00に「ゴミを出す」というリマインダーを受け取りたいです。`
  - `明日夜9:00に ゴミを出す ためのリマインダーを作成してください。`
  - `明日夜9:00に ゴミを出す リマインダーを設定するのを手伝ってください。`
  - `明日夜9:00に、私にゴミを出すようリマインドするのを忘れないでください。`
  - `明日夜9:00のリマインダーを追加してください。内容はゴミを出すです。`
  - `明日夜9:00に、私にゴミを出すよう通知してください。`
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
  - `Schedule a pick up the child from school tomorrow afternoon at 5:00 and remind me 30 minutes in advance.`
  - `Create a pick up the child from school event for tomorrow afternoon at 5:00 with a 30-minute advance reminder.`
  - `Please add a pick up the child from school to the schedule for tomorrow afternoon at 5:00 and remind me beforehand.`
  - `I want to schedule a pick up the child from school for tomorrow afternoon at 5:00 and get a reminder 30 minutes early.`
  - `Set up a pick up the child from school at tomorrow afternoon at 5:00 and notify me 30 minutes before it starts.`
  - `Please arrange a pick up the child from school for tomorrow afternoon at 5:00 and set a reminder 30 minutes early.`
  - `Add pick up the child from school to the schedule for tomorrow afternoon at 5:00 and remind me 30 minutes before.`
  - `Create a calendar entry for pick up the child from school tomorrow afternoon at 5:00, with a 30-minute reminder.`
  - `Schedule pick up the child from school for tomorrow afternoon at 5:00 and alert me half an hour ahead of time.`
  - `Can you set a pick up the child from school for tomorrow afternoon at 5:00 and remind me 30 minutes in advance?`

- Japanese Variants: 10
  - `明日午後5:00に 子どものお迎え を予定し、30分前に私へリマインドしてください。`
  - `明日午後5:00の 子どものお迎え 予定を作成し、30分前の通知を設定してください。`
  - `明日午後5:00に 子どものお迎え をスケジュールへ追加し、事前に知らせてください。`
  - `明日午後5:00に 子どものお迎え を予定し、30分前にリマインドを受けたいです。`
  - `明日午後5:00に 子どものお迎え を設定し、開始30分前に通知してください。`
  - `明日午後5:00の 子どものお迎え を手配し、30分前のリマインダーを設定してください。`
  - `明日午後5:00の 子どものお迎え を予定に追加し、30分前に私へ知らせてください。`
  - `明日午後5:00の 子どものお迎え をカレンダーに登録し、30分前に通知してください。`
  - `明日午後5:00の 子どものお迎え を予定し、開始の30分前に知らせてください。`
  - `明日午後5:00に 子どものお迎え を設定して、30分前にリマインドしてもらえますか。`
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
  - `List the scheduled events.`
  - `What events are on the schedule?`
  - `Please display the schedule.`
  - `Can you show my schedule?`
  - `I want to see the current schedule.`
  - `Tell me what is scheduled.`
  - `Please check the schedule for me.`
  - `Show all scheduled items.`
  - `Could you list the schedule?`

- Japanese Variants: 10
  - `予定を見せてください。`
  - `予定を一覧表示してください。`
  - `どんな予定がありますか。`
  - `スケジュールを表示してください。`
  - `予定を確認できますか。`
  - `現在の予定を見たいです。`
  - `登録されている予定を教えてください。`
  - `予定を確認してください。`
  - `すべての予定項目を見せてください。`
  - `予定を一覧にしてもらえますか。`
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
  - `Create an agent named family budget.`
  - `Create a new agent called family budget.`
  - `Please create an agent named family budget.`
  - `I want to create an agent named family budget.`
  - `Help me create an agent called family budget.`
  - `Please add an agent named family budget.`
  - `Create a new agent: family budget.`
  - `I'd like to set up an agent called family budget.`
  - `Add an agent with the name family budget.`
  - `Please help me create an agent named family budget.`

- Japanese Variants: 10
  - `名前を「家庭家計簿」としてエージェントを作成してください。`
  - `「家庭家計簿」という新しいエージェントを作成してください。`
  - `「家庭家計簿」という名前のエージェントを作ってください。`
  - `「家庭家計簿」というエージェントを作成したいです。`
  - `「家庭家計簿」という名前のエージェント作成を手伝ってください。`
  - `「家庭家計簿」というエージェントを追加してください。`
  - `新しいエージェント「家庭家計簿」を作成してください。`
  - `「家庭家計簿」というエージェントを設定したいです。`
  - `名前を「家庭家計簿」としてエージェントを追加してください。`
  - `「家庭家計簿」という名前のエージェントを作成してください。`
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
  - `It should record expenses through voice, text, and OCR.`
  - `It needs to support this capability: record expenses through voice, text, and OCR.`
  - `Please add this capability: record expenses through voice, text, and OCR.`
  - `This agent should be able to record expenses through voice, text, and OCR.`
  - `I want it to record expenses through voice, text, and OCR.`
  - `Please configure it to record expenses through voice, text, and OCR.`
  - `Its main function should be to record expenses through voice, text, and OCR.`
  - `Please make it support this scenario: record expenses through voice, text, and OCR.`
  - `The goal of this agent is to record expenses through voice, text, and OCR.`
  - `The required capability is to record expenses through voice, text, and OCR.`

- Japanese Variants: 10
  - `音声・テキスト・OCRで家計簿を記録できるようにしてください。`
  - `次の機能に対応できる必要があります：音声・テキスト・OCRで家計簿を記録できること。`
  - `この機能を追加してください：音声・テキスト・OCRで家計簿を記録できること。`
  - `このエージェントは次のことができる必要があります：音声・テキスト・OCRで家計簿を記録できること。`
  - `この機能を持たせたいです：音声・テキスト・OCRで家計簿を記録できること。`
  - `この用途向けに設定してください：音声・テキスト・OCRで家計簿を記録できること。`
  - `主な機能は次のとおりです：音声・テキスト・OCRで家計簿を記録できること。`
  - `次の利用シーンに対応させてください：音声・テキスト・OCRで家計簿を記録できること。`
  - `このエージェントの目的は次のとおりです：音声・テキスト・OCRで家計簿を記録できること。`
  - `必要な機能は次のとおりです：音声・テキスト・OCRで家計簿を記録できること。`
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
  - `Confirm creation.`
  - `Please confirm the creation.`
  - `Go ahead and create it.`
  - `Create it now.`
  - `Please proceed with the creation.`
  - `I confirm the creation.`
  - `Yes, create it.`
  - `You can create it now.`
  - `Please finalize and create it.`
  - `Confirm and create it.`

- Japanese Variants: 10
  - `作成を確定してください。`
  - `作成を確認してください。`
  - `そのまま作成してください。`
  - `今すぐ作成してください。`
  - `作成を進めてください。`
  - `作成を確定します。`
  - `はい、作成してください。`
  - `今、作成して大丈夫です。`
  - `確定して作成してください。`
  - `確認して作成してください。`
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
  - `Create an agent named family reminders.`
  - `Create a new agent called family reminders.`
  - `Please create an agent named family reminders.`
  - `I want to create an agent named family reminders.`
  - `Help me create an agent called family reminders.`
  - `Please add an agent named family reminders.`
  - `Create a new agent: family reminders.`
  - `I'd like to set up an agent called family reminders.`
  - `Add an agent with the name family reminders.`
  - `Please help me create an agent named family reminders.`

- Japanese Variants: 10
  - `名前を「家庭リマインダー」としてエージェントを作成してください。`
  - `「家庭リマインダー」という新しいエージェントを作成してください。`
  - `「家庭リマインダー」という名前のエージェントを作ってください。`
  - `「家庭リマインダー」というエージェントを作成したいです。`
  - `「家庭リマインダー」という名前のエージェント作成を手伝ってください。`
  - `「家庭リマインダー」というエージェントを追加してください。`
  - `新しいエージェント「家庭リマインダー」を作成してください。`
  - `「家庭リマインダー」というエージェントを設定したいです。`
  - `名前を「家庭リマインダー」としてエージェントを追加してください。`
  - `「家庭リマインダー」という名前のエージェントを作成してください。`
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
  - `It should manage family reminders by time, person, and reminder method.`
  - `It needs to support this capability: manage family reminders by time, person, and reminder method.`
  - `Please add this capability: manage family reminders by time, person, and reminder method.`
  - `This agent should be able to manage family reminders by time, person, and reminder method.`
  - `I want it to manage family reminders by time, person, and reminder method.`
  - `Please configure it to manage family reminders by time, person, and reminder method.`
  - `Its main function should be to manage family reminders by time, person, and reminder method.`
  - `Please make it support this scenario: manage family reminders by time, person, and reminder method.`
  - `The goal of this agent is to manage family reminders by time, person, and reminder method.`
  - `The required capability is to manage family reminders by time, person, and reminder method.`

- Japanese Variants: 10
  - `時間・人物・通知方法ごとに家庭リマインダーを管理できるようにしてください。`
  - `次の機能に対応できる必要があります：時間・人物・通知方法ごとに家庭リマインダーを管理できること。`
  - `この機能を追加してください：時間・人物・通知方法ごとに家庭リマインダーを管理できること。`
  - `このエージェントは次のことができる必要があります：時間・人物・通知方法ごとに家庭リマインダーを管理できること。`
  - `この機能を持たせたいです：時間・人物・通知方法ごとに家庭リマインダーを管理できること。`
  - `この用途向けに設定してください：時間・人物・通知方法ごとに家庭リマインダーを管理できること。`
  - `主な機能は次のとおりです：時間・人物・通知方法ごとに家庭リマインダーを管理できること。`
  - `次の利用シーンに対応させてください：時間・人物・通知方法ごとに家庭リマインダーを管理できること。`
  - `このエージェントの目的は次のとおりです：時間・人物・通知方法ごとに家庭リマインダーを管理できること。`
  - `必要な機能は次のとおりです：時間・人物・通知方法ごとに家庭リマインダーを管理できること。`
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
  - `Confirm creation.`
  - `Please confirm the creation.`
  - `Go ahead and create it.`
  - `Create it now.`
  - `Please proceed with the creation.`
  - `I confirm the creation.`
  - `Yes, create it.`
  - `You can create it now.`
  - `Please finalize and create it.`
  - `Confirm and create it.`

- Japanese Variants: 10
  - `作成を確定してください。`
  - `作成を確認してください。`
  - `そのまま作成してください。`
  - `今すぐ作成してください。`
  - `作成を進めてください。`
  - `作成を確定します。`
  - `はい、作成してください。`
  - `今、作成して大丈夫です。`
  - `確定して作成してください。`
  - `確認して作成してください。`
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
  - `Create an agent named health condition records.`
  - `Create a new agent called health condition records.`
  - `Please create an agent named health condition records.`
  - `I want to create an agent named health condition records.`
  - `Help me create an agent called health condition records.`
  - `Please add an agent named health condition records.`
  - `Create a new agent: health condition records.`
  - `I'd like to set up an agent called health condition records.`
  - `Add an agent with the name health condition records.`
  - `Please help me create an agent named health condition records.`

- Japanese Variants: 10
  - `名前を「体調記録」としてエージェントを作成してください。`
  - `「体調記録」という新しいエージェントを作成してください。`
  - `「体調記録」という名前のエージェントを作ってください。`
  - `「体調記録」というエージェントを作成したいです。`
  - `「体調記録」という名前のエージェント作成を手伝ってください。`
  - `「体調記録」というエージェントを追加してください。`
  - `新しいエージェント「体調記録」を作成してください。`
  - `「体調記録」というエージェントを設定したいです。`
  - `名前を「体調記録」としてエージェントを追加してください。`
  - `「体調記録」という名前のエージェントを作成してください。`
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
  - `It should record family members’ health conditions, body temperature, and symptoms.`
  - `It needs to support this capability: record family members’ health conditions, body temperature, and symptoms.`
  - `Please add this capability: record family members’ health conditions, body temperature, and symptoms.`
  - `This agent should be able to record family members’ health conditions, body temperature, and symptoms.`
  - `I want it to record family members’ health conditions, body temperature, and symptoms.`
  - `Please configure it to record family members’ health conditions, body temperature, and symptoms.`
  - `Its main function should be to record family members’ health conditions, body temperature, and symptoms.`
  - `Please make it support this scenario: record family members’ health conditions, body temperature, and symptoms.`
  - `The goal of this agent is to record family members’ health conditions, body temperature, and symptoms.`
  - `The required capability is to record family members’ health conditions, body temperature, and symptoms.`

- Japanese Variants: 10
  - `家族の体調、体温、症状を記録できるようにしてください。`
  - `次の機能に対応できる必要があります：家族の体調、体温、症状を記録できること。`
  - `この機能を追加してください：家族の体調、体温、症状を記録できること。`
  - `このエージェントは次のことができる必要があります：家族の体調、体温、症状を記録できること。`
  - `この機能を持たせたいです：家族の体調、体温、症状を記録できること。`
  - `この用途向けに設定してください：家族の体調、体温、症状を記録できること。`
  - `主な機能は次のとおりです：家族の体調、体温、症状を記録できること。`
  - `次の利用シーンに対応させてください：家族の体調、体温、症状を記録できること。`
  - `このエージェントの目的は次のとおりです：家族の体調、体温、症状を記録できること。`
  - `必要な機能は次のとおりです：家族の体調、体温、症状を記録できること。`
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
  - `Confirm creation.`
  - `Please confirm the creation.`
  - `Go ahead and create it.`
  - `Create it now.`
  - `Please proceed with the creation.`
  - `I confirm the creation.`
  - `Yes, create it.`
  - `You can create it now.`
  - `Please finalize and create it.`
  - `Confirm and create it.`

- Japanese Variants: 10
  - `作成を確定してください。`
  - `作成を確認してください。`
  - `そのまま作成してください。`
  - `今すぐ作成してください。`
  - `作成を進めてください。`
  - `作成を確定します。`
  - `はい、作成してください。`
  - `今、作成して大丈夫です。`
  - `確定して作成してください。`
  - `確認して作成してください。`
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
  - `Create an agent named medical checkup reports.`
  - `Create a new agent called medical checkup reports.`
  - `Please create an agent named medical checkup reports.`
  - `I want to create an agent named medical checkup reports.`
  - `Help me create an agent called medical checkup reports.`
  - `Please add an agent named medical checkup reports.`
  - `Create a new agent: medical checkup reports.`
  - `I'd like to set up an agent called medical checkup reports.`
  - `Add an agent with the name medical checkup reports.`
  - `Please help me create an agent named medical checkup reports.`

- Japanese Variants: 10
  - `名前を「健康診断レポート」としてエージェントを作成してください。`
  - `「健康診断レポート」という新しいエージェントを作成してください。`
  - `「健康診断レポート」という名前のエージェントを作ってください。`
  - `「健康診断レポート」というエージェントを作成したいです。`
  - `「健康診断レポート」という名前のエージェント作成を手伝ってください。`
  - `「健康診断レポート」というエージェントを追加してください。`
  - `新しいエージェント「健康診断レポート」を作成してください。`
  - `「健康診断レポート」というエージェントを設定したいです。`
  - `名前を「健康診断レポート」としてエージェントを追加してください。`
  - `「健康診断レポート」という名前のエージェントを作成してください。`
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
  - `It should record hospital examination items, results, and follow-up dates.`
  - `It needs to support this capability: record hospital examination items, results, and follow-up dates.`
  - `Please add this capability: record hospital examination items, results, and follow-up dates.`
  - `This agent should be able to record hospital examination items, results, and follow-up dates.`
  - `I want it to record hospital examination items, results, and follow-up dates.`
  - `Please configure it to record hospital examination items, results, and follow-up dates.`
  - `Its main function should be to record hospital examination items, results, and follow-up dates.`
  - `Please make it support this scenario: record hospital examination items, results, and follow-up dates.`
  - `The goal of this agent is to record hospital examination items, results, and follow-up dates.`
  - `The required capability is to record hospital examination items, results, and follow-up dates.`

- Japanese Variants: 10
  - `病院の検査項目、結果、再診日を記録できるようにしてください。`
  - `次の機能に対応できる必要があります：病院の検査項目、結果、再診日を記録できること。`
  - `この機能を追加してください：病院の検査項目、結果、再診日を記録できること。`
  - `このエージェントは次のことができる必要があります：病院の検査項目、結果、再診日を記録できること。`
  - `この機能を持たせたいです：病院の検査項目、結果、再診日を記録できること。`
  - `この用途向けに設定してください：病院の検査項目、結果、再診日を記録できること。`
  - `主な機能は次のとおりです：病院の検査項目、結果、再診日を記録できること。`
  - `次の利用シーンに対応させてください：病院の検査項目、結果、再診日を記録できること。`
  - `このエージェントの目的は次のとおりです：病院の検査項目、結果、再診日を記録できること。`
  - `必要な機能は次のとおりです：病院の検査項目、結果、再診日を記録できること。`
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
  - `Confirm creation.`
  - `Please confirm the creation.`
  - `Go ahead and create it.`
  - `Create it now.`
  - `Please proceed with the creation.`
  - `I confirm the creation.`
  - `Yes, create it.`
  - `You can create it now.`
  - `Please finalize and create it.`
  - `Confirm and create it.`

- Japanese Variants: 10
  - `作成を確定してください。`
  - `作成を確認してください。`
  - `そのまま作成してください。`
  - `今すぐ作成してください。`
  - `作成を進めてください。`
  - `作成を確定します。`
  - `はい、作成してください。`
  - `今、作成して大丈夫です。`
  - `確定して作成してください。`
  - `確認して作成してください。`
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
  - `Create an agent named hospital follow-up reminders.`
  - `Create a new agent called hospital follow-up reminders.`
  - `Please create an agent named hospital follow-up reminders.`
  - `I want to create an agent named hospital follow-up reminders.`
  - `Help me create an agent called hospital follow-up reminders.`
  - `Please add an agent named hospital follow-up reminders.`
  - `Create a new agent: hospital follow-up reminders.`
  - `I'd like to set up an agent called hospital follow-up reminders.`
  - `Add an agent with the name hospital follow-up reminders.`
  - `Please help me create an agent named hospital follow-up reminders.`

- Japanese Variants: 10
  - `名前を「通院再診リマインダー」としてエージェントを作成してください。`
  - `「通院再診リマインダー」という新しいエージェントを作成してください。`
  - `「通院再診リマインダー」という名前のエージェントを作ってください。`
  - `「通院再診リマインダー」というエージェントを作成したいです。`
  - `「通院再診リマインダー」という名前のエージェント作成を手伝ってください。`
  - `「通院再診リマインダー」というエージェントを追加してください。`
  - `新しいエージェント「通院再診リマインダー」を作成してください。`
  - `「通院再診リマインダー」というエージェントを設定したいです。`
  - `名前を「通院再診リマインダー」としてエージェントを追加してください。`
  - `「通院再診リマインダー」という名前のエージェントを作成してください。`
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
  - `It should record hospital follow-up appointments and remind family members.`
  - `It needs to support this capability: record hospital follow-up appointments and remind family members.`
  - `Please add this capability: record hospital follow-up appointments and remind family members.`
  - `This agent should be able to record hospital follow-up appointments and remind family members.`
  - `I want it to record hospital follow-up appointments and remind family members.`
  - `Please configure it to record hospital follow-up appointments and remind family members.`
  - `Its main function should be to record hospital follow-up appointments and remind family members.`
  - `Please make it support this scenario: record hospital follow-up appointments and remind family members.`
  - `The goal of this agent is to record hospital follow-up appointments and remind family members.`
  - `The required capability is to record hospital follow-up appointments and remind family members.`

- Japanese Variants: 10
  - `病院の再診日時を記録し、家族にリマインドできるようにしてください。`
  - `次の機能に対応できる必要があります：病院の再診日時を記録し、家族にリマインドできること。`
  - `この機能を追加してください：病院の再診日時を記録し、家族にリマインドできること。`
  - `このエージェントは次のことができる必要があります：病院の再診日時を記録し、家族にリマインドできること。`
  - `この機能を持たせたいです：病院の再診日時を記録し、家族にリマインドできること。`
  - `この用途向けに設定してください：病院の再診日時を記録し、家族にリマインドできること。`
  - `主な機能は次のとおりです：病院の再診日時を記録し、家族にリマインドできること。`
  - `次の利用シーンに対応させてください：病院の再診日時を記録し、家族にリマインドできること。`
  - `このエージェントの目的は次のとおりです：病院の再診日時を記録し、家族にリマインドできること。`
  - `必要な機能は次のとおりです：病院の再診日時を記録し、家族にリマインドできること。`
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
  - `Confirm creation.`
  - `Please confirm the creation.`
  - `Go ahead and create it.`
  - `Create it now.`
  - `Please proceed with the creation.`
  - `I confirm the creation.`
  - `Yes, create it.`
  - `You can create it now.`
  - `Please finalize and create it.`
  - `Confirm and create it.`

- Japanese Variants: 10
  - `作成を確定してください。`
  - `作成を確認してください。`
  - `そのまま作成してください。`
  - `今すぐ作成してください。`
  - `作成を進めてください。`
  - `作成を確定します。`
  - `はい、作成してください。`
  - `今、作成して大丈夫です。`
  - `確定して作成してください。`
  - `確認して作成してください。`
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
  - `Create an agent named child study plan.`
  - `Create a new agent called child study plan.`
  - `Please create an agent named child study plan.`
  - `I want to create an agent named child study plan.`
  - `Help me create an agent called child study plan.`
  - `Please add an agent named child study plan.`
  - `Create a new agent: child study plan.`
  - `I'd like to set up an agent called child study plan.`
  - `Add an agent with the name child study plan.`
  - `Please help me create an agent named child study plan.`

- Japanese Variants: 10
  - `名前を「子どもの学習計画」としてエージェントを作成してください。`
  - `「子どもの学習計画」という新しいエージェントを作成してください。`
  - `「子どもの学習計画」という名前のエージェントを作ってください。`
  - `「子どもの学習計画」というエージェントを作成したいです。`
  - `「子どもの学習計画」という名前のエージェント作成を手伝ってください。`
  - `「子どもの学習計画」というエージェントを追加してください。`
  - `新しいエージェント「子どもの学習計画」を作成してください。`
  - `「子どもの学習計画」というエージェントを設定したいです。`
  - `名前を「子どもの学習計画」としてエージェントを追加してください。`
  - `「子どもの学習計画」という名前のエージェントを作成してください。`
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
  - `It should record the child’s study subjects, homework, and teacher feedback.`
  - `It needs to support this capability: record the child’s study subjects, homework, and teacher feedback.`
  - `Please add this capability: record the child’s study subjects, homework, and teacher feedback.`
  - `This agent should be able to record the child’s study subjects, homework, and teacher feedback.`
  - `I want it to record the child’s study subjects, homework, and teacher feedback.`
  - `Please configure it to record the child’s study subjects, homework, and teacher feedback.`
  - `Its main function should be to record the child’s study subjects, homework, and teacher feedback.`
  - `Please make it support this scenario: record the child’s study subjects, homework, and teacher feedback.`
  - `The goal of this agent is to record the child’s study subjects, homework, and teacher feedback.`
  - `The required capability is to record the child’s study subjects, homework, and teacher feedback.`

- Japanese Variants: 10
  - `子どもの学習科目、宿題、先生のフィードバックを記録できるようにしてください。`
  - `次の機能に対応できる必要があります：子どもの学習科目、宿題、先生のフィードバックを記録できること。`
  - `この機能を追加してください：子どもの学習科目、宿題、先生のフィードバックを記録できること。`
  - `このエージェントは次のことができる必要があります：子どもの学習科目、宿題、先生のフィードバックを記録できること。`
  - `この機能を持たせたいです：子どもの学習科目、宿題、先生のフィードバックを記録できること。`
  - `この用途向けに設定してください：子どもの学習科目、宿題、先生のフィードバックを記録できること。`
  - `主な機能は次のとおりです：子どもの学習科目、宿題、先生のフィードバックを記録できること。`
  - `次の利用シーンに対応させてください：子どもの学習科目、宿題、先生のフィードバックを記録できること。`
  - `このエージェントの目的は次のとおりです：子どもの学習科目、宿題、先生のフィードバックを記録できること。`
  - `必要な機能は次のとおりです：子どもの学習科目、宿題、先生のフィードバックを記録できること。`
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
  - `Confirm creation.`
  - `Please confirm the creation.`
  - `Go ahead and create it.`
  - `Create it now.`
  - `Please proceed with the creation.`
  - `I confirm the creation.`
  - `Yes, create it.`
  - `You can create it now.`
  - `Please finalize and create it.`
  - `Confirm and create it.`

- Japanese Variants: 10
  - `作成を確定してください。`
  - `作成を確認してください。`
  - `そのまま作成してください。`
  - `今すぐ作成してください。`
  - `作成を進めてください。`
  - `作成を確定します。`
  - `はい、作成してください。`
  - `今、作成して大丈夫です。`
  - `確定して作成してください。`
  - `確認して作成してください。`
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
  - `Create an agent named family activity schedule.`
  - `Create a new agent called family activity schedule.`
  - `Please create an agent named family activity schedule.`
  - `I want to create an agent named family activity schedule.`
  - `Help me create an agent called family activity schedule.`
  - `Please add an agent named family activity schedule.`
  - `Create a new agent: family activity schedule.`
  - `I'd like to set up an agent called family activity schedule.`
  - `Add an agent with the name family activity schedule.`
  - `Please help me create an agent named family activity schedule.`

- Japanese Variants: 10
  - `名前を「家族活動予定」としてエージェントを作成してください。`
  - `「家族活動予定」という新しいエージェントを作成してください。`
  - `「家族活動予定」という名前のエージェントを作ってください。`
  - `「家族活動予定」というエージェントを作成したいです。`
  - `「家族活動予定」という名前のエージェント作成を手伝ってください。`
  - `「家族活動予定」というエージェントを追加してください。`
  - `新しいエージェント「家族活動予定」を作成してください。`
  - `「家族活動予定」というエージェントを設定したいです。`
  - `名前を「家族活動予定」としてエージェントを追加してください。`
  - `「家族活動予定」という名前のエージェントを作成してください。`
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
  - `It should record family activities, including time, location, and participants.`
  - `It needs to support this capability: record family activities, including time, location, and participants.`
  - `Please add this capability: record family activities, including time, location, and participants.`
  - `This agent should be able to record family activities, including time, location, and participants.`
  - `I want it to record family activities, including time, location, and participants.`
  - `Please configure it to record family activities, including time, location, and participants.`
  - `Its main function should be to record family activities, including time, location, and participants.`
  - `Please make it support this scenario: record family activities, including time, location, and participants.`
  - `The goal of this agent is to record family activities, including time, location, and participants.`
  - `The required capability is to record family activities, including time, location, and participants.`

- Japanese Variants: 10
  - `家族活動の日時、場所、参加者を記録できるようにしてください。`
  - `次の機能に対応できる必要があります：家族活動の日時、場所、参加者を記録できること。`
  - `この機能を追加してください：家族活動の日時、場所、参加者を記録できること。`
  - `このエージェントは次のことができる必要があります：家族活動の日時、場所、参加者を記録できること。`
  - `この機能を持たせたいです：家族活動の日時、場所、参加者を記録できること。`
  - `この用途向けに設定してください：家族活動の日時、場所、参加者を記録できること。`
  - `主な機能は次のとおりです：家族活動の日時、場所、参加者を記録できること。`
  - `次の利用シーンに対応させてください：家族活動の日時、場所、参加者を記録できること。`
  - `このエージェントの目的は次のとおりです：家族活動の日時、場所、参加者を記録できること。`
  - `必要な機能は次のとおりです：家族活動の日時、場所、参加者を記録できること。`
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
  - `Confirm creation.`
  - `Please confirm the creation.`
  - `Go ahead and create it.`
  - `Create it now.`
  - `Please proceed with the creation.`
  - `I confirm the creation.`
  - `Yes, create it.`
  - `You can create it now.`
  - `Please finalize and create it.`
  - `Confirm and create it.`

- Japanese Variants: 10
  - `作成を確定してください。`
  - `作成を確認してください。`
  - `そのまま作成してください。`
  - `今すぐ作成してください。`
  - `作成を進めてください。`
  - `作成を確定します。`
  - `はい、作成してください。`
  - `今、作成して大丈夫です。`
  - `確定して作成してください。`
  - `確認して作成してください。`
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
  - `Create an agent named family schedule.`
  - `Create a new agent called family schedule.`
  - `Please create an agent named family schedule.`
  - `I want to create an agent named family schedule.`
  - `Help me create an agent called family schedule.`
  - `Please add an agent named family schedule.`
  - `Create a new agent: family schedule.`
  - `I'd like to set up an agent called family schedule.`
  - `Add an agent with the name family schedule.`
  - `Please help me create an agent named family schedule.`

- Japanese Variants: 10
  - `名前を「家族スケジュール」としてエージェントを作成してください。`
  - `「家族スケジュール」という新しいエージェントを作成してください。`
  - `「家族スケジュール」という名前のエージェントを作ってください。`
  - `「家族スケジュール」というエージェントを作成したいです。`
  - `「家族スケジュール」という名前のエージェント作成を手伝ってください。`
  - `「家族スケジュール」というエージェントを追加してください。`
  - `新しいエージェント「家族スケジュール」を作成してください。`
  - `「家族スケジュール」というエージェントを設定したいです。`
  - `名前を「家族スケジュール」としてエージェントを追加してください。`
  - `「家族スケジュール」という名前のエージェントを作成してください。`
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
  - `It should record family schedules, including time, location, participants, and notes.`
  - `It needs to support this capability: record family schedules, including time, location, participants, and notes.`
  - `Please add this capability: record family schedules, including time, location, participants, and notes.`
  - `This agent should be able to record family schedules, including time, location, participants, and notes.`
  - `I want it to record family schedules, including time, location, participants, and notes.`
  - `Please configure it to record family schedules, including time, location, participants, and notes.`
  - `Its main function should be to record family schedules, including time, location, participants, and notes.`
  - `Please make it support this scenario: record family schedules, including time, location, participants, and notes.`
  - `The goal of this agent is to record family schedules, including time, location, participants, and notes.`
  - `The required capability is to record family schedules, including time, location, participants, and notes.`

- Japanese Variants: 10
  - `家族の予定の日時、場所、参加者、注意事項を記録できるようにしてください。`
  - `次の機能に対応できる必要があります：家族の予定の日時、場所、参加者、注意事項を記録できること。`
  - `この機能を追加してください：家族の予定の日時、場所、参加者、注意事項を記録できること。`
  - `このエージェントは次のことができる必要があります：家族の予定の日時、場所、参加者、注意事項を記録できること。`
  - `この機能を持たせたいです：家族の予定の日時、場所、参加者、注意事項を記録できること。`
  - `この用途向けに設定してください：家族の予定の日時、場所、参加者、注意事項を記録できること。`
  - `主な機能は次のとおりです：家族の予定の日時、場所、参加者、注意事項を記録できること。`
  - `次の利用シーンに対応させてください：家族の予定の日時、場所、参加者、注意事項を記録できること。`
  - `このエージェントの目的は次のとおりです：家族の予定の日時、場所、参加者、注意事項を記録できること。`
  - `必要な機能は次のとおりです：家族の予定の日時、場所、参加者、注意事項を記録できること。`
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
  - `Confirm creation.`
  - `Please confirm the creation.`
  - `Go ahead and create it.`
  - `Create it now.`
  - `Please proceed with the creation.`
  - `I confirm the creation.`
  - `Yes, create it.`
  - `You can create it now.`
  - `Please finalize and create it.`
  - `Confirm and create it.`

- Japanese Variants: 10
  - `作成を確定してください。`
  - `作成を確認してください。`
  - `そのまま作成してください。`
  - `今すぐ作成してください。`
  - `作成を進めてください。`
  - `作成を確定します。`
  - `はい、作成してください。`
  - `今、作成して大丈夫です。`
  - `確定して作成してください。`
  - `確認して作成してください。`
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
  - `Create an agent named grocery assistant.`
  - `Create a new agent called grocery assistant.`
  - `Please create an agent named grocery assistant.`
  - `I want to create an agent named grocery assistant.`
  - `Help me create an agent called grocery assistant.`
  - `Please add an agent named grocery assistant.`
  - `Create a new agent: grocery assistant.`
  - `I'd like to set up an agent called grocery assistant.`
  - `Add an agent with the name grocery assistant.`
  - `Please help me create an agent named grocery assistant.`

- Japanese Variants: 10
  - `名前を「買い物アシスタント」としてエージェントを作成してください。`
  - `「買い物アシスタント」という新しいエージェントを作成してください。`
  - `「買い物アシスタント」という名前のエージェントを作ってください。`
  - `「買い物アシスタント」というエージェントを作成したいです。`
  - `「買い物アシスタント」という名前のエージェント作成を手伝ってください。`
  - `「買い物アシスタント」というエージェントを追加してください。`
  - `新しいエージェント「買い物アシスタント」を作成してください。`
  - `「買い物アシスタント」というエージェントを設定したいです。`
  - `名前を「買い物アシスタント」としてエージェントを追加してください。`
  - `「買い物アシスタント」という名前のエージェントを作成してください。`
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
  - `It should record grocery items, quantities, and notes, and support Excel export.`
  - `It needs to support this capability: record grocery items, quantities, and notes, and support Excel export.`
  - `Please add this capability: record grocery items, quantities, and notes, and support Excel export.`
  - `This agent should be able to record grocery items, quantities, and notes, and support Excel export.`
  - `I want it to record grocery items, quantities, and notes, and support Excel export.`
  - `Please configure it to record grocery items, quantities, and notes, and support Excel export.`
  - `Its main function should be to record grocery items, quantities, and notes, and support Excel export.`
  - `Please make it support this scenario: record grocery items, quantities, and notes, and support Excel export.`
  - `The goal of this agent is to record grocery items, quantities, and notes, and support Excel export.`
  - `The required capability is to record grocery items, quantities, and notes, and support Excel export.`

- Japanese Variants: 10
  - `買い物項目、数量、メモを記録し、Excel にエクスポートできるようにしてください。`
  - `次の機能に対応できる必要があります：買い物項目、数量、メモを記録し、Excel にエクスポートできること。`
  - `この機能を追加してください：買い物項目、数量、メモを記録し、Excel にエクスポートできること。`
  - `このエージェントは次のことができる必要があります：買い物項目、数量、メモを記録し、Excel にエクスポートできること。`
  - `この機能を持たせたいです：買い物項目、数量、メモを記録し、Excel にエクスポートできること。`
  - `この用途向けに設定してください：買い物項目、数量、メモを記録し、Excel にエクスポートできること。`
  - `主な機能は次のとおりです：買い物項目、数量、メモを記録し、Excel にエクスポートできること。`
  - `次の利用シーンに対応させてください：買い物項目、数量、メモを記録し、Excel にエクスポートできること。`
  - `このエージェントの目的は次のとおりです：買い物項目、数量、メモを記録し、Excel にエクスポートできること。`
  - `必要な機能は次のとおりです：買い物項目、数量、メモを記録し、Excel にエクスポートできること。`
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
  - `Confirm creation.`
  - `Please confirm the creation.`
  - `Go ahead and create it.`
  - `Create it now.`
  - `Please proceed with the creation.`
  - `I confirm the creation.`
  - `Yes, create it.`
  - `You can create it now.`
  - `Please finalize and create it.`
  - `Confirm and create it.`

- Japanese Variants: 10
  - `作成を確定してください。`
  - `作成を確認してください。`
  - `そのまま作成してください。`
  - `今すぐ作成してください。`
  - `作成を進めてください。`
  - `作成を確定します。`
  - `はい、作成してください。`
  - `今、作成して大丈夫です。`
  - `確定して作成してください。`
  - `確認して作成してください。`
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
  - `Record a breakfast expense of 480 yen at 7:30 today.`
  - `Please log a breakfast expense of 480 yen at 7:30 today.`
  - `Add an expense record for 7:30 today: breakfast, 480 yen.`
  - `Please enter that I spent 480 yen on breakfast at 7:30 today.`
  - `Record today's 7:30 breakfast spending of 480 yen.`
  - `Log a spending entry: 7:30 today, breakfast, 480 yen.`
  - `Please add today's breakfast expense at 7:30, amount 480 yen.`
  - `Enter a budget record for 7:30 today: breakfast, 480 yen.`
  - `Record that 480 yen was spent on breakfast at 7:30 today.`
  - `Add this expense: 7:30 today, breakfast, 480 yen.`

- Japanese Variants: 10
  - `今日の 7:30 に 朝食 で 480 円使った記録を追加してください。`
  - `今日の 7:30 の 朝食 の支出 480 円を記録してください。`
  - `支出記録を追加してください：今日 7:30、朝食、480 円。`
  - `今日の 7:30 に 朝食 に 480 円使ったことを入力してください。`
  - `今日 7:30 の 朝食 の支出 480 円を記録してください。`
  - `支出エントリーを記録してください：今日 7:30、朝食、480 円。`
  - `今日の 7:30 の 朝食 の支出、金額 480 円を追加してください。`
  - `家計簿に入力してください：今日 7:30、朝食、480 円。`
  - `今日の 7:30 に 朝食 で 480 円使ったと記録してください。`
  - `この支出を追加してください：今日 7:30、朝食、480 円。`
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
  - `Record a subway expense of 220 yen at 8:20 today.`
  - `Please log a subway expense of 220 yen at 8:20 today.`
  - `Add an expense record for 8:20 today: subway, 220 yen.`
  - `Please enter that I spent 220 yen on subway at 8:20 today.`
  - `Record today's 8:20 subway spending of 220 yen.`
  - `Log a spending entry: 8:20 today, subway, 220 yen.`
  - `Please add today's subway expense at 8:20, amount 220 yen.`
  - `Enter a budget record for 8:20 today: subway, 220 yen.`
  - `Record that 220 yen was spent on subway at 8:20 today.`
  - `Add this expense: 8:20 today, subway, 220 yen.`

- Japanese Variants: 10
  - `今日の 8:20 に 地下鉄 で 220 円使った記録を追加してください。`
  - `今日の 8:20 の 地下鉄 の支出 220 円を記録してください。`
  - `支出記録を追加してください：今日 8:20、地下鉄、220 円。`
  - `今日の 8:20 に 地下鉄 に 220 円使ったことを入力してください。`
  - `今日 8:20 の 地下鉄 の支出 220 円を記録してください。`
  - `支出エントリーを記録してください：今日 8:20、地下鉄、220 円。`
  - `今日の 8:20 の 地下鉄 の支出、金額 220 円を追加してください。`
  - `家計簿に入力してください：今日 8:20、地下鉄、220 円。`
  - `今日の 8:20 に 地下鉄 で 220 円使ったと記録してください。`
  - `この支出を追加してください：今日 8:20、地下鉄、220 円。`
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
  - `Record a groceries expense of 2000 yen at 10:20 today.`
  - `Please log a groceries expense of 2000 yen at 10:20 today.`
  - `Add an expense record for 10:20 today: groceries, 2000 yen.`
  - `Please enter that I spent 2000 yen on groceries at 10:20 today.`
  - `Record today's 10:20 groceries spending of 2000 yen.`
  - `Log a spending entry: 10:20 today, groceries, 2000 yen.`
  - `Please add today's groceries expense at 10:20, amount 2000 yen.`
  - `Enter a budget record for 10:20 today: groceries, 2000 yen.`
  - `Record that 2000 yen was spent on groceries at 10:20 today.`
  - `Add this expense: 10:20 today, groceries, 2000 yen.`

- Japanese Variants: 10
  - `今日の 10:20 に 食材 で 2000 円使った記録を追加してください。`
  - `今日の 10:20 の 食材 の支出 2000 円を記録してください。`
  - `支出記録を追加してください：今日 10:20、食材、2000 円。`
  - `今日の 10:20 に 食材 に 2000 円使ったことを入力してください。`
  - `今日 10:20 の 食材 の支出 2000 円を記録してください。`
  - `支出エントリーを記録してください：今日 10:20、食材、2000 円。`
  - `今日の 10:20 の 食材 の支出、金額 2000 円を追加してください。`
  - `家計簿に入力してください：今日 10:20、食材、2000 円。`
  - `今日の 10:20 に 食材 で 2000 円使ったと記録してください。`
  - `この支出を追加してください：今日 10:20、食材、2000 円。`
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
  - `Record a lunch expense of 800 yen at 12:00 today.`
  - `Please log a lunch expense of 800 yen at 12:00 today.`
  - `Add an expense record for 12:00 today: lunch, 800 yen.`
  - `Please enter that I spent 800 yen on lunch at 12:00 today.`
  - `Record today's 12:00 lunch spending of 800 yen.`
  - `Log a spending entry: 12:00 today, lunch, 800 yen.`
  - `Please add today's lunch expense at 12:00, amount 800 yen.`
  - `Enter a budget record for 12:00 today: lunch, 800 yen.`
  - `Record that 800 yen was spent on lunch at 12:00 today.`
  - `Add this expense: 12:00 today, lunch, 800 yen.`

- Japanese Variants: 10
  - `今日の 12:00 に 昼食 で 800 円使った記録を追加してください。`
  - `今日の 12:00 の 昼食 の支出 800 円を記録してください。`
  - `支出記録を追加してください：今日 12:00、昼食、800 円。`
  - `今日の 12:00 に 昼食 に 800 円使ったことを入力してください。`
  - `今日 12:00 の 昼食 の支出 800 円を記録してください。`
  - `支出エントリーを記録してください：今日 12:00、昼食、800 円。`
  - `今日の 12:00 の 昼食 の支出、金額 800 円を追加してください。`
  - `家計簿に入力してください：今日 12:00、昼食、800 円。`
  - `今日の 12:00 に 昼食 で 800 円使ったと記録してください。`
  - `この支出を追加してください：今日 12:00、昼食、800 円。`
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
  - `Record a fruit expense of 650 yen at 14:10 today.`
  - `Please log a fruit expense of 650 yen at 14:10 today.`
  - `Add an expense record for 14:10 today: fruit, 650 yen.`
  - `Please enter that I spent 650 yen on fruit at 14:10 today.`
  - `Record today's 14:10 fruit spending of 650 yen.`
  - `Log a spending entry: 14:10 today, fruit, 650 yen.`
  - `Please add today's fruit expense at 14:10, amount 650 yen.`
  - `Enter a budget record for 14:10 today: fruit, 650 yen.`
  - `Record that 650 yen was spent on fruit at 14:10 today.`
  - `Add this expense: 14:10 today, fruit, 650 yen.`

- Japanese Variants: 10
  - `今日の 14:10 に 果物 で 650 円使った記録を追加してください。`
  - `今日の 14:10 の 果物 の支出 650 円を記録してください。`
  - `支出記録を追加してください：今日 14:10、果物、650 円。`
  - `今日の 14:10 に 果物 に 650 円使ったことを入力してください。`
  - `今日 14:10 の 果物 の支出 650 円を記録してください。`
  - `支出エントリーを記録してください：今日 14:10、果物、650 円。`
  - `今日の 14:10 の 果物 の支出、金額 650 円を追加してください。`
  - `家計簿に入力してください：今日 14:10、果物、650 円。`
  - `今日の 14:10 に 果物 で 650 円使ったと記録してください。`
  - `この支出を追加してください：今日 14:10、果物、650 円。`
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
  - `Show me what records are in family budget.`
  - `List the records in family budget.`
  - `What records are saved in family budget?`
  - `Please display the records in family budget.`
  - `Can you show the entries in family budget?`
  - `I want to see the current records in family budget.`
  - `Tell me what has been recorded in family budget.`
  - `Please check the records in family budget for me.`
  - `Show all record entries in family budget.`
  - `Could you list the saved records in family budget?`

- Japanese Variants: 10
  - `家庭家計簿 にはどんな記録がありますか。`
  - `家庭家計簿 の記録を一覧表示してください。`
  - `家庭家計簿 に保存されている記録は何ですか。`
  - `家庭家計簿 の記録を表示してください。`
  - `家庭家計簿 のエントリーを見せてもらえますか。`
  - `家庭家計簿 の現在の記録を見たいです。`
  - `家庭家計簿 に何が記録されているか教えてください。`
  - `家庭家計簿 の記録を確認してください。`
  - `家庭家計簿 のすべての記録項目を見せてください。`
  - `家庭家計簿 に保存された記録を一覧にしてもらえますか。`
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
  - `Export the family budget document.`
  - `Please export the family budget document.`
  - `Create an exported document for family budget.`
  - `I want to export the family budget document.`
  - `Generate an export file for family budget.`
  - `Please create an export of family budget.`
  - `Output family budget as an exportable document.`
  - `Can you export family budget for me?`
  - `Please generate the exported file for family budget.`
  - `Make an export document for family budget.`

- Japanese Variants: 10
  - `家庭家計簿 の文書をエクスポートしてください。`
  - `家庭家計簿 の文書を出力してください。`
  - `家庭家計簿 のエクスポート用文書を作成してください。`
  - `家庭家計簿 をエクスポートしたいです。`
  - `家庭家計簿 のエクスポートファイルを生成してください。`
  - `家庭家計簿 のエクスポートを作成してください。`
  - `家庭家計簿 をエクスポート可能な文書として出力してください。`
  - `家庭家計簿 をエクスポートしてもらえますか。`
  - `家庭家計簿 の出力ファイルを生成してください。`
  - `家庭家計簿 のエクスポート文書を作ってください。`
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
  - `What is the total spending up to today? If it exceeds 3000 yen, create a reminder and send it to HomeHub.`
  - `Tell me the total expenses through today, and if they are over 3000 yen, send a reminder to HomeHub.`
  - `Please calculate the total spending so far; if it goes beyond 3000 yen, create a HomeHub reminder.`
  - `How much has been spent up to today? If the amount is above 3000 yen, notify HomeHub.`
  - `Give me today's cumulative spending, and trigger a reminder to HomeHub if it exceeds 3000 yen.`
  - `Please total the spending through today and send a reminder to HomeHub if the total is over 3000 yen.`
  - `Check the spending total up to today. If it is more than 3000 yen, create a reminder for HomeHub.`
  - `What is the running total of spending today? If it passes 3000 yen, send a HomeHub alert.`
  - `Calculate the total spent up to today and create a HomeHub reminder when it exceeds 3000 yen.`
  - `Please provide the total spending through today, and if it is above 3000 yen, send a reminder to HomeHub.`

- Japanese Variants: 10
  - `今日までの支出総額はいくらですか。3000 円を超えたらリマインダーを作成し、HomeHub に送ってください。`
  - `今日までの支出総額を教えてください。3000 円を超えた場合は HomeHub に通知してください。`
  - `これまでの支出を集計し、3000 円を超えたら HomeHub 用のリマインダーを作成してください。`
  - `今日までにいくら使いましたか。3000 円を上回ったら HomeHub に知らせてください。`
  - `本日までの累計支出を教えてください。3000 円を超えたら HomeHub へリマインダーを送ってください。`
  - `今日までの支出合計を計算し、3000 円を超える場合は HomeHub に通知してください。`
  - `今日までの支出総額を確認し、3000 円を超えたら HomeHub 向けのリマインダーを作成してください。`
  - `今日までの支出累計はいくらですか。3000 円を超えたら HomeHub にアラートを送ってください。`
  - `今日までの総支出を計算し、3000 円を超えた場合は HomeHub のリマインダーを作成してください。`
  - `今日までの支出総額を出して、3000 円を上回ったら HomeHub にリマインダーを送ってください。`
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
  - `What is the total spending up to today, and generate an Excel file with the expense details.`
  - `Please calculate total spending through today and create an Excel file of the expenses.`
  - `Show me the total spent up to today and export the spending data to Excel.`
  - `Tell me the total expenses up to today and make an Excel file with the details.`
  - `I want the cumulative spending up to today and an Excel export of the expense information.`
  - `Please total the spending so far and generate an Excel sheet of all expense records.`
  - `How much have we spent up to today? Also create an Excel file of the spending details.`
  - `Calculate the total spending through today and output the expense data as Excel.`
  - `Give me the spending total so far and build an Excel file from the expense information.`
  - `Please provide the total expense amount through today and export the expense details into Excel.`

- Japanese Variants: 10
  - `今日までの支出総額はいくらですか。あわせて支出情報を Excel ファイルにしてください。`
  - `今日までの支出総額を計算し、支出明細の Excel ファイルを作成してください。`
  - `今日までに使った合計を見せて、支出データを Excel にエクスポートしてください。`
  - `今日までの支出総額を教えて、詳細を Excel ファイルにしてください。`
  - `今日までの累計支出と、支出情報の Excel 出力がほしいです。`
  - `これまでの支出を合計し、すべての支出記録を Excel シートにしてください。`
  - `今日までにいくら使ったか教えてください。あわせて支出詳細を Excel ファイルにしてください。`
  - `今日までの支出総額を計算し、支出データを Excel として出力してください。`
  - `現在までの支出合計を出して、支出情報から Excel ファイルを作成してください。`
  - `今日までの総支出額を教えて、支出明細を Excel にエクスポートしてください。`
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
  - `Record a tissues expense of 320 yen at 15:30 today.`
  - `Please log a tissues expense of 320 yen at 15:30 today.`
  - `Add an expense record for 15:30 today: tissues, 320 yen.`
  - `Please enter that I spent 320 yen on tissues at 15:30 today.`
  - `Record today's 15:30 tissues spending of 320 yen.`
  - `Log a spending entry: 15:30 today, tissues, 320 yen.`
  - `Please add today's tissues expense at 15:30, amount 320 yen.`
  - `Enter a budget record for 15:30 today: tissues, 320 yen.`
  - `Record that 320 yen was spent on tissues at 15:30 today.`
  - `Add this expense: 15:30 today, tissues, 320 yen.`

- Japanese Variants: 10
  - `今日の 15:30 に ティッシュ で 320 円使った記録を追加してください。`
  - `今日の 15:30 の ティッシュ の支出 320 円を記録してください。`
  - `支出記録を追加してください：今日 15:30、ティッシュ、320 円。`
  - `今日の 15:30 に ティッシュ に 320 円使ったことを入力してください。`
  - `今日 15:30 の ティッシュ の支出 320 円を記録してください。`
  - `支出エントリーを記録してください：今日 15:30、ティッシュ、320 円。`
  - `今日の 15:30 の ティッシュ の支出、金額 320 円を追加してください。`
  - `家計簿に入力してください：今日 15:30、ティッシュ、320 円。`
  - `今日の 15:30 に ティッシュ で 320 円使ったと記録してください。`
  - `この支出を追加してください：今日 15:30、ティッシュ、320 円。`
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
  - `Record a entertainment expense of 5800 yen at 17:00 today.`
  - `Please log a entertainment expense of 5800 yen at 17:00 today.`
  - `Add an expense record for 17:00 today: entertainment, 5800 yen.`
  - `Please enter that I spent 5800 yen on entertainment at 17:00 today.`
  - `Record today's 17:00 entertainment spending of 5800 yen.`
  - `Log a spending entry: 17:00 today, entertainment, 5800 yen.`
  - `Please add today's entertainment expense at 17:00, amount 5800 yen.`
  - `Enter a budget record for 17:00 today: entertainment, 5800 yen.`
  - `Record that 5800 yen was spent on entertainment at 17:00 today.`
  - `Add this expense: 17:00 today, entertainment, 5800 yen.`

- Japanese Variants: 10
  - `今日の 17:00 に 交際費 で 5800 円使った記録を追加してください。`
  - `今日の 17:00 の 交際費 の支出 5800 円を記録してください。`
  - `支出記録を追加してください：今日 17:00、交際費、5800 円。`
  - `今日の 17:00 に 交際費 に 5800 円使ったことを入力してください。`
  - `今日 17:00 の 交際費 の支出 5800 円を記録してください。`
  - `支出エントリーを記録してください：今日 17:00、交際費、5800 円。`
  - `今日の 17:00 の 交際費 の支出、金額 5800 円を追加してください。`
  - `家計簿に入力してください：今日 17:00、交際費、5800 円。`
  - `今日の 17:00 に 交際費 で 5800 円使ったと記録してください。`
  - `この支出を追加してください：今日 17:00、交際費、5800 円。`
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
  - `Record a milk expense of 260 yen at 18:15 today.`
  - `Please log a milk expense of 260 yen at 18:15 today.`
  - `Add an expense record for 18:15 today: milk, 260 yen.`
  - `Please enter that I spent 260 yen on milk at 18:15 today.`
  - `Record today's 18:15 milk spending of 260 yen.`
  - `Log a spending entry: 18:15 today, milk, 260 yen.`
  - `Please add today's milk expense at 18:15, amount 260 yen.`
  - `Enter a budget record for 18:15 today: milk, 260 yen.`
  - `Record that 260 yen was spent on milk at 18:15 today.`
  - `Add this expense: 18:15 today, milk, 260 yen.`

- Japanese Variants: 10
  - `今日の 18:15 に 牛乳 で 260 円使った記録を追加してください。`
  - `今日の 18:15 の 牛乳 の支出 260 円を記録してください。`
  - `支出記録を追加してください：今日 18:15、牛乳、260 円。`
  - `今日の 18:15 に 牛乳 に 260 円使ったことを入力してください。`
  - `今日 18:15 の 牛乳 の支出 260 円を記録してください。`
  - `支出エントリーを記録してください：今日 18:15、牛乳、260 円。`
  - `今日の 18:15 の 牛乳 の支出、金額 260 円を追加してください。`
  - `家計簿に入力してください：今日 18:15、牛乳、260 円。`
  - `今日の 18:15 に 牛乳 で 260 円使ったと記録してください。`
  - `この支出を追加してください：今日 18:15、牛乳、260 円。`
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
  - `Record a dinner expense of 1500 yen at 19:40 today.`
  - `Please log a dinner expense of 1500 yen at 19:40 today.`
  - `Add an expense record for 19:40 today: dinner, 1500 yen.`
  - `Please enter that I spent 1500 yen on dinner at 19:40 today.`
  - `Record today's 19:40 dinner spending of 1500 yen.`
  - `Log a spending entry: 19:40 today, dinner, 1500 yen.`
  - `Please add today's dinner expense at 19:40, amount 1500 yen.`
  - `Enter a budget record for 19:40 today: dinner, 1500 yen.`
  - `Record that 1500 yen was spent on dinner at 19:40 today.`
  - `Add this expense: 19:40 today, dinner, 1500 yen.`

- Japanese Variants: 10
  - `今日の 19:40 に 夕食 で 1500 円使った記録を追加してください。`
  - `今日の 19:40 の 夕食 の支出 1500 円を記録してください。`
  - `支出記録を追加してください：今日 19:40、夕食、1500 円。`
  - `今日の 19:40 に 夕食 に 1500 円使ったことを入力してください。`
  - `今日 19:40 の 夕食 の支出 1500 円を記録してください。`
  - `支出エントリーを記録してください：今日 19:40、夕食、1500 円。`
  - `今日の 19:40 の 夕食 の支出、金額 1500 円を追加してください。`
  - `家計簿に入力してください：今日 19:40、夕食、1500 円。`
  - `今日の 19:40 に 夕食 で 1500 円使ったと記録してください。`
  - `この支出を追加してください：今日 19:40、夕食、1500 円。`
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
  - `Record a parking expense of 700 yen at 20:10 today.`
  - `Please log a parking expense of 700 yen at 20:10 today.`
  - `Add an expense record for 20:10 today: parking, 700 yen.`
  - `Please enter that I spent 700 yen on parking at 20:10 today.`
  - `Record today's 20:10 parking spending of 700 yen.`
  - `Log a spending entry: 20:10 today, parking, 700 yen.`
  - `Please add today's parking expense at 20:10, amount 700 yen.`
  - `Enter a budget record for 20:10 today: parking, 700 yen.`
  - `Record that 700 yen was spent on parking at 20:10 today.`
  - `Add this expense: 20:10 today, parking, 700 yen.`

- Japanese Variants: 10
  - `今日の 20:10 に 駐車場代 で 700 円使った記録を追加してください。`
  - `今日の 20:10 の 駐車場代 の支出 700 円を記録してください。`
  - `支出記録を追加してください：今日 20:10、駐車場代、700 円。`
  - `今日の 20:10 に 駐車場代 に 700 円使ったことを入力してください。`
  - `今日 20:10 の 駐車場代 の支出 700 円を記録してください。`
  - `支出エントリーを記録してください：今日 20:10、駐車場代、700 円。`
  - `今日の 20:10 の 駐車場代 の支出、金額 700 円を追加してください。`
  - `家計簿に入力してください：今日 20:10、駐車場代、700 円。`
  - `今日の 20:10 に 駐車場代 で 700 円使ったと記録してください。`
  - `この支出を追加してください：今日 20:10、駐車場代、700 円。`
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
  - `Show me what records are in family budget.`
  - `List the records in family budget.`
  - `What records are saved in family budget?`
  - `Please display the records in family budget.`
  - `Can you show the entries in family budget?`
  - `I want to see the current records in family budget.`
  - `Tell me what has been recorded in family budget.`
  - `Please check the records in family budget for me.`
  - `Show all record entries in family budget.`
  - `Could you list the saved records in family budget?`

- Japanese Variants: 10
  - `家庭家計簿 にはどんな記録がありますか。`
  - `家庭家計簿 の記録を一覧表示してください。`
  - `家庭家計簿 に保存されている記録は何ですか。`
  - `家庭家計簿 の記録を表示してください。`
  - `家庭家計簿 のエントリーを見せてもらえますか。`
  - `家庭家計簿 の現在の記録を見たいです。`
  - `家庭家計簿 に何が記録されているか教えてください。`
  - `家庭家計簿 の記録を確認してください。`
  - `家庭家計簿 のすべての記録項目を見せてください。`
  - `家庭家計簿 に保存された記録を一覧にしてもらえますか。`
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
  - `Export the family budget document.`
  - `Please export the family budget document.`
  - `Create an exported document for family budget.`
  - `I want to export the family budget document.`
  - `Generate an export file for family budget.`
  - `Please create an export of family budget.`
  - `Output family budget as an exportable document.`
  - `Can you export family budget for me?`
  - `Please generate the exported file for family budget.`
  - `Make an export document for family budget.`

- Japanese Variants: 10
  - `家庭家計簿 の文書をエクスポートしてください。`
  - `家庭家計簿 の文書を出力してください。`
  - `家庭家計簿 のエクスポート用文書を作成してください。`
  - `家庭家計簿 をエクスポートしたいです。`
  - `家庭家計簿 のエクスポートファイルを生成してください。`
  - `家庭家計簿 のエクスポートを作成してください。`
  - `家庭家計簿 をエクスポート可能な文書として出力してください。`
  - `家庭家計簿 をエクスポートしてもらえますか。`
  - `家庭家計簿 の出力ファイルを生成してください。`
  - `家庭家計簿 のエクスポート文書を作ってください。`
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
  - `What is the total spending up to today? If it exceeds 10000 yen, create a reminder and send it to HomeHub.`
  - `Tell me the total expenses through today, and if they are over 10000 yen, send a reminder to HomeHub.`
  - `Please calculate the total spending so far; if it goes beyond 10000 yen, create a HomeHub reminder.`
  - `How much has been spent up to today? If the amount is above 10000 yen, notify HomeHub.`
  - `Give me today's cumulative spending, and trigger a reminder to HomeHub if it exceeds 10000 yen.`
  - `Please total the spending through today and send a reminder to HomeHub if the total is over 10000 yen.`
  - `Check the spending total up to today. If it is more than 10000 yen, create a reminder for HomeHub.`
  - `What is the running total of spending today? If it passes 10000 yen, send a HomeHub alert.`
  - `Calculate the total spent up to today and create a HomeHub reminder when it exceeds 10000 yen.`
  - `Please provide the total spending through today, and if it is above 10000 yen, send a reminder to HomeHub.`

- Japanese Variants: 10
  - `今日までの支出総額はいくらですか。10000 円を超えたらリマインダーを作成し、HomeHub に送ってください。`
  - `今日までの支出総額を教えてください。10000 円を超えた場合は HomeHub に通知してください。`
  - `これまでの支出を集計し、10000 円を超えたら HomeHub 用のリマインダーを作成してください。`
  - `今日までにいくら使いましたか。10000 円を上回ったら HomeHub に知らせてください。`
  - `本日までの累計支出を教えてください。10000 円を超えたら HomeHub へリマインダーを送ってください。`
  - `今日までの支出合計を計算し、10000 円を超える場合は HomeHub に通知してください。`
  - `今日までの支出総額を確認し、10000 円を超えたら HomeHub 向けのリマインダーを作成してください。`
  - `今日までの支出累計はいくらですか。10000 円を超えたら HomeHub にアラートを送ってください。`
  - `今日までの総支出を計算し、10000 円を超えた場合は HomeHub のリマインダーを作成してください。`
  - `今日までの支出総額を出して、10000 円を上回ったら HomeHub にリマインダーを送ってください。`
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
  - `What is the total spending up to today, and generate an Excel file with the expense details.`
  - `Please calculate total spending through today and create an Excel file of the expenses.`
  - `Show me the total spent up to today and export the spending data to Excel.`
  - `Tell me the total expenses up to today and make an Excel file with the details.`
  - `I want the cumulative spending up to today and an Excel export of the expense information.`
  - `Please total the spending so far and generate an Excel sheet of all expense records.`
  - `How much have we spent up to today? Also create an Excel file of the spending details.`
  - `Calculate the total spending through today and output the expense data as Excel.`
  - `Give me the spending total so far and build an Excel file from the expense information.`
  - `Please provide the total expense amount through today and export the expense details into Excel.`

- Japanese Variants: 10
  - `今日までの支出総額はいくらですか。あわせて支出情報を Excel ファイルにしてください。`
  - `今日までの支出総額を計算し、支出明細の Excel ファイルを作成してください。`
  - `今日までに使った合計を見せて、支出データを Excel にエクスポートしてください。`
  - `今日までの支出総額を教えて、詳細を Excel ファイルにしてください。`
  - `今日までの累計支出と、支出情報の Excel 出力がほしいです。`
  - `これまでの支出を合計し、すべての支出記録を Excel シートにしてください。`
  - `今日までにいくら使ったか教えてください。あわせて支出詳細を Excel ファイルにしてください。`
  - `今日までの支出総額を計算し、支出データを Excel として出力してください。`
  - `現在までの支出合計を出して、支出情報から Excel ファイルを作成してください。`
  - `今日までの総支出額を教えて、支出明細を Excel にエクスポートしてください。`
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
  - `Record a medicine expense of 980 yen at 21:00 today.`
  - `Please log a medicine expense of 980 yen at 21:00 today.`
  - `Add an expense record for 21:00 today: medicine, 980 yen.`
  - `Please enter that I spent 980 yen on medicine at 21:00 today.`
  - `Record today's 21:00 medicine spending of 980 yen.`
  - `Log a spending entry: 21:00 today, medicine, 980 yen.`
  - `Please add today's medicine expense at 21:00, amount 980 yen.`
  - `Enter a budget record for 21:00 today: medicine, 980 yen.`
  - `Record that 980 yen was spent on medicine at 21:00 today.`
  - `Add this expense: 21:00 today, medicine, 980 yen.`

- Japanese Variants: 10
  - `今日の 21:00 に 医薬品 で 980 円使った記録を追加してください。`
  - `今日の 21:00 の 医薬品 の支出 980 円を記録してください。`
  - `支出記録を追加してください：今日 21:00、医薬品、980 円。`
  - `今日の 21:00 に 医薬品 に 980 円使ったことを入力してください。`
  - `今日 21:00 の 医薬品 の支出 980 円を記録してください。`
  - `支出エントリーを記録してください：今日 21:00、医薬品、980 円。`
  - `今日の 21:00 の 医薬品 の支出、金額 980 円を追加してください。`
  - `家計簿に入力してください：今日 21:00、医薬品、980 円。`
  - `今日の 21:00 に 医薬品 で 980 円使ったと記録してください。`
  - `この支出を追加してください：今日 21:00、医薬品、980 円。`
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
  - `Record a pet food expense of 2300 yen at 21:20 today.`
  - `Please log a pet food expense of 2300 yen at 21:20 today.`
  - `Add an expense record for 21:20 today: pet food, 2300 yen.`
  - `Please enter that I spent 2300 yen on pet food at 21:20 today.`
  - `Record today's 21:20 pet food spending of 2300 yen.`
  - `Log a spending entry: 21:20 today, pet food, 2300 yen.`
  - `Please add today's pet food expense at 21:20, amount 2300 yen.`
  - `Enter a budget record for 21:20 today: pet food, 2300 yen.`
  - `Record that 2300 yen was spent on pet food at 21:20 today.`
  - `Add this expense: 21:20 today, pet food, 2300 yen.`

- Japanese Variants: 10
  - `今日の 21:20 に ペットフード で 2300 円使った記録を追加してください。`
  - `今日の 21:20 の ペットフード の支出 2300 円を記録してください。`
  - `支出記録を追加してください：今日 21:20、ペットフード、2300 円。`
  - `今日の 21:20 に ペットフード に 2300 円使ったことを入力してください。`
  - `今日 21:20 の ペットフード の支出 2300 円を記録してください。`
  - `支出エントリーを記録してください：今日 21:20、ペットフード、2300 円。`
  - `今日の 21:20 の ペットフード の支出、金額 2300 円を追加してください。`
  - `家計簿に入力してください：今日 21:20、ペットフード、2300 円。`
  - `今日の 21:20 に ペットフード で 2300 円使ったと記録してください。`
  - `この支出を追加してください：今日 21:20、ペットフード、2300 円。`
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
  - `Record a internet bill expense of 4300 yen at 21:40 today.`
  - `Please log a internet bill expense of 4300 yen at 21:40 today.`
  - `Add an expense record for 21:40 today: internet bill, 4300 yen.`
  - `Please enter that I spent 4300 yen on internet bill at 21:40 today.`
  - `Record today's 21:40 internet bill spending of 4300 yen.`
  - `Log a spending entry: 21:40 today, internet bill, 4300 yen.`
  - `Please add today's internet bill expense at 21:40, amount 4300 yen.`
  - `Enter a budget record for 21:40 today: internet bill, 4300 yen.`
  - `Record that 4300 yen was spent on internet bill at 21:40 today.`
  - `Add this expense: 21:40 today, internet bill, 4300 yen.`

- Japanese Variants: 10
  - `今日の 21:40 に インターネット料金 で 4300 円使った記録を追加してください。`
  - `今日の 21:40 の インターネット料金 の支出 4300 円を記録してください。`
  - `支出記録を追加してください：今日 21:40、インターネット料金、4300 円。`
  - `今日の 21:40 に インターネット料金 に 4300 円使ったことを入力してください。`
  - `今日 21:40 の インターネット料金 の支出 4300 円を記録してください。`
  - `支出エントリーを記録してください：今日 21:40、インターネット料金、4300 円。`
  - `今日の 21:40 の インターネット料金 の支出、金額 4300 円を追加してください。`
  - `家計簿に入力してください：今日 21:40、インターネット料金、4300 円。`
  - `今日の 21:40 に インターネット料金 で 4300 円使ったと記録してください。`
  - `この支出を追加してください：今日 21:40、インターネット料金、4300 円。`
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
  - `Record a water bill expense of 3200 yen at 22:00 today.`
  - `Please log a water bill expense of 3200 yen at 22:00 today.`
  - `Add an expense record for 22:00 today: water bill, 3200 yen.`
  - `Please enter that I spent 3200 yen on water bill at 22:00 today.`
  - `Record today's 22:00 water bill spending of 3200 yen.`
  - `Log a spending entry: 22:00 today, water bill, 3200 yen.`
  - `Please add today's water bill expense at 22:00, amount 3200 yen.`
  - `Enter a budget record for 22:00 today: water bill, 3200 yen.`
  - `Record that 3200 yen was spent on water bill at 22:00 today.`
  - `Add this expense: 22:00 today, water bill, 3200 yen.`

- Japanese Variants: 10
  - `今日の 22:00 に 水道料金 で 3200 円使った記録を追加してください。`
  - `今日の 22:00 の 水道料金 の支出 3200 円を記録してください。`
  - `支出記録を追加してください：今日 22:00、水道料金、3200 円。`
  - `今日の 22:00 に 水道料金 に 3200 円使ったことを入力してください。`
  - `今日 22:00 の 水道料金 の支出 3200 円を記録してください。`
  - `支出エントリーを記録してください：今日 22:00、水道料金、3200 円。`
  - `今日の 22:00 の 水道料金 の支出、金額 3200 円を追加してください。`
  - `家計簿に入力してください：今日 22:00、水道料金、3200 円。`
  - `今日の 22:00 に 水道料金 で 3200 円使ったと記録してください。`
  - `この支出を追加してください：今日 22:00、水道料金、3200 円。`
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
  - `Record a electricity bill expense of 5100 yen at 22:10 today.`
  - `Please log a electricity bill expense of 5100 yen at 22:10 today.`
  - `Add an expense record for 22:10 today: electricity bill, 5100 yen.`
  - `Please enter that I spent 5100 yen on electricity bill at 22:10 today.`
  - `Record today's 22:10 electricity bill spending of 5100 yen.`
  - `Log a spending entry: 22:10 today, electricity bill, 5100 yen.`
  - `Please add today's electricity bill expense at 22:10, amount 5100 yen.`
  - `Enter a budget record for 22:10 today: electricity bill, 5100 yen.`
  - `Record that 5100 yen was spent on electricity bill at 22:10 today.`
  - `Add this expense: 22:10 today, electricity bill, 5100 yen.`

- Japanese Variants: 10
  - `今日の 22:10 に 電気料金 で 5100 円使った記録を追加してください。`
  - `今日の 22:10 の 電気料金 の支出 5100 円を記録してください。`
  - `支出記録を追加してください：今日 22:10、電気料金、5100 円。`
  - `今日の 22:10 に 電気料金 に 5100 円使ったことを入力してください。`
  - `今日 22:10 の 電気料金 の支出 5100 円を記録してください。`
  - `支出エントリーを記録してください：今日 22:10、電気料金、5100 円。`
  - `今日の 22:10 の 電気料金 の支出、金額 5100 円を追加してください。`
  - `家計簿に入力してください：今日 22:10、電気料金、5100 円。`
  - `今日の 22:10 に 電気料金 で 5100 円使ったと記録してください。`
  - `この支出を追加してください：今日 22:10、電気料金、5100 円。`
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
  - `Show me what records are in family budget.`
  - `List the records in family budget.`
  - `What records are saved in family budget?`
  - `Please display the records in family budget.`
  - `Can you show the entries in family budget?`
  - `I want to see the current records in family budget.`
  - `Tell me what has been recorded in family budget.`
  - `Please check the records in family budget for me.`
  - `Show all record entries in family budget.`
  - `Could you list the saved records in family budget?`

- Japanese Variants: 10
  - `家庭家計簿 にはどんな記録がありますか。`
  - `家庭家計簿 の記録を一覧表示してください。`
  - `家庭家計簿 に保存されている記録は何ですか。`
  - `家庭家計簿 の記録を表示してください。`
  - `家庭家計簿 のエントリーを見せてもらえますか。`
  - `家庭家計簿 の現在の記録を見たいです。`
  - `家庭家計簿 に何が記録されているか教えてください。`
  - `家庭家計簿 の記録を確認してください。`
  - `家庭家計簿 のすべての記録項目を見せてください。`
  - `家庭家計簿 に保存された記録を一覧にしてもらえますか。`
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
  - `Export the family budget document.`
  - `Please export the family budget document.`
  - `Create an exported document for family budget.`
  - `I want to export the family budget document.`
  - `Generate an export file for family budget.`
  - `Please create an export of family budget.`
  - `Output family budget as an exportable document.`
  - `Can you export family budget for me?`
  - `Please generate the exported file for family budget.`
  - `Make an export document for family budget.`

- Japanese Variants: 10
  - `家庭家計簿 の文書をエクスポートしてください。`
  - `家庭家計簿 の文書を出力してください。`
  - `家庭家計簿 のエクスポート用文書を作成してください。`
  - `家庭家計簿 をエクスポートしたいです。`
  - `家庭家計簿 のエクスポートファイルを生成してください。`
  - `家庭家計簿 のエクスポートを作成してください。`
  - `家庭家計簿 をエクスポート可能な文書として出力してください。`
  - `家庭家計簿 をエクスポートしてもらえますか。`
  - `家庭家計簿 の出力ファイルを生成してください。`
  - `家庭家計簿 のエクスポート文書を作ってください。`
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
  - `What is the total spending up to today? If it exceeds 20000 yen, create a reminder and send it to HomeHub.`
  - `Tell me the total expenses through today, and if they are over 20000 yen, send a reminder to HomeHub.`
  - `Please calculate the total spending so far; if it goes beyond 20000 yen, create a HomeHub reminder.`
  - `How much has been spent up to today? If the amount is above 20000 yen, notify HomeHub.`
  - `Give me today's cumulative spending, and trigger a reminder to HomeHub if it exceeds 20000 yen.`
  - `Please total the spending through today and send a reminder to HomeHub if the total is over 20000 yen.`
  - `Check the spending total up to today. If it is more than 20000 yen, create a reminder for HomeHub.`
  - `What is the running total of spending today? If it passes 20000 yen, send a HomeHub alert.`
  - `Calculate the total spent up to today and create a HomeHub reminder when it exceeds 20000 yen.`
  - `Please provide the total spending through today, and if it is above 20000 yen, send a reminder to HomeHub.`

- Japanese Variants: 10
  - `今日までの支出総額はいくらですか。20000 円を超えたらリマインダーを作成し、HomeHub に送ってください。`
  - `今日までの支出総額を教えてください。20000 円を超えた場合は HomeHub に通知してください。`
  - `これまでの支出を集計し、20000 円を超えたら HomeHub 用のリマインダーを作成してください。`
  - `今日までにいくら使いましたか。20000 円を上回ったら HomeHub に知らせてください。`
  - `本日までの累計支出を教えてください。20000 円を超えたら HomeHub へリマインダーを送ってください。`
  - `今日までの支出合計を計算し、20000 円を超える場合は HomeHub に通知してください。`
  - `今日までの支出総額を確認し、20000 円を超えたら HomeHub 向けのリマインダーを作成してください。`
  - `今日までの支出累計はいくらですか。20000 円を超えたら HomeHub にアラートを送ってください。`
  - `今日までの総支出を計算し、20000 円を超えた場合は HomeHub のリマインダーを作成してください。`
  - `今日までの支出総額を出して、20000 円を上回ったら HomeHub にリマインダーを送ってください。`
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
  - `What is the total spending up to today, and generate an Excel file with the expense details.`
  - `Please calculate total spending through today and create an Excel file of the expenses.`
  - `Show me the total spent up to today and export the spending data to Excel.`
  - `Tell me the total expenses up to today and make an Excel file with the details.`
  - `I want the cumulative spending up to today and an Excel export of the expense information.`
  - `Please total the spending so far and generate an Excel sheet of all expense records.`
  - `How much have we spent up to today? Also create an Excel file of the spending details.`
  - `Calculate the total spending through today and output the expense data as Excel.`
  - `Give me the spending total so far and build an Excel file from the expense information.`
  - `Please provide the total expense amount through today and export the expense details into Excel.`

- Japanese Variants: 10
  - `今日までの支出総額はいくらですか。あわせて支出情報を Excel ファイルにしてください。`
  - `今日までの支出総額を計算し、支出明細の Excel ファイルを作成してください。`
  - `今日までに使った合計を見せて、支出データを Excel にエクスポートしてください。`
  - `今日までの支出総額を教えて、詳細を Excel ファイルにしてください。`
  - `今日までの累計支出と、支出情報の Excel 出力がほしいです。`
  - `これまでの支出を合計し、すべての支出記録を Excel シートにしてください。`
  - `今日までにいくら使ったか教えてください。あわせて支出詳細を Excel ファイルにしてください。`
  - `今日までの支出総額を計算し、支出データを Excel として出力してください。`
  - `現在までの支出合計を出して、支出情報から Excel ファイルを作成してください。`
  - `今日までの総支出額を教えて、支出明細を Excel にエクスポートしてください。`
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
  - `Record a school supplies expense of 890 yen at 22:20 today.`
  - `Please log a school supplies expense of 890 yen at 22:20 today.`
  - `Add an expense record for 22:20 today: school supplies, 890 yen.`
  - `Please enter that I spent 890 yen on school supplies at 22:20 today.`
  - `Record today's 22:20 school supplies spending of 890 yen.`
  - `Log a spending entry: 22:20 today, school supplies, 890 yen.`
  - `Please add today's school supplies expense at 22:20, amount 890 yen.`
  - `Enter a budget record for 22:20 today: school supplies, 890 yen.`
  - `Record that 890 yen was spent on school supplies at 22:20 today.`
  - `Add this expense: 22:20 today, school supplies, 890 yen.`

- Japanese Variants: 10
  - `今日の 22:20 に 学用品 で 890 円使った記録を追加してください。`
  - `今日の 22:20 の 学用品 の支出 890 円を記録してください。`
  - `支出記録を追加してください：今日 22:20、学用品、890 円。`
  - `今日の 22:20 に 学用品 に 890 円使ったことを入力してください。`
  - `今日 22:20 の 学用品 の支出 890 円を記録してください。`
  - `支出エントリーを記録してください：今日 22:20、学用品、890 円。`
  - `今日の 22:20 の 学用品 の支出、金額 890 円を追加してください。`
  - `家計簿に入力してください：今日 22:20、学用品、890 円。`
  - `今日の 22:20 に 学用品 で 890 円使ったと記録してください。`
  - `この支出を追加してください：今日 22:20、学用品、890 円。`
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
  - `Record a laundry detergent expense of 640 yen at 22:30 today.`
  - `Please log a laundry detergent expense of 640 yen at 22:30 today.`
  - `Add an expense record for 22:30 today: laundry detergent, 640 yen.`
  - `Please enter that I spent 640 yen on laundry detergent at 22:30 today.`
  - `Record today's 22:30 laundry detergent spending of 640 yen.`
  - `Log a spending entry: 22:30 today, laundry detergent, 640 yen.`
  - `Please add today's laundry detergent expense at 22:30, amount 640 yen.`
  - `Enter a budget record for 22:30 today: laundry detergent, 640 yen.`
  - `Record that 640 yen was spent on laundry detergent at 22:30 today.`
  - `Add this expense: 22:30 today, laundry detergent, 640 yen.`

- Japanese Variants: 10
  - `今日の 22:30 に 洗濯洗剤 で 640 円使った記録を追加してください。`
  - `今日の 22:30 の 洗濯洗剤 の支出 640 円を記録してください。`
  - `支出記録を追加してください：今日 22:30、洗濯洗剤、640 円。`
  - `今日の 22:30 に 洗濯洗剤 に 640 円使ったことを入力してください。`
  - `今日 22:30 の 洗濯洗剤 の支出 640 円を記録してください。`
  - `支出エントリーを記録してください：今日 22:30、洗濯洗剤、640 円。`
  - `今日の 22:30 の 洗濯洗剤 の支出、金額 640 円を追加してください。`
  - `家計簿に入力してください：今日 22:30、洗濯洗剤、640 円。`
  - `今日の 22:30 に 洗濯洗剤 で 640 円使ったと記録してください。`
  - `この支出を追加してください：今日 22:30、洗濯洗剤、640 円。`
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
  - `Record a birthday cake expense of 2750 yen at 22:40 today.`
  - `Please log a birthday cake expense of 2750 yen at 22:40 today.`
  - `Add an expense record for 22:40 today: birthday cake, 2750 yen.`
  - `Please enter that I spent 2750 yen on birthday cake at 22:40 today.`
  - `Record today's 22:40 birthday cake spending of 2750 yen.`
  - `Log a spending entry: 22:40 today, birthday cake, 2750 yen.`
  - `Please add today's birthday cake expense at 22:40, amount 2750 yen.`
  - `Enter a budget record for 22:40 today: birthday cake, 2750 yen.`
  - `Record that 2750 yen was spent on birthday cake at 22:40 today.`
  - `Add this expense: 22:40 today, birthday cake, 2750 yen.`

- Japanese Variants: 10
  - `今日の 22:40 に バースデーケーキ で 2750 円使った記録を追加してください。`
  - `今日の 22:40 の バースデーケーキ の支出 2750 円を記録してください。`
  - `支出記録を追加してください：今日 22:40、バースデーケーキ、2750 円。`
  - `今日の 22:40 に バースデーケーキ に 2750 円使ったことを入力してください。`
  - `今日 22:40 の バースデーケーキ の支出 2750 円を記録してください。`
  - `支出エントリーを記録してください：今日 22:40、バースデーケーキ、2750 円。`
  - `今日の 22:40 の バースデーケーキ の支出、金額 2750 円を追加してください。`
  - `家計簿に入力してください：今日 22:40、バースデーケーキ、2750 円。`
  - `今日の 22:40 に バースデーケーキ で 2750 円使ったと記録してください。`
  - `この支出を追加してください：今日 22:40、バースデーケーキ、2750 円。`
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
  - `Record a coffee expense of 450 yen at 22:50 today.`
  - `Please log a coffee expense of 450 yen at 22:50 today.`
  - `Add an expense record for 22:50 today: coffee, 450 yen.`
  - `Please enter that I spent 450 yen on coffee at 22:50 today.`
  - `Record today's 22:50 coffee spending of 450 yen.`
  - `Log a spending entry: 22:50 today, coffee, 450 yen.`
  - `Please add today's coffee expense at 22:50, amount 450 yen.`
  - `Enter a budget record for 22:50 today: coffee, 450 yen.`
  - `Record that 450 yen was spent on coffee at 22:50 today.`
  - `Add this expense: 22:50 today, coffee, 450 yen.`

- Japanese Variants: 10
  - `今日の 22:50 に コーヒー で 450 円使った記録を追加してください。`
  - `今日の 22:50 の コーヒー の支出 450 円を記録してください。`
  - `支出記録を追加してください：今日 22:50、コーヒー、450 円。`
  - `今日の 22:50 に コーヒー に 450 円使ったことを入力してください。`
  - `今日 22:50 の コーヒー の支出 450 円を記録してください。`
  - `支出エントリーを記録してください：今日 22:50、コーヒー、450 円。`
  - `今日の 22:50 の コーヒー の支出、金額 450 円を追加してください。`
  - `家計簿に入力してください：今日 22:50、コーヒー、450 円。`
  - `今日の 22:50 に コーヒー で 450 円使ったと記録してください。`
  - `この支出を追加してください：今日 22:50、コーヒー、450 円。`
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
  - `Record a late-night snack expense of 990 yen at 23:00 today.`
  - `Please log a late-night snack expense of 990 yen at 23:00 today.`
  - `Add an expense record for 23:00 today: late-night snack, 990 yen.`
  - `Please enter that I spent 990 yen on late-night snack at 23:00 today.`
  - `Record today's 23:00 late-night snack spending of 990 yen.`
  - `Log a spending entry: 23:00 today, late-night snack, 990 yen.`
  - `Please add today's late-night snack expense at 23:00, amount 990 yen.`
  - `Enter a budget record for 23:00 today: late-night snack, 990 yen.`
  - `Record that 990 yen was spent on late-night snack at 23:00 today.`
  - `Add this expense: 23:00 today, late-night snack, 990 yen.`

- Japanese Variants: 10
  - `今日の 23:00 に 夜食 で 990 円使った記録を追加してください。`
  - `今日の 23:00 の 夜食 の支出 990 円を記録してください。`
  - `支出記録を追加してください：今日 23:00、夜食、990 円。`
  - `今日の 23:00 に 夜食 に 990 円使ったことを入力してください。`
  - `今日 23:00 の 夜食 の支出 990 円を記録してください。`
  - `支出エントリーを記録してください：今日 23:00、夜食、990 円。`
  - `今日の 23:00 の 夜食 の支出、金額 990 円を追加してください。`
  - `家計簿に入力してください：今日 23:00、夜食、990 円。`
  - `今日の 23:00 に 夜食 で 990 円使ったと記録してください。`
  - `この支出を追加してください：今日 23:00、夜食、990 円。`
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
  - `Show me what records are in family budget.`
  - `List the records in family budget.`
  - `What records are saved in family budget?`
  - `Please display the records in family budget.`
  - `Can you show the entries in family budget?`
  - `I want to see the current records in family budget.`
  - `Tell me what has been recorded in family budget.`
  - `Please check the records in family budget for me.`
  - `Show all record entries in family budget.`
  - `Could you list the saved records in family budget?`

- Japanese Variants: 10
  - `家庭家計簿 にはどんな記録がありますか。`
  - `家庭家計簿 の記録を一覧表示してください。`
  - `家庭家計簿 に保存されている記録は何ですか。`
  - `家庭家計簿 の記録を表示してください。`
  - `家庭家計簿 のエントリーを見せてもらえますか。`
  - `家庭家計簿 の現在の記録を見たいです。`
  - `家庭家計簿 に何が記録されているか教えてください。`
  - `家庭家計簿 の記録を確認してください。`
  - `家庭家計簿 のすべての記録項目を見せてください。`
  - `家庭家計簿 に保存された記録を一覧にしてもらえますか。`
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
  - `Export the family budget document.`
  - `Please export the family budget document.`
  - `Create an exported document for family budget.`
  - `I want to export the family budget document.`
  - `Generate an export file for family budget.`
  - `Please create an export of family budget.`
  - `Output family budget as an exportable document.`
  - `Can you export family budget for me?`
  - `Please generate the exported file for family budget.`
  - `Make an export document for family budget.`

- Japanese Variants: 10
  - `家庭家計簿 の文書をエクスポートしてください。`
  - `家庭家計簿 の文書を出力してください。`
  - `家庭家計簿 のエクスポート用文書を作成してください。`
  - `家庭家計簿 をエクスポートしたいです。`
  - `家庭家計簿 のエクスポートファイルを生成してください。`
  - `家庭家計簿 のエクスポートを作成してください。`
  - `家庭家計簿 をエクスポート可能な文書として出力してください。`
  - `家庭家計簿 をエクスポートしてもらえますか。`
  - `家庭家計簿 の出力ファイルを生成してください。`
  - `家庭家計簿 のエクスポート文書を作ってください。`
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
  - `What is the total spending up to today? If it exceeds 35000 yen, create a reminder and send it to HomeHub.`
  - `Tell me the total expenses through today, and if they are over 35000 yen, send a reminder to HomeHub.`
  - `Please calculate the total spending so far; if it goes beyond 35000 yen, create a HomeHub reminder.`
  - `How much has been spent up to today? If the amount is above 35000 yen, notify HomeHub.`
  - `Give me today's cumulative spending, and trigger a reminder to HomeHub if it exceeds 35000 yen.`
  - `Please total the spending through today and send a reminder to HomeHub if the total is over 35000 yen.`
  - `Check the spending total up to today. If it is more than 35000 yen, create a reminder for HomeHub.`
  - `What is the running total of spending today? If it passes 35000 yen, send a HomeHub alert.`
  - `Calculate the total spent up to today and create a HomeHub reminder when it exceeds 35000 yen.`
  - `Please provide the total spending through today, and if it is above 35000 yen, send a reminder to HomeHub.`

- Japanese Variants: 10
  - `今日までの支出総額はいくらですか。35000 円を超えたらリマインダーを作成し、HomeHub に送ってください。`
  - `今日までの支出総額を教えてください。35000 円を超えた場合は HomeHub に通知してください。`
  - `これまでの支出を集計し、35000 円を超えたら HomeHub 用のリマインダーを作成してください。`
  - `今日までにいくら使いましたか。35000 円を上回ったら HomeHub に知らせてください。`
  - `本日までの累計支出を教えてください。35000 円を超えたら HomeHub へリマインダーを送ってください。`
  - `今日までの支出合計を計算し、35000 円を超える場合は HomeHub に通知してください。`
  - `今日までの支出総額を確認し、35000 円を超えたら HomeHub 向けのリマインダーを作成してください。`
  - `今日までの支出累計はいくらですか。35000 円を超えたら HomeHub にアラートを送ってください。`
  - `今日までの総支出を計算し、35000 円を超えた場合は HomeHub のリマインダーを作成してください。`
  - `今日までの支出総額を出して、35000 円を上回ったら HomeHub にリマインダーを送ってください。`
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
  - `What is the total spending up to today, and generate an Excel file with the expense details.`
  - `Please calculate total spending through today and create an Excel file of the expenses.`
  - `Show me the total spent up to today and export the spending data to Excel.`
  - `Tell me the total expenses up to today and make an Excel file with the details.`
  - `I want the cumulative spending up to today and an Excel export of the expense information.`
  - `Please total the spending so far and generate an Excel sheet of all expense records.`
  - `How much have we spent up to today? Also create an Excel file of the spending details.`
  - `Calculate the total spending through today and output the expense data as Excel.`
  - `Give me the spending total so far and build an Excel file from the expense information.`
  - `Please provide the total expense amount through today and export the expense details into Excel.`

- Japanese Variants: 10
  - `今日までの支出総額はいくらですか。あわせて支出情報を Excel ファイルにしてください。`
  - `今日までの支出総額を計算し、支出明細の Excel ファイルを作成してください。`
  - `今日までに使った合計を見せて、支出データを Excel にエクスポートしてください。`
  - `今日までの支出総額を教えて、詳細を Excel ファイルにしてください。`
  - `今日までの累計支出と、支出情報の Excel 出力がほしいです。`
  - `これまでの支出を合計し、すべての支出記録を Excel シートにしてください。`
  - `今日までにいくら使ったか教えてください。あわせて支出詳細を Excel ファイルにしてください。`
  - `今日までの支出総額を計算し、支出データを Excel として出力してください。`
  - `現在までの支出合計を出して、支出情報から Excel ファイルを作成してください。`
  - `今日までの総支出額を教えて、支出明細を Excel にエクスポートしてください。`
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
  - `Please record this in health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`
  - `Add this entry to health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`
  - `Please save the following in health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`
  - `Record this information in health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`
  - `Enter this into health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`
  - `Please add the following record to health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`
  - `Write this into health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`
  - `Save this entry in health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`
  - `Register this information in health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`
  - `Please store this in health condition records: Grandmahad a temperature of 37.5°C today，a mild cough，has drunk water and is resting.`

- Japanese Variants: 10
  - `体調記録 に次の内容を記録してください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
  - `体調記録 にこの記録を追加してください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
  - `体調記録 に次の内容を保存してください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
  - `体調記録 にこの情報を記録してください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
  - `体調記録 に次の内容を入力してください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
  - `体調記録 に次の記録を追加してください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
  - `体調記録 に次の内容を書き込んでください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
  - `体調記録 にこのエントリーを保存してください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
  - `この情報を 体調記録 に登録してください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
  - `体調記録 にこの内容を保存してください：おばあちゃん今日の体温は37.5度，軽いせき，水を飲んで休んでいる。`
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
  - `Show me what records are in health condition records.`
  - `List the records in health condition records.`
  - `What records are saved in health condition records?`
  - `Please display the records in health condition records.`
  - `Can you show the entries in health condition records?`
  - `I want to see the current records in health condition records.`
  - `Tell me what has been recorded in health condition records.`
  - `Please check the records in health condition records for me.`
  - `Show all record entries in health condition records.`
  - `Could you list the saved records in health condition records?`

- Japanese Variants: 10
  - `体調記録 にはどんな記録がありますか。`
  - `体調記録 の記録を一覧表示してください。`
  - `体調記録 に保存されている記録は何ですか。`
  - `体調記録 の記録を表示してください。`
  - `体調記録 のエントリーを見せてもらえますか。`
  - `体調記録 の現在の記録を見たいです。`
  - `体調記録 に何が記録されているか教えてください。`
  - `体調記録 の記録を確認してください。`
  - `体調記録 のすべての記録項目を見せてください。`
  - `体調記録 に保存された記録を一覧にしてもらえますか。`
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
  - `Export the health condition records document.`
  - `Please export the health condition records document.`
  - `Create an exported document for health condition records.`
  - `I want to export the health condition records document.`
  - `Generate an export file for health condition records.`
  - `Please create an export of health condition records.`
  - `Output health condition records as an exportable document.`
  - `Can you export health condition records for me?`
  - `Please generate the exported file for health condition records.`
  - `Make an export document for health condition records.`

- Japanese Variants: 10
  - `体調記録 の文書をエクスポートしてください。`
  - `体調記録 の文書を出力してください。`
  - `体調記録 のエクスポート用文書を作成してください。`
  - `体調記録 をエクスポートしたいです。`
  - `体調記録 のエクスポートファイルを生成してください。`
  - `体調記録 のエクスポートを作成してください。`
  - `体調記録 をエクスポート可能な文書として出力してください。`
  - `体調記録 をエクスポートしてもらえますか。`
  - `体調記録 の出力ファイルを生成してください。`
  - `体調記録 のエクスポート文書を作ってください。`
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
  - `Please record this in medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`
  - `Add this entry to medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`
  - `Please save the following in medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`
  - `Record this information in medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`
  - `Enter this into medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`
  - `Please add the following record to medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`
  - `Write this into medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`
  - `Save this entry in medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`
  - `Register this information in medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`
  - `Please store this in medical checkup reports: Momhad a blood test on April 20，the result showed low vitamin D，follow-up in one month.`

- Japanese Variants: 10
  - `健康診断レポート に次の内容を記録してください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
  - `健康診断レポート にこの記録を追加してください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
  - `健康診断レポート に次の内容を保存してください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
  - `健康診断レポート にこの情報を記録してください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
  - `健康診断レポート に次の内容を入力してください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
  - `健康診断レポート に次の記録を追加してください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
  - `健康診断レポート に次の内容を書き込んでください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
  - `健康診断レポート にこのエントリーを保存してください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
  - `この情報を 健康診断レポート に登録してください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
  - `健康診断レポート にこの内容を保存してください：お母さん4月20日に血液検査を受けた，結果はビタミンDがやや低かった，1か月後に再検査。`
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
  - `Show me what records are in medical checkup reports.`
  - `List the records in medical checkup reports.`
  - `What records are saved in medical checkup reports?`
  - `Please display the records in medical checkup reports.`
  - `Can you show the entries in medical checkup reports?`
  - `I want to see the current records in medical checkup reports.`
  - `Tell me what has been recorded in medical checkup reports.`
  - `Please check the records in medical checkup reports for me.`
  - `Show all record entries in medical checkup reports.`
  - `Could you list the saved records in medical checkup reports?`

- Japanese Variants: 10
  - `健康診断レポート にはどんな記録がありますか。`
  - `健康診断レポート の記録を一覧表示してください。`
  - `健康診断レポート に保存されている記録は何ですか。`
  - `健康診断レポート の記録を表示してください。`
  - `健康診断レポート のエントリーを見せてもらえますか。`
  - `健康診断レポート の現在の記録を見たいです。`
  - `健康診断レポート に何が記録されているか教えてください。`
  - `健康診断レポート の記録を確認してください。`
  - `健康診断レポート のすべての記録項目を見せてください。`
  - `健康診断レポート に保存された記録を一覧にしてもらえますか。`
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
  - `Export the medical checkup reports document.`
  - `Please export the medical checkup reports document.`
  - `Create an exported document for medical checkup reports.`
  - `I want to export the medical checkup reports document.`
  - `Generate an export file for medical checkup reports.`
  - `Please create an export of medical checkup reports.`
  - `Output medical checkup reports as an exportable document.`
  - `Can you export medical checkup reports for me?`
  - `Please generate the exported file for medical checkup reports.`
  - `Make an export document for medical checkup reports.`

- Japanese Variants: 10
  - `健康診断レポート の文書をエクスポートしてください。`
  - `健康診断レポート の文書を出力してください。`
  - `健康診断レポート のエクスポート用文書を作成してください。`
  - `健康診断レポート をエクスポートしたいです。`
  - `健康診断レポート のエクスポートファイルを生成してください。`
  - `健康診断レポート のエクスポートを作成してください。`
  - `健康診断レポート をエクスポート可能な文書として出力してください。`
  - `健康診断レポート をエクスポートしてもらえますか。`
  - `健康診断レポート の出力ファイルを生成してください。`
  - `健康診断レポート のエクスポート文書を作ってください。`
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
  - `Please record this in hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`
  - `Add this entry to hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`
  - `Please save the following in hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`
  - `Record this information in hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`
  - `Enter this into hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`
  - `Please add the following record to hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`
  - `Write this into hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`
  - `Save this entry in hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`
  - `Register this information in hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`
  - `Please store this in hospital follow-up reminders: Dada cardiology follow-up on April 18 at 9:00 a.m.，reminder method: HomeHub.`

- Japanese Variants: 10
  - `通院再診リマインダー に次の内容を記録してください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
  - `通院再診リマインダー にこの記録を追加してください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
  - `通院再診リマインダー に次の内容を保存してください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
  - `通院再診リマインダー にこの情報を記録してください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
  - `通院再診リマインダー に次の内容を入力してください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
  - `通院再診リマインダー に次の記録を追加してください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
  - `通院再診リマインダー に次の内容を書き込んでください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
  - `通院再診リマインダー にこのエントリーを保存してください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
  - `この情報を 通院再診リマインダー に登録してください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
  - `通院再診リマインダー にこの内容を保存してください：お父さん4月18日午前9時に循環器内科の再診，通知方法はHomeHub。`
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
  - `Show me what records are in hospital follow-up reminders.`
  - `List the records in hospital follow-up reminders.`
  - `What records are saved in hospital follow-up reminders?`
  - `Please display the records in hospital follow-up reminders.`
  - `Can you show the entries in hospital follow-up reminders?`
  - `I want to see the current records in hospital follow-up reminders.`
  - `Tell me what has been recorded in hospital follow-up reminders.`
  - `Please check the records in hospital follow-up reminders for me.`
  - `Show all record entries in hospital follow-up reminders.`
  - `Could you list the saved records in hospital follow-up reminders?`

- Japanese Variants: 10
  - `通院再診リマインダー にはどんな記録がありますか。`
  - `通院再診リマインダー の記録を一覧表示してください。`
  - `通院再診リマインダー に保存されている記録は何ですか。`
  - `通院再診リマインダー の記録を表示してください。`
  - `通院再診リマインダー のエントリーを見せてもらえますか。`
  - `通院再診リマインダー の現在の記録を見たいです。`
  - `通院再診リマインダー に何が記録されているか教えてください。`
  - `通院再診リマインダー の記録を確認してください。`
  - `通院再診リマインダー のすべての記録項目を見せてください。`
  - `通院再診リマインダー に保存された記録を一覧にしてもらえますか。`
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
  - `Export the hospital follow-up reminders document.`
  - `Please export the hospital follow-up reminders document.`
  - `Create an exported document for hospital follow-up reminders.`
  - `I want to export the hospital follow-up reminders document.`
  - `Generate an export file for hospital follow-up reminders.`
  - `Please create an export of hospital follow-up reminders.`
  - `Output hospital follow-up reminders as an exportable document.`
  - `Can you export hospital follow-up reminders for me?`
  - `Please generate the exported file for hospital follow-up reminders.`
  - `Make an export document for hospital follow-up reminders.`

- Japanese Variants: 10
  - `通院再診リマインダー の文書をエクスポートしてください。`
  - `通院再診リマインダー の文書を出力してください。`
  - `通院再診リマインダー のエクスポート用文書を作成してください。`
  - `通院再診リマインダー をエクスポートしたいです。`
  - `通院再診リマインダー のエクスポートファイルを生成してください。`
  - `通院再診リマインダー のエクスポートを作成してください。`
  - `通院再診リマインダー をエクスポート可能な文書として出力してください。`
  - `通院再診リマインダー をエクスポートしてもらえますか。`
  - `通院再診リマインダー の出力ファイルを生成してください。`
  - `通院再診リマインダー のエクスポート文書を作ってください。`
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
  - `Please record this in child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`
  - `Add this entry to child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`
  - `Please save the following in child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`
  - `Record this information in child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`
  - `Enter this into child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`
  - `Please add the following record to child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`
  - `Write this into child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`
  - `Save this entry in child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`
  - `Register this information in child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`
  - `Please store this in child study plan: Xiaomingcompleted 20 mental-math problems and English vocabulary review today，the teacher’s feedback was positive.`

- Japanese Variants: 10
  - `子どもの学習計画 に次の内容を記録してください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
  - `子どもの学習計画 にこの記録を追加してください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
  - `子どもの学習計画 に次の内容を保存してください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
  - `子どもの学習計画 にこの情報を記録してください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
  - `子どもの学習計画 に次の内容を入力してください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
  - `子どもの学習計画 に次の記録を追加してください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
  - `子どもの学習計画 に次の内容を書き込んでください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
  - `子どもの学習計画 にこのエントリーを保存してください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
  - `この情報を 子どもの学習計画 に登録してください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
  - `子どもの学習計画 にこの内容を保存してください：小明今日は算数の暗算20問と英単語の復習を終えた，先生からの評価は良好。`
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
  - `Show me what records are in child study plan.`
  - `List the records in child study plan.`
  - `What records are saved in child study plan?`
  - `Please display the records in child study plan.`
  - `Can you show the entries in child study plan?`
  - `I want to see the current records in child study plan.`
  - `Tell me what has been recorded in child study plan.`
  - `Please check the records in child study plan for me.`
  - `Show all record entries in child study plan.`
  - `Could you list the saved records in child study plan?`

- Japanese Variants: 10
  - `子どもの学習計画 にはどんな記録がありますか。`
  - `子どもの学習計画 の記録を一覧表示してください。`
  - `子どもの学習計画 に保存されている記録は何ですか。`
  - `子どもの学習計画 の記録を表示してください。`
  - `子どもの学習計画 のエントリーを見せてもらえますか。`
  - `子どもの学習計画 の現在の記録を見たいです。`
  - `子どもの学習計画 に何が記録されているか教えてください。`
  - `子どもの学習計画 の記録を確認してください。`
  - `子どもの学習計画 のすべての記録項目を見せてください。`
  - `子どもの学習計画 に保存された記録を一覧にしてもらえますか。`
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
  - `Export the child study plan spreadsheet.`
  - `Please export the child study plan spreadsheet.`
  - `Create an exported spreadsheet for child study plan.`
  - `I want to export the child study plan spreadsheet.`
  - `Generate an export file for child study plan.`
  - `Please create an export of child study plan.`
  - `Output child study plan as an exportable spreadsheet.`
  - `Can you export child study plan for me?`
  - `Please generate the exported file for child study plan.`
  - `Make an export spreadsheet for child study plan.`

- Japanese Variants: 10
  - `子どもの学習計画 の表をエクスポートしてください。`
  - `子どもの学習計画 の表を出力してください。`
  - `子どもの学習計画 のエクスポート用表を作成してください。`
  - `子どもの学習計画 をエクスポートしたいです。`
  - `子どもの学習計画 のエクスポートファイルを生成してください。`
  - `子どもの学習計画 のエクスポートを作成してください。`
  - `子どもの学習計画 をエクスポート可能な表として出力してください。`
  - `子どもの学習計画 をエクスポートしてもらえますか。`
  - `子どもの学習計画 の出力ファイルを生成してください。`
  - `子どもの学習計画 のエクスポート表を作ってください。`
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
  - `Please record this in family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`
  - `Add this entry to family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`
  - `Please save the following in family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`
  - `Record this information in family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`
  - `Enter this into family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`
  - `Please add the following record to family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`
  - `Write this into family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`
  - `Save this entry in family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`
  - `Register this information in family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`
  - `Please store this in family activity schedule: go for a picnic at Ueno Park on Sunday，参加成员DadMom和Xiaoming，remember to bring a water bottle.`

- Japanese Variants: 10
  - `家族活動予定 に次の内容を記録してください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
  - `家族活動予定 にこの記録を追加してください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
  - `家族活動予定 に次の内容を保存してください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
  - `家族活動予定 にこの情報を記録してください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
  - `家族活動予定 に次の内容を入力してください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
  - `家族活動予定 に次の記録を追加してください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
  - `家族活動予定 に次の内容を書き込んでください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
  - `家族活動予定 にこのエントリーを保存してください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
  - `この情報を 家族活動予定 に登録してください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
  - `家族活動予定 にこの内容を保存してください：日曜日に上野公園へピクニックに行く，参加成员お父さんお母さん和小明，水筒を持参すること。`
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
  - `Show me what records are in family activity schedule.`
  - `List the records in family activity schedule.`
  - `What records are saved in family activity schedule?`
  - `Please display the records in family activity schedule.`
  - `Can you show the entries in family activity schedule?`
  - `I want to see the current records in family activity schedule.`
  - `Tell me what has been recorded in family activity schedule.`
  - `Please check the records in family activity schedule for me.`
  - `Show all record entries in family activity schedule.`
  - `Could you list the saved records in family activity schedule?`

- Japanese Variants: 10
  - `家族活動予定 にはどんな記録がありますか。`
  - `家族活動予定 の記録を一覧表示してください。`
  - `家族活動予定 に保存されている記録は何ですか。`
  - `家族活動予定 の記録を表示してください。`
  - `家族活動予定 のエントリーを見せてもらえますか。`
  - `家族活動予定 の現在の記録を見たいです。`
  - `家族活動予定 に何が記録されているか教えてください。`
  - `家族活動予定 の記録を確認してください。`
  - `家族活動予定 のすべての記録項目を見せてください。`
  - `家族活動予定 に保存された記録を一覧にしてもらえますか。`
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
  - `Export the family activity schedule document.`
  - `Please export the family activity schedule document.`
  - `Create an exported document for family activity schedule.`
  - `I want to export the family activity schedule document.`
  - `Generate an export file for family activity schedule.`
  - `Please create an export of family activity schedule.`
  - `Output family activity schedule as an exportable document.`
  - `Can you export family activity schedule for me?`
  - `Please generate the exported file for family activity schedule.`
  - `Make an export document for family activity schedule.`

- Japanese Variants: 10
  - `家族活動予定 の文書をエクスポートしてください。`
  - `家族活動予定 の文書を出力してください。`
  - `家族活動予定 のエクスポート用文書を作成してください。`
  - `家族活動予定 をエクスポートしたいです。`
  - `家族活動予定 のエクスポートファイルを生成してください。`
  - `家族活動予定 のエクスポートを作成してください。`
  - `家族活動予定 をエクスポート可能な文書として出力してください。`
  - `家族活動予定 をエクスポートしてもらえますか。`
  - `家族活動予定 の出力ファイルを生成してください。`
  - `家族活動予定 のエクスポート文書を作ってください。`
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
  - `Please record this in family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`
  - `Add this entry to family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`
  - `Please save the following in family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`
  - `Record this information in family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`
  - `Enter this into family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`
  - `Please add the following record to family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`
  - `Write this into family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`
  - `Save this entry in family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`
  - `Register this information in family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`
  - `Please store this in family schedule: 周六下午2点家庭聚会在Grandma家，participants: the whole family，remember to bring a gift.`

- Japanese Variants: 10
  - `家族スケジュール に次の内容を記録してください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
  - `家族スケジュール にこの記録を追加してください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
  - `家族スケジュール に次の内容を保存してください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
  - `家族スケジュール にこの情報を記録してください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
  - `家族スケジュール に次の内容を入力してください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
  - `家族スケジュール に次の記録を追加してください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
  - `家族スケジュール に次の内容を書き込んでください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
  - `家族スケジュール にこのエントリーを保存してください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
  - `この情報を 家族スケジュール に登録してください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
  - `家族スケジュール にこの内容を保存してください：周六下午2点家庭聚会在おばあちゃん家，参加者は家族全員，プレゼントを持参すること。`
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
  - `Show me what records are in family schedule.`
  - `List the records in family schedule.`
  - `What records are saved in family schedule?`
  - `Please display the records in family schedule.`
  - `Can you show the entries in family schedule?`
  - `I want to see the current records in family schedule.`
  - `Tell me what has been recorded in family schedule.`
  - `Please check the records in family schedule for me.`
  - `Show all record entries in family schedule.`
  - `Could you list the saved records in family schedule?`

- Japanese Variants: 10
  - `家族スケジュール にはどんな記録がありますか。`
  - `家族スケジュール の記録を一覧表示してください。`
  - `家族スケジュール に保存されている記録は何ですか。`
  - `家族スケジュール の記録を表示してください。`
  - `家族スケジュール のエントリーを見せてもらえますか。`
  - `家族スケジュール の現在の記録を見たいです。`
  - `家族スケジュール に何が記録されているか教えてください。`
  - `家族スケジュール の記録を確認してください。`
  - `家族スケジュール のすべての記録項目を見せてください。`
  - `家族スケジュール に保存された記録を一覧にしてもらえますか。`
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
  - `Export the family schedule document.`
  - `Please export the family schedule document.`
  - `Create an exported document for family schedule.`
  - `I want to export the family schedule document.`
  - `Generate an export file for family schedule.`
  - `Please create an export of family schedule.`
  - `Output family schedule as an exportable document.`
  - `Can you export family schedule for me?`
  - `Please generate the exported file for family schedule.`
  - `Make an export document for family schedule.`

- Japanese Variants: 10
  - `家族スケジュール の文書をエクスポートしてください。`
  - `家族スケジュール の文書を出力してください。`
  - `家族スケジュール のエクスポート用文書を作成してください。`
  - `家族スケジュール をエクスポートしたいです。`
  - `家族スケジュール のエクスポートファイルを生成してください。`
  - `家族スケジュール のエクスポートを作成してください。`
  - `家族スケジュール をエクスポート可能な文書として出力してください。`
  - `家族スケジュール をエクスポートしてもらえますか。`
  - `家族スケジュール の出力ファイルを生成してください。`
  - `家族スケジュール のエクスポート文書を作ってください。`
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
  - `What is the total spending up to today? If it exceeds 2000 yen, create a reminder and send it to HomeHub.`
  - `Tell me the total expenses through today, and if they are over 2000 yen, send a reminder to HomeHub.`
  - `Please calculate the total spending so far; if it goes beyond 2000 yen, create a HomeHub reminder.`
  - `How much has been spent up to today? If the amount is above 2000 yen, notify HomeHub.`
  - `Give me today's cumulative spending, and trigger a reminder to HomeHub if it exceeds 2000 yen.`
  - `Please total the spending through today and send a reminder to HomeHub if the total is over 2000 yen.`
  - `Check the spending total up to today. If it is more than 2000 yen, create a reminder for HomeHub.`
  - `What is the running total of spending today? If it passes 2000 yen, send a HomeHub alert.`
  - `Calculate the total spent up to today and create a HomeHub reminder when it exceeds 2000 yen.`
  - `Please provide the total spending through today, and if it is above 2000 yen, send a reminder to HomeHub.`

- Japanese Variants: 10
  - `今日までの支出総額はいくらですか。2000 円を超えたらリマインダーを作成し、HomeHub に送ってください。`
  - `今日までの支出総額を教えてください。2000 円を超えた場合は HomeHub に通知してください。`
  - `これまでの支出を集計し、2000 円を超えたら HomeHub 用のリマインダーを作成してください。`
  - `今日までにいくら使いましたか。2000 円を上回ったら HomeHub に知らせてください。`
  - `本日までの累計支出を教えてください。2000 円を超えたら HomeHub へリマインダーを送ってください。`
  - `今日までの支出合計を計算し、2000 円を超える場合は HomeHub に通知してください。`
  - `今日までの支出総額を確認し、2000 円を超えたら HomeHub 向けのリマインダーを作成してください。`
  - `今日までの支出累計はいくらですか。2000 円を超えたら HomeHub にアラートを送ってください。`
  - `今日までの総支出を計算し、2000 円を超えた場合は HomeHub のリマインダーを作成してください。`
  - `今日までの支出総額を出して、2000 円を上回ったら HomeHub にリマインダーを送ってください。`
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
  - `Show me what records are in medical checkup reports.`
  - `List the records in medical checkup reports.`
  - `What records are saved in medical checkup reports?`
  - `Please display the records in medical checkup reports.`
  - `Can you show the entries in medical checkup reports?`
  - `I want to see the current records in medical checkup reports.`
  - `Tell me what has been recorded in medical checkup reports.`
  - `Please check the records in medical checkup reports for me.`
  - `Show all record entries in medical checkup reports.`
  - `Could you list the saved records in medical checkup reports?`

- Japanese Variants: 10
  - `健康診断レポート にはどんな記録がありますか。`
  - `健康診断レポート の記録を一覧表示してください。`
  - `健康診断レポート に保存されている記録は何ですか。`
  - `健康診断レポート の記録を表示してください。`
  - `健康診断レポート のエントリーを見せてもらえますか。`
  - `健康診断レポート の現在の記録を見たいです。`
  - `健康診断レポート に何が記録されているか教えてください。`
  - `健康診断レポート の記録を確認してください。`
  - `健康診断レポート のすべての記録項目を見せてください。`
  - `健康診断レポート に保存された記録を一覧にしてもらえますか。`
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
  - `Export the child study plan spreadsheet.`
  - `Please export the child study plan spreadsheet.`
  - `Create an exported spreadsheet for child study plan.`
  - `I want to export the child study plan spreadsheet.`
  - `Generate an export file for child study plan.`
  - `Please create an export of child study plan.`
  - `Output child study plan as an exportable spreadsheet.`
  - `Can you export child study plan for me?`
  - `Please generate the exported file for child study plan.`
  - `Make an export spreadsheet for child study plan.`

- Japanese Variants: 10
  - `子どもの学習計画 の表をエクスポートしてください。`
  - `子どもの学習計画 の表を出力してください。`
  - `子どもの学習計画 のエクスポート用表を作成してください。`
  - `子どもの学習計画 をエクスポートしたいです。`
  - `子どもの学習計画 のエクスポートファイルを生成してください。`
  - `子どもの学習計画 のエクスポートを作成してください。`
  - `子どもの学習計画 をエクスポート可能な表として出力してください。`
  - `子どもの学習計画 をエクスポートしてもらえますか。`
  - `子どもの学習計画 の出力ファイルを生成してください。`
  - `子どもの学習計画 のエクスポート表を作ってください。`
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
  - `Classify the files under /tmp/homehub-family-suite/ext-school and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/ext-school into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/ext-school by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/ext-school into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/ext-school and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/ext-school organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/ext-school by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/ext-school into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/ext-school.`
  - `Could you classify the files under /tmp/homehub-family-suite/ext-school and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/ext-school の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-school のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/ext-school の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-school のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/ext-school のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/ext-school の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/ext-school のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-school の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/ext-school のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-school の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /tmp/homehub-family-suite/ext-bills and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/ext-bills into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/ext-bills by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/ext-bills into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/ext-bills and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/ext-bills organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/ext-bills by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/ext-bills into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/ext-bills.`
  - `Could you classify the files under /tmp/homehub-family-suite/ext-bills and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/ext-bills の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-bills のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/ext-bills の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-bills のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/ext-bills のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/ext-bills の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/ext-bills のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-bills の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/ext-bills のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-bills の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /tmp/homehub-family-suite/ext-photos and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/ext-photos into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/ext-photos by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/ext-photos into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/ext-photos and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/ext-photos organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/ext-photos by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/ext-photos into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/ext-photos.`
  - `Could you classify the files under /tmp/homehub-family-suite/ext-photos and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/ext-photos の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-photos のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/ext-photos の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-photos のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/ext-photos のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/ext-photos の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/ext-photos のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-photos の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/ext-photos のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-photos の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /tmp/homehub-family-suite/ext-recipes and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/ext-recipes into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/ext-recipes by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/ext-recipes into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/ext-recipes and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/ext-recipes organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/ext-recipes by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/ext-recipes into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/ext-recipes.`
  - `Could you classify the files under /tmp/homehub-family-suite/ext-recipes and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/ext-recipes の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-recipes のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/ext-recipes の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-recipes のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/ext-recipes のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/ext-recipes の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/ext-recipes のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-recipes の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/ext-recipes のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-recipes の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /tmp/homehub-family-suite/ext-mixed and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/ext-mixed into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/ext-mixed by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/ext-mixed into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/ext-mixed and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/ext-mixed organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/ext-mixed by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/ext-mixed into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/ext-mixed.`
  - `Could you classify the files under /tmp/homehub-family-suite/ext-mixed and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/ext-mixed の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-mixed のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/ext-mixed の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-mixed のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/ext-mixed のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/ext-mixed の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/ext-mixed のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-mixed の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/ext-mixed のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-mixed の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /tmp/homehub-family-suite/ext-visitors and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/ext-visitors into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/ext-visitors by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/ext-visitors into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/ext-visitors and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/ext-visitors organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/ext-visitors by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/ext-visitors into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/ext-visitors.`
  - `Could you classify the files under /tmp/homehub-family-suite/ext-visitors and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/ext-visitors の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-visitors のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/ext-visitors の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-visitors のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/ext-visitors のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/ext-visitors の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/ext-visitors のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-visitors の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/ext-visitors のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-visitors の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /tmp/homehub-family-suite/ext-pet and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/ext-pet into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/ext-pet by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/ext-pet into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/ext-pet and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/ext-pet organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/ext-pet by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/ext-pet into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/ext-pet.`
  - `Could you classify the files under /tmp/homehub-family-suite/ext-pet and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/ext-pet の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-pet のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/ext-pet の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-pet のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/ext-pet のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/ext-pet の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/ext-pet のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-pet の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/ext-pet のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-pet の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /tmp/homehub-family-suite/ext-health and create new folders by type.`
  - `Please sort the files in /tmp/homehub-family-suite/ext-health into new folders based on file type.`
  - `Organize the files under /tmp/homehub-family-suite/ext-health by type and create separate folders.`
  - `Can you group the files in /tmp/homehub-family-suite/ext-health into new folders by category?`
  - `Please classify the files in /tmp/homehub-family-suite/ext-health and make new folders for each type.`
  - `I want the files under /tmp/homehub-family-suite/ext-health organized into new type-based folders.`
  - `Sort the files in /tmp/homehub-family-suite/ext-health by file type and create folders.`
  - `Please reorganize the files under /tmp/homehub-family-suite/ext-health into folders by type.`
  - `Create new folders by type for the files in /tmp/homehub-family-suite/ext-health.`
  - `Could you classify the files under /tmp/homehub-family-suite/ext-health and place them into new folders by type?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/ext-health の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-health のファイルを種類別に新しいフォルダへ整理してください。`
  - `/tmp/homehub-family-suite/ext-health の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-health のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/tmp/homehub-family-suite/ext-health のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/tmp/homehub-family-suite/ext-health の下にあるファイルを種類別フォルダに整理したいです。`
  - `/tmp/homehub-family-suite/ext-health のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-health の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/tmp/homehub-family-suite/ext-health のファイル用に種類別の新しいフォルダを作成してください。`
  - `/tmp/homehub-family-suite/ext-health の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読んでください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を開いて読んでください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の内容を見せてください。`
  - `ファイル /tmp/homehub-family-suite/family-reading/shopping-note.txt を読めますか。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の中身を見たいです。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を開いて内容を教えてください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の内容を確認してください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を読んで見せてください。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt の内容を表示してもらえますか。`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt を見て読み上げてください。`
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
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を読んでください。`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を開いて読んでください。`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md の内容を見せてください。`
  - `ファイル /tmp/homehub-family-suite/family-library/meal-plan.md を読めますか。`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md の中身を見たいです。`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を開いて内容を教えてください。`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md の内容を確認してください。`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を読んで見せてください。`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md の内容を表示してもらえますか。`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md を見て読み上げてください。`
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
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読んでください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を開いて読んでください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の内容を見せてください。`
  - `ファイル /tmp/homehub-family-suite/family-reading/recipe.json を読めますか。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の中身を見たいです。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を開いて内容を教えてください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の内容を確認してください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を読んで見せてください。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json の内容を表示してもらえますか。`
  - `/tmp/homehub-family-suite/family-reading/recipe.json を見て読み上げてください。`
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
  - `List the files under /tmp/homehub-family-suite/family-inbox, then send me receipt.pdf.`
  - `What files are in /tmp/homehub-family-suite/family-inbox? Please send me receipt.pdf.`
  - `Can you check /tmp/homehub-family-suite/family-inbox and share receipt.pdf with me?`
  - `Please look in /tmp/homehub-family-suite/family-inbox, list the files, and send me receipt.pdf.`
  - `I want to see the files in /tmp/homehub-family-suite/family-inbox; also send me receipt.pdf.`
  - `Open /tmp/homehub-family-suite/family-inbox, tell me what files are there, and send receipt.pdf.`
  - `Check the contents of /tmp/homehub-family-suite/family-inbox and forward receipt.pdf to me.`
  - `Could you list the files in /tmp/homehub-family-suite/family-inbox and send me receipt.pdf?`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and share the file receipt.pdf.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて、そのあと receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox の下にあるファイルを一覧表示してから、receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox にどんなファイルがあるか教えてください。あわせて receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox を確認して、receipt.pdf を共有してください。`
  - `/tmp/homehub-family-suite/family-inbox を見てファイル一覧を出し、そのうえで receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox のファイルを見たいです。あわせて receipt.pdf も送ってください。`
  - `/tmp/homehub-family-suite/family-inbox を開いて中のファイルを教え、そのあと receipt.pdf を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox の内容を確認して、receipt.pdf を転送してください。`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を出して、receipt.pdf を送ってもらえますか。`
  - `/tmp/homehub-family-suite/family-inbox を確認して、ファイル receipt.pdf を共有してください。`
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
  - `List the files under /tmp/homehub-family-suite/family-inbox, then send me monthly_budget.xlsx.`
  - `What files are in /tmp/homehub-family-suite/family-inbox? Please send me monthly_budget.xlsx.`
  - `Can you check /tmp/homehub-family-suite/family-inbox and share monthly_budget.xlsx with me?`
  - `Please look in /tmp/homehub-family-suite/family-inbox, list the files, and send me monthly_budget.xlsx.`
  - `I want to see the files in /tmp/homehub-family-suite/family-inbox; also send me monthly_budget.xlsx.`
  - `Open /tmp/homehub-family-suite/family-inbox, tell me what files are there, and send monthly_budget.xlsx.`
  - `Check the contents of /tmp/homehub-family-suite/family-inbox and forward monthly_budget.xlsx to me.`
  - `Could you list the files in /tmp/homehub-family-suite/family-inbox and send me monthly_budget.xlsx?`
  - `Please inspect /tmp/homehub-family-suite/family-inbox and share the file monthly_budget.xlsx.`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せて、そのあと monthly_budget.xlsx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox の下にあるファイルを一覧表示してから、monthly_budget.xlsx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox にどんなファイルがあるか教えてください。あわせて monthly_budget.xlsx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox を確認して、monthly_budget.xlsx を共有してください。`
  - `/tmp/homehub-family-suite/family-inbox を見てファイル一覧を出し、そのうえで monthly_budget.xlsx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox のファイルを見たいです。あわせて monthly_budget.xlsx も送ってください。`
  - `/tmp/homehub-family-suite/family-inbox を開いて中のファイルを教え、そのあと monthly_budget.xlsx を送ってください。`
  - `/tmp/homehub-family-suite/family-inbox の内容を確認して、monthly_budget.xlsx を転送してください。`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧を出して、monthly_budget.xlsx を送ってもらえますか。`
  - `/tmp/homehub-family-suite/family-inbox を確認して、ファイル monthly_budget.xlsx を共有してください。`
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
  - `Search for meal files under /tmp/homehub-family-suite/family-library.`
  - `Find the meal files in /tmp/homehub-family-suite/family-library.`
  - `Please look through /tmp/homehub-family-suite/family-library for files matching meal.`
  - `Can you search /tmp/homehub-family-suite/family-library for any meal files?`
  - `Show me files related to meal under /tmp/homehub-family-suite/family-library.`
  - `I need you to find meal-related files in /tmp/homehub-family-suite/family-library.`
  - `Please check /tmp/homehub-family-suite/family-library and search for meal files.`
  - `Look in /tmp/homehub-family-suite/family-library for anything named meal.`
  - `Search the folder /tmp/homehub-family-suite/family-library for meal.`
  - `Could you find files connected to meal in /tmp/homehub-family-suite/family-library?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-library の下で meal ファイルを検索してください。`
  - `/tmp/homehub-family-suite/family-library で meal ファイルを探してください。`
  - `/tmp/homehub-family-suite/family-library の中から meal に一致するファイルを探してください。`
  - `/tmp/homehub-family-suite/family-library に meal ファイルがあるか検索してください。`
  - `/tmp/homehub-family-suite/family-library の下にある meal 関連のファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-library の中で meal に関係するファイルを見つけてください。`
  - `/tmp/homehub-family-suite/family-library を確認して meal ファイルを検索してください。`
  - `/tmp/homehub-family-suite/family-library で名前に meal を含むものを探してください。`
  - `フォルダ /tmp/homehub-family-suite/family-library で meal を検索してください。`
  - `/tmp/homehub-family-suite/family-library の中で meal に関連するファイルを見つけてもらえますか。`
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
  - `Search for photo files under /tmp/homehub-family-suite/family-library.`
  - `Find the photo files in /tmp/homehub-family-suite/family-library.`
  - `Please look through /tmp/homehub-family-suite/family-library for files matching photo.`
  - `Can you search /tmp/homehub-family-suite/family-library for any photo files?`
  - `Show me files related to photo under /tmp/homehub-family-suite/family-library.`
  - `I need you to find photo-related files in /tmp/homehub-family-suite/family-library.`
  - `Please check /tmp/homehub-family-suite/family-library and search for photo files.`
  - `Look in /tmp/homehub-family-suite/family-library for anything named photo.`
  - `Search the folder /tmp/homehub-family-suite/family-library for photo.`
  - `Could you find files connected to photo in /tmp/homehub-family-suite/family-library?`

- Japanese Variants: 10
  - `/tmp/homehub-family-suite/family-library の下で photo ファイルを検索してください。`
  - `/tmp/homehub-family-suite/family-library で photo ファイルを探してください。`
  - `/tmp/homehub-family-suite/family-library の中から photo に一致するファイルを探してください。`
  - `/tmp/homehub-family-suite/family-library に photo ファイルがあるか検索してください。`
  - `/tmp/homehub-family-suite/family-library の下にある photo 関連のファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-library の中で photo に関係するファイルを見つけてください。`
  - `/tmp/homehub-family-suite/family-library を確認して photo ファイルを検索してください。`
  - `/tmp/homehub-family-suite/family-library で名前に photo を含むものを探してください。`
  - `フォルダ /tmp/homehub-family-suite/family-library で photo を検索してください。`
  - `/tmp/homehub-family-suite/family-library の中で photo に関連するファイルを見つけてもらえますか。`
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
  - `/tmp/homehub-family-suite/family-inbox にあるファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-inbox の下にあるファイルを一覧にしてください。`
  - `/tmp/homehub-family-suite/family-inbox にはどんなファイルがありますか。`
  - `/tmp/homehub-family-suite/family-inbox の中にあるファイルを確認してください。`
  - `/tmp/homehub-family-suite/family-inbox の下にあるファイルを教えてください。`
  - `/tmp/homehub-family-suite/family-inbox の内容を見たいです。`
  - `/tmp/homehub-family-suite/family-inbox を開いて中のファイルを一覧表示してください。`
  - `/tmp/homehub-family-suite/family-inbox を確認してファイルを見せてください。`
  - `/tmp/homehub-family-suite/family-inbox のファイル一覧をください。`
  - `/tmp/homehub-family-suite/family-inbox の中にどんなファイルがあるか教えてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `Classify the files under /Users/home/Documents and create new folders by type.`
  - `Please sort the files in /Users/home/Documents into new folders based on file type.`
  - `Organize the files under /Users/home/Documents by type and create separate folders.`
  - `Can you group the files in /Users/home/Documents into new folders by category?`
  - `Please classify the files in /Users/home/Documents and make new folders for each type.`
  - `I want the files under /Users/home/Documents organized into new type-based folders.`
  - `Sort the files in /Users/home/Documents by file type and create folders.`
  - `Please reorganize the files under /Users/home/Documents into folders by type.`
  - `Create new folders by type for the files in /Users/home/Documents.`
  - `Could you classify the files under /Users/home/Documents and place them into new folders by type?`

- Japanese Variants: 10
  - `/Users/home/Documents の下にあるファイルを分類し、種類ごとに新しいフォルダを作成してください。`
  - `/Users/home/Documents のファイルを種類別に新しいフォルダへ整理してください。`
  - `/Users/home/Documents の下にあるファイルをタイプごとに分けて、別々のフォルダを作成してください。`
  - `/Users/home/Documents のファイルをカテゴリごとに新しいフォルダへまとめてもらえますか。`
  - `/Users/home/Documents のファイルを分類し、各タイプごとに新しいフォルダを作ってください。`
  - `/Users/home/Documents の下にあるファイルを種類別フォルダに整理したいです。`
  - `/Users/home/Documents のファイルをファイル形式ごとに整理してフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを種類ごとのフォルダに再整理してください。`
  - `/Users/home/Documents のファイル用に種類別の新しいフォルダを作成してください。`
  - `/Users/home/Documents の下にあるファイルを分類して、新しいフォルダへ種類別に入れてください。`
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
  - `What is the weather like in Tokyo today?`
  - `Can you check today's weather in Tokyo?`
  - `Tell me today's temperature in Tokyo.`
  - `How's the weather in Tokyo today?`
  - `Please give me today's forecast for Tokyo.`
  - `What's the high temperature in Tokyo today?`
  - `Tell me today's high and low temperatures in Tokyo.`
  - `How warm will it get in Tokyo today?`
  - `Please check today's forecast and temperatures for Tokyo.`
  - `I'd like today's weather and temperature details for Tokyo.`

- Japanese Variants: 10
  - `東京の今日の天気を教えてください。`
  - `東京の今日の天気を確認してください。`
  - `東京の今日の気温を教えてください。`
  - `東京の今日の天気はどうですか。`
  - `東京の今日の天気予報を教えてください。`
  - `東京の今日の最高気温は何度ですか。`
  - `東京の今日の最高気温と最低気温を教えてください。`
  - `東京は今日どれくらい暖かくなりますか。`
  - `東京の今日の予報と気温を確認してください。`
  - `東京の今日の天気と気温の詳細を知りたいです。`
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
  - `Will it rain in Fukuoka today?`
  - `Can you check whether it will rain in Fukuoka today?`
  - `Please tell me today's weather in Fukuoka and whether rain is expected.`
  - `Show me today's forecast for Fukuoka, including the chance of rain.`
  - `Is rain expected in Fukuoka today?`
  - `Tell me the temperature and rain forecast for Fukuoka today.`
  - `Please check today's weather in Fukuoka, especially the rain forecast.`
  - `What will the weather be like in Fukuoka today? Will it rain?`
  - `I'd like today's weather and rain information for Fukuoka.`
  - `Can you give me today's forecast for Fukuoka, including rain and temperature?`

- Japanese Variants: 10
  - `福岡は今日、雨が降りますか。`
  - `福岡の今日の雨予報を確認してください。`
  - `福岡の今日の天気と雨の情報を教えてください。`
  - `福岡の今日の降水確率を見せてください。`
  - `福岡では今日、雨の予報がありますか。`
  - `福岡の今日の気温と雨予報を教えてください。`
  - `福岡の今日の天気を、雨を中心に確認してください。`
  - `福岡の今日の天気はどうですか。雨は降りますか。`
  - `福岡の今日の天気と降雨情報を知りたいです。`
  - `福岡の今日の予報を、気温と雨を含めて教えてください。`
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
  - `What is the weather like in Osaka today?`
  - `Can you check today's weather in Osaka?`
  - `Tell me today's temperature in Osaka.`
  - `How's the weather in Osaka today?`
  - `Please give me today's forecast for Osaka.`
  - `What's the high temperature in Osaka today?`
  - `Tell me today's high and low temperatures in Osaka.`
  - `How warm will it get in Osaka today?`
  - `Please check today's forecast and temperatures for Osaka.`
  - `I'd like today's weather and temperature details for Osaka.`

- Japanese Variants: 10
  - `大阪の今日の天気を教えてください。`
  - `大阪の今日の天気を確認してください。`
  - `大阪の今日の気温を教えてください。`
  - `大阪の今日の天気はどうですか。`
  - `大阪の今日の天気予報を教えてください。`
  - `大阪の今日の最高気温は何度ですか。`
  - `大阪の今日の最高気温と最低気温を教えてください。`
  - `大阪は今日どれくらい暖かくなりますか。`
  - `大阪の今日の予報と気温を確認してください。`
  - `大阪の今日の天気と気温の詳細を知りたいです。`
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
  - `Please check the flight times and ticket prices from Tokyo to San Francisco for May 31, 2026.`
  - `Look up the approximate flight schedule and fares from Tokyo to San Francisco for May 31, 2026.`
  - `I'd like to know the flight times and prices from Tokyo to San Francisco for May 31, 2026.`
  - `Can you find reliable flight times and ticket prices from Tokyo to San Francisco for May 31, 2026?`
  - `Please show me the departure times and fares from Tokyo to San Francisco for May 31, 2026.`
  - `Check the flight options, times, and prices from Tokyo to San Francisco for May 31, 2026.`
  - `Tell me the likely flight schedule and cost from Tokyo to San Francisco for May 31, 2026.`
  - `Please search for airfare and flight times from Tokyo to San Francisco for May 31, 2026.`
  - `I want to see the available flight times and ticket prices from Tokyo to San Francisco for May 31, 2026.`
  - `Find trustworthy sources for flight times and prices from Tokyo to San Francisco for May 31, 2026.`

- Japanese Variants: 10
  - `東京からサンフランシスコ の 2026年5月31日 の便について、フライト時間と航空券の料金を調べてください。`
  - `東京からサンフランシスコ の 2026年5月31日 のおおよその便スケジュールと運賃を調べてください。`
  - `東京からサンフランシスコ の 2026年5月31日 のフライト時間と料金を知りたいです。`
  - `東京からサンフランシスコ の 2026年5月31日 の便について、信頼できる時間と料金情報を探してください。`
  - `東京からサンフランシスコ の 2026年5月31日 の出発時刻と料金を見せてください。`
  - `東京からサンフランシスコ の 2026年5月31日 の便の候補、時間、価格を確認してください。`
  - `東京からサンフランシスコ の 2026年5月31日 の大まかなフライト予定と費用を教えてください。`
  - `東京からサンフランシスコ の 2026年5月31日 の航空券価格と便の時間を検索してください。`
  - `東京からサンフランシスコ の 2026年5月31日 の利用可能な便の時間と料金を見たいです。`
  - `東京からサンフランシスコ の 2026年5月31日 の時間と価格について、信頼できる情報源を探してください。`
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
  - `Please check the train times and fares from Fukuoka to Osaka for April 20, 2026.`
  - `Look up the schedule and ticket costs from Fukuoka to Osaka for April 20, 2026.`
  - `I'd like to know the train times and prices from Fukuoka to Osaka for April 20, 2026.`
  - `Can you find the train timetable and fares from Fukuoka to Osaka for April 20, 2026?`
  - `Please show me the departure times and prices from Fukuoka to Osaka for April 20, 2026.`
  - `Check the train options, times, and costs from Fukuoka to Osaka for April 20, 2026.`
  - `Tell me the likely train schedule and fare from Fukuoka to Osaka for April 20, 2026.`
  - `Please search for train tickets and times from Fukuoka to Osaka for April 20, 2026.`
  - `I want to see the available train times and ticket prices from Fukuoka to Osaka for April 20, 2026.`
  - `Find trustworthy sources for train times and fares from Fukuoka to Osaka for April 20, 2026.`

- Japanese Variants: 10
  - `福岡から大阪 の 2026年4月20日 の列車について、時間と料金を調べてください。`
  - `福岡から大阪 の 2026年4月20日 の時刻表とチケット代を調べてください。`
  - `福岡から大阪 の 2026年4月20日 の列車時間と料金を知りたいです。`
  - `福岡から大阪 の 2026年4月20日 の列車の時刻と運賃を探してください。`
  - `福岡から大阪 の 2026年4月20日 の出発時刻と価格を見せてください。`
  - `福岡から大阪 の 2026年4月20日 の列車候補、時間、費用を確認してください。`
  - `福岡から大阪 の 2026年4月20日 の大まかな時刻と運賃を教えてください。`
  - `福岡から大阪 の 2026年4月20日 の列車チケットと時刻を検索してください。`
  - `福岡から大阪 の 2026年4月20日 の利用可能な列車時間とチケット価格を見たいです。`
  - `福岡から大阪 の 2026年4月20日 の時間と料金について、信頼できる情報源を探してください。`
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
  - `For everyday office work, which is more suitable: MacBook Air or MacBook Pro? Please base the advice on Apple's official website.`
  - `Please compare MacBook Air and MacBook Pro for daily office use, using Apple’s official information.`
  - `I want a recommendation between MacBook Air and MacBook Pro for normal office work, based on Apple’s website.`
  - `Can you advise whether MacBook Air or MacBook Pro is better for everyday work, referring to Apple’s official site?`
  - `Please tell me which is a better fit for regular office tasks: MacBook Air or MacBook Pro, based on Apple’s website.`
  - `Using Apple’s official website as a reference, recommend MacBook Air or MacBook Pro for daily office use.`
  - `Help me decide between MacBook Air and MacBook Pro for everyday office work with Apple’s official guidance.`
  - `Please compare the two models for common office tasks and recommend one based on Apple’s official information.`
  - `For day-to-day office use, which should I buy, a MacBook Air or a MacBook Pro? Please use Apple’s official site.`
  - `Give me a recommendation for MacBook Air vs. MacBook Pro for routine office work, using Apple’s official website.`

- Japanese Variants: 10
  - `日常的なオフィス作業には MacBook Air と MacBook Pro のどちらが適していますか。Apple 公式サイトを参考に教えてください。`
  - `普段の事務作業向けに、MacBook Air と MacBook Pro を Apple 公式情報に基づいて比較してください。`
  - `通常のオフィス用途では MacBook Air と MacBook Pro のどちらがおすすめか、Apple 公式サイトをもとに知りたいです。`
  - `日常業務には MacBook Air と MacBook Pro のどちらがよいか、Apple 公式サイトを参照してアドバイスしてください。`
  - `一般的なオフィス作業には MacBook Air と MacBook Pro のどちらが向いているか、Apple 公式サイトをもとに教えてください。`
  - `Apple 公式サイトを参考に、日常業務向けに MacBook Air と MacBook Pro のおすすめを出してください。`
  - `毎日のオフィスワーク向けに、MacBook Air と MacBook Pro のどちらを選ぶべきか Apple 公式情報で判断したいです。`
  - `一般的な事務作業向けに 2 つのモデルを比較し、Apple 公式情報に基づいておすすめしてください。`
  - `日々のオフィス利用なら MacBook Air と MacBook Pro のどちらを買うべきですか。Apple 公式サイトを使って教えてください。`
  - `通常のオフィス作業向けに、MacBook Air と MacBook Pro のどちらがよいか Apple 公式サイトをもとに提案してください。`
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
  - `What is the starting price of the 13-inch MacBook Air on Apple’s official website?`
  - `Please tell me the base price of the 13-inch MacBook Air on Apple’s website.`
  - `I want to know the starting price of the 13-inch MacBook Air from Apple’s official site.`
  - `Can you check the official starting price of the 13-inch MacBook Air on Apple’s website?`
  - `Please look up the Apple website price for the 13-inch MacBook Air.`
  - `Tell me the official starting price for the 13-inch MacBook Air.`
  - `What does Apple’s official website list as the starting price for the 13-inch MacBook Air?`
  - `Please check Apple’s website and tell me the starting price of the 13-inch MacBook Air.`
  - `I’d like the official base price of the 13-inch MacBook Air.`
  - `Can you find the 13-inch MacBook Air starting price on Apple’s official website?`

- Japanese Variants: 10
  - `Apple 公式サイトで 13 インチ MacBook Air の開始価格はいくらですか。`
  - `Apple 公式サイトにある 13 インチ MacBook Air の価格を教えてください。`
  - `13 インチ MacBook Air の Apple 公式での開始価格を知りたいです。`
  - `Apple 公式サイトで 13 インチ MacBook Air の開始価格を確認してください。`
  - `Apple 公式サイトの 13 インチ MacBook Air の価格を調べてください。`
  - `13 インチ MacBook Air の公式開始価格を教えてください。`
  - `Apple 公式サイトでは 13 インチ MacBook Air の開始価格はいくらになっていますか。`
  - `Apple 公式サイトを確認して、13 インチ MacBook Air の開始価格を教えてください。`
  - `13 インチ MacBook Air の公式のベース価格を知りたいです。`
  - `Apple 公式サイトで 13 インチ MacBook Air の開始価格を探してください。`
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
  - `What is the starting price of the 14-inch MacBook Pro on Apple’s official website?`
  - `Please tell me the base price of the 14-inch MacBook Pro on Apple’s website.`
  - `I want to know the starting price of the 14-inch MacBook Pro from Apple’s official site.`
  - `Can you check the official starting price of the 14-inch MacBook Pro on Apple’s website?`
  - `Please look up the Apple website price for the 14-inch MacBook Pro.`
  - `Tell me the official starting price for the 14-inch MacBook Pro.`
  - `What does Apple’s official website list as the starting price for the 14-inch MacBook Pro?`
  - `Please check Apple’s website and tell me the starting price of the 14-inch MacBook Pro.`
  - `I’d like the official base price of the 14-inch MacBook Pro.`
  - `Can you find the 14-inch MacBook Pro starting price on Apple’s official website?`

- Japanese Variants: 10
  - `Apple 公式サイトで 14 インチ MacBook Pro の開始価格はいくらですか。`
  - `Apple 公式サイトにある 14 インチ MacBook Pro の価格を教えてください。`
  - `14 インチ MacBook Pro の Apple 公式での開始価格を知りたいです。`
  - `Apple 公式サイトで 14 インチ MacBook Pro の開始価格を確認してください。`
  - `Apple 公式サイトの 14 インチ MacBook Pro の価格を調べてください。`
  - `14 インチ MacBook Pro の公式開始価格を教えてください。`
  - `Apple 公式サイトでは 14 インチ MacBook Pro の開始価格はいくらになっていますか。`
  - `Apple 公式サイトを確認して、14 インチ MacBook Pro の開始価格を教えてください。`
  - `14 インチ MacBook Pro の公式のベース価格を知りたいです。`
  - `Apple 公式サイトで 14 インチ MacBook Pro の開始価格を探してください。`
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
  - `what is Time Machine and what is it used for?`
  - `please explain what Time Machine is and what it does.`
  - `I'd like to know what Time Machine means and what its purpose is.`
  - `can you tell me what Time Machine is mainly used for?`
  - `please explain the role of Time Machine.`
  - `what exactly is Time Machine?`
  - `help me understand what Time Machine does.`
  - `please tell me the purpose of Time Machine.`
  - `what is the main function of Time Machine?`
  - `explain Time Machine in simple terms.`

- Japanese Variants: 10
  - `Time Machine とは何か、何に使うのか教えてください。`
  - `Time Machine が何で、どんな働きをするのか説明してください。`
  - `Time Machine の意味と目的を知りたいです。`
  - `Time Machine が主に何に使われるのか教えてもらえますか。`
  - `Time Machine の役割を説明してください。`
  - `Time Machine とは具体的に何ですか。`
  - `Time Machine が何をするのか分かるように教えてください。`
  - `Time Machine の目的を教えてください。`
  - `Time Machine の主な機能は何ですか。`
  - `Time Machine を分かりやすく説明してください。`
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
  - `Please search online for what a Liquid Retina display is.`
  - `What is a Liquid Retina display? Please search online.`
  - `I'd like to know what Liquid Retina means. Please look it up online.`
  - `Can you explain what a Liquid Retina display is by searching the web?`
  - `Please tell me what Liquid Retina display technology is.`
  - `Search online and explain what a Liquid Retina display is.`
  - `Help me understand what Liquid Retina display means.`
  - `What exactly is a Liquid Retina display?`
  - `Please look up Liquid Retina display and explain it.`
  - `Explain Liquid Retina display in simple terms after searching online.`

- Japanese Variants: 10
  - `Liquid Retina ディスプレイとは何か、ネットで調べてください。`
  - `Liquid Retina ディスプレイとは何ですか。ネット検索して教えてください。`
  - `Liquid Retina の意味を知りたいです。オンラインで調べてください。`
  - `Web 検索をして、Liquid Retina ディスプレイとは何か説明してください。`
  - `Liquid Retina ディスプレイ技術とは何か教えてください。`
  - `ネットで調べて、Liquid Retina ディスプレイを説明してください。`
  - `Liquid Retina ディスプレイの意味が分かるように教えてください。`
  - `Liquid Retina ディスプレイとは具体的に何ですか。`
  - `Liquid Retina ディスプレイを調べて説明してください。`
  - `ネット検索のうえ、Liquid Retina ディスプレイを分かりやすく説明してください。`
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
  - `Based on the local knowledge base, what is Time Machine and what is it used for?`
  - `Based on the local knowledge base, please explain what Time Machine is and what it does.`
  - `Based on the local knowledge base, I'd like to know what Time Machine means and what its purpose is.`
  - `Based on the local knowledge base, can you tell me what Time Machine is mainly used for?`
  - `Based on the local knowledge base, please explain the role of Time Machine.`
  - `Based on the local knowledge base, what exactly is Time Machine?`
  - `Based on the local knowledge base, help me understand what Time Machine does.`
  - `Based on the local knowledge base, please tell me the purpose of Time Machine.`
  - `Based on the local knowledge base, what is the main function of Time Machine?`
  - `Based on the local knowledge base, explain Time Machine in simple terms.`

- Japanese Variants: 10
  - `ローカル知識ベースに基づいて、Time Machine とは何か、何に使うのか教えてください。`
  - `ローカル知識ベースに基づいて、Time Machine が何で、どんな働きをするのか説明してください。`
  - `ローカル知識ベースに基づいて、Time Machine の意味と目的を知りたいです。`
  - `ローカル知識ベースに基づいて、Time Machine が主に何に使われるのか教えてもらえますか。`
  - `ローカル知識ベースに基づいて、Time Machine の役割を説明してください。`
  - `ローカル知識ベースに基づいて、Time Machine とは具体的に何ですか。`
  - `ローカル知識ベースに基づいて、Time Machine が何をするのか分かるように教えてください。`
  - `ローカル知識ベースに基づいて、Time Machine の目的を教えてください。`
  - `ローカル知識ベースに基づいて、Time Machine の主な機能は何ですか。`
  - `ローカル知識ベースに基づいて、Time Machine を分かりやすく説明してください。`
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
  - `What is the weather like in Tokyo today?`
  - `Can you check today's weather in Tokyo?`
  - `Tell me today's temperature in Tokyo.`
  - `How's the weather in Tokyo today?`
  - `Please give me today's forecast for Tokyo.`
  - `What's the high temperature in Tokyo today?`
  - `Tell me today's high and low temperatures in Tokyo.`
  - `How warm will it get in Tokyo today?`
  - `Please check today's forecast and temperatures for Tokyo.`
  - `I'd like today's weather and temperature details for Tokyo.`

- Japanese Variants: 10
  - `東京の今日の天気を教えてください。`
  - `東京の今日の天気を確認してください。`
  - `東京の今日の気温を教えてください。`
  - `東京の今日の天気はどうですか。`
  - `東京の今日の天気予報を教えてください。`
  - `東京の今日の最高気温は何度ですか。`
  - `東京の今日の最高気温と最低気温を教えてください。`
  - `東京は今日どれくらい暖かくなりますか。`
  - `東京の今日の予報と気温を確認してください。`
  - `東京の今日の天気と気温の詳細を知りたいです。`
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
  - `Will it rain in Tokyo today?`
  - `Can you check whether it will rain in Tokyo today?`
  - `Please tell me today's weather in Tokyo and whether rain is expected.`
  - `Show me today's forecast for Tokyo, including the chance of rain.`
  - `Is rain expected in Tokyo today?`
  - `Tell me the temperature and rain forecast for Tokyo today.`
  - `Please check today's weather in Tokyo, especially the rain forecast.`
  - `What will the weather be like in Tokyo today? Will it rain?`
  - `I'd like today's weather and rain information for Tokyo.`
  - `Can you give me today's forecast for Tokyo, including rain and temperature?`

- Japanese Variants: 10
  - `東京は今日、雨が降りますか。`
  - `東京の今日の雨予報を確認してください。`
  - `東京の今日の天気と雨の情報を教えてください。`
  - `東京の今日の降水確率を見せてください。`
  - `東京では今日、雨の予報がありますか。`
  - `東京の今日の気温と雨予報を教えてください。`
  - `東京の今日の天気を、雨を中心に確認してください。`
  - `東京の今日の天気はどうですか。雨は降りますか。`
  - `東京の今日の天気と降雨情報を知りたいです。`
  - `東京の今日の予報を、気温と雨を含めて教えてください。`
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
  - `what is Time Machine and what is it used for?`
  - `please explain what Time Machine is and what it does.`
  - `I'd like to know what Time Machine means and what its purpose is.`
  - `can you tell me what Time Machine is mainly used for?`
  - `please explain the role of Time Machine.`
  - `what exactly is Time Machine?`
  - `help me understand what Time Machine does.`
  - `please tell me the purpose of Time Machine.`
  - `what is the main function of Time Machine?`
  - `explain Time Machine in simple terms.`

- Japanese Variants: 10
  - `Time Machine とは何か、何に使うのか教えてください。`
  - `Time Machine が何で、どんな働きをするのか説明してください。`
  - `Time Machine の意味と目的を知りたいです。`
  - `Time Machine が主に何に使われるのか教えてもらえますか。`
  - `Time Machine の役割を説明してください。`
  - `Time Machine とは具体的に何ですか。`
  - `Time Machine が何をするのか分かるように教えてください。`
  - `Time Machine の目的を教えてください。`
  - `Time Machine の主な機能は何ですか。`
  - `Time Machine を分かりやすく説明してください。`
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
  - `I'd like a chicken curry recipe for tonight's family dinner. Please search online and tell me the main ingredients and steps.`
  - `Please find an online chicken curry recipe for tonight's family dinner, including the main ingredients and method.`
  - `Can you give me a chicken curry recipe for tonight and list the main ingredients and cooking steps?`
  - `Please look up a chicken curry recipe online for family dinner tonight.`
  - `I want to make chicken curry for dinner tonight. Please tell me the ingredients and how to make it.`
  - `Search online for a chicken curry recipe and explain the key ingredients and directions.`
  - `Please recommend a chicken curry recipe for tonight's dinner and include the main ingredients and steps.`
  - `Help me find a reliable chicken curry recipe online for tonight's family meal.`
  - `Can you look up how to make chicken curry tonight and list the ingredients and method?`
  - `Please search for a chicken curry recipe online and summarize the ingredients and cooking process.`

- Japanese Variants: 10
  - `今夜の家族の夕食にチキンカレーを作りたいので、ネットでレシピを調べて主な材料と作り方を教えてください。`
  - `今夜の家族の夕食向けに、オンラインでチキンカレーのレシピを探して、主な材料と手順を教えてください。`
  - `今夜のチキンカレーのレシピと、主な材料・作り方を教えてもらえますか。`
  - `今夜の家族の夕食用に、ネットでチキンカレーのレシピを調べてください。`
  - `今夜はチキンカレーを作りたいです。材料と作り方を教えてください。`
  - `ネットでチキンカレーのレシピを探して、主な材料と手順を説明してください。`
  - `今夜の夕食向けにおすすめのチキンカレーレシピを教えて、主な材料と手順も含めてください。`
  - `今夜の家族の食事向けに、信頼できるチキンカレーのレシピをネットで探してください。`
  - `今夜のチキンカレーの作り方を調べて、材料と手順を一覧にしてください。`
  - `ネットでチキンカレーのレシピを検索し、材料と調理手順を要約してください。`
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
  - `Please find a simple breakfast recipe suitable for an elementary school child before school, with ingredients and steps.`
  - `I need an easy breakfast recipe for a child before school. Please give me the ingredients and steps.`
  - `Can you search for a simple breakfast recipe for elementary school kids and list the ingredients and method?`
  - `Please recommend a quick breakfast recipe suitable for a school-age child, including ingredients and instructions.`
  - `I want a simple breakfast recipe for a child before school. Please tell me the ingredients and steps.`
  - `Find an easy breakfast recipe for elementary school children and explain how to make it.`
  - `Please look up a kid-friendly breakfast recipe for before school and include the ingredients and steps.`
  - `Help me find a simple breakfast idea for a child before school, with ingredients and directions.`
  - `Can you suggest an easy breakfast for an elementary school student and tell me the ingredients and procedure?`
  - `Please search for a breakfast recipe suitable for children going to school and summarize the ingredients and method.`

- Japanese Variants: 10
  - `小学生が登校前に食べやすい簡単な朝食レシピを探して、材料と手順を教えてください。`
  - `登校前の子ども向けに、簡単な朝食レシピと材料・作り方を教えてください。`
  - `小学生向けの簡単な朝食レシピを検索して、材料と手順を一覧にしてください。`
  - `通学前の子どもに合う手軽な朝食レシピを、材料と作り方つきでおすすめしてください。`
  - `登校前の子ども向けに、簡単な朝食レシピを知りたいです。材料と手順を教えてください。`
  - `小学生向けの簡単な朝食レシピを探して、作り方を説明してください。`
  - `通学前に食べやすい子ども向け朝食レシピを調べて、材料と手順を含めてください。`
  - `登校前の子ども向けに、簡単な朝食アイデアを材料と作り方つきで探してください。`
  - `小学生向けの手軽な朝食を提案して、材料と流れを教えてください。`
  - `学校へ行く前の子ども向け朝食レシピを検索し、材料と手順を要約してください。`
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
  - `what is photosynthesis?`
  - `please explain what photosynthesis is.`
  - `I'd like to know what photosynthesis means.`
  - `can you tell me what photosynthesis is?`
  - `please describe photosynthesis.`
  - `what exactly is photosynthesis?`
  - `help me understand photosynthesis.`
  - `please tell me the meaning of photosynthesis.`
  - `what is the basic idea of photosynthesis?`
  - `explain photosynthesis in simple terms.`

- Japanese Variants: 10
  - `光合成とは何か教えてください。`
  - `光合成が何か説明してください。`
  - `光合成の意味を知りたいです。`
  - `光合成とは何か教えてもらえますか。`
  - `光合成について説明してください。`
  - `光合成とは具体的に何ですか。`
  - `光合成が分かるように教えてください。`
  - `光合成の意味を教えてください。`
  - `光合成の基本的な考え方は何ですか。`
  - `光合成を分かりやすく説明してください。`
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
  - `Based on the local knowledge base, what is photosynthesis?`
  - `Based on the local knowledge base, please explain what photosynthesis is.`
  - `Based on the local knowledge base, I'd like to know what photosynthesis means.`
  - `Based on the local knowledge base, can you tell me what photosynthesis is?`
  - `Based on the local knowledge base, please describe photosynthesis.`
  - `Based on the local knowledge base, what exactly is photosynthesis?`
  - `Based on the local knowledge base, help me understand photosynthesis.`
  - `Based on the local knowledge base, please tell me the meaning of photosynthesis.`
  - `Based on the local knowledge base, what is the basic idea of photosynthesis?`
  - `Based on the local knowledge base, explain photosynthesis in simple terms.`

- Japanese Variants: 10
  - `ローカル知識ベースに基づいて、光合成とは何か教えてください。`
  - `ローカル知識ベースに基づいて、光合成が何か説明してください。`
  - `ローカル知識ベースに基づいて、光合成の意味を知りたいです。`
  - `ローカル知識ベースに基づいて、光合成とは何か教えてもらえますか。`
  - `ローカル知識ベースに基づいて、光合成について説明してください。`
  - `ローカル知識ベースに基づいて、光合成とは具体的に何ですか。`
  - `ローカル知識ベースに基づいて、光合成が分かるように教えてください。`
  - `ローカル知識ベースに基づいて、光合成の意味を教えてください。`
  - `ローカル知識ベースに基づいて、光合成の基本的な考え方は何ですか。`
  - `ローカル知識ベースに基づいて、光合成を分かりやすく説明してください。`
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
  - `What are today's top news stories in Japan? Please give me two summaries.`
  - `Please show me two summaries of today's major news in Japan.`
  - `I'd like to know the hot topics in Japan today. Please summarize two stories.`
  - `Can you check today's trending news in Japan and give me two brief summaries?`
  - `Please tell me two highlights from today's news in Japan.`
  - `Show me two short summaries of Japan's top news today.`
  - `Please look up today's major Japanese news and summarize two items.`
  - `I want two brief summaries of today's hot news in Japan.`
  - `Can you find two important Japan news stories from today and summarize them?`
  - `Please provide two concise summaries of today's headlines in Japan.`

- Japanese Variants: 10
  - `今日の日本の注目ニュースを 2 件、要約つきで教えてください。`
  - `今日の日本の主要ニュースを 2 件、簡単にまとめてください。`
  - `今日の日本の話題のニュースを知りたいので、2 件要約してください。`
  - `今日の日本のトレンドニュースを確認して、短い要約を 2 件ください。`
  - `今日の日本のニュースから 2 つの注目ポイントを教えてください。`
  - `今日の日本のトップニュースを 2 件、短くまとめてください。`
  - `今日の日本の主要ニュースを調べて、2 件要約してください。`
  - `今日の日本のホットニュースを 2 件、簡潔に知りたいです。`
  - `今日の日本で重要なニュースを 2 件探して要約してください。`
  - `今日の日本の見出しニュースを 2 件、簡潔にまとめてください。`
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
  - `What is NVIDIA's stock price today and how it changed today?`
  - `Please tell me NVIDIA's stock price today and how it changed today.`
  - `I'd like to know NVIDIA's share price today and how it changed today.`
  - `Can you check NVIDIA's stock price for today and how it changed today?`
  - `Please look up today's stock price for NVIDIA and how it changed today.`
  - `Tell me the current price of NVIDIA stock today and how it changed today.`
  - `What is today's market price for NVIDIA and how it changed today?`
  - `Please check how NVIDIA stock is doing today and how it changed today.`
  - `I want today's price for NVIDIA stock and how it changed today.`
  - `Can you find NVIDIA's stock price today and how it changed today?`

- Japanese Variants: 10
  - `エヌビディア の今日の株価 と今日の値動きを教えてください。`
  - `エヌビディア の今日の株価 と今日の値動きを確認してください。`
  - `エヌビディア の今日の株価 と今日の値動きを知りたいです。`
  - `エヌビディア の本日の株価 と今日の値動きを調べてもらえますか。`
  - `エヌビディア の今日の株価情報 と今日の値動きを教えてください。`
  - `エヌビディア 株の現在価格 と今日の値動きを教えてください。`
  - `エヌビディア の本日の市場価格 と今日の値動きはどうですか。`
  - `エヌビディア の株が今日どう動いているか と今日の値動き確認してください。`
  - `エヌビディア 株の今日の価格 と今日の値動きが知りたいです。`
  - `エヌビディア の今日の株価 と今日の値動きを探してください。`
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
  - `Please tell me Apple's stock price today.`
  - `I'd like to know Apple's share price today.`
  - `Can you check Apple's stock price for today?`
  - `Please look up today's stock price for Apple.`
  - `Tell me the current price of Apple stock today.`
  - `What is today's market price for Apple?`
  - `Please check how Apple stock is doing today.`
  - `I want today's price for Apple stock.`
  - `Can you find Apple's stock price today?`

- Japanese Variants: 10
  - `Apple の今日の株価を教えてください。`
  - `Apple の今日の株価を確認してください。`
  - `Apple の今日の株価を知りたいです。`
  - `Apple の本日の株価を調べてもらえますか。`
  - `Apple の今日の株価情報を教えてください。`
  - `Apple 株の現在価格を教えてください。`
  - `Apple の本日の市場価格はどうですか。`
  - `Apple の株が今日どう動いているか確認してください。`
  - `Apple 株の今日の価格が知りたいです。`
  - `Apple の今日の株価を探してください。`
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
  - `please explain why fractions need a common denominator in a way a child can understand.`
  - `why do we need to make denominators the same when adding or comparing fractions in a way a child can understand?`
  - `I'd like to know why fractions need a common denominator in a way a child can understand.`
  - `can you explain the reason for finding a common denominator in fractions in a way a child can understand?`
  - `please tell me why common denominators are needed for fractions in a way a child can understand.`
  - `what is the purpose of making denominators the same in fractions in a way a child can understand?`
  - `help me understand why fractions need a common denominator in a way a child can understand.`
  - `please explain common denominators for fractions in a way a child can understand.`
  - `why is a common denominator necessary in fraction problems in a way a child can understand?`
  - `explain why we use common denominators with fractions in a way a child can understand.`

- Japanese Variants: 10
  - `分数で通分が必要な理由を子どもにも分かるように。`
  - `分数を足したり比べたりするとき、なぜ分母をそろえる必要があるのか子どもにも分かるように。`
  - `分数で通分が必要な理由を知りたいです。`
  - `分数で通分する理由を子どもにも分かるように。`
  - `分数に通分が必要なわけを子どもにも分かるように。`
  - `分数で分母をそろえる目的は何ですか。`
  - `分数で通分が必要な理由が分かるように子どもにも分かるように。`
  - `分数の通分について子どもにも分かるように。`
  - `分数の問題で通分が必要なのはなぜですか。`
  - `分数で通分を使う理由を子どもにも分かるように。`
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
  - `Based on the local knowledge base, please explain why fractions need a common denominator.`
  - `Based on the local knowledge base, why do we need to make denominators the same when adding or comparing fractions?`
  - `Based on the local knowledge base, I'd like to know why fractions need a common denominator.`
  - `Based on the local knowledge base, can you explain the reason for finding a common denominator in fractions?`
  - `Based on the local knowledge base, please tell me why common denominators are needed for fractions.`
  - `Based on the local knowledge base, what is the purpose of making denominators the same in fractions?`
  - `Based on the local knowledge base, help me understand why fractions need a common denominator.`
  - `Based on the local knowledge base, please explain common denominators for fractions.`
  - `Based on the local knowledge base, why is a common denominator necessary in fraction problems?`
  - `Based on the local knowledge base, explain why we use common denominators with fractions.`

- Japanese Variants: 10
  - `ローカル知識ベースに基づいて、分数で通分が必要な理由を説明してください。`
  - `ローカル知識ベースに基づいて、分数を足したり比べたりするとき、なぜ分母をそろえる必要があるのか教えてください。`
  - `ローカル知識ベースに基づいて、分数で通分が必要な理由を知りたいです。`
  - `ローカル知識ベースに基づいて、分数で通分する理由を説明してもらえますか。`
  - `ローカル知識ベースに基づいて、分数に通分が必要なわけを教えてください。`
  - `ローカル知識ベースに基づいて、分数で分母をそろえる目的は何ですか。`
  - `ローカル知識ベースに基づいて、分数で通分が必要な理由が分かるように教えてください。`
  - `ローカル知識ベースに基づいて、分数の通分について説明してください。`
  - `ローカル知識ベースに基づいて、分数の問題で通分が必要なのはなぜですか。`
  - `ローカル知識ベースに基づいて、分数で通分を使う理由を説明してください。`
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
  - `Please check the train times and fares from Tokyo to Osaka for tomorrow.`
  - `Look up the schedule and ticket costs from Tokyo to Osaka for tomorrow.`
  - `I'd like to know the train times and prices from Tokyo to Osaka for tomorrow.`
  - `Can you find the train timetable and fares from Tokyo to Osaka for tomorrow?`
  - `Please show me the departure times and prices from Tokyo to Osaka for tomorrow.`
  - `Check the train options, times, and costs from Tokyo to Osaka for tomorrow.`
  - `Tell me the likely train schedule and fare from Tokyo to Osaka for tomorrow.`
  - `Please search for train tickets and times from Tokyo to Osaka for tomorrow.`
  - `I want to see the available train times and ticket prices from Tokyo to Osaka for tomorrow.`
  - `Find trustworthy sources for train times and fares from Tokyo to Osaka for tomorrow.`

- Japanese Variants: 10
  - `東京から大阪 の 明日 の列車について、時間と料金を調べてください。`
  - `東京から大阪 の 明日 の時刻表とチケット代を調べてください。`
  - `東京から大阪 の 明日 の列車時間と料金を知りたいです。`
  - `東京から大阪 の 明日 の列車の時刻と運賃を探してください。`
  - `東京から大阪 の 明日 の出発時刻と価格を見せてください。`
  - `東京から大阪 の 明日 の列車候補、時間、費用を確認してください。`
  - `東京から大阪 の 明日 の大まかな時刻と運賃を教えてください。`
  - `東京から大阪 の 明日 の列車チケットと時刻を検索してください。`
  - `東京から大阪 の 明日 の利用可能な列車時間とチケット価格を見たいです。`
  - `東京から大阪 の 明日 の時間と料金について、信頼できる情報源を探してください。`
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
  - `Please check the flight times and ticket prices from Tokyo to San Francisco for the end of the month.`
  - `Look up the approximate flight schedule and fares from Tokyo to San Francisco for the end of the month.`
  - `I'd like to know the flight times and prices from Tokyo to San Francisco for the end of the month.`
  - `Can you find reliable flight times and ticket prices from Tokyo to San Francisco for the end of the month?`
  - `Please show me the departure times and fares from Tokyo to San Francisco for the end of the month.`
  - `Check the flight options, times, and prices from Tokyo to San Francisco for the end of the month.`
  - `Tell me the likely flight schedule and cost from Tokyo to San Francisco for the end of the month.`
  - `Please search for airfare and flight times from Tokyo to San Francisco for the end of the month.`
  - `I want to see the available flight times and ticket prices from Tokyo to San Francisco for the end of the month.`
  - `Find trustworthy sources for flight times and prices from Tokyo to San Francisco for the end of the month.`

- Japanese Variants: 10
  - `東京からサンフランシスコ の 今月末 の便について、フライト時間と航空券の料金を調べてください。`
  - `東京からサンフランシスコ の 今月末 のおおよその便スケジュールと運賃を調べてください。`
  - `東京からサンフランシスコ の 今月末 のフライト時間と料金を知りたいです。`
  - `東京からサンフランシスコ の 今月末 の便について、信頼できる時間と料金情報を探してください。`
  - `東京からサンフランシスコ の 今月末 の出発時刻と料金を見せてください。`
  - `東京からサンフランシスコ の 今月末 の便の候補、時間、価格を確認してください。`
  - `東京からサンフランシスコ の 今月末 の大まかなフライト予定と費用を教えてください。`
  - `東京からサンフランシスコ の 今月末 の航空券価格と便の時間を検索してください。`
  - `東京からサンフランシスコ の 今月末 の利用可能な便の時間と料金を見たいです。`
  - `東京からサンフランシスコ の 今月末 の時間と価格について、信頼できる情報源を探してください。`
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
  - `Please explain to a child why we can see rainbows during the day.`
  - `Tell a child in simple words why rainbows can be seen in the daytime.`
  - `I want an easy explanation for a child about why rainbows appear during the day.`
  - `Can you explain in a child-friendly way why we see rainbows in daylight?`
  - `Please give a simple explanation for kids about why rainbows show up during the day.`
  - `Help me explain to a child why rainbows can be seen in the daytime.`
  - `Could you describe why rainbows appear in daytime in words a child can understand?`
  - `Please explain the daytime rainbow in an easy way for children.`
  - `I need a kid-friendly explanation of why rainbows are visible during the day.`
  - `Explain to a child, in simple terms, why rainbows can be seen in the daytime.`

- Japanese Variants: 10
  - `昼間に虹が見える理由を、子どもにも分かる言葉で説明してください。`
  - `どうして昼間に虹が見えるのか、子ども向けにやさしく教えてください。`
  - `昼間に虹が現れる理由を、子どもにも分かりやすく説明してほしいです。`
  - `なぜ明るい昼間に虹が見えるのか、子ども向けに説明してもらえますか。`
  - `昼間に虹が出る理由を、子どもが理解できるように説明してください。`
  - `子どもに、どうして昼間に虹が見えるのか説明するのを手伝ってください。`
  - `昼の虹が見える仕組みを、子ども向けに分かりやすく教えてください。`
  - `昼間の虹について、子どもにもやさしい説明をしてください。`
  - `昼間に虹が見えるのはなぜか、子ども向けに簡単に説明してください。`
  - `昼間に虹が見える理由を、簡単な言葉で子どもに説明してください。`