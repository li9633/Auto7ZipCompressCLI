# Auto7ZipCompressCLI
## 关于本项目
Auto7ZipCompressCLI是一个批量生成压缩7z文件命令行的控制台程序
可用于快速对每个文件夹或每个文件单独压缩

## 配置环境变量
*仅限Windows用户*
1.将二进制文件放入任意目录
2.**将二进制文件所在目录添加到系统环境PATH变量中**
3.**将7zip安装目录添加到系统PATH变量中**
4.使用命令提示符或PowerShell 输入 **a7z -h** 成功后程序将返回帮助菜单

***
## 可选参数

基本参数|效果
---|:----:
-h|打印帮助菜单
-r|将**path.txt**文件替换为**run.cmd**
-n|生成一个新的**run.cmd**文件，**path.txt**将不会被改变
-p{password}|为压缩文件设置一个密码，例子 **-p1234**
-v{size}|为压缩文件设置分卷包，例子 **-v1g**
-mhe|关闭加密文件头     默认 **开启**

## 使用案例

要将以下文件或文件夹压缩
<img src="resource\a.png" alt="第一步" style="zoom:80%;" />

选择你要压缩的文件或文件夹后，按住Shift+鼠标右键，选择复制文件地址
<img src="resource\c.png" alt="第三步" style="zoom:80%;" />

在当前目录创建path.txt，将刚才复制的路径粘贴到path.txt中，保存后退出
<img src="resource\d.png" style="zoom:80%;" />

打开CMD或PowerShell，并进入该目录
<img src="resource\b.png" alt="第二部" style="zoom:80%;" /> 

输入 **a7z -n -p123**
<img src="resource\e.png" alt="第五步" style="zoom:80%;" />

如果以上操作都没有问题，那么该目录下会生成一个名为 **run.cmd**的脚本文件，脚本内容已经自动生成，直接运行即可
<img src="resource\f.png" style="zoom:80%;" />

***