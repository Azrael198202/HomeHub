# HomeHub Detailed Test Results

## Executive Summary

**Generated**: 2026-04-12T16:39
**Source Document**: homehub-clean.md
**Test Cases Executed**: 20
**✅ PASS**: 19 (95.0%)
**❌ FAIL**: 1
**⚠️ ERRORS**: 0

---

## Performance Metrics

- **Total Execution Time**: 377.82 seconds
- **Average Response Time**: 18.89 seconds per test
- **Fastest Response**: 0.00s
- **Slowest Response**: 37.96s

---

## Results by Stage

| Stage | Total | PASS | FAIL | ERRORS | Pass Rate | Avg Time |
|-------|-------|------|------|--------|-----------|----------|
| 阶段1 | 20 | 19 | 1 | 0 | 95.0% | 18.89s |

---

## Detailed Test Results

### S1-01: 本地问候 1

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 0.00 seconds

#### Query
```
你好
```

#### Expected Result
```
返回自然问候。
```

#### Actual Result
```
你好，有什么可以帮忙的？
```

#### Validation Analysis
- **Validation Score**: 1.00/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 12 chars
- ✅ **Greeting content**: Greeting tokens found: True

---

### S1-02: 本地问候 2

**Status**: FAIL
**Stage**: 阶段1
**Execution Time**: 18.78 seconds

#### Query
```
你好啊 HomeHub
```

#### Expected Result
```
返回自然问候。
```

#### Actual Result
```
家庭活动安排 已完成。核心职责：用于记录家庭活动时间、地点和参与成员。；触发：家庭成员提出需要规划家庭活动的需求或请求。；输出：根据你的需求，我将为你规划一个家庭活动，并在指定的时间内通知所有成员。。 家庭活动安排 的 feature 模板已生成，路径是 /Users/home/workspace/HomeHub/runtime/features/customize/family_feature.py。
```

#### Validation Analysis
- **Validation Score**: 0.00/1.0
- **Analysis**: Test failed or requires manual review

##### Validation Checks
- ✅ **Response exists**: Response length: 203 chars
- ❌ **Greeting content**: Greeting tokens found: False

##### Recommendations
- Manual verification recommended

---

### S1-03: 本地问候 3

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 0.00 seconds

#### Query
```
早上好
```

#### Expected Result
```
返回自然问候。
```

#### Actual Result
```
你好，有什么可以帮忙的？
```

#### Validation Analysis
- **Validation Score**: 1.00/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 12 chars
- ✅ **Greeting content**: Greeting tokens found: True

---

### S1-04: 本地问候 4

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 0.00 seconds

#### Query
```
晚上好
```

#### Expected Result
```
返回自然问候。
```

#### Actual Result
```
你好，有什么可以帮忙的？
```

#### Validation Analysis
- **Validation Score**: 1.00/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 12 chars
- ✅ **Greeting content**: Greeting tokens found: True

---

### S1-05: 天气查询 1

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 30.82 seconds

#### Query
```
福冈今天的天气怎么样，最高温多少
```

#### Expected Result
```
返回天气信息或明确降级。
```

#### Actual Result
```
福冈今天的天气最高温度为20.9℃，体感温度约为18℃。有阵雨，风速约为7.6公里/小时。
来源：福冈县, 福冈县, 日本天气预报和情况 - The Weather Channel | Weather.com (weather.com)；【福冈天气】福冈天气预报,天气预报一周,天气预报15天查询 (weather.com.cn)；福冈的今日天气｜日本｜Luft Time (time.luft.co.jp)
```

#### Validation Analysis
- **Validation Score**: 0.80/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 204 chars
- ✅ **Weather information**: Weather indicators found: True

---

### S1-06: 天气查询 2

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 29.42 seconds

#### Query
```
东京今天气温多少
```

#### Expected Result
```
返回天气信息或明确降级。
```

#### Actual Result
```
根据网络查询，东京今天的气温约为23°C。请注意，这个信息可能需要结合其他因素来判断，如风力和湿度等。
来源：天气 - 东京 - 14天预报：气温、风和雷达 | Ventusky (ventusky.com)；东京都, 东京都, 日本天气预报和情况 - The Weather Channel | Weather.com (weather.com)；今天天气 - 东京, 日本 - Weather Atlas (weather-atlas.com)
```

#### Validation Analysis
- **Validation Score**: 0.80/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 224 chars
- ✅ **Weather information**: Weather indicators found: True

---

### S1-07: 天气查询 3

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 19.00 seconds

#### Query
```
大阪今天会下雨吗
```

#### Expected Result
```
返回天气信息或明确降级。
```

