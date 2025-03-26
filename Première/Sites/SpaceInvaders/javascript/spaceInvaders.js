class Keys {
    #memo = {}

    onKeyDown (key) {
        this.#memo [key] = true;
    }

    onKeyUp (key) {
        this.#memo [key] = false;
    }

    isDown (key) {
        return this.#memo [key];
    }
}

class SpaceShip {
    #alive = [
        0b0000001000000,
        0b0000011100000,
        0b0000011100000,
        0b0111111111110,
        0b1111111111111,
        0b1111111111111,
        0b1111111111111
    ];
    #dead = [
        0b0000100000000,
        0b0000000000000,
        0b0000101010000,
        0b0010100000000,
        0b0000011011000,
        0b1001011010100,
        0b0011111111101,
        0b0111111110101
    ]

    constructor (x, y, color, drawing) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.drawing = drawing;
        this.dx = 0;
        this.width = 13;
        this.isAlive = true;
    }

    draw () {
        let y = this.y;
        if (!this.isAlive)
            --y;
        const start = this.x;
        const datas = this.isAlive ? this.#alive : this.#dead;

        for (let line of datas) {
            let mask = 0b0000000000001;

            for (let i = 0; i < 13; i++) {
                if (line & mask) {
                    this.drawing.drawPixel (start + i, y, this.color);
                }
                mask = mask << 1;
            }
            ++y;
        }
    }

    left () {
        this.dx = -1;
    }

    right () {
        this.dx = 1;
    }

    stop () {
        this.dx = 0;
    }

    update () {
        this.x += this.dx;
        if (this.x < 0)
            this.x = 0
        else if (this.x + 13 > this.drawing.width)
            this.x = this.drawing.width - 13
    }
}

