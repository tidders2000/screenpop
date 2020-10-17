var CACHE_STATIC_NAME = 'static-v5';
var CACHE_DYNAMIC_NAME = 'dynamic-v2';
var offlinePage = '/accounts/error/'

self.addEventListener('install', function(event) {
    console.log('[Service Worker] Installing Service Worker ...', event);
    event.waitUntil(
        caches.open(CACHE_STATIC_NAME)
        .then(function(cache) {
            console.log('[Service Worker] Precaching App Shell');
            cache.addAll([
                '/',
                '/accounts/error/',
                // // '/accounts/logout/',

                '/accounts/dashboard/',
                '/static/images/error_pattern.png',



                '/static/js/custom.js',
                '/static/css/main-style.css',
                '/static/css/style.css',
                '/static/css/custom.css',

                // 'https://code.jquery.com/jquery-3.2.1.slim.min.js',
                // 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
                // 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js',
                // 'https://kit.fontawesome.com/6cdfe06436.js',
            ]);
        })
    )
});

self.addEventListener('activate', function(event) {
    console.log('[Service Worker] Activating Service Worker ....', event);
    event.waitUntil(
        caches.keys()
        .then(function(keyList) {
            return Promise.all(keyList.map(function(key) {
                if (key !== CACHE_STATIC_NAME && key !== CACHE_DYNAMIC_NAME) {
                    console.log('[Service Worker] Removing old cache.', key);
                    return caches.delete(key);
                }
            }));
        })
    );
    return self.clients.claim();
});

addEventListener('fetch', fetchEvent => {
    const request = fetchEvent.request;
    if (request.method !== 'GET') {
        return;
    }
    fetchEvent.respondWith(async function() {
        const responseFromFetch = fetch(request);
        fetchEvent.waitUntil(async function() {
            const responseCopy = (await responseFromFetch).clone();
            const myCache = await caches.open(CACHE_STATIC_NAME);
            await myCache.put(request, responseCopy);
        }());
        if (request.headers.get('Accept').includes('text/html')) {
            try {
                return await responseFromFetch;
            } catch (error) {
                const responseFromCache = await caches.match(request);
                return responseFromCache || caches.match(offlinePage);
            }
        } else {
            const responseFromCache = await caches.match(request);
            return responseFromCache || responseFromFetch;
        }
    }());
});

// self.addEventListener('fetch', function(event) {
//     event.respondWith(
//         fetch(event.request)
//         .then(function(res) {
//             return caches.open(CACHE_DYNAMIC_NAME)
//                 .then(function(cache) {
//                     cache.put(event.request.url, res.clone());
//                     return res;
//                 })
//         })
//         .catch(function(err) {


//             return caches.match(event.request)



//         }).catch(function(err) {
//             return caches.open(CACHE_STATIC_NAME)
//                 .then(function(cache) {
//                     return cache.match('/accounts/error/');
//                 });
//         })

//     )

// })


// self.addEventListener('fetch', function(event) {
//     event.respondWith(
//         fetch(event.request)
//         .then(function(response) {
//             if (response) {



//                 return caches.open(CACHE_DYNAMIC_NAME)
//                     .then(function(cache) {
//                         cache.put(event.request.url, res.clone());
//                         return res;

//                     })

//             } else {
//                 caches.match(event.request)
//                     .then(function(response) {

//                         return response;

//                     })
//                     .catch(function(err) {
//                         return caches.open(CACHE_STATIC_NAME)
//                             .then(function(cache) {
//                                 return cache.match('/accounts/error');
//                             });
//                     })
//             }

//         })
//     )
// })