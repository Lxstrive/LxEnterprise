function NewsList() {
    
}


NewsList.prototype.listenSubmitEvent = function(){
    var submitBtn = $('.submit-btn');
    var textArea = $('textarea[name="comment"]');
    submitBtn.click(function () {
        var content = textArea.val();
        var news_id = submitBtn.attr('data-news-id');
        myajax.post({
            'url': '/news/public_comment/',
            'data': {
                'content': content,
                'news_id': news_id
            },
            'success': function (result) {
                if (result['code'] === 200){
                    var comment = result['data'];
                    var tpl = template('comment-item', {'comment': comment});
                    var commentListGroup = $('.comment-list');
                    commentListGroup.prepend(tpl);
                    swal({
                        title: '评论成功',
                        type: 'success',
                    }).then(function () {
                        window.location.reload()
                    })
                }else {
                    swal({
                        title:result['message'],
                        type:'error',
                    })
                }
            }
        });

    })
};


NewsList.prototype.run = function () {
    this.listenSubmitEvent();
};


$(function () {
   var newsList = new NewsList();
   newsList.run();
});