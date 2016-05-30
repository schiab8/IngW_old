function get_invitations() {
    $.ajax({url: url_get_invitations, data:""}).done(update_invitations_list);
}

function update_invitations_list(data,options) {
    $('#invitations-list').html(data);
}

$('#toggle-invitations').click(function() {
    get_invitations();
    $('#invitations-list').toggle();
});
