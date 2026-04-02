export const voiceGatewayProfile = {
  stt: {
    primary: "on-device-whisper",
    fallback: "cloud-streaming-stt"
  },
  tts: {
    primary: "cloud-neural-voice",
    fallback: "system-tts"
  },
  notes: [
    "Keep wake-word detection on device.",
    "Stream partial transcripts to the TV shell for visible turn-taking."
  ]
};

console.log(JSON.stringify(voiceGatewayProfile, null, 2));
