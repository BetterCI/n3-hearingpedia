// Native controls remain usable when scripting is unavailable.
const players = [...document.querySelectorAll('[data-ci-vocoder-demo] audio')];
for (const player of players) {
  player.volume = 0.2;
  player.addEventListener('play', () => {
    for (const other of players) if (other !== player) other.pause();
  });
}
