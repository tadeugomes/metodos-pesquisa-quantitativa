/* Navegação dos slides UFMA.
 *
 * Setas, espaço, PgUp/PgDn e clique percorrem as telas; Home/End vão às pontas.
 * A posição vai no hash da URL, para retomar o ponto exato do aula.
 *
 * A tecla D alterna o modo detalhe: no modo apresentacao so as telas do deck
 * aparecem; no modo detalhe o arquivo vira um documento rolável, em que a
 * condução de cada seção aparece logo abaixo das telas a que ela se refere.
 * O modo chosen fica no hash (#detalhe / #deck), e ?so_deck na URL faz a
 * impressão sair só com as telas.
 */
(function () {
  var slides = Array.prototype.slice.call(document.querySelectorAll(".slide"));
  var atual = 0;

  function mostra(i) {
    if (i < 0 || i >= slides.length) return;
    slides[atual].classList.remove("ativo");
    atual = i;
    slides[atual].classList.add("ativo");
    var num = slides[atual].querySelector(".numero-slide");
    if (num) num.textContent = (atual + 1) + " / " + slides.length;
  }

  // Muda a URL para retomar o ponto da aula. O replaceState LANÇA SecurityError em
  // arquivo aberto direto do disco (file://), e a exceção derrubaria o resto do
  // script: as setas e a tecla D parariam de funcionar. Por isso o try/catch — perder
  // a posição na URL é aceitável; perder a navegação não.
  function mudaHash(url) {
    try {
      history.replaceState(null, "", url);
    } catch (e) {
      /* file:// não permite; seguimos sem gravar a posição */
    }
  }

  function marcaHash(i) {
    var prefixo = document.body.classList.contains("modo-detalhe") ? "#detalhe/" : "#";
    mudaHash(prefixo + (i + 1));
  }

  function vai(i) {
    mostra(i);
    marcaHash(i);
  }

  // numera todas as telas
  slides.forEach(function (s, i) {
    var num = document.createElement("div");
    num.className = "numero-slide";
    num.textContent = (i + 1) + " / " + slides.length;
    s.appendChild(num);
  });

  // ---- modo detalhe ----
  function rolando(px) {
    try {
      window.scrollTo(0, px);
    } catch (e) {
      /* ambientes sem scroll (e jsdom) nao devem derrubar a navegacao */
    }
  }

  function alternaDetalhe(ligado) {
    document.body.classList.toggle("modo-detalhe", ligado);
    var barra = document.querySelector(".barra-detalhe");
    if (barra) barra.style.display = ligado ? "none" : "block";
    if (ligado) {
      rolando(0);
    } else {
      mudaHash("#" + (atual + 1));
    }
  }

  // o botao da barra chama isto pelo onclick, e a tecla D chama direto
  window.alternaDetalhe = function () {
    alternaDetalhe(!document.body.classList.contains("modo-detalhe"));
  };

  // ---- leitura do hash: #so_deck, #detalhe, #detalhe/N, #N ----
  var hash = location.hash.replace("#", "");
  var soDeck = /[?&]so_deck/.test(location.search);
  if (soDeck) document.body.classList.add("so-deck");

  var partes = hash.split("/");
  var inicial = parseInt(partes[partes.length - 1], 10);

  slides[0].classList.add("ativo");
  if (partes[0] === "detalhe") {
    alternaDetalhe(true);
    if (!isNaN(inicial)) {
      var alvo = document.getElementById("det-" + inicial);
      if (alvo) rolando(Math.max(0, alvo.offsetTop - 20));
    }
  } else if (!isNaN(inicial) && inicial >= 1 && inicial <= slides.length) {
    vai(inicial - 1);
  } else {
    vai(0);
  }

  document.addEventListener("keydown", function (e) {
    if (e.key === "d" || e.key === "D") {
      if (document.getSelection().toString()) return;
      alternaDetalhe(!document.body.classList.contains("modo-detalhe"));
      return;
    }
    if (document.body.classList.contains("modo-detalhe")) return; // no modo detalhe, role normalmente
    if (["ArrowRight", "ArrowDown", "PageDown", " "].indexOf(e.key) >= 0) {
      e.preventDefault();
      vai(atual + 1);
    } else if (["ArrowLeft", "ArrowUp", "PageUp"].indexOf(e.key) >= 0) {
      e.preventDefault();
      vai(atual - 1);
    } else if (e.key === "Home") {
      vai(0);
    } else if (e.key === "End") {
      vai(slides.length - 1);
    }
  });

  document.addEventListener("click", function (e) {
    if (document.body.classList.contains("modo-detalhe")) return;
    if (window.getSelection().toString()) return; // não avança ao selecionar texto
    if (e.target.closest && e.target.closest(".barra-detalhe")) return;
    vai(e.clientX > window.innerWidth * 0.25 ? atual + 1 : atual - 1);
  });
})();
