/* Service worker — static app shell cached for offline study.
   The AI endpoint (…/api/chat, …/.netlify/*) is NEVER intercepted or cached: it always goes to the network.
   Works from the site root (Netlify) and from a project subpath (GitHub Pages: /Microbiolo_zzee/).
   DEPLOYING: bump VERSION on every deploy that changes the shell. Returning visitors then pick up the new
   worker on their next visit/tab focus (index.html registers with updateViaCache:'none'); pages load network-first. */
const VERSION = 'mb-v4';
const SHELL = ['./', 'index.html', 'manifest.webmanifest', 'icons/icon-192.png', 'icons/icon-512.png', 'icons/icon-maskable-512.png', 'icons/apple-touch-icon.png', 'icons/favicon-32.png', 'vendor/marked.min.js'];
const CACHEABLE_HOSTS = ['fonts.googleapis.com', 'fonts.gstatic.com'];

self.addEventListener('install', (e) => {
  e.waitUntil((async () => {
    const c = await caches.open(VERSION);
    // cache:'reload' bypasses the HTTP cache (GitHub Pages sends max-age=600) so a new version never precaches stale files
    await Promise.all(SHELL.map(async (u) => {
      const r = await fetch(new Request(u, { cache: 'reload' }));
      if (!r.ok) throw new Error('precache failed: ' + u);
      await c.put(u, r);
    }));
    await self.skipWaiting();
  })());
});

self.addEventListener('activate', (e) => {
  e.waitUntil((async () => {
    for (const k of await caches.keys()) if (k !== VERSION) await caches.delete(k);
    await self.clients.claim();
  })());
});

self.addEventListener('fetch', (e) => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== 'GET') return;                                              // POSTs (AI chat) are never touched
  if (url.origin === location.origin && (/\/api\//.test(url.pathname) || url.pathname.includes('/.netlify/'))) return; // AI/API: network only (subpath-safe)
  if (url.origin !== location.origin && !CACHEABLE_HOSTS.includes(url.hostname)) return;

  // Page loads: network first, revalidated (so new deploys appear immediately); cached copy when offline
  if (req.mode === 'navigate') {
    e.respondWith((async () => {
      try {
        const r = await fetch(req, { cache: 'no-cache' });
        if (r.ok) { const c = await caches.open(VERSION); c.put('index.html', r.clone()); }
        return r;
      } catch (_) {
        return (await caches.match('index.html')) || (await caches.match('./')) || Response.error();
      }
    })());
    return;
  }

  // Everything else (icons, fonts, libraries): cache first, revalidate in background
  e.respondWith((async () => {
    const c = await caches.open(VERSION);
    const hit = await c.match(req);
    const net = fetch(req, url.origin === location.origin ? { cache: 'no-cache' } : undefined)
      .then((r) => { if (r && (r.ok || r.type === 'opaque')) c.put(req, r.clone()); return r; }).catch(() => null);
    return hit || (await net) || Response.error();
  })());
});
