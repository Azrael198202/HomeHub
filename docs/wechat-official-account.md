# WeChat Official Account Setup

HomeHub now supports WeChat Official Account developer mode in `plaintext` webhook mode.

## Required secrets

Store these values in `runtime/secrets.local.json`:

```json
{
  "wechatOfficialToken": "your-wechat-token",
  "wechatOfficialAppId": "wx1234567890abcdef",
  "wechatOfficialAppSecret": "your-app-secret",
  "wechatOfficialEncodingAesKey": ""
}
```

`wechatOfficialEncodingAesKey` can stay empty for now because the current webhook implementation is for plaintext mode, not AES-encrypted mode.

## Webhook URL

Point the WeChat developer callback URL to:

```text
https://your-homehub-domain/api/external-channels/wechat/webhook
```

## Current behavior

- Supports WeChat developer verification with `signature`, `timestamp`, `nonce`, and `echostr`
- Accepts inbound XML messages from the Official Account webhook
- Routes text, image, voice, and basic event messages into HomeHub
- Returns passive XML text replies back to WeChat
- Stores inbound and outbound channel activity in `runtime/data/external_channels.json`

## Current limitation

- AES encrypted webhook mode is not implemented yet
- Active customer-service message sending is still queued only
- Access-token based outbound push is not wired yet

## Recommended test flow

1. Fill `wechatOfficialToken` and `wechatOfficialAppId` in `runtime/secrets.local.json`
2. Restart HomeHub
3. Configure the same token in the WeChat Official Account developer console
4. Use plaintext mode for the first webhook test
5. Send a text message to the Official Account and verify HomeHub replies

## documents

https://github.com/BytePioneer-AI/openclaw-china/blob/main/doc/guides/wechat-mp/configuration.md
