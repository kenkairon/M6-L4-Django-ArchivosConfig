// static/js/main.js
document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("theme-toggle");
    const body = document.body;

    // Cargar tema guardado en localStorage
    const savedTheme = localStorage.getItem("theme");
    if (savedTheme) {
        body.className = savedTheme;
    }

    toggleButton.addEventListener("click", function () {
        // Alternar entre los modos claro y oscuro
        if (body.classList.contains("dark-mode")) {
            body.classList.remove("dark-mode");
            body.classList.add("light-mode");
            localStorage.setItem("theme", "light-mode");
        } else {
            body.classList.remove("light-mode");
            body.classList.add("dark-mode");
            localStorage.setItem("theme", "dark-mode");
        }
    });
});