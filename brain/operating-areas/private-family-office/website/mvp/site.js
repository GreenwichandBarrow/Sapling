const modal = document.getElementById('release-modal');

document.querySelectorAll('[data-open-modal]').forEach((element) => {
  element.addEventListener('click', () => {
    if (modal) modal.showModal();
  });
});

document.querySelectorAll('[data-close-modal]').forEach((element) => {
  element.addEventListener('click', () => {
    if (modal) modal.close();
  });
});

