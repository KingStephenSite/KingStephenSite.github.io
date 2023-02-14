function generateHeart() {
    const heart = document.createElement('div')
    heart.innerText = "❤️";
    heart.style.left = math.random() * 100 + 'vw';
    heart.style.animationDuration = math.random * 5 + 6 + 's';
    heart.classList.add('heart');
    document.body.appendChild(heart)
}

setInterval(generateHeart, 100);