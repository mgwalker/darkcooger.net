(function () {
  const end = new Date("2021-01-20T12:00:00-0500");

  function go() {
    $(".table .cell").show();

    if (moment().isAfter(end)) {
      $("header").hide();
      $(".table .cell").text(
        "The twice-impeached seditious motherfucker is out!"
      );
      return;
    }

    var remainder = timediff(new Date(), end, "HmS");

    if (remainder.hours < 1) {
      $("#hours").hide();
    }

    $("#remainder-hours").text(remainder.hours);
    $("#remainder-hours-s")[remainder.hours === 1 ? "hide" : "show"]();
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
