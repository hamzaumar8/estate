$(document).ready(function() {
    var b = $("#basic-datatable").DataTable({
        "pageLength": 25,
        "order": [[ 0, "desc" ]],
        buttons: [{
                extend:    'copyHtml5',
                text:      '<i class="mdi mdi-content-copy mr-1"></i> copy',
                titleAttr: 'Copy'
            },
            {
                extend:    'csvHtml5',
                text:      '<i class="mdi mdi-file-alert-outline  mr-1"></i> CSV',
                titleAttr: 'CSV'
            },
            {
                extend:    'excelHtml5',
                text:      '<i class="mdi mdi-file-excel mr-1"></i> Excel',
                titleAttr: 'Excel'
            },
                {
                    extend:    'pdfHtml5',
                    text:      '<i class="mdi mdi-file-pdf-outline  mr-1"></i> PDF',
                    titleAttr: 'PDF'
            },
            "print"
        ],
        language: {
            paginate: {
                previous: "<i class='fas fa-angle-left'>",
                next: "<i class='fas fa-angle-right'>"
            }
        },
        drawCallback: function() {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    });
    var a = $("#datatable-buttons").DataTable({
        "pageLength": 25,
        "order": [[ 0, "desc" ]],
        buttons: [{
                extend:    'copyHtml5',
                text:      '<i class="mdi mdi-content-copy mr-1"></i> copy',
                titleAttr: 'Copy'
            },
            {
                extend:    'csvHtml5',
                text:      '<i class="mdi mdi-file-alert-outline  mr-1"></i> CSV',
                titleAttr: 'CSV'
            },
            {
                extend:    'excelHtml5',
                text:      '<i class="mdi mdi-file-excel mr-1"></i> Excel',
                titleAttr: 'Excel'
            },
                {
                    extend:    'pdfHtml5',
                    text:      '<i class="mdi mdi-file-pdf-outline  mr-1"></i> PDF',
                    titleAttr: 'PDF'
            },
            "print"
        ],
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>"
            }
        },
        drawCallback: function() {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    });

    var cat = $("#datatable-buttons-cat").DataTable({
        "pageLength": 25,
        "order": [[ 0, "desc" ]],
        buttons: [{
                extend:    'csvHtml5',
                text:      '<i class="mdi mdi-file-alert-outline  mr-1"></i> CSV',
                titleAttr: 'CSV'
            },
            {
                extend:    'excelHtml5',
                text:      '<i class="mdi mdi-file-excel mr-1"></i> Excel',
                titleAttr: 'Excel'
            },
            "print"
        ],
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>"
            }
        },
        drawCallback: function() {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    });

    var cat2 = $("#datatable-buttons-cat2").DataTable({
        "pageLength": 25,
        "order": [[ 0, "desc" ]],
        buttons: [{
                extend:    'csvHtml5',
                text:      '<i class="mdi mdi-file-alert-outline  mr-1"></i> CSV',
                titleAttr: 'CSV'
            },
            {
                extend:    'excelHtml5',
                text:      '<i class="mdi mdi-file-excel mr-1"></i> Excel',
                titleAttr: 'Excel'
            },
            "print"
        ],
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>"
            }
        },
        drawCallback: function() {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    });
    
    var cat3 = $("#datatable-buttons-cat3").DataTable({
        "pageLength": 25,
        "order": [[ 0, "desc" ]],
        buttons: [{
                extend:    'csvHtml5',
                text:      '<i class="mdi mdi-file-alert-outline  mr-1"></i> CSV',
                titleAttr: 'CSV'
            },
            {
                extend:    'excelHtml5',
                text:      '<i class="mdi mdi-file-excel mr-1"></i> Excel',
                titleAttr: 'Excel'
            },
            "print"
        ],
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>"
            }
        },
        drawCallback: function() {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    });

    $("#selection-datatable").DataTable({
        select: {
            style: "multi"
        },
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>"
            }
        },
        drawCallback: function() {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    }),
    $("#key-datatable").DataTable({
        keys: !0,
        language: {
            paginate: {
                previous: "<i class='mdi mdi-chevron-left'>",
                next: "<i class='mdi mdi-chevron-right'>"
            }
        },
        drawCallback: function() {
            $(".dataTables_paginate > .pagination").addClass("pagination-rounded")
        }
    }),
    // a.buttons().container().appendTo("#datatable-buttons_wrapper .row:eq(2)")
    b.buttons().container().appendTo("#basic-datatable_wrapper .row:eq(2)")

    // cat.buttons().container().appendTo("#datatable-buttons-cat_wrapper .row:eq(2)")
    // cat2.buttons().container().appendTo("#datatable-buttons-cat2_wrapper .row:eq(2)")
    // cat3.buttons().container().appendTo("#datatable-buttons-cat3_wrapper .row:eq(2)")

    $("#basic-datatable_wrapper .row:eq(0)").addClass('px-3')
    $("#basic-datatable_wrapper .row:eq(2)").addClass('card-footer')
    $('.dt-buttons').addClass('col-sm-12 mt-2 p-0').removeClass('btn-group');
    $('.dt-buttons .btn').removeClass('btn-secondary').addClass('btn-sm mx-1');
    $('.buttons-copy').addClass('btn-primary ');
    $('.buttons-csv').addClass('btn-info');
    $('.buttons-excel').addClass('btn-success');
    $('.buttons-pdf').addClass('btn-danger');
    $('.buttons-print').addClass('btn-warning').prepend('<i class="mdi mdi-printer  mr-1"></i>') ;
    $("#basic-datatable_filter input").addClass('form-control-alternative').css('border', '1px solid')
})