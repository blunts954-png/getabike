const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in-view");
      }
    });
  },
  { threshold: 0.2 }
);

document.querySelectorAll("[data-animate]").forEach((el) => observer.observe(el));

const track = document.getElementById("inventory-track");
const buttons = document.querySelectorAll(".carousel-btn");

buttons.forEach((btn) => {
  btn.addEventListener("click", () => {
    const dir = btn.dataset.dir === "next" ? 1 : -1;
    track.scrollBy({ left: dir * 320, behavior: "smooth" });
  });
});

const inventoryCount = document.getElementById("inventory-count");
let count = 32;
setInterval(() => {
  const delta = Math.random() > 0.6 ? 1 : -1;
  count = Math.min(48, Math.max(18, count + delta));
  inventoryCount.textContent = count.toString();
}, 4200);
