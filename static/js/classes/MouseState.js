// track the mouse button state (used to allow slides)
// https://stackoverflow.com/a/48970682

export default class MouseState {
    constructor() {
        this.buttonState = false;

        document.addEventListener("mousedown", this.setState);
        document.addEventListener("mouseup", this.setState);
        // how expensive are these event listeners?
        // Do we need to be listening for every mouse move?
        document.addEventListener("mousemove", this.setState);
    }

    setState(event) {
        const flags = event.buttons !== undefined ? event.buttons : event.which;
        this.buttonState = flags === 1;
    }
}
