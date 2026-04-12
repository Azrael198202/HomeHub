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
  - `おれさま、こんにちは`
  - `こんにちは、？`
  - `やあ HomeHub`
  - `こんにちは、おいします`
  - `ちょっとです、こんにちは`
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
  - `HomeHub、？`
  - `やあ、HomeHub`
  - `HomeHub にです`
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
  - `のです、おはよう`
  - `もおはよう`
  - `やあ、おはよう`
  - `おはようございます、HomeHub`
  - `ですね、おはよう`
  - `もおはよう`
  - `おはよう、？`

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
  - `は`
  - `やあ、こんばんは`
  - `こんばんは、HomeHub さん`
  - `もこんばんは`
  - `のです、こんばんは`
  - `こんばんは、？`
  - `おれさま、こんばんは`
  - `こんばんは、よろしくおいします`

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
  - `Tell me the weather in Fukuoka today.`
  - `How's the weather in Fukuoka today?`
  - `Please give me today's forecast in Fukuoka.`
  - `What's the high temperature in Fukuoka today?`
  - `Tell me today's high temperature in Fukuoka.`
  - `How warm will it get in Fukuoka today?`
  - `Please check today's forecast and high temperature for Fukuoka.`
  - `I'd like today's weather and the high temperature in Fukuoka.`

- Japanese Variants: 10
  - `ののをえて`
  - `はどんなかりたい`
  - `ののをて`
  - `のをして`
  - `ははどんな？`
  - `ののは？`
  - `のとをえて`
  - `はまでがる？`
  - `ののいをりたい`
  - `ののとをして`

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
  - `Tell me the weather in Tokyo today.`
  - `How's the weather in Tokyo today?`
  - `Please give me today's forecast in Tokyo.`
  - `What's today's temperature in Tokyo?`
  - `Tell me the temperature in Tokyo today.`
  - `How many degrees is it in Tokyo today?`
  - `Can you check today's temperature for Tokyo?`
  - `I'd like to know the current temperature in Tokyo today.`

- Japanese Variants: 10
  - `ののをえて`
  - `はどんなかりたい`
  - `ののをて`
  - `のをして`
  - `ははどんな？`
  - `ののは？`
  - `ののをえて`
  - `ははくらい？`
  - `ののをして`
  - `ののがりたい`

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
  - `What is the weather like in Osaka today?`
  - `Can you check today's weather in Osaka?`
  - `Tell me the weather in Osaka today.`
  - `How's the weather in Osaka today?`
  - `Please give me today's forecast in Osaka.`
  - `Will it rain in Osaka today?`
  - `Can you check whether it's going to rain in Osaka today?`
  - `Is rain expected in Osaka today?`
  - `Tell me if I should expect rain in Osaka today.`
  - `Please check today's rain chances in Osaka.`

- Japanese Variants: 10
  - `ののをえて`
  - `はどんなかりたい`
  - `ののをて`
  - `のをして`
  - `ははどんな？`
  - `はがる？`
  - `ののをえて`
  - `ではのがある？`
  - `ののをして`
  - `ははになるかて`

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
  - `Tell me the weather today.`
  - `How's the weather today?`
  - `Please give me today's forecast.`
  - `What's the high temperature in the area today?`
  - `Tell me today's high temperature.`
  - `How warm will it get today?`
  - `Please check today's forecast and high temperature for today.`
  - `I'd like today's weather and the high temperature.`

