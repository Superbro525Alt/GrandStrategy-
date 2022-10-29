mainQuit = document.getElementById("mainQuit");
quitMenu = document.getElementById("quitMenu");
mainQuit.addEventListener("click", function() {
    if (quitMenu.style.display == "none") {
        quitMenu.style.display = "block";
    } else {
        quitMenu.style.display = "none";
    }
});