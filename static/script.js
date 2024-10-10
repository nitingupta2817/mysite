document.addEventListener('DOMContentLoaded', (event) => {
    const button = document.getElementById('changeContentButton');
    const content = document.getElementById('content');

    button.addEventListener('click', () => {
        content.textContent = 'The content has been changed!';
    });
});
