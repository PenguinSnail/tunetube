import { Player } from "../classes.js";
import { generatePlaybackHandler } from "../playback.js";

const context = new AudioContext();
const player = new Player(context);

const playButtons = document.querySelectorAll("button.play-button");
playButtons.forEach((button) => generatePlaybackHandler(button, player));
