/* aaronc.ca — the page's accent changes with the day.
 *
 * Progressive enhancement. The page is complete, readable and correctly coloured
 * without this file: the resting hue stands on its own.
 *
 * The day is reckoned from sunrise, not midnight, so the change lands at dawn.
 * Sunrise is computed for the working location with the standard equation of
 * time, accurate to about ±2 minutes.
 *
 * The accent changes hue only. Saturation and both lightnesses are pinned in CSS
 * so every day carries identical contrast.
 */
(function () {
  var LAT = 43.09, LON = -79.08;   // working location
  var RAD = Math.PI / 180;

  /* Local clock hour of sunrise for the date given. */
  function sunriseHour(date) {
    var start = Date.UTC(date.getFullYear(), 0, 0);
    var N = Math.floor((date.getTime() - start) / 86400000) + 0.5;   // day of year

    // Equation of time, in minutes. Needs BOTH terms — the eccentricity term
    // alone is out by up to ~16 min in November.
    var B = 2 * Math.PI * (N - 81) / 364;
    var EoT = 9.87 * Math.sin(2 * B) - 7.53 * Math.cos(B) - 1.5 * Math.sin(B);

    // Solar declination.
    var g = (357.5291 + 0.98560028 * N) % 360;
    var C = 1.9148 * Math.sin(g * RAD) + 0.02 * Math.sin(2 * g * RAD)
          + 0.0003 * Math.sin(3 * g * RAD);
    var L = (g + C + 180 + 102.9372) % 360;
    var dec = Math.asin(Math.sin(L * RAD) * Math.sin(23.44 * RAD)) / RAD;

    // Hour angle at sunrise, allowing for refraction and solar radius (-0.833°).
    var cosH = (Math.sin(-0.833 * RAD) - Math.sin(LAT * RAD) * Math.sin(dec * RAD))
             / (Math.cos(LAT * RAD) * Math.cos(dec * RAD));
    var H = Math.acos(Math.max(-1, Math.min(1, cosH))) / RAD;

    var noonUTC = 720 - 4 * LON - EoT;            // minutes past UTC midnight
    var riseUTC = noonUTC - 4 * H;

    // UTC -> local clock hour. getTimezoneOffset already accounts for DST.
    return riseUTC / 60 - date.getTimezoneOffset() / 60;
  }

  var now = new Date();
  var day = new Date(now);

  // Before sunrise the day has not turned yet.
  if (now.getHours() + now.getMinutes() / 60 < sunriseHour(now)) {
    day.setDate(day.getDate() - 1);
  }

  document.documentElement.setAttribute('data-accent', 'd' + day.getDay());
})();
