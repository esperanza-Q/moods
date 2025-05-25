const CafeList = [
  {
    name: "스타벅스",
    comment: "깔끔하고 쾌적해요",
    address: "서울 강남구",
  },
  {
    name: "할리스",
    comment: "조용한 분위기 좋아요",
    address: "서울 마포구",
  },
  {
    name: "이디야",
    comment: "커피가 맛있음",
    address: "서울 동작구",
  },
   {
    name: "아마스빈",
    comment: "가성비펄",
    address: "서울 성북구",
  }
  ,
  {
    name: "이디야",
    comment: "커피가 맛있음",
    address: "서울 동작구",
  },
   {
    name: "아마스빈",
    comment: "가성비펄",
    address: "서울 성북구",
  }
];

const container = document.getElementById('cafeListContainer');

CafeList.forEach(cafe => {
  const div = document.createElement('div');
  div.className = 'maincafesearchlist';

  div.innerHTML = `
    <a href="select_detail.html?name=${encodeURIComponent(cafe.name)}" class="selectcafelink">
      <div class="maincafesearch">
        <div class="maincafesearchimg" src="${cafe.imageUrl || '../default.jpg'}">
        </div>
        <div class="maincafesearchtext">
          <div class="maincafesearchname">${cafe.name}</div>
          <div class="maincafesearchcomment">${cafe.comment}</div>
          <div class="maincafesearchaddress">${cafe.address}</div>
        </div>
      </div>
    </a>
    <hr class="selectafterbottomline" />
  `;

  container.appendChild(div);
});

