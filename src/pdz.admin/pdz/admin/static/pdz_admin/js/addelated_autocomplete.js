var oldDismissAddAnotherPopup = dismissAddAnotherPopup || null;



var dismissAddAnotherPopup = function(win, newId, newRepr) {

    if (win.name == "id_users") {
        var widget =  $("#" + win.name);
        var data = widget.select2("data");
        data.push(
            {
                id: new String(newId),
                text: newRepr
            }
        );
        widget.select2("data", [], true);
        widget.select2("data", data, true);
        win.close()
    } else {
        return oldDismissAddAnotherPopup(win, newId, newRepr)
    }


}
