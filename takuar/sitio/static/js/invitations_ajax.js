// Ajax setup
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


function get_invitations() {
    $.ajax({url: url_get_invitations, data:""}).done(update_invitations_list);
}

function accepted_invitation() {
    alert("Aceptada");
}

function update_invitations_list(data,options) {
    $('#invitations-list').html(data);
    $('.invitation-form').submit(function(e) {
        e.preventDefault();
        var form = $(this).get(0);
        console.log("El form: ", form);
        form_data = new FormData(form);
        console.log("Lo que recibe el ajax: ",form_data);
        console.log("Listado de key+values:");
        for (var [key, value] of form_data.entries()) { 
              console.log("+++", key, value);
        }
        $.ajax(
            {
                type: 'POST',
                url: url_accept_invitation,
                data: form_data,
                success: accepted_invitation(),
                processData: false,
                contentType: false,
            });
    });
}

$('#toggle-invitations').click(function() {
    $('#invitations-list').toggle();
    get_invitations();
});


$(document).ready(function() {
    get_invitations();
}); 

