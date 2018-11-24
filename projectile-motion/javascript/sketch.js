new p5();

var ball;
var width;
var height;

function sleep(millisecs) {
    var initiation = new Date().getTime();
    while ((new Date().getTime() - initiation) < millisecs);
}

function setup() {
    ball = new Ball(37, 25, 10, 30);
    width = 640;
    height = 480;
    createCanvas(width, height);
}

function draw () {
    background(255); fill(255);
    stroke(0); strokeWeight(3);

    line(0, height, width, height);

    var x = ball.pos[0];
    var y = ball.pos[1];

    var x_ = map(x, 0, ball.range, 0, width);
    var y_ = map(y, 0, ball.max_y, height, 0)

    text (`Object(a=${ball.a / (Math.PI / 180)}, v=[${[round(ball.v[0]), round(ball.v[1])]}], g=${ball.g})`, 10, 15);
    text (`range: ${round(ball.range)}`, 10, 30);
    text (`max_y: ${round(ball.max_y)}`, 10, 45)
    text (`curr pos: [${[round(x), round(y)]}]`, 10, 60)

    strokeWeight(1);
    ellipse(x_, y_, 10, 10); ball.update();

    sleep(90);
}