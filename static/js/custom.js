function sendComment(){
    // console.log('hi')
    var comment = $("#CommentText").val();

    $.get('/articles/add-article-comment', {
        comment
    }).then(res => {
        console.log(res)
    })
}