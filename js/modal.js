// 요소 가져오기
const modal = document.getElementById("modal");
const openModalBtn = document.querySelector(".open-modal-btn");
const closeModalBtn = document.querySelector(".close-btn");

// 모달 열기
openModalBtn.addEventListener("click", () => {
    modal.style.display = "block";
});

// 모달 닫기 (X 버튼)
closeModalBtn.addEventListener("click", () => {
    modal.style.display = "none";
});

// 모달창 외부 클릭 시 닫기
window.addEventListener("click", (event) => {
    if (event.target === modal) {
        modal.style.display = "none";
    }
});
