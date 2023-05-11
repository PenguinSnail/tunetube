import { Player } from "../classes.js";
import { setupCard } from "../post-card.js";

const context = new AudioContext();
const player = new Player(context);

setupCard(document.querySelector("button.play-button"), player, false);

/*
const postComment = document.getElementById("post-comment");

postComment.addEventListener("keypress", function (e) {
    if (e.keyCode == 13 && !e.shiftKey) {
        document.getElementById("comment-form").submit();
    }
});
*/
