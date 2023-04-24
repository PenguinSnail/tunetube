export default class Note {
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