- Japanese Variants: 10
  - `のをえて`
  - `はどんなかりたい`
  - `のをて`
  - `をして`
  - `はどんな？`
  - `のは？`
  - `のとをえて`
  - `はまでがる？`
  - `のいをりたい`
  - `のとをして`

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
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをせて`
  - `/tmp/homehub-family-suite/family-inbox のファイルをにして`
  - `/tmp/homehub-family-suite/family-inbox のにのファイルがあるかえて`
  - `/tmp/homehub-family-suite/family-inbox のファイルをしたい`
  - `/tmp/homehub-family-suite/family-inbox のをせてください`
  - `/tmp/homehub-family-suite/family-inbox にっているファイルをして`
  - `/tmp/homehub-family-suite/family-inbox をいてをして`
  - `/tmp/homehub-family-suite/family-inbox のファイルをえて`
  - `/tmp/homehub-family-suite/family-inbox にがあるかチェックして`
  - `/tmp/homehub-family-suite/family-inbox のファイルをせて`

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
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをせて、そのあと family_trip.pptx をって`
  - `/tmp/homehub-family-suite/family-inbox のファイルをして、family_trip.pptx をってください`
  - `/tmp/homehub-family-suite/family-inbox にがあるかして、family_trip.pptx をして`
  - `/tmp/homehub-family-suite/family-inbox のをせてから family_trip.pptx をって`
  - `/tmp/homehub-family-suite/family-inbox をして、family_trip.pptx をにして`
  - `/tmp/homehub-family-suite/family-inbox のファイルをして、family_trip.pptx をして`
  - `/tmp/homehub-family-suite/family-inbox にあるものをえて、family_trip.pptx もって`
  - `/tmp/homehub-family-suite/family-inbox をいてファイルをし、family_trip.pptx をってください`
  - `/tmp/homehub-family-suite/family-inbox のをて、family_trip.pptx をしてください`
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをしたうえで family_trip.pptx をって`

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
  - `/tmp/homehub-family-suite/family-inbox で budget にするファイルをして`
  - `/tmp/homehub-family-suite/family-inbox の budget ファイルをして`
  - `/tmp/homehub-family-suite/family-inbox のから budget にするファイルをつけて`
  - `/tmp/homehub-family-suite/family-inbox で budget をむファイルをして`
  - `/tmp/homehub-family-suite/family-inbox の budget ファイルをたい`
  - `/tmp/homehub-family-suite/family-inbox をして budget ファイルをつけて`
  - `/tmp/homehub-family-suite/family-inbox にある budget ファイルをして`
  - `/tmp/homehub-family-suite/family-inbox ので budget にいファイルをして`
  - `/tmp/homehub-family-suite/family-inbox から budget ファイルをつけてください`
  - `/tmp/homehub-family-suite/family-inbox の budget にするファイルをして`

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
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をんで`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をいてをせて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のをして`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をみってください`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のをして`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をいてんでほしい`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のファイルをえて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をしてをせて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をんでをして`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のをしてください`

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
  - `/tmp/homehub-family-suite/family-reading/recipe.json をんで`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をいてをせて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のをして`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をみってください`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のをして`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をいてんでほしい`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のファイルをえて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をしてをせて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をんでをして`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のをしてください`

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
  - `/tmp/homehub-family-suite/family-library にあるファイルをせて`
  - `/tmp/homehub-family-suite/family-library のファイルをにして`
  - `/tmp/homehub-family-suite/family-library のにのファイルがあるかえて`
  - `/tmp/homehub-family-suite/family-library のファイルをしたい`
  - `/tmp/homehub-family-suite/family-library のをせてください`
  - `/tmp/homehub-family-suite/family-library にっているファイルをして`
  - `/tmp/homehub-family-suite/family-library をいてをして`
  - `/tmp/homehub-family-suite/family-library のファイルをえて`
  - `/tmp/homehub-family-suite/family-library にがあるかチェックして`
  - `/tmp/homehub-family-suite/family-library のファイルをせて`

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
  - `/Users/home/Documents にあるファイルをせて、そのあと AI_Agent_Build2026 en.pptx をって`
  - `/Users/home/Documents のファイルをして、AI_Agent_Build2026 en.pptx をってください`
  - `/Users/home/Documents にがあるかして、AI_Agent_Build2026 en.pptx をして`
  - `/Users/home/Documents のをせてから AI_Agent_Build2026 en.pptx をって`
  - `/Users/home/Documents をして、AI_Agent_Build2026 en.pptx をにして`
  - `/Users/home/Documents のファイルをして、AI_Agent_Build2026 en.pptx をして`
  - `/Users/home/Documents にあるものをえて、AI_Agent_Build2026 en.pptx もって`
  - `/Users/home/Documents をいてファイルをし、AI_Agent_Build2026 en.pptx をってください`
  - `/Users/home/Documents のをて、AI_Agent_Build2026 en.pptx をしてください`
  - `/Users/home/Documents にあるファイルをしたうえで AI_Agent_Build2026 en.pptx をって`

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
  - `/tmp/homehub-family-suite/family-library で photo にするファイルをして`
  - `/tmp/homehub-family-suite/family-library の photo ファイルをして`
  - `/tmp/homehub-family-suite/family-library のから photo にするファイルをつけて`
  - `/tmp/homehub-family-suite/family-library で photo をむファイルをして`
  - `/tmp/homehub-family-suite/family-library の photo ファイルをたい`
  - `/tmp/homehub-family-suite/family-library をして photo ファイルをつけて`
  - `/tmp/homehub-family-suite/family-library にある photo ファイルをして`
  - `/tmp/homehub-family-suite/family-library ので photo にいファイルをして`
  - `/tmp/homehub-family-suite/family-library から photo ファイルをつけてください`
  - `/tmp/homehub-family-suite/family-library の photo にするファイルをして`

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
  - ` /tmp/homehub-family-suite/classify-alpha ，。`
  - `このをおいします:  /tmp/homehub-family-suite/classify-alpha ，。`
  - `のでしてください:  /tmp/homehub-family-suite/classify-alpha ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/classify-alpha ，。`
  - `このをめてください:  /tmp/homehub-family-suite/classify-alpha ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/classify-alpha ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/classify-alpha ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/classify-alpha ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/classify-alpha ，。`
  - `このでおいします:  /tmp/homehub-family-suite/classify-alpha ，。`

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
  - ` /tmp/homehub-family-suite/classify-beta ，。`
  - `このをおいします:  /tmp/homehub-family-suite/classify-beta ，。`
  - `のでしてください:  /tmp/homehub-family-suite/classify-beta ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/classify-beta ，。`
  - `このをめてください:  /tmp/homehub-family-suite/classify-beta ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/classify-beta ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/classify-beta ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/classify-beta ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/classify-beta ，。`
  - `このでおいします:  /tmp/homehub-family-suite/classify-beta ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをせて、そのあと receipt.pdf をって`
  - `/tmp/homehub-family-suite/family-inbox のファイルをして、receipt.pdf をってください`
  - `/tmp/homehub-family-suite/family-inbox にがあるかして、receipt.pdf をして`
  - `/tmp/homehub-family-suite/family-inbox のをせてから receipt.pdf をって`
  - `/tmp/homehub-family-suite/family-inbox をして、receipt.pdf をにして`
  - `/tmp/homehub-family-suite/family-inbox のファイルをして、receipt.pdf をして`
  - `/tmp/homehub-family-suite/family-inbox にあるものをえて、receipt.pdf もって`
  - `/tmp/homehub-family-suite/family-inbox をいてファイルをし、receipt.pdf をってください`
  - `/tmp/homehub-family-suite/family-inbox のをて、receipt.pdf をしてください`
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをしたうえで receipt.pdf をって`

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
  - `7にとリマインドして`
  - `7にことをらせて`
  - `7に「」のリマインダーをして`
  - `7になったらとして`
  - `7のリマインダーとしてをして`
  - `7にのをれて`
  - `7にことをれないようらせて`
  - `7のでをリマインドして`
  - `7にへとえて`
  - `7にのをって`

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
  - `8にとリマインドして`
  - `8にことをらせて`
  - `8に「」のリマインダーをして`
  - `8になったらとして`
  - `8のリマインダーとしてをして`
  - `8にのをれて`
  - `8にことをれないようらせて`
  - `8のでをリマインドして`
  - `8にへとえて`
  - `8にのをって`

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
  - `9にとリマインドして`
  - `9にことをらせて`
  - `9に「」のリマインダーをして`
  - `9になったらとして`
  - `9のリマインダーとしてをして`
  - `9にのをれて`
  - `9にことをれないようらせて`
  - `9のでをリマインドして`
  - `9にへとえて`
  - `9にのをって`

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
  - `リマインダーをせて`
  - `のリマインダーをして`
  - `リマインダーのリストをしたい`
  - `みのリマインダーをえて`
  - `リマインダーをいて`
  - `いまっているリマインダーをたい`
  - `リマインダーをして`
  - `のをせて`
  - `リマインダーをして`
  - `のリマインダーをして`

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
  - `リマインダーをせて`
  - `のリマインダーをして`
  - `リマインダーのリストをしたい`
  - `みのリマインダーをえて`
  - `リマインダーをいて`
  - `いまっているリマインダーをたい`
  - `リマインダーをして`
  - `のをせて`
  - `リマインダーをして`
  - `のリマインダーをして`

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
  - `3にをにれて、30にらせて`
  - `3のをして、30にリマインドして`
  - `3にをし、30にして`
  - `3のとしてをして、30にえて`
  - `を3にれて、30にらせてください`
  - `3のをスケジュールして、30にして`
  - `3にをして、に30でらせて`
  - `3のをにれ、30にリマインドして`
  - `を3にして、30のをして`
  - `3にをし、30にえて`

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
  - `4にをにれて、30にらせて`
  - `4のをして、30にリマインドして`
  - `4にをし、30にして`
  - `4のとしてをして、30にえて`
  - `を4にれて、30にらせてください`
  - `4のをスケジュールして、30にして`
  - `4にをして、に30でらせて`
  - `4のをにれ、30にリマインドして`
  - `を4にして、30のをして`
  - `4にをし、30にえて`

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
  - `をせて`
  - `スケジュールをいて`
  - `をしたい`
  - `のをして`
  - `カレンダーをせて`
  - `をして`
  - `これからのをして`
  - `スケジュールをえて`
  - `をたい`
  - `されているをして`

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
  - `8にとリマインドして`
  - `8にことをらせて`
  - `8に「」のリマインダーをして`
  - `8になったらとして`
  - `8のリマインダーとしてをして`
  - `8にのをれて`
  - `8にことをれないようらせて`
  - `8のでをリマインドして`
  - `8にへとえて`
  - `8にのをって`

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
  - `9にとリマインドして`
  - `9にことをらせて`
  - `9に「」のリマインダーをして`
  - `9になったらとして`
  - `9のリマインダーとしてをして`
  - `9にのをれて`
  - `9にことをれないようらせて`
  - `9のでをリマインドして`
  - `9にへとえて`
  - `9にのをって`

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
  - `5にをにれて、30にらせて`
  - `5のをして、30にリマインドして`
  - `5にをし、30にして`
  - `5のとしてをして、30にえて`
  - `を5にれて、30にらせてください`
  - `5のをスケジュールして、30にして`
  - `5にをして、に30でらせて`
  - `5のをにれ、30にリマインドして`
  - `を5にして、30のをして`
  - `5にをし、30にえて`

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
  - `をせて`
  - `スケジュールをいて`
  - `をしたい`
  - `のをして`
  - `カレンダーをせて`
  - `をして`
  - `これからのをして`
  - `スケジュールをえて`
  - `をたい`
  - `されているをして`

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
  - ` というのエージェントをって`
  - ` というエージェントをして`
  - ` でエージェントをして`
  - ` というカスタムエージェントをって`
  - ` のエージェントをりたい`
  - ` をにしてエージェントをって`
  - ` というしいエージェントをして`
  - ` というでしてください`
  - ` のエージェントをちげて`
  - ` をとするエージェントをして`

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
  - `，，OCR`
  - `このをたせてください: ，，OCR`
  - `のにできるようにして: ，，OCR`
  - `このエージェントにはのがです: ，，OCR`
  - `のをサポートしてほしいです: ，，OCR`
  - `このでえるようにしてください: ，，OCR`
  - `のにするエージェントにして: ，，OCR`
  - `このをめてください: ，，OCR`
  - `しているはこれです: ，，OCR`
  - `このをたすようにしてください: ，，OCR`

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
  - `をして`
  - `このでして`
  - `はい、をめて`
  - `そのままして`
  - `ないのでして`
  - `をしてください`
  - `このでさせて`
  - `そのでって`
  - `ではをけて`
  - `してして`

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
  - ` というのエージェントをって`
  - ` というエージェントをして`
  - ` でエージェントをして`
  - ` というカスタムエージェントをって`
  - ` のエージェントをりたい`
  - ` をにしてエージェントをって`
  - ` というしいエージェントをして`
  - ` というでしてください`
  - ` のエージェントをちげて`
  - ` をとするエージェントをして`

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
  - `、にとリマインドして`
  - `、にことをらせて`
  - `、に「」のリマインダーをして`
  - `、になったらとして`
  - `、のリマインダーとしてをして`
  - `、にのをれて`
  - `、にことをれないようらせて`
  - `、のでをリマインドして`
  - `、にへとえて`
  - `、にのをって`

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
  - `をして`
  - `このでして`
  - `はい、をめて`
  - `そのままして`
  - `ないのでして`
  - `をしてください`
  - `このでさせて`
  - `そのでって`
  - `ではをけて`
  - `してして`

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
  - ` というのエージェントをって`
  - ` というエージェントをして`
  - ` でエージェントをして`
  - ` というカスタムエージェントをって`
  - ` のエージェントをりたい`
  - ` をにしてエージェントをって`
  - ` というしいエージェントをして`
  - ` というでしてください`
  - ` のエージェントをちげて`
  - ` をとするエージェントをして`

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
  - `、`
  - `このをたせてください: 、`
  - `のにできるようにして: 、`
  - `このエージェントにはのがです: 、`
  - `のをサポートしてほしいです: 、`
  - `このでえるようにしてください: 、`
  - `のにするエージェントにして: 、`
  - `このをめてください: 、`
  - `しているはこれです: 、`
  - `このをたすようにしてください: 、`

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
  - `をして`
  - `このでして`
  - `はい、をめて`
  - `そのままして`
  - `ないのでして`
  - `をしてください`
  - `このでさせて`
  - `そのでって`
  - `ではをけて`
  - `してして`

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
  - ` というのエージェントをって`
  - ` というエージェントをして`
  - ` でエージェントをして`
  - ` というカスタムエージェントをって`
  - ` のエージェントをりたい`
  - ` をにしてエージェントをって`
  - ` というしいエージェントをして`
  - ` というでしてください`
  - ` のエージェントをちげて`
  - ` をとするエージェントをして`

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
  - `、`
  - `このをたせてください: 、`
  - `のにできるようにして: 、`
  - `このエージェントにはのがです: 、`
  - `のをサポートしてほしいです: 、`
  - `このでえるようにしてください: 、`
  - `のにするエージェントにして: 、`
  - `このをめてください: 、`
  - `しているはこれです: 、`
  - `このをたすようにしてください: 、`

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
  - `をして`
  - `このでして`
  - `はい、をめて`
  - `そのままして`
  - `ないのでして`
  - `をしてください`
  - `このでさせて`
  - `そのでって`
  - `ではをけて`
  - `してして`

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
  - ` というのエージェントをって`
  - ` というエージェントをして`
  - ` でエージェントをして`
  - ` というカスタムエージェントをって`
  - ` のエージェントをりたい`
  - ` をにしてエージェントをって`
  - ` というしいエージェントをして`
  - ` というでしてください`
  - ` のエージェントをちげて`
  - ` をとするエージェントをして`

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
  - `にとリマインドして`
  - `にことをらせて`
  - `に「」のリマインダーをして`
  - `になったらとして`
  - `のリマインダーとしてをして`
  - `にのをれて`
  - `にことをれないようらせて`
  - `のでをリマインドして`
  - `にへとえて`
  - `にのをって`

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
  - `をして`
  - `このでして`
  - `はい、をめて`
  - `そのままして`
  - `ないのでして`
  - `をしてください`
  - `このでさせて`
  - `そのでって`
  - `ではをけて`
  - `してして`

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
  - ` というのエージェントをって`
  - ` というエージェントをして`
  - ` でエージェントをして`
  - ` というカスタムエージェントをって`
  - ` のエージェントをりたい`
  - ` をにしてエージェントをって`
  - ` というしいエージェントをして`
  - ` というでしてください`
  - ` のエージェントをちげて`
  - ` をとするエージェントをして`

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
  - `、`
  - `このをたせてください: 、`
  - `のにできるようにして: 、`
  - `このエージェントにはのがです: 、`
  - `のをサポートしてほしいです: 、`
  - `このでえるようにしてください: 、`
  - `のにするエージェントにして: 、`
  - `このをめてください: 、`
  - `しているはこれです: 、`
  - `このをたすようにしてください: 、`

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
  - `をして`
  - `このでして`
  - `はい、をめて`
  - `そのままして`
  - `ないのでして`
  - `をしてください`
  - `このでさせて`
  - `そのでって`
  - `ではをけて`
  - `してして`

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
  - ` というのエージェントをって`
  - ` というエージェントをして`
  - ` でエージェントをして`
  - ` というカスタムエージェントをって`
  - ` のエージェントをりたい`
  - ` をにしてエージェントをって`
  - ` というしいエージェントをして`
  - ` というでしてください`
  - ` のエージェントをちげて`
  - ` をとするエージェントをして`

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
  - `、`
  - `このをたせてください: 、`
  - `のにできるようにして: 、`
  - `このエージェントにはのがです: 、`
  - `のをサポートしてほしいです: 、`
  - `このでえるようにしてください: 、`
  - `のにするエージェントにして: 、`
  - `このをめてください: 、`
  - `しているはこれです: 、`
  - `このをたすようにしてください: 、`

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
  - `をして`
  - `このでして`
  - `はい、をめて`
  - `そのままして`
  - `ないのでして`
  - `をしてください`
  - `このでさせて`
  - `そのでって`
  - `ではをけて`
  - `してして`

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
  - ` というのエージェントをって`
  - ` というエージェントをして`
  - ` でエージェントをして`
  - ` というカスタムエージェントをって`
  - ` のエージェントをりたい`
  - ` をにしてエージェントをって`
  - ` というしいエージェントをして`
  - ` というでしてください`
  - ` のエージェントをちげて`
  - ` をとするエージェントをして`

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
  - `、、`
  - `このをたせてください: 、、`
  - `のにできるようにして: 、、`
  - `このエージェントにはのがです: 、、`
  - `のをサポートしてほしいです: 、、`
  - `このでえるようにしてください: 、、`
  - `のにするエージェントにして: 、、`
  - `このをめてください: 、、`
  - `しているはこれです: 、、`
  - `このをたすようにしてください: 、、`

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
  - `をして`
  - `このでして`
  - `はい、をめて`
  - `そのままして`
  - `ないのでして`
  - `をしてください`
  - `このでさせて`
  - `そのでって`
  - `ではをけて`
  - `してして`

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
  - ` というのエージェントをって`
  - ` というエージェントをして`
  - ` でエージェントをして`
  - ` というカスタムエージェントをって`
  - ` のエージェントをりたい`
  - ` をにしてエージェントをって`
  - ` というしいエージェントをして`
  - ` というでしてください`
  - ` のエージェントをちげて`
  - ` をとするエージェントをして`

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
  - `、，excel`
  - `このをたせてください: 、，excel`
  - `のにできるようにして: 、，excel`
  - `このエージェントにはのがです: 、，excel`
  - `のをサポートしてほしいです: 、，excel`
  - `このでえるようにしてください: 、，excel`
  - `のにするエージェントにして: 、，excel`
  - `このをめてください: 、，excel`
  - `しているはこれです: 、，excel`
  - `このをたすようにしてください: 、，excel`

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
  - `をして`
  - `このでして`
  - `はい、をめて`
  - `そのままして`
  - `ないのでして`
  - `をしてください`
  - `このでさせて`
  - `そのでって`
  - `ではをけて`
  - `してして`

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
  - `の0730にで480ったをして`
  - `0730の 480をとしてして`
  - `0730の480をして`
  - `0730にった 480をにして`
  - `0730のとして 480をして`
  - `に480ったので、0730のにれて`
  - `の0730、で480ったことをして`
  - `0730の 480をして`
  - `0730の480をして`
  - `に0730の 480をれて`

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
  - `の0820にで220ったをして`
  - `0820の 220をとしてして`
  - `0820の220をして`
  - `0820にった 220をにして`
  - `0820のとして 220をして`
  - `に220ったので、0820のにれて`
  - `の0820、で220ったことをして`
  - `0820の 220をして`
  - `0820の220をして`
  - `に0820の 220をれて`

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
  - `の1020にで2000ったをして`
  - `1020の 2000をとしてして`
  - `1020の2000をして`
  - `1020にった 2000をにして`
  - `1020のとして 2000をして`
  - `に2000ったので、1020のにれて`
  - `の1020、で2000ったことをして`
  - `1020の 2000をして`
  - `1020の2000をして`
  - `に1020の 2000をれて`

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
  - `の1200にで800ったをして`
  - `1200の 800をとしてして`
  - `1200の800をして`
  - `1200にった 800をにして`
  - `1200のとして 800をして`
  - `に800ったので、1200のにれて`
  - `の1200、で800ったことをして`
  - `1200の 800をして`
  - `1200の800をして`
  - `に1200の 800をれて`

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
  - `の1410にで650ったをして`
  - `1410の 650をとしてして`
  - `1410の650をして`
  - `1410にった 650をにして`
  - `1410のとして 650をして`
  - `に650ったので、1410のにれて`
  - `の1410、で650ったことをして`
  - `1410の 650をして`
  - `1410の650をして`
  - `に1410の 650をれて`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - `，3000に， homehubとリマインドして`
  - `，3000に， homehubことをらせて`
  - `，3000に「， homehub」のリマインダーをして`
  - `，3000になったら， homehubとして`
  - `，3000のリマインダーとして， homehubをして`
  - `，3000に， homehubのをれて`
  - `，3000に， homehubことをれないようらせて`
  - `，3000ので， homehubをリマインドして`
  - `，3000にへ， homehubとえて`
  - `，3000に， homehubのをって`

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
  - `までのをして、を Excel にまとめて`
  - `ここまでのをして、Excel をって`
  - `のをし、Excel ファイルもして`
  - `をして、を Excel にしてほしい`
  - `とそのを Excel でして`
  - `までのをして、Excel でまとめて`
  - `のをえて、そのを Excel にして`
  - `までのをし、Excel ファイルをして`
  - `ここまでのを Excel としてして`
  - `のと、Excel へのきしをおい`

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
  - `の1530にで320ったをして`
  - `1530の 320をとしてして`
  - `1530の320をして`
  - `1530にった 320をにして`
  - `1530のとして 320をして`
  - `に320ったので、1530のにれて`
  - `の1530、で320ったことをして`
  - `1530の 320をして`
  - `1530の320をして`
  - `に1530の 320をれて`

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
  - `の1700にで5800ったをして`
  - `1700の 5800をとしてして`
  - `1700の5800をして`
  - `1700にった 5800をにして`
  - `1700のとして 5800をして`
  - `に5800ったので、1700のにれて`
  - `の1700、で5800ったことをして`
  - `1700の 5800をして`
  - `1700の5800をして`
  - `に1700の 5800をれて`

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
  - `の1815にで260ったをして`
  - `1815の 260をとしてして`
  - `1815の260をして`
  - `1815にった 260をにして`
  - `1815のとして 260をして`
  - `に260ったので、1815のにれて`
  - `の1815、で260ったことをして`
  - `1815の 260をして`
  - `1815の260をして`
  - `に1815の 260をれて`

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
  - `の1940にで1500ったをして`
  - `1940の 1500をとしてして`
  - `1940の1500をして`
  - `1940にった 1500をにして`
  - `1940のとして 1500をして`
  - `に1500ったので、1940のにれて`
  - `の1940、で1500ったことをして`
  - `1940の 1500をして`
  - `1940の1500をして`
  - `に1940の 1500をれて`

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
  - `の2010にで700ったをして`
  - `2010の 700をとしてして`
  - `2010の700をして`
  - `2010にった 700をにして`
  - `2010のとして 700をして`
  - `に700ったので、2010のにれて`
  - `の2010、で700ったことをして`
  - `2010の 700をして`
  - `2010の700をして`
  - `に2010の 700をれて`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - `，10000に， homehubとリマインドして`
  - `，10000に， homehubことをらせて`
  - `，10000に「， homehub」のリマインダーをして`
  - `，10000になったら， homehubとして`
  - `，10000のリマインダーとして， homehubをして`
  - `，10000に， homehubのをれて`
  - `，10000に， homehubことをれないようらせて`
  - `，10000ので， homehubをリマインドして`
  - `，10000にへ， homehubとえて`
  - `，10000に， homehubのをって`

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
  - `までのをして、を Excel にまとめて`
  - `ここまでのをして、Excel をって`
  - `のをし、Excel ファイルもして`
  - `をして、を Excel にしてほしい`
  - `とそのを Excel でして`
  - `までのをして、Excel でまとめて`
  - `のをえて、そのを Excel にして`
  - `までのをし、Excel ファイルをして`
  - `ここまでのを Excel としてして`
  - `のと、Excel へのきしをおい`

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
  - `の2100にで980ったをして`
  - `2100の 980をとしてして`
  - `2100の980をして`
  - `2100にった 980をにして`
  - `2100のとして 980をして`
  - `に980ったので、2100のにれて`
  - `の2100、で980ったことをして`
  - `2100の 980をして`
  - `2100の980をして`
  - `に2100の 980をれて`

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
  - `の2120にで2300ったをして`
  - `2120の 2300をとしてして`
  - `2120の2300をして`
  - `2120にった 2300をにして`
  - `2120のとして 2300をして`
  - `に2300ったので、2120のにれて`
  - `の2120、で2300ったことをして`
  - `2120の 2300をして`
  - `2120の2300をして`
  - `に2120の 2300をれて`

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
  - `の2140にで4300ったをして`
  - `2140の 4300をとしてして`
  - `2140の4300をして`
  - `2140にった 4300をにして`
  - `2140のとして 4300をして`
  - `に4300ったので、2140のにれて`
  - `の2140、で4300ったことをして`
  - `2140の 4300をして`
  - `2140の4300をして`
  - `に2140の 4300をれて`

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
  - `の2200にで3200ったをして`
  - `2200の 3200をとしてして`
  - `2200の3200をして`
  - `2200にった 3200をにして`
  - `2200のとして 3200をして`
  - `に3200ったので、2200のにれて`
  - `の2200、で3200ったことをして`
  - `2200の 3200をして`
  - `2200の3200をして`
  - `に2200の 3200をれて`

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
  - `の2210にで5100ったをして`
  - `2210の 5100をとしてして`
  - `2210の5100をして`
  - `2210にった 5100をにして`
  - `2210のとして 5100をして`
  - `に5100ったので、2210のにれて`
  - `の2210、で5100ったことをして`
  - `2210の 5100をして`
  - `2210の5100をして`
  - `に2210の 5100をれて`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - `，20000に， homehubとリマインドして`
  - `，20000に， homehubことをらせて`
  - `，20000に「， homehub」のリマインダーをして`
  - `，20000になったら， homehubとして`
  - `，20000のリマインダーとして， homehubをして`
  - `，20000に， homehubのをれて`
  - `，20000に， homehubことをれないようらせて`
  - `，20000ので， homehubをリマインドして`
  - `，20000にへ， homehubとえて`
  - `，20000に， homehubのをって`

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
  - `までのをして、を Excel にまとめて`
  - `ここまでのをして、Excel をって`
  - `のをし、Excel ファイルもして`
  - `をして、を Excel にしてほしい`
  - `とそのを Excel でして`
  - `までのをして、Excel でまとめて`
  - `のをえて、そのを Excel にして`
  - `までのをし、Excel ファイルをして`
  - `ここまでのを Excel としてして`
  - `のと、Excel へのきしをおい`

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
  - `の2220にで890ったをして`
  - `2220の 890をとしてして`
  - `2220の890をして`
  - `2220にった 890をにして`
  - `2220のとして 890をして`
  - `に890ったので、2220のにれて`
  - `の2220、で890ったことをして`
  - `2220の 890をして`
  - `2220の890をして`
  - `に2220の 890をれて`

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
  - `の2230にで640ったをして`
  - `2230の 640をとしてして`
  - `2230の640をして`
  - `2230にった 640をにして`
  - `2230のとして 640をして`
  - `に640ったので、2230のにれて`
  - `の2230、で640ったことをして`
  - `2230の 640をして`
  - `2230の640をして`
  - `に2230の 640をれて`

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
  - `の2240にで2750ったをして`
  - `2240の 2750をとしてして`
  - `2240の2750をして`
  - `2240にった 2750をにして`
  - `2240のとして 2750をして`
  - `に2750ったので、2240のにれて`
  - `の2240、で2750ったことをして`
  - `2240の 2750をして`
  - `2240の2750をして`
  - `に2240の 2750をれて`

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
  - `の2250にで450ったをして`
  - `2250の 450をとしてして`
  - `2250の450をして`
  - `2250にった 450をにして`
  - `2250のとして 450をして`
  - `に450ったので、2250のにれて`
  - `の2250、で450ったことをして`
  - `2250の 450をして`
  - `2250の450をして`
  - `に2250の 450をれて`

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
  - `の2300にで990ったをして`
  - `2300の 990をとしてして`
  - `2300の990をして`
  - `2300にった 990をにして`
  - `2300のとして 990をして`
  - `に990ったので、2300のにれて`
  - `の2300、で990ったことをして`
  - `2300の 990をして`
  - `2300の990をして`
  - `に2300の 990をれて`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - `，35000に， homehubとリマインドして`
  - `，35000に， homehubことをらせて`
  - `，35000に「， homehub」のリマインダーをして`
  - `，35000になったら， homehubとして`
  - `，35000のリマインダーとして， homehubをして`
  - `，35000に， homehubのをれて`
  - `，35000に， homehubことをれないようらせて`
  - `，35000ので， homehubをリマインドして`
  - `，35000にへ， homehubとえて`
  - `，35000に， homehubのをって`

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
  - `までのをして、を Excel にまとめて`
  - `ここまでのをして、Excel をって`
  - `のをし、Excel ファイルもして`
  - `をして、を Excel にしてほしい`
  - `とそのを Excel でして`
  - `までのをして、Excel でまとめて`
  - `のをえて、そのを Excel にして`
  - `までのをし、Excel ファイルをして`
  - `ここまでのを Excel としてして`
  - `のと、Excel へのきしをおい`

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
  - ` にのをして: 37.5，，`
  - ` へこのをして: 37.5，，`
  - ` にこのをして: 37.5，，`
  - ` に 37.5，， をして`
  - ` のとして 37.5，， をれて`
  - ` にをしてください: 37.5，，`
  - ` へこのをきんで: 37.5，，`
  - ` にしいを: 37.5，，`
  - `37.5，， を  にして`
  - ` にこのをして: 37.5，，`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - ` にのをして: 420，D，`
  - ` へこのをして: 420，D，`
  - ` にこのをして: 420，D，`
  - ` に 420，D， をして`
  - ` のとして 420，D， をれて`
  - ` にをしてください: 420，D，`
  - ` へこのをきんで: 420，D，`
  - ` にしいを: 420，D，`
  - `420，D， を  にして`
  - ` にこのをして: 420，D，`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - `に：4189，HomeHubとリマインドして`
  - `に：4189，HomeHubことをらせて`
  - `に「：4189，HomeHub」のリマインダーをして`
  - `になったら：4189，HomeHubとして`
  - `のリマインダーとして：4189，HomeHubをして`
  - `に：4189，HomeHubのをれて`
  - `に：4189，HomeHubことをれないようらせて`
  - `ので：4189，HomeHubをリマインドして`
  - `にへ：4189，HomeHubとえて`
  - `に：4189，HomeHubのをって`

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
  - `にとリマインドして`
  - `にことをらせて`
  - `に「」のリマインダーをして`
  - `になったらとして`
  - `のリマインダーとしてをして`
  - `にのをれて`
  - `にことをれないようらせて`
  - `のでをリマインドして`
  - `にへとえて`
  - `にのをって`

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
  - `にとリマインドして`
  - `にことをらせて`
  - `に「」のリマインダーをして`
  - `になったらとして`
  - `のリマインダーとしてをして`
  - `にのをれて`
  - `にことをれないようらせて`
  - `のでをリマインドして`
  - `にへとえて`
  - `にのをって`

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
  - ` にのをして: 20，`
  - ` へこのをして: 20，`
  - ` にこのをして: 20，`
  - ` に 20， をして`
  - ` のとして 20， をれて`
  - ` にをしてください: 20，`
  - ` へこのをきんで: 20，`
  - ` にしいを: 20，`
  - `20， を  にして`
  - ` にこのをして: 20，`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - ` にのをして: ，，`
  - ` へこのをして: ，，`
  - ` にこのをして: ，，`
  - ` に ，， をして`
  - ` のとして ，， をれて`
  - ` にをしてください: ，，`
  - ` へこのをきんで: ，，`
  - ` にしいを: ，，`
  - `，， を  にして`
  - ` にこのをして: ，，`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - ` にのをして: 2，，`
  - ` へこのをして: 2，，`
  - ` にこのをして: 2，，`
  - ` に 2，， をして`
  - ` のとして 2，， をれて`
  - ` にをしてください: 2，，`
  - ` へこのをきんで: 2，，`
  - ` にしいを: 2，，`
  - `2，， を  にして`
  - ` にこのをして: 2，，`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - `，2000に， homehubとリマインドして`
  - `，2000に， homehubことをらせて`
  - `，2000に「， homehub」のリマインダーをして`
  - `，2000になったら， homehubとして`
  - `，2000のリマインダーとして， homehubをして`
  - `，2000に， homehubのをれて`
  - `，2000に， homehubことをれないようらせて`
  - `，2000ので， homehubをリマインドして`
  - `，2000にへ， homehubとえて`
  - `，2000に， homehubのをって`

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
  - ` のをせて`
  - ` にあるをして`
  - ` のをしたい`
  - ` のをたい`
  - ` にっているをせて`
  - ` のをして`
  - ` のをえて`
  - ` のエントリーをして`
  - ` のデータをいて`
  - ` にがされているかせて`

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
  - ` をエクスポートして`
  - ` のデータをして`
  - ` をきしてください`
  - ` のをエクスポートしたい`
  - ` のエクスポートファイルをって`
  - ` をして`
  - ` のをファイルでして`
  - ` のデータをにして`
  - ` をダウンロードできるでして`
  - ` のエクスポートをして`

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
  - ` /tmp/homehub-family-suite/ext-school ，。`
  - `このをおいします:  /tmp/homehub-family-suite/ext-school ，。`
  - `のでしてください:  /tmp/homehub-family-suite/ext-school ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/ext-school ，。`
  - `このをめてください:  /tmp/homehub-family-suite/ext-school ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/ext-school ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/ext-school ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/ext-school ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/ext-school ，。`
  - `このでおいします:  /tmp/homehub-family-suite/ext-school ，。`

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
  - ` /tmp/homehub-family-suite/ext-bills ，。`
  - `このをおいします:  /tmp/homehub-family-suite/ext-bills ，。`
  - `のでしてください:  /tmp/homehub-family-suite/ext-bills ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/ext-bills ，。`
  - `このをめてください:  /tmp/homehub-family-suite/ext-bills ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/ext-bills ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/ext-bills ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/ext-bills ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/ext-bills ，。`
  - `このでおいします:  /tmp/homehub-family-suite/ext-bills ，。`

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
  - ` /tmp/homehub-family-suite/ext-photos ，。`
  - `このをおいします:  /tmp/homehub-family-suite/ext-photos ，。`
  - `のでしてください:  /tmp/homehub-family-suite/ext-photos ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/ext-photos ，。`
  - `このをめてください:  /tmp/homehub-family-suite/ext-photos ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/ext-photos ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/ext-photos ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/ext-photos ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/ext-photos ，。`
  - `このでおいします:  /tmp/homehub-family-suite/ext-photos ，。`

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
  - ` /tmp/homehub-family-suite/ext-recipes ，。`
  - `このをおいします:  /tmp/homehub-family-suite/ext-recipes ，。`
  - `のでしてください:  /tmp/homehub-family-suite/ext-recipes ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/ext-recipes ，。`
  - `このをめてください:  /tmp/homehub-family-suite/ext-recipes ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/ext-recipes ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/ext-recipes ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/ext-recipes ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/ext-recipes ，。`
  - `このでおいします:  /tmp/homehub-family-suite/ext-recipes ，。`

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
  - ` /tmp/homehub-family-suite/ext-mixed ，。`
  - `このをおいします:  /tmp/homehub-family-suite/ext-mixed ，。`
  - `のでしてください:  /tmp/homehub-family-suite/ext-mixed ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/ext-mixed ，。`
  - `このをめてください:  /tmp/homehub-family-suite/ext-mixed ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/ext-mixed ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/ext-mixed ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/ext-mixed ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/ext-mixed ，。`
  - `このでおいします:  /tmp/homehub-family-suite/ext-mixed ，。`

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
  - ` /tmp/homehub-family-suite/ext-visitors ，。`
  - `このをおいします:  /tmp/homehub-family-suite/ext-visitors ，。`
  - `のでしてください:  /tmp/homehub-family-suite/ext-visitors ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/ext-visitors ，。`
  - `このをめてください:  /tmp/homehub-family-suite/ext-visitors ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/ext-visitors ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/ext-visitors ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/ext-visitors ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/ext-visitors ，。`
  - `このでおいします:  /tmp/homehub-family-suite/ext-visitors ，。`

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
  - ` /tmp/homehub-family-suite/ext-pet ，。`
  - `このをおいします:  /tmp/homehub-family-suite/ext-pet ，。`
  - `のでしてください:  /tmp/homehub-family-suite/ext-pet ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/ext-pet ，。`
  - `このをめてください:  /tmp/homehub-family-suite/ext-pet ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/ext-pet ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/ext-pet ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/ext-pet ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/ext-pet ，。`
  - `このでおいします:  /tmp/homehub-family-suite/ext-pet ，。`

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
  - ` /tmp/homehub-family-suite/ext-health ，。`
  - `このをおいします:  /tmp/homehub-family-suite/ext-health ，。`
  - `のでしてください:  /tmp/homehub-family-suite/ext-health ，。`
  - `いえるとこういうです:  /tmp/homehub-family-suite/ext-health ，。`
  - `このをめてください:  /tmp/homehub-family-suite/ext-health ，。`
  - `のをしてほしいです:  /tmp/homehub-family-suite/ext-health ，。`
  - `このとしてってください:  /tmp/homehub-family-suite/ext-health ，。`
  - `のはのとおりです:  /tmp/homehub-family-suite/ext-health ，。`
  - `のリクエストにえてください:  /tmp/homehub-family-suite/ext-health ，。`
  - `このでおいします:  /tmp/homehub-family-suite/ext-health ，。`

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
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をんで`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をいてをせて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のをして`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をみってください`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のをして`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をいてんでほしい`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のファイルをえて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をしてをせて`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt をんでをして`
  - `/tmp/homehub-family-suite/family-reading/shopping-note.txt のをしてください`

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
  - `/tmp/homehub-family-suite/family-library/meal-plan.md をんで`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md をいてをせて`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md のをして`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md をみってください`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md のをして`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md をいてんでほしい`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md のファイルをえて`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md をしてをせて`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md をんでをして`
  - `/tmp/homehub-family-suite/family-library/meal-plan.md のをしてください`

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
  - `/tmp/homehub-family-suite/family-reading/recipe.json をんで`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をいてをせて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のをして`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をみってください`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のをして`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をいてんでほしい`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のファイルをえて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をしてをせて`
  - `/tmp/homehub-family-suite/family-reading/recipe.json をんでをして`
  - `/tmp/homehub-family-suite/family-reading/recipe.json のをしてください`

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
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをせて、そのあと receipt.pdf をって`
  - `/tmp/homehub-family-suite/family-inbox のファイルをして、receipt.pdf をってください`
  - `/tmp/homehub-family-suite/family-inbox にがあるかして、receipt.pdf をして`
  - `/tmp/homehub-family-suite/family-inbox のをせてから receipt.pdf をって`
  - `/tmp/homehub-family-suite/family-inbox をして、receipt.pdf をにして`
  - `/tmp/homehub-family-suite/family-inbox のファイルをして、receipt.pdf をして`
  - `/tmp/homehub-family-suite/family-inbox にあるものをえて、receipt.pdf もって`
  - `/tmp/homehub-family-suite/family-inbox をいてファイルをし、receipt.pdf をってください`
  - `/tmp/homehub-family-suite/family-inbox のをて、receipt.pdf をしてください`
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをしたうえで receipt.pdf をって`

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
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをせて、そのあと monthly_budget.xlsx をって`
  - `/tmp/homehub-family-suite/family-inbox のファイルをして、monthly_budget.xlsx をってください`
  - `/tmp/homehub-family-suite/family-inbox にがあるかして、monthly_budget.xlsx をして`
  - `/tmp/homehub-family-suite/family-inbox のをせてから monthly_budget.xlsx をって`
  - `/tmp/homehub-family-suite/family-inbox をして、monthly_budget.xlsx をにして`
  - `/tmp/homehub-family-suite/family-inbox のファイルをして、monthly_budget.xlsx をして`
  - `/tmp/homehub-family-suite/family-inbox にあるものをえて、monthly_budget.xlsx もって`
  - `/tmp/homehub-family-suite/family-inbox をいてファイルをし、monthly_budget.xlsx をってください`
  - `/tmp/homehub-family-suite/family-inbox のをて、monthly_budget.xlsx をしてください`
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをしたうえで monthly_budget.xlsx をって`

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
  - `/tmp/homehub-family-suite/family-library で meal にするファイルをして`
  - `/tmp/homehub-family-suite/family-library の meal ファイルをして`
  - `/tmp/homehub-family-suite/family-library のから meal にするファイルをつけて`
  - `/tmp/homehub-family-suite/family-library で meal をむファイルをして`
  - `/tmp/homehub-family-suite/family-library の meal ファイルをたい`
  - `/tmp/homehub-family-suite/family-library をして meal ファイルをつけて`
  - `/tmp/homehub-family-suite/family-library にある meal ファイルをして`
  - `/tmp/homehub-family-suite/family-library ので meal にいファイルをして`
  - `/tmp/homehub-family-suite/family-library から meal ファイルをつけてください`
  - `/tmp/homehub-family-suite/family-library の meal にするファイルをして`

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
  - `/tmp/homehub-family-suite/family-library で photo にするファイルをして`
  - `/tmp/homehub-family-suite/family-library の photo ファイルをして`
  - `/tmp/homehub-family-suite/family-library のから photo にするファイルをつけて`
  - `/tmp/homehub-family-suite/family-library で photo をむファイルをして`
  - `/tmp/homehub-family-suite/family-library の photo ファイルをたい`
  - `/tmp/homehub-family-suite/family-library をして photo ファイルをつけて`
  - `/tmp/homehub-family-suite/family-library にある photo ファイルをして`
  - `/tmp/homehub-family-suite/family-library ので photo にいファイルをして`
  - `/tmp/homehub-family-suite/family-library から photo ファイルをつけてください`
  - `/tmp/homehub-family-suite/family-library の photo にするファイルをして`

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
  - `/tmp/homehub-family-suite/family-inbox にあるファイルをせて`
  - `/tmp/homehub-family-suite/family-inbox のファイルをにして`
  - `/tmp/homehub-family-suite/family-inbox のにのファイルがあるかえて`
  - `/tmp/homehub-family-suite/family-inbox のファイルをしたい`
  - `/tmp/homehub-family-suite/family-inbox のをせてください`
  - `/tmp/homehub-family-suite/family-inbox にっているファイルをして`
  - `/tmp/homehub-family-suite/family-inbox をいてをして`
  - `/tmp/homehub-family-suite/family-inbox のファイルをえて`
  - `/tmp/homehub-family-suite/family-inbox にがあるかチェックして`
  - `/tmp/homehub-family-suite/family-inbox のファイルをせて`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - ` /Users/home/Documents ，。`
  - `このをおいします:  /Users/home/Documents ，。`
  - `のでしてください:  /Users/home/Documents ，。`
  - `いえるとこういうです:  /Users/home/Documents ，。`
  - `このをめてください:  /Users/home/Documents ，。`
  - `のをしてほしいです:  /Users/home/Documents ，。`
  - `このとしてってください:  /Users/home/Documents ，。`
  - `のはのとおりです:  /Users/home/Documents ，。`
  - `のリクエストにえてください:  /Users/home/Documents ，。`
  - `このでおいします:  /Users/home/Documents ，。`

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
  - `Tell me the weather in Tokyo today.`
  - `How's the weather in Tokyo today?`
  - `Please give me today's forecast in Tokyo.`
  - `What's the high temperature in Tokyo today?`
  - `Tell me today's high temperature in Tokyo.`
  - `How warm will it get in Tokyo today?`
  - `Please check today's forecast and high temperature for Tokyo.`
  - `I'd like today's weather and the high temperature in Tokyo.`

