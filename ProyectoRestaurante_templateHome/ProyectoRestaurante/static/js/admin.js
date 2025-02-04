document.addEventListener("DOMContentLoaded", function () {
    // Animación de entrada para el encabezado
    gsap.from("#header", {
        duration: 1,
        y: -50,
        opacity: 0,
        ease: "power2.out"
    });

    // Animación de entrada para los módulos
    gsap.from(".module", {
        duration: 0.8,
        opacity: 0,
        y: 20,
        stagger: 0.2,
        ease: "power2.out"
    });

    // Animación de hover en botones
    document.querySelectorAll("button, input[type='submit'], .button").forEach(button => {
        button.addEventListener("mouseenter", function () {
            gsap.to(this, { scale: 1.05, duration: 0.2, ease: "power2.out" });
        });
        button.addEventListener("mouseleave", function () {
            gsap.to(this, { scale: 1, duration: 0.2, ease: "power2.out" });
        });
    });

    // Animación de desplazamiento para los módulos
    gsap.utils.toArray(".module").forEach(module => {
        gsap.from(module, {
            scrollTrigger: {
                trigger: module,
                start: "top 80%",
                toggleActions: "play none none none"
            },
            opacity: 0,
            y: 30,
            duration: 0.8,
            ease: "power2.out"
        });
    });
});
