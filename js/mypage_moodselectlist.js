const mockMoodList = [
  {
    id: 1,
    review: "혼자 작업하기 좋았어요!",
    name: "블루보틀",
    comment: "콘센트 많음",
    address: "서울 강남구"
  },
  {
    id: 2,
    review: "디저트가 맛있었어요.",
    name: "카페드파리",
    comment: "딸기 케이크 추천",
    address: "서울 마포구"
  },
  {
    id: 3,
    review: "조용하고 분위기 좋음",
    name: "빈브라더스",
    comment: "공부하기 좋아요",
    address: "서울 종로구"
  },
  {
    id: 4,
    review: "조용하고 분위기 좋음",
    name: "빈브라더스",
    comment: "공부하기 좋아요",
    address: "서울 종로구"
  }
  ,
  {
    id: 5,
    review: "조용하고 분위기 좋음",
    name: "빈브라더스",
    comment: "공부하기 좋아요",
    address: "서울 종로구"
  },
  {
    id: 6,
    review: "조용하고 분위기 좋음",
    name: "빈브라더스",
    comment: "공부하기 좋아요",
    address: "서울 종로구"
  }
  
];

const container = document.getElementById("moodListContainer");

function renderReviews() {
  container.innerHTML = ""; // 초기화

  mockMoodList.forEach((moodData) => {
    const div = document.createElement("div");
    div.className = "moodmaincontainer1";
    div.innerHTML = `
    <div class="mypmoodselectmain">
      <div class="mypmoodselectimg"></div>
      <div class="mypmoodselecttext">
          <div class="mypmoodselectname1">${moodData.name}</div>
          <div class="mypmoodselectcomment1">${moodData.comment}</div>
          <div class="mypmoodselectaddress1">${moodData.address}</div>
      </div>
  </div>
  <hr class="moodselectbottomline"></hr>
    `;
    container.appendChild(div);
  });
}

// 초기 렌더링
renderReviews();
