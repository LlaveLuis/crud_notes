$(function()
{
   function filter_posts()
   {
      var csrftoken = getCookie('csrftoken');
      $('#posts_list').load(url_filter_posts, { csrfmiddlewaretoken: csrftoken,
      id_user: $(this).val() } );
   }
   $('#sel_user').on('change', filter_posts);
});