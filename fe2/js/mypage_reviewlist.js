const mockReviewList = [
  {
    id: 1,
    review: "혼자 작업하기 좋았어요!",
    cafeName: "블루보틀",
    comment: "콘센트 많음",
    address: "서울 강남구"
  },
  {
    id: 2,
    review: "디저트가 맛있었어요.",
    cafeName: "카페드파리",
    comment: "딸기 케이크 추천",
    address: "서울 마포구"
  },
  {
    id: 3,
    review: "조용하고 분위기 좋음",
    cafeName: "빈브라더스",
    comment: "공부하기 좋아요",
    address: "서울 종로구"
  },
  {
    id: 4,
    review: "조용하고 분위기 좋음",
    cafeName: "빈브라더스",
    comment: "공부하기 좋아요",
    address: "서울 종로구"
  }
  ,
  {
    id: 5,
    review: "조용하고 분위기 좋음",
    cafeName: "빈브라더스",
    comment: "공부하기 좋아요",
    address: "서울 종로구"
  },
  {
    id: 6,
    review: "조용하고 분위기 좋음",
    cafeName: "빈브라더스",
    comment: "공부하기 좋아요",
    address: "서울 종로구"
  }
  
];

const container = document.getElementById("reviewListContainer");

function renderReviews() {
  container.innerHTML = ""; // 초기화

  mockReviewList.forEach((reviewData) => {
    const div = document.createElement("div");
    div.className = "reviewmaincontainer1";
    div.innerHTML = `
      <div class="reviewmain">
        <div class="reviewleft">${reviewData.review}</div>
        <div class="reviewright">
          <div class="myreviewimg"></div>
          <div class="myreviewmain">
            <div class="myreviewname">${reviewData.cafeName}</div>
            <div class="myreviewcomment">${reviewData.comment}</div>
            <div class="myreviewaddress">${reviewData.address}</div>
          </div>
        </div>
        <button class="deletebutton" data-id="${reviewData.id}">Delete</button>
      </div>
      <hr class="reviewbottomline">
    `;
    container.appendChild(div);
  });

  // Delete 버튼 이벤트 연결 누르면 삭제됨
  const deleteButtons = document.querySelectorAll(".deletebutton");
  deleteButtons.forEach((button) => {
    button.addEventListener("click", (e) => {
      const id = parseInt(e.target.getAttribute("data-id"));
      // 리스트에서 제거
      const index = mockReviewList.findIndex(r => r.id === id);
      if (index !== -1) {
        mockReviewList.splice(index, 1); // 데이터 제거
        renderReviews(); // 다시 렌더링
      }
    });
  });
}

// 초기 렌더링
renderReviews();
