document.addEventListener("DOMContentLoaded", () => {
    const cartIcon = document.querySelector(".home4");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                cartIcon.classList.add("visible");
            } else {
                cartIcon.classList.remove("visible");
            }
        });
    });

    observer.observe(cartIcon);
});

document.addEventListener("DOMContentLoaded", () => {
    const cartIcon = document.querySelector(".home5");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                cartIcon.classList.add("visible");
            } else {
                cartIcon.classList.remove("visible");
            }
        });
    });

    observer.observe(cartIcon);
});

document.addEventListener("DOMContentLoaded", () => {
    const cartIcon = document.querySelector(".icon");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                cartIcon.classList.add("visible");
            } else {
                cartIcon.classList.remove("visible");
            }
        });
    });

    observer.observe(cartIcon);
});

document.addEventListener("DOMContentLoaded", () => {
    const cartIcon = document.querySelector(".vs-icon");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                cartIcon.classList.add("visible");
            } else {
                cartIcon.classList.remove("visible");
            }
        });
    });

    observer.observe(cartIcon);
});

document.addEventListener("DOMContentLoaded", () => {
    const cartIcon = document.querySelector(".share-icon");

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                cartIcon.classList.add("visible");
            } else {
                cartIcon.classList.remove("visible");
            }
        });
    });

    observer.observe(cartIcon);
});



document.addEventListener("DOMContentLoaded", function () {
    const container = document.querySelector(".scrollpromo");
    const pages = document.querySelectorAll(".promo");
    let currentPage = 0;
    const intervalTime = 3000;

    function scrollToNextPage() {
        currentPage++;
        if (currentPage >= pages.length) {
            currentPage = 0;
        }
        container.scrollTo({
            left: container.clientWidth * currentPage,
            behavior: "smooth"
        });
    }

    setInterval(scrollToNextPage, intervalTime);
});
