import { Player } from "./classes.js";

const context = new AudioContext();
const player = new Player(context);

const playButtons = document.querySelectorAll("button.play-btn");
playButtons.forEach((button) =>
    button.addEventListener("click", async () => {
        player.stop();

        const oldBtn = document.querySelector(".fa-circle-pause");
        if (oldBtn) {
            oldBtn.classList.remove("fa-circle-pause");
            oldBtn.classList.add("fa-circle-play");
        }

        const i = button.querySelector("i");
        if (i.classList.contains("fa-circle-play")) {
            i.classList.remove("fa-circle-play");
            i.classList.add("fa-circle-pause");

            try {
                const response = await fetch(`/post/${button.id}/data`);
                const data = await response.json();

                player.load(data);
                await player.start();
                i.classList.remove("fa-circle-pause");
                i.classList.add("fa-circle-play");
            } catch (e) {
                console.error(e);
                i.classList.remove("fa-circle-pause");
                i.classList.add("fa-circle-play");
            }
        } else {
            player.stop();
            i.classList.remove("fa-circle-pause");
            i.classList.add("fa-circle-play");
        }
    })
);
