const ipc = require('electron').ipcRenderer

const selectDirBin = document.getElementById('select-directory')

selectDirBin.addEventListener('click', function(event){
    ipc.send('open-file-dialog')
})

ipc.on('select-directory',function(event, path){
    document.getElementById('select-file').innerHTML='You Selected: ${path}'
})