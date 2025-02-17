const infoBtn = document.querySelector('i.info');
const dialog = document.querySelector('dialog');
const closeBtn = document.querySelector('dialog span');
const border = document.querySelector('dialog .dialog')

infoBtn.addEventListener('click', () => {
    dialog.showModal();
    dialog.scrollTop = 0;
})

closeBtn.addEventListener('click', () => {
    dialog.close();
})

dialog.addEventListener('click', (event) => {
    dialog.close();
})

border.addEventListener('click', (event) => {
    event.stopPropagation();
})
