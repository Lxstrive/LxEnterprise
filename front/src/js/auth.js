// 点击登录按钮弹出模态对话框
$(function () {
   $('#btn').click(function () {
      $('.mask-wrapper').show();
   });
   $('.close-btn').click(function () {
      $('.mask-wrapper').hide();
   });
});


$(function () {
    $('.switch').click(function () {
       var scrollWrapper = $('.scroll-wrapper');
       var currentLef = scrollWrapper.css('left');
       currentLef = parseInt(currentLef);
       if (currentLef < 0 ){
           scrollWrapper.animate({'left': '0'});
       }else {
           scrollWrapper.animate({'left': '-400px'})
       }
    });
});



// function Auth() {
//   var self = this;
//   self.maskWrapper = $('.mask-wrapper');
// }
// Auth.prototype.run = function(){
//     var self = this;
//     self.listenShowHideEvent()
// };
//
// Auth.prototype.showEvent = function () {
//     var self = this;
//     self.maskWrapper.show();
// };
// Auth.prototype.hideEvent = function(){
//     var self = this;
//     self.maskWrapper.show();
// };
// Auth.prototype.listenShowHideEvent = function(){
//     var self = this;
//     var signupBtn = $('.signup-btn');
//     var signinBtn = $('.signin-btn');
//     signinBtn.click(function () {
//         self.showEvent();
//     });
//
//     signupBtn.click(function () {
//         self.hideEvent();
//     })
// };
//
// $(function () {
//    var auth = new Auth();
//    auth.run();
// });