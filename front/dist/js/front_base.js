function FrontBase() {
    
}

FrontBase.prototype.run = function(){
    var self = this;
    self.listenAuthBoxHover();
};

FrontBase.prototype.listenAuthBoxHover = function () {
    var authBox = $('.auth-box');
    var serviceBar = $('.service-bar');
    authBox.hover(function () {
        serviceBar.show();
    }, function () {
        serviceBar.hide();
    });
};

$(function () {
    var frontBase = new FrontBase();
    frontBase.run();
});

$(function () {
   if (window.template){
        template.defaults.imports.timeSince = function(dateValue){
            var date = new Date(dateValue);
            var dateTs = date.getTime();//得到毫秒
            var nowTs = (new Date()).getTime(); //得到当前时间
            var timestamp = (nowTs - dateTs)/1000; //得到秒数
         if (timestamp < 60){
             return '刚刚';
             }
            else if (timestamp >= 60 && timestamp < 60 * 60){
                minutes = parseInt(timestamp / 60);
                return minutes + '分钟前';
            }
            else if (timestamp >= 60 * 60 && timestamp < 60 * 60 * 24){
              hours = parseInt(timestamp / 60 / 60);
                return hours + '小时前';
            }
            else if (timestamp >= 60 * 60 * 24 && timestamp < 60 * 60 * 24 * 30){
                days = parseInt(timestamp / 60 / 60 / 24);
                return days + '天前';
            }
            else{
                var year = date.getFullYear();
                var month = date.getMonth();
                var day = date.getDay();
                var hour = date.getHours();
                var minute = date.getMinutes();
                return year + '/' + month + '/' + day + ' '+ hour + ':' + minute
        }
    };
   }
});