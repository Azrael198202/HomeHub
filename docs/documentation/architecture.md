# HomeHub Architecture

## System Overview

HomeHub is a living-room AI box system composed of six layers:

1. `TV Display Layer`
2. `Starter Capability Layer`
3. `Core Engine`
4. `Voice Layer`
5. `Communication Bridge`
6. `Box System Layer`

## Runtime Flow

1. The box boots directly into the TV shell.
2. The TV shell fetches device state, pair status, and household modules from local services.
3. Commands can arrive from voice, mobile companion app, external IM, or local remote control UI.
4. The communication bridge normalizes text, image, and audio instructions.
5. The core engine fans work out to multiple agents in parallel.
6. Agent progress and development activity are surfaced on the TV screen in real time.
7. Results are dispatched back to TV, phone, or external IM.

## Security Notes

- Pairing should use one-time QR codes with short expiry.
- Relay content for text, image, and voice should be deleted immediately after delivery.
- Sensitive household memory should support encrypted local storage.
