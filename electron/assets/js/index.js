const {ipcRenderer} = require('electron')

const getStart = document.getElementById('get-started')

getStart.addEventListener('click', function(event){
    ipcRenderer.send('open-mainwindow')
})
