function openModal() {
    document.getElementById("profilechangeModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("profilechangeModal").style.display = "none";
}

window.onclick = function(event) {
    let modal = document.getElementById("profilechangeModal");
    if (event.target === modal) {
        closeModal();
    }
};