function likeClick(user_name, like_users_name) {
    let heartStatus = document.getElementById("btn-like");
    if (heartStatus.innerHTML === "<i class=\"far fa-heart\"></i>") {
        $.ajax({
            type: "POST",
            url: "/like",
            data: {user_name_give: user_name, like_users_give: like_users_name},
            success: function (response) {
                if (response["result"] == "success") {
                    alert(response["msg"]);
                    window.location.reload();
                }
            }
        })
        heartStatus.innerHTML = "<i class=\"fas fa-heart\"></i>"
    } else {
        $.ajax({
            type: "POST",
            url: "/cancel",
            data: {user_name_give: user_name, like_users_give: like_users_name},
            success: function (response) {
                if (response["result"] == "success") {
                    alert(response["msg"]);
                    window.location.reload();
                }
            }
        })
        heartStatus.innerHTML = "<i class=\"far fa-heart\"></i>"
    }
}