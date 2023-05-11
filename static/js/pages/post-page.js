import { Player } from "../classes.js";
import { generatePlaybackHandler } from "../playback.js";

const context = new AudioContext();
const player = new Player(context);

generatePlaybackHandler(document.querySelector("button.play-button"), player);

/*
const postComment = document.getElementById("post-comment");

postComment.addEventListener("keypress", function (e) {
    if (e.keyCode == 13 && !e.shiftKey) {
        document.getElementById("comment-form").submit();
    }
});
*/
