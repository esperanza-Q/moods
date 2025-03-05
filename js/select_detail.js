// 모달 열기
function openModal() {
    document.getElementById("reviewModal").style.display = "flex";
}

// 모달 닫기
function closeModal() {
    document.getElementById("reviewModal").style.display = "none";
}

// 배경 클릭 시 모달 닫기
window.onclick = function(event) {
    let modal = document.getElementById("reviewModal");
    if (event.target === modal) {
        closeModal();
    }
};
