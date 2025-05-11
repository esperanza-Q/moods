document.getElementById("confirmBtn").addEventListener("click", () => {
  const checkedTags = [...document.querySelectorAll('.tag:checked')].map(tag => tag.value);
  if (checkedTags.length > 0) {
    const queryString = checkedTags.map(tag => `tag=${encodeURIComponent(tag)}`).join("&");
    window.location.href = `search_after.html?${queryString}`;
  } else {
    alert("태그를 하나 이상 선택해주세요.");
  }
});
