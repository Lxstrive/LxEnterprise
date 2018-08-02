function Banners() {

}

Banners.prototype.loadData = function(){
    var self = this;
    myajax.get({
        'url': '/cms/banner_list',
        'success': function (result) {
            if (result['code'] === 200){
                var banners = result['data'];
                for (var i=0; i<banners.length; i++){
                    var banner = banners[i];
                    self.createBannerItem(banner);
                }
            }
        }
    });
};

Banners.prototype.createBannerItem = function(banner){
    var self = this;
    var tpl = template("banner-item", {"banner": banner});
    var bannerListGroup = $('.banner-list-group');
    var bannerItem = null;
    if (banner){
        bannerListGroup.append(tpl);
        bannerItem = bannerListGroup.find(".banner-item:last");
    }else {
        bannerListGroup.prepend(tpl);
        bannerItem = bannerListGroup.find(".banner-item:first");
    }

    self.addImageSelectEvent(bannerItem);
    self.listenRemoveBannerEvent(bannerItem);
    self.addSaveBannerEvent(bannerItem);
};


Banners.prototype.listenAddBannerEvent = function(){
    var self = this;
    var addBtn = $('#add-banner-btn');
    addBtn.click(function () {
        var bannerListGroup = $('.banner-list-group');
        var length = bannerListGroup.children().length;
        if (length >= 6){
            swal({
                title:'最多只能添加6张轮播图',
                text: "2秒后自动关闭。",
                timer: 2000,
                showConfirmButton: false,
                type:'error',
                animation:true,
            });
            return;
    }
       self.createBannerItem();
    })
};


Banners.prototype.addImageSelectEvent = function(bannerItem){
    var image = bannerItem.find('.thumbnail');
    var imageInput = bannerItem.find('.image-input');
    //图片是不能打开选择文件框 只能通过input type=file
    image.click(function () {
        imageInput.click();
    });
    imageInput.change(function () {
        var file = this.files[0];
        var formData = new FormData();
        formData.append('file', file);
        myajax.post({
            'url': '/cms/upload_file/',
            'data': formData,
            'processData': false,
            'contentType': false,
            'success': function (result) {
                if (result['code'] === 200){
                    var url = result['data']['url'];
                    image.attr('src', url);
                }
            }
        });
    });
};

Banners.prototype.listenRemoveBannerEvent = function(bannerItem){
    var closeBtn = bannerItem.find('.close-btn');

    closeBtn.click(function () {
        var bannerId = bannerItem.attr('data-banner-id');
        if (bannerId){
            swal({
                text: '确定删除吗？',
                confirmButton:true,
                type: 'warning',
                confirmButtonText: '确定'
            }).then(function () {
                myajax.post({
                    'url': '/cms/delete_banner/',
                    'data': {
                        'banner_id': bannerId
                    },
                    'success': function (result) {
                        if (result['code'] === 200){
                            bannerItem.remove();
                            swal({
                                text: '删除成功',
                                type: 'success',
                            }).then(function () {
                                window.location.reload();
                            })
                        }
                    }
                });
            });
        }else {
            bannerItem.remove();
        }
    })
};

Banners.prototype.addSaveBannerEvent = function(bannerItem){
    var saveBtn = bannerItem.find('.save-btn');
    var imageTag = bannerItem.find('.thumbnail');
    var priorityTag = bannerItem.find('input[name="priority"]');
    var linkToTag = bannerItem.find('input[name="link_to"]');
    var prioritySpan = bannerItem.find('span[class="priority"]');
    var bannerId = bannerItem.attr('data-banner-id');
    var url = '';
    if (bannerId){
        url = '/cms/edit_banner/';
    }else{
        url = '/cms/add_banner/'
    }
    saveBtn.click(function () {
        var image_url = imageTag.attr('src');
        var priority = priorityTag.val();
        var link_to = linkToTag.val();

        myajax.post({
            'url': url,
            'data': {
                'image_url': image_url,
                'priority': priority,
                'link_to': link_to,
                'pk': bannerId
            },
            'success': function (result) {
                if (result['code'] === 200){
                    if (bannerId){
                        swal({
                            title:'轮播图修改完成',
                            type: 'success'
                        }).then(function () {
                            window.location.reload();
                        });
                    }else{
                          bannerId = result['data']['banner_id'];
                          bannerItem.attr('data-banner-id', bannerId);
                          swal({
                                title: '轮播图添加完成',
                                type: 'success'
                            }).then(function () {
                              window.location.reload();
                          })
                    }
                     prioritySpan.text("优先级: "+priority);
                }

            }
        });
    });
};


Banners.prototype.run = function () {
    this.listenAddBannerEvent();
    this.loadData();
};


$(function () {
    var banners = new Banners();
    banners.run();
});