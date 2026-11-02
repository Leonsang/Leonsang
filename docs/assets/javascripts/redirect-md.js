// Auto-redirect if accessed with .md extension & enforce white notebook scheme
(function() {
  // 0. Always enforce white school notebook scheme ('default'), clearing any cached dark/slate mode
  function enforceWhiteNotebook() {
    if (document.body) {
      document.body.setAttribute('data-md-color-scheme', 'default');
      document.body.setAttribute('data-md-color-primary', 'indigo');
      document.body.setAttribute('data-md-color-accent', 'blue');
    }
    try {
      for (var i = 0; i < localStorage.length; i++) {
        var k = localStorage.key(i);
        if (k && k.indexOf('__palette') !== -1) {
          localStorage.removeItem(k);
        }
      }
    } catch (e) {}
  }
  enforceWhiteNotebook();

  // 1. If the current page URL ends with .md or contains .md, immediately redirect
  var path = window.location.pathname;
  if (path.indexOf('.md') !== -1) {
    var newPath = path.replace(/\/index\.md(\/)?$/i, '/').replace(/\.md(\/)?$/i, '/');
    if (newPath !== path) {
      window.location.replace(newPath + window.location.search + window.location.hash);
      return;
    }
  }

  // 2. Client-side link protection: catch any link pointing to a .md file and clean it
  function sanitizeLinks() {
    enforceWhiteNotebook();
    var links = document.querySelectorAll('a[href]');
    for (var i = 0; i < links.length; i++) {
      var href = links[i].getAttribute('href');
      if (!href || href.startsWith('http') || href.startsWith('mailto:') || href.startsWith('javascript:') || href.startsWith('#')) {
        continue;
      }
      if (href.indexOf('.md') !== -1) {
        var cleanHref = href.replace(/\/index\.md(\/)?/i, '/').replace(/\.md(\/)?/i, '/');
        links[i].setAttribute('href', cleanHref);
      }
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', sanitizeLinks);
  } else {
    sanitizeLinks();
  }
})();
