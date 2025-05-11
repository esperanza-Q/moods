// search_after.js
document.addEventListener('DOMContentLoaded', function () {
    const cafeBoxes = document.querySelectorAll('.cafe-box');

    cafeBoxes.forEach(box => {
        box.addEventListener('click', () => {
            const cafeId = box.getAttribute('data-id');
            window.location.href = `/search_detail/${cafeId}/`;  // 또는 URL에 맞게 수정
        });
    });
});
