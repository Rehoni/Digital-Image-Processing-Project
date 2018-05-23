const {ipcRenderer} = require('electron')

const selectFile = document.getElementById('select-directory')

selectFile.addEventListener('click', function(event){
    ipcRenderer.send('open-file-dialog')
})

