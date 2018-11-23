new p5();

var ball;
var width;
var height;

function sleep(millisecs) {
    var initiation = new Date().getTime();
    while ((new Date().getTime() - initiation) < millisecs);
}

function setup() {
    ball = new Ball(37, 25, 10, 60);
    width = 600;
    height = 480;
    createCanvas(width, height);
}

function draw () {
    background(0);
    stroke(255);
    strokeWeight(3);

    var x = ball.pos[0];
    var y = ball.pos[1];

    var x_ = map(x, 0, ball.range, 0, width);
    var y_ = map(y, 0, ball.max_y, height, 0)

    text (`Object(a=${ball.a / (Math.PI / 180)}, v=[${[round(ball.v[0]), round(ball.v[1])]}], g=${ball.g})`, 10, 15);
    text (`range: ${round(ball.range)}`, 10, 30);
    text (`max_y: ${round(ball.max_y)}`, 10, 45)
    text (`curr pos: [${[round(x), round(y)]}]`, 10, 60)

    strokeWeight(5); point (x_, y_); ball.update();
    sleep(90);
}