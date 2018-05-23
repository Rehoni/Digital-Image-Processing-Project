const electron = require('electron')
//electron.app负责管理Electron 应用程序的生命周期， electron.BrowserWindow类负责创建窗口。 

const BrowserWindow = electron.BrowserWindow
const Menu = electron.Menu
const app = electron.app


const path = require('path')
const url = require('url')
const os = require('os')
const { ipcMain } = require('electron')
const { ipcRender } = require('electron')
const { dialog } = require('electron')

const zerorpc = require('zerorpc');

var client = new zerorpc.Client();
client.connect("tcp://127.0.0.1:4242");

client.invoke('hello','rpc',function(error,res,more){
    console.log(res);
})

let template = [{
    label: '编辑',
    submenu: [{
        label: '撤销',
        accelerator: 'CmdOrCtrl+Z',
        role: 'undo'
    }, {
        label: '重做',
        accelerator: 'Shift+CmdOrCtrl+Z',
        role: 'redo'
    }, {
        type: 'separator'
    }, {
        label: '剪切',
        accelerator: 'CmdOrCtrl+X',
        role: 'cut'
    }, {
        label: '复制',
        accelerator: 'CmdOrCtrl+C',
        role: 'copy'
    }, {
        label: '粘贴',
        accelerator: 'CmdOrCtrl+V',
        role: 'paste'
    }, {
        label: '全选',
        accelerator: 'CmdOrCtrl+A',
        role: 'selectall'
    }]
}, {
    label: '文件',
    submenu: [{
        label: '打开图片',
        accelerator: '',
        click: function () {
            dialog.showOpenDialog({
                properties: ['openFile'],
                filters: [{ name: 'Images', extensions: ['jpg', 'png', 'gif'] }] //指定为图片
            }, function (files) {
                if (files) win.webContents.send('selected-image', files)
            })
        }
    }, {
        label: '转化为灰度图',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '保存图片',
        accelerator: '',
        click: function (event) {
            saveFile(event)
        }
    }]
}, {
    label: '增强',
    submenu: [{
        label: '直方图修正',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '灰度图增强',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '彩色图增强',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '低通滤波',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '高通滤波',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '同态滤波',
        accelerator: '',
        click: function (event) {

        }
    }]
}, {
    label: '变换',
    submenu: [{
        label: '旋转平移',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '拉伸（调整尺寸）',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '放大缩小',
        accelerator: '',
        click: function (event) {

        }
    }]
}, {
    label: '边缘检测',
    submenu: [{
        label: 'Sobel',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: 'Laplace',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: 'Prewitt',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: 'Roberts',
        accelerator: '',
        click: function (event) {

        }
    }]
}, {
    label: '高级',
    submenu: [{
        label: '图像复原',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '图像分割',
        accelerator: '',
        click: function (event) {

        }
    }, {
        label: '图像压缩',
        accelerator: '',
        click: function (event) {

        }
    }]
}, {
    label: '查看',
    submenu: [{
        label: '重载',
        accelerator: 'CmdOrCtrl+R',
        click: function (item, focusedWindow) {
            if (focusedWindow) {
                // 重载之后, 刷新并关闭所有的次要窗体
                if (focusedWindow.id === 1) {
                    BrowserWindow.getAllWindows().forEach(function (win) {
                        if (win.id > 1) {
                            win.close()
                        }
                    })
                }
                focusedWindow.reload()
            }
        }
    }, {
        label: '切换全屏',
        accelerator: (function () {
            if (process.platform === 'darwin') {
                return 'Ctrl+Command+F'
            } else {
                return 'F11'
            }
        })(),
        click: function (item, focusedWindow) {
            if (focusedWindow) {
                focusedWindow.setFullScreen(!focusedWindow.isFullScreen())
            }
        }
    }, {
        label: '切换开发者工具',
        accelerator: (function () {
            if (process.platform === 'darwin') {
                return 'Alt+Command+I'
            } else {
                return 'Ctrl+Shift+I'
            }
        })(),
        click: function (item, focusedWindow) {
            if (focusedWindow) {
                focusedWindow.toggleDevTools()
            }
        }
    }, {
        type: 'separator'
    }, {
        label: '应用程序菜单演示',
        click: function (item, focusedWindow) {
            if (focusedWindow) {
                const options = {
                    type: 'info',
                    title: '应用程序菜单演示',
                    buttons: ['好的'],
                    message: '此演示用于 "菜单" 部分, 展示如何在应用程序菜单中创建可点击的菜单项.'
                }
                electron.dialog.showMessageBox(focusedWindow, options, function () { })
            }
        }
    }]
}, {
    label: '窗口',
    role: 'window',
    submenu: [{
        label: '最小化',
        accelerator: 'CmdOrCtrl+M',
        role: 'minimize'
    }, {
        label: '关闭',
        accelerator: 'CmdOrCtrl+W',
        role: 'close'
    }, {
        type: 'separator'
    }, {
        label: '重新打开窗口',
        accelerator: 'CmdOrCtrl+Shift+T',
        enabled: false,
        key: 'reopenMenuItem',
        click: function () {
            app.emit('activate')
        }
    }]
}, {
    label: '帮助',
    role: 'help',
    submenu: [{
        label: '学习更多',
        click: function () {
            electron.shell.openExternal('http://electron.atom.io')
        }
    }]
}]

