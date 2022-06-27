function sendComment(articleid) {
    // console.log('hi')
    var comment = $("#CommentText").val();
    var parentid = $("#parent_id").val();


    $.get('/articles/add-article-comment', {
        comment,
        articleid,
        parentid: parentid

    }).then(res => {
        console.log(res)
        $("#comments_area").html(res)
        $("#CommentText").val("");
        $("#parent_id").val('');
        document.getElementById('command_'+comment.id).scrollIntoView({behavior:"smooth"})

    })
}

function FillParentId(parentid) {
    $("#parent_id").val(parentid)
    document.getElementById('command_form').scrollIntoView({behavior:"smooth"})
}