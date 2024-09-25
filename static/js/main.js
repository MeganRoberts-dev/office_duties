// Array of motivational quotes
var quotes = [
    "Believe in yourself and all that you are.",
    "The only way to achieve the impossible is to believe it is possible.",
    "Success is not the key to happiness. Happiness is the key to success.",
    "Don't watch the clock; do what it does. Keep going.",
    "You are never too old to set another goal or to dream a new dream.",
    "Start where you are. Use what you have. Do what you can."
];

function changeTitle() {
    var randomIndex = Math.floor(Math.random() * quotes.length);
    titleElement.textContent = quotes[randomIndex];
}

// Change the title every 5 seconds
var titleElement = document.querySelector('#motivational-header');
if (titleElement) {
    setInterval(changeTitle, 5000);
    changeTitle();
}

function toggleIcon(label) {
    const checkbox = label.previousElementSibling; // Get the checkbox
    checkbox.checked = !checkbox.checked; // Toggle checked state
    // Optionally, update the icon's class based on the checkbox state
    if (checkbox.checked) {
        label.innerHTML = '<i class="bi bi-check-circle-fill check-icon"></i>';
    } else {
        label.innerHTML = '<i class="bi bi-circle check-icon"></i>';
    }
}
document.addEventListener('DOMContentLoaded', function () {
    setTimeout(function () {
        let flashMessage = document.querySelector('.flash-banner');
        if (flashMessage) {
            flashMessage.style.transition = "opacity 0.5s ease-out";
            flashMessage.style.opacity = 0; // Fade out effect
            setTimeout(() => flashMessage.remove(), 500); // Remove after fade-out
        }
    }, 2000); // 2 seconds
});
