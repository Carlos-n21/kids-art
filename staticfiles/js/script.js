/* jshint esversion: 6 */
console.log("Kids-Art: Celebrating your kids artwork");

function slugify(text) {
    return text.toString().toLowerCase()
        .replace(/\s+/g, '-')           // Replace spaces with -
        .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
        .replace(/\-\-+/g, '-')         // Replace multiple - with single -
        .replace(/^-+/, '')             // Trim - from start of text
        .replace(/-+$/, '');            // Trim - from end of text
}

document.addEventListener('DOMContentLoaded', function() {
    const titleInput = document.querySelector('#id_title');
    const slugInput = document.querySelector('#id_slug');

    if (titleInput && slugInput) {
        titleInput.addEventListener('input', function() {
            slugInput.value = slugify(titleInput.value);
        });
    }
});