window.onload = function() {
    // Returns a Promise that resolves after "ms" Milliseconds
    const timer = ms => new Promise(res => setTimeout(res, ms))

    async function load () { // We need to wrap the loop into an async function for this to work
        for (var i = 0; i < 9999999; i++) {
            await timer(3000); // then the created Promise can be awaited
            document.getElementById("check").submit();
        }
    }

    load();
}