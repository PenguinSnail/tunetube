export const generatePlaybackHandler = (button, player) =>
    button.addEventListener("click", async () => {
        const icon = button.querySelector("i");

        const currentlyPlaying = document.querySelector(".fa-circle-pause");
        if (currentlyPlaying && currentlyPlaying != icon) {
            currentlyPlaying.classList.remove("fa-circle-pause");
            currentlyPlaying.classList.add("fa-circle-play");
            player.stop();
        }

        if (icon.classList.contains("fa-circle-play")) {
            icon.classList.remove("fa-circle-play");
            icon.classList.add("fa-circle-pause");

            try {
                const response = await fetch(`/post/${button.dataset.id}/data`);
                const data = await response.json();

                player.load(data);
                player.setProgressOutput(button.parentElement.querySelector("span"));
                await player.start();
                icon.classList.remove("fa-circle-pause");
                icon.classList.add("fa-circle-play");
            } catch (e) {
                console.error(e);
                icon.classList.remove("fa-circle-pause");
                icon.classList.add("fa-circle-play");
            }
        } else {
            player.stop();
            icon.classList.remove("fa-circle-pause");
            icon.classList.add("fa-circle-play");
        }
    });
