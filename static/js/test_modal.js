// 모달 열기 버튼과 닫기 버튼
const modal = document.getElementById("reviewModal");
const btn = document.querySelector(".review_btn");
const span = document.querySelector(".close");

// 버튼 클릭 시 모달 열기
btn.onclick = function() {
    modal.style.display = "block";  // 모달 보이기
}

// 닫기 버튼 클릭 시 모달 닫기
span.onclick = function() {
    modal.style.display = "none";  // 모달 숨기기
}

// 모달 외부 클릭 시 닫기
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";  // 모달 숨기기
    }
}