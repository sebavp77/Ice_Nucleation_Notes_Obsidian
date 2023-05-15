window.MathJax = {
    tex: {
      inlineMath: [['$', '$']],
      displayMath: [["$$", "$$"]],
      processEscapes: true,
      processEnvironments: false
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };

  document$.subscribe(() => {
    MathJax.typesetPromise()
  })
