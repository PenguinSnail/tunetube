import Note from "./classes/Note.js";

export default class Player {
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
        try {
            this.data = JSON.parse(data);
        } catch {
            alert("Error parsing tune data!");
            return false;
        }

        // for each event in the data
        this.data.forEach((event) => {
            // check if the note for this event exists in the notes map
            if (!this.notes.get(event.frequency)) {
                // create a new note of a specified frequency
                this.notes.set(event.frequency, new Note(this.context, event.frequency));
            }
        });

        return true;
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
