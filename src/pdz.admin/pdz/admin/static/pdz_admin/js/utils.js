function init_datepicker(selector) {
    $(selector).attr('readonly', true);
    $(selector).datepicker({
        dateFormat: "dd/mm/yy",
        changeMonth: true,
        changeYear: true,
        yearRange: '1920:2099',
        minDate: (new Date(1920, 1 - 1, 1)),
        maxDate: 0,
        daysOfWeek: ["Dom", "Lun", "Mar", "Mer", "Gio", "Ven", "Sab"],
        monthNames: ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"],
        monthNamesShort: ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"],
    })
}
function init_timepicker(selector) {
    $(selector).attr('readonly', true);
    $(selector).timepicker({
        hourText: 'Ora',             
        minuteText: 'Minuti',  
    })
}