- Japanese Variants: 10
  - `ののをえて`
  - `はどんなかりたい`
  - `ののをて`
  - `のをして`
  - `ははどんな？`
  - `ののは？`
  - `のとをえて`
  - `はまでがる？`
  - `ののいをりたい`
  - `ののとをして`

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
  - `What is the weather like in Fukuoka today?`
  - `Can you check today's weather in Fukuoka?`
  - `Tell me the weather in Fukuoka today.`
  - `How's the weather in Fukuoka today?`
  - `Please give me today's forecast in Fukuoka.`
  - `Will it rain in Fukuoka today?`
  - `Can you check whether it's going to rain in Fukuoka today?`
  - `Is rain expected in Fukuoka today?`
  - `Tell me if I should expect rain in Fukuoka today.`
  - `Please check today's rain chances in Fukuoka.`

- Japanese Variants: 10
  - `ののをえて`
  - `はどんなかりたい`
  - `ののをて`
  - `のをして`
  - `ははどんな？`
  - `はがる？`
  - `ののをえて`
  - `ではのがある？`
  - `ののをして`
  - `ははになるかて`

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
  - `Tell me the weather in Osaka today.`
  - `How's the weather in Osaka today?`
  - `Please give me today's forecast in Osaka.`
  - `What's today's temperature in Osaka?`
  - `Tell me the temperature in Osaka today.`
  - `How many degrees is it in Osaka today?`
  - `Can you check today's temperature for Osaka?`
  - `I'd like to know the current temperature in Osaka today.`