#### Actual Result
```
根据提供的信息，大阪市今天不会下雨。您可以参考日本气象协会的天気预报（tenki.jp）和Yahoo!天气灾害页面获取更详细的信息。如果您想了解其他地区的天气情况，请告诉我。
来源：大阪市の1時間天気 - 日本気象協会 tenki.jp (tenki.jp)；大阪市の天気予報(1時間・今日明日・週間) - ウェザーニュース (weathernews.jp)；大阪（大阪）の天気 - Yahoo!天気・災害 (weather.yahoo.co.jp)
```

#### Validation Analysis
- **Validation Score**: 0.80/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 225 chars
- ✅ **Weather information**: Weather indicators found: True

---

### S1-08: 天气查询 4

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 37.96 seconds

#### Query
```
请告诉我今天的天气，并告诉我最高温度
```

#### Expected Result
```
返回天气信息或明确降级。
```

#### Actual Result
```
今天最高温度预计为25℃。请注意防暑降温。
来源：中国气象局-天气预报 (weather.cma.cn)；天气网 (weather.com.cn)；天气预报,天气预报查询一周,天气预报15天查询,今天,明天,7天,10天,15天,30天,今天,明天,40天,未来一周天气预报查询_天气网 (tianqi.com)
```

#### Validation Analysis
- **Validation Score**: 0.80/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 156 chars
- ✅ **Weather information**: Weather indicators found: True

---

### S1-09: 列出家庭收件箱

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 17.06 seconds

#### Query
```
查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
路径不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 20 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-10: 发送收件箱演示文稿

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 14.69 seconds

#### Query
```
查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，family_trip.pptx 文件发给我。
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
路径不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 20 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-11: 搜索预算文件

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 17.54 seconds

#### Query
```
搜索 /tmp/homehub-family-suite/family-inbox 下面的 budget 文件
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
搜索目录不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 22 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-12: 读取购物便签

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 23.45 seconds

#### Query
```
读取 /tmp/homehub-family-suite/family-reading/shopping-note.txt
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
路径不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 20 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-13: 读取菜谱 JSON

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 35.10 seconds

#### Query
```
读取 /tmp/homehub-family-suite/family-reading/recipe.json
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
路径不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 20 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-14: 列出家庭资料库

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 15.81 seconds

#### Query
```
查看 /tmp/homehub-family-suite/family-library 下面有什么文件
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
路径不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 20 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-15: 发送 Documents 夹里的演示文稿

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 18.44 seconds

#### Query
```
查看 /Users/home/Documents 下面有什么文件，AI_Agent_Build2026 en.pptx 文件发给我。
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
/Users/home/Documents 下有这些文件：Documents、Finance、Media、Playground、Text、AI_Agent_Build2026 en.pptx。我也已经把 AI_Agent_Build2026 en.pptx 准备成附件了。
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 136 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-16: 搜索照片

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 16.11 seconds

#### Query
```
搜索 /tmp/homehub-family-suite/family-library 下面的 photo 文件
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
搜索目录不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 22 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-17: 分类 Alpha 目录

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 23.96 seconds

#### Query
```
将 /tmp/homehub-family-suite/classify-alpha 下的文件，进行分类。类型创建新的文件夹。
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
路径不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 20 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-18: 分类 Beta 目录

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 15.19 seconds

#### Query
```
将 /tmp/homehub-family-suite/classify-beta 下的文件，进行分类。类型创建新的文件夹。
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
路径不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 20 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-19: 家庭文档目录权限降级

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 24.11 seconds

#### Query
```
将 /Users/home/Documents 下的文件，进行分类。类型创建新的文件夹。
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
我已经按类型整理了 /Users/home/Documents 下的文件，并创建了这些文件夹：Documents。
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 57 chars
- ✅ **File operation response**: File indicators found: True

---

### S1-20: 发送 PDF 收据

**Status**: PASS
**Stage**: 阶段1
**Execution Time**: 20.38 seconds

#### Query
```
查看 /tmp/homehub-family-suite/family-inbox 下面有什么文件，receipt.pdf 文件发给我。
```

#### Expected Result
```
完成本地文件操作或给出明确降级。
```

#### Actual Result
```
路径不可用：path_not_found
```

#### Validation Analysis
- **Validation Score**: 0.90/1.0
- **Analysis**: Test passed with good confidence

##### Validation Checks
- ✅ **Response exists**: Response length: 20 chars
- ✅ **File operation response**: File indicators found: True

---

## Test Statistics

### Response Quality Distribution
- **0.0 - 0.3**: 1 tests
- **0.3 - 0.6**: 0 tests
- **0.6 - 0.8**: 0 tests
- **0.8 - 1.0**: 16 tests

### Common Failure Patterns
- **Greeting content**: 1 occurrences

---

## Test Environment

- **Python Version**: 3.14.3
- **Platform**: macOS
- **Runtime**: HomeHub local server
- **Test Mode**: Detailed execution with validation

## Notes

- Tests executed in isolated runtime environment
- Network-dependent tests may fail in offline environments
- Validation uses heuristic analysis of response content
- Manual review recommended for borderline cases
