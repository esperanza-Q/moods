function openModal() {
    document.getElementById("reviewModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("reviewModal").style.display = "none";
    const preview = document.getElementById("preview-image");
    const plusIcon = document.getElementById("plus-icon");
    const fileInput = document.getElementById("review_image");

    preview.src = "#";
    preview.style.display = "none";
    plusIcon.style.display = "block";
    fileInput.value = "";  // 파일 선택도 초기화
}

window.onclick = function(event) {
    let modal = document.getElementById("reviewModal");
    if (event.target === modal) {
        closeModal();
    }
};
