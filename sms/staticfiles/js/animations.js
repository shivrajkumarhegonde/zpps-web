// Floating effect for images using GSAP (GreenSock Animation Platform)
gsap.to(".img-float", {
    y: -15,
    duration: 2,
    repeat: -1,
    yoyo: true,
    ease: "ease-in-out",
});

// Optional: Add more animations as needed
// For example, you can animate text appearance or image movements on scroll