function addUpdateMenuItems(items, position) {
    if (process.mas) return

    const version = electron.app.getVersion()
    let updateItems = [{
        label: `Version ${version}`,
        enabled: false
    }, {
        label: '正在检查更新',
        enabled: false,
        key: 'checkingForUpdate'
    }, {
        label: '检查更新',
        visible: false,
        key: 'checkForUpdate',
        click: function () {
            require('electron').autoUpdater.checkForUpdates()
        }
    }, {
        label: '重启并安装更新',
        enabled: true,
        visible: false,
        key: 'restartToUpdate',
        click: function () {
            require('electron').autoUpdater.quitAndInstall()
        }
    }]

    items.splice.apply(items, [position, 0].concat(updateItems))
}

function findReopenMenuItem() {
    const menu = Menu.getApplicationMenu()
    if (!menu) return

    let reopenMenuItem
    menu.items.forEach(function (item) {
        if (item.submenu) {
            item.submenu.items.forEach(function (item) {
                if (item.key === 'reopenMenuItem') {
                    reopenMenuItem = item
                }
            })
        }
    })
    return reopenMenuItem
}

if (process.platform === 'darwin') {
    const name = electron.app.getName()
    template.unshift({
        label: name,
        submenu: [{
            label: `关于 ${name}`,
            role: 'about'
        }, {
            type: 'separator'
        }, {
            label: '服务',
            role: 'services',
            submenu: []
        }, {
            type: 'separator'
        }, {
            label: `隐藏 ${name}`,
            accelerator: 'Command+H',
            role: 'hide'
        }, {
            label: '隐藏其它',
            accelerator: 'Command+Alt+H',
            role: 'hideothers'
        }, {
            label: '显示全部',
            role: 'unhide'
        }, {
            type: 'separator'
        }, {
            label: '退出',
            accelerator: 'Command+Q',
            click: function () {
                app.quit()
            }
        }]
    })
    // 窗口菜单.
    template[3].submenu.push({
        type: 'separator'
    }, {
            label: '前置所有',
            role: 'front'
        })

    addUpdateMenuItems(template[0].submenu, 1)
}



function createWindow() {
    win = new BrowserWindow({ width: 1300, height: 800 })
    win.loadURL(url.format({
        pathname: path.join(__dirname, 'about.html'),
        protocol: 'file:',
        slashes: true
    }))
}

function openFile(event) {
    dialog.showOpenDialog({
        properties: ['openFile'],
        filters: [{ name: 'Images', extensions: ['jpg', 'png', 'gif'] }] //指定为图片
    }, function (files) {
        if (files) event.sender.send('selected-image', files)
    })
}

function saveFile(event) {
    const options = {
        title: '保存图片',
        filters: [
            { names: 'Images', extensions: ['jpg', 'png', 'gif'] }
        ]
    }
    dialog.showSaveDialog(options, function (filename) {
        event.sender.send('save-file', filename)
    })
}

app.on('ready', createWindow)

ipcMain.on('open-mainwindow', function () {
    win.loadURL(url.format({
        pathname: path.join(__dirname, 'main.html'),
        protocol: 'file:',
        slashes: true
    }))

    const menu = Menu.buildFromTemplate(template)
    Menu.setApplicationMenu(menu)
})

ipcMain.on('open-file-dialog', function (event) {
    openFile(event)
})

ipcMain.on('save-file-dialog', function (event) {
    saveFile(event)
})

app.on('browser-window-created', function () {
    let reopenMenuItem = findReopenMenuItem()
    if (reopenMenuItem) reopenMenuItem.enabled = false
})

app.on('window-all-closed', () => {
    let reopenMenuItem = findReopenMenuItem()
    if (reopenMenuItem) reopenMenuItem.enabled = true
    app.quit()
})