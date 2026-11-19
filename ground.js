/* aaronc.ca — the hero ground answers whichever input is moving.
 *
 * Scroll: the ground lags behind the content, so it settles as the hero leaves.
 * Pointer: it drifts a few px against the mouse.
 *
 * VERTICAL ONLY, and that is a hard constraint rather than a preference. The
 * layer is full-bleed (it spans the viewport exactly), so any horizontal
 * displacement extends the scrollable area and produces a stray horizontal
 * scrollbar. `overflow-x: clip` on <html> does not absorb it reliably. The page
 * is already taller than the viewport, so vertical movement is free — sideways
 * movement is not. If you want the pointer's X to matter again, the layer has to
 * stop spanning the viewport first, which costs the full-bleed edge.
 *
 * Both inputs are bound unconditionally, on purpose. Switching between them on
 * matchMedia('(pointer: coarse)') would be the tidier-looking choice, but that
 * branch cannot be exercised by the test harness at all — and I would rather
 * ship behaviour that is identical on every device and that I have actually
 * measured. The two inputs rarely arrive together, and when they do the last one
 * simply wins.
 *
 * Touch pointermove is ignored, because on a touch device that would fight the
 * scroll: the scroll already carries the phone, and the guard keeps a drag from
 * driving the pointer path as well.
 *
 * Device orientation is the obvious third input and is deliberately NOT here:
 * DeviceOrientationEvent.requestPermission() needs a user-gesture prompt AND a
 * secure context, so it cannot be verified on an http preview and would ship
 * untested. Worth adding on the HTTPS deploy if you want it.
 *
 * The text never moves — only the ground. That is what makes it read as depth
 * rather than as animation.
 *
 * Skipped under prefers-reduced-motion: a JS transform is invisible to the CSS
 * media query, so it has to be checked here as well.
 *
 * Cost: two passive listeners, and a rAF that stops itself as soon as the value
 * settles. No background work.
 */
(function () {
  var hero = document.querySelector('.hero');
  if (!hero) return;

  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  if (reduced.matches) return;

  var MAX = 18;            // px of pointer travel at the vertical extremes
  var SCROLL_TRAVEL = 40;  // px the ground lags across the whole hero
  var EASE = 0.08;

  var target = 0;   // where the ground wants to be
  var cur = 0;      // where it is
  var running = false;

  function frame() {
    cur += (target - cur) * EASE;
    hero.style.setProperty('--py', cur.toFixed(2) + 'px');

    // Settle, snap, stop. Nothing schedules another frame until an input arrives.
    if (Math.abs(target - cur) < 0.05) {
      hero.style.setProperty('--py', target.toFixed(2) + 'px');
      running = false;
      return;
    }
    requestAnimationFrame(frame);
  }

  function schedule() {
    if (running) return;
    running = true;
    requestAnimationFrame(frame);
  }

  // Cheap on-screen test inside the handler. An earlier version gated everything
  // behind an IntersectionObserver's `visible` flag, which is set in an async
  // callback — the effect silently did nothing until (and unless) it fired.
  function onScreen() {
    var r = hero.getBoundingClientRect();
    return r.bottom > 0 && r.top < window.innerHeight;
  }

  function scrollDrift() {
    if (!onScreen()) return;
    var h = hero.getBoundingClientRect().height || 1;
    var progress = Math.min(1, Math.max(0, window.scrollY / h));
    target = -progress * SCROLL_TRAVEL;   // the ground lags the content
    schedule();
  }

  function pointerDrift(e) {
    if (e.pointerType === 'touch') return; // the scroll carries touch devices
    if (!onScreen()) return;
    // The pointer's Y, not its X: see the vertical-only note at the top.
    target = -(((e.clientY / window.innerHeight) * 2) - 1) * MAX;
    schedule();
  }

  window.addEventListener('scroll', scrollDrift, { passive: true });
  window.addEventListener('pointermove', pointerDrift, { passive: true });

  // If the visitor switches reduced-motion on mid-session, stop and reset.
  reduced.addEventListener('change', function (e) {
    if (!e.matches) return;
    window.removeEventListener('scroll', scrollDrift);
    window.removeEventListener('pointermove', pointerDrift);
    hero.style.removeProperty('--py');
    running = false;
    target = cur = 0;
  });
})();
