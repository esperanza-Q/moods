function openModal() {
    document.getElementById("profilechangeModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("profilechangeModal").style.display = "none";
    const preview = document.getElementById("preview-profile_image");
    const plusIcon = document.getElementById("plus-icon");
    const fileInput = document.getElementById("profile_image_update");

    preview.src = "#";
    preview.style.display = "none";
    plusIcon.style.display = "block";
    fileInput.value = "";  // 파일 선택도 초기화
}

window.onclick = function(event) {
    let modal = document.getElementById("profilechangeModal");
    if (event.target === modal) {
        closeModal();
    }
};