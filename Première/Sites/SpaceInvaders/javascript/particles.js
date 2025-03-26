class Particle {
    constructor (color, drawing) {
        this.dx = (Math.random () - 0.5) * Math.random () * 6;
        this.dy = (Math.random () - 0.5) * Math.random () * 6;
        this.alpha = 1
        this.drawing = drawing;
        this.color = color;
        this.alive = true;
        this.x = 0;
        this.y = 0;
    }

    update () {
        if (this.alive) {
            this.alpha -= 0.01;
            if (this.alpha <= 0)
                this.alive = false;
            this.x += this.dx;
            this.y += this.dy;
        }
    }

    draw (x, y) {
        if (this.alive)
            this.drawing.drawPixelWithAlpha (x + this.x, y + this.y, this.color, this.alpha);
    }

}