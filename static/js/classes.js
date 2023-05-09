export class Note {
    /**
     * @param {AudioContext} context AudioContext to play audio to
     * @param {Number} frequency Note frequency
     */
    constructor(context, frequency) {
        this.context = context;
        this.frequency = frequency;
        this.oscillator;
    }

    start() {
        // stop the note in case it was somehow left playing or stuck on
        // the cause seems to be fixed but we'll leave this here just in case
        this.stop();

        // create a new oscillator and connect to the audio context
        this.oscillator = new OscillatorNode(this.context);
        this.oscillator.connect(this.context.destination);
        // set the oscillator frequency
        this.oscillator.frequency.setValueAtTime(this.frequency, this.context.currentTime);
        // start playing the tone
        this.oscillator.start();
    }

    stop() {
        if (this.oscillator) {
            // stop and disconnect the oscillator, then delete it
            // will be recreated when the note is played next
            this.oscillator.stop();
            this.oscillator.disconnect();
            delete this.oscillator;
        }
    }
}

/* -------------------------------------------------------------------------- */

export class Key {
    /**
     * @param {HTMLElement} element HTML element for the key
     * @param {Note} note Note object for the key
     * @param {Recorder} recorder Recorder object to record notes to
     */
    constructor(element, note, recorder) {
        this.element = element;
        this.note = note;
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
        // listen for leaving a key
        this.element.addEventListener("mouseleave", this.release.bind(this));
    }
}

/* -------------------------------------------------------------------------- */

export class Recorder {
    constructor() {
        this.data = [];
        this.recording = false;
        this.startTime;
    }

    /**
     * Start recording
     */
    start() {
        this.data = [];
        this.recording = true;
        this.startTime = Date.now();
    }

    /**
     * Stop recording
     */
    stop() {
        this.recording = false;
    }

    /**
     * Record a note event
     * @param {number} frequency note frequency
     * @param {boolean} playing note start or end
     */
    addEvent(frequency, playing) {
        // if we are recording, push a new event object to the data array
        if (this.recording) {
            this.data.push({
                time: Date.now() - this.startTime,
                frequency: frequency,
                playing: playing,
            });
        }
    }
}

/* -------------------------------------------------------------------------- */

export class Player {
    /**
     * @param {AudioContext} context AudioContext to play audio to
     */
    constructor(context) {
        this.context = context;
        this.playing = false;
        /** Map of each note needed to play the tune */
        this.notes = new Map();
        /** Tune event array */
        this.data = [];
        /** Timers for each event */
        this.timers = [];
    }

    /**
     * Load tune data into the player
     * @param {string} data JSON string of events
     * @returns {boolean} load succeeded or failed
     */
    load(data) {
        this.data = data;

        // for each event in the data
        this.data.forEach((event) => {
            // check if the note for this event exists in the notes map
            if (!this.notes.get(event.frequency)) {
                // create a new note of a specified frequency
                this.notes.set(event.frequency, new Note(this.context, event.frequency));
            }
        });
    }

    /**
     * Start playback
     * @returns {Promise<void>} resolves when/if playback completes (does not resolve if playback is forcefully stopped)
     */
    start() {
        return new Promise((resolve) => {
            // set the playing flag
            this.playing = true;
            // for each event
            this.data.forEach((event) => {
                // add a new timer to the timers array for the time specified in the event
                this.timers.push(
                    setTimeout(() => {
                        // get the note specified from the notes map
                        const note = this.notes.get(event.frequency);
                        // stop or start the note according to the event
                        if (event.playing) {
                            note.start();
                        } else {
                            note.stop();
                        }
                    }, event.time)
                );
            });

            // get the timestamp of the last event
            console.log(this.data);
            const endTime = this.data[this.data.length - 1].time;
            // create a timer for the last event timestamp
            this.timers.push(
                setTimeout(() => {
                    // stop playback and resolve the promise
                    this.stop();
                    resolve();
                }, endTime)
            );
        });
    }

    /** Stop playback */
    stop() {
        this.playing = false;
        // clear all remaining timers
        this.timers.forEach((timer) => clearTimeout(timer));
        // stop playing all notes
        this.notes.forEach((note) => note.stop());
    }
}
