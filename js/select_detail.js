document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.getElementById('reviewImageInput');
    const previewDiv = document.getElementById('reviewImagePreview');

    if (imageInput) {
        imageInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            previewDiv.innerHTML = '';
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const img = document.createElement('img');
                    img.src = e.target.result;
                    img.style.maxWidth = '250px';
                    img.style.maxHeight = '250px';
                    img.style.borderRadius = '8px';
                    previewDiv.appendChild(img);
                };
                reader.readAsDataURL(file);
            }
        });
    }

    const reviewForm = document.getElementById('reviewForm');
    if (reviewForm) {
        reviewForm.addEventListener('submit', function(e) {
            e.preventDefault();
            alert('리뷰 제출 완료');
            closeModal();
            reviewForm.reset();
            document.getElementById('reviewImagePreview').innerHTML = '';
        });
    }
});

function openModal() {
    document.getElementById("reviewModal").style.display = "flex";
}

function closeModal() {
    document.getElementById("reviewModal").style.display = "none";
}

window.onclick = function(event) {
    let modal = document.getElementById("reviewModal");
    if (event.target === modal) {
        closeModal();
    }
};
