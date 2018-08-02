
function Auth() {
  var self = this;
  self.maskWrapper = $('.mask-wrapper');
  self.scrollWrapper = $('.scroll-wrapper');
}
Auth.prototype.run = function(){
    var self = this;
    self.listenShowHideEvent();
    self.listenSwitchEvent();
    self.listenSigninEvent();
    self.listenSignupEvent();

};

Auth.prototype.showEvent = function () {
    var self = this;
    self.maskWrapper.show();
};
Auth.prototype.hideEvent = function(){
    var self = this;
    self.maskWrapper.show();
};
Auth.prototype.closeEvent = function(){
    var self = this;
    self.maskWrapper.hide();
};
Auth.prototype.listenShowHideEvent = function(){
    var self = this;
    var signupBtn = $('.signup-btn');
    var signinBtn = $('.signin-btn');
    var closeBtn = $('.close-btn');


    signinBtn.click(function () {
        self.showEvent();
        self.scrollWrapper.css({'left': 0});
    });

    signupBtn.click(function () {
        self.hideEvent();
        self.scrollWrapper.css({'left': -400})
    });
    closeBtn.click(function () {
        self.closeEvent();
    })
};
//监听点击切换事件
Auth.prototype.listenSwitchEvent = function(){
        var self = this;
       var switcher =  $('.switch');
       switcher.click(function () {

       var currentLef = self.scrollWrapper.css('left');
       currentLef = parseInt(currentLef);
       if (currentLef < 0 ){
           self.scrollWrapper.animate({'left': '0'});
       }else {
           self.scrollWrapper.animate({'left': '-400px'})
       }
    });
};

//ajax发送请求 登录
Auth.prototype.listenSigninEvent = function(){
    var self = this;
    var siginiGroup = $('.signin-group');
    var telephonInput = siginiGroup.find('input[name="telephone"]');
    var passwordInput = siginiGroup.find('input[name="password"]');
    var rememberInput = siginiGroup.find('input[name="remember"]');
    var submitBtn = siginiGroup.find(".submit-btn");
    submitBtn.click(function () {
        var telephone = telephonInput.val();
        var password = passwordInput.val();
        var remember = rememberInput.prop('checked');
        myajax.post({
            'url': '/account/login/',
            'data': {
                'telephone': telephone,
                'password': password,
                'remember': remember?1:0,

            },
            'success': function (result) {
                if (result['code'] == 200){
                    self.hideEvent();
                    window.location.reload();
                }else {
                    var messageObject = result['message'];
                    if (typeof messageObject == 'string' || messageObject.constructor == String){
                        // console.log(messageObject);
                        swal(messageObject);
                    }else {
                        for(var key in messageObject){
                            var messages = messageObject[key];
                            var message = messages[0];
                            swal(message)
                        }
                    }
                }
            },
            'fail': function (error) {
                swal(error)
            }
        });

    });
};
// ajax发送请求 注册
Auth.prototype.listenSignupEvent = function(){
    var self = this;
    var signupgroup = $('.signup-group');
    var telephonInput = signupgroup.find('input[name="telephone"]');
    var usernameInput = signupgroup.find('input[name="username"]');
    var password1Input = signupgroup.find('input[name="password1"]');
    var password2Input = signupgroup.find('input[name="password2"]');
    var submitBtn = signupgroup.find(".submit-btn");
    submitBtn.click(function () {
        var telephone = telephonInput.val();
        var username = usernameInput.val();
        var password1 = password1Input.val();
        var password2 = password2Input.val();
        myajax.post({
            'url': '/account/register/',
            'data': {
                'telephone': telephone,
                'username': username,
                'password1': password1,
                'password2': password2,
            },
            'success': function (result) {
                if (result['code'] == 200){
                    self.hideEvent();
                    window.location.reload();
                }else {
                    var messageObject = result['message'];
                    if (typeof messageObject == 'string' || messageObject.constructor == String){
                        // console.log(messageObject);
                        swal(messageObject);
                    }else {
                        for(var key in messageObject){
                            var messages = messageObject[key];
                            var message = messages[0];
                            swal(message)
                        }
                    }
                }
            },
            'fail': function (error) {
                swal(error)
            }
        });

    });
};

$(function () {
   var auth = new Auth();
   auth.run();
});