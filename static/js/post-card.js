/**
 * Setup event handlers on a post card
 * @param {HTMLElement} card post card div element
 * @param {Player} player tune player object
 * @param {Boolean} link whether or not to link to the post page
 */
export function setupCard(card, player, link) {
    const playButton = card.querySelector(".play-button");
    const likeButton = card.querySelector(".like-button");
    const deleteButton = card.querySelector(".delete-button");

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
                const response = await fetch(`/tunes/${card.dataset.id}/data`);
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

    likeButton.addEventListener("click", async (event) => {
        event.stopPropagation();
        const icon = likeButton.querySelector("i");

        try {
            const response = await fetch(`/tunes/${card.dataset.id}/like`, {
                method: icon.classList.contains("fa-solid") ? "DELETE" : "POST",
            });

            if (response.ok) {
                icon.classList.toggle("fa-solid");
                icon.classList.toggle("fa-regular");
            } else {
                alert("Error liking post!");
            }
        } catch (e) {
            console.error(e);
        }
    });

    if (deleteButton)
        deleteButton.addEventListener("click", async (event) => {
            event.stopPropagation();
            try {
                const response = await fetch(`/tunes/${card.dataset.id}`, { method: "DELETE" });

                if (response.ok) {
                    window.location.href = "/tunes";
                } else {
                    alert("Error deleting post!");
                }
            } catch (e) {
                console.error(e);
            }
        });

    if (link)
        card.addEventListener("click", () => {
            window.location.href = `/tunes/${card.dataset.id}`;
        });
}
