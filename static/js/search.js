function search()
{
  keyword = $('.search').val();

$.ajax({
    type: 'GET',
    url: "../search/"+keyword+'/',
    timeout: 5000,
    success: function(data){
        $( "li" ).css("background-color","white");
    data.forEach(function(element) {
 $( "li[value='" +  element + "']" ).css("background-color","yellow");
})
   },
    error: function(xhr, textStatus, errorThrown){
       $(window).unbind('scroll');
    }
  });

}



