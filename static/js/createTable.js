$(function() {
    $.ajax({
        url: '/layup',
        type: 'GET',
        success: function(response) {
            $('#table').html(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
});