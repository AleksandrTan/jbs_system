$('#set_update').click(function () {
    let id_data = $(this).attr('data-id');
    console.log($(this).parent().prev().children().text());
    $.get(
      "/mainsystem/settings/update/",
      {
          id_data: id_data
      },
      function(data) {
      if (data.status) {
          console.log(3500);

      }
      else {
          console.log(4000);
      }
    }
    );
});
