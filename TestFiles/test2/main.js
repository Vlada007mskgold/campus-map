import * as functions from './functions.js';



const canvas = document.getElementById("canvas");

const floor_1 = document.getElementById("floor_1");
const floor_2 = document.getElementById("floor_2");
const floor_3 = document.getElementById("floor_3");
const floor_4 = document.getElementById("floor_4");

const button_1 = document.getElementById("button_1");
const button_2 = document.getElementById("button_2");
const button_3 = document.getElementById("button_3");
const button_4 = document.getElementById("button_4");


canvas.width = 1280;
canvas.height = 577;
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');

button_1.style.position = "absolute";
button_1.style.top = "100px";
button_1.style.left = "1550px";

button_2.style.position = "absolute";
button_2.style.top = "150px";
button_2.style.left = "1550px";

button_3.style.position = "absolute";
button_3.style.top = "200px";
button_3.style.left = "1550px";

button_4.style.position = "absolute";
button_4.style.top = "250px";
button_4.style.left = "1550px";



ctx.drawImage(floor_1, 0, 0);
functions.line(0, 0, 500, 500);

button_1.style.visibility = "visible";
button_2.style.visibility = "visible";
button_3.style.visibility = "visible";
button_4.style.visibility = "visible";
