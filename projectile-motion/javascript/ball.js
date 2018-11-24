/*
    Projectile motion simulation by gh/l0x6c
    ball.js
*/

function Ball (a, v, g, p) {
    this.p = p;
    this.g = g;
    this.a = a * (Math.PI / 180);
    this.v = [
        v * Math.cos(this.a),
        v * Math.sin(this.a)
    ];

    this.pos = [0, 0];
    this.passed_t = 0;

    this._time = 2 * this.v[1] / g;
    this.range = this.v[0] * this._time;
    this.max_y = Math.pow(this.v[1], 2) / (2 * g);

    this.position = function (t) {
        return [
            this.v[0] * t,
            this.v[1] * t - this.g * Math.pow(t, 2) / 2
        ];
    }

    this.update = function () {
        if (this.passed_t >= this._time) {
            this.passed_t = 0;
        }

        this.passed_t += this._time / this.p;
        this.pos = this.position(this.passed_t)
    }
}