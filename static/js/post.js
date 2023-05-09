postComment = document.getElementById("post-comment")

postComment.addEventListener("keypress", function(e){
    if (e.keyCode == 13 && !e.shiftKey){
        document.getElementById("comment-form").submit();
    }
});
