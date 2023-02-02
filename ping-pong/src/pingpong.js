/*jslint browser*/
/*global window*/
function Game() {
    'use strict';

    var canvas = document.getElementById('game_loop'),
        screen = canvas.getContext('2d'),
        debugMode = false,
        debugLines = false;

    function Keyboarder() {
        var that = this,
            pressed = {},
            KEY = {
                W: 87,
                S: 83,
                I: 73,
                J: 74,
                G: 71
            },
            listeners = {};

        window.addEventListener('keydown', function (e) {
            var keyCode = e.keyCode;
            pressed[keyCode] = true;

            if (listeners[keyCode]) {
                listeners[keyCode]();
            }
        });
        window.addEventListener('keyup', function (e) {
            var keyCode = e.keyCode;
            pressed[keyCode] = false;
        });

        that.onPress = function (keyCode, fun) {
            listeners[keyCode] = fun;
        };
        that.isPressed = function (keyCode) {
            return pressed[keyCode];
        };
        that.KEY = KEY;

        return that;
    }

    function Player(gameSize, xPercGameSize, yPercGameSize, up, down, keyboarder, livesXPerc) {
        var that = this,
            velocity = 0.5,
            center = {
                x: gameSize.x * xPercGameSize,
                y: gameSize.y * yPercGameSize
            },
            height = 60,
            width = 5,
            lost = false,
            ball,
            maxLives = 11,
            lives = maxLives,
            livesX = gameSize.x * livesXPerc;

        function goUpOrDown(timestep) {
            if (!debugMode) {
                if (keyboarder.isPressed(keyboarder.KEY[up])) {
                    center.y -= velocity * timestep;
                }

                if (keyboarder.isPressed(keyboarder.KEY[down])) {
                    center.y += velocity * timestep;
                }
            } else {
                center.y = ball.centerY();
            }
            center.y = Math.max(center.y, height / 2);
            center.y = Math.min(center.y, gameSize.y - height / 2);
        }

        that.upKey = up;
        that.downKey = down;
        that.height = function () {
            return height;
        };
        that.width = function () {
            return width;
        };
        that.leftX = function () {
            return center.x - width / 2;
        };
        that.rightX = function () {
            return center.x + width / 2;
        };
        that.topY = function () {
            return center.y - height / 2;
        };
        that.bottomY = function () {
            return center.y + height / 2;
        };
        that.flagLost = function () {
            lost = true;
            lives -= 1;
        };
        that.unflagLost = function () {
            lost = false;
        };
        that.lost = function () {
            return lost;
        };
        that.playWith = function (ball0) {
            ball = ball0;
        };
        that.lives = function () {
            return lives;
        };
        that.resetLives = function () {
            lives = maxLives;
        };
        that.update = function (timestep) {
            goUpOrDown(timestep);
        };
        that.draw = function () {
            var l,
                i;

            screen.save();
            screen.fillRect(that.leftX(), that.topY(), width, height);
            screen.restore();

            screen.save();
            for (i = 0; i < lives; i += 1) {
                screen.fillStyle = 'lightgreen';
                screen.fillRect(livesX - 3, parseInt(0.05 * gameSize.y + i * 0.98 * gameSize.y / maxLives, 10), 4, 4);
                screen.fill();
            }
            screen.restore();

            if (debugMode && debugLines) {
                l = [
                    {x1: that.leftX(), y1: 0, x2: that.leftX(), y2: gameSize.y},
                    {x1: that.rightX(), y1: 0, x2: that.rightX(), y2: gameSize.y},
                    {x1: 0, y1: that.topY(), x2: gameSize.x, y2: that.topY()},
                    {x1: 0, y1: that.bottomY(), x2: gameSize.x, y2: that.bottomY()}
                ];
                for (i = 0; i < l.length; i += 1) {
                    screen.save();
                    screen.strokeStyle = 'yellow';
                    screen.beginPath();
                    screen.moveTo(l[i].x1, l[i].y1);
                    screen.lineTo(l[i].x2, l[i].y2);
                    screen.stroke();
                    screen.restore();
                }
            }
        };
        that.draw();

        return that;
    }

    function LeftPlayer(gameSize, keyboarder) {
        var that = new Player(gameSize, 0.1, 0.5, 'W', 'S', keyboarder, 0.02);
        return that;
    }

    function RightPlayer(gameSize, keyboarder) {
        var that = new Player(gameSize, 0.9, 0.5, 'I', 'J', keyboarder, 0.98);
        return that;
    }

    function Ball(gameSize, leftPlayer, rightPlayer, speaker) {
        var that = this,
            center = {},
            ballVelocity = 0.3,
            velocity = {},
            radius = 6,
            respawn = false,
            showCollision = 0,
            collisionPoint = {
                x: 0,
                y: 0
            };

        function doRespawn() {
            center = {
                x: gameSize.x / 2,
                y: gameSize.y / 2
            };
            velocity = {
                x: Math.random() > 0.5
                    ? 1.3 * ballVelocity
                    : -1.3 * ballVelocity,
                y: Math.random() > 0.5
                    ? 0.5 * ballVelocity
                    : -0.5 * ballVelocity
            };

            if (leftPlayer.lost() && velocity.x < 0) {
                velocity.x *= -1;
            }

            if (rightPlayer.lost() && velocity.x > 0) {
                velocity.x *= -1;
            }

            leftPlayer.unflagLost();
            rightPlayer.unflagLost();
            respawn = false;
        }
        function leftX() {
            return center.x - radius;
        }
        function rightX() {
            return center.x + radius;
        }
        function topY() {
            return center.y - radius;
        }
        function bottomY() {
            return center.y + radius;
        }
        function prepareToCollide(cpx) {
            velocity.x *= -1;
            collisionPoint.x = cpx;
            collisionPoint.y = center.y;
            showCollision = 3;
            speaker.playRandHit();
            velocity.y += (2 * Math.random() - 1) / 7;
        }
        function checkLeftPlayerCollision() {
            if (leftX() < leftPlayer.rightX()) {
                if (bottomY() > leftPlayer.topY()
                        && topY() < leftPlayer.bottomY()) {
                    if (!respawn) {
                        prepareToCollide(leftX());
                    }
                } else {
                    if (!respawn) {
                        leftPlayer.flagLost();
                    }
                    respawn = true;
                }
            }
        }
        function checkRightPlayerCollision() {
            if (rightX() > rightPlayer.leftX()) {
                if (bottomY() > rightPlayer.topY()
                        && topY() < rightPlayer.bottomY()) {
                    if (!respawn) {
                        prepareToCollide(rightX());
                    }
                } else {
                    if (!respawn) {
                        rightPlayer.flagLost();
                    }
                    respawn = true;
                }
            }
        }

        that.centerY = function () {
            return center.y;
        };
        that.update = function (timestep) {
            if (topY() <= 0 || bottomY() >= gameSize.y) {
                velocity.y *= -1;
            }

            checkLeftPlayerCollision();
            checkRightPlayerCollision();

            if (respawn) {
                if (leftX() < 0 || rightX() > gameSize.x) {
                    doRespawn();
                }
            }

            showCollision = Math.max(0, showCollision - 1);
            center.x = center.x + velocity.x * timestep;
            center.y = center.y + velocity.y * timestep;
            velocity.x = Math.min(1.8 * ballVelocity, 1.0005 * velocity.x);
            collisionPoint.y = center.y;
        };
        that.draw = function () {
            var l,
                i;

            screen.save();
            screen.fillStyle = 'red';
            screen.beginPath();
            screen.arc(center.x, center.y, radius, 0, 2 * Math.PI);
            screen.fill();
            screen.restore();

            if (showCollision) {
                screen.save();
                screen.fillStyle = 'green';
                screen.beginPath();
                screen.arc(collisionPoint.x, collisionPoint.y, 10, 0, 2 * Math.PI);
                screen.fill();
                screen.restore();
            }

            if (debugMode && debugLines) {
                l = [
                    {x1: leftX(), y1: 0, x2: leftX(), y2: gameSize.y},
                    {x1: rightX(), y1: 0, x2: rightX(), y2: gameSize.y},
                    {x1: 0, y1: topY(), x2: gameSize.x, y2: topY()},
                    {x1: 0, y1: bottomY(), x2: gameSize.x, y2: bottomY()}
                ];
                for (i = 0; i < l.length; i += 1) {
                    screen.save();
                    screen.strokeStyle = 'green';
                    screen.beginPath();
                    screen.moveTo(l[i].x1, l[i].y1);
                    screen.lineTo(l[i].x2, l[i].y2);
                    screen.stroke();
                    screen.restore();
                }
            }
        };
        doRespawn();

        return that;
    }

    function Speaker() {
        var that = this,
            hit = ['sounds/hit_1.wav', 'sounds/hit_2.wav', 'sounds/hit_3.wav'],
            gameOver = 'sounds/game_over.wav';

        that.playRandHit = function () {
            var audio = new Audio(hit[parseInt(hit.length * Math.random() - 0.1)]);
            audio.volume = 0.5;
            return audio.play();
        };
        that.playGameOver = function () {
            return new Audio(gameOver).play();
        };
        return that;
    }

    (function () {
        var that = this,
            k = {
                TIME_STEP: 1000 / 60
            },
            delta = 0,
            lastMs = 0,
            gameSize = {
                x: canvas.width,
                y: canvas.height
            },
            keyboarder = new Keyboarder(),
            leftPlayer = new LeftPlayer(gameSize, keyboarder),
            rightPlayer = new RightPlayer(gameSize, keyboarder),
            speaker = new Speaker(),
            ball = new Ball(gameSize, leftPlayer, rightPlayer, speaker),
            elements = [leftPlayer, rightPlayer, ball],
            started = false,
            over = true,
            startMs = 0;

        leftPlayer.playWith(ball);
        rightPlayer.playWith(ball);

        function screenClear() {
            screen.clearRect(0, 0, gameSize.x, gameSize.y);
        }
        function help() {
            screen.save();
            screen.font = '13px PT Mono';
            screen.fillStyle = 'black';
            screen.textAlign = 'center';
            screen.fillText('Welcome to a table tennis 2d HTML5 canvas (+ sound) demo', gameSize.x / 2, gameSize.y / 2 - 50);
            screen.fillText('Use keys \'W\' and \'S\' to move the left player up and down', gameSize.x / 2, gameSize.y / 2 - 17);
            screen.fillText('Use keys \'I\' and \'J\' to move the right player up and down', gameSize.x / 2, gameSize.y / 2 + 17);
            screen.fillText('Start the game now by pressing key \'G\'', gameSize.x / 2, gameSize.y / 2 + 50);
            screen.restore();
        }
        function handleGameOver() {
            screen.font = '30px PT Mono';
            screen.fillStyle = 'black';
            screen.textAlign = 'center';
            screen.fillText('Game Over', gameSize.x / 2, gameSize.y / 2);
            setTimeout(function () {
                var i;

                screenClear();

                for (i = 0; i < elements.length; i += 1) {
                    elements[i].draw();
                    if (elements[i].resetLives !== undefined) {
                        elements[i].resetLives();
                    }
                }

                help();
            }, 7500);
        }
        function update(timestep) {
            var i;

            for (i = 0; i < elements.length; i += 1) {
                elements[i].update(timestep);
                if (elements[i].lives !== undefined && elements[i].lives() < 0) {
                    over = true;
                    speaker.playGameOver();
                }
            }
        }
        function draw() {
            var i;

            screenClear();
            for (i = 0; i < elements.length; i += 1) {
                elements[i].draw();
            }
        }
        function tick(nowMs0) {
            var nowMs;

            if (!started) {
                startMs = nowMs0;
                started = true;
            }

            nowMs = nowMs0 - startMs;

            if (nowMs - lastMs > k.TIME_STEP) {
                delta += nowMs - lastMs;

                while (delta >= k.TIME_STEP) {
                    update(k.TIME_STEP);
                    delta -= k.TIME_STEP;
                }
                draw();
            }
            lastMs = nowMs;

            if (!over) {
                window.requestAnimationFrame(tick);
            } else {
                handleGameOver();
            }
        }
        keyboarder.onPress(keyboarder.KEY.G, function () {
            if (over) {
                started = false;
                over = false;
                window.requestAnimationFrame(tick);
            }
        });
        help();

        console.log('You found this! Congratulations...');
        console.log('Find me (and more projects of mine) on GitHub at https://github.com/paulo-ferraz-oliveira');
        return that;
    }());
}

window.addEventListener('load', Game);