// Auto-redirect if accessed with .md extension & rewrite dynamic DOM links
(function() {
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
