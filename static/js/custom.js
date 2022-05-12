function sendComment(articleid) {
    // console.log('hi')
    var comment = $("#CommentText").val();

    $.get('/articles/add-article-comment', {
        comment,
        articleid,
        parentid: null

    }).then(res => {
        console.log(res)
    })
}