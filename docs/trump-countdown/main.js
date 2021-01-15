(function() {
  var start = new Date('2017-01-20T12:00:00-0500');
  var end = new Date('2021-01-20T12:00:00-0500');
  var total = timediff(start, end, 'DHm');

  function getTotalDays(dhmDuration) {
    return dhmDuration.days + (dhmDuration.hours / 24) + (dhmDuration.minutes / 1440);
  }

  function getPercentDone(total, remainder) {
    var totalDays = getTotalDays(total);
    var remainderDays = getTotalDays(remainder);
    return Math.round((1 - (remainderDays / totalDays)) * 10000) / 100;
  }

  $(document).ready(function() {
    setInterval(() => {
      var remainder = timediff(new Date(), end, 'DHm');
      var percentDone = getPercentDone(total, remainder);

      $('div.progress-bar').css('width', percentDone + '%');
      $('#remainder-percent').text(percentDone);
      $('#remainder-days').text(remainder.days);
      $('#remainder-hours').text(remainder.hours + 1);
      $('#remainder-minutes').text(remainder.minutes);
    }, 1000);
  });
})();
