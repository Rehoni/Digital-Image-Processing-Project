const { ipcRenderer } = require('electron')

const selectImage = document.getElementById('select-image')

selectImage.addEventListener('click', function (event) {
    ipcRenderer.send('open-file-dialog')
})

ipcRenderer.on('selected-image', function (event, path) {
    let img = document.getElementById('selected-image')
    img.src = path;
    img.style.display = 'flex';
    img.style.margin = 'auto';
    selectImage.style.display = 'none';
})

