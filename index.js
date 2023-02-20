const { app, BrowserWindow } = require("electron");
const path = require('path')

app.whenReady().then(createWindow);

function createWindow() {
  const win = new BrowserWindow({
    width: 1080,
    height: 1080,
    resizable: false,
    icon: path.join(__dirname, 'images/favicon.ico'),
    autoHideMenuBar: true
  });
  win.loadFile("index.html");
}