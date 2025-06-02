function login() {
    let id = document.querySelector('#id-input').value;
    let pw = document.querySelector('#pw-input').value;

    if (id && pw) {
        location.href = 'home.html';
    } else {
        alert('아이디와 비밀번호를 입력하세요.');
    }
}