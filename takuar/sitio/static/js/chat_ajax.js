url_chat
$.ajaxSetup({ 
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    } 
});
// /Ajax setup


function get_chat() {
    var form = $('#chat-form')[0];
    console.log(form)
    form_data = new FormData(form);
    console.log(form_data);
    $.ajax({url: url_chat, data:form_data}).done(update_chat);
}

function update_chat(data,options){
    $('chats').html(data);
}

$(document).ready(function() {
    get_chat();
    $('#chat-form').submit(function(e) {
        e.preventDefault();
        var form = $(this).get(0);
        form_data = new FormData(form);
        for (var [key, value] of form_data.entries()) { 
              console.log("+++", key, value);
        }
        $.ajax(
            {
                type: 'POST',
                url: url_chat,
                data: form_data,
                success: update_chat(),
                processData: false,
                contentType: false,
            }).done(get_invitations);
    });
});
