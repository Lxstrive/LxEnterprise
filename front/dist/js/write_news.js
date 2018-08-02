function News() {
    
}

//富文本编辑器集成
News.prototype.initUEditor = function(){
     window.ue = UE.getEditor('editor',{
        'initialFrameHeight': 400,
        'serverUrl': '/ueditor/upload/'
    });

};

//上传图片
News.prototype.listenUploadFileEvent = function(){
    var uploadBtn = $('#thumbnail-btn');
    uploadBtn.change(function () {
       var file = uploadBtn[0].files[0];
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
                    var thumbnailInput = $('#thumbnail-form');
                    thumbnailInput.val(url)
               }
           }
       })
    });
};


//发布新闻
News.prototype.listenSubmitEvent = function(){
    var submitBtn = $('#submit-btn');
    submitBtn.click(function (event) {
        event.preventDefault();
        var btn = $(this);
        var pk = btn.attr('data-news-id');
        var title = $('input[name="title"]').val();
        var category = $('select[name="category"]').val();
        var desc = $('input[name="desc"]').val();
        var thumbnail = $('input[name="thumbnail"]').val();
        var content = window.ue.getContent();
        var url = '';
        if (pk){
            url = '/cms/edit_news/'
        }else{
            url = '/cms/write_news/'
        }
        myajax.post({
            'url': url,
            'data': {
                'title': title,
                'category': category,
                'desc': desc,
                'thumbnail': thumbnail,
                'content': content,
                'pk': pk
            },
            'success': function (result) {
                if (result['code'] === 200){
                    swal({
                        type: 'success',
                        title: '提交成功',
                    }).then(function () {
                        window.location.reload();
                    });

                }else {
                    swal({
                        type:'error',
                        title: '格式不正确, 请重试'
                    })
                }
            }
        })
    });
};

News.prototype.run = function () {
    var self = this;
    self.listenSubmitEvent();
    self.listenUploadFileEvent();
    self.initUEditor();

};

$(function () {
    var news = new News();
    news.run();
});