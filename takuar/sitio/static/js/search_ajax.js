function get_user_list() {
    name = $('#user-search-field').val();
    console.log('Pidiendo usuario: ' + name);
    $.ajax({url: url_search_user, data:"text="+name}).done(update_users_search_list);
}

function update_users_search_list(data,options) {
    $('#user-search-list').html(data);
}

$('#search-button').click(function() {
    get_user_list();
});