class Alien {
    #types = [
        {
            first: [
                0b00100000100,
                0b00010001000,
                0b00111111100,
                0b01101110110,
                0b11111111111,
                0b10111111101,
                0b10100000101,
                0b00011011000
            ],
            second: [
                0b00100000100,
                0b10010001001,
                0b10111111101,
                0b11101110111,
                0b11111111111,
                0b01111111110,
                0b00100000100,
                0b01000000010
            ],
            explosion: [
                0b00100000100,
                0b10010001001,
                0b01000000010,
                0b00100000100,
                0b00100000100,
                0b01000000010,
                0b10010001001,
                0b00100000100,
            ],
            mask: 0b00000000001,
            width: 11,
            color: "rgb(255,0,0)"
        },
        {
            first: [
                0b00011000,
                0b00111100,
                0b01111110,
                0b11011011,
                0b11111111,
                0b00100100,
                0b01011010,
                0b10100101
            ],
            second: [
                0b00011000,
                0b00111100,
                0b01111110,
                0b11011011,
                0b11111111,
                0b00100100,
                0b01000010,
                0b00100100
            ],
            explosion: [
                0b00100100,
                0b10011001,
                0b01000010,
                0b00100100,
                0b00100100,
                0b01000010,
                0b10011001,
                0b00100100,
            ],
            mask: 0b00000001,
            width: 8,
            color: "rgb(255,255,0)"
        },
        {
            first: [
                0b000011110000,
                0b011111111110,
                0b111111111111,
                0b111001100111,
                0b111111111111,
                0b000110011000,
                0b001001100100,
                0b000100001000
            ],
            second: [
                0b000011110000,
                0b011111111110,
                0b111111111111,
                0b111001100111,
                0b111111111111,
                0b000110011000,
                0b001101101100,
                0b110000000011
            ],
            explosion: [
                0b001000000100,
                0b100100001001,
                0b010000000010,
                0b001000000100,
                0b001000000100,
                0b010000000010,
                0b100100001001,
                0b001000000100,
            ],
            mask: 0b000000000001,
            width: 12,
            color: "rgb(0,255,0)"
        },
        {
            first: [
                0b0010000100,
                0b0001001000,
                0b0011111100,
                0b0110110110,
                0b1111111111,
                0b1011111101,
                0b1001001001,
                0b0010000100
            ],
            second: [
                0b0000000000,
                0b0001001000,
                0b0011111100,
                0b0111111110,
                0b1110110111,
                0b1011111101,
                0b1001001001,
                0b0011001100
            ],
            explosion: [
                0b0010000100,
                0b1001001001,
                0b0100000010,
                0b0010000100,
                0b0010000100,
                0b0100000010,
                0b1001001001,
                0b0010000100,
            ],
            mask: 0b0000000001,
            width: 10,
            color: "rgb(128,128,128)"
        },
        {
            first: [
                0b1000001,
                0b0111110,
                0b1101011,
                0b1101011,
                0b0111110,
                0b1010101,
                0b1000001,
                0b0110110
            ],
            second: [
                0b1000001,
                0b0111110,
                0b1101011,
                0b1101011,
                0b0111110,
                0b0010100,
                0b0100010,
                0b1000001
            ],
            explosion: [
                0b0010100,
                0b1001001,
                0b0100010,
                0b0010100,
                0b0010100,
                0b0100010,
                0b1001001,
                0b0010100,
            ],
            mask: 0b0000001,
            width: 7,
            color: "rgb(64,64,255)"
        },
        {
            first: [
                0b001111100,
                0b011111110,
                0b110010011,
                0b111111111,
                0b000111000,
                0b001000100,
                0b010000010,
                0b100000001
            ],
            second: [
                0b001111100,
                0b011111110,
                0b110010011,
                0b111111111,
                0b000111000,
                0b001000100,
                0b010000010,
                0b001101100
            ],
            explosion: [
                0b001000100,
                0b100101001,
                0b010000010,
                0b001000100,
                0b001000100,
                0b010000010,
                0b100101001,
                0b001000100,
            ],
            mask: 0b000000001,
            width: 9,
            color: "rgb(255,255,255)"
        },
        {
            first: [
                0b0010000100,
                0b0001001000,
                0b0011111100,
                0b1110110111,
                0b1111111111,
                0b1011111101,
                0b1010000101,
                0b0001001000
            ],
            second: [
                0b0010000100,
                0b1001001001,
                0b1011111101,
                0b1110110111,
                0b0110110110,
                0b0111111110,
                0b0101001010,
                0b1100000011
            ],
            explosion: [
                0b0010000100,
                0b1001001001,
                0b0100000010,
                0b0010000100,
                0b0010000100,
                0b0100000010,
                0b1001001001,
                0b0010000100,
            ],
            mask: 0b0000000001,
            width: 10,
            color: "rgb(255,128,0)"
        },
        {
            first: [
                0b00011000,
                0b01111110,
                0b11111111,
                0b10011001,
                0b11111111,
                0b01011010,
                0b01000010,
                0b00111100
            ],
            second: [
                0b00011000,
                0b01111110,
                0b11111111,
                0b10011001,
                0b11111111,
                0b00100100,
                0b01011010,
                0b10000001
            ],
            explosion: [
                0b00100100,
                0b10011001,
                0b01000010,
                0b00100100,
                0b00100100,
                0b01000010,
                0b10011001,
                0b00100100,
            ],
            mask: 0b00000001,
            width: 8,
            color: "rgb(0,128,255)"
        },
        {
            first: [
                0b000000000,
                0b001000100,
                0b011111110,
                0b110010011,
                0b111111111,
                0b111111111,
                0b010101010,
                0b101010101
            ],
            second: [
                0b000000000,
                0b001000100,
                0b011111110,
                0b110010011,
                0b111111111,
                0b111111111,
                0b101010101,
                0b010101010
            ],
            explosion: [
                0b001000100,
                0b100101001,
                0b010000010,
                0b001000100,
                0b001000100,
                0b010000010,
                0b100101001,
                0b001000100,
            ],
            mask: 0b000000001,
            width: 9,
            color: "rgb(255,0,255)"
        },
        {
            first: [
                0b00100100,
                0b01111110,
                0b11011011,
                0b11111111,
                0b10100101,
                0b10011001,
                0b10000001,
                0b11000011
            ],
            second: [
                0b00100100,
                0b00011000,
                0b10111101,
                0b11011011,
                0b11111111,
                0b10111101,
                0b10011001,
                0b11000011
            ],
            explosion: [
                0b00100100,
                0b10011001,
                0b01000010,
                0b00100100,
                0b00100100,
                0b01000010,
                0b10011001,
                0b00100100,
            ],
            mask: 0b00000001,
            width: 8,
            color: "rgb(255,192,192)"
        },
    ];

    constructor (x, y, type, next, step, val, player, drawing) {
        this.x = x;
        this.y = y;
        this.color = this.#types [type].color;
        this.first = this.#types [type].first;
        this.second = this.#types [type].second;
        this.explosion = this.#types [type].explosion;
        this.mask = this.#types [type].mask;
        this.width = this.#types [type].width;
        this.current = this.first;
        this.dx = 1;
        this.drawing = drawing;
        this.counter = 0;
        this.next = next;
        this.step = step;
        this.killed = false;
        this.countdown = 0;
        this.value = val;
        this.firing = false;
        this.bomb = new Bomb (player, this, this.drawing, this.color);
        this.speedOn = false;
        this.exploding = false;
        this.particles = []
        for (let i = 0; i < 50; i++)
            this.particles.push (new Particle (this.color, this.drawing))

    }

    touched () {
        this.killed = true;
        this.current = this.explosion;
        this.countdown = 20;
    }

    fire () {
        this.firing = true;
        this.bomb.x = this.x + this.width / 2;
        this.bomb.y = this.y + 10
    }

    draw () {
        if (this.exploding) {
            this.particles.forEach ((particle, i) => particle.draw (this.xc, this.yc))
        }
        else {
            if (this.countdown > 10) {   
                --this.countdown;
            }
            else if (this.countdown > 1) {
                this.drawing.text (this.x + this.width / 2, this.y + 5, this.value, "center", "middle", this.color);
            }
            if (this.countdown == 0 || this.countdown > 10) {
                let y = this.y;

                for (let line of this.current) {
                    let mask = this.mask;

                    for (let i = 0; i < this.width; i++) {
                        if (line & mask) {
                            this.drawing.drawPixel (this.x + i, y, this.color);
                        }
                        mask = mask << 1;
                    }
                    ++y;
                }
            }
            if (this.firing)
                this.bomb.draw ();
        }
    }

    explode () {
        this.exploding = true;
        this.xc = this.x + this.width / 2;
        this.yc= this.y + 4;
    }

    update () {
        if (this.exploding) {
            this.particles.forEach ((particle, i) => particle.update ())
        }
        else {
            this.counter = (this.counter + 1) % 6;
            if (this.counter == 0) {
                if (this.countdown == 0) {
                    if (this.current == this.first)
                        this.current = this.second;
                    else
                        this.current = this.first;
                }
            }
            if (this.speedOn || this.counter == 0 || this.counter == 2 || this.counter == 4) {
                if (this.next == null) {
                    if (this.x + this.width >= this.drawing.width - 2) {
                        this.dx = -this.dx;
                        this.y += 16;
                    }
                }
                else {
                    if (this.x > this.next.x + this.next.width + this.step) {
                        this.dx = -this.dx;
                        this.x = this.next.x + this.next.width + this.step
                        this.y += 16;    
                    }
                }
                if (this.next == null) {
                    if (this.x <= 2) {
                        this.dx = -this.dx;
                        this.y += 16;
                    }
                }
                else {
                    if (this.dx == -1 && this.x < this.next.x - this.width - this.step) {
                        this.dx = -this.dx;
                        this.x = this.next.x - this.width - this.step
                        this.y += 16;    
                    }
                }
                this.x += this.dx
                if (this.y >= 100)
                    this.y = 10;
            }
            if (this.firing)
                this.bomb.update ();
        }
    }
}

