window.addEventListener('DOMContentLoaded', event => {
    $(document).ready(function () {
        $('#datatablesSimple').on('column-visibility.dt', function (e, settings, columnIdx, state) {
            var headerRow = $(settings.nTable).DataTable().table().header();
            $('tr:eq(1) th', headerRow).each(function (i) {
                if (i === columnIdx) {
                    $(this).css('display', state ? '' : 'none');
                }
            });
        });
        $('#datatablesSimple').DataTable({
            initComplete: function () {
                var api = this.api();

                var newRow = $('<tr>').appendTo(api.table().header());

                api.columns().every(function () {
                    var column = this;
                    var title = $(column.header()).text();

                    if (title != "Foto") {
                        var searchInput = $('<input>', {
                            type: "text",
                            class: "form-control",
                            style: "text-align:center; width: 100%; font-size: 15px;",
                            placeholder: title,
                            on: {
                                'keyup change clear': function () {
                                    if (column.search() !== this.value) {
                                        column.search(this.value).draw();
                                    }
                                }
                            }
                        });
                        $('<th>').append(searchInput).appendTo(newRow);
                    } else {
                        $('<th>').appendTo(newRow);
                    }
                });
            },
            searching: true,
            scrollX: true,
            scrollY: 500,
            columnDefs: [
                {
                    targets: 1,
                    className: 'noVis'
                }
            ],
            dom: '<"top"Bf>rt<"bottom"lip><"clear">',
            buttons: [
                {
                    text: 'Exportovat do CSV',
                    extend: 'csv',
                    charset: 'UTF-8',
                    bom: true,
                    filename: 'pspDataset',
                    className: 'btn btn-primary mr-2',
                    exportOptions: {
                        columns: ':visible'
                    }
                },
                {
                    text: 'Exportovat do Excelu',
                    extend: 'excel',
                    filename: 'pspDataset',
                    className: 'btn btn-primary mr-2',
                    exportOptions: {
                        columns: ':visible'
                    }
                },
                {
                    text: 'Výběr sloupců',
                    extend: 'colvis',
                    columns: ':not(.noVis)',
                    popoverTitle: 'Vyberat sloupce',
                    className: 'btn btn-primary mr-2'
                }
            ],
            lengthChange: true,
            lengthMenu: [[10, 25, 50, -1], [10, 25, 50, "všechny"]],
            language: {
                info: 'Stránka _PAGE_ z _PAGES_',
                infoEmpty: 'Nejsou k dispozici žádné záznamy',
                infoFiltered: '(filtrováno z _MAX_ celkových záznamů)',
                lengthMenu: 'Zobrazeno _MENU_ záznamů na stránku',
                zeroRecords: 'Nic nebylo nalezeno'

            }
        });
    });
});