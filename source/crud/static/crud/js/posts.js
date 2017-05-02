$(function()
{
   function filter_posts()
   {
      var csrftoken = getCookie('csrftoken');
      $('#posts_list').load(url_filter_posts, { csrfmiddlewaretoken: csrftoken,
      id_user: $(this).val() } );
   }
   function get_data_post(ev)
   {
      var id = $(ev.relatedTarget).attr('id');
      var ind = id.lastIndexOf('_');
      $.ajax({
         url : url_get_post,
         type : "POST",
         dataType: "json",
         data : { id_post: id.substring(ind+1),
         },
         // used with Django
         beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain)
               xhr.setRequestHeader("X-CSRFToken", csrftoken);
         },
         success : function(json)
         {
            $("input#id_title").val(json['title']);
            $("textarea#id_content").val(json['content']);
            var date_pub = json['date_pub'];
            var ind1 = 0;
            var ind2 = date_pub.indexOf('-');
            var year = date_pub.substring(ind1, ind2);
            ind1 = ind2+1;
            ind2 = date_pub.indexOf('-', ind1);
            var month = date_pub.substring(ind1, ind2);
            if (month.charAt(0) == '0')
               month = month.substring(1);
            ind1 = ind2+1;
            ind2 = date_pub.indexOf('T', ind1);
            var day = date_pub.substring(ind1, ind2);
            if (month.charAt(0) == '0')
               month = month.substring(1);
            $("select#id_date_pub_year option[value='"+year+"']").prop
            ('selected', true);
            $("select#id_date_pub_month option[value='"+month+"']").prop
            ('selected', true);
            $("select#id_date_pub_day option[value='"+day+"']").prop
            ('selected', true);
         },
         error : function(xhr,errmsg,err)
         {
            console.log(xhr.status + ": " + xhr.responseText);
         }
      });
   }
   $('#sel_user').on('change', filter_posts);
   $("#mymod").on('show.bs.modal', get_data_post);
});