class Bullet {
    constructor (drawing, color) {
        this.drawing = drawing;
        this.firing = false;
        this.color = color;
        this.x = 0;
        this.y = 0;
        this.countdown = 0;
    }

    draw () {
        this.drawing.drawPixel (this.x, this.y, this.color);
        this.drawing.drawPixel (this.x, this.y + 1, this.color);
    }

    update () {
        this.y -= 2;
        if (this.y < 0)
            this.firing = false;

    }
}

class Bomb {
    constructor (target, parent, drawing, color) {
        this.drawing = drawing;
        this.color = color;
        this.x = 0;
        this.y = 0;
        this.target = target;
        this.parent = parent;
        this.current = 0;
    }

    draw () {
        if (this.current < 1) {
            this.drawing.drawPixel (this.x, this.y, this.color);
            this.drawing.drawPixel (this.x - 1, this.y - 1, this.color);
            this.drawing.drawPixel (this.x, this.y - 2, this.color);
            this.drawing.drawPixel (this.x + 1, this.y - 3, this.color);
            this.drawing.drawPixel (this.x + 1, this.y + 1, this.color);
            this.drawing.drawPixel (this.x, this.y + 2, this.color);
            this.drawing.drawPixel (this.x - 1, this.y + 3, this.color);
        }
        if (this.current < 2) {
            this.drawing.drawPixel (this.x, this.y, this.color);
            this.drawing.drawPixel (this.x, this.y + 1, this.color);
            this.drawing.drawPixel (this.x, this.y + 2, this.color);
            this.drawing.drawPixel (this.x, this.y + 3, this.color);
            this.drawing.drawPixel (this.x, this.y - 1, this.color);
            this.drawing.drawPixel (this.x, this.y - 2, this.color);
            this.drawing.drawPixel (this.x, this.y - 3, this.color);
        }
        else {
            this.drawing.drawPixel (this.x, this.y, this.color);
            this.drawing.drawPixel (this.x - 1, this.y + 1, this.color);
            this.drawing.drawPixel (this.x, this.y + 2, this.color);
            this.drawing.drawPixel (this.x + 1, this.y + 3, this.color);
            this.drawing.drawPixel (this.x + 1, this.y - 1, this.color);
            this.drawing.drawPixel (this.x, this.y - 2, this.color);
            this.drawing.drawPixel (this.x - 1, this.y - 3, this.color);
        }
        this.current = (this.current + 1) % 3;
    }

