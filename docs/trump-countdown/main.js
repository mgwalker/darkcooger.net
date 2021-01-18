(function () {
  const start = new Date("2017-01-20T12:00:00-0500");
  const end = new Date("2021-01-20T12:00:00-0500");
  const total = timediff(start, end, "DHm");

  function getTotalDays(dhmDuration) {
    return (
      dhmDuration.days + dhmDuration.hours / 24 + dhmDuration.minutes / 1440
    );
  }

  function getPercentDone(total, remainder) {
    const totalDays = getTotalDays(total);
    const remainderDays = getTotalDays(remainder);
    return Math.round((1 - remainderDays / totalDays) * 10000) / 100;
  }

  function go() {
    $(".table .cell").show();

    if (moment().isAfter(end)) {
      $("header").hide();
      $(".table .cell").text(
        "The twice-impeached seditious motherfucker is out!"
      );
      return;
    }

    var remainder = timediff(new Date(), end, "DHmS");
    var percentDone = getPercentDone(total, remainder);

    $("header").show();
    $("div.progress-bar").css("width", percentDone + "%");
    $("#remainder-percent").text(percentDone);
    $("#remainder-days").text(remainder.days);
    $("#remainder-days-s")[remainder.days === 1 ? "hide" : "show"]();
    $("#remainder-hours").text(remainder.hours + 1);
    $("#remainder-hours-s")[remainder.hours === 0 ? "hide" : "show"]();
    $("#remainder-minutes").text(remainder.minutes);
    $("#remainder-minutes-s")[remainder.minutes === 1 ? "hide" : "show"]();
    $("#remainder-seconds").text(remainder.seconds);
    $("#remainder-seconds-s")[remainder.seconds === 1 ? "hide" : "show"]();
  }

  $(document).ready(function () {
    go();
    setInterval(go, 1000);
  });
})();
