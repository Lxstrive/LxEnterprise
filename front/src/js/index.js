//轮播图
function Banner() {
    this.bannerWidth = 798;
    this.bannerGroup = $('#banner-group');
    this.index = 1;
    this.leftArrow = $('.left-arrow');
    this.rightArrow = $('.right-arrow');
    this.bannerUL = $('#banner-ul');
    this.liList = this.bannerUL.children('li');
    this.bannerCount = this.liList.length;
    this.pageControl = $('.page-control');
    this.listenBannerHover();
}

//轮播图ul动态宽度 方便添加任意多个轮播图
Banner.prototype.initBanner = function () {
    var self = this;
    // 无限轮播
    var fistBanner = self.liList.eq(0).clone();
    var lastBanner = self.liList.eq(self.bannerCount-1).clone();
    self.bannerUL.append(fistBanner);
    self.bannerUL.append(lastBanner);
    this.bannerUL.css({'width': self.bannerWidth*(self.bannerCount+2), 'left': -self.bannerWidth});
};
// 动态添加li标签 (轮播图下面的小点点)
Banner.prototype.initPageControl = function () {
    var self = this;
    for (var i=0; i<self.bannerCount; i++){
        var circle = $('<li></li>');
        self.pageControl.append(circle);
        if(i === 0){
            circle.addClass('active');
        }
    }
    self.pageControl.css({'width': self.bannerCount*12+8*2+16*(self.bannerCount-1)});
};
// 轮播图左右2边的箭头
Banner.prototype.toggleArrow = function (isShow) {
    var self = this;
    if (isShow){
        self.leftArrow.show();
        self.rightArrow.show();
    }else {
        self.leftArrow.hide();
        self.rightArrow.hide();
    }

};
//轮播图鼠标移上暂停轮播 移出开始轮播
Banner.prototype.listenBannerHover = function () {
    var self = this;
    this.bannerGroup.hover(function () {
        // 第一个函数是 把鼠标移动到banner上执行的函数
        clearInterval(self.timer);
        self.toggleArrow(true);
    }, function () {
        // 第二个函数是 把鼠标移出banner上执行的函数
        self.loop();
        self.toggleArrow(false);
    });
};
//轮播图下面的小点点 控制轮播图事件
Banner.prototype.listenPageControl = function () {
    var self = this;
    self.pageControl.children('li').each(function (index, obj) {
        $(obj).click(function () {
           self.index = index;
           self.animate();
        });
    });
};
//轮播图移动像素
Banner.prototype.animate = function () {
    var self = this;
    self.bannerUL.animate({'left': -798*self.index}, 500);
    var index = self.index;
    if (index === 0){
        index = self.bannerCount-1;
    }else if(index === self.bannerCount+1){
        index = 0;
    }else {
        index = self.index-1;
    }

    self.pageControl.children('li').eq(index).addClass('active').siblings().removeClass('active');
};
Banner.prototype.loop = function () {
    var self = this;
    this.timer = setInterval(function () {
        if (self.index >= self.bannerCount+1){
            self.bannerUL.css({'left': -self.bannerWidth});
            self.index = 2;
        }else{
            self.index++;
        }
        self.animate();
    }, 2000);
};
//轮播图左右2遍小箭头点击事件
Banner.prototype.listenArrowClick = function () {
    var self = this;
    self.leftArrow.click(function () {
        if(self.index === 0){
            self.bannerUL.css({'left': -self.bannerCount*self.bannerWidth});
            self.index = self.bannerCount - 1;
        }else {
            self.index--;
        }
        self.animate();
    });
    self.rightArrow.click(function () {
        if(self.index === self.bannerCount+1){
            self.bannerUL.css({'left': -self.bannerWidth});
            self.index = 2;
        }else {
            self.index++;
        }
        self.animate();
    })
};
// js入口函数
Banner.prototype.run = function () {
    this.loop();
    this.listenArrowClick();
    this.initPageControl();
    this.initBanner();
    this.listenPageControl();

};
$(function () {
   var banner = new Banner();
   banner.run()
});