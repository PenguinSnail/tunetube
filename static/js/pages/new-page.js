import { Note, Key, Recorder } from "../classes.js";

const context = new AudioContext();
const recorder = new Recorder();

// Get all our key elements and attach new Key objects
Array.from(document.querySelectorAll(".key")).forEach(
    (element) => new Key(element, new Note(context, Number(element.id)), recorder)
);

const form = document.querySelector("form");
const recordBtn = document.querySelector("#record-button");
const submitBtn = document.querySelector("#submit-button");

recordBtn.addEventListener("click", (e) => {
    e.preventDefault();
    if (!recorder.recording) {
        recorder.start();
        recordBtn.textContent = "Stop Recording";
        submitBtn.setAttribute("disabled", "true");
    } else {
        recorder.stop();
        console.log(recorder.data);
        recordBtn.textContent = "Record";
        if (recorder.data.length > 0) {
            submitBtn.removeAttribute("disabled");
        }
    }
});

submitBtn.addEventListener("click", (e) => {
    e.preventDefault();
    if (form.reportValidity()) {
        if (recorder.data.length > 0) {
            const dataElem = document.createElement("input");
            dataElem.type = "hidden";
            dataElem.name = "data";
            dataElem.value = JSON.stringify(recorder.data);
            form.appendChild(dataElem);
            form.submit();
        }
    }
});
