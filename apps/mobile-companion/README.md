# Mobile Companion

This directory is reserved for the Flutter-based companion app.

## Intended User Experience

- phone and tablet interface similar to mainstream IM applications
- pairing with the HomeHub box through QR code
- send text, voice, and image instructions to the box
- receive replies, status updates, and household notifications

## Suggested Flutter Modules

- `lib/app`: app shell and navigation
- `lib/features/pairing`: QR scan and pair session handling
- `lib/features/chat`: IM-style message timeline
- `lib/features/voice`: hold-to-talk and voice reply playback
- `lib/features/box`: device list and settings
- `lib/data`: API clients for the communication bridge
