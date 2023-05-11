import { Player } from "../classes.js";
import { setupCard } from "../post-card.js";

const context = new AudioContext();
const player = new Player(context);

setupCard(document.querySelector(".post-card"), player, false);
