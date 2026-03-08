const canvas = document.getElementById("canvas");

const floor_1 = document.getElementById("floor_1");
const floor_2 = document.getElementById("floor_2");
const floor_3 = document.getElementById("floor_3");
const floor_4 = document.getElementById("floor_4");
const floors = [floor_1, floor_2, floor_3, floor_4]

const button_1 = document.getElementById("button_1");
const button_2 = document.getElementById("button_2");
const button_3 = document.getElementById("button_3");
const button_4 = document.getElementById("button_4");
const buttons = [button_1, button_2, button_3, button_4];


const ctx = canvas.getContext('2d');

for (let i = 0; i < buttons.length; i++) {
    buttons[i].style.position = "absolute";
    buttons[i].style.top = `${100 + 50 * i}px`;
    buttons[i].style.left = "1300px";
    buttons[i].style.visibility = "visible";
}



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

    ctx.drawImage(floors[parseInt(floor) - 1], 0, 0);
}



ctx.drawImage(floor_1, 0, 0);
