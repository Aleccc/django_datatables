$(document).ready(function() {
    var dt_table = $('.datatable').dataTable({
        "bFilter": true,
        "iDisplayLength" : 25,
        "bAutoWidth": true,
        "bProcessing": true,
        "bServerSide": true,
        "bStateSave": true,
        "sAjaxSource": DATA_TABLE_URL,
    });
});