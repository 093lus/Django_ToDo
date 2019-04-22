  $( function() {

    $( "#sortable" ).sortable({

start: function(e, ui) {
        // creates a temporary attribute on the element with the old index
        $(this).attr('data-previndex', ui.item.index());
    },
    update: function(e, ui) {
        // gets the new and old index then removes the temporary attribute
        var newIndex = ui.item.index();
        var oldIndex = $(this).attr('data-previndex');
        $(this).removeAttr('data-previndex');
         $.ajax({
                url: '/reorder/',
                type: 'post',
                data: {'oldIndex':oldIndex, 'newIndex': newIndex}
            });
    }

});
    $( "#sortable" ).disableSelection();
  } );