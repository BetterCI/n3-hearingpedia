// Native controls; no automatic playback or response collection.
const players = [...document.querySelectorAll('.timbre-audio-demo audio')];
for (const player of players) {
  player.volume = 0.2;
  player.addEventListener('play', () => {
    for (const other of players) {
      if (other !== player) other.pause();
    }
  });
}
