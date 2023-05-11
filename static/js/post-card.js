/**
 * Setup event handlers on a post card
 * @param {HTMLElement} card post card div element
 * @param {Player} player tune player object
 * @param {Boolean} link whether or not to link to the post page
 */
export function setupCard(card, player, link) {
    const playButton = card.querySelector(".play-button");
    playButton.addEventListener("click", async (event) => {
        event.stopPropagation();
        const icon = playButton.querySelector("i");

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
                const response = await fetch(`/post/${card.dataset.id}/data`);
                const data = await response.json();

                player.load(data);
                player.setProgressOutput(playButton.parentElement.querySelector("span"));
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

    if (link)
        card.addEventListener("click", () => {
            window.location.href = `/post/${card.dataset.id}`;
        });
}
