document.addEventListener("DOMContentLoaded", () => {
    const likeButtons = document.querySelectorAll(".like-btn");

    likeButtons.forEach(btn => {
        btn.addEventListener("click", () => {
            let count = btn.querySelector("span");
            count.textContent = parseInt(count.textContent) + 1;
            btn.style.background = "#d32f2f";
        });
    });
});
