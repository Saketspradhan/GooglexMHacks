let rendering = true;

// Simulate an asynchronous function that fetches new data
async function fetchNewPrompt() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve("New Prompt");
        }, 1000);
    });
}

// Simulate an asynchronous function that processes the data
async function asyncFunction(prompt) {
    console.log(`Processing: ${prompt}`);
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(`Processed: ${prompt}`);
        }, 1000);
    });
}

// Simulate a rendering function
async function render() {
    console.log("Rendering...");
    return new Promise(resolve => {
        setTimeout(() => {
            console.log("Rendered!");
            resolve();
        }, 1000);
    });
}

// Function to check if the page is still rendering
function isRendering() {
    return rendering;
}

// Main function
async function main() {
    while(isRendering()) {
        const prompt = await fetchNewPrompt(); // Fetch new prompt for the AI
        await asyncFunction(prompt);
        await render();
    }
}

// Run the main function
main();

// After 5 seconds, stop the rendering
setTimeout(() => {
    rendering = false;
}, 5000);
