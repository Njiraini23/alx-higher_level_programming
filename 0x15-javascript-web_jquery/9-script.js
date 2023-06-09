$('document').ready(function () {
  $.get('https://fourthtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
}):