    update () {
        ++this.y;
        if (this.y >= this.drawing.height + 2)
            this.parent.firing = false;
        if (this.y == this.target.y && this.x >= this.target.x && this.x <= this.target.x + this.target.width) {
            this.target.isAlive = false;
            this.parent.firing = false;
        }
    }
}



class Drawing {
    #ctx = null;

    constructor (canvasName, width, height, pixelSize) {
        this.#ctx = document.getElementById (canvasName).getContext ("2d");
        this.#ctx.font = "20pt retroGaming";
        this.width = width;
        this.height = height;
        this.pixelSize = pixelSize;    
    }

    drawPixel (x, y, color) {
        this.#ctx.beginPath ();
        this.#ctx.fillStyle = color;
        this.#ctx.rect (x * this.pixelSize, y * this.pixelSize, this.pixelSize, this.pixelSize);
        this.#ctx.fill ();
    }

    cls () {
        this.#ctx.clearRect (0, 0, this.width * this.pixelSize, this.height * this.pixelSize)
    }

    text (x, y, str, h, v, color) {
        this.#ctx.beginPath ();
        this.#ctx.textAlign = h;
        this.#ctx.textBaseline = v;
        this.#ctx.fillStyle = color;
        this.#ctx.fillText (str, x * this.pixelSize, y * this.pixelSize);
        this.#ctx.fill ();
    }

    bar (x, y, height, color) {
        for (let i = 0; i < height; i++)
            this.drawPixel (x, y + i, color);
    }

    drawPixelWithAlpha (x, y, color, alpha) {
        this.#ctx.save ();
        this.#ctx.globalAlpha = alpha;
        this.drawPixel (x, y, color)
        this.#ctx.restore ();
    }
}

