@echo off
nircmd.exe win hide ititle "cmd.exe"
nircmd exec hide "c:\batch files\syncfiles.bat"
nircmd.exe win hide ititle "cmd.exe"
npm start