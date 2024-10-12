@echo off
conda activate fav
python C:\Users\Administrator\Desktop\fav\fav.py


@REM 通过运行命令 shell:startup 打开启动文件夹。按下 Win + R，输入 shell:startup，然后按 Enter。
@REM
@REM 将批处理文件复制到启动文件夹：
@REM 将 start_fav.bat 文件复制到这个启动文件夹中。

@REM Conda 环境路径：
@REM 确保 Conda 环境的路径正确。如果 conda activate 命令在批处理脚本中不起作用，可以尝试使用绝对路径，例如：
@REM
@REM
@REM @echo off
@REM call C:\Users\YourUsername\Anaconda3\Scripts\activate.bat fav
@REM python C:\Users\Administrator\Desktop\fav\fav.py
@REM 权限问题：
@REM 如果遇到权限问题，可以尝试以管理员身份运行批处理脚本，或者在批处理脚本中使用 runas 命令。
@REM
@REM 日志记录：
@REM 为了方便调试和查看日志，可以将输出重定向到一个日志文件：
@REM
@REM @echo off
@REM call conda activate fav > C:\Users\Administrator\Desktop\fav\startup_log.txt 2>&1
@REM python C:\Users\Administrator\Desktop\fav\fav.py >> C:\Users\Administrator\Desktop\fav\startup_log.txt 2>&1