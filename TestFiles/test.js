const canvas = document.getElementById("canvas");
const image = document.getElementById("image_1");

canvas.width = 500;
canvas.height = 500;
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');



let x = canvas.width / 2;
let y = canvas.height / 2;
let angle = 0;


function line(x1, y1, x2, y2) {
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}


function forward(distance) {
    const rad = angle * Math.PI / 180;
    const newX = x + distance * Math.cos(rad);
    const newY = y + distance * Math.sin(rad);
    line(x, y, newX, newY);
    x = newX;
    y = newY;
}


function right(deg) {
    angle = (angle + deg) % 360;
}


async function draw() {
    ctx.lineWidth = 1;
    ctx.strokeStyle = 'black';
    for (let i = 0; i < 500; i++) {
        forward(i/5);
        right(10);
        await new Promise(resolve => setTimeout(resolve, 10));
    }
}



ctx.drawImage(image, 0, 0);
draw();
line(0, 0, 500, 250);
