import Note from "./classes/Note.js";
import Key from "./classes/Key.js";
import Recorder from "./classes/Recorder.js";
import MouseState from "./classes/MouseState.js";

const context = new AudioContext();
const recorder = new Recorder();
const mouse = new MouseState();

// Get all our key elements and attach new Key objects
Array.from(document.querySelectorAll(".key")).forEach(
    (element) => new Key(element, new Note(context, Number(element.id)), mouse, recorder)
);

/*
const recordBtn = document.querySelector('#output-section button');
recordBtn.addEventListener('click', () => {
    if (!recorder.recording) {
        recorder.start();
        recordBtn.textContent = "STOP RECORDING";
    } else {
        recorder.stop();
        document.querySelector('#output').textContent = JSON.stringify(recorder.data, undefined, 2);
        recordBtn.textContent = "RECORD";
    }
});
*/
