import { Player } from "../classes.js";
import { setupCard } from "../post-card.js";

const context = new AudioContext();
const player = new Player(context);

const postCards = document.querySelectorAll(".post-card");
postCards.forEach((post) => setupCard(post, player, true));
