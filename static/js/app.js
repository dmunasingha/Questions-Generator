document.addEventListener('DOMContentLoaded', () => {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/js/service-worker.js', { scope: '/' })
            .then((registration) => {
            })
            .catch((error) => {
                console.log('Service Worker registration failed:', error);
            });
    }

    // Function to reload the page when back online
    function handleConnectionChange() {
        if (navigator.onLine) {
            // Connection restored, reload the page
            console.log('Back online, reloading the page...');
            location.reload();
        } else {
            console.log('You are currently offline.');
        }
    }

    // Event listeners for online and offline events
    window.addEventListener('online', handleConnectionChange);
    window.addEventListener('offline', handleConnectionChange);

    let deferredPrompt;
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e; // Save the event for later use
        // Show your own install button if you like
        const installButton = document.querySelector('#installButton');
        installButton.style.display = 'block';

        installButton.addEventListener('click', () => {
            deferredPrompt.prompt(); // Show the install prompt
            deferredPrompt.userChoice.then((choiceResult) => {
                if (choiceResult.outcome === 'accepted') {
                    console.log('User accepted the install prompt');
                } else {
                    console.log('User dismissed the install prompt');
                }
                deferredPrompt = null;
            });
        });
    });

});
