'use strict';

document.addEventListener('DOMContentLoaded', function () {
    /* =====================================================
        HERO SLIDER
    ===================================================== */
    var heroSlider = new Swiper('.hero-slider', {
        slidesPerView: 1,
        spaceBetween: 0,
        loop: true,
        effect: 'fade',
        autoplay: {
            delay: 4000,
        },
        pagination: {
            el: '.swiper-pagination',
            type: 'bullets',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
    });

    /* =====================================================
        TESTIMONIALS SLIDER
    ===================================================== */
    var testimonialsSlider = new Swiper('.testimonials-slider', {
        slidesPerView: 1,
        spaceBetween: 10,
        pagination: {
            el: '.swiper-pagination',
            type: 'bullets',
            dynamicBullets: true,
            clickable: true,
        },
        breakpoints: {
            991: {
                slidesPerView: 2,
            },
        },
    });

    /* =====================================================
        MODAL VIDEO
    ===================================================== */
    new ModalVideo('.video-btn');
});
