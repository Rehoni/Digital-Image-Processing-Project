const { ipcRenderer } = require('electron')

const selectImage = document.getElementById('select-image')

selectImage.addEventListener('click', function (event) {
    ipcRenderer.send('open-file-dialog')

})

ipcRenderer.on('selected-image', function (event, path) {
    document.getElementById('selected-image').src = path;
    document.getElementById('selected-image').style.display = 'flex';
    selectImage.style.display = 'none';
})

