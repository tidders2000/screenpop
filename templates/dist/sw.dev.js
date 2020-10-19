"use strict";

var CACHE_STATIC_NAME = 'static-v5';
var CACHE_DYNAMIC_NAME = 'dynamic-v2';
var offlinePage = '/accounts/error/';
self.addEventListener('install', function (event) {
  console.log('[Service Worker] Installing Service Worker ...', event);
  event.waitUntil(caches.open(CACHE_STATIC_NAME).then(function (cache) {
    console.log('[Service Worker] Precaching App Shell');
    cache.addAll(['/', '/accounts/error/', // // '/accounts/logout/',
    '/accounts/dashboard/', '/static/images/error_pattern.png', '/static/js/custom.js', '/static/css/main-style.css', '/static/css/style.css', '/static/css/custom.css' // 'https://code.jquery.com/jquery-3.2.1.slim.min.js',
    // 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
    // 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js',
    // 'https://kit.fontawesome.com/6cdfe06436.js',
    ]);
  }));
});
self.addEventListener('activate', function (event) {
  console.log('[Service Worker] Activating Service Worker ....', event);
  event.waitUntil(caches.keys().then(function (keyList) {
    return Promise.all(keyList.map(function (key) {
      if (key !== CACHE_STATIC_NAME && key !== CACHE_DYNAMIC_NAME) {
        console.log('[Service Worker] Removing old cache.', key);
        return caches["delete"](key);
      }
    }));
  }));
  return self.clients.claim();
});
addEventListener('fetch', function (fetchEvent) {
  var request = fetchEvent.request;

  if (request.method !== '') {
    return;
  }

  fetchEvent.respondWith(function _callee2() {
    var responseFromFetch, responseFromCache, _responseFromCache;

    return regeneratorRuntime.async(function _callee2$(_context2) {
      while (1) {
        switch (_context2.prev = _context2.next) {
          case 0:
            responseFromFetch = fetch(request);
            fetchEvent.waitUntil(function _callee() {
              var responseCopy, myCache;
              return regeneratorRuntime.async(function _callee$(_context) {
                while (1) {
                  switch (_context.prev = _context.next) {
                    case 0:
                      _context.next = 2;
                      return regeneratorRuntime.awrap(responseFromFetch);

                    case 2:
                      responseCopy = _context.sent.clone();
                      _context.next = 5;
                      return regeneratorRuntime.awrap(caches.open(CACHE_STATIC_NAME));

                    case 5:
                      myCache = _context.sent;
                      _context.next = 8;
                      return regeneratorRuntime.awrap(myCache.put(request, responseCopy));

                    case 8:
                    case "end":
                      return _context.stop();
                  }
                }
              });
            }());

            if (!request.headers.get('Accept').includes('text/html')) {
              _context2.next = 17;
              break;
            }

            _context2.prev = 3;
            _context2.next = 6;
            return regeneratorRuntime.awrap(responseFromFetch);

          case 6:
            return _context2.abrupt("return", _context2.sent);

          case 9:
            _context2.prev = 9;
            _context2.t0 = _context2["catch"](3);
            _context2.next = 13;
            return regeneratorRuntime.awrap(caches.match(request));

          case 13:
            responseFromCache = _context2.sent;
            return _context2.abrupt("return", responseFromCache || caches.match(offlinePage));

          case 15:
            _context2.next = 21;
            break;

          case 17:
            _context2.next = 19;
            return regeneratorRuntime.awrap(caches.match(request));

          case 19:
            _responseFromCache = _context2.sent;
            return _context2.abrupt("return", _responseFromCache || responseFromFetch);

          case 21:
          case "end":
            return _context2.stop();
        }
      }
    }, null, null, [[3, 9]]);
  }());
}); // self.addEventListener('fetch', function(event) {
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