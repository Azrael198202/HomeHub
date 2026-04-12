# HomeHub Stage 1 Live Network Validation

- Generated at: 2026-04-09T22:43
- Scope: targeted live-network validation for the remaining Stage 1 network-dependent cases
- Note: this supplements the offline regression report and does not replace the full 3-phase local regression results

## Case 1: 福冈天气

- Query: `福冈今天的天气怎么样，温度多少。`
- Result: `PASS`
- Actual:

  `福冈今天的天气预报显示，温度大约在16℃到19℃之间。预计会有阵雨和中雨转小雨的天气变化，风速为每小时28公里，湿度约为82%，露点温度为17℃。空气质量一般，能见度较低，风向主要是南风。请注意携带雨具并注意安全。`

- Sources:
  - `weather.com.cn`
  - `weather.com`
  - `accuweather.com`

## Case 2: 日本 -> 美国航班

- Query: `我要从日本去美国，帮我查询5月31号的所有去美国的飞机，时间和价格`
- Result: `PASS`
- Actual:

  `我已经查到可用的机票搜索来源，但它们目前提供的主要是搜索入口，还没有直接给出“日本全境到美国全境、5月31日”的完整航班时间和价格列表。这类查询范围太大，时间和价格会随出发城市、到达城市、是否直飞而变化。如果你补充出发城市和到达城市，例如“东京到洛杉矶”或“福冈到纽约”，我就可以继续按时间和价格帮你整理。`

- Sources:
  - `google.com/flights`
  - `flights.ctrip.com`
  - `skyscanner.net`

## Outcome

- Weather lookup now returns a real grounded weather answer when network access is available.
- Broad flight queries no longer hallucinate fake flight numbers, fake times, or placeholder prices.
- For underspecified country-to-country flight requests, HomeHub now gives a conservative, source-grounded next-step answer instead of inventing details.
