function get_user_list() {
    name = $('#user-search-field').val();
    $.ajax({url: url_search_user, data:"text="+name}).done(update_users_search_list);
}

function update_users_search_list(data,options) {
    $('#user-search-list').html(data);
    $('.add-button').click(function() {
        if (get_guests_ids().length<4) {
            var $user = $(this).parent().clone();
            $user.children('.add-button').addClass('remove-button btn-danger').removeClass('add-button btn-success').text('Quitar');
            $('#guests').append($user);
            update_guests();
        }
    });
}
function update_guests(){
    $('.remove-button').click(function() {
        $(this).parent().remove();
    });
};

function get_guests_ids(){
    var id_list = [];
    $('#guests').children('.user-box').children('.user-card').children('.user-id').each(function() { id_list.push($(this).text()) });
    return id_list;
};

$('#group-form').submit(function(e){
    var guest_string = get_guests_ids().join(',');
    $('#group-form input[name="guests_ids"]').val(guest_string);
    console.log($('#selected_event').text());
    $('#group-form input[name="event_id"]').val($('#selected_event').text());
    if (get_guests_ids().length<5){
        return true;
    }
    else{
        console.log(get_guests_ids());
        $('#group-form').prepend('<span>Demasiados invitados</span>');
        return false;
    }
});


$('#search-button').click(function() {
    get_user_list();
});
