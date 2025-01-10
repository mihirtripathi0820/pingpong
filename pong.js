const canvas = document.getElementById("pongCanvas");
const ctx = canvas.getContext("2d");

// Create the paddles
const paddleWidth = 10, paddleHeight = 100;
let leftPaddleY = canvas.height / 2 - paddleHeight / 2, rightPaddleY = canvas.height / 2 - paddleHeight / 2;

// Ball properties
let ballRadius = 10;
let ballX = canvas.width / 2, ballY = canvas.height / 2;
let ballSpeedX = 4, ballSpeedY = 4;

// Player scores
let playerAScore = 0, playerBScore = 0;

// Control paddles using keys
let leftPaddleUp = false, leftPaddleDown = false, rightPaddleUp = false, rightPaddleDown = false;

document.addEventListener("keydown", (e) => {
    if (e.key === "w") leftPaddleUp = true;
    if (e.key === "s") leftPaddleDown = true;
    if (e.key === "ArrowUp") rightPaddleUp = true;
    if (e.key === "ArrowDown") rightPaddleDown = true;
});

document.addEventListener("keyup", (e) => {
    if (e.key === "w") leftPaddleUp = false;
    if (e.key === "s") leftPaddleDown = false;
    if (e.key === "ArrowUp") rightPaddleUp = false;
    if (e.key === "ArrowDown") rightPaddleDown = false;
});

// Draw the paddles
function drawPaddles() {
    ctx.fillStyle = "white";
    ctx.fillRect(0, leftPaddleY, paddleWidth, paddleHeight);  // Left paddle
    ctx.fillRect(canvas.width - paddleWidth, rightPaddleY, paddleWidth, paddleHeight);  // Right paddle
}

// Draw the ball
function drawBall() {
    ctx.beginPath();
    ctx.arc(ballX, ballY, ballRadius, 0, Math.PI * 2);
    ctx.fillStyle = "red";
    ctx.fill();
    ctx.closePath();
}

// Draw the scores
function drawScores() {
    ctx.font = "24px Arial";
    ctx.fillText(`Player A: ${playerAScore}`, canvas.width / 4, 30);
    ctx.fillText(`Player B: ${playerBScore}`, (canvas.width / 4) * 3, 30);
}

// Move the paddles
function movePaddles() {
    if (leftPaddleUp && leftPaddleY > 0) leftPaddleY -= 5;
    if (leftPaddleDown && leftPaddleY < canvas.height - paddleHeight) leftPaddleY += 5;
    if (rightPaddleUp && rightPaddleY > 0) rightPaddleY -= 5;
    if (rightPaddleDown && rightPaddleY < canvas.height - paddleHeight) rightPaddleY += 5;
}

// Move the ball
function moveBall() {
    ballX += ballSpeedX;
    ballY += ballSpeedY;

    // Ball collisions with top and bottom
    if (ballY - ballRadius < 0 || ballY + ballRadius > canvas.height) {
        ballSpeedY = -ballSpeedY;
    }

    // Ball collisions with paddles
    if (ballX - ballRadius < paddleWidth && ballY > leftPaddleY && ballY < leftPaddleY + paddleHeight) {
        ballSpeedX = -ballSpeedX;
    }

    if (ballX + ballRadius > canvas.width - paddleWidth && ballY > rightPaddleY && ballY < rightPaddleY + paddleHeight) {
        ballSpeedX = -ballSpeedX;
    }

    // Ball out of bounds (scoring)
    if (ballX - ballRadius < 0) {
        playerBScore++;
        resetBall();
    }

    if (ballX + ballRadius > canvas.width) {
        playerAScore++;
        resetBall();
    }
}

// Reset the ball to the center
function resetBall() {
    ballX = canvas.width / 2;
    ballY = canvas.height / 2;
    ballSpeedX = -ballSpeedX;
    ballSpeedY = 4 * (Math.random() < 0.5 ? 1 : -1);
}

// Main game loop
function gameLoop() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    drawPaddles();
    drawBall();
    drawScores();

    movePaddles();
    moveBall();

    requestAnimationFrame(gameLoop);
}

// Start the game loop
gameLoop();
