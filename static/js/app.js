document.addEventListener('DOMContentLoaded', () => {
    if ('serviceWorker' in navigator) {
        navigator.serviceWorker.register('/static/js/service-worker.js', { scope: '/' })
            .then((registration) => {
                console.log('Service Worker registered:', registration);
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
});
