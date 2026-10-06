// Preserve the selected section when comparing the two palettes.
// All content and links also work without JavaScript.
for (const link of document.querySelectorAll('[data-theme-choice]')) {
  link.addEventListener('click', () => {
    link.hash = window.location.hash;
  });
}
