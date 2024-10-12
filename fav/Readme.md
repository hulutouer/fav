## 这是一个浏览器收藏夹的小应用

##### 随着浏览器收藏夹越来越多，不得不分目录保存，但是分目录不在收藏夹栏之后又不方便寻找

##### 所以突然有一个思路就是把所有收藏的网址放在一个页面中 直接`Control+f`搜索就好啦

## 使用之前：

### 安装虚拟环境（conda或者virtualenv等）

#### 

```sh
# 创建虚拟环境
conda create -n fav python=3.10
# 进入虚拟环境
conda activate fav
#下载flask
pip install flask
```

### windows配置
> 1.bat批处理文件第三行：修改py文件的绝对路径

> 2.`Win+r` 输入 `shell:startup` 按`Enter` 把批处理文件拷贝到打开的目录中

### linux配置
> sh文件第三行：修改py文件的绝对路径

##### 增加执行权限

> chmod +x /home/sam/.config/fav/start_fav.sh

### linux设置开机自启（可选）

创建 systemd 服务文件：
在 /etc/systemd/system/ 目录下创建一个新的服务文件，例如 fav.service

```sh
sudo vim  /etc/systemd/system/fav.service
```

##### 粘贴内容

```shell
[Unit]
Description=Start Flask Application

[Service]
Type=simple
ExecStart=/home/sam/.config/fav/start_fav.sh
Restart=on-failure
User=sam
WorkingDirectory=/home/sam/.config/fav

[Install]
WantedBy=multi-user.target
```

> ExecStart：指定启动脚本的路径。
> User：指定运行服务的用户。
> WorkingDirectory：指定项目的工作目录。

##### 退出编辑器

```sh
:wq
```

重新加载 systemd 配置：

```sh
sudo systemctl daemon-reload
```

启用并启动服务：
启用服务以使其开机自启，并立即启动服务。

```shell
sudo systemctl enable fav.service
sudo systemctl start fav.service
```

检查服务状态：
确保运行正常。

```shell
sudo systemctl status fav.service
```