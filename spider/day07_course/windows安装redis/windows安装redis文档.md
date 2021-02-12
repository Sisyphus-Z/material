## **windows安装并设置redis**

- **安装步骤**

  ```
  【1】下载windows版本的redis安装包
  【2】解压到任意路径下
  	比如解压到：E:\redis-64.3.0.503
  【3】简单测试
  	切换到解压目录后，
      启动服务端: 双击 redis-server.exe
      测试客户端: 双击 redis-cli.exe
      
  【4】配置文件重命名
  	把目录下的：redis.windows.conf 改为 redis.conf
  【5】添加到计算机的服务当中
  	进入cmd命令行（在当前redis的路径下），执行如下命令：
  	redis-server --service-install redis.conf --loglevel verbose
  【6】设置服务自动启动
  	右键此电脑 - 管理 - 服务和应用程序 - 服务 - 右侧找到redis并双击 - 点击启动 - 启动类型选择自动 - 确定
  ```