function initThings () {
    const drawing = new Drawing ("spaceInvaders", 220, 100, 4);
    let saveTime = 0;
    const bombs = [];
    let paused = false;
    let nbKilled = 0;
    let endOfLevel = false;
    let score = 0;
    let timer;
    let target = null;
    let nbAliens = 6;
    let level = 0;
    let bonus = 0, goalStart = 0, goalEnd = nbAliens - 1;
    let gameBegin = true;
    let exploding = false;
    //let audioCtx = undefined;

    const fire = new Audio ("assets/sounds/shoot.wav");
    const invaderKilled = new Audio ("assets/sounds/invaderKilled.wav");
    const gameOver = new Audio ("assets/sounds/explosion.wav");
    const endLevel = new Audio ("assets/sounds/roundEnd.wav");
    

    let gameOverSoundPlayed = false;
    
    const levelsWithBombList = [[2, 10], [3, 9], [4, 11], [5, 8], [6, 12]];
    let levelsWithBomb = levelsWithBombList [Math.floor (Math.random () * levelsWithBombList.length)];

    function beep (freq) {
        const oscillator = audioCtx.createOscillator ();
        oscillator.connect (audioCtx.destination);
        
        oscillator.frequency.value = freq;
        oscillator.type = "sine";
        
        oscillator.start (audioCtx.currentTime);
        oscillator.stop (audioCtx.currentTime + 0.2);
    };

    function animateEndLevel () {
        if (typeof animateEndLevel.phase == "undefined")
            animateEndLevel.phase = 1;

        drawing.cls ();
        switch (animateEndLevel.phase) {
            case 1:
                drawing.text (110, 35, "Level completed...", "center", "top", "rgb(255,255,255)");
                animateEndLevel.phase = 2;
                break;
            case 2:
                animateEndLevel.bonus = 0;
                if (bonus > 0) {
                    drawing.text (110, 35, "Level completed...", "center", "top", "rgb(255,255,255)");
                    drawing.text (110, 45, "Bonus : ", "center", "top", "rgb(255,255,255)");
                    drawScore ();
                    animateEndLevel.phase = 3;        
                }
                else {
                    drawing.text (110, 35, "Level completed...", "center", "top", "rgb(255,255,255)");
                    drawing.text (110, 45, "No bonus...", "center", "top", "rgb(255,255,255)");
                    animateEndLevel.phase = 4;
                }
                break;
            case 3:
                if (bonus > 0) {
                    --bonus;
                    ++score;
                    ++animateEndLevel.bonus;
                    //beep (400 + animateEndLevel.bonus * 100);
                    drawing.text (110, 35, "Level completed...", "center", "top", "rgb(255,255,255)");
                    drawing.text (110, 45, "Bonus : " + animateEndLevel.bonus, "center", "top", "rgb(255,255,255)");
                    if (bonus == 0)
                        animateEndLevel.phase = 4;
                }
                break;
            case 4:
                drawing.text (110, 35, "Level completed...", "center", "top", "rgb(255,255,255)");
                if (animateEndLevel.bonus > 0)
                    drawing.text (110, 45, "Bonus : " + animateEndLevel.bonus, "center", "top", "rgb(255,255,255)");
                else
                    drawing.text (110, 45, "No bonus...", "center", "top", "rgb(255,255,255)");
                if (nbAliens <= 15) {
                    drawing.text (110, 55, "Next level in 3", "center", "top", "rgb(255,255,255)");
                    animateEndLevel.phase = 5;
                }
                else
                    drawing.text (110, 55, "Game finished, you are some dichotomic MASTER !", "center", "top", "rgb(255,255,255)");
                break;
            case 5:
                drawing.text (110, 35, "Level completed...", "center", "top", "rgb(255,255,255)");
                if (animateEndLevel.bonus > 0)
                    drawing.text (110, 45, "Bonus : " + animateEndLevel.bonus, "center", "top", "rgb(255,255,255)");
                else
                    drawing.text (110, 45, "No bonus...", "center", "top", "rgb(255,255,255)");
                drawing.text (110, 55, "Next level in 2", "center", "top", "rgb(255,255,255)");
                animateEndLevel.phase = 6;
                break;
            case 6:
                drawing.text (110, 35, "Level completed...", "center", "top", "rgb(255,255,255)");
                if (animateEndLevel.bonus > 0)
                    drawing.text (110, 45, "Bonus : " + animateEndLevel.bonus, "center", "top", "rgb(255,255,255)");
                else
                    drawing.text (110, 45, "No bonus...", "center", "top", "rgb(255,255,255)");
                drawing.text (110, 55, "Next level in 1", "center", "top", "rgb(255,255,255)");
                animateEndLevel.phase = 7;
                break;
            case 7:
                clearInterval (timer);
                animateEndLevel.phase = 1;
                newLevel ();
                break;
        }
        spaceShip.draw ();
        drawMunitions ();
        drawScore ();
    }

    function newGame () {
        spaceShip.isAlive = true;
        gameOverSoundPlayed = false;
        level = 0;
        score = 0;
        nbAliens = 6;
        nbKilled = 0;
        levelsWithBomb = levelsWithBombList [Math.floor (Math.random () * levelsWithBombList.length)];
        newLevel ();
    }

    function newLevel () {
        exploding = false;
        ++level;
        aliens.length = 0;
        let start = 3;
        let next = null;
        let values = buildValues (++nbAliens);
        const step = nbAliens <= 12 ? 20 - nbAliens : 4;

        bonus = 0;
        goalStart = 0;
        goalEnd = nbAliens - 1;
        goals = nbAliens % 2 == 0 ? [nbAliens >> 1, (nbAliens >> 1) - 1] : [(nbAliens - 1) >> 1];
        for (let i = 0; i < nbAliens; i++) {
            const alien = new Alien (start, 10, i % 10, null, step, values [i], spaceShip, drawing)
            if (next != null) {
                next.next = alien
            }
            next = alien
            aliens.push (alien);
            start += alien.width + step;
        }
        endOfLevel = false;
        munitions = Math.floor (Math.log2 (nbAliens)) + 2;
        let indiceCible = buildTarget (nbAliens);
        target = values [indiceCible];
        if (levelsWithBomb.includes (level))
            ++target;
        gameLoop ();
    }

    function initExplode () {
        endLevel.play ();
        exploding = true;
        for (let alien of aliens)
            alien.explode ();
        nbKilled = 0;
        setTimeout (() => {
            endOfLevel = true;
            bullet.firing = false;
            timer = setInterval (animateEndLevel, 1000)
        }, 4000);
    }

    function gameLoop (theTime) {
        if (endOfLevel)
            return
        if (paused) {
            requestAnimationFrame (gameLoop);
            return
        }
        if (!gameBegin && spaceShip.isAlive) {
            if (nbKilled == nbAliens)
                initExplode ()
            if (keys.isDown ("ArrowLeft"))
                spaceShip.left ()
            else if (keys.isDown ("ArrowRight"))
                spaceShip.right ()
            else
                spaceShip.stop ()
            if (keys.isDown ("Space") && munitions > 0 && !bullet.firing && bullet.countdown == 0) {
                fire.play ();
                bullet.firing = true;
                bullet.x = spaceShip.x + 6;
                bullet.y = spaceShip.y;
                --munitions;
            }
        }
        if (theTime - saveTime > 25) {
            saveTime = theTime;
            draw ();
        }
        requestAnimationFrame (gameLoop);
    }

    function drawMunitions () {
        for (let i = 0; i < munitions; i++)
        drawing.bar (drawing.width - 4 - i * 2, drawing.height - 8, 5, "#FFFFFF");
    }

    function drawScore () {
        drawing.text (drawing.width - 4, 4, score, "right", "top", "rgb(255,255,255)")
        drawing.text (4, 4, "★ ".repeat (bonus), "left", "top", "rgb(255,255,0)")
    }

    function max (a, b) {
        return a > b ? a : b;
    }

    function min (a, b) {
        return a < b ? a : b;
    }

    function draw () {
        drawing.cls ();
        drawMunitions ();
        drawScore ();
        if (target != null) {
            drawing.text (5, 90, target, "left", "top", "rgb(255,255,255)");
            drawing.text (22, 90, aliens [0].value <= aliens [1].value ?  "UP" : "DOWN", "left", "top", "rgb(255,255,255)");
        }
        if (bullet.firing) {
            bullet.update ();
            bullet.draw ();
            for (let [index, alien] of aliens.entries ()) {
                if (!alien.killed && bullet.y >= alien.y && bullet.y <= alien.y + 8 && bullet.x >= alien.x && bullet.x <= alien.x + alien.width) {
                    if (nbKilled < nbAliens)
                        invaderKilled.play ();
                    alien.touched ();
                    ++nbKilled;
                    ++score;
                    if (target != null) {
                        if (goals.includes (index))
                            ++bonus;
                        if (aliens [0].value <= aliens [1].value) {
                            if (target > alien.value)
                                goalStart = max (goalStart, index + 1);
                            else
                                goalEnd = min (goalEnd, index - 1);
                        }
                        else {
                            if (target < alien.value)
                                goalStart = max (goalStart, index + 1);
                            else
                                goalEnd = min (goalEnd, index - 1);
                        }
                        if (goalStart == goalEnd)
                            goals = [goalStart]
                        else {
                            const width = goalEnd - goalStart + 1;
                            goals = width % 2 == 0 ? [goalStart + (width >> 1), goalStart + (width >> 1) - 1] : [goalStart + (width >> 1)];
                        }
                    }
                    console.log (goalStart, goalEnd);
                    console.log (goals);
                    bullet.firing = false;
                    bullet.countdown = 10;
                    if (alien.value == target) {
                        munitions = nbAliens;
                        target = null;
                        goals = [];
                        for (let alien of aliens)
                            alien.speedOn = true;
                    }
                }
            }
        }
        else if (bullet.countdown > 0)
            --bullet.countdown;
        for (let alien of aliens) {
            alien.update ();
            if (!alien.killed && alien.y == 90 && alien.x <= spaceShip.x + spaceShip.width)
                spaceShip.isAlive = false;
            const hasard = target != null ? Math.random () < 0.002 : Math.random () < 0.05; 
            if (!alien.firing && !alien.killed && hasard)
                alien.fire ();
            alien.draw ();
        }
        for (let b of bombs) {
            b.draw ()
        }
        if (gameBegin) {
            drawing.text (110, 35, "*** SPACE INVADERS ***", "center", "top", "rgb(255,0,0)");
            drawing.text (110, 45, "Press N to play", "center", "top", "rgb(255,255,255)");
        }
        else if (!spaceShip.isAlive) {
            if (!gameOverSoundPlayed) {
                gameOver.play ();
                gameOverSoundPlayed = true;
            }
            drawing.text (110, 35, "GAME OVER", "center", "top", "rgb(255,0,0)");
            drawing.text (110, 45, "Press N for new game", "center", "top", "rgb(255,255,255)");
        }
        if (spaceShip.isAlive)
            spaceShip.update ();
        spaceShip.draw ();
    }

    function buildValues (n) {
        let res = [];
        let croissant = level <= 2 || Math.random () < 0.5 ? true : false;
        let val = Math.floor (Math.random () * 20) + 10;

        for (let i = 0; i < n; i++) {
            res.push (val);
            val += Math.floor (Math.random () * 10) + 3;
        }
        return croissant ? (res.sort ((a, b) => a - b)) : (res.sort ((a, b) => a - b)).reverse ();
    }

    function buildTarget (n) {
        let start = 0, end = n - 1;

        while (start < end) {
            const middle = Math.floor ((start + end) / 2);
            if (Math.random () < 0.5)
                start = middle + 1
            else
                end = middle - 1
        }
        return start
    }

    const spaceShip = new SpaceShip (104, 90, "#FFFFFF", drawing);
    const bullet = new Bullet (drawing, "#FFFFFF");
    const keys = new Keys ();
    const aliens = [];

    newLevel ();

    gameLoop ();

    document.getElementById ("container").focus ();
    document.getElementById ("container").addEventListener ("keypress", (evt) => {
        if (exploding)
            return;
        if (evt.code == "KeyP")
            paused = !paused;
        if (!gameBegin && evt.code == "KeyB") {
            if (levelsWithBomb.includes (level))
                initExplode ();
            else
                spaceShip.isAlive = false;
        }
        if ((gameBegin || !spaceShip.isAlive) && evt.code == "KeyN") {
            // if (audioCtx == undefined)
            //     audioCtx = new (window.AudioContext || window.webkitAudioContext || window.audioContext);
            gameBegin = false;
            newGame ();
        }
    });
 
    document.getElementById ("container").addEventListener ("keydown", (evt) => {
        if (evt.code == "Space")
            evt.preventDefault ();
        keys.onKeyDown (evt.code)
    });
    document.getElementById ("container").addEventListener ("keyup", (evt) => {
        keys.onKeyUp (evt.code)
    })

}