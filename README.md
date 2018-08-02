# LxEnterprise 企业官网项目(Django2.0, python3.x)
## [我的csdn](https://blog.csdn.net/weixin_41827390/)

### 下载项目到本地



>>1.进入到项目所在目录找到` requirements.txt `安装项目所需环境

>>2.pip install -r requirements.txt

>>3.安装mysql数据库 密码 ：123456

>>4.新建数据库  数据库名  django_combat

>>5.导入项目目录下的django_combat.sql文件到自己的sql数据库中，(不导入sql文件，视频不能播放)

>>6.python manage.py runserver 

>>7.浏览器中访问 127.0.0.1:8000访问

>>8,课程视频播放需要登陆之后才可播放

>>9.用户名: 18811112222 密码:123456

>>10. 可以自行注册

>>11.手机验证码功能没有实现，不用添
   



### 项目环境


>>前端语言:html/css/js/ajax/jquery/ 插件:gulp

>>后端语言:python3.x

>>框架: django-2.0/djangorestframework

>>调试工具: django-debug-toolbar

>>实现分页功能第三方库: django-pure-pagination

>>视频点播: 百度云

>> 个人收付款功能: paysAPI


 ### 项目介绍
 
*实在不知道该怎么介绍啊*

*为了方便测试注册的所有用户都是超级管理员，如果需要修改 可以再user的models.py中修改*
```python
class UserManager(BaseUserManager):
    def _create_user(self, telephone, username, password, **kwargs):
        if not telephone:
            raise ValueError('请输入手机号码')
        if not username:
            raise ValueError('请输入用户名')
        if not password:
            raise ValueError('请输入密码')
        user = self.model(telephone=telephone, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone, username, password, **kwargs):
        # 创建普通用户
        # 方便测试创建的用户都是超级用户可以使用后台管理
        kwargs['is_superuser'] = True # 修改普通用户权限把这2个设置为False
        kwargs['is_staff'] = True
        return self._create_user(telephone, username, password, **kwargs)

    def create_superuser(self, telephone, username, password, **kwargs):
        # 创建超级用户
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone, username, password, **kwargs)
```
