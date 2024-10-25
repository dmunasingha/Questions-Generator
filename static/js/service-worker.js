const cacheName = 'pwa-v1';
const resourcesToCache = [
    '/',
    '/static/css/style.css',
    '/static/js/home.js',
    '/static/js/formValidator.js',
    '/static/js/app.js',
    '/offline', // Ensure this is your offline page
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(cacheName).then((cache) => {
            return cache.addAll(resourcesToCache);
        })
    );
    self.skipWaiting(); // Forces waiting service workers to become active
});

self.addEventListener('activate', (event) => {
    event.waitUntil(self.clients.claim()); // Take control of clients as soon as it's activated
});

self.addEventListener('fetch', (event) => {
    console.log('Fetch event for:', event.request.url); // Log every fetch request

    event.respondWith(
        caches.match(event.request).then((response) => {
            if (response) {
                console.log('Serving from cache:', event.request.url);
                return response; // Return cached response
            }

            // Fetch from network if not in cache
            return fetch(event.request).then((response) => {
                if (!response || response.status !== 200 || response.type !== 'basic') {
                    return response; // If response is invalid, return it
                }

                // Clone the response to cache it
                const responseToCache = response.clone();

                caches.open(cacheName).then((cache) => {
                    cache.put(event.request, responseToCache);
                });

                return response; // Return the original response
            }).catch((error) => {
                console.error('Fetching failed:', error);
                if (event.request.mode === 'navigate') {
                    return caches.match('/offline.html'); // Fallback to offline page
                }
                return new Response('You are offline and no cache is available.', {
                    status: 404,
                    statusText: 'Not Found',
                });
            });
        })
    );
});
