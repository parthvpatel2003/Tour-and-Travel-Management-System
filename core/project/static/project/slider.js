document.addEventListener('DOMContentLoaded', () => {
    const slides = document.querySelector('.slides');
    let index = 0;

    const timings = [3000, 6000, 3000]; // time for each slide

    function showSlide() {
        slides.style.transform = `translateX(-${index * 100}%)`;

        setTimeout(() => {
            index = (index + 1) % 3;
            showSlide();
        }, timings[index]);
    }

    showSlide();
});
