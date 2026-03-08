const canvas = document.getElementById("canvas");

const floor_1 = document.getElementById("floor_1");
const floor_2 = document.getElementById("floor_2");
const floor_3 = document.getElementById("floor_3");
const floor_4 = document.getElementById("floor_4");

const button_1 = document.getElementById("button_1");
const button_2 = document.getElementById("button_2");
const button_3 = document.getElementById("button_3");
const button_4 = document.getElementById("button_4");



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



function line(x1, y1, x2, y2) {
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}



function handleClick(buttonElement) {
    const data = buttonElement.value;
    floor = data;
    document.getElementById('output').textContent = 'Button value: ' + floor;

    if (floor == "1") { ctx.drawImage(floor_1, 0, 0); }
    else if (floor == "2") { ctx.drawImage(floor_2, 0, 0); }
    else if (floor == "3") { ctx.drawImage(floor_3, 0, 0); }
    else if (floor == "4") { ctx.drawImage(floor_4, 0, 0); }
}



ctx.drawImage(floor_1, 0, 0);
button_1.style.visibility = "visible";
button_2.style.visibility = "visible";
button_3.style.visibility = "visible";
button_4.style.visibility = "visible";
