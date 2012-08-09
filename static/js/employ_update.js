$("li").click(function () {
    $(this).addClass('trim');
    var id = $(this).attr("id");
    var available = $(this).attr("data-available");
    available = (available === "True");
    available = !available;
    $.ajax({
        type : "PUT",
        url: "/employees",
        data: {
            employ_id : id,
            available : available}
    })
    alert(available);
});
