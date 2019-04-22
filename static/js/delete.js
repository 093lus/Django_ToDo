function delete_task(id)
{

$.ajax({
    type: 'DELETE',
    url: "../delete/"+id+'/',
    timeout: 5000,
    success: function(data){

 $( "li[value='" +  data + "']" ).remove()

   },
    error: function(xhr, textStatus, errorThrown){
       $(window).unbind('scroll');
    }
  });

}
