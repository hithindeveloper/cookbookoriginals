(function($) {
    $(document).ready(function(e) {
        //$('a:contains("Home")').attr("href","");

        //used to submit search form
        $(".searchbutton").bind('click', function(e) {
            var search_text = $("#searchright").val();
            if (search_text != "") {
                $("#searchform").submit();

            }
        });

        if ($(".subscribe").length) {
            $("#newsletter_subscription").bind("submit", function(e) {
                param = {
                    "email_id": $("#email").val(),
                    "csrfmiddlewaretoken": $("[name='csrfmiddlewaretoken']").val()
                }
                $.ajax({
                    type: "POST",
                    url: "subscribe",
                    data: param,
                    success: function(data) {
                        $('.msg').html(data.msg);

                        $("#email").val("");
                        $(".msg").fadeOut(3000);
                    },
                    error: function() {}
                });
                e.preventDefault();
            });
        }
    });
}(jQuery));