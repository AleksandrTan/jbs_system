$('#set_update').click(function () {
    that = $(this);
    let id_data = $(this).attr('data-id');
    console.log($(this).parent().prev().children());
    $.ajax({
            url: "/mainsystem/settings/update/",
            type: "get",
            async: false,
            data: "id_data="+id_data,
            success: function (data) {
                if (data.status) {
                    console.log(data.color, data.text, $(this).parent().prev().children());
                    that.parent().prev().children().css("color", data.color).text(data.text);
                } else {
                    return false;
                }
            }
        }
    );
});
