function openModal() {
    document.getElementById("reviewModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("reviewModal").style.display = "none";
}

window.onclick = function(event) {
    let modal = document.getElementById("reviewModal");
    if (event.target === modal) {
        closeModal();
    }
};
