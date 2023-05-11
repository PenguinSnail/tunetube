import { Player } from "../classes.js";
import { generatePlaybackHandler } from "../playback.js";

const context = new AudioContext();
const player = new Player(context);

const postCards = document.querySelectorAll(".post-card");
postCards.forEach((post) => {
    generatePlaybackHandler(post.querySelector(".play-button"), player);
    post.addEventListener("click", () => {
        window.location.href = `/post/${post.dataset.id}`;
    });
});
