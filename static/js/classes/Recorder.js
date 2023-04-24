export default class Recorder {
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
