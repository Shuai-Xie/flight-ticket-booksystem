[详细介绍 - 数据库课程设计 - 机票预订系统 - 简书](http://www.jianshu.com/p/60a392df9f03)

注册和登录界面都学习这位仁兄的 [buckyroberts-Viberr](https://github.com/buckyroberts/Viberr)

## 五、界面设计

### 5.1 欢迎界面

![欢迎界面](http://upload-images.jianshu.io/upload_images/1877813-c078119ecf8b22bf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

拟定一趟行程（长沙→上海 2017/4/2）

![输入行程](http://upload-images.jianshu.io/upload_images/1877813-8e7d67d4ba9be92c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.2 查询界面
用户 Let’s Go 之后，加载查询结果页面。

![查询成功界面](http://upload-images.jianshu.io/upload_images/1877813-c607acdbf2f65b32.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

默认的机票信息按照价格升序排列，用户通过点击机票信息上方的字段可以选择按照起飞时间或者到达时间升序排列，如下图，注意后两行的变化。


![查询结果按照起飞时间升序排列](http://upload-images.jianshu.io/upload_images/1877813-59e9c048ac02d75b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如果用户需要的航班数据库中不存在，就反馈错误信息。
将用户的目的地修改成中国（数据库中没有这趟航班）进行测试。


![查询失败界面](http://upload-images.jianshu.io/upload_images/1877813-b01972455fe041a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.3 订票界面

![点击订票按钮进行订票](http://upload-images.jianshu.io/upload_images/1877813-f31476f891dae2ff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

由于用户还没有登录，会直接反馈到登录界面。


![登录页面](http://upload-images.jianshu.io/upload_images/1877813-19d3851f0df7eb48.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

由于用户尚未注册，用户在该页面点击 Click here 进入注册账号页面，完成账号注册。 


![注册页面](http://upload-images.jianshu.io/upload_images/1877813-78e026c005cb9b8e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

用户注册完账号直接加载到查询页面。


![登录成功之后](http://upload-images.jianshu.io/upload_images/1877813-1ce7b06008a254f7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

用户再次点击订票，如果用户尚未订过该趟航班，加载订票确认页面，如果用户已经订过了，加载订票冲突页面。


![正常订票页面](http://upload-images.jianshu.io/upload_images/1877813-84ddfba39dca9100.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在正常订票页面点击确认，完成订票。


![正常订票页面完成订票](http://upload-images.jianshu.io/upload_images/1877813-d0cac0d501cfb050.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在个人中心用户可以查看自己的订票信息。


![用户个人中心](http://upload-images.jianshu.io/upload_images/1877813-070977fbe83f6167.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如果用户选择了自己已经订过的机票，加载订票冲突页面。


![订票冲突页面](http://upload-images.jianshu.io/upload_images/1877813-9c2f7a2ece954b5f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.4 退票界面

在用户的个人中心，可以进行退票。

![退票页面](http://upload-images.jianshu.io/upload_images/1877813-010c33405c8e8794.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

选择确认，完成退票，用户订票信息刷新。


![退票后的用户个人中心](http://upload-images.jianshu.io/upload_images/1877813-ef2d63e1012518d3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.5 管理员界面

![管理员 admin 登录账号](http://upload-images.jianshu.io/upload_images/1877813-bfe34ac3da390ca0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

在前面的 login_user 函数中已经有过判定，如果登录用户是管理员，加载航空公司的财务页面。


![login_user 函数登录用户身份判定](http://upload-images.jianshu.io/upload_images/1877813-b62cc6784cd273f9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

管理员登录成功。


![管理员页面 - 公司财务信息](http://upload-images.jianshu.io/upload_images/1877813-cc4afc25d37c4ef9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 5.6 后台管理界面

链接尾部输入 admin 进入后台管理


![进入后台](http://upload-images.jianshu.io/upload_images/1877813-5b533403b65c584e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

管理员登录账号


![管理员登录](http://upload-images.jianshu.io/upload_images/1877813-d2bfaf67531e5d9b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

后台数据，包括 Flight，User 和 Django 默认生成的数据。

![后台界面](http://upload-images.jianshu.io/upload_images/1877813-5d97aa787c87e85d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

航班信息管理，显示所有航班信息，可以增删改查。

![航班信息管理](http://upload-images.jianshu.io/upload_images/1877813-14106ac6b678c1df.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

旅客信息管理，操作同航班信息管理，注册的用户的信息都会保存在这里。

![旅客信息管理](http://upload-images.jianshu.io/upload_images/1877813-0d2f61b05e1b9393.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
