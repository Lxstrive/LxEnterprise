function CmsNewsList() {
    
}

//后台时间控件
CmsNewsList.prototype.initDataPicker = function(){
    var startPicker = $('#start-picker');
    var endPicker = $('#end-picker');
    var todayDate = new Date();
    var todayStr = todayDate.getFullYear()+'/'+(todayDate.getMonth()+1)+'/'+todayDate.getDate();
    var options = {
        'showButtonPanel': true,
        'format': 'yyyy/mm/dd',
        'startDate': '',
        'endDate': todayStr,
        'language': 'zh-CN',
        'todayBtn': 'linked',
        'todayHighlight':true,
        'clearBtn': true,
        'autoclose':true,
    };

    startPicker.datepicker(options);
    endPicker.datepicker(options);
};

//删除新闻

CmsNewsList.prototype.listenDeleteEvent = function(){
    var deleteBtns = $('.delete-btn');
    deleteBtns.click(function () {
        var btn = $(this);
        var news_id = btn.attr('data-news-id');
        myajax.post({
            'url': '/cms/delete_news/',
            'data':{
                'news_id': news_id
            },
            'success':function (result) {
                if (result['code'] === 200){
                    swal({
                        title: '删除成功',
                        type: 'success',
                    }).then(function () {
                        window.location = window.location.href;
                    })
                }
            }
        });
    })
}

CmsNewsList.prototype.run = function () {
    this.initDataPicker();
    this.listenDeleteEvent();
};

$(function () {
   var newsList = new CmsNewsList();
   newsList.run();
});