export default class Key {
    /**
     * @param {HTMLElement} element HTML element for the key
     * @param {Note} note Note object for the key
     * @param {MouseState} mouse MouseState object to track mouse clicks even when not on the keyboard
     * @param {Recorder} recorder Recorder object to record notes to
     */
    constructor(element, note, mouse, recorder) {
        this.element = element;
        this.note = note;
        this.mouse = mouse;
        this.recorder = recorder;

        this.pressed = false;

        this.setListeners();
    }

    press() {
        // set the key press flag
        this.pressed = true;
        // set the active class on the key
        this.element.classList.add("active");
        // start playing the note
        this.note.start();
        this.recorder.addEvent(this.note.frequency, true);
    }

    release() {
        // if the key is currently being pressed
        if (this.pressed) {
            // unset the press flag
            this.pressed = false;
            // unset the active class on the key
            this.element.classList.remove("active");
            // stop playing the note
            this.note.stop();
            this.recorder.addEvent(this.note.frequency, false);
        }
    }

    enter() {
        // if the mouse button is held down, play the note
        console.log(this.mouse.buttonState);
        if (this.mouse.buttonState) this.press();
    }

    /**
     * Create event listeners on each key element
     */
    setListeners() {
        // listeners for mouse and touch press
        this.element.addEventListener("mousedown", this.press.bind(this));
        this.element.addEventListener("touchstart", this.press.bind(this));
        // listeners for releasing the key
        this.element.addEventListener("mouseup", this.release.bind(this));
        this.element.addEventListener("touchend", this.release.bind(this));
        // listen for entering and leaving a key
        this.element.addEventListener("mouseenter", this.enter.bind(this));
        this.element.addEventListener("mouseleave", this.release.bind(this));
    }
}
