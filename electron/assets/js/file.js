//jshint esversion:6 

const zerorpc = require("zerorpc");
const {
    ipcRenderer
} = require('electron');
let client = new zerorpc.Client();

client.connect("tcp://127.0.0.1:4242");

const selectImage = document.getElementById('select-image');

selectImage.addEventListener('click', function (event) {
    ipcRenderer.send('open-file-dialog');
});

ipcRenderer.on('selected-image', function (event, path) {
    let img = document.getElementById('selected-image');
    img.src = path;
    img.style.display = 'flex';
    img.style.margin = 'auto';
    selectImage.style.display = 'none';
    let original = document.getElementById('original-image');
    original.src = path;
    original.style.display = 'flex';
    original.style.margin = 'auto';
    let modified = document.getElementById('modified-image');
    modified.src = path;
    modified.style.display = 'flex';
    modified.style.margin = 'auto';
    let shape = document.getElementById('shape');
    let mean = document.getElementById('mean');
    let size = document.getElementById('size');
    client.invoke("echo", "hello",(error, res)=>{
        console.log(res);
    });
    client.invoke("size", path, (error, res) => {
        if (res == undefined) {

        } else {
            document.getElementById('size').innerHTML = 'size:' + res;
        }
    });
});