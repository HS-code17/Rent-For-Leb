function() {
  var $this = $contactDetails.filter('[data-rel="' + $(this).attr('data-rel') + '"]');
  if ($this.hasClass('callTo')) return true;
  if ($this.hasClass('activated')) return true;
  var path = $this.data("path"),
    id = $this.data("id"),
    securitySuggest = $this.closest('.contactbox').find('.contactwarn');
  if (securitySuggest.length) securitySuggest.show();
  var url = www_base_ajax + '/misc/contact/' + path + '/' + id + '/';
  $.get(url, function(dat) {
    if (path == 'phone' && typeof module_contact_as_image != 'undefined' && module_contact_as_image == 1) {
      $('#contact_methods .contact-a, .contact_methods .contact-a, #contact_methods_below .contact-a').filter('[data-rel="phone"]').closest('li').find('strong').html(dat.value);
      $.get(url + 'white/', function(dat) {
        $('#contact_methodsBigImage .contact-a').filter('[data-rel="phone"]').find('strong').html(dat.value)
      })
    } else $this.find('strong').html(dat.value);
    $this.find('.spoiler').hide();
    $this.removeClass('cpointer');
    $this.addClass('activated');
    $('body').trigger('adPageShowContact', {
      type: path
    })
  });
  if (useExternalScripts && typeof module_ati_tracking !== 'undefined') {
    var myxt = xtcustom,
      p = 'showing_' + path;
    myxt.action_type = p;
    p += ';' + adID;
    delete myxt.page_name;
    xt_med('C', '', p + '&stc=' + encodeURIComponent(JSON.stringify(myxt)), 'A')
  };
  return false
}