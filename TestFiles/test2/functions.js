const canvas = document.getElementById("canvas");
canvas.width = 1280;
canvas.height = 577;
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');

const floor_1 = document.getElementById("floor_1");
const floor_2 = document.getElementById("floor_2");
const floor_3 = document.getElementById("floor_3");
const floor_4 = document.getElementById("floor_4");


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