$(function()
{
   $("a#help_user").on("click", function(ev){
      ev.preventDefault();
   });
   $("a#help_user").messagebox({
      title: 'Available users',
      messageText: "user1: admin, admin123<br>user2: john, john0123",
      messageSubType: 'info',
      messageType : 'alert'
   });
});