import { Player } from "../classes.js";
import { setupCard } from "../post-card.js";

const context = new AudioContext();
const player = new Player(context);

const postCard = document.querySelector(".post-card");

setupCard(postCard, player, false);

document.querySelectorAll(".comment-card").forEach((commentCard) => {
    const deleteButton = commentCard.querySelector(".delete-button");
    deleteButton.addEventListener("click", async (event) => {
        event.stopPropagation();
        try {
            const response = await fetch(`/tunes/${postCard.dataset.id}/comments/${commentCard.dataset.id}`, {
                method: "DELETE",
            });

            if (response.ok) {
                window.location.href = `/tunes/${postCard.dataset.id}`;
            } else {
                alert("Error deleting comment!");
            }
        } catch (e) {
            console.error(e);
        }
    });
});
