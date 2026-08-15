/* Navegação dos slides UFMA: setas, espaço, PgUp/PgDn, clique; posição no hash da URL. */
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll(".slide"));
  var atual = 0;

  function mostra(i) {
    if (i < 0 || i >= slides.length) return;
    slides[atual].classList.remove("ativo");
    atual = i;
    slides[atual].classList.add("ativo");
    history.replaceState(null, "", "#" + (atual + 1));
    var num = slides[atual].querySelector(".numero-slide");
    if (num) num.textContent = (atual + 1) + " / " + slides.length;
  }

  // numera todos os slides
  slides.forEach(function (s, i) {
    var num = document.createElement("div");
    num.className = "numero-slide";
    num.textContent = (i + 1) + " / " + slides.length;
    s.appendChild(num);
  });

  document.addEventListener("keydown", function (e) {
    if (["ArrowRight", "ArrowDown", "PageDown", " "].indexOf(e.key) >= 0) {
      e.preventDefault();
      mostra(atual + 1);
    } else if (["ArrowLeft", "ArrowUp", "PageUp"].indexOf(e.key) >= 0) {
      e.preventDefault();
      mostra(atual - 1);
    } else if (e.key === "Home") {
      mostra(0);
    } else if (e.key === "End") {
      mostra(slides.length - 1);
    }
  });

  document.addEventListener("click", function (e) {
    if (window.getSelection().toString()) return; // não avança ao selecionar texto
    mostra(e.clientX > window.innerWidth * 0.25 ? atual + 1 : atual - 1);
  });

  var inicial = parseInt(location.hash.replace("#", ""), 10);
  slides[0].classList.add("ativo");
  if (!isNaN(inicial) && inicial >= 1 && inicial <= slides.length) {
    mostra(inicial - 1);
  } else {
    mostra(0);
  }
})();
