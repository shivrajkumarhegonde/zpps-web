document.addEventListener("DOMContentLoaded", function () {
  let currentImages = [];
  let currentIndex = 0;

  document.querySelectorAll(".view-more-btn").forEach(button => {
    button.addEventListener("click", function () {
      currentImages = this.dataset.images.split(",");
      currentIndex = 0;
      document.getElementById("modalImage").src = currentImages[currentIndex];
      document.getElementById("modalTitle").innerText = this.dataset.title;
      $("#imageModal").modal("show");
    });
  });

  document.querySelector(".prev-btn").addEventListener("click", function () {
    if (currentIndex > 0) {
      currentIndex--;
      document.getElementById("modalImage").src = currentImages[currentIndex];
    }
  });

  document.querySelector(".next-btn").addEventListener("click", function () {
    if (currentIndex < currentImages.length - 1) {
      currentIndex++;
      document.getElementById("modalImage").src = currentImages[currentIndex];
    }
  });
});