- Japanese Variants: 10
  - `ののをえて`
  - `はどんなかりたい`
  - `ののをて`
  - `のをして`
  - `ははどんな？`
  - `ののは？`
  - `ののをえて`
  - `ははくらい？`
  - `ののをして`
  - `ののがりたい`

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
  - `こののフライトとをべて`
  - `ののスケジュールとをして`
  - `このののとをりたい`
  - `するフライトのとをて`
  - `こののをべて`
  - `のとをしてほしい`
  - `このフライトのなとをして`
  - `のスケジュールとをせて`
  - `こののフライトとをべて`
  - `できるでフライトとをして`

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
  - `こののとをべて`
  - `ルートののとをして`
  - `こののスケジュールとをりたい`
  - `のとをて`
  - `こののとをべて`
  - `のとをしてほしい`
  - `こののをべて`
  - `するのとをせて`
  - `このルートのとをして`
  - `のとをして`

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
  - `のなら MacBook Air と MacBook Pro のどちらがいているか、Apple をにえて`
  - `Apple サイトをに、には Air と Pro のどちらがうかえて`
  - `のオフィスワークに MacBook Air と Pro をべてほしい`
  - `Apple ベースで、なら Air と Pro のどちらがよいかりたい`
  - `なけに Air と Pro のおすすめを Apple をてえて`
  - `MacBook Air と Pro のどちらがのにしているかてほしい`
  - `Apple のサイトをに、けのおすすめをえて`
  - `として Air と Pro のどちらをぶべきか Apple でえて`
  - `オフィスなら Air と Pro のどちらがいているかりたい`
  - `Apple をに MacBook Air と Pro をしてアドバイスして`

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
  - `Apple サイトで 13 インチ MacBook Air のはいくら？`
  - `13 インチ MacBook Air のAppleのをえて`
  - `Apple で 13 インチ MacBook Air はいくらから？`
  - `13 インチ MacBook Air のなをして`
  - `Apple サイトの 13 インチ MacBook Air のをりたい`
  - `13 インチ MacBook Air のベースを Apple でべて`
  - `Apple ページで 13 インチ MacBook Air のをて`
  - `13 インチ MacBook Air のスタートはいくらかえて`
  - `Apple の 13 インチ MacBook Air のをして`
  - `Apple サイトで 13 インチ MacBook Air ののをえて`

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
  - `Apple サイトで 14 インチ MacBook Pro のはいくら？`
  - `14 インチ MacBook Pro のAppleのをえて`
  - `Apple で 14 インチ MacBook Pro はいくらから？`
  - `14 インチ MacBook Pro のなをして`
  - `Apple サイトの 14 インチ MacBook Pro のをりたい`
  - `14 インチ MacBook Pro のベースを Apple でべて`
  - `Apple ページで 14 インチ MacBook Pro のをて`
  - `14 インチ MacBook Pro のスタートはいくらかえて`
  - `Apple の 14 インチ MacBook Pro のをして`
  - `Apple サイトで 14 インチ MacBook Pro ののをえて`

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
  - `Time Machine ， とはかえて`
  - `Time Machine ， についてして`
  - `Time Machine ， のをりたい`
  - `Time Machine ， がなのかえて`
  - `Time Machine ， をにして`
  - `Time Machine ， のをえて`
  - `Time Machine ， って？`
  - `Time Machine ， についてわかりやすくえて`
  - `Time Machine ， のなをりたい`
  - `Time Machine ， がどんなものかして`

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
  - `Liquid Retina  とはかえて`
  - `Liquid Retina  についてして`
  - `Liquid Retina  のをりたい`
  - `Liquid Retina  がなのかえて`
  - `Liquid Retina  をにして`
  - `Liquid Retina  のをえて`
  - `Liquid Retina  って？`
  - `Liquid Retina  についてわかりやすくえて`
  - `Liquid Retina  のなをりたい`
  - `Liquid Retina  がどんなものかして`

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
  - `Time Machine  とはかえて`
  - `Time Machine  についてして`
  - `Time Machine  のをりたい`
  - `Time Machine  がなのかえて`
  - `Time Machine  をにして`
  - `Time Machine  のをえて`
  - `Time Machine  って？`
  - `Time Machine  についてわかりやすくえて`
  - `Time Machine  のなをりたい`
  - `Time Machine  がどんなものかして`

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
  - `Tell me the weather in Tokyo today.`
  - `How's the weather in Tokyo today?`
  - `Please give me today's forecast in Tokyo.`
  - `What's today's temperature in Tokyo?`
  - `Tell me the temperature in Tokyo today.`
  - `How many degrees is it in Tokyo today?`
  - `Can you check today's temperature for Tokyo?`
  - `I'd like to know the current temperature in Tokyo today.`

