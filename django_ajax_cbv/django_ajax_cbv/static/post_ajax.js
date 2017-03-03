if((typeof Ajax) == 'undefined'){
    var Ajax = {};
}

Ajax.post = function(caller, form, data)
{
    if(typeof data == 'undefined') data = {};

    var url = $(form).data('ajax-action'),
        path = window.location.pathname,
        ajax_req = $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: function(data, textStatus, jqXHR) {
                if(data.success){
                    caller.success(data, textStatus, jqXHR);
                } else {
                    caller.ajax_error();
                }
            },
            error: function(data, textStatus, jqXHR) {
                if(data.status == 400){
                    caller.ajax_error('400');
                } else if(data.status == 401){
                    window.location.href = '/signin/?go=' + path;
                } else if(data.status == 404){
                    caller.ajax_error('404');
                } else {
                    caller.ajax_error();
                }
            }
        });
};

if((typeof Post) == 'undefined'){
    var Post = {};
}

Author.init = function()
{
    var data = {
        name: $('myform').find('#id_name').val()
    };

    Ajax.post(this, 'myform', data);
};

Author.success = function(data, textStatus, jqXHR)
{
    console.log(data);
};

Author.ajax_error = function(etype)
{
    console.log('error');
};

$(function() {
    Author.init();
});