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
        forward(i / 5);
        right(10);
        await new Promise(resolve => setTimeout(resolve, 10));
    }
}


function handleClick(buttonElement) {
    const data = buttonElement.value;
    floor = data;
    document.getElementById('output').textContent = 'Button value: ' + floor;

    if (floor == "1") { ctx.drawImage(floor_1, 0, 0); }
    else { ctx.drawImage(floor_2, 0, 0); }
}