- Japanese Variants: 10
  - `ののをえて`
  - `はどんなかりたい`
  - `ののをて`
  - `のをして`
  - `ははどんな？`
  - `ののは？`
  - `ののをえて`
  - `ははくらい？`
  - `ののをして`
  - `ののがりたい`

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
  - `What is the weather like in Tokyo today?`
  - `Can you check today's weather in Tokyo?`
  - `Tell me the weather in Tokyo today.`
  - `How's the weather in Tokyo today?`
  - `Please give me today's forecast in Tokyo.`
  - `Will it rain in Tokyo today?`
  - `Can you check whether it's going to rain in Tokyo today?`
  - `Is rain expected in Tokyo today?`
  - `Tell me if I should expect rain in Tokyo today.`
  - `Please check today's rain chances in Tokyo.`

- Japanese Variants: 10
  - `ののをえて`
  - `はどんなかりたい`
  - `ののをて`
  - `のをして`
  - `ははどんな？`
  - `はがる？`
  - `ののをえて`
  - `ではのがある？`
  - `ののをして`
  - `ははになるかて`

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
  - `Time Machine  とはかえて`
  - `Time Machine  についてして`
  - `Time Machine  のをりたい`
  - `Time Machine  がなのかえて`
  - `Time Machine  をにして`
  - `Time Machine  のをえて`
  - `Time Machine  って？`
  - `Time Machine  についてわかりやすくえて`
  - `Time Machine  のなをりたい`
  - `Time Machine  がどんなものかして`

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
  - `，，`
  - `こののレシピとな、りをえて`
  - `りとなをめたレシピをりたい`
  - `このにうレシピをして、もえて`
  - `とつきでレシピをえて`
  - `このメニューのりをにまとめて`
  - `なとをえてほしい`
  - `レシピをして、とれをして`
  - `このをるためのとをりたい`
  - `でりやすいレシピをえて`

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
  - `，`
  - `こののレシピとな、りをえて`
  - `りとなをめたレシピをりたい`
  - `このにうレシピをして、もえて`
  - `とつきでレシピをえて`
  - `このメニューのりをにまとめて`
  - `なとをえてほしい`
  - `レシピをして、とれをして`
  - `このをるためのとをりたい`
  - `でりやすいレシピをえて`

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
  - `  とはかえて`
  - `  についてして`
  - `  のをりたい`
  - `  がなのかえて`
  - `  をにして`
  - `  のをえて`
  - `  って？`
  - `  についてわかりやすくえて`
  - `  のなをりたい`
  - `  がどんなものかして`

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
  - ` とはかえて`
  - ` についてして`
  - ` のをりたい`
  - ` がなのかえて`
  - ` をにして`
  - ` のをえて`
  - ` って？`
  - ` についてわかりやすくえて`
  - ` のなをりたい`
  - ` がどんなものかして`

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
  - `ののニュースを2、きでえて`
  - `でのニュースを2つして`
  - `ののホットニュースを2まとめて`
  - `ののニュースを2つくして`
  - `ののを2だけでえて`
  - `のニュースからを2つして`
  - `のできなニュースを2まとめてほしい`
  - `ののトレンドニュースを2えて`
  - `のニュースのを2つだけりたい`
  - `ののしニュースを2して`

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
  - `NVIDIA ののはいくら？`
  - `NVIDIA ののをえて`
  - `NVIDIA はいくらでされている？`
  - `NVIDIA ののをして`
  - `NVIDIA ののをりたい`
  - `NVIDIA ののときをえて`
  - `NVIDIA ののとげげをして`
  - `NVIDIA ははどういている？もえて`
  - `NVIDIA ののとをたい`
  - `NVIDIA のとのをえて`

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
  - `Apple ののはいくら？`
  - `Apple ののをえて`
  - `Apple はいくらでされている？`
  - `Apple ののをして`
  - `Apple ののをりたい`
  - `Apple のをでせて`
  - `Apple ののをして`
  - `Apple ののをえて`
  - `Apple のをたい`
  - `Apple ののをチェックして`

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
  - `， とはかえて`
  - `， についてして`
  - `， のをりたい`
  - `， がなのかえて`
  - `， をにして`
  - `， のをえて`
  - `， って？`
  - `， についてわかりやすくえて`
  - `， のなをりたい`
  - `， がどんなものかして`

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
  - ` とはかえて`
  - ` についてして`
  - ` のをりたい`
  - ` がなのかえて`
  - ` をにして`
  - ` のをえて`
  - ` って？`
  - ` についてわかりやすくえて`
  - ` のなをりたい`
  - ` がどんなものかして`

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
  - `こののとをべて`
  - `ルートののとをして`
  - `こののスケジュールとをりたい`
  - `のとをて`
  - `こののとをべて`
  - `のとをしてほしい`
  - `こののをべて`
  - `するのとをせて`
  - `このルートのとをして`
  - `のとをして`

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
  - `Please check the flight times and fares for 帮我查一下月底从Tokyo飞旧金山的大概航班时间和价格，尽量给我靠谱来源.`
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
  - `こののフライトとをべて`
  - `ののスケジュールとをして`
  - `このののとをりたい`
  - `するフライトのとをて`
  - `こののをべて`
  - `のとをしてほしい`
  - `このフライトのなとをして`
  - `のスケジュールとをせて`
  - `こののフライトとをべて`
  - `できるでフライトとをして`

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
  - `，`
  - `どもにもわかるいでして`
  - `けにやさしくえて`
  - `どもがしやすいでして`
  - `できるだけにして`
  - `どもけのやさしいにして`
  - `なでわかりやすくえて`
  - `しいをわずにして`
  - `どもにすようにやさしくして`
  - `かみいてわかりやすくえて`
