(function ($) {
    if (!!$.fn.select2) {
        var params = $.fn.select2.defaults;
        params.formatInputTooShort = function () {
            return "Inserire più caratteri"
        };
        params.formatNoMatches = function () {
            return "Nessun risultato"
        };
    }
})($);
