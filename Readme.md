# BJTU_Web_Auto_Login

可以自动登录北交校园网的python程序，支持编译为exe
-----
## library_require

- requests
- plyer
- subprocess
- pywifi
- time
- pyinstaller

## build

```shell
$ git clone
$ pyinstaller -F -i picture.ico main.py -n 校园网登录 --noconsole --hidden-import plyer.platforms.win.notification
```
