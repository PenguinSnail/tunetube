/* Noah Piraino - 2023-03-29 */

/**
 * Controls nav link visibility on mobile devices
 */

const navLinksContainer = document.querySelector(".nav-links-container");
const menuButton = document.querySelector("nav .menu-button");
const menuButtonIcon = menuButton.querySelector("i");

menuButton.addEventListener("click", () => {
    navLinksContainer.classList.toggle("visible");

    menuButtonIcon.classList.toggle("fa-bars");
    menuButtonIcon.classList.toggle("fa-xmark");
});
