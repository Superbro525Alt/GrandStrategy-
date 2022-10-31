mainQuit = document.getElementById("mainQuit");
quitMenu = document.getElementById("quitMenu");
quitYes = document.getElementById("quitYes");
quitNo = document.getElementById("quitNo");
mainQuit.addEventListener("click", function() {
    if (quitMenu.style.display == "none") {
        quitMenu.style.display = "block";
    } else {
        quitMenu.style.display = "none";
    }
});
quitYes.addEventListener("click", function() {
    window.close();
});
quitNo.addEventListener("click", function() {
    quitMenu.style.display = "none";
});