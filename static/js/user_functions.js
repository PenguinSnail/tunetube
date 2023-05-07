// Franky Yang
function postLikedBy(){
    var userID = document.getElementById("currentUser")
    $.ajax({
        type: "POST",
        url: "/process_qtc",
        data: JSON.stringify(server_data),
        contentType: "application/json",
        dataType: 'json' 
      });

}
