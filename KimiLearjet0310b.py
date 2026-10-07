#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
======================================================================
 L E A R J E T   --   Full Pygame Flight Simulator with Perfect Panel
                              2X SCALED EDITION

 A tribute to the 1980s VZ-200 classic "Learjet", by J. Keech and
 P. Russell (Dick Smith Electronics, 1983).
 Full-screen pygame version with all four original screens:
   1. Introduction
   2. Route Selection
   3. Enroute Briefing
   4. Main Flight HUD (Pixel-Perfect Panel - 2X Scale)

 v2: airport letters (one per airport) on the briefing title,
     and a DME channel button [C] on the HUD that cycles three
     stations -- the destination (distance to it), the enroute
     airport (distance to it), and the origin (distance flown
     from it) -- with the tuned airport's letter inside the DME
     bracket, e.g. DME(M), DME(U) or DME(S). The two title
     letters are always among the stations on the cycle.

 v3: enroute (intermediate) airports on all 12 routes. The
     asterisk on the Enroute screen's dashed line now sits at the
     airport's true proportional distance from the origin, with
     the same info block as the origin/destination airports:
     ICAO code, ALT xxFT, and a distance-from-origin readout.

 v4: land at the enroute airport OR the destination -- every
     airport has a 2,000 m runway, and each airport's distance is
     measured from the origin start line to the END of its runway.
     Touch down before the runway start = crash at the airport;
     still rolling past the end = overrun crash. Overfly the
     enroute airport and the flight simply continues. The DME
     readout switches to metres 10,000 m before the tuned runway's
     threshold (12,000 m from its end).

 v5: navigation! An OBS course readout sits alongside the *HDG* line,
     automatically set to the course bearing for the destination at
     the start of the flight (twist it with [O] / [Shift+O]). A
     horizontal CDI gauge just right of the AUTO PILOT ON/OFF box --
     about four centimetres wide -- has a blue vertical needle that
     sits in the middle on course and walks TOWARD the course line as
     you drift off it, so the [A]/[D] turn keys move the line.
     Cross-track error is modelled for real: drift costs along-track
     progress, and the red square on the Enroute screen's dashed
     progress line rides above or below the line by your drift.

 v6: sound! All synthesised in code - no sound files to lose. A
     buzzing engine hum that spools up with N1, wind rush with
     airspeed, a stall buzzer, and cabin-chime BINGS for the big
     moments: gear locked, glideslope alive, autopilot on/off,
     level-off capture, the enroute callout, off-course and low-fuel
     warnings, touchdown - and a descending tone for the prangs.
     [M] mutes the lot.

 v7: the Enroute screen's blinking red square now BUZZES while it is
     lit -- the buzzer sounds the instant the square comes ON and
     falls silent the instant it goes OFF, so the screen chirps along
     with the flash. Respects the [M] mute.

 v8: the CRUISE VOICE. The sound mix is re-voiced for high-speed
     flight the way a real jet sounds at FL410: the wind rush swells
     to LEAD the mix in the cruise, the buzzy climb whine crossfades
     into a smooth high purr as speed builds past 150-250 kt (and
     softens as N1 settles), and a deep airframe rumble hums beneath
     it all. Also: silence about an intermediate airport the moment
     the red square passes it on the Enroute screen.

 v9: the CRASH DEBRIEF. A flight recorder counts stalls, overspeeds,
     terrain scares, off-course excursions, configuration habits and
     glideslope work; the crash screen then reviews the WHOLE flight
     -- what went well, the lessons, a tip matched to the prang --
     and rates the handling as a percentage: 0% = no skill shown,
     80%+ = a substantial improvement.

 v10: LONG-RANGE GLIDESLOPE. The G/S wakes 100 NM out at EVERY
      airport -- intermediate and destination alike -- and the
      AUTOLAND invitation now comes at 100 NM too: accept it and she
      flies the 3-degree path all the way down, staying clean and
      fast (240 kt) until 25 nm out, then configuring on schedule.

 v11: INTO-WIND TAKEOFF, like the VZ-200 original. Every flight
      starts parked 90 degrees OFF the runway heading: start the
      engines, turn her onto the runway heading with [A]/[D] (she
      refuses to rotate until HDG matches the runway), then brakes
      off and away you go. Ground turns need the engines running.

 v12: CODE-REVIEW FIXES. The flap-under-20 touchdown crash is live
      again (was dead code behind the too-fast branch); retiring a
      speed warning now clears only its OWN INFO line, never another
      system's message; the [V] enroute peek is protected from key
      auto-repeat (one press = one peek, like the [A]/[D] turns); the
      intro prompt genuinely pulses; the fuel counter reads LB to
      match the rest of the sim; dead variables removed.

 v13: THE LAP OF AUSTRALIA. All-new routes: twelve legs anti-clockwise
      around the coast -- Sydney up the Reef to Cairns, across the Top
      End, down the West, and home along the Bight with the westerlies
      astern -- plus two garnish legs (Adelaide-Melbourne via Mt
      Gambier, Melbourne-Sydney via Merimbula) for a fully coastal
      finish. Every distance is the true great-circle figure, every
      airport sits at its REAL elevation (the departure field's height
      now travels with the route instead of a hard-coded 31 ft), and
      with 30 airports exhausting the alphabet, the last four take
      digits: MADURA=1, WHYALLA=2, MT GAMBIER=3, MERIMBULA=4.

 v14: THE TRIBUTE. The bottom band of the intro screen now carries a
      three-line dedication to J. Keech and P. Russell, the authors of
      the 1983 Dick Smith Electronics original -- thank you, gentlemen.

 v15: TWO ENROUTE STOPS ON BRISBANE-TOWNSVILLE. The leg north now calls
      at ROCKHAMPTON (280 nm) AND MACKAY (431 nm, YBMK, letter Y) -- the
      first route with two intermediate airports. The enroute-airport
      system now takes a LIST of fields on any route ("vias"): the stars
      and ICAO/ALT/distance blocks on the Enroute screen, the terrain
      profile, the 100 NM glideslopes, the landings, the "ahead"
      callout and the post-passing silence all work field by field, and
      the DME [C] button cycles the destination, each enroute field in
      route order, then the origin. Single-"via" routes are untouched,
      and old save files still load (boolean via flags and the old "v"
      DME channel migrate to the first enroute field).

 v16: REVIEW PASS. A full-file audit. Four palette colours that nothing
      referenced are gone (GOLD, LIGHT_GREY, BOX_BLUE -- a duplicate of
      BORDER_BLUE -- and STAR_YELLOW); the v4 note's DME claim corrected
      (the "-" channel tracks the destination; it is the metre switch
      that every tuned channel shares); the crash debrief's tip matcher
      now tests "too little flap" BEFORE "overrun" -- the flap-less
      overrun's message ends in "overrun!" and used to win the wrong
      tip; the duplicate v13 changelog number split (the TRIBUTE entry
      is v14); comments aligned with the multi-enroute DME channels.

 v17: ETA, NOT ETI. The time box beside GROUND SPEED is relabelled ETA
      and now follows the DME station: the time to the destination on
      "-", and to each enroute field on "v0"/"v1" ... Any airport
      already passed reads "--:--", just as the DME reads "---" -- so
      the "+" origin channel, which only ever looks back, always shows
      "--:--".

 v18: CABIN PRESSURE. At very infrequent, random times while above
      10,000 ft the CAB PRESS box on the top row flashes its dark face
      red -- a pressurisation failure, with a warning at INFO. The
      light burns until the jet is brought below 10,000 ft; once it
      clears there she is free to climb back to her level, and the
      clock quietly re-arms for the next (equally rare) failure.
      Just like it used to occur in the original game.

 v19: THE LANDING-SEQUENCE FIXES (the Dunk Island review). Five
      changes, all flown and verified on the model itself:
      (1) the hard-arrival limit moves from -700 to -900 fpm -- the
      3-degree glideslope itself asks 600-700 fpm at the taught
      120-140 kt, so a good needle-arrival used to collapse the gear
      at the top of the band;
      (2) [W]/[S] now step 250 fpm a press and are protected from key
      auto-repeat like [A]/[D] -- the old 500-fpm steps (plus the
      flap-40 balloon of +280) could never hold the slope's -650 fpm,
      and a held pitch key slammed the command to +/-3,000;
      (3) an enroute field is no longer marked "behind us" until
      MID-RUNWAY -- the G/S needle, the descent chatter and the
      TOO LOW - GEAR warning now live all the way to the flare (they
      used to die at the threshold, parking the marker at LOW just
      when it mattered most);
      (4) the descent profile now aims at the runway THRESHOLD (was
      the runway END -- a full runway-length long, 500 ft high over
      the fence at approach speed) and the chatter hushes inside
      10 nm, where the needle rules the final;
      (5) AUTOLAND is now offered for the enroute field too, exactly
      as the v10 note always promised -- accept it and she flies the
      3-degree path to whichever airport is ahead, with a missed-
      runway hand-back for safety. Flying School's landing page now
      teaches the flare and the reversers.

 v20: THE MISSING FENCE (Dunk Island, revisited). Monte-Carlo flying
      on the model -- 300 hand-flown, needle-following arrivals into
      DUNK IS. -- showed barely one in three surviving: a third into
      the turf short of the runway, a third collapsing the gear. The
      glideslope aimed at the THRESHOLD at field elevation plus zero,
      so the corridor at the fence was exactly zero feet tall and any
      low wobble (or one coarse frame on a slow machine) was turf.
      The slope now aims 300 m INTO the runway and crosses the fence
      48 ft up; inside the touchdown zone the path flattens at the
      runway surface -- the needle can never order flight below the
      runway -- and parks at flare height: land by the taught flare,
      not by chasing the needle into the ground. Flying School now
      also teaches the anti-float [S] tap, and keeping the POWER ON
      against the buckets -- reverse bite comes from N1, so "cut
      thrust" (v19) was throwing the brakes away; the overrun tip now
      says so too. Same Monte Carlo after the fix: 300 of 300 land,
      and 150 of 150 on a slow machine's coarse frames.

 v21: WHITE ALTITUDE FIGURES ON THE ENROUTE SCREEN. Every ALT readout
      above the dashed route line -- origin, each enroute airport, and
      the destination -- now shows its figures in white; the words
      "ALT" and "FT" stay the yellow they always were. The HUD's own
      ALT box is untouched.

 v22: THE ENROUTE STOPOVER. A full stop at an intermediate airport no
      longer ends the flight: the captain is asked -- [C] continue the
      flight, [R] return to Route Selection. Continue and she is parked
      where she stopped, engines running, free to rotate at ANY heading
      (the into-wind rule is waived for this one departure): turn her
      round and go from where she sits, or back-taxi to the threshold
      2,000 m behind the runway end, turn round there and take off --
      the wheels now track the nose on the ground, so the DME metre
      readout and the Enroute-screen square unwind as she taxis back.
      The OBS is re-laid on the course to the destination and the
      cross-track count restarts at the field, so the CDI shows the
      correct track once airborne again. Landing at the destination is
      unchanged: flight summary, then Route Selection.

 v23: THE LEVEL-OFF LEAK, FIXED -- and a longer START flourish. A
      captured level is now HELD actively: after the dip-and-settle the
      capture moves into a hold that keeps a gentle correction on the
      target (the same law the autopilot's level hold uses), so a
      drifting flap balloon can no longer leave a stale trim behind
      and quietly sink her -- the old code froze vsi_cmd at the
      completion instant, and as the speed (and with it the balloon)
      moved on she leaked a couple of feet a minute forever, every
      fresh [L] re-capturing the sunk altitude a few feet lower.
      Re-pressing [L] while she holds simply confirms the level
      instead of dipping again. Any [W]/[S] still releases her. And
      the two spinning cells left of START now turn for the first
      FIFTEEN seconds of the flight after engine start, then rest.

 v24: THE CAPTAIN'S THREE. (1) THE OBS GATE: after engine start she
      may idle through the turn onto the runway, but takes no thrust
      for the roll until HDG reads what OBS reads -- an early [+]
      earns a CHECK HEADING reminder at INFO, and the lever simply
      waits at idle until she is straight (the enroute-stop
      departure, free at any heading, is exempt). (2) Flying School
      page 2: the DME/ETA line is word-wrapped inside the blue
      border. (3) THE [Z] ABANDON: the first press only MAKES the
      offer -- a flashing placard under the SAVE/LOAD/PAUSE buttons
      and a line at INFO, with the world frozen and the cockpit
      silent while the captain decides -- and a second, fresh [Z]
      (or a click on the placard) hands the flight back to Route
      Selection, no summary. Any other key flies on.

 v25: THE FLY-AROUND. Reaching the destination still airborne no
      longer teleports her back to DME 12 nm with the descent still
      running -- the old "ATC vectors you back" simply repeated the
      same approach until she finally landed. She now holds over the
      far end, the DME pinned at 0.0, while INFO advises: "Overshot
      the field - FLY AROUND for another attempt." Climb away, turn
      back: the moment she rounds out onto the return heading the
      DME counts back up, the advisory re-arms a mile out, and the
      approach is there to fly again (and again). Flying School's
      pear-shaped page teaches the manoeuvre.

 v26: THROTTLE DISCIPLINE, AND THE START CELLS TO LIFTOFF. The
      thrust lever now answers only with the engines running -- an
      early [+] before [E] used to wind the gauge to 100% while
      nothing moved; it now brings "Engines are off - start them
      [E] first." to INFO and the lever stays at idle. And the two
      spinning cells left of START no longer rest after fifteen
      seconds: they turn from engine start all the way to wheels-
      off, parking only when she leaves the ground (and falling
      quiet if the engines are shut down again on the ground).

 v27: THE SIXFOLD CLOCK, TAUGHT. Flying School now owns up to the
      time compression: the welcome page carries the fact (the sim
      runs six seconds for every real one -- an hour aloft takes
      ten real minutes), and the descent-planning page warns that
      its "minutes to run" -- like the ETA box and the thirty-
      second AUTOLAND window -- are sim minutes, ticking by six
      times faster than the wall clock. Both lines are written
      from TIME_SCALE itself, so they stay true if the dial moves.

 v28: THE GAUGE BAND. The Elevation (attitude indicator), G/S tape
      and FLAP gauge now form one tidy group in the clear band
      between the right edge of the ETA box and the left purple bar
      of the THRUST system: four equal gaps -- ETA to AI, AI to G/S,
      G/S to FLAP, FLAP to the purple bar -- so the G/S and FLAP
      labels no longer print on top of each other and the FLAP tick
      numbers no longer crowd the purple bar. The band's right edge
      is traced from the THRUST geometry before the gauges draw, so
      the group always lands exactly between its two neighbours.

 v29: FORTY-THREE YEARS, AND A CLEANER HEADING. The intro screen's
      tribute to J. Keech and P. Russell now counts more than 43
      years of enjoyment from their 1983 original. On the panel the
      heading readout drops its three asterisks -- it now reads
      HDG285\u00b0, a degree symbol after the output like the OBS
      readout beside it.

 v30: THE CAB PRESS SIREN, AND 25% MORE FUEL. While the CAB PRESS
      warning burns, a police-style HIGH-LOW siren now sounds along
      with the flashing box, and holds its note until the jet is below
      10,000 ft and the light goes out -- no more silent
      pressurisation failures. And every flight now loads 25% more
      fuel than the route's published figure (the briefing quotes the
      uplifted load), so a full stop at the intermediate airport
      still leaves enough in the tanks to reach the destination.

 v31: THE 45-DEGREE BANK. The Attitude Indicator's bank scale now
      reads 0 to 45 degrees on BOTH sides -- ten-degree rests at 10,
      20 and 30, the last rest at 45 -- and 45 degrees is the limit:
      no banking beyond it is allowed, the needle included.

 v32: THE 40-REST, AND SCHOOL AFTER THE PRANG. The bank scale
      gains another mark line between 30 and 45 on BOTH sides -- the
      40, labelled above the line like every other rest (the 45
      labels step a touch further out, so the two never sit on each
      other five degrees apart). And the CRASH screen now answers
      [T]: straight to Flying School from the debrief, then back to
      Route Selection when class is over.

 v33: THE BANK THAT STAYS BANKED. The AI's needle used to flick
      toward a turn and snap back to zero within a blink -- the bank
      target was released only 0.4 sim-seconds after the last turn
      command, and even a HELD turn key (a step every 1.8 sim-
      seconds) let the needle sag between steps. She now holds her
      30-degree bank THROUGH the turn: fresh commands keep the bank
      on the whole time, and when they stop she turns through the
      last step the way a jet really does -- about two seconds at
      30 degrees for five degrees of heading -- then rolls smoothly
      back to wings level, the needle riding it all the way in,
      through, and out. And the wings stay LEVEL on the ground:
      taxi turns no longer park the needle at 30 degrees.

 v34: THE GENTLE NEEDLE. The bank no longer slews at one flat,
      mechanical rate. She CHASES the commanded bank with a first-
      order lag, so the needle develops smoothly as the turn
      develops -- and when the turn is done she fights her way back
      to straight-ahead flight on a slower first-order return, the
      needle easing to zero over several seconds instead of motoring
      home at full rate.

 v35: PITCH IN DEGREES, AND [SHIFT+K]. The [W]/[S] keys now speak
      DEGREES of pitch instead of feet-per-minute: each press advances
      or retards the commanded pitch by ONE degree, snapped to the
      whole degree so the numbers stay clean -- at approach speed one
      degree is about 230 fpm, right where v19's quarter-thousand
      steps used to land. And holding either key keeps winding a
      degree at a time until released, at the same measured cadence
      the [A]/[D] turns use (one press on the ground is still just
      the rotation). The command is clamped to ten degrees either
      way, so a held key can never slam the vertical world to
      +/-3,000 fpm. And the assigned flight level now winds BOTH
      ways: [K] up ten, [Shift+K] back down ten.

 v36: THIRTY DEGREES OF PITCH. The pitch command's clamp opens
      from ten degrees either way to THIRTY -- matching the AI's
      pitch ladder, whose labels always ran to 30. Hold [W] and she
      winds up to a full 30-degree climb; hold [S] for a 30-degree
      bunt. One degree a press, as ever -- and the stall and
      overspeed warnings still keep score of what thirty degrees
      does to the airspeed.

 v37: THE GLIDE. Running the tanks dry no longer means certain
      death: with both engines flamed out the jet becomes a glider --
      25 NM for every 10,000 ft of height (about 15:1, the real
      Learjet's own figure) in the clean configuration at best-glide
      speed, around 150 kt. The descent speed-credit runs stronger
      while she is engineless, so pitching down BUYS speed and
      pulling up spends it -- the deadstick flare included. Fly her
      dirty or fast and the glide steepens, exactly as it should.
      The flameout INFO names the bargain: clean her up, hold 150
      kt, and find somewhere to land.

 v38: THE MACHMETER. The IAS box now changes over like the real
      panel: faster than Mach 0.4 -- or anywhere above 18,000 ft --
      the readout reports the MACH number and the little yellow "K"
      badge reads MACH; back below 18,000 ft AND under Mach 0.4 and
      the honest knots return, badge and all. True airspeed grows
      about two percent per thousand feet over the indicated, and
      the speed of sound falls away to 573.8 kt in the stratosphere
      -- at FL410 a 250 kt needle reads a very Learjet Mach 0.79.

 v39: THE AI'S NAMEPLATE. The Pitch/Bank gauge gets its title at
      last: "AI", centred one eighth of an inch above the instrument,
      in the same panel yellow as her sister labels -- measured with
      the panel's physical-unit helper, so it is a true eighth of an
      inch on any screen.

 v40: THE LIVE AI, AND THE FORTY-DEGREE SCALE. The Attitude Indicator
      no longer freezes while the autopilot has the aircraft: her turns
      now show on the gauge -- a bank into the turn, two degrees of bank
      for every degree the heading is off the bug (up to the limit),
      easing back to wings level as the bug is captured -- so the needle
      works through an autopilot turn exactly as it does through a
      hand-flown one. And the bank scale loses the 45 mark each side:
      the rests now run 0 to 40, spread a little further round the
      semicircle -- a degree of bank draws a degree and a half round the
      arc, so the outermost 40 rest sits sixty degrees off the top --
      and forty degrees is the new limit each way: the bank a turn
      command asks for, and no banking beyond it, the needle included.

 v41: THE CABIN ATMOSPHERE. The synthesised cruise voice (v8) -- the
      wind rush leading the mix, the fan purr and the deep airframe
      rumble -- is RETIRED. A real cabin-atmosphere recording now
      loops on the mixer's music stream for the WHOLE of every flight,
      from the moment the panel lights up to the full stop (or the
      prang). The file lives next to the script (see
      CRUISE_SOUND_CANDIDATES); if it cannot be found or decoded, the
      old synthesised cruise voice quietly returns, so the sim is
      never left voiceless. The bings, the stall buzzer, the CAB
      PRESS siren and the crash tone are untouched, and [M] still
      mutes the lot.

 v42: THE SINGLE-FILE .EXE, AND THE THIRTY-MINUTE HOP. Resources now
      resolve through _resource_candidates(): the hard-coded path, then
      the .exe/script folder, then the PyInstaller one-file bundle's
      unpack folder (sys._MEIPASS) -- so the cabin-atmosphere recording
      AND the intro photo can both be packed INTO the .exe:
          pyinstaller --onefile --windowed --add-data "learjet_cruise_atmos.mp3;." --add-data "learjet_takeoff_atmos.wav;." --add-data "learjet_landing_atmos.wav;." --add-data "learjet_takeoff.jpg;." --add-data "learjet_topdown.png;." --add-data "learjet_panel_bg.png;." --add-data "learjet_enroute_bg.jpg;." --add-data "learjet_route_bg.jpg;." learjet_full_panel_2x.py

 v75: THE COMPLETE BUILD LINE. The v42 command above is now brought up
      to date (the line directly beneath it): it packs ALL THREE real
      recordings -- cruise atmosphere, takeoff roar and landing voice
      -- plus the intro photo INTO the one-file .exe. The old line
      packed only the cruise MP3 and the photo, so on every PC but the
      captain's own (where the D-drive code folder quietly supplied the
      missing files) the roar and the landing voice were left behind
      and the synthesised stand-ins played instead -- "very ordinary
      generic sounds". If a takeoff/landing recording is an MP3 rather
      than a WAV, use that name in the build line instead. No program
      code changed in v75 -- the fix was the build line, never the sim.
      The save file now always lives beside the .exe/script (it used to
      follow __file__, which points INSIDE the throwaway unpack folder
      when frozen -- every save would have vanished on exit). And the
      clock slows from TIME_SCALE 6 to 2.9: measured on the model
      itself, MELBOURNE-SYDNEY runs about 86 sim-minutes gate to gate
      -- at 2.9 that is thirty REAL minutes.

 v43: THE ENGINE-START CABIN, AND A SHY CLOCK. The cabin-atmosphere
      recording now waits for the engines: it begins the moment they
      are started [E] and falls silent the moment they are shut down
      or flame out -- no engines, no cabin sound (mute, pause and
      flight-over still hush it too). And directly under the ETA box
      a second, quieter clock counts REAL elapsed time -- sim minutes
      divided by the compression, so pauses freeze it and a loaded
      save resumes it honestly -- drawn in a dim light blue: there
      when you look for it, all but invisible when you don't.

 v44: THE SHY CLOCK MOVES INBOARD -- AND COUNTS DOWN. The REAL
      readout leaves its perch under the ETA box for the box itself:
      a shadowy dim-blue line along the bottom edge, vague enough
      that you barely notice it. And it counts DOWN now: every route
      carries "sim_min", the sim-minutes the leg genuinely takes,
      timed on the model itself -- all fourteen legs flown with a
      fast climb, a 300 kt cruise and the AUTOLAND from the 100 nm
      offer. From the moment the panel lights up it reads the REAL
      minutes the flight should need (Melbourne-Sydney: about thirty
      at the 2.9 clock) and melts toward 0:00 as the wall clock runs.
      Land early and the spare minutes freeze on the panel at the
      full stop; run late and it quietly counts past zero.

 v45: THE NAMELESS COUNTDOWN. The shadowy clock inside the ETA box
      drops its "REAL" label, and its leading digit now sits directly
      under the ETA's own leading digit -- the two clocks read as one
      column of time: the sim's above, the real world's below. (In
      overtime the minus sign hangs one character left, so the digits
      -- not the sign -- keep the column.)

 v46: THE LIVING APPROACH. A pilot watched an autopilot landing at
      Merimbula and the attitude gauge never moved -- and she was
      right: with the wind aloft switched off the approach was laser
      straight, the bug sat on the course the whole way down, the
      bank needle pinned at zero, and the pitch read the flight-path
      angle only, frozen at two or three degrees down through every
      long phase. Two truths fix it. First, the gauge now reads pitch
      ATTITUDE -- the path angle plus the angle of attack, which
      grows as the speed comes back and eases as the flap takes the
      load -- so the nose lowers into the descent, rises through the
      slowdown from 240 to 130, nods at each flap gate and comes up
      into the flare. Second, the air on an approach is never glass:
      while the autopilot has her she tastes light turbulence, two
      slow random walks in heading and vertical speed, and her own
      steering and path laws chase every wobble back -- the AI banks
      gently into each correction, the VSI shimmers, and the
      glideslope needle hunts around the notch instead of parking
      beside it -- and the glideslope tape itself now reads the way
      a real receiver does, an ANGLE off the beam rather than a
      fixed five hundred feet of full scale, so the marker walks in
      off the peg as the path is joined and grows sensitive as the
      runway nears. The chop fades away through the last 600 feet,
      so the flare, the touchdown and the v20 fence all stay
      truthful: six hundred autolands under the chop -- three hundred
      at Merimbula, three hundred at Dunk -- six hundred arrivals.

 v47: THE COUNTDOWN RIDES THE DME. The shadowy clock inside the ETA
      box now follows the [C] channel just like the ETA above it:
      tuned to an enroute field it counts down the real minutes THAT
      leg still needs -- every enroute leg timed on the model, from
      brake release to touchdown, exactly as the route legs were
      (Townsville to Dunk Is. is twenty-six sim minutes, about nine
      of yours) -- tuned to the destination it reads the whole leg
      as before, and tuned to the origin it shows "--:--", because
      the origin only ever looks back; a field already passed reads
      the same dashes. Measuring those legs turned up a stowaway:
      the only invitation Dunk Is. can ever send arrives a thousand
      feet after take-off, and accepting it chased a beam still
      twenty thousand feet overhead all the way into the sea. The
      autoland now refuses to descend while she is low, far out and
      below the beam -- she holds her height and lets the path come
      down to her. And this changelog is back in marching order:
      the entries read v2 through v47, top to bottom, as they
      should have all along.

 v48: THE HONEST HORIZON. The v46 angle-of-attack offset had to go.
      It read truly -- a jet on a three-degree final really does hold
      her nose on the horizon -- but it broke the contract that
      matters more: the ladder's degrees and the [W]/[S] commands
      speak flight-path angle, so a degree commanded must be a
      degree shown. Three presses of [S] on final showed the
      aircraft still sitting on the horizon, and that is a lie the
      gauge may not tell. The attitude indicator reads the
      flight-path angle again: [S] lowers the nose below the horizon
      from the first press, at any speed. And the gauge keeps its
      v46 life under the autopilot -- not from a fudged offset now,
      but from the approach chop itself: the bank needle working
      every correction, the horizon shimmering with the VSI, the
      glideslope hunting its notch.

 v49: THE REV PLACARD. The REV flag leaves its perch beside the
      THRUST title for a placard directly under it: the R of REV
      rides exactly under the R of THRUST, the E and V following,
      inside a yellow rectangle the SAVE GAME button's own size,
      lettered in the button's smaller font so the word sits
      properly inside its box. The thrust marks and bars below step
      a dozen pixels down to make room. It still only shows while
      the buckets are out.

 v50: THE FLASHING R/TH. The REV placard under the THRUST title is
      gone after a single version -- reverse thrust now announces
      itself where the reverser lives: the R/TH label above the
      GEAR cluster flashes yellow-red, and the two guard squares
      beside it flash red-yellow in step, all on the CAB PRESS
      half-second cadence, for as long as the buckets are out. The
      thrust marks and bars return to their old positions.

 v51: THE THIRTY-SECOND INFO LINE. Every message posted at INFO: now
      carries the sim-time it was written, and step() retires any
      message that has not been re-asserted for thirty sim-seconds --
      the same thirty the AUTOLAND window counts, since v27 taught
      that the times on the INFO line are sim time. One-shot notices
      (DME channels, gear and flap calls, clearances) appear, are
      read, and quietly blank half a sim-minute later. Standing
      warnings such as STALL! and CAB PRESS re-post themselves every
      step while their condition holds, so they stay lit for the
      whole emergency and fade thirty sim-seconds after it ends.
      Pausing freezes the clock, and a crashed or finished flight
      keeps its last word on the line.

 v52: WIND FOR THE TUNED FIELD. The INFO line's surface wind now
      belongs to the airport tuned in the DME -- the destination on
      "-", each intermediate field on "v0","v1" ..., the origin on
      "+" -- named by its ICAO code, exactly as the DME itself
      follows [C]. And the wind direction is no longer a fixed
      westerly: it is always the route track plus one hundred and
      eighty degrees, so the aircraft arrives heading straight into
      the wind -- and departs into it too, which is just how a
      Learjet likes it. The direction is now shown three-figure,
      as a proper bearing.

 v53: THREE GOOD HABITS. (1) The R/TH cluster's flashing now ends
      with the landing run itself: the moment she comes to a full
      stop on the ground the buckets stow themselves, the label and
      its guard squares settle back to their steady stand-by
      colours -- silently right after an autoland, so the welcome
      message keeps the INFO line. (2) Standing brakes genuinely
      hold her: with the brakes on, engine power alone can no
      longer start her rolling, let alone take her into the air --
      she moves when [B] lets the brakes off, and not before.
      (Braking a rolling jet is untouched.) (3) The IAS, ALT and
      ASS FL titles now stand as far above the tops of their
      rectangles as the titles of the row below stand above
      theirs -- the line of each title ends right at its box top,
      the same clean clearance the DME, GROUND SPEED and ETA
      titles have always enjoyed.

 v54: ASLEEP UNTIL ENGINE START. The GROUND SPEED and ETA registers
      now hold the VZ-200 "display asleep" graphic -- a static row of
      the black/white diagonal cells, the same graphic that stands to
      the left of START and between START and F/F -- for as long as
      the engines are off. Nothing spins or flashes; the cells simply
      sit there. [E] brings the boxes to life: the cells vanish and
      the live ground speed, the ETA and the shadowy real countdown
      take their places. Shut the engines down on the ground and the
      cells return. (Also fixed: a five-character FUEL/VSI reading,
      e.g. "-1224", no longer spills its last digit onto the yellow
      unit backing.)

 v55: THE CAPTAIN'S SECOND THREE. (1) THE COUNTDOWN RESETS AT THE
      STOPOVER: the shadowy REAL clock used to keep counting the
      ORIGIN-to-destination figure straight through an intermediate
      landing. It now re-arms the moment the captain presses [C] at
      the stopover prompt: the new leg gets its own clock (starting
      now) and its own budget -- the tuned airport's measured sim-
      minutes LESS the field she has just left -- so Townsville-Dunk
      Is. reads about nine REAL minutes on departure from Townsville,
      and Rockhampton-Mackay-Townsville counts each hop separately.
      (2) THE WALL CLOCK: on the same dim-blue line as the countdown,
      at the right edge of the ETA box, the current time of day in
      24-hour HH:MM -- same tiny face, same shadowy blue. (3) THE
      HONEST ZERO: the full stop used to be declared the moment the
      speed dipped under 2 kt and the world froze with 1.x still on
      the gauge, so a parked jet read "001 K". The IAS (and with it
      the GROUND SPEED) now snaps to a true 000 K at the full stop.

 v56: TWO LEGS IN REAL TIME. TOWNSVILLE-CAIRNS (39 minutes up the Reef,
      past Dunk Is.) and KARRATHA-PERTH (145 minutes down the West, past
      Carnarvon) now fly at an honest 1:1 clock -- no compression at all,
      every minute aloft a minute of yours. The route screen badges them
      *REAL TIME*, the briefing says so before you commit, the flight
      opens with a settle-in note at INFO, and the ETA box's wall clock
      and countdown finally read the same minutes as your watch. The
      time scale now travels WITH the flight (jet.time_scale) instead of
      the global dial: the world's step, the countdown's conversion and
      a reloaded save all read the leg's own figure, and a pre-v56 save
      on either leg picks the flag up by route name. The other twelve
      legs are untouched at 2.9. For the long haul down the West:
      settle in, captain -- two and a half honest hours.

 v57: FUEL FOR HEIGHT. The higher she cruises, the less the engines
      drink: fuel flow now scales with altitude on the captain's own
      table -- FL200 the baseline (0% saved), then 15% at FL250, 28%
      at FL300, 38% at FL350, 46% at FL400 and 52% at FL450,
      interpolated straight-line between the listed levels, no saving
      at all below FL200, and the 52% figure holding at the ceiling.
      The published loads are unchanged, so height is pure profit --
      measured on the model itself: KARRATHA-PERTH cruised at FL450
      lands with 3,083 lb still in the tanks against 1,439 lb at the
      assigned FL210, on the same 6,000 lb uplift. One caution, flown
      and verified the same way: the AUTOLAND's 1,400 fpm descent cap
      cannot bring a high-cruising jet down to the 3-degree path
      inside its 100 nm capture -- from FL350 and above she never
      regains the beam, settles at the far end of the runway and
      overruns. From the assigned levels the beam comes down to her
      and she joins it 65 nm out; from FL330 she chases it down and
      catches it with 28 nm in hand. Cruising high? Be back down
      about FL300 by the 100 nm offer -- or land her yourself.
      Flying School's climb-and-cruise page teaches the table.

 v58: THE FL300 REMINDER, IN SCHOOL. Flying School's glideslope page
      now names the autoland's altitude limit in so many words: the
      invitation comes 100 nm out at ANY level, but the 1,400 fpm
      descent cap means she can only make the field from about FL300
      or below -- from FL350 up she lands long and overruns (v57
      measured it on the model). Cruising high on the fuel savings?
      Be down in time -- or keep her and land yourself.

 v59: THE 200 NM INVITATION (KARRATHA-PERTH ONLY). Both fields on the
      long haul down the West now offer the AUTOLAND 200 NM out --
      CARNARVON on the way down the coast, and PERTH at the end of
      it. Every other route on the Lap keeps the 100 NM offer. Two
      and a half honest hours at the 1:1 clock earn an unhurried
      arrival, and from the high cruising levels the v57 fuel table
      encourages, the extra hundred miles give the 1,400 fpm descent
      cap the room to bring her down to the 3-degree path in good
      time: far below the beam she drifts down gently, joins it as
      it comes down to her, and rides it to the fence. Carnarvon's
      early invitation is safe for the very reason Dunk Island's
      close one became so -- the v47 guard never chases a beam still
      overhead into the ground: engaged low, far out and below the
      path, she holds her height until the path comes down to her.

 v60: THE CAPTAIN'S VETO. An AUTOLAND request is the captain's to
      refuse, and now she can. While the invitation is on the table
      [N] declines it on the spot -- the placard reads A/L? Y/N so
      the whole choice is in front of her -- and once engaged, [Y]
      again WITHDRAWS the request and hands her back, gently: the
      autopilot keeps the heading bug and levels her exactly where
      she is, steady at any point of the approach, short final
      included. Either way the field joins the declined list, so the
      invitation cannot pop straight back up while she is still in
      range. [W]/[S] and [P] still take her the direct way, and now
      the autopilot comes fully off with her -- "you have the
      controls" is finally the truth. The placard itself is
      clickable too: click A/L? Y/N to accept, click AUTOLAND to
      hand her back.

 v61: THE SCHOOL LINE THAT LEAKED. The v60 AUTOLAND line on Flying
      School's GLIDESLOPE page grew to ninety-five characters and ran
      past the blue border -- the invitation's new [N] decline was the
      straw. The lesson is now three shorter lines inside the border,
      the teaching intact: the offer, the decline, and the [Y]
      hand-back.

 v62: THE TAKEOFF ROAR. A real takeoff recording now sounds on EVERY
      departure: the instant the thrust lever reaches 100% for the roll
      -- engines running, lined up, on the ground; never in the landing
      rollout, where [+] winds the reversers -- the cabin-atmosphere
      recording steps aside and the roar plays out in full, about
      twenty-one seconds (the captain's own file, its last ten seconds
      trimmed away). When the recording ends the existing ambience is
      heard again, exactly as before. Chopping the lever below 100%
      before liftoff -- a rejected takeoff -- ends the roar early and
      brings the ambience straight back; the prang and the full stop
      end it at once; the pause holds it mid-note, and [M] still mutes
      the lot. The stopover departure (v22) gets it too: every takeoff,
      every flight. The file lives next to the script (see
      TAKEOFF_SOUND_CANDIDATES) and packs into the .exe with
      --add-data "learjet_takeoff_atmos.mp3;." -- if it cannot be found
      or decoded, the ambience simply carries the takeoff as it always
      has, so the sim is never left voiceless.

      v62, revisited after a silent flight: the recording now ships as
      a WAV (learjet_takeoff_atmos.wav) and is tried FIRST -- the music
      stream decodes MP3 on any build, but a mixer Sound chunk cannot
      on some, which used to fail quietly into the general silence.
      Both names are still honoured, the load now REPORTS itself on the
      console (which file loaded, or every path tried and why), and the
      .exe build line gains --add-data "learjet_takeoff_atmos.wav;.".

 v63: THE LANDING VOICE, AND A WAY BACK FROM THE BRIEFING.
      (1) A real landing recording now sounds on EVERY arrival: the
      instant she descends through 400 FT above the field ahead it
      starts, LOOPING -- the approach, the RETARD call, the touchdown
      and the landing roll, all in the captain's own file -- and only
      the FULL STOP ends it. The prang ends it sooner, and a go-around
      that climbs back above 550 ft ends it and re-arms the trigger
      for the next attempt. While it leads, the cabin ambience steps
      aside, exactly as it does for the takeoff roar; the pause holds
      it mid-note, [M] silences it, and a [V] peek at the map hushes
      it and rejoins it on the return to the cockpit. The file lives
      next to the script as learjet_landing_atmos.wav (WAV first, the
      MP3 name welcome too -- see LANDING_SOUND_CANDIDATES), the load
      reports itself on the console, and the .exe build line gains
      --add-data "learjet_landing_atmos.wav;.".
      (2) THE BRIEFING'S [R]. The Enroute screen now offers a way back
      to Route Selection BEFORE the flight begins: [R] at the briefing
      and she never leaves the gate. Once the flight is under way the
      offer is gone -- the [V] peek still answers every key with the
      cockpit, exactly as before.

 v64: ONE TIME ON THE 1:1 LEGS. A captain at the start of KARRATHA-
      PERTH caught the ETA box telling two times at once: the white ETA
      read 251:01 -- 676 nm divided by the 161 kt she happened to have
      just off the ground -- while the shadowy countdown beneath it read
      2:24:05, the leg's measured 145 minutes less the minute she had
      flown. Both were honest, but on a REAL TIME leg the sim minute IS
      the wall-clock minute, and two clocks that should agree must
      agree. They now do: on the 1:1 legs the white ETA is driven by the
      countdown's own figure -- the tuned field's measured budget less
      the time this leg has run -- reading minutes:seconds as ever,
      while the dim-blue line below states the same duration in
      hours:minutes:seconds (and in overtime both carry the minus).
      The distance-over-speed estimate still rules the twelve compressed
      legs, where the two clocks speak different time by design.

 v65: THE DESKTOP BUTTON. A fourth bar joins SAVE GAME, LOAD GAME and
      PAUSE at the top right: DESKTOP closes the sim to the desktop with
      a single click, in lieu of [ESC] -- live in every state the key is
      live in (paused, at the enroute stop prompt, and through the
      full-stop dwell), and while the [Z] offer is up a click away from
      the placard still cancels it, exactly as ESC always has. The
      ABANDON placard moves to the DESKTOP row, immediately left of the
      button -- the band under the stack belongs to the ITT label, so
      the ITT 1/2 spacing is untouched. And "[ESC] quit" leaves the
      bottom legend: the key still works everywhere it always did, but
      the row no longer spends the space on it.

 v66: FIVE REAL SECONDS OF LEAD ON THE LANDING VOICE. The landing
      recording's own "100 feet" was arriving as the wheels stopped --
      the file's timeline runs a touch behind the flight it is
      dubbing. The trigger still watches the 400 ft mark above the
      field ahead, but it now fires EARLY by LANDING_LEAD_S real
      seconds, measured against the live sink rate and the leg's own
      clock: on a normal 3-degree final at 600-700 fpm that wakes the
      voice around 555-570 ft on the 2.9 legs and around 455 ft on the
      two 1:1 REAL TIME legs -- five real seconds sooner either way, by
      the wall clock, on every route. A 200 ft cap keeps a steep, fast
      descent from waking it hundreds of feet early, and the go-around
      re-arm now rides 100 ft above the (moving) trigger instead of
      sitting at a fixed 550 ft -- the led trigger could otherwise sit
      ABOVE the re-arm, and one small wobble on short final would have
      silenced the voice for the rest of the approach. One knob:
      LANDING_LEAD_S. Nudge it, fly the arrival, listen, repeat.

 v67: THE CLEAN DESK. (1) THE CLEAN EXIT: every way out of the sim --
      the DESKTOP button, [ESC], the window's own close -- now runs one
      shared shutdown: the mixer silenced and its device released, the
      window closed, the process itself ended outright. And if Sublime
      Text is still open, it too is asked to close -- gracefully, by
      its own [X], so hot-exit keeps the work. The sim returns cleanly
      to the desktop from Sublime, from a terminal, and from the
      converted single-file .exe alike -- where the goodbye line, with
      no console to print to, is guarded and simply vanishes.
      (2) THE VSI'S STEADY LAST DIGIT: the FUEL and VSI figures now
      share one fixed right edge, both right-justified against it, so a
      descent past 1,000 fpm ("-1224") grows LEFT into the dark cutout
      instead of jumping one space right -- the rightmost digit of the
      VSI always lines up with the rightmost digit of the FUEL above
      it, and the LB/FPM badges stand still too (they used to nudge
      right with a five-character reading).

 v68: A VARIED WIND, AND THREE MORE SECONDS OF LEAD. (1) THE SURFACE
      WIND SHOW: the INFO line's surface wind speed is no longer the
      perpetual 23 -- each airport of the flight now draws its own
      figure from the 10-30 range the first time the DME is tuned to
      it, and keeps it for the rest of the flight: the readout varies
      from field to field and from flight to flight, without ever
      flickering frame to frame. FOR SHOW ONLY, as ordered -- the
      flight model reads nothing of it; the only wind she feels is
      still the gentle heading wander, untouched. (2) THREE MORE REAL
      SECONDS OF LEAD on the landing voice: five proved too few --
      the recording's own timeline still trails the flight it is
      dubbing -- so LANDING_LEAD_S grows to eight real seconds, and
      the lead's altitude cap rises from 200 to 300 ft: at the 2.9
      clock eight seconds of a normal 600-700 fpm final is 232-271 ft
      of altitude, and the old cap would have quietly handed back the
      very seconds being added. The knob is still LANDING_LEAD_S --
      nudge it, fly the arrival, listen, repeat.

 v69: FIVE MORE REAL SECONDS OF LEAD. Eight was still not enough --
      the landing recording's opening still trailed the flight it is
      dubbing -- so LANDING_LEAD_S grows to thirteen real seconds,
      and the lead's altitude cap rises from 300 to 450 ft: at the
      2.9 clock thirteen seconds of a normal 600-700 fpm final is
      377-440 ft of altitude, and the 300 ft cap would have quietly
      handed back five of the very seconds being added. The knob is
      still LANDING_LEAD_S -- nudge it, fly the arrival, listen,
      repeat.

 v70: FOUR MORE REAL SECONDS OF LEAD. Thirteen was close but not it
      -- so LANDING_LEAD_S grows to seventeen real seconds, and the
      lead's altitude cap rises from 450 to 600 ft: at the 2.9 clock
      seventeen seconds of a normal 600-700 fpm final is 493-575 ft
      of altitude, and the old cap would have quietly handed back the
      very seconds being added. The knob is still LANDING_LEAD_S --
      nudge it, fly the arrival, listen, repeat.

 v71: THE COMMA, CLOSED UP. The ALT window's thousands separator rode
      in a full monospace character cell with 8 px of air on each
      side, so the thousands number and the last three digits stood
      about 1.6 character widths apart -- wider than the gap between
      the digits and their own FT badge -- and one number read as
      two: "39 , 650". The flanking gaps are now 2 px and 4 px, the
      comma carries the separation on its own, and the altitude reads
      as a single figure again: "39,650". The group recentres itself,
      and the below-1,000-ft graphics share the same constants.

 v72: QUIET REAL-TIME LEGS, AND A FULL NAME FOR THE AI. (1) The CAB
      PRESS random failure is SUSPENDED on the two 1:1 REAL TIME legs
      (TOWNSVILLE-CAIRNS and KARRATHA-PERTH): no failure at all there,
      no flashing box, no siren -- the cruise sound effect simply
      continues undisturbed until the aircraft has landed. The other
      twelve legs keep the failure exactly as v18/v30 made it. (2) The
      attitude indicator's nameplate now reads ATT IND instead of AI,
      the letters balanced across the top of the gauge and letter-
      spaced a touch wider than the instrument, so the word overlaps
      the gauge a little on either side.

 v73: THE CAPTAIN'S THIRD THREE. (1) THE THREE-SECOND ARRIVAL: at the
      full stop -- Intermediate or Destination alike -- the panel now
      holds the landed details EXACTLY as they are for three REAL
      seconds before any option is offered (the [C]/[R] stopover
      choice, or the any-key road to the flight summary), keys and
      clicks resting with the parked jet for the while -- ESC and the
      DESKTOP button stay live, as ever. And ALL sound continues
      through the hold: the landing voice plays on and the cabin
      ambience stays with her, the cockpit falling silent only when
      the options appear, exactly as it used to at the stop itself.
      One knob: LANDED_HOLD_S. (2) THE DESKTOP DOUBLE-CHECK: the
      DESKTOP button no longer closes the sim on a single click (the
      v65 note's "no questions asked" is answered after all) -- the
      first click only MAKES the offer: the button itself becomes a
      flashing DESKTOP? placard on the ABANDON placard's half-second
      cadence, with a line at INFO and the world frozen and the
      cockpit silent while the captain decides, and a second click on
      it confirms. Any other click, or any key -- ESC included --
      cancels and flies on: the [Z] ABANDON routine (v24), brought to
      the mouse. [ESC], [Q] and the window's own close still leave at
      once. (3) THE BRISK CELLS: the four diagonal cells between
      START and F/F now cycle at TWICE the rate -- a flip every three
      sim-seconds (was six). The rapid pair left of START is
      untouched.

 v74: THE LANDING VOICE LEAVES THE REAL-TIME LEGS, AND A RACE MENDED.
      (1) The captain's standing order, restated: the landing
      recording stays OFF the two 1:1 REAL TIME legs
      (TOWNSVILLE-CAIRNS and KARRATHA-PERTH) -- there the cruise
      recording simply continues undisturbed all the way to the full
      stop -- while EVERY compressed leg keeps her, exactly as
      v63/v66 made her. The gate keys on the route's own real_time
      flag, in audio_update. (2) A v73 blemish, found by listening:
      the three-second hold armed itself a frame AFTER the audio gate
      had already read the full stop, so the landing voice was cut at
      the stop itself and never rejoined for the very hold that
      promised "all sound continues". The hold now arms the very
      frame the wheels stop, BEFORE audio_update runs -- the
      touchdown roll plays out in full, right through the hold.

 v75: THE MOVING-TARGET RACE, FIXED. A captain on MELBOURNE-SYDNEY
      heard the landing voice at Merimbula and never at Sydney -- and
      the cause was a race, not a route: the v66 trigger rides 400 ft
      PLUS a lead computed from the live sink rate, so the v46 approach
      chop dances the trigger up and down by a couple of hundred feet,
      while the old crossing test compared LAST frame's height against
      THIS frame's (moved) trigger. Whenever the sink deepened between
      frames the trigger jumped UP over the descending jet, the strict
      test never registered, and the voice stayed silent the whole way
      down -- a coin toss at EVERY airport, Merimbula's by luck the
      other side of the same coin. The state machine is now explicit:
      she ARMS above the re-arm line (the ground disarms her, so a low
      departure past a high next field still cannot wake it), and an
      armed jet descending at/below the led mark starts the voice --
      the moving trigger now chooses only WHERE the file starts, never
      WHETHER it starts. The go-around re-arm, the touchdown-to-full-
      stop loop and the REAL-TIME-leg exemption (v74) are unchanged.
      Monte-Carlo on the model: every one of the Lap's thirty airports
      landed by autoland in the chop -- the voice fired at every single
      one, the takeoff roar sounded at every departure, origin and
      stopover alike, and the cabin ambience carried every mile between.

 v76: HARDLY EVER, AND FLIGHT HOURS. (1) The CAB PRESS failure clock
      re-spans: a pressurisation failure now looms once every 15-25
      SIM hours aloft -- one in twenty hours' flying on average, so
      effectively hardly ever (was every 20-70 sim-minutes). The two
      1:1 REAL TIME legs keep their standing v72 exemption: no
      failures there at all. (2) The ETA box gains a third shadowy
      readout in CLOCK_BLUE (its face one size under the two bottom
      clocks, so the figures can hold their seat between them): the
      flight's CUMULATIVE FLIGHT HOURS -- its airborne time, counted
      across every stopover leg of the flight -- in the style
      "Flight Hours: H h: MM m". It sits on the bottom line between
      the real countdown (left) and the wall clock (right); where
      that gap cannot take the whole string, the figures alone keep
      the bottom line and the words "Flight Hours" appear above the
      output, just inside the top of the box.

 v77: THREE LABELLED READOUTS, IN REAL HOURS. The captain's re-think
      on the v76 box: (1) every readout on the ETA box's bottom line
      now wears its name above the output, always -- "Real Time" over
      the countdown (left), "Flight Hours" over the flight's own
      hours (middle), "Current Time" over the wall clock (right) --
      three little captions in the same shadowy CLOCK_BLUE, just
      inside the top of the box. (2) The flight-hours figures now
      count REAL hours played, not sim hours -- the airborne clock
      converted by the leg's own time scale, so a compressed hour
      aloft counts the twenty-odd real minutes it truly took (the
      1:1 REAL TIME legs are unchanged, their sim hour being a real
      one already). (3) The figures draw at the SAME size as the
      outputs on either side -- the countdown's own tiny face; to
      make that seat always available the countdown anchors at the
      box's left inner edge now (the v45 column under the white
      ETA's leading digit retires), stepping down a size only when
      a long, late countdown genuinely crowds the middle out.

 v78: THE CAPTAIN'S FOURTH -- WELL, TWO. (1) KARRATHA-PERTH's Real
      Time readout drops its seconds: the long haul down the West now
      counts down in hours:minutes only ("2:24"), the other thirteen
      legs unchanged. (2) FLIGHT HOURS BECOME CAREER HOURS. The
      middle readout used to count only the current flight's airborne
      time, so every fresh route started again from zero. It now
      counts the TOTAL real time played over every route since
      installation: a learjet_hours.json file beside the program (the
      save file's own neighbour) banks the airborne time -- converted
      by the leg's own clock, so a compressed hour aloft counts the
      ~21 real minutes it took -- every fifteen real seconds aloft,
      at every save, and at every flight's end (landing, prang,
      abandon or quit alike). Route A flown for an hour means route B
      opens showing 1 h: 00 m; shut the computer down, fly route C
      tomorrow, and she opens showing 2 h: 00 m. The figure the box
      shows is the banked total plus the current flight's unbanked
      minutes, so the readout still ticks up live as you fly, and a
      save/load mid-flight can neither lose nor double-count a minute
      (the jet carries how much of her airborne time is banked).

 v79: THE OFFICE LINE THAT LEAKED. The v77 ETA-box line on Flying
      School's OFFICE page grew past the blue border -- the v78 career
      hours were the straw this time. The lesson is now two shorter
      lines inside the border, and the teaching names the new truth:
      the Flight Hours are every route's hours, not just today's.

 v80: THE LIVE ETA. The white ETA used to be a fixed appointment --
      the captain's-table leg budget counting down no matter how the
      ship was actually flown (KARRATHA-PERTH ran its 145 minutes out
      on final and landed twenty minutes "late" whenever she had been
      nursed along a knot slower than the reference flight). No more.
      Once she is airborne the ETA is a GHOST FLIGHT: a copy of the
      jet, taken from her present state -- distance to the tuned
      field, altitude, airspeed, vertical speed, thrust, N1 spool,
      flap, gear, brakes, fuel, heading off the course line -- and
      flown forward in fast-time with the sim's own physics and the
      sim's own control laws, down the 3-degree path and the two-step
      flare to the runway surface. The seconds the ghost needs are
      the ETA. Every setting the captain touches moves the figure
      the same second: feed her and it shortens, hang the flap and
      gear out and it stretches, drift off the course line and the
      detour is priced in, flame out and it flies the 150-knot
      best glide. With the AUTOLAND committed the ghost flies the
      autoland's own laws, so the prediction IS the plan -- on final
      approach the ETA is the truth, counting down to zero at the
      touchdown. The ghost is re-flown every couple of sim-seconds
      (and the instant any configuration changes) and the figure
      ticks down live between flights, so the clock never sits
      stale. The dim-blue REAL countdown under it reads the same
      live figure through the leg's own clock, so the two times
      still agree on the 1:1 legs. On the ground before the first
      takeoff the box keeps its old manners: the planned leg time,
      counting down from brake release.

 v81: THE TRAVELLING .EXE, HARDENED -- AND THE THOUSAND-FOOT FLOOR.
      The sim now travels to a friend's computer as ONE self-contained
      file with nothing to install and nothing to copy: build her with
      the complete v75 line (all three recordings plus the intro photo
      packed inside) and she finds everything in the bundle. A full
      headless test programme for the trip -- every one of the fourteen
      legs flown start to stop on the model, no display attached --
      turned up one real trap and made three quiet repairs. THE TRAP,
      FIXED FIRST: where the next field lies inside the offer range
      from the moment of take-off (Dunk Is. is 87 nm out of Townsville,
      Karratha 100 out of Port Hedland, Adelaide 95 out of Whyalla),
      the AUTOLAND invitation was on the table the very first airborne
      frame, and an [Y] pressed a heartbeat after liftoff engaged the
      landing law a few dozen feet up. Under sixty feet the v47
      hold-height guard does not even run -- the two-step flare put her
      in the terrain ninety-odd miles short; above it the guard held
      treetop height all the way to the field, where no safe path down
      remained. Three of the fourteen legs pranged this way under the
      test pilot, all before the fix, none after: the invitation now
      waits for a thousand feet above the field ahead -- the height
      v47's own invitation arrived at -- where holding for the beam is
      the tested, safe answer. All fourteen legs then flew green, some
      many times over. The three repairs:
      (1) THE CONSOLE-LESS PRINT: a --windowed .exe has no console, so
      sys.stdout is None and a bare print() RAISES -- caught by
      audio_init's own guard, that one raise silenced the ENTIRE sim,
      buzz included, on the very build meant for sharing. Every report
      now goes through _say(), which prints when there is a console,
      never raises when there is not, and either way appends the line
      to a tiny learjet_log.txt beside the program -- a friend can
      post it back if a recording ever misbehaves. (2) THE SPLIT
      GUARD: the cruise, takeoff and landing recordings now load each
      on their own, AFTER the synthesised voice is alive -- a codec
      hiccup in any one file can no longer take the others, or the
      bings and the buzzer, down with it. (3) THE WRITABLE SAVE: the
      save and career-hours files still live beside the program, but
      if a friend parks the .exe somewhere read-only (Program Files
      and the like) the files quietly move to a "Learjet" folder under
      the user's profile, so saving works from anywhere.

 v82: THE INTRO'S MISSING [C]. The Introduction screen now says plainly
      how to leave it: the pulsing prompt reads "Press [C] for Route
      Selection", the bottom legend reads "[T] Flying School  |  [C]
      Continue  |  [ESC] Quit", and the keys agree -- [C], [Enter] and
      [Space] all fly on (a mouse click does too), while every other
      key simply waits. And with the sim now travelling as a single
      self-contained .exe, the info line's old "run from terminal or
      double-click" is retired -- the Python roots stay proudly in the
      title bar, but nothing on the screen speaks of installing or
      running code any more: the line now reads "A complete flight
      simulator in a single file -- just double-click and fly".

 v83: THE INTRO, DRESSED. Four touches on the Introduction screen:
      (1) a tiny build tag -- v83, from the new VERSION constant --
      in the top bar's right corner, so any screenshot names the
      build. (2) The career flight hours (v78) appear under the
      credits once the first minute is banked: the pilot's logbook
      opens on the front door. (3) Whenever a saved flight exists, a
      dim "[F9] resume your saved flight" line sits under the
      legend -- and [F9] now works right here, loading straight
      into the flight, no Route Selection in between. (4) The
      legend gains "[M] Mute in flight". And the docstring's old
      "pip install pygame / Run: python ..." tail is retired: the
      sim travels as a single self-contained .exe, with the Python
      source available on request.

 v84: THE LEARJET ON THE LINE, AND THE SCREEN'S NEW VOICE. The Enroute
      screen's blinking red square is retired: a top-down photograph of
      the Learjet herself now rides the dashed route line, her NOSE TIP
      on the aircraft's live position and the airframe balanced evenly
      astride the dashes (riding above or below the line with the
      cross-track drift, exactly as the square did). The ends of the
      line cannot take the whole airframe, so she BUILDS UP from the
      nose over the first few percent of the route -- a nose sliver at
      the origin first, the tail growing out behind her -- and
      approaching the destination she dissolves away again from the
      tail forward, the nose last, so the position she reports stays
      true until she is gone. Fully in view for everything between.
      And the screen's sound changes with her: the chirping
      blink-buzzer is gone, and the cabin-atmosphere recording already
      heard on the HUD now plays while the map is up, [M] muting it as
      ever -- it is raised when the screen opens and handed back to
      audio_update on the return to the cockpit. The photograph lives
      beside the script as learjet_topdown.png (see
      ENROUTE_PLANE_CANDIDATES; pack her into the .exe with --add-data
      "learjet_topdown.png;.", already on the v75 build line). If she
      cannot be found, the old blinking red square -- and its buzzer --
      stand in exactly as before, so the screen is never left unmarked.

 v85: THREADED ON THE LINE. The captain's re-think of v84's marker: the
      Learjet now flies ON the dashed line itself -- the line threads
      in through her tail and out her nose, the dashes and the airport
      stars parting as she approaches a point on the route and closing
      again behind her, a travelling gap exactly her length. And she
      holds the line at ALL times: the v84 cross-track wander above
      and below the dashes is gone. The OFF COURSE message -- still
      posted in words when she strays -- keeps a fixed station below
      the dashes, clear of her lowest wingtip wherever along the route
      she is. (The stand-in red square, for when the photograph is
      missing, keeps its old drifting ways.)

 v86: THE DRIFT RESTORED. The captain's verdict after a think: v85's
      pinning was too honest by half -- flown off course, the marker
      should SHOW it. The Learjet once again rides above or below the
      dashed line by the cross-track error (full drift at 2 nm off),
      while keeping everything v85 brought: on course she threads the
      line, the dashes and stars parting for her tail-to-nose and
      closing again behind her. Off course the travelling gap stays ON
      the route line at her along-track station -- her shadow on the
      planned track -- while she rides at her true offset beside it.
      The OFF COURSE message keeps to the opposite side of the line
      from the airframe, placed beyond her furthest reach.

 v87: THE PILOT'S LOGBOOK. The front door now keeps the career book.
      A learjet_stats.json file beside the save and hours files (the
      v81 _writable_dir, so it travels with the .exe and survives a
      read-only Program Files) banks every flight's tale: flights,
      arrivals (hand-flown and autoland counted SEPARATELY -- an
      autoland greaser is hers, not yours, so the greaser count and
      the smoothest-touchdown record book hand-flown arrivals only),
      prangs and the arrival rate, distance flown (banked with the
      hours every fifteen real seconds aloft, so a power cut loses
      almost nothing; the figure converts to laps of the 6,294 nm
      Lap), the highest cruise, the airports visited of the Lap's
      thirty and the legs completed of its fourteen -- fly them all
      and the logbook says THE LAP IS COMPLETE in pulsing gold -- the
      favourite leg, the best crash-debrief handling rating (rated on
      every concluded flight now, not just the prangs), deadstick
      saves (tanks dry, then landed -- the v37 glide earns its medal),
      CAB PRESS failures survived (a new per-flight counter where the
      light goes out below 10,000 ft), the current clean-arrival
      streak (a prang zeroes it; an abandon or a quit leaves it be),
      and the dates of the first and last flights. Arrivals bank at
      the full stop itself, so a [C] stopover-continue counts its
      landing before flying on; the flight's own record banks at
      flight_hud's exit, whatever ended the flight. The ETA ghost is
      untouched -- she is pure floats, no Jet, and banks nothing. On
      the Introduction screen the logbook is a navy-and-gold card
      where the art used to sit (the photo still shines round its
      edges): a letterspaced header over two rows of stat cards,
      little progress bars on the airports and legs cards, and two
      record lines beneath -- shown once the first flight is in the
      book; the v83 career-hours line holds the fort until then. Old
      save files load untouched -- every new jet attribute rides
      behind a getattr default.

 v88: THE COCKPIT PHOTO PANEL. The flight HUD no longer draws on a
      dark-green glass plate: the stripped Learjet cockpit photograph
      (learjet_panel_bg.png, found beside the script/.exe or inside
      the PyInstaller bundle -- build with --add-data like the intro
      photo; the old dark glass remains as the fallback) fills the
      panel, and every instrument of the pixel-perfect panel floats
      on it as translucent blue glass, the sky ghosting through the
      boxes. The panel canvas grows from 2000x1200 to 2160x1440 --
      exactly twice the 1080x720 reference HUD and the photo's own
      3:2 aspect, so the photograph fills the canvas with no crop
      and no distortion and every element sits at twice its
      reference position. The rectangular blue border is gone: a
      hexagonal neon frame now hugs the windscreen -- its top edge
      running under the overhead panel so both dome lights keep
      their setting, the sides following the side-window posts so
      the two side windows stay balanced, the lower corners
      chamfering back out to the frame's bottom edge. The attitude
      indicator turns vivid and ghosts the sky through at one steady
      alpha; the gear lights are wired into a little tricycle
      diagram with curved green struts; the flap marker is the
      reference HUD's blue four-point star; the autopilot's ON/OFF
      box wears a red rim; the help legend is the reference HUD's
      wide ribbon of navy glass with a blue rim along the bottom
      edge. Every behaviour is unchanged -- the Mach changeover, the
      thousands graphics, the idle and spinning cells, the ETA's
      three bottom-line clocks, the brake and reverser flashes, the
      gear transit and door light, the buttons, the click mapping --
      only the glass it all floats on is new.

 v89: THE ENROUTE BACKDROP, AND SHE ARRIVES WHOLE. (1) The Enroute
      screen gains a background photograph: learjet_enroute_bg.jpg (or
      .png), cover-scaled and centre-cropped like the intro photo and
      blended over the classic dark green at ENROUTE_BG_ALPHA so the
      briefing's yellows and whites keep their footing. Same three
      homes as the other resources (hard-coded, the .exe/script
      folder, the PyInstaller bundle); if she cannot be found the
      screen wears the plain green she always has, and the load
      reports itself to the log either way. (2) The route-line
      Learjet's arrival dissolve is retired: she used to melt away
      from the tail over the last of the route until only the
      feathered nose cone was left, which read as the aeroplane
      decaying on approach -- she now carries the whole airframe to
      the destination star, her nose tip true on the position to the
      last.

 v90: THE MISSING BUILD-LINE FILES, AND THE ONE-PIXEL CROP. (1) The
      build line above gains the two photographs it never listed:
      learjet_panel_bg.png (v88's cockpit panel) and
      learjet_enroute_bg.jpg (v89's backdrop) -- both were quietly
      left behind on every PC but the captain's own, where the
      D-drive code folder supplied them. (2) The cover-scale in the
      two full-screen photo loaders could come up ONE PIXEL short of
      the screen when float truncation bit (a 1366x768 display met a
      5184x3456 photograph); the centre-crop then raised and the
      loader fell silently back to the plain fill. Both loaders now
      scale a pixel to spare and clamp the crop. (3)
      learjet_enroute_bg.jpeg is a welcome name too.

 v91: THE DOUBLE-WRITING FIX. The Enroute screen's doubled text was
      never the sim drawing twice: every screen repaints the whole
      surface each frame, so an old frame cannot persist inside the
      app -- the laptop's panel was showing the current frame PLUS a
      scaled, stale copy of an older one composited over it (the
      copies' offsets grow toward the screen edges: a scaled
      duplicate about the screen centre, not two draw positions).
      The trigger is the page-flipped FULLSCREEN path through the
      graphics driver's fullscreen optimizations, with a dual-screen
      different-DPI desk as the classic stage. The sim now opens a
      NOFRAME window at the desktop size instead (identical full-
      screen look, but the window is presented normally, so no stale
      buffer can be scaled over the frame), and the DPI-awareness
      call is finally VERIFIED -- its return code was never checked,
      so a failed call used to leave Windows silently scaling the
      game's output on scaled displays. The state reports to
      learjet_log.txt: a friend's machine can be diagnosed from the
      log alone. If a captain insists on the old FULLSCREEN path,
      the exe's Properties > Compatibility > "Disable fullscreen
      optimizations" is the per-machine alternative.

 v92: THE DOUBLE IMAGE, FOUND AT LAST -- AND IT WAS NEVER THE CODE.
      The proof came from the captain's own photograph of the screen:
      the ghost carried TWO states no single frame can hold ("Press any
      key to taxi onto the runway" from the pre-flight briefing AND
      "Press any key to return to the cockpit" from the mid-flight [V]
      peek), and the ghost's glyphs were LARGER than the live ones --
      the signature of a picture scaled up to cover the screen, wider
      apart the further from the centre. The Enroute screen's backdrop
      on the stricken machine is not a photograph of clouds at all: it
      is a SCREENSHOT of this very screen, taken mid-peek (the Learjet
      near arrival, the cockpit prompt on her), travelling under the
      photograph's name. Every frame the sim faithfully blits that
      backdrop -- writing and all -- then draws its live writing on
      top; no repaint logic, buffer change or DPI fix could ever wash
      her out. (1) The fix is a file, not code: a clean cloud
      photograph travels with this build -- let her replace the
      impostor wherever the log says the backdrop loaded from. (2) The
      loader now logs the backdrop's size beside her path, and murmurs
      in the log when she has the shape of a screenshot rather than a
      camera photograph (16:9-ish, no taller than a display). (3) A
      kill-switch: an empty learjet_enroute_bg.off beside the program
      retires the photograph to plain green -- if the doubling dies
      with her, the picture was the ghost, proven in half a minute.

 v93: THE CAPTAIN'S PHOTOGRAPH, MATCHED. Three restorations, every
      one measured off the captain's own photograph of the classic
      bottom-left panel.
      (1) THE CDI'S NAMEPLATE: "Course Deviation Indicator" used to
      shout in the big label face, sprawling well past both ends of
      its gauge (and centred off it besides). It now wears its own
      smaller face, fitted to the track's width and centred exactly
      over the needle's travel.
      (2) THE LOWER-LEFT REGISTER, REBUILT: the yellow block is the
      castle-profiled original again -- START and F/F as raised tabs
      with the dark spinning-cell bays beside and between them, the
      full-width field below carrying AUTO PILOT: / FUEL: / VSI:, the
      right column running unbroken from F/F down through LB and FPM
      with all three right-aligned on the one edge, and the INFO: tag
      continuing the left column one row below the field. The block
      hugs the DME row above and stretches from the IAS/DME column's
      left edge to the ALT/GROUND SPEED column's; the figure cutout
      steps in to hug the FUEL: and VSI: labels individually; the
      rows tighten to the photograph's pitch. The autopilot's ON/OFF
      flag loses its red picture frame: the yellow box now stands
      BETWEEN two detached red guard bars, a dark gap either side,
      centred on the AUTO PILOT line. And the STALL pill is solid
      panel blue again, the data boxes' own fill, not glass.
      (3) THE THRUST LEVER'S MANNERS: [+] and [-] now step ONE point
      a press (was five), and a held key keeps winding a point at a
      time -- after the usual short pause, then a point every 100 ms
      -- until the key comes up, on the same hold-to-repeat machinery
      the [A]/[D]/[W]/[S] keys use (keypad +/- included). The lever's
      disciplines are untouched and now shared by press and hold
      alike in the one thrust_step(): no engines, no thrust (v26);
      the CHECK HEADING gate (v24); the takeoff roar at 100% (v62).

 v94: THE CAPTAIN'S PHOTOGRAPH, MATCHED AGAIN -- six more fittings,
      all measured off the bottom-right photograph.
      (1) THE TOP ROW'S MARGIN: STALL, 1, 2 and CAB PRESS now wear
      their own smaller face (a size down from the panel face), so a
      thick margin of box stands all round the letters -- the text no
      longer fills its pill.
      (2) THE R/TH GUARD SQUARES: reverse thrust's red squares now
      stand either side of the R/TH label on its own row, below the #
      detent marks -- steady red on stand-by, flashing red-yellow on
      the half-second cadence for as long as the buckets are out.
      (3) THE BLANK THRUST SQUARES: the squares that ride the purple
      bars are EMPTY blue frames now -- nothing inside -- the pair of
      them moving up and down together with the lever to mark the
      thrust selected. The # marks stay home at the 0% line either
      side, the idle detent, drawn over the squares so they show at
      every setting.
      (4) THE GEAR STEM RETIRED: the little down-stem and arms under
      the top green square are gone -- three plain green squares,
      nose and mains, and the *D door light, nothing more.
      (5) THE FLAP MARKER: the blue four-point star is retired. The
      selected setting is an ORANGE square on the bar, clamped flush
      to the bar's own ends at the 0 and 50 gates, with the blue
      asterisk centred in the middle of the square -- centred by its
      ink, so the star sits truly central.
      (6) THE BR GUARD BARS: the brake flag is the AUTO PILOT flag's
      v93 style turned upright -- the yellow ON/OFF box stands BETWEEN
      two detached red bars, a dark gap either side, all three the
      one width, exactly as the photograph shows.

 v95: THE STRUT CLOCK, TICKING. The clock on the centre window strut
      was a photograph of a clock -- frozen at whatever o'clock it was
      when the camera shutter fell. Now it is a clock: real local
      time, the same wall clock as the Current Time readout in the
      ETA box, with hour and minute hands and a sweeping red second
      hand, redrawn every frame. It stands between the 1 and 2 boxes
      on their own eyeline, dead centre on the strut, and it keeps on
      ticking while the sim is paused -- the pause freezes the jet,
      not the world. STRUT_CLOCK_CX, STRUT_CLOCK_CY and STRUT_CLOCK_R
      set its place and size, should the photograph want it nudged a
      pixel or two.

 v96: THE STRUT CLOCK, SEATED ON ITS PHOTOGRAPH. The cockpit photograph
      itself arrived (learjet_panel_bg.png), so the clock's place and
      size are measured now, not guessed: centre (1086, 347), rim
      radius 43 -- panel coordinates, 2x the photograph, where the
      frozen clock's own rim reads photo (543, 173.5), radius 20.5.
      The working clock swallows the photographed one whole -- the
      cradle mount above and below still holds it -- and wears its
      livery: a near-black rim, an ivory dial, black ticks and black
      hands.  v95's panel-blue face was only a stand-in until the
      photograph could be consulted.

 v97: THREE LAST FITTINGS BEFORE CLOSING TIME. (1) THE YELLOW HAIRLINE
      SHAVED: the register block's field reached 3 pixels below the VSI
      cutout's floor, and that sliver read as a thin yellow line running
      right to the F/F column's far edge between the VSI and INFO rows.
      The field now ends flush with the cutout, the F/F column with it,
      and the INFO tag butts up beneath -- no line. (2) THE THRUST
      MARKERS ARE BLANK SPACES: the selected level is a square notch in
      each purple bar where the bar is simply not painted, so the
      photograph's own detail shows clean through, the pair riding up
      and down with the lever -- v94's blue-framed squares are retired;
      the marker is the absence of bar. (3) THE DARK GEAR SQUARES FADE:
      with the wheels raised, the three squares (and the *D door
      placeholder) are a faint grey ghost, barely seen against the
      photograph, not the near-black slabs they were.

 v98: THE WINDSCREEN'S BLUE LINE, RETIRED. The thin bright-blue frame
      that ringed the panel -- the top edge running under the overhead
      panel, the sides sloping in along the side-window posts, then
      chamfering back out to the bottom corners -- is gone. The
      photograph frames itself; the gauges float on it bare. FRAME_PTS
      and FRAME_BLUE go with it.

 v99: THE THRUST FIGURES, STRAIGHTENED UP. The 0% mark now right-
      aligns, its unit standing squarely beneath the 100% mark's unit
      instead of drifting left of the column; it still never moves and
      still always reads 0%. The live percentage has moved house from
      beneath the 100% down to the space just above the 0%, counting up
      and down as the throttle keys are worked, the blank spaces in the
      purple bars riding alongside the figure all the way to 100% and
      back down again. At the two ends the fixed marks do the talking
      and the live figure stays extinguished, exactly as before.

 v100: THE THRUST GAUGE, TRUED UP. The right-hand purple bar's left
      edge now falls in line with the down stroke of the last T of
      THRUST, and the 100% mark's crown sits flush with the tops of
      both bars. The yellow # marks no longer stay home at the 0%
      line: they ride INSIDE the blank spaces either side of the
      thrust figure, showing at the setting currently held, resting at
      the 0% line only when the levers are closed. The blanks
      themselves still travel their three spaces between the marks.

 v101: THREE LINES FOR THE THRUST. The level now reads as three
      stacked lines -- 100% on the top line, the live 1% to 99% figure
      on the middle line, 0% on the bottom -- the readout no longer
      hugging the foot of the scale but holding the centre between the
      fixed marks. The # marks keep riding inside the blank spaces,
      top to bottom with the percentage.

 v102: THE THRUST GAUGE'S HONEST FACE. A photograph of the parked
      cockpit -- engines OFF, lever CLOSED, brakes on -- showed a bold
      white "100%" under the THRUST title, with the ITT boxes reading
      0015 and 0064: the very picture of full power on dead engines.
      Two things were lying. First, the gauge's FIXED top-of-scale
      mark: drawn big and white since the gauge was born, it read as
      the live lever setting, and with the live figure extinguished at
      the ends (v101) nothing on the scale contradicted it. The panel's
      own grammar now holds here -- yellow for fixed legends, white
      only for live readings: the 100% and 0% marks wear the small face
      in panel yellow (the 100% crown still flush with the bar tops,
      the 0% still at the foot), and the big white live figure burns at
      EVERY setting, 0 and 100 included, on the centre line between the
      marks, right-aligned on their edge as ever. The largest digits on
      the gauge now always speak for the lever; the # marks and the
      blank bar notches ride it unchanged. Second, engine 2's ITT: the
      old x0.95+50 split put a fantasy +49 degrees between the twins at
      idle (the 0015 / 0064 in the photograph), the +50 swamping the
      scale on cold engines. She now runs a steady two degrees hotter
      than her sister, all the way up the dial.

 v103: THREE WHITE LINES FOR THE THRUST. The captain's ruling on the
      thrust gauge, flown and found wrong: the level reads as THREE
      stacked lines again (v101), SINGLE-SPACED one line pitch apart
      (the 0% mark leaves its foot-of-scale perch and closes up under
      the live figure -- the old spacing left a three-line void
      between the marks) -- the fixed 100% on the top line,
      the live figure on the middle line for 1% TO 99% ONLY, and the
      fixed 0% on the bottom line. At the two ends the middle line is
      extinguished and the fixed marks do the talking: the top line
      never reads anything but 100%, the bottom line never anything
      but 0%, and no figure is ever printed twice. And ALL THREE
      figures wear the big white panel face now -- the fixed marks
      included, v102's small yellow legends retired by order. The
      blank spaces in the purple bars ride with the lever exactly as
      before -- parked level with the 0% line at idle, climbing with
      every point wound on, arriving at the 100% line at full thrust,
      and back down again as the lever comes off -- the # marks riding
      inside them, unchanged. v102's second fix stands: engine 2 still
      runs her steady two degrees hot.

 v104: THE GEAR CLUSTER, TWO ROWS LOWER. The whole undercarriage
      assembly -- the yellow GEAR label bar, the three green squares
      (nose above, the two mains below) and the *D door light -- rides
      TWO ROWS down, at the register's own row pitch (2 x 48 = 96 px),
      by the captain's order. One knob: GEAR_DROP, in the GEAR section.
      The cluster's layout within itself is unchanged, and it clears
      the R/TH guard squares above it with room to spare.

 v105: NO PURPLE BELOW THE 0% LINE. With the v103 stack closed up, the
      thrust gauge's two purple tracks still ran on down to the old
      foot of the scale, a hundred pixels of bar hanging beneath the
      bottom line. Both bars now END flush with the foot of the 0%
      mark's ink: the tracks frame exactly the three lines of the
      scale -- the 100% crown at the top, the 0% foot at the bottom --
      and no purple shows below 0% on either side, by the captain's
      order. The blank squares and # marks ride the shortened tracks
      unchanged: parked at the 0% line they sit at the very foot of
      the bars, at full thrust at the very crown.

 v106: THE BAR TOPS, BACK ON THE 100% CROWN -- AND THE GEAR UP A ROW.
      (1) The v105 bottom-setter had the bars RISING ABOVE the 100%
      mark: assigning to a pygame Rect's "bottom" SLIDES the whole
      rectangle with its height unchanged, so the tracks' tops came
      off the 100% crown. The bars are RESIZED now (height set, tops
      unmoved): they start flush with the top of the 100% and end
      flush with the foot of the 0%, framing the three lines exactly.
      (2) The GEAR assembly rides back UP one row: the v104 drop was
      two register rows; the net drop is now one (GEAR_DROP = 1 * 48).

 v109: THE STANDING CELLS, AND GLASS FOR THE FIGURES. (1) The
      checkered rectangles by START stand in their bays at ALL times
      now: parked in the standing pattern before the engines are
      started -- until now the bays were bare dark glass before [E],
      so the rectangles looked missing -- then spinning exactly as
      before, the pair on the left rapid to liftoff, the four between
      START and F/F slow for the whole flight. (2) The FUEL: and VSI:
      figures read off the CAB PRESS near-clear glass now -- the
      near-opaque dark cutout behind them is retired, the photograph
      ghosting through behind the numbers -- and the cut_fill recipe
      retires with it (v16's tidy rule).

 v108: THE START TAB, SET BY THE PHOTOGRAPH. v107's reading of the
      order was the wrong track -- START had gone hard right against
      the F/F column and the four slow cells were retired with their
      bay. The captain's photograph settles it: the yellow bar under
      START runs tightly from the 'S' to the final 'T' -- ink-tight,
      no yellow side margins -- the 'S' stands directly above the 'T'
      of AUTO and the final 'T' directly above the 'I' of PILOT, the
      word occupying character columns 2-6 of the register's monospace
      line; and the four slow-flipping cells between START and F/F
      stay EXACTLY as they were, bay and all. The two rapid cells on
      the left keep the point of the order: the yellow trimmed from
      the old tab's left overhang widens their bay, so they spin
      unsquashed. The rest of v107 stands: the glass panel, the
      raised ATT IND.

 v107: THE CAPTAIN'S PANEL ORDERS, THREE. (1) THE START TAB, HARD
      RIGHT: the two spinning graphics left of START were squeezed
      into a 29-pixel slot. START now sits hard over to the right,
      flush against the F/F column, and the dark cell bay stretches
      the whole way from the windscreen post to the tab -- the two
      graphics fill it at four times their old width, with room to
      spin, unsquashed. The four slow cells between START and F/F are
      retired: with START hard right their bay is gone. (2) THE GLASS
      PANEL: STALL, HDG, OBS, IAS, ALT, ASS FL, DME( ), GROUND SPEED,
      ETA and the COURSE DEVIATION INDICATOR track now wear the CAB
      PRESS near-clear glass -- the photograph ghosts through them
      all, exactly as it does through CAB PRESS (the 1 and 2 engine
      boxes were that glass already, and keep it). STALL still
      flashes red while she is stalling; the rims, the unit badges,
      the figures, the dots and the needle are unchanged, and nothing
      else on the panel changes -- the G/S tape, the FLAP bar, the
      THRUST tracks, the GEAR cluster, BR, ITT and the yellow register
      block keep their look, by order. The SKY_FILL and NAVY_FILL
      glass recipes (and the long-dead NAVY_BORD) retire with the
      change (v16's tidy rule: a colour nothing references is gone). (3) THE ATT IND, ONE
      ROW UP: the nameplate and the attitude gauge ride one register
      row higher (48 px), the gauge's top now level with the THRUST
      title.

 v110: THE SECONDARY LEVER, AND THE SHIFT RAM. The thrust lever gains a
      second pair of hands: the Up/Down arrow keys drive the very same
      lever, one point a press with the same hold-to-repeat cadence --
      a secondary control for whichever hand is free. And Shift held
      with [+] is the RAPID increase: RAPID_THRUST_STEP points a press
      (twenty-five, as shipped), so the lever runs from idle to full
      thrust in four presses. Press, hold and ram alike still come
      through the one thrust_step(), so every discipline holds: no
      engines, no thrust
      (v26); the CHECK HEADING gate (v24); the takeoff roar at 100%
      (v62), reverser work included. Shift is read LIVE, so it can be
      pressed or released mid-hold and the lever changes gear on the
      spot. The unshifted [=] and the keypad's [+] keep the one-point
      fine control, and [-] keeps its one-point manners, Shift or no
      Shift. One knob: RAPID_THRUST_STEP.

 v111: THE REGISTER, ONE ROW DOWN -- AND NAVY FOR THE ETA'S SHADOWS.
      (1) The whole lower-left register rides ONE ROW down, at the
      register's own 48 px pitch (the same step the GEAR cluster's
      GEAR_DROP uses), by the captain's order: the START and F/F tabs,
      the spinning-cell bays, the AUTO PILOT: / FUEL: / VSI: field and
      its white figures, the autopilot's ON/OFF flag with its red guard
      bars, the AUTOLAND placard, and the INFO: tag with its line all
      keep their places WITHIN the block -- the block itself drops.
      One knob: REGISTER_DROP, in the register's section. The DME /
      GROUND SPEED / ETA row above stays put, so the block no longer
      hugs it, and the CDI keeps its station exactly where it was.
      (2) The ETA box's shadowy readouts -- the Real Time / Flight
      Hours / Current Time captions along the top edge and their three
      little clocks along the bottom -- trade the v44 dim light blue
      for the DARK NAVY of the bottom key ribbon's glass, by the
      captain's order. CLOCK_BLUE now IS the ribbon's blue, and the
      ribbon fills from the same constant, so the two can never drift
      apart.

 v112: A SEAT FOR THE ETA'S SHADOWS. The v111 navy told the truth but
      vanished into the cockpit photograph -- the key ribbon gets away
      with that navy because there it is the BACKGROUND, with white
      writing on top; as INK over the near-clear photo glass it had no
      contrast. The six shadowy readouts -- the Real Time / Flight
      Hours / Current Time captions and their three clocks -- now sit
      on a faintly FROSTED seat, a pale glass pill hugging each line
      the way the NM and MIN badges hug theirs, so the captain's navy
      reads clean against any sky while the clocks keep their
      whisper-quiet manners. The navy itself is unchanged -- still the
      ribbon's own (8, 26, 110), one constant serving both. One knob:
      ETA_INFO_FROST -- raise the alpha for a firmer seat, lower it
      toward the old bare glass.

 v113: AMBER FOR THE ETA'S SHADOWS. The captain's re-think on the v111
      navy: out it goes. The six shadowy readouts -- the Real Time /
      Flight Hours / Current Time captions and their three clocks --
      now wear a DIM AMBER (190, 148, 52). Full gold was on the table
      and reads anywhere, but on this panel yellow is the LABEL colour
      -- the ETA nameplate, the MIN badge, DME / GROUND SPEED -- and
      gold captions would have read as three more titles, shouting
      against the white ETA figure. The dim amber stays visibly junior
      to the big white readout, warm against the photograph, and
      honest aircraft-panel language for a secondary readout. The
      v112 frosted seat is PARKED, not deleted: it was built to rescue
      a DARK ink, and a pale seat under the amber washed out
      light-on-light (seen on the mock) -- so ETA_INFO_FROST ships at
      alpha 0 and the bare amber reads on its own. Raise the alpha
      toward 128 if a bright sky ever swallows a readout. One ink, one
      constant: ETA_INFO_INK. CLOCK_BLUE retires with the navy (v16's
      tidy rule), and the key ribbon keeps its navy as a literal of
      its own -- the v111 tie between them is no longer needed.

 v114: THE SHY AMBER. The captain's ruling on the ETA box: the six
      shadowy readouts must NEVER be dominant -- barely discernible,
      with the big white Estimated Time of Arrival always the main
      detail seen. (The v111 navy had failed the other way --
      invisible entirely; v113's full-voice amber still argued with
      the ETA.) The fix keeps the amber hue and turns its voice
      down: the six readouts now blit at a dimmed text alpha, fading
      toward the cockpit photograph instead of sitting on top of it.
      Mocked true-alpha over the photo, three notches: 255 = v113's
      full voice, clearly readable and arguing with the ETA; 150 =
      shipped SHY, there when you look for it; 115 = ghost, near the
      navy's fate. One knob: ETA_INFO_DIM.

 v115: HALF-INTENSITY YELLOW FOR THE SHADOWS. The captain's report
      on v114: "can't see a thing." True enough -- the shy amber's
      alpha-dimmed strokes, already tiny at the 0.5 panel-to-screen
      scale, faded into the photograph altogether. So the captain's
      experiment: the panel's own label yellow at HALF INTENSITY,
      (128, 128, 0), opaque. The dimming moves out of the alpha and
      into the colour itself, so the little strokes land at full
      strength and READ, while the hue stays visibly junior to the
      big white ETA and a full step below the nameplate's yellow.
      Mocked over the photo, five notches: amber @150 (v114,
      invisible); half yellow (shipped); yellow @ half alpha (the
      other half -- a touch washed); three-quarter yellow (the
      notch above, if more is wanted); full yellow (the label's
      own voice -- shouts). ETA_INFO_DIM parks at 255, kept as the
      fade knob for any future bright ink.

 v116: THE BADGE SEATS -- THE OLD RECIPE, REBORN. The captain's
      report on v115: "Nothing to see. I see nothing." -- and the
      memory that unlocks it: "It worked well when the faint blue
      text appeared on a dark blue background." Of course it did:
      before v88 the data boxes were opaque dark blue glass, and the
      v44 shy blue (70, 105, 175) sat on that calm navy like writing
      on a chalkboard. Since v88 the boxes are near-clear glass, and
      every bare ink tried since -- navy, amber, half yellow --
      fought the photograph ghosting through: dark inks die on dark
      patches, light inks die on glare, and alpha-dimmed tiny
      strokes die everywhere. The fix is not another ink but the
      background itself, in miniature: each of the six readouts now
      sits on a small NAVY BADGE pill -- the key ribbon's own recipe
      (navy band, light writing), hugging its line the way the MIN
      badge hugs its figures -- with the v44 dim light blue restored
      as the ink, opaque. Faint blue on dark blue, exactly as the
      captain remembers; always junior to the big white ETA, and now
      impossible for the photograph to swallow. Mocked over a
      backdrop half shadow, half glare: bare inks vanish in the
      glare; the badge seats read through both. Two knobs:
      ETA_INFO_SEAT (alpha 0 parks the pills) and ETA_INFO_INK
      (brighter notches ready: (110,150,215), (170,195,230)).
      ETA_INFO_FROST retires into ETA_INFO_SEAT (v16's tidy rule).

 v117: THE CANARY. Four inks in a row have reported back "nothing
      to see" -- navy, amber at full voice, half yellow, and the
      v44 shy blue on navy badge seats. On the black top edge the
      captain describes, the v113 full-strength amber could not
      have hidden -- so suspicion turns from the ink to the
      plumbing. Two temporary witnesses ship with this build. (1)
      The ETA nameplate reads "ETA v117": if the panel still shows
      a plain "ETA", an OLD BUILD is flying -- the .exe must be
      rebuilt from the new source (the v75 PyInstaller line) or the
      freshly downloaded .py run in place of an older copy; the
      intro screen's tiny build tag tells the same story. (2) The
      six shadowy readouts wear UNMISSABLE bright green on their
      navy badge seats. One standing condition: the whole ETA
      register sleeps behind its diagonal cells until the engines
      are started with [E] -- as it has since long before these
      changes -- so the canary can only sing with engines running.
      If the nameplate reads v117 and the white ETA and MIN badge
      are showing yet no green lines appear, the fault is inside
      the block itself, and a screenshot of the ETA box will find
      it. The v116 recipe -- shy blue (70,105,175) on navy seats --
      is parked one line away in ETA_INFO_INK, ready to restore the
      moment the canary has sung.

 v118: THE CANARY HAS SUNG. The captain's own pre-flight found the
      fault: the engines had never been started -- and the whole
      ETA register, shadowy readouts included, sleeps behind its
      diagonal cells until [E] fires them, as it has since long
      before these changes. Every ink since v111 was very likely
      fine; there was simply nothing awake to see. The witnesses
      stand down: the nameplate is plain "ETA" once more, the
      diagnostic green retires, and the v116 recipe ships as
      intended -- the v44 shy blue (70, 105, 175), opaque, on the
      navy badge seats: faint blue on dark blue exactly as the
      captain remembers it, always junior to the big white ETA.
      The seats stay on -- they are the guarantee that no patch of
      photograph can swallow the lines again. Brighter notches
      ready in ETA_INFO_INK: (110,150,215), then (170,195,230).

 v119: THE ROUTE SCREEN'S POSTCARD. The Route Selection screen gains
      a background photograph: learjet_route_bg.jpg (or .jpeg/.png) --
      the "Greetings from Sydney" postcard -- cover-scaled and centre-
      cropped like the intro photo and blended over the classic dark
      green at ROUTE_BG_ALPHA so the gold title and the white hints
      keep their footing. Same three homes as the other resources
      (hard-coded, the .exe/script folder, the PyInstaller bundle --
      pack her in with --add-data "learjet_route_bg.jpg;."). If she
      cannot be found the screen wears the plain green she always has.

 v120: THE GLASS PANEL. The Route Selection screen's solid green
      fills are gone: a TRANSLUCENT pane of the classic BOX_GREEN now
      lies over the postcard -- the photograph shows through her at
      full strength (ROUTE_BG_ALPHA 255) -- and every line of writing
      carries a soft dark shadow, so the golds and yellows keep their
      footing anywhere on the picture, sky, sign or sea. The route box
      keeps her blue border: a picture frame round the fourteen legs.
      Two knobs: ROUTE_GLASS_ALPHA is the pane's opacity out of 255
      (0 retires her to bare glass, 255 is the old solid panel), and
      ROUTE_TEXT_SHADOW is the shadow's offset in pixels (0 = none).

 v121: THE AIRPORT COUPLE, AND THE GLASS RETIRED. The Route Selection
      screen's backdrop is now the sunset silhouette of the couple at
      the airport, sunburst and all (learjet_route_bg.jpg -- same file
      name, so the build line and the three homes are untouched). And
      the translucent pane is gone with her: ROUTE_GLASS_ALPHA 0 means
      every line of writing -- the gold title, the fourteen yellow
      legs, the white hints -- sits DIRECTLY on the photograph, only
      the soft dark shadow (ROUTE_TEXT_SHADOW) beneath each line
      keeping the letters legible against sky and sunburst alike.
      The route box keeps her blue picture frame.

 v122: FIVE OF THE CAPTAIN'S ORDERS, ONE FLIGHT. (1) The landing
      voice starts AT the 400 ft mark: LANDING_LEAD_S retires to
      0.0 -- the seventeen-second head start had the recording
      open, finish and loop four times through before its proper
      cue. (2) The ETA box wears the captain's colour photograph:
      the white ETA and the yellow MIN badge already matched it,
      and the bottom line's ink is now the photograph's pale sky
      blue (ETA_INFO_INK 130,170,250) on BARE glass -- the navy
      badge seats are parked (ETA_INFO_SEAT alpha 0; the photo
      shows none). (3) The R/TH label and its two red guard squares
      ride up to the purple thrust bars -- the squares' tops a
      millimetre below the bars' feet, the label balanced between
      the squares' top and bottom by its INK, not its glyph cell.
      (4) The yellow GEAR label lifts to one register row below the
      guard squares' bottoms; the three green squares and the *D
      door light keep their places. (5) The register from START to
      INFO: loses a quarter of its transparency -- the parked-cell
      bays to alpha 203, the FUEL / VSI panes to a local 109 --
      while TOP_FILL, worn panel-wide, stays untouched and the
      register's yellows, opaque already, do not move.

 v123: THE ETA BLUE, AND THE GEAR SQUARES RAISED. By the captain's
      order: the ETA box wears the colour photograph's nice vivid
      blue (ETA_BOX_BLUE 5,49,245) SOLID -- the big white ETA and
      the MIN badge up top and the pale sky-blue bottom line all
      sit on it now, exactly as the photo shows (the near-clear
      glass is retired for this one box; every other data box
      keeps it). And the three green gear squares rise to a
      millimetre below the GEAR label bar -- the R/TH squares' own
      physical millimetre -- the top square's middle centred
      exactly on the word GEAR; the bottom pair and the *D door
      light keep the formation. GEAR_DROP is retired (v16's tidy
      rule: a knob nothing references is gone).

 v124: THE ETA BLUE AS BANDS. The captain's clarification of v123:
      the ETA rectangle itself goes back to the near-clear glass
      every data box wears -- the photograph's nice vivid blue
      (ETA_BOX_BLUE) now appears ONLY directly behind the messages,
      and only the thickness of the messages: one band hugging the
      big white ETA and its MIN badge up top, one band under the
      bottom line's three readouts. The rest of the rectangle is
      clear again, just like the photo. (The box's own fill is
      TOP_FILL once more; the data_box fill parameter, added and
      used only by v123, is retired with it.)

 v125: THE BLUE COMES OUT FROM BEHIND THE HOURS AND MINUTES. One
      spot in the ETA rectangle still wore the vivid blue where the
      captain wanted clear glass: behind the FLIGHT HOURS figures
      on the bottom line -- the hours and minutes themselves. The
      bottom band is split in two: one pill hugging the countdown
      at the left edge, one hugging the wall clock at the right,
      each the thickness of its own message. The career hours
      between them, and every gap, sit on the clear glass.

 v126: THE NEW COCKPIT PHOTOGRAPH, AND GEAR ON THE R/TH CENTRELINE.
      (1) The HUD's background photograph is replaced with the
      captain's new cockpit photo -- still learjet_panel_bg.png
      beside the script/.exe, centre-cropped to the panel's 3:2
      so it fills the canvas true, with no stretch. The loader,
      the name and the .exe build line are all unchanged. (2) The
      yellow GEAR label -- bar and word together -- now centres on
      the R/TH label's own centreline, the midpoint between the two
      red guard squares either side of R/TH, instead of the panel's
      old 1851. Nothing else moves: the bar keeps its row and its
      size, and the three green squares and the *D door light keep
      their seats exactly as before (the top square's centre is
      pinned, no longer read from the bar).

 v127: THE BLUE OUT FROM BEHIND MIN AND THE WALL CLOCK. The
      captain's eye caught the vivid ETA blue in two more places:
      running THROUGH the word MIN and slightly beyond it (the top
      band's tail past the badge), and under the HH:MM wall clock
      at the bottom right. Both are out. The top band now hugs the
      white ETA figures alone and ends before the badge, so MIN
      sits on the bare glass; and the wall clock's pill is retired,
      so HH:MM reads on glass exactly like the hours and minutes
      beside it (v125). The white ETA keeps its band, and the
      countdown keeps its pill at the left edge.

 v128: THE LAST OF THE TOP-LINE BLUE. One step further on the
      captain's order: after v127 took the band's tail through
      MIN, the big white ETA itself -- the HH:MM reading, or the
      --:-- of no estimate -- still wore the vivid blue band.
      The band is retired outright: the white figures now read
      on the bare glass, the MIN badge clear beside them. The
      countdown's little pill at the bottom left is the ETA
      box's last blue.

 v129: THE ETA BOX, BANDED TOP AND BOTTOM. The captain's re-think
      on the bare-glass bottom line: the vivid blue returns as TWO
      full-width bands -- one spanning the ENTIRE bottom of the box
      behind all three readouts (countdown, flight hours and wall
      clock, all in the paler blue), one spanning the top behind
      the three captions. Each band hugs its line's INK by 4 px
      top and bottom and is fitted 2 px inside the inner white rim
      on every side -- the rim's inner edge stands 10 px in from
      the box (6 px inset plus its 4 px stroke) -- corners rounded
      inside the rim's own, never encroaching on the white. The
      bottom line rides 3 px lower so the band's top edge clears
      the MIN badge above by 2 px.

 v130: THE NEW COCKPIT PHOTOGRAPH, AND THE GEAR SQUARES UNDER THE
      WORD. (1) The HUD's background photograph is replaced with the
      captain's new cockpit photo -- still learjet_panel_bg.png beside
      the script/.exe, centre-cropped to the panel's 3:2 so she fills
      the canvas true, with no stretch; the loader, the name, the
      build line and every HUD element are exactly as they were.
      (2) The top green gear square's middle now lines up under the
      E and A of the word GEAR -- the label bar's own centreline --
      the bottom pair and the *D door light moving with it in
      formation; the v126 pin at the label's old 1851 retires.

 v131: THE FULL-SCREEN HUD. The flight HUD was the one screen that did
      not fill the display: the 2160x1440 panel scaled to FIT inside
      the window (and never up), centred over black -- so every
      widescreen display wore thick black bars down both sides while
      the Introduction, Route Selection and Enroute screens all ran
      edge to edge. The panel now takes those screens' own treatment:
      scaled to COVER the whole screen and centre-cropped, the cockpit
      photograph and every instrument on her scaling TOGETHER as one
      picture, so nothing on the panel moves relative to anything
      else. On a 16:9 screen the panel stands about a sixth LARGER
      than before and the crop takes only the photograph's top and
      bottom margins -- every box, gauge, placard and button stays on
      screen (the top boxes begin 242 px down; the INFO line ends well
      above the bound). The help legend, still drawn at native
      resolution after the scale, now seats itself above the SCREEN'S
      bottom edge instead of the panel's, whose bottom edge now lies
      below the display. The crop is bounded (PANEL_SAFE_CROP_X / _Y)
      so an unusually shaped screen can never crop into the furniture
      -- there the panel simply holds at the bound and centres,
      exactly as it used to -- and the mouse-click mapping reads the
      same fit figures, so the buttons land exactly where they are
      seen.

 v132: THE COMPLETE PACKING LIST, FOR FRIENDS OVERSEAS. The build line
      above gains learjet_route_bg.jpg -- the Route Selection
      screen's backdrop (v119) never made the v75 list, so a packed
      .exe quietly lost the postcard on every machine but the
      captain's own, where the D:\code folder supplied it unseen
      (the very trap v75 named for the sounds). And the code folder
      gains build_exe.bat: double-click it and it checks that every
      photograph and recording is present, packs them ALL into the
      one .exe (the .jpeg/.png and .mp3 alternates included), and
      reports plainly what it did. The single file in dist\ is the
      whole simulator -- post it to a friend as it is, with nothing
      else to copy and nothing left to go wrong.

 The flight HUD is the v88 cockpit photo panel: the user's
 pixel-perfect panel recreation as translucent blue glass over the
 stripped cockpit photograph, wired to live flight physics.

 Distribution: a single self-contained Windows .exe, built with
     PyInstaller (see the v75 build line above). The Python source
     is available on request.
======================================================================
"""

import pygame
import sys
import math
import os
import json
import array
import random
import time     # the wall clock in the ETA box (v55)

# ----------------------------------------------------------------------
#  SAFE REPORTING (v81) -- a --windowed PyInstaller .exe has NO console:
#  sys.stdout is None there, and a bare print() RAISES. Inside
#  audio_init() that single raise was caught by the outer guard and cost
#  the sim its ENTIRE voice -- every sound, buzz included, on the very
#  build meant for sharing. _say() can never raise; it also keeps a tiny
#  load-report log beside the program, so a friend two thousand
#  kilometres away can simply post the file back if a recording ever
#  misbehaves.
# ----------------------------------------------------------------------
_LOG_PATH = None


def _say(msg):
    """Print to the console when there is one; never crash when there is
    not. Either way the line joins the little log file."""
    try:
        print(msg, flush=True)
    except Exception:
        pass
    global _LOG_PATH
    try:
        if _LOG_PATH is None:
            _LOG_PATH = os.path.join(_writable_dir(), "learjet_log.txt")
        with open(_LOG_PATH, "a", encoding="utf-8") as f:
            f.write(str(msg) + "\n")
    except Exception:
        pass

# ----------------------------------------------------------------------
#  COLOUR PALETTES
# ----------------------------------------------------------------------
SKY_BLUE    = (135, 206, 235)
DARK_BLUE   = ( 45,  85, 145)
WHITE       = (255, 255, 255)
DARK_GREY   = (100, 100, 115)

BG_GREEN      = ( 34,  85,  51)
BOX_GREEN     = ( 42,  95,  59)
BORDER_BLUE   = ( 50, 100, 200)
BOX_YELLOW    = (255, 215,  60)
BOX_RED       = (220,  60,  60)
BOX_GREEN_L   = ( 60, 200,  80)
BOX_ORANGE    = (255, 165,  50)
TEXT_YELLOW   = (255, 220,  80)
TEXT_WHITE    = (255, 255, 255)
TEXT_BLACK    = ( 20,  20,  20)
TEXT_DIM      = (180, 200, 180)
TITLE_GOLD    = (255, 215,   0)

# ----------------------------------------------------------------------
#  PANEL COLOURS (2X scaled fonts)
# ----------------------------------------------------------------------
PANEL_GREEN    = (0, 40, 0)
PANEL_YELLOW   = (255, 255, 0)
PANEL_BLUE     = (0, 0, 200)
PANEL_RED      = (220, 0, 0)
PANEL_WHITE    = (255, 255, 255)
PANEL_ORANGE   = (255, 140, 0)
PANEL_PURPLE   = (148, 0, 211)
BRIGHT_GREEN   = (0, 255, 0)

# ----------------------------------------------------------------------
#  ROUTES -- THE LAP OF AUSTRALIA
#  Twelve legs anti-clockwise around the coast: Sydney up the Reef to
#  Cairns, across the Top End, down the West, and home along the Bight
#  with the westerlies astern. Keys M and N are the "garnish": a fully
#  coastal finish from Adelaide to Sydney in two hops. Every distance
#  is the true great-circle figure (nm, origin to airport), every
#  elevation is the airport's REAL height above sea level in feet,
#  and "orig_elev" is the real elevation of the departure field --
#  each leg starts from a different airport now. Enroute stops travel
#  as via/via_dist/via_elev for a single stop, or as a "vias" LIST of
#  {"name", "dist", "elev"} when a leg calls at more than one field --
#  Brisbane-Townsville is the first with two, calling at Rockhampton
#  AND Mackay on the way north (v15). "sim_min" (v44) is the leg's
#  measured duration in SIM minutes -- every leg flown on the model:
#  a fast climb to the assigned level, ~300 kt cruise, AUTOLAND taken
#  at the 100 nm offer. The ETA box's shadowy REAL clock counts down
#  from sim_min / TIME_SCALE real minutes, so at the 2.9 clock a
#  Melbourne-Sydney shows about thirty. On the two 1:1 REAL TIME legs
#  the white ETA above it reads this SAME figure (v64) -- there the two
#  clocks agree by design.
# ----------------------------------------------------------------------
ROUTES = [
    {"key": "A", "name": "SYDNEY-BRISBANE",       "dist": 406, "hdg":  15, "elev":  13, "fl": 150, "fuel": 3200, "orig_elev":  21, "sim_min": 91,
     "via": "COFFS HARB.",  "via_dist": 239, "via_elev":  18, "via_sim_min": [57]},
    {"key": "B", "name": "BRISBANE-TOWNSVILLE",   "dist": 601, "hdg": 325, "elev":  18, "fl": 200, "fuel": 4400, "orig_elev":  13, "sim_min": 130,
     "vias": [{"name": "ROCKHAMPTON", "dist": 280, "elev":  34},
              {"name": "MACKAY",      "dist": 431, "elev":  19}],
     "via_sim_min": [65, 95]},
    {"key": "C", "name": "TOWNSVILLE-CAIRNS",     "dist": 154, "hdg": 340, "elev":  10, "fl":  80, "fuel": 2000, "orig_elev":  18, "sim_min": 39,
     "via": "DUNK IS.",     "via_dist":  87, "via_elev":   6, "via_sim_min": [26], "real_time": True},
    {"key": "D", "name": "CAIRNS-GOVE",           "dist": 588, "hdg": 295, "elev": 192, "fl": 200, "fuel": 4300, "orig_elev":  10, "sim_min": 127,
     "via": "WEIPA",        "via_dist": 336, "via_elev":  63, "via_sim_min": [76]},
    {"key": "E", "name": "GOVE-DARWIN",           "dist": 348, "hdg": 270, "elev": 103, "fl": 140, "fuel": 2800, "orig_elev": 192, "sim_min": 79,
     "via": "MANINGRIDA",   "via_dist": 152, "via_elev": 123, "via_sim_min": [40]},
    {"key": "F", "name": "DARWIN-BROOME",         "dist": 601, "hdg": 235, "elev":  56, "fl": 200, "fuel": 4400, "orig_elev": 103, "sim_min": 130,
     "via": "KUNUNURRA",    "via_dist": 238, "via_elev": 145, "via_sim_min": [57]},
    {"key": "G", "name": "BROOME-KARRATHA",       "dist": 351, "hdg": 240, "elev":  29, "fl": 140, "fuel": 2800, "orig_elev":  56, "sim_min": 80,
     "via": "PORT HEDLAND", "via_dist": 251, "via_elev":  33, "via_sim_min": [59]},
    {"key": "H", "name": "KARRATHA-PERTH",        "dist": 676, "hdg": 185, "elev":  67, "fl": 210, "fuel": 4800, "orig_elev":  29, "sim_min": 145,
     "via": "CARNARVON",    "via_dist": 304, "via_elev":  13, "via_sim_min": [70], "real_time": True},
    {"key": "I", "name": "PERTH-ESPERANCE",       "dist": 313, "hdg": 110, "elev": 470, "fl": 120, "fuel": 2600, "orig_elev":  67, "sim_min": 72,
     "via": "ALBANY",       "via_dist": 203, "via_elev": 233, "via_sim_min": [50]},
    {"key": "J", "name": "ESPERANCE-CEDUNA",      "dist": 606, "hdg":  85, "elev":  77, "fl": 200, "fuel": 4400, "orig_elev": 470, "sim_min": 131,
     "via": "MADURA",       "via_dist": 284, "via_elev": 344, "via_sim_min": [66]},
    {"key": "K", "name": "CEDUNA-ADELAIDE",       "dist": 295, "hdg": 125, "elev":  20, "fl": 120, "fuel": 2400, "orig_elev":  77, "sim_min": 68,
     "via": "WHYALLA",      "via_dist": 200, "via_elev":  41, "via_sim_min": [49]},
    {"key": "L", "name": "ADELAIDE-SYDNEY",       "dist": 628, "hdg":  85, "elev":  21, "fl": 200, "fuel": 4500, "orig_elev":  20, "sim_min": 135,
     "via": "MELBOURNE",    "via_dist": 346, "via_elev": 434, "via_sim_min": [78]},
    # ---------- The garnish: a fully coastal finish in two hops ----------
    {"key": "M", "name": "ADELAIDE-MELBOURNE",    "dist": 346, "hdg": 120, "elev": 434, "fl": 130, "fuel": 2800, "orig_elev":  20, "sim_min": 79,
     "via": "MT GAMBIER",   "via_dist": 200, "via_elev": 212, "via_sim_min": [49]},
    {"key": "N", "name": "MELBOURNE-SYDNEY",      "dist": 381, "hdg":  55, "elev":  21, "fl": 150, "fuel": 3000, "orig_elev": 434, "sim_min": 86,
     "via": "MERIMBULA",    "via_dist": 246, "via_elev":   7, "via_sim_min": [58]},
]

# ----------------------------------------------------------------------
#  AIRPORT ICAO CODES + LETTERS
#  ICAO code for each airport (verified against real-world codes), and
#  one ID character per airport for the briefing title and the DME
#  bracket. The Lap uses 30 airports -- more than the 26 letters of
#  the alphabet -- so the last four airports take DIGITS instead
#  (the captain's own suggestion): MADURA=1, WHYALLA=2, MT GAMBIER=3,
#  MERIMBULA=4. No route ever shows the same character twice.
# ----------------------------------------------------------------------
AIRPORT_ICAO = {
    "SYDNEY":       "YSSY",
    "BRISBANE":     "YBBN",
    "TOWNSVILLE":   "YBTL",
    "CAIRNS":       "YBCS",
    "GOVE":         "YPGV",
    "DARWIN":       "YPDN",
    "BROOME":       "YBRM",
    "KARRATHA":     "YPKA",
    "PERTH":        "YPPH",
    "ESPERANCE":    "YESP",
    "CEDUNA":       "YCDU",
    "ADELAIDE":     "YPAD",
    "MELBOURNE":    "YMML",
    # Enroute (intermediate) airports
    "PORT MACQ.":   "YPMQ",
    "COFFS HARB.":  "YCFS",
    "BUNDABERG":    "YBUD",
    "ROCKHAMPTON":  "YBRK",
    "MACKAY":       "YBMK",
    "DUNK IS.":     "YDKI",
    "WEIPA":        "YBWP",
    "MANINGRIDA":   "YMGD",
    "KUNUNURRA":    "YPKU",
    "PORT HEDLAND": "YPPD",
    "CARNARVON":    "YCAR",
    "GERALDTON":    "YGEL",
    "ALBANY":       "YABA",
    "MADURA":       "YMAD",
    "WHYALLA":      "YWHA",
    "MT GAMBIER":   "YMTG",
    "MERIMBULA":    "YMER",
}

AIRPORT_LETTERS = {
    "SYDNEY":       "S",
    "BRISBANE":     "B",
    "TOWNSVILLE":   "T",
    "CAIRNS":       "C",
    "GOVE":         "G",
    "DARWIN":       "D",
    "BROOME":       "R",
    "KARRATHA":     "K",
    "PERTH":        "P",
    "ESPERANCE":    "E",
    "CEDUNA":       "U",
    "ADELAIDE":     "A",
    "MELBOURNE":    "M",
    # Enroute (intermediate) airports
    "PORT MACQ.":   "Q",
    "COFFS HARB.":  "F",
    "BUNDABERG":    "N",
    "ROCKHAMPTON":  "O",
    "MACKAY":       "Y",
    "DUNK IS.":     "I",
    "WEIPA":        "W",
    "MANINGRIDA":   "Z",
    "KUNUNURRA":    "X",
    "PORT HEDLAND": "H",
    "CARNARVON":    "V",
    "GERALDTON":    "L",
    "ALBANY":       "J",
    # The alphabet ran out -- digits take over from here
    "MADURA":       "1",
    "WHYALLA":      "2",
    "MT GAMBIER":   "3",
    "MERIMBULA":    "4",
}

# ----------------------------------------------------------------------
#  SIMULATOR CONSTANTS
# ----------------------------------------------------------------------
TIME_SCALE = 2.9        # game speed: sim-seconds per real second (v42).

VERSION = "v132"        # build tag, shown tiny on the intro screen (v83):
                         # any screenshot of the front door names the build
                        # Flown on the model: MELBOURNE-SYDNEY takes ~86
                        # sim-minutes (fast climb to FL150, ~300 kt cruise,
                        # AUTOLAND from the 100 nm offer), so 2.9 lands the
                        # flight at ~30 REAL minutes. Was 6 (~14 min).
ORIGIN_ELEV = 31        # fallback only: every Lap route now carries its
                        # own "orig_elev" -- the REAL elevation of the
                        # departure airport. The fallback keeps old save
                        # files (whose routes predate orig_elev) working.
MAX_FL = 450
BANK_MAX = 40.0     # the bank limit (v40: was 45): the AI's bank scale reads
                    # 0-40 degrees each side -- ten-degree rests at 10, 20 and
                    # 30, the last rest at 40 (the 45 mark is gone) -- and no
                    # banking beyond 40 degrees is allowed, the needle
                    # included.
BANK_VISUAL = 1.5   # the scale's spread round the semicircle (v40): each
                    # degree of bank draws this many degrees round the arc, so
                    # the outermost 40 rest sits sixty degrees off the top
                    # instead of forty -- the gauge spreads a little further
                    # round the semicircle rather than bunching at the top.
TURN_BANK_DEG = 40.0  # the bank a turn command asks for -- the full forty
                      # degrees now (v40: was thirty)
TURN_HOLD_S = 12.0    # sim-seconds the bank stays on after the last turn
                      # command (~2 real seconds): the time the bank takes to
                      # wind through a 5-degree step at jet speed. Commands
                      # that keep coming -- a held turn key steps every 1.8
                      # sim-seconds -- keep the bank on the whole time (v33).
BANK_IN_TAU = 3.0     # sim-seconds: the first-order chase INTO the bank --
                      # the needle develops smoothly as the turn develops
BANK_OUT_TAU = 8.0    # sim-seconds: the slow first-order fight back to
                      # wings level once the turn is done -- "the aircraft
                      # fights against the turn" home to straight ahead (v34)


def origin_elev(route):
    """Elevation (ft) of the departure airport for a route. Each Lap of
    Australia leg starts from a different field -- from Cairns at 10 ft
    to Esperance at 470 ft -- so the figure travels with the route."""
    return float(route.get("orig_elev", ORIGIN_ELEV))


def route_vias(route):
    """The enroute (intermediate) airports of a route, IN ROUTE ORDER --
    each a dict with "name", "dist" (nm from the origin start line to the
    END of its runway) and "elev" (ft). A route may carry any number of
    them as a "vias" list (Brisbane-Townsville was the first with two:
    Rockhampton and Mackay); the original single-airport fields
    via/via_dist/via_elev are still understood, so old save files and
    every other leg of the Lap keep working unchanged."""
    vias = [{"name": v["name"], "dist": float(v["dist"]),
             "elev": float(v["elev"])} for v in route.get("vias", [])]
    if not vias and route.get("via"):
        vias.append({"name": route["via"],
                     "dist": float(route["via_dist"]),
                     "elev": float(route["via_elev"])})
    vias.sort(key=lambda v: v["dist"])
    return vias

# Fuel uplift (v30): every flight loads 25% more fuel than the route's
# published figure -- a full stop at the intermediate airport used to
# leave too little in the tanks to reach the destination.
FUEL_UPLIFT = 1.25


def route_fuel(route):
    """The fuel actually loaded for a flight: the route's published
    figure plus the 25% uplift every flight now carries (v30). The
    briefing quotes this figure and the Jet starts the flight with it."""
    return float(route["fuel"]) * FUEL_UPLIFT

# Altitude fuel efficiency (v57): the higher she cruises, the less the
# engines drink. The captain's table -- the fraction of fuel SAVED at
# each flight level against the FL200 baseline. Straight-line
# interpolation between the listed levels (FL275 cruises at 21.5%), no
# saving at all below FL200 (the baseline), and the 52% figure holding
# at the ceiling -- MAX_FL is 450 anyway.
FUEL_SAVE_TABLE = [     # (flight level, fraction saved vs the FL200 baseline)
    (200, 0.00),        # FL200 -- the baseline itself
    (250, 0.15),        # FL250 -- 15% saved
    (300, 0.28),        # FL300 -- 28% saved
    (350, 0.38),        # FL350 -- 38% saved
    (400, 0.46),        # FL400 -- 46% saved
    (450, 0.52),        # FL450 -- 52% saved
]


def fuel_flow_factor(alt_ft):
    """The fuel-flow multiplier for the present altitude: 1.0 at the
    FL200 baseline (and everywhere below it), shrinking as the v57
    savings table climbs -- 0.48 at the FL450 ceiling. Linear between
    the listed flight levels, flat beyond both ends."""
    fl = alt_ft / 100.0
    if fl <= FUEL_SAVE_TABLE[0][0]:
        return 1.0
    for (fl0, s0), (fl1, s1) in zip(FUEL_SAVE_TABLE, FUEL_SAVE_TABLE[1:]):
        if fl <= fl1:
            return 1.0 - (s0 + (s1 - s0) * (fl - fl0) / (fl1 - fl0))
    return 1.0 - FUEL_SAVE_TABLE[-1][1]

# Runway model: every airport has a 2,000 m runway, and each airport's
# published distance is measured from the origin start line to the END
# of its runway. Touch down before the runway start (2,000 m before the
# end) and you crash at the airport; still rolling past the end = overrun.
RWY_M = 2000.0
RWY_NM = RWY_M / 1852.0           # runway length in nm (~1.08)
# v20: the glideslope aims GS_AIM_NM past the threshold -- the classic
# touchdown-zone markers ~300 m in -- so the 3-degree path crosses the
# fence 48 ft up instead of meeting the ground AT the fence with zero
# feet of margin (any low wobble used to be turf short of the runway).
GS_AIM_NM = 0.16                  # nm past the threshold (~300 m)
GS_FULL_DEG = 1.0                 # v46: the G/S tape reads ANGULAR deviation,
                                  # +/- this many degrees off the beam for a
                                  # full-scale swing (a real receiver's way)
# DME metre readout: on approach the DME switches from nm to metres when
# 10,000 m before the runway THRESHOLD -- i.e. 12,000 m from the runway
# end (threshold + 2,000 m of runway). The readout still counts down the
# distance to the END, so 2000M marks the threshold and 0M the end.
APCH_METRES_M = 10000.0
M_PER_NM = 1852.0
APCH_ZONE_NM = 5.0                # "at the airport" zone ahead of the field
# Glideslope: wakes 100 NM out at EVERY airport -- the intermediate
# field and the destination alike -- so the G/S tape (and the AUTOLAND)
# can fly the 3-degree path from a long way out. (Was 15 nm at the
# enroute airport, 100 km at the destination.)
GS_ACTIVE_NM = 100.0
GEAR_STEP_SIM = 5.0     # sim-seconds between each gear light changing (~0.8 real s)
DOOR_DELAY_SIM = 0.2 * TIME_SCALE  # the yellow *D placard turns over one
                                   # fifth of a (real) second after the last
                                   # green square changes

def _exe_dir():
    """The folder the program runs from: the .exe's own folder when frozen
    (e.g. by PyInstaller), the script's folder when run as .py."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.abspath(__file__))


_WDIR = None


def _writable_dir():
    """Where the save, career-hours and log files live (v81): the
    .exe/script's own folder when it is writable -- the normal case, so
    the files sit beside the program exactly as they always have. But a
    friend who parks the .exe in Program Files (or any read-only place)
    must not lose saving: then the files go to a "Learjet" folder under
    the user's profile instead. Any trouble at all and the old folder is
    returned -- the writers are guarded and simply do nothing."""
    global _WDIR
    if _WDIR is not None:
        return _WDIR
    d = _exe_dir()
    try:
        probe = os.path.join(d, ".learjet_write_probe")
        with open(probe, "w") as f:
            f.write("ok")
        os.remove(probe)
        _WDIR = d
        return _WDIR
    except Exception:
        pass
    try:
        base = os.environ.get("APPDATA") or os.path.expanduser("~")
        d = os.path.join(base, "Learjet")
        os.makedirs(d, exist_ok=True)
        _WDIR = d
        return _WDIR
    except Exception:
        _WDIR = _exe_dir()
        return _WDIR


def _resource_candidates(filename, hardcoded=None):
    """Everywhere a resource file may live, most specific first: an
    optional hard-coded path, then the .exe/script folder, then -- for a
    PyInstaller one-file build -- the bundle's unpacked folder
    (sys._MEIPASS), so the file travels INSIDE the single .exe (v42).
    Build with: --add-data "<filename>;." and it is found there."""
    cands = []
    if hardcoded:
        cands.append(hardcoded)
    cands.append(os.path.join(_exe_dir(), filename))
    bundle_dir = getattr(sys, "_MEIPASS", None)
    if bundle_dir:
        cands.append(os.path.join(bundle_dir, filename))
    return cands


# Intro photo: hard-coded first choice, then the .exe/script folder, then
# inside a PyInstaller one-file bundle, then ASCII art.
INTRO_PHOTO_CANDIDATES = _resource_candidates("learjet_takeoff.jpg",
                                              r"D:\code\learjet_takeoff.jpg")

# Cruise atmosphere (v41): a real cabin-atmos recording, looped on the
# music stream for the duration of EVERY flight. Hard-coded first choice,
# then the .exe/script folder, then inside a PyInstaller bundle (v42) --
# the original download name is welcome too. If none of them loads, the
# synthesised v8 cruise voice plays instead, exactly as before.
CRUISE_SOUND_CANDIDATES = (
    _resource_candidates("learjet_cruise_atmos.mp3",
                         r"D:\code\learjet_cruise_atmos.mp3")
    + _resource_candidates("freesound_community-airplane-atmos-22955.mp3"))
CRUISE_MUSIC_VOL = 0.60   # steady level for the flight, under the bings

# Takeoff roar (v62): a real takeoff recording -- the captain's own
# file, its last ten seconds trimmed away -- heard on EVERY flight the
# instant the thrust lever reaches 100% for the roll; the cabin
# ambience steps aside while it plays and is heard again the moment it
# ends. The WAV is tried FIRST: pygame's music stream decodes MP3 on
# any build, but a mixer Sound chunk cannot on some -- the WAV loads
# with no codec at all. Same homes as the cruise atmos (hard-coded,
# the .exe/script folder, the PyInstaller bundle); if none of them
# loads, the ambience simply carries the takeoff too, as it always has.
TAKEOFF_SOUND_CANDIDATES = (
    _resource_candidates("learjet_takeoff_atmos.wav",
                         r"D:\code\learjet_takeoff_atmos.wav")
    + _resource_candidates("learjet_takeoff_atmos.mp3",
                           r"D:\code\learjet_takeoff_atmos.mp3"))
TAKEOFF_SND_VOL = 0.90   # the roar LEADS the mix; the ambience waits

# Landing voice (v63): a real landing recording -- the captain's own
# file, the approach and the RETARD call and the touchdown roll --
# heard on every COMPRESSED arrival, LOOPING until the wheels stop:
# only the full stop ends it (the prang ends it sooner; a go-around
# ends it and re-arms the trigger). v74: the two 1:1 REAL TIME legs
# keep her OFF by the captain's standing order -- there the cruise
# recording simply continues undisturbed all the way down. v66 led the
# 400 ft mark by LANDING_LEAD_S real seconds, flown against the live
# sink rate and the leg's own clock; v122 RETIRES the lead to 0.0 --
# the file now starts AT the mark itself, on the captain's call: the
# old head start had the recording open, finish, and loop four times
# through before its proper cue. WAV first, for the same codec reason
# as the roar; the load reports itself on the console.
LANDING_SOUND_CANDIDATES = (
    _resource_candidates("learjet_landing_atmos.wav",
                         r"D:\code\learjet_landing_atmos.wav")
    + _resource_candidates("learjet_landing_atmos.mp3",
                           r"D:\code\learjet_landing_atmos.mp3"))
LANDING_SND_VOL = 0.90    # the landing voice leads the mix, like the roar
LANDING_TRIG_FT = 400.0   # the mark the start leads: this height above
                          # the field ahead
LANDING_LEAD_S = 0.0      # v122: the lead is RETIRED -- the voice now
                          # starts AT the 400 ft mark, not ahead of it.
                          # The old seventeen-second head start had the
                          # recording open, finish, and loop four times
                          # through before its proper cue; v66's knob
                          # was the way to hunt the start, and the start
                          # is found. Raise it only to lead again --
                          # converted to feet through the live sink rate
                          # and the leg's own clock (jet.time_scale).
LANDING_LEAD_MAX_FT = 600.0   # cap on the lead's altitude, so a steep,
                              # fast descent cannot wake the voice
                              # hundreds of feet early. v122: INERT while
                              # LANDING_LEAD_S is 0.0 -- kept as the guard
                              # rail should the lead knob ever return
LANDING_REARM_GAP_FT = 100.0  # the go-around re-arm rides this far ABOVE
                              # the (now moving) trigger -- a fixed 550 ft
                              # could fall BELOW a led trigger, and one
                              # small wobble on short final would silence
                              # the voice for the rest of the approach

# Enroute-screen Learjet (v84): a top-down photograph of the jet that
# rides the briefing screen's dashed route line in place of the old
# blinking red square -- her nose tip marking the live position, the
# airframe balanced evenly astride the dashes. Same three homes as the
# other resources (hard-coded, the .exe/script folder, the PyInstaller
# bundle). If she cannot be found the red square stands in, as before.
ENROUTE_PLANE_CANDIDATES = _resource_candidates(
    "learjet_topdown.png", r"D:\code\learjet_topdown.png")
ENROUTE_PLANE_W = 0.085     # her length, as a fraction of screen width
ENROUTE_PLANE_BUILD = 0.08  # the fraction of the route over which she
                            # builds up from the nose after takeoff (v89:
                            # the arrival dissolve is retired -- she now
                            # carries the whole airframe to the destination)
ENROUTE_PLANE_MIN = 0.15    # the nose sliver always on show at the
                            # origin, so the marker never quite vanishes

# Enroute-screen background photograph (v89): the briefing screen's
# backdrop, cover-scaled and centre-cropped like the intro photo and
# blended over the classic dark green so the briefing's yellows and
# whites keep their footing. Same three homes as the other resources
# (hard-coded, the .exe/script folder, the PyInstaller bundle -- pack
# her in with --add-data "learjet_enroute_bg.jpg;."). If she cannot be
# found the screen wears the plain green she always has.
ENROUTE_BG_CANDIDATES = (
    _resource_candidates("learjet_enroute_bg.jpg",
                         r"D:\code\learjet_enroute_bg.jpg")
    + _resource_candidates("learjet_enroute_bg.jpeg",
                           r"D:\code\learjet_enroute_bg.jpeg")
    + _resource_candidates("learjet_enroute_bg.png",
                           r"D:\code\learjet_enroute_bg.png"))
ENROUTE_BG_ALPHA = 128    # the photograph's strength over the green:
                          # 0 = the green alone, 255 = the raw photograph
                          # (128 is the intro backdrop's own setting)

# Route-screen background photograph (v119): the Route Selection
# screen's backdrop -- now the airport-sunset couple (v121; was the
# "Greetings from Sydney" postcard) -- cover-scaled and centre-cropped
# like the intro photo and blended over the classic dark green so the
# gold title and the white hints keep their footing. Same three homes as the other resources (hard-coded, the
# .exe/script folder, the PyInstaller bundle -- pack her in with
# --add-data "learjet_route_bg.jpg;."). If she cannot be found the
# screen wears the plain green she always has.
ROUTE_BG_CANDIDATES = (
    _resource_candidates("learjet_route_bg.jpg",
                         r"D:\code\learjet_route_bg.jpg")
    + _resource_candidates("learjet_route_bg.jpeg",
                           r"D:\code\learjet_route_bg.jpeg")
    + _resource_candidates("learjet_route_bg.png",
                           r"D:\code\learjet_route_bg.png"))
ROUTE_BG_ALPHA = 255    # the photograph's strength over the green:
                        # 0 = the green alone, 255 = the raw photograph.
                        # v120: full strength now the panel is glass --
                        # lower her only if you want the green wash back
ROUTE_TEXT_SHADOW = 3   # the writing's soft dark shadow on the
                        # postcard, in pixels down-right; 0 = no shadow
ROUTE_GLASS_ALPHA = 0   # the translucent panel's opacity over the
                        # photograph: 0 = bare glass (the writing alone
                        # on the photograph), 255 = the old solid panel.
                        # v121: RETIRED to bare glass -- no pane at all,
                        # the writing sits straight on the photograph

# ----------------------------------------------------------------------
#  PYGAME SETUP
# ----------------------------------------------------------------------
def init_display():
    # v91: THE DOUBLE-WRITING FIX. Ask Windows for the display's TRUE
    # physical pixels before the window exists -- and this time VERIFY
    # the answer: the old code never checked the awareness call's
    # return code, so a failed call left Windows silently scaling the
    # game's output on 125% / 150% displays. Then open a NOFRAME
    # window at the desktop size instead of page-flipped FULLSCREEN:
    # identical full-screen look, but the compositor presents the
    # window normally, so no stale, scaled copy of an old frame can
    # reach the panel. That ghost lives in the driver's fullscreen
    # optimizations path -- every screen here repaints the whole
    # surface each frame, so it cannot be the app's. The verdict and
    # the chosen size report to the log, so a friend's machine can be
    # diagnosed from learjet_log.txt alone. (No-op off Windows.)
    dpi_ok = False
    try:
        import ctypes
        dpi_ok = (ctypes.windll.shcore.SetProcessDpiAwareness(2) == 0)  # per-monitor aware
    except Exception:
        try:
            import ctypes
            dpi_ok = bool(ctypes.windll.user32.SetProcessDPIAware())    # Vista+ fallback
        except Exception:
            dpi_ok = False
    try:
        pygame.mixer.pre_init(44100, -16, 2, 512)
    except Exception:
        pass
    pygame.init()
    pygame.display.set_caption("Learjet 35A Flight Simulator")
    info = pygame.display.Info()
    sw, sh = info.current_w, info.current_h
    _say("DPI awareness: %s | display %dx%d" % ("OK" if dpi_ok else "FAILED", sw, sh))
    screen = pygame.display.set_mode((sw, sh), pygame.NOFRAME | pygame.DOUBLEBUF)
    return screen, sw, sh
def load_fonts(sh):
    font_names = ["consolas", "liberation mono", "dejavu sans mono", "courier new", "monospace"]
    fonts = {
        "title":    pygame.font.SysFont(font_names, int(sh * 0.065), bold=True),
        "subtitle": pygame.font.SysFont(font_names, int(sh * 0.035)),
        "route":    pygame.font.SysFont(font_names, int(sh * 0.032), bold=True),
        "label":    pygame.font.SysFont(font_names, int(sh * 0.028), bold=True),
        "data":     pygame.font.SysFont(font_names, int(sh * 0.035), bold=True),
        "body":     pygame.font.SysFont(font_names, int(sh * 0.028)),
        "hint":     pygame.font.SysFont(font_names, int(sh * 0.024)),
        "small":    pygame.font.SysFont(font_names, int(sh * 0.022)),
        "tiny":     pygame.font.SysFont(font_names, int(sh * 0.018)),
        "prompt":   pygame.font.SysFont(font_names, int(sh * 0.030), bold=True, italic=True),
    }
    return fonts



def render_text(screen, font, text, colour, x, y, align="left"):
    surface = font.render(text, True, colour)
    rect = surface.get_rect()
    if align == "center":
        rect.center = (x, y)
    elif align == "right":
        rect.right = x
        rect.centery = y
    else:
        rect.left = x
        rect.centery = y
    screen.blit(surface, rect)
    return rect


def render_text_shadow(screen, font, text, colour, x, y, align="left",
                       offset=ROUTE_TEXT_SHADOW):
    """render_text with a soft dark shadow offset px down-right (v120):
    the Route Selection screen's writing sits straight on the postcard
    now, and the shadow keeps the golds and yellows legible anywhere on
    the photograph. offset 0 is plain render_text again."""
    if offset > 0:
        render_text(screen, font, text, TEXT_BLACK, x + offset, y + offset, align)
    return render_text(screen, font, text, colour, x, y, align)


def _glass_panel(screen, x, y, w, h, colour, alpha, radius=12):
    """A rounded rectangle of colour at alpha, blended onto whatever is
    beneath (v120): the Route Selection screen's translucent pane -- the
    postcard shows through, the writing keeps a quiet seat. alpha 0
    draws nothing: bare glass, the photograph alone under the text."""
    if alpha <= 0:
        return
    pane = pygame.Surface((w, h), pygame.SRCALPHA)
    pygame.draw.rect(pane, colour + (min(255, alpha),), (0, 0, w, h),
                     border_radius=radius)
    screen.blit(pane, (x, y))


def render_alt_ft(screen, font, alt_ft, x, y, align="left"):
    """Enroute-screen altitude readout: the figures in white, the words
    "ALT" and "FT" in their original TEXT_YELLOW. Supports the same
    left/center/right anchoring as render_text."""
    alt_img = font.render("ALT ", True, TEXT_YELLOW)
    num_img = font.render("%d" % alt_ft, True, TEXT_WHITE)
    ft_img = font.render("FT", True, TEXT_YELLOW)
    total_w = (alt_img.get_width() + num_img.get_width()
               + ft_img.get_width())
    if align == "right":
        left = x - total_w
    elif align == "center":
        left = x - total_w // 2
    else:
        left = x
    rect = alt_img.get_rect()
    rect.left = left
    rect.centery = y
    screen.blit(alt_img, rect.topleft)
    num_rect = num_img.get_rect()
    num_rect.left = rect.right
    num_rect.centery = y
    screen.blit(num_img, num_rect.topleft)
    ft_rect = ft_img.get_rect()
    ft_rect.left = num_rect.right
    ft_rect.centery = y
    screen.blit(ft_img, ft_rect.topleft)
    return pygame.Rect(left, rect.top, total_w, rect.height)


def draw_box(surface, colour, x, y, w, h, border=0, border_colour=None, radius=4):
    if border > 0 and border_colour:
        pygame.draw.rect(surface, border_colour, (x, y, w, h), border_radius=radius)
        pygame.draw.rect(surface, colour, (x + border, y + border, w - 2*border, h - 2*border), border_radius=radius-1)
    else:
        pygame.draw.rect(surface, colour, (x, y, w, h), border_radius=radius)


def cm_px(sh, cm=1.0):
    """Approximate physical centimetres in pixels for layout spacing.
    Uses the Windows vertical DPI when available, otherwise falls back
    to a desktop-like density proportional to the screen height."""
    try:
        import ctypes
        hdc = ctypes.windll.user32.GetDC(0)
        dpi_y = ctypes.windll.gdi32.GetDeviceCaps(hdc, 90)  # LOGPIXELSY
        ctypes.windll.user32.ReleaseDC(0, hdc)
        return max(1, int(dpi_y / 2.54 * cm))
    except Exception:
        return max(1, int(sh * 0.037 * cm))


# ----------------------------------------------------------------------
#  INTRO JET IMAGE LOADER  (photo first, ASCII fallback)
# ----------------------------------------------------------------------
def _load_intro_jet(sw, sh):
    """Return a surface for the intro jet: photo if found, else ASCII art."""
    max_w = int(sw * 0.62)
    max_h = int(sh * 0.30)

    for path in INTRO_PHOTO_CANDIDATES:
        try:
            if path and os.path.exists(path):
                img = pygame.image.load(path).convert()
                # Crop the thin light border so the photo sits cleanly in the card.
                crop = max(6, min(img.get_width(), img.get_height()) // 70)
                if img.get_width() > 2 * crop and img.get_height() > 2 * crop:
                    img = img.subsurface((crop, crop,
                                          img.get_width() - 2 * crop,
                                          img.get_height() - 2 * crop)).copy()
                scale = min(max_w / img.get_width(), max_h / img.get_height(), 1.25)
                new_size = (max(1, int(img.get_width() * scale)),
                            max(1, int(img.get_height() * scale)))
                return pygame.transform.smoothscale(img, new_size)
        except Exception:
            pass

    # Fallback: original ASCII jet silhouette.
    jet_art = [
        r"                                    /\                                    ",
        r"                             ______/  \______                            ",
        r"                             \    LEARJET   /_____                        ",
        r"                              \ __ o  o __/      \__                    ",
        r"                                 (__)  (__)                              ",
    ]
    jet_font = pygame.font.SysFont("consolas", int(sh * 0.028), bold=True)
    jet_surfaces = [jet_font.render(line, True, DARK_BLUE) for line in jet_art]
    jet_height = sum(s.get_height() for s in jet_surfaces)
    jet_width = max(s.get_width() for s in jet_surfaces)
    jet_surface = pygame.Surface((jet_width, jet_height), pygame.SRCALPHA)
    y_off = 0
    for s in jet_surfaces:
        jet_surface.blit(s, ((jet_width - s.get_width()) // 2, y_off))
        y_off += s.get_height()
    return jet_surface


def _load_intro_photo_bg(sw, sh):
    """Load the intro photo scaled to COVER the whole screen (centre-cropped).
    Returns None if no photo file is found, so the old layout can be used."""
    for path in INTRO_PHOTO_CANDIDATES:
        try:
            if path and os.path.exists(path):
                img = pygame.image.load(path).convert()
                # Crop the thin light border as before.
                crop = max(6, min(img.get_width(), img.get_height()) // 70)
                if img.get_width() > 2 * crop and img.get_height() > 2 * crop:
                    img = img.subsurface((crop, crop,
                                          img.get_width() - 2 * crop,
                                          img.get_height() - 2 * crop)).copy()
                # Scale to cover the screen, then centre-crop the overflow.
                # v90: scale a pixel to SPARE -- int() truncation could
                # land the cover-scale one pixel short of the screen, and
                # the centre-crop then raised: a silent fall back to the
                # plain layout. The crop is clamped to match.
                scale = max(sw / img.get_width(), sh / img.get_height())
                new_size = (max(sw, int(img.get_width() * scale) + 1),
                            max(sh, int(img.get_height() * scale) + 1))
                img = pygame.transform.smoothscale(img, new_size)
                x = max(0, (img.get_width() - sw) // 2)
                y = max(0, (img.get_height() - sh) // 2)
                return img.subsurface((x, y, sw, sh)).copy()
        except Exception:
            pass
    return None


# ----------------------------------------------------------------------
#  ENROUTE-SCREEN PLANE LOADER (v84) -- the top-down Learjet that rides
#  the briefing screen's dashed line in place of the old red square
# ----------------------------------------------------------------------
_ENROUTE_PLANE = None   # (surface, nose_x, nose_y) once loaded; False if
                        # the photograph is missing -- the blinking red
                        # square then stands in, exactly as before


def _load_enroute_plane(sw, sh):
    """The top-down Learjet for the Enroute screen's route line.
    Returns (surface, nose_x, nose_y): the plane scaled to
    ENROUTE_PLANE_W of the screen width, with the pixel offsets of her
    NOSE TIP from the surface's top-left -- the nose is the position
    marker, so every blit anchors on it. Loaded once and cached; None
    if no photograph is found."""
    global _ENROUTE_PLANE
    if _ENROUTE_PLANE is not None:
        # She is scaled to a fraction of the SCREEN WIDTH -- rebuild her
        # when the cache was baked for a different screen, or she and the
        # travelling gap she parts the dashes with no longer fit the
        # live display.
        if (not _ENROUTE_PLANE) or _ENROUTE_PLANE[0].get_width() == \
                max(1, int(round(sw * ENROUTE_PLANE_W))):
            return _ENROUTE_PLANE or None
        _ENROUTE_PLANE = None
    for path in ENROUTE_PLANE_CANDIDATES:
        try:
            if path and os.path.exists(path):
                img = pygame.image.load(path).convert_alpha()
                w0, h0 = img.get_width(), img.get_height()
                # The nose tip is the rightmost opaque column (she
                # points right, the way the route runs); its vertical
                # centre is the fuselage line, which sits ON the dashed
                # line so the airframe balances evenly astride it.
                box = img.get_bounding_rect(min_alpha=10)
                tip_x = box.right - 1
                ys = []
                for cx in range(max(box.left, tip_x - 2), box.right):
                    for cy in range(box.top, box.bottom):
                        if img.get_at((cx, cy))[3] > 10:
                            ys.append(cy)
                tip_y = (sum(ys) / float(len(ys))) if ys else box.centery
                scale = (sw * ENROUTE_PLANE_W) / float(w0)
                new_size = (max(1, int(round(w0 * scale))),
                            max(1, int(round(h0 * scale))))
                img = pygame.transform.smoothscale(img, new_size)
                nose_x = min(new_size[0] - 1, int(round(tip_x * scale)))
                nose_y = min(new_size[1] - 1, int(round(tip_y * scale)))
                _ENROUTE_PLANE = (img, nose_x, nose_y)
                _say("Enroute plane loaded: %s" % path)
                break
        except Exception as exc:
            _say("Enroute plane would not load from %s (%s)" % (path, exc))
    if _ENROUTE_PLANE is None:
        _ENROUTE_PLANE = False
        _say("ENROUTE PLANE NOT LOADED -- looked in:")
        for path in ENROUTE_PLANE_CANDIDATES:
            try:
                _say("    %s  %s" % (path, "(found)"
                      if os.path.exists(path) else "(missing)"))
            except Exception:
                pass
    return _ENROUTE_PLANE or None


# ----------------------------------------------------------------------
#  ENROUTE-SCREEN BACKGROUND LOADER (v89) -- the photograph behind the
#  briefing screen
# ----------------------------------------------------------------------
_ENROUTE_BG = None   # the finished backdrop surface once built; False if
                     # no photograph is found -- the plain dark green then
                     # stands in, exactly as before


def _load_enroute_bg(sw, sh):
    """The Enroute screen's backdrop: the captain's photograph scaled to
    COVER the whole screen (centre-cropped, the intro photo's own
    treatment), blended over the classic BG_GREEN at ENROUTE_BG_ALPHA so
    the briefing's yellows and whites keep their footing. Built once and
    cached; None if no photograph is found."""
    global _ENROUTE_BG
    # v92: the kill-switch. An empty file named learjet_enroute_bg.off
    # beside the program (or in D:\code) retires the photograph to
    # plain green. If the doubled writing dies with her, the ghost was
    # baked into the picture itself -- see the changelog.
    for flag in _resource_candidates("learjet_enroute_bg.off",
                                     r"D:\code\learjet_enroute_bg.off"):
        try:
            if flag and os.path.exists(flag):
                _ENROUTE_BG = False
                _say("Enroute background retired by %s -- plain green." % flag)
                return None
        except Exception:
            pass
    if _ENROUTE_BG is not None:
        # Rebuild the cache when it was baked at a different screen
        # size: a stale backdrop that no longer covers the whole screen
        # leaves last frame's writing ghosted under this frame's -- the
        # "double image of writing" on the Enroute screen.
        if (not _ENROUTE_BG) or _ENROUTE_BG.get_size() == (sw, sh):
            return _ENROUTE_BG or None
        _ENROUTE_BG = None
    for path in ENROUTE_BG_CANDIDATES:
        try:
            if path and os.path.exists(path):
                img = pygame.image.load(path).convert()
                # v92: tell the log WHAT we loaded, and judge her shape.
                # A screenshot of this very screen once travelled under
                # the photograph's name, and the writing baked into it
                # haunted the screen as a doubled image. Camera
                # photographs are 3:2 or 4:3 and thousands of pixels
                # tall; a 16:9-ish frame no taller than a display is the
                # shape of a screenshot, so the log says so.
                w0, h0 = img.get_width(), img.get_height()
                _say("Enroute background loaded: %s (%dx%d)"
                     % (path, w0, h0))
                if 1.55 <= w0 / float(h0) <= 1.85 and h0 <= 1600:
                    _say("  ...that is the shape of a SCREENSHOT, not a "
                         "camera photograph. If the writing on this "
                         "screen looks doubled, the ghost is baked into "
                         "the picture itself -- replace the file with a "
                         "true photograph, or retire it with "
                         "learjet_enroute_bg.off.")
                # v90: scale a pixel to SPARE -- int() truncation could
                # land the cover-scale one pixel short of the screen (a
                # 1366x768 display met a 5184x3456 photograph), and the
                # centre-crop then raised: a silent fall back to plain
                # green. The crop is clamped to match.
                scale = max(sw / img.get_width(), sh / img.get_height())
                new_size = (max(sw, int(img.get_width() * scale) + 1),
                            max(sh, int(img.get_height() * scale) + 1))
                img = pygame.transform.smoothscale(img, new_size)
                x = max(0, (img.get_width() - sw) // 2)
                y = max(0, (img.get_height() - sh) // 2)
                img = img.subsurface((x, y, sw, sh)).copy()
                base = pygame.Surface((sw, sh))
                base.fill(BG_GREEN)
                img.set_alpha(ENROUTE_BG_ALPHA)
                base.blit(img, (0, 0))
                _ENROUTE_BG = base.convert()
                _say("Enroute background loaded: %s" % path)
                break
        except Exception as exc:
            _say("Enroute background would not load from %s (%s)"
                 % (path, exc))
    if _ENROUTE_BG is None:
        _ENROUTE_BG = False
        _say("ENROUTE BACKGROUND NOT LOADED -- looked in:")
        for path in ENROUTE_BG_CANDIDATES:
            try:
                _say("    %s  %s" % (path, "(found)"
                      if os.path.exists(path) else "(missing)"))
            except Exception:
                pass
    return _ENROUTE_BG or None


# ----------------------------------------------------------------------
#  ROUTE-SCREEN BACKGROUND LOADER (v119) -- the postcard behind the
#  Route Selection screen
# ----------------------------------------------------------------------
_ROUTE_BG = None   # the finished backdrop surface once built; False if
                   # no photograph is found -- the plain dark green then
                   # stands in, exactly as before


def _load_route_bg(sw, sh):
    """The Route Selection screen's backdrop: the captain's postcard
    scaled to COVER the whole screen (centre-cropped, the intro photo's
    own treatment), blended over the classic BG_GREEN at ROUTE_BG_ALPHA
    so the screen's golds and whites keep their footing. Built once and
    cached; None if no photograph is found."""
    global _ROUTE_BG
    if _ROUTE_BG is not None:
        # Rebuild the cache when it was baked at a different screen
        # size (the Enroute backdrop's v91 lesson).
        if (not _ROUTE_BG) or _ROUTE_BG.get_size() == (sw, sh):
            return _ROUTE_BG or None
        _ROUTE_BG = None
    for path in ROUTE_BG_CANDIDATES:
        try:
            if path and os.path.exists(path):
                img = pygame.image.load(path).convert()
                _say("Route-screen background loaded: %s (%dx%d)"
                     % (path, img.get_width(), img.get_height()))
                # v90: scale a pixel to SPARE -- int() truncation could
                # land the cover-scale one pixel short of the screen.
                scale = max(sw / img.get_width(), sh / img.get_height())
                new_size = (max(sw, int(img.get_width() * scale) + 1),
                            max(sh, int(img.get_height() * scale) + 1))
                img = pygame.transform.smoothscale(img, new_size)
                x = max(0, (img.get_width() - sw) // 2)
                y = max(0, (img.get_height() - sh) // 2)
                img = img.subsurface((x, y, sw, sh)).copy()
                base = pygame.Surface((sw, sh))
                base.fill(BG_GREEN)
                img.set_alpha(ROUTE_BG_ALPHA)
                base.blit(img, (0, 0))
                _ROUTE_BG = base.convert()
                break
        except Exception as exc:
            _say("Route-screen background would not load from %s (%s)"
                 % (path, exc))
    if _ROUTE_BG is None:
        _ROUTE_BG = False
        _say("ROUTE-SCREEN BACKGROUND NOT LOADED -- looked in:")
        for path in ROUTE_BG_CANDIDATES:
            try:
                _say("    %s  %s" % (path, "(found)"
                      if os.path.exists(path) else "(missing)"))
            except Exception:
                pass
    return _ROUTE_BG or None


def _segments_line(screen, font, segments, cx, y):
    """One centred line of (label, value) pairs: the labels dim, the
    figures gold, a dim " . " between the pairs. v87 -- the logbook's
    record lines."""
    if not segments:
        return
    parts = []
    for i, (label, value) in enumerate(segments):
        if i:
            parts.append(("   \u00b7   ", TEXT_DIM))
        parts.append((label + ": ", TEXT_DIM))
        parts.append((value, TEXT_YELLOW))
    widths = [font.size(t)[0] for t, _c in parts]
    x = cx - sum(widths) // 2
    for (t, colour), w in zip(parts, widths):
        render_text(screen, font, t, colour, x, y, align="left")
        x += w


def draw_logbook_panel(screen, sw, sh, fonts):
    """v87: THE PILOT'S LOGBOOK on the front door -- a navy-and-gold
    career card sitting where the intro art used to (the photo still
    shines round its edges). A letterspaced header, the career hours
    and the captain-since date beneath it, two rows of four stat cards
    (little progress bars on the laps, airports and legs), and two
    record lines under them. Fly all fourteen legs and the first
    record line gives way to THE LAP IS COMPLETE in pulsing gold.
    Reads the banked _stats; shown once the first flight is in the
    book (the v83 career-hours line holds the fort until then)."""
    st = _stats
    flights = int(st.get("flights", 0))
    arrivals = int(st.get("arrivals", 0))
    hand = int(st.get("arrivals_hand", 0))
    auto = int(st.get("arrivals_auto", 0))
    prangs = int(st.get("prangs", 0))
    greasers = int(st.get("greasers", 0))
    dist_nm = float(st.get("distance_nm", 0.0))
    laps = dist_nm / float(LAP_NM) if LAP_NM else 0.0
    apts = st.get("airports", []) or []
    legs = st.get("legs_done", []) or []
    lap_done = len(legs) >= len(ROUTES)

    # ---------- the card itself ----------
    pw = int(sw * 0.74)
    ph = int(sh * 0.300)
    px = (sw - pw) // 2
    py = int(sh * 0.360)
    panel = pygame.Surface((pw, ph), pygame.SRCALPHA)
    pygame.draw.rect(panel, (*DARK_BLUE, 216), (0, 0, pw, ph),
                     border_radius=16)
    pygame.draw.rect(panel, TITLE_GOLD, (0, 0, pw, ph), 2,
                     border_radius=16)
    screen.blit(panel, (px, py))

    # ---------- the header, with a gold rule either side ----------
    head = "P I L O T ' S   L O G B O O K"
    hy = py + int(sh * 0.024)
    render_text(screen, fonts["hint"], head, TITLE_GOLD, sw // 2, hy,
                align="center")
    hw = fonts["hint"].size(head)[0]
    rule_y = hy
    for x0, x1 in ((px + int(pw * 0.06), sw // 2 - hw // 2 - 14),
                   (sw // 2 + hw // 2 + 14, px + pw - int(pw * 0.06))):
        if x1 > x0:
            pygame.draw.line(screen, TITLE_GOLD, (x0, rule_y),
                             (x1, rule_y), 1)

    # ---------- the hours aloft, and the day the career began ----------
    sub = "%d h: %02d m at the controls" % (int(_career_hours_s // 3600.0),
                                            int((_career_hours_s % 3600.0)
                                                // 60.0))
    if st.get("first_flight"):
        sub += "   \u00b7   captain since %s" % st["first_flight"]
    render_text(screen, fonts["tiny"], sub, TEXT_DIM, sw // 2,
                py + int(sh * 0.047), align="center")

    # ---------- the stat cards, two rows of four ----------
    side = int(pw * 0.028)
    gap = int(pw * 0.012)
    cw = (pw - 2 * side - 3 * gap) // 4
    chh = int(sh * 0.084)
    rows_y = (py + int(sh * 0.062), py + int(sh * 0.152))

    if hand and auto:
        arr_sub = "%d hand-flown \u00b7 %d autoland" % (hand, auto)
    elif auto:
        arr_sub = "all by autoland"
    else:
        arr_sub = "all hand-flown" if arrivals else ""
    rate = (100.0 * arrivals / (arrivals + prangs)) if (arrivals + prangs) else None
    cards = [
        (str(flights), "FLIGHTS", "", None),
        (str(arrivals), "ARRIVALS", arr_sub, None),
        (str(prangs), "PRANGS",
         ("%d%% arrival rate" % round(rate)) if rate is not None else "",
         None),
        (str(greasers), "GREASERS",
         ("of %d hand-flown" % hand) if hand else "", None),
        (format(int(dist_nm), ","), "NM FLOWN", "", None),
        ("%.2f" % laps, "LAPS OF AUSTRALIA", "", laps % 1.0),
        ("%d/%d" % (len(apts), len(AIRPORT_ICAO)), "AIRPORTS VISITED", "",
         len(apts) / float(len(AIRPORT_ICAO))),
        ("%d/%d" % (len(legs), len(ROUTES)), "LEGS COMPLETED", "",
         len(legs) / float(len(ROUTES))),
    ]
    for i, (value, caption, subc, bar) in enumerate(cards):
        cx0 = px + side + (i % 4) * (cw + gap)
        cy0 = rows_y[i // 4]
        card = pygame.Surface((cw, chh), pygame.SRCALPHA)
        pygame.draw.rect(card, (80, 125, 195, 70), (0, 0, cw, chh),
                         border_radius=9)
        pygame.draw.rect(card, (*BORDER_BLUE, 220), (0, 0, cw, chh), 1,
                         border_radius=9)
        screen.blit(card, (cx0, cy0))
        render_text(screen, fonts["label"], value, TEXT_YELLOW,
                    cx0 + cw // 2, cy0 + int(chh * 0.30), align="center")
        render_text(screen, fonts["tiny"], caption, TEXT_WHITE,
                    cx0 + cw // 2, cy0 + int(chh * 0.60), align="center")
        if subc:
            render_text(screen, fonts["tiny"], subc, TEXT_DIM,
                        cx0 + cw // 2, cy0 + int(chh * 0.80), align="center")
        if bar is not None:
            bw = cw - 18
            bx = cx0 + 9
            by = cy0 + chh - 7
            pygame.draw.rect(screen, (25, 45, 90), (bx, by, bw, 4),
                             border_radius=2)
            fill = max(0.0, min(1.0, bar))
            if fill > 0.0:
                pygame.draw.rect(screen, TITLE_GOLD,
                                 (bx, by, max(2, int(bw * fill)), 4),
                                 border_radius=2)

    # ---------- the record lines ----------
    # One priority list of (label, value) pairs, wrapped by MEASURED
    # pixel width into up to three lines that never leave the card --
    # so the book reads as well on a small laptop as on the big
    # screen. Fly all fourteen legs and the first line gives way to
    # THE LAP IS COMPLETE in pulsing gold.
    items = []
    if st.get("best_touch_fpm") is not None:
        items.append(("Smoothest touchdown", "%d fpm at %s" % (
            int(st["best_touch_fpm"]), st.get("best_touch_apt") or "the field")))
    if int(st.get("best_rating", 0)) > 0:
        items.append(("Best handling", "%d%%" % int(st["best_rating"])))
    if float(st.get("highest_alt", 0.0)) > 0.0:
        items.append(("Highest cruise", "FL%d" % int(round(
            float(st["highest_alt"]) / 100.0))))
    if int(st.get("streak", 0)) > 0:
        n = int(st["streak"])
        items.append(("Streak", "%d clean arrival%s" % (n,
                      "s" if n != 1 else "")))
    if int(st.get("deadstick", 0)) > 0:
        items.append(("Deadstick saves", str(int(st["deadstick"]))))
    if int(st.get("cab_survivals", 0)) > 0:
        items.append(("CAB PRESS survived", str(int(st["cab_survivals"]))))
    counts = st.get("route_counts", {}) or {}
    if counts:
        fav = max(counts, key=lambda k: counts[k])
        items.append(("Favourite leg", "%s x%d" % (fav, int(counts[fav]))))
    if st.get("last_flight"):
        items.append(("Last flight", st["last_flight"]))

    rfont = fonts["tiny"]
    sep_w = rfont.size("   \u00b7   ")[0]
    max_w = int(pw * 0.92)
    lines, cur, cur_w = [], [], 0
    for label, value in items:
        w = rfont.size(label + ": ")[0] + rfont.size(value)[0]
        add = w + (sep_w if cur else 0)
        if cur and cur_w + add > max_w:
            lines.append(cur)
            cur, cur_w = [], 0
            add = w
        cur.append((label, value))
        cur_w += add
    if cur:
        lines.append(cur)
    n_rows = 3
    y0 = py + int(sh * 0.2415)
    dy = int(sh * 0.0188)
    row = 0
    if lap_done:
        pulse = int(150 + 105 * abs(math.sin(pygame.time.get_ticks() / 500)))
        render_text(screen, fonts["tiny"],
                    "*  T H E   L A P   O F   A U S T R A L I A   I S "
                    "  C O M P L E T E  *",
                    (pulse, int(pulse * 0.85), 40), sw // 2, y0,
                    align="center")
        row = 1
    for ln in lines[:max(0, n_rows - row)]:
        _segments_line(screen, rfont, ln, sw // 2, y0 + row * dy)
        row += 1

# ----------------------------------------------------------------------
#  SCREEN 1: INTRODUCTION
# ----------------------------------------------------------------------
def intro_screen(screen, sw, sh, fonts):
    """Display the intro. When the photo is found it fills the whole screen
    at 50% transparency behind all the existing text; otherwise the old
    white-panel layout with the centred art is used."""
    clock = pygame.time.Clock()
    running = True

    PHOTO_ALPHA = 128          # backdrop transparency: 0 invisible, 255 solid

    # Full-screen photo backdrop (None if no photo file is found).
    photo_bg = _load_intro_photo_bg(sw, sh)

    # Old layout only: small centred art (photo card or ASCII fallback).
    jet_surface = None
    jet_width = jet_height = 0
    if photo_bg is None:
        jet_surface = _load_intro_jet(sw, sh)
        jet_width, jet_height = jet_surface.get_size()

    # Spacer keeps the info line at its old position when the backdrop is used.
    art_height = jet_height if jet_surface is not None else int(sh * 0.30)
    # v87: when the logbook panel shows, the art (or the photo's spacer)
    # has yielded its space to the card -- the spacer takes the card's
    # height instead, so the info line drops below the panel in both
    # layouts, exactly as the photo layout's spacer always arranged.
    if int(_stats.get("flights", 0)) > 0:
        art_height = max(art_height, int(sh * 0.31))

    # Text colours: title and prompt stay dark blue as originally designed;
    # the rest is white over the photo backdrop, dark grey on the white panel.
    TEXT_SOFT = WHITE if photo_bg is not None else DARK_GREY

    # v83: does a saved flight wait behind the front door? If so the
    # legend gains a dim [F9] line and the key resumes it on the spot.
    save_available = os.path.exists(SAVE_PATH)

    # v87: the PILOT'S LOGBOOK shows once the first flight is in the
    # book; until then the front door looks exactly as it always has
    # (and the v83 career-hours line holds the fort for a career that
    # has banked minutes but no concluded flight yet).
    logbook_shown = int(_stats.get("flights", 0)) > 0

    # Bottom-of-intro line spacing: about two centimetres between lines.
    CM2 = cm_px(sh, 2.0)

    # Animation: fade in (to 50% for the backdrop, to solid for the old art).
    jet_alpha = 0
    jet_fade_speed = 4

    while running:
        clock.tick(60)  # 60 FPS

        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # quit
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None       # quit
                if event.key == pygame.K_t:
                    return "tutorial" # built-in Flying School
                if event.key == pygame.K_F9 and save_available:
                    return "load"     # v83: resume the saved flight from here
                if event.key in (pygame.K_c, pygame.K_RETURN, pygame.K_SPACE):
                    return True       # [C] continue = on to Route Selection
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                return True           # a click continues too

        # --- Drawing ---
        screen.fill(SKY_BLUE)

        # Full-screen photo backdrop at 50% transparency (fades in).
        if photo_bg is not None:
            jet_alpha = min(PHOTO_ALPHA, jet_alpha + jet_fade_speed)
            photo_bg.set_alpha(jet_alpha)
            screen.blit(photo_bg, (0, 0))

        # Decorative top and bottom bars (filled with DARK_BLUE)
        draw_box(screen, DARK_BLUE, 0, 0, sw, int(sh * 0.08), border=0, radius=0)
        draw_box(screen, DARK_BLUE, 0, int(sh * 0.92), sw, int(sh * 0.08), border=0, radius=0)

        # Top title bar text
        render_text(screen, fonts["small"], "LEARJET 35A  |  PYTHON 3.11  |  NO EXTERNAL LIBRARIES (except pygame)",
                    WHITE, sw // 2, int(sh * 0.04), align="center")

        # Build tag (v83): tiny, in the top bar's right corner.
        render_text(screen, fonts["tiny"], VERSION, WHITE,
                    sw - int(sw * 0.015), int(sh * 0.04), align="right")

        # Bottom status bar: the tribute to the original authors, J. Keech
        # and P. Russell -- three short lines inside the dark blue band,
        # where the old "A tribute to the 1980s VZ-200 classic" line sat.
        tribute_lines = [
            "Dedicated with gratitude and admiration to J. KEECH and P. RUSSELL, authors of the original 1983 Dick Smith",
            "Electronics game \"Learjet\" for the VZ-200, whose creation has given me more than 43 years of enjoyment.",
            "This recreation is my tribute to their vision and ingenuity, and to all who still fondly remember playing it.",
        ]
        for trib_i, trib_line in enumerate(tribute_lines):
            render_text(screen, fonts["tiny"], trib_line, WHITE,
                        sw // 2, int(sh * (0.939 + trib_i * 0.021)), align="center")

        # Main content box - white fill with dark blue border
        box_margin = int(sw * 0.08)
        box_w = sw - 2 * box_margin
        box_h = int(sh * 0.72)
        box_x = box_margin
        box_y = int(sh * 0.14)

        if photo_bg is not None:
            # Transparent fill: dark blue border only, so the photo shows through.
            pygame.draw.rect(screen, DARK_BLUE, (box_x, box_y, box_w, box_h), 4, border_radius=16)
        else:
            # White fill
            draw_box(screen, WHITE, box_x, box_y, box_w, box_h, border=0, radius=16)
            # Dark blue border (4px)
            draw_box(screen, WHITE, box_x, box_y, box_w, box_h, border=4, border_colour=DARK_BLUE, radius=16)

        # Title: L E A R J E T
        title_y = box_y + int(sh * 0.06)
        render_text(screen, fonts["title"], "L E A R J E T", DARK_BLUE, sw // 2, title_y, align="center")

        # Subtitle
        sub_y = title_y + int(sh * 0.09)
        render_text(screen, fonts["subtitle"], "a text-mode flight simulator", TEXT_SOFT, sw // 2, sub_y, align="center")

        # Credits: two tiny lines centred in the gap between the subtitle
        # and the art (that gap is empty in both the photo and the old
        # white-panel layout, so nothing else needs to move).
        render_text(screen, fonts["tiny"], "Coded by Kimi K3 Max", TEXT_SOFT,
                    sw // 2, sub_y + int(sh * 0.032), align="center")
        render_text(screen, fonts["tiny"], "Managed by J Vromans", TEXT_SOFT,
                    sw // 2, sub_y + int(sh * 0.049), align="center")
        # v83: the pilot's logbook on the front door -- the banked career
        # hours, shown once the first real minute has been flown. v87:
        # once the LOGBOOK panel is up it carries the hours in its own
        # header, so this single line only holds the fort until then.
        if _career_hours_s >= 60.0 and not logbook_shown:
            render_text(screen, fonts["tiny"],
                        "Career flight time:  %d h: %02d m" % (
                            int(_career_hours_s // 3600.0),
                            int((_career_hours_s % 3600.0) // 60.0)),
                        TEXT_SOFT, sw // 2, sub_y + int(sh * 0.066), align="center")

        # Centred art (old layout only, when no photo file is found).
        # v87: when the logbook panel is showing it takes this space,
        # so the little jet retires from the front door.
        jet_y = sub_y + int(sh * 0.08)
        if jet_surface is not None and not logbook_shown:
            jet_alpha = min(255, jet_alpha + jet_fade_speed)
            jet_surface.set_alpha(jet_alpha)
            jet_x = (sw - jet_width) // 2
            screen.blit(jet_surface, (jet_x, jet_y))

        # Info line
        info_y = jet_y + art_height + int(sh * 0.06)
        render_text(screen, fonts["body"], "A complete flight simulator in a single file  —  just double-click and fly",
                    TEXT_SOFT, sw // 2, info_y, align="center")

        # v87: the PILOT'S LOGBOOK card, over the photo (or the white
        # panel), in the space the art used to fill.
        if logbook_shown:
            draw_logbook_panel(screen, sw, sh, fonts)

        # Prompt box at bottom
        prompt_y = box_y + box_h - int(sh * 0.10)
        prompt_text = "Press [C] for Route Selection ..."

        # Gentle pulse effect on the prompt: a blue-family glow that stays
        # readable on the white panel AND over the photo backdrop. (The
        # old grey pulse faded to pure white at its peak and vanished
        # entirely on the white panel, so DARK_BLUE was drawn instead --
        # the pulse was computed but never used.)
        pulse = abs(math.sin(pygame.time.get_ticks() / 800))
        prompt_colour = (int(45 + 90 * pulse), int(85 + 90 * pulse), 200)

        render_text(screen, fonts["prompt"], prompt_text, prompt_colour, sw // 2, prompt_y, align="center")

        # Offer the built-in tutorial to first-time flyers, two centimetres
        # above the prompt, with the hint two centimetres below it.
        offer_y = prompt_y - CM2
        # v83: two lines now share the space below the prompt (the legend
        # and, when a save exists, the dim [F9] nudge), so they sit a
        # touch closer -- half a CM2 each -- and both stay inside the box.
        hint_y = min(prompt_y + CM2 // 2, int(sh * 0.90))
        render_text(screen, fonts["small"], "New to the Learjet? Press [T] for Flying School - no experience needed.",
                    TEXT_YELLOW, sw // 2, offer_y, align="center")

        # Small hint
        render_text(screen, fonts["small"],
                    "[T] Flying School  |  [C] Continue  |  [M] Mute in flight  |  [ESC] Quit",
                    TEXT_SOFT, sw // 2, hint_y, align="center")

        # v83: the save-waiting nudge -- dim, and only when a save exists.
        if save_available:
            save_y = min(hint_y + CM2 // 2, int(sh * 0.90))
            render_text(screen, fonts["tiny"], "[F9] resume your saved flight",
                        TEXT_SOFT, sw // 2, save_y, align="center")

        pygame.display.flip()
# ----------------------------------------------------------------------
#  SCREEN 1A: FLYING SCHOOL (built-in tutorial)
# ----------------------------------------------------------------------
def tutorial_screen(screen, sw, sh, fonts):
    """A paged beginner school that travels inside the program file."""
    clock = pygame.time.Clock()
    page = 0
    pages = [
        ("FLYING SCHOOL - WELCOME ABOARD", [
            "Welcome, captain. This school assumes you have flown nothing but a chair.",
            "The job is simple: take off, follow the route line, then land gently.",
            "You do not need real pilot knowledge. The INFO line is your instructor.",
            "> Time is compressed %g:1 - an hour aloft takes about %d real minutes." % (
                TIME_SCALE, round(60.0 / TIME_SCALE)),
            "> Except the two REAL TIME legs at 1:1: Townsville-Cairns and Karratha-Perth (v56).",
            "> If a message appears at INFO, read it first. It usually names the next key.",
            "> The intro screen's PILOT'S LOGBOOK keeps your career: "
            "flights, greasers, laps of the Lap, streaks and all.",
            "Use [N] or [SPACE] for the next page, [P] to go back, [ESC] to leave school.",
        ]),
        ("YOUR OFFICE - WHAT THE BOXES MEAN", [
            "IAS: airspeed in knots. Near the ground, too slow is the real danger.",
            "ALT: altitude in feet. VSI: vertical speed in feet per minute, up or down.",
            "THRUST: engine power. FLAP: lift and drag. GEAR: wheels. Three greens = down.",
            "DME: distance. GROUND SPEED: speed over the ground.",
            "ETA: time to the field the DME is tuned to.",
            "> REAL TIME legs: the ETA and the dim amber clock beneath it read the SAME time.",
            "> The ETA box's blue line: Real Time on the left, Current Time on the right.",
            "> Flight Hours in the middle: your total real hours aloft over every route flown.",
            "AUTO PILOT can hold heading and a flight level, but you remain the captain.",
        ]),
        ("TAKEOFF - FROM BRAKES TO BLUE SKY", [
            "After the briefing, press a key to taxi. Brakes are ON, engines are off.",
            "> Press [E] to start the engines - the little diagonal cells spin until liftoff.",
            "You are parked 90 degrees off the runway heading, like the VZ-200 original.",
            "> Turn into wind with [A] or [D] until HDG reads the runway heading.",
            "Now [B] brakes off, hold [+] to 100%. At 125 kt press [W] to rotate.",
            "Positive rate and climbing? Press [G] to raise the gear. Takeoff flap: 0-20.",
        ]),
        ("CLIMB AND CRUISE - SMALL HANDS WIN", [
            "[W] pitches up one degree a press, [S] one degree down - hold to keep winding.",
            "Trim speed with [+] and [-]. Watch overspeed and flap warnings at INFO.",
            "> [K] winds the assigned flight level up, [Shift+K] down, then [P] autopilot.",
            "Hand-flying? [A] and [D] turn five degrees. [H] nudges the heading bug ten.",
            "[L] levels off gently right where you are - very handy in busy moments.",
            "Height is money: the higher the cruise, the less fuel she burns.",
            "> FL250 saves 15% over FL200 - FL300 28%, FL350 38%, FL400 46%, FL450 52%.",
        ]),
        ("FINDING THE LINE - OBS, CDI AND WIND", [
            "The Enroute picture [V] shows the route as a dashed line. The Learjet's nose is you.",
            "OBS is the course line. It starts on the route; twist it with [O] and [Shift+O].",
            "The CDI needle beside AUTO PILOT shows drift. Centre it and you are on course.",
            "> If INFO says OFF COURSE, turn toward the side it names and centre the needle.",
            "A gentle wind wanders the heading over time, so glance at the CDI now and then.",
        ]),
        ("DESCENT PLANNING - LET INFO DO THE MATHS", [
            "Profile rule: be at field elevation plus 1,000 ft for every minute to run.",
            "Example: five minutes to run means about 5,000 ft above the airport.",
            "Those minutes are sim minutes - they tick %g times faster than your watch." % TIME_SCALE,
            "On the two REAL TIME legs they tick exactly WITH your watch - no compression.",
            "Follow START YOUR DESCENT messages, then check you are ON PROFILE.",
            "Too high? More [S] or less thrust. Too low? Ease the descent with [W].",
            "Slow below 200 kt before the gear comes down, and mind the flap speed limits.",
        ]),
        ("GLIDESLOPE - THE SAFE PATH DOWN", [
            "The G/S tape wakes 100 nm out - at the destination and any enroute airport too.",
            "The blue centre notch is the safe path. The orange marker is you.",
            "> Marker above the notch = HIGH. Press [S] or reduce thrust to come down.",
            "> Marker on the notch = ON GLIDESLOPE. Marker below = LOW. Press [W] or add power.",
            "Fly the marker to the notch and keep it there. Small corrections beat heroics.",
            "AUTOLAND: autopilot on, and 100 nm out she offers to land for you.",
            "> [Y] accepts, [N] declines - or just let the 30-second window run out.",
            "> Engaged? [Y] again hands her back: she levels where she is, AP on the bug.",
            "> KARRATHA-PERTH: both fields invite at 200 nm - settle in and let her down early.",
            "> Cruising high? Be near FL300 by the offer - from FL350 up she lands long.",
        ]),
        ("LANDING - WHERE THE RUBBER MEETS THE RUNWAY", [
            "> Save game prior to landing in case you need to retry - [F5] saves, [F9] reloads.",
            "Before 8 nm and below field +2,000 ft: gear down [G]. Wait for three greens.",
            "Use flap 30 or 40 with [F]. Keep about 120-140 kt on final.",
            "Each flap step adds lift: the nose balloons, so ease it back with [S].",
            "Touch down only after the DME switches to metres: that is the runway starting.",
            "Between 2000M and 0M is your 2,000 m runway. Land early, not at the last brick.",
            "> Over the fence, one [W] tap to flare - arrive under 900 fpm, gently does it.",
            "> If she floats, one [S] tap settles her on - don't drift toward 0M.",
            "On touchdown press [B] AND reverse [R], and KEEP THE POWER ON",
            "against the buckets - reverse bite comes from N1. Stop before 0M.",
        ]),
        ("IF IT GOES PEAR-SHAPED - AND FINAL CHECKS", [
            "STALL: nose down [S], add thrust [+], then ease back to the climb.",
            "TOO LOW - GEAR: wheels down now. TERRAIN: climb first, think later.",
            "> Overshot? FLY AROUND for another attempt - climb [W], turn back, re-join.",
            "> CAB PRESS flashing: a pressurisation failure - get below 10,000 ft and it goes out.",
            "Fuel is a promise, not a suggestion. LOW FUEL means land soon.",
            "> Out of fuel she is a glider: ~25 NM per 10,000 ft. Clean up, 150 kt.",
            "PAUSE with [SPACE] if the phone rings. [M] mutes, [F5] saves, [F9] loads.",
            "> Final checklist: three greens, flaps set, 120-140 kt, marker on the notch.",
            "That is it. Go fly. The sky is patient and the runway is wide-ish.",
        ]),
    ]

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key in (pygame.K_p, pygame.K_LEFT):
                    page = max(0, page - 1)
                elif event.key in (pygame.K_n, pygame.K_SPACE, pygame.K_RETURN, pygame.K_RIGHT):
                    page += 1
                    if page >= len(pages):
                        return True

        screen.fill(BG_GREEN)
        margin = int(sw * 0.07)
        box = pygame.Rect(margin, int(sh * 0.07), sw - 2 * margin, int(sh * 0.82))
        draw_box(screen, BOX_GREEN, box.x, box.y, box.w, box.h,
                 border=8, border_colour=BORDER_BLUE, radius=12)

        title, lines = pages[page]
        render_text(screen, fonts["title"], title, TITLE_GOLD,
                    sw // 2, box.y + int(sh * 0.055), align="center")

        y = box.y + int(sh * 0.135)
        left = box.x + int(sw * 0.055)
        step_y = int(sh * 0.041)
        for line in lines:
            if line == "":
                y += step_y // 2
                continue
            colour = TEXT_WHITE
            txt = line
            if line.startswith(">"):
                txt = line[1:].lstrip()
                colour = TEXT_YELLOW
            render_text(screen, fonts["body"], txt, colour, left, y, align="left")
            y += step_y

        footer = "Page %d of %d   |   [N]/[SPACE] next   [P] back   [ESC] leave Flying School" % (
            page + 1, len(pages))
        render_text(screen, fonts["small"], footer, TEXT_DIM,
                    sw // 2, box.bottom - int(sh * 0.045), align="center")
        pygame.display.flip()


# ----------------------------------------------------------------------
#  SCREEN 2: ROUTE SELECTION
# ----------------------------------------------------------------------
def route_screen(screen, sw, sh, fonts):
    clock = pygame.time.Clock()
    running = True
    selected = None

    margin = int(sw * 0.06)
    box_x = margin
    box_w = sw - 2 * margin
    title_y = int(sh * 0.08)
    inner_margin = int(sw * 0.04)
    route_box_x = box_x + inner_margin
    route_box_w = box_w - 2 * inner_margin
    route_box_y = int(sh * 0.18)
    route_box_h = int(sh * 0.62)
    n_routes = len(ROUTES)
    row_height = route_box_h // (n_routes + 1)
    # Add top padding so first route doesn't touch the blue border
    top_padding = int(sh * 0.025)  # extra space at top of route box
    first_row_y = route_box_y + top_padding + row_height // 2
    col_key = route_box_x + int(route_box_w * 0.03)
    col_name = route_box_x + int(route_box_w * 0.12)
    col_dist = route_box_x + int(route_box_w * 0.85)

    # LOAD GAME button, bottom-right: click it or press [F9] to jump
    # straight back into a saved flight. Greyed out when no save exists.
    save_available = os.path.exists(SAVE_PATH)
    lb_label = "LOAD GAME  [F9]" if save_available else "NO SAVE YET"
    lb_w = fonts["hint"].size(lb_label)[0] + 40
    lb_h = int(sh * 0.05)
    lb_rect = pygame.Rect(sw - margin - lb_w, int(sh * 0.85) - lb_h // 2, lb_w, lb_h)

    # The screen's backdrop (v119): the captain's postcard over the
    # classic green, or the green alone when she is not found.
    bg = _load_route_bg(sw, sh)

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return None
                if event.key == pygame.K_F9 and save_available:
                    return "__LOAD__"
                key_pressed = event.unicode.upper()
                for route in ROUTES:
                    if key_pressed == route["key"]:
                        selected = route
                        running = False
                        break
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if save_available and lb_rect.collidepoint(event.pos):
                    return "__LOAD__"

        if bg is not None:   # v119: the postcard backdrop...
            screen.blit(bg, (0, 0))
        else:                # ...or the plain green she always wore
            screen.fill(BG_GREEN)
        # v120/v121: THE GLASS PANEL, RETIRED -- ROUTE_GLASS_ALPHA 0, so
        # this draws nothing and the writing sits straight on the
        # photograph. Raise the knob to bring the translucent pane back.
        _glass_panel(screen, box_x, int(sh * 0.05), box_w, int(sh * 0.88),
                     BOX_GREEN, ROUTE_GLASS_ALPHA, radius=12)
        title_text = "YOUR CHOICE OF ROUTE ?"
        render_text_shadow(screen, fonts["title"], "*   " + title_text + "   *", TITLE_GOLD, sw // 2, title_y, align="center")
        # The route box keeps only her blue border -- a picture frame
        # round the fourteen legs.
        pygame.draw.rect(screen, BORDER_BLUE,
                         (route_box_x, route_box_y, route_box_w, route_box_h),
                         width=8, border_radius=4)

        for i, route in enumerate(ROUTES):
            y = first_row_y + i * row_height
            key_text = route["key"] + ":"
            name_text = route["name"] + ("  *REAL TIME*" if route.get("real_time") else "")  # v56
            dist_text = str(route["dist"]) + "NM"
            name_w = fonts["route"].size(name_text)[0]
            dist_w = fonts["route"].size(dist_text)[0]
            dot_w = fonts["route"].size(".")[0]
            # Dots start after the route name, end before the distance text
            dots_start_x = col_name + name_w + 10
            dots_end_x = col_dist - dist_w - 10
            available = dots_end_x - dots_start_x
            n_dots = max(0, available // dot_w)
            dots = "." * n_dots
            render_text_shadow(screen, fonts["route"], key_text, TEXT_YELLOW, col_key, y, align="left")
            render_text_shadow(screen, fonts["route"], name_text, TEXT_YELLOW, col_name, y, align="left")
            render_text_shadow(screen, fonts["route"], dots, TEXT_YELLOW, dots_start_x, y, align="left")
            render_text_shadow(screen, fonts["route"], dist_text, TEXT_YELLOW, col_dist, y, align="right")

        render_text_shadow(screen, fonts["hint"], "Press the letter of your chosen route  |  [ESC] to quit",
                           TEXT_WHITE, sw // 2, int(sh * 0.92), align="center")

        if save_available:
            draw_box(screen, BOX_YELLOW, lb_rect.x, lb_rect.y, lb_rect.w, lb_rect.h, radius=8)
            render_text(screen, fonts["hint"], lb_label, TEXT_BLACK,
                        lb_rect.centerx, lb_rect.centery, align="center")
        else:
            draw_box(screen, DARK_GREY, lb_rect.x, lb_rect.y, lb_rect.w, lb_rect.h, radius=8)
            render_text(screen, fonts["hint"], lb_label, TEXT_DIM,
                        lb_rect.centerx, lb_rect.centery, align="center")
        pygame.display.flip()
    return selected
# ----------------------------------------------------------------------
#  SCREEN 3: ENROUTE BRIEFING
# ----------------------------------------------------------------------
def briefing_screen(screen, sw, sh, fonts, route, jet=None):
    clock = pygame.time.Clock()
    running = True
    orig_name, dest_name = route["name"].split("-")
    orig_ltr = AIRPORT_LETTERS.get(orig_name, "?")
    dest_ltr = AIRPORT_LETTERS.get(dest_name, "?")

    # Intermediate (enroute) airports: each star sits at its true
    # proportional distance from the origin along the dashed line.
    vias = route_vias(route)
    via_fracs = [max(0.02, min(0.98, v["dist"] / float(route["dist"])))
                 for v in vias]

    # When called from the HUD with [V], jet is passed in and the red
    # square on the route line shows the aircraft's live position.
    in_flight = jet is not None
    progress = 0.0
    if in_flight:
        progress = jet.dist_flown / float(route["dist"])

    pygame.event.clear()   # swallow any held/repeated keys from the caller

    # Silence the cockpit loops while the map is up: the engine hum,
    # wind rush and stall buzzer all fall quiet for the duration. The
    # cabin-atmosphere recording is the screen's own voice now (v84) --
    # it is raised again inside the draw loop below. When you return to
    # the HUD, audio_update() restores every loop on its next frame, so
    # the engine is heard again the moment you're back in the seat.
    audio_off()

    _blink_buzz_on = False   # tracks the fallback blink-buzzer (sounded
                             # only when the cruise recording never loaded)

    # The screen's backdrop (v89): the captain's photograph over the
    # classic green, or the green alone when she is not found. From here
    # on, everything the screen "erases" -- the dashes behind the
    # airport stars, the travelling gap the Learjet parts the line with
    # -- must restore the BACKDROP, not paint bare green, or the
    # photograph would show green wounds.
    bg = _load_enroute_bg(sw, sh)

    def wipe(rect):
        """Restore one rectangle of the screen's backdrop."""
        rect = pygame.Rect(rect).clip(screen.get_rect())
        if rect.width <= 0 or rect.height <= 0:
            return
        # Restore from the backdrop ONLY when it covers the live screen
        # exactly; otherwise fall back to the plain green -- a partial
        # restore is what lets old writing linger as a ghost image.
        if bg is not None and bg.get_size() == (sw, sh):
            screen.blit(bg, rect.topleft, rect)
        else:
            pygame.draw.rect(screen, BG_GREEN, rect)

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_enroute_sound()
                return False
            if event.type == pygame.KEYDOWN:
                stop_enroute_sound()    # never leave the screen's voice sounding
                if in_flight:
                    return True             # any key = back to the cockpit
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_r:
                    # v63: [R] back to Route Selection -- offered only
                    # BEFORE the flight begins; once she is under way
                    # (the [V] peek above) every key returns to the
                    # cockpit, so the offer can never appear mid-flight.
                    return "routes"
                else:
                    return True

        # A full, opaque repaint EVERY frame, no exceptions: the one
        # way writing can appear doubled on this screen is a frame that
        # was not completely cleared underneath it.
        if bg is not None and bg.get_size() == (sw, sh):
            screen.blit(bg, (0, 0))
        else:
            screen.fill(BG_GREEN)
        title_text = "(%s)*%s*(%s)" % (orig_ltr, route["name"], dest_ltr)
        render_text(screen, fonts["title"], title_text, TEXT_YELLOW, sw // 2, int(sh * 0.10), align="center")

        bar_w = int(sw * 0.70)
        bar_h = int(sh * 0.02)          # half the original thickness
        bar_x = (sw - bar_w) // 2
        bar_y = int(sh * 0.14)
        draw_box(screen, BOX_RED, bar_x, bar_y, bar_w, bar_h, radius=2)

        # ---------- FULL-WIDTH ROUTE LINE + RED POSITION SQUARE ----------
        line_y = int(sh * 0.54)
        line_left = int(sw * 0.02)                     # extreme left
        line_right = int(sw * 0.98)                    # extreme right
        line_span = line_right - line_left

        lfont = fonts["label"]
        dash_w, _ = lfont.size("-")
        star_w, _ = lfont.size("*")

        # Tile dashes from the extreme left to the extreme right
        n_dashes = max(1, line_span // dash_w)
        dash_img = lfont.render("-" * n_dashes, True, TEXT_YELLOW)
        dash_rect = dash_img.get_rect()
        dash_rect.left = line_left
        dash_rect.centery = line_y
        screen.blit(dash_img, dash_rect.topleft)

        # Where the dash and star INK actually sits (the "-" glyph rides
        # a touch off the line box's centre in most fonts): the Learjet
        # erases exactly this strip as she passes (v85) -- the dashes
        # and stars part for her and close again behind her.
        dash_probe = lfont.render("-", True, TEXT_YELLOW)
        star_probe = lfont.render("*", True, TEXT_YELLOW)
        d_ink = dash_probe.get_bounding_rect()
        s_ink = star_probe.get_bounding_rect()
        dash_cy = line_y + d_ink.centery - dash_probe.get_height() // 2
        strip_top = min(dash_cy - d_ink.height // 2,
                        line_y - s_ink.height // 2) - 3
        strip_bot = max(dash_cy + d_ink.height // 2,
                        line_y + s_ink.height // 2) + 3

        # Stars at both ends and at each enroute airport's true
        # proportional position, on top of the dashes. The asterisk
        # glyph rides high in the font's line box while the dashes sit
        # at mid-height, so centre the star's INK on the line --
        # otherwise every star floats above the dashes.
        for pos in [0.0] + via_fracs + [1.0]:
            star_img = lfont.render("*", True, TEXT_YELLOW)
            star_ink = star_img.get_bounding_rect()
            sr = star_img.get_rect()
            sr.centerx = int(line_left + pos * line_span)
            sr.centery = line_y
            wipe(sr)     # erase dashes behind: the BACKDROP, not bare green
            screen.blit(star_img, (sr.centerx - star_ink.centerx,
                                   line_y - star_ink.centery))

        # ---------- THE LEARJET THREADED ON THE LINE (v84/v85/v86) ----
        # A top-down photograph of the Learjet flies the dashed line in
        # place of the old blinking red square: her NOSE TIP marks the
        # aircraft's position (progress 0.0 = extreme left, the start;
        # 1.0 = extreme right, the arrival). On course the fuselage sits
        # right ON the dashes, so the line threads in through her tail
        # and out her nose -- and the dashes, and the stars, PART as
        # she approaches a point: the strip of line she occupies is
        # erased tail-to-nose just before she is drawn, and it closes
        # again behind her as she passes, a travelling gap exactly her
        # length. v86: flown OFF course she diverges from the line
        # again -- riding above or below it by the cross-track error,
        # full drift at 2 nm off, exactly as the square used to; the
        # travelling gap stays ON the route line at her along-track
        # station, her shadow on the planned track, while she rides at
        # her true offset beside it. The LEFT end of the route cannot
        # take the whole airframe, so over the first ENROUTE_PLANE_BUILD
        # of the route she BUILDS UP from the nose -- a sliver of nose
        # at the origin, the tail growing out behind her. v89: the
        # arrival dissolve is RETIRED -- she used to melt away from the
        # tail over the last of the route until only the feathered nose
        # cone was left, which read as the aeroplane decaying on
        # approach; she now carries the whole airframe all the way to
        # the destination star, her nose tip true on the position to
        # the last. If the photograph is missing the old blinking red
        # square stands in, exactly as before.
        frac = max(0.0, min(1.0, progress))
        pos_x = int(line_left + frac * line_span)
        # Off-course drift: while viewing from the cockpit with [V], she
        # rides ABOVE or BELOW the dashed line by the aircraft's
        # cross-track error, so you can see at a glance how the
        # navigation is going.
        mark_drift = 0
        if in_flight:
            mark_drift = int(max(-1.0, min(1.0, getattr(jet, "xte", 0.0) / 2.0)) * sh * 0.06)
        mark_y = line_y - mark_drift
        square_on = (pygame.time.get_ticks() // 500) % 2 == 0
        plane = _load_enroute_plane(sw, sh)
        if plane is not None:
            surf, nose_x, nose_y = plane
            pw, ph = surf.get_width(), surf.get_height()
            show = 1.0
            if frac < ENROUTE_PLANE_BUILD:
                # Building up: the nose first, the tail growing out
                # behind her (ENROUTE_PLANE_MIN keeps a sliver of nose
                # on show at the origin, so the marker never quite
                # vanishes before she has moved). There is NO matching
                # dissolve at the far end any more (v89) -- she arrives
                # whole.
                show = max(frac / ENROUTE_PLANE_BUILD, ENROUTE_PLANE_MIN)
            if show >= 1.0:
                view, keep = surf, pw
            elif show > 0.01:
                keep = max(1, int(round(pw * show)))
                view = surf.subsurface((pw - keep, 0, keep, ph)).copy()
                # Feather the cut edge: a soft alpha ramp over the
                # clipped (left) quarter of the view, so the airframe
                # grows in and melts away instead of shearing -- a
                # wingtip tank caught mid-slice fades rather than
                # hanging there detached.
                ramp_w = max(1, keep // 4)
                ramp = pygame.Surface((keep, ph), pygame.SRCALPHA)
                ramp.fill((255, 255, 255, 255))
                for rx in range(ramp_w):
                    pygame.draw.line(
                        ramp, (255, 255, 255, int(255 * rx / ramp_w)),
                        (rx, 0), (rx, ph))
                view.blit(ramp, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            else:
                view, keep = None, 0       # arrived: she is gone
            if view is not None:
                # The clip keeps the nose end: the tip rides at the
                # view's right edge, still exactly on the position.
                blit_x = pos_x - nose_x + pw - keep
                # First the line parts for her -- the strip she occupies,
                # tail to nose, is erased (dashes AND stars). The gap
                # stays ON the route line even when she is drifting off
                # it: her along-track station on the planned track.
                wipe((blit_x, strip_top, keep, strip_bot - strip_top))
                # ... then she settles onto her place: threading the
                # gap on course, riding beside it when she is not.
                screen.blit(view, (blit_x, mark_y - nose_y))
        else:
            # Fallback: the blinking red square, as she always was.
            sq = int(star_w * 1.2)
            if square_on:
                pygame.draw.rect(screen, BOX_RED,
                                 (pos_x - sq // 2,
                                  mark_y - sq // 2, sq, sq))

        # The screen's voice (v84): the chirping blink-buzzer is
        # retired -- the cabin-atmosphere recording already heard on
        # the HUD plays while the map is up, steady, [M] muting it as
        # ever. audio_off() above hushed the cockpit loops (and the
        # recording); here the recording is simply raised again for as
        # long as the screen shows, and stop_enroute_sound() drops it
        # on the way out -- the cockpit's audio_update() re-raises it
        # on the next frame back, exactly as before. If the recording
        # never loaded, the old blink-buzz carries on as the fallback.
        if AUDIO_OK and _cruise_music_ok:
            try:
                pygame.mixer.music.set_volume(
                    0.0 if _sound_muted else CRUISE_MUSIC_VOL)
            except Exception:
                pass
        elif square_on != _blink_buzz_on:
            # Fallback voice (v7): buzz with the blink, on the instant
            # the marker comes ON and silent the instant it goes OFF.
            _blink_buzz_on = square_on
            if AUDIO_OK:
                try:
                    if square_on and not _sound_muted:
                        _ch_buzz.set_volume(0.45)
                    else:
                        _ch_buzz.set_volume(0.0)
                except Exception:
                    pass
        if in_flight and abs(getattr(jet, "xte", 0.0)) > 0.3:
            side = "RIGHT" if jet.xte > 0 else "LEFT"
            # v86: the message keeps to the OPPOSITE side of the line
            # from the drifting airframe, placed beyond her furthest
            # reach, so she can never sit on the words that name her
            # wanderings.
            if mark_drift > 0:   # she rides ABOVE the line
                reach = (plane[0].get_height() - plane[2]) if plane else int(sh * 0.01)
                oc_y = line_y + reach + int(sh * 0.012)
            else:                # she rides BELOW the line
                oc_y = line_y - int(sh * 0.03) - fonts["small"].get_height()
            render_text(screen, fonts["small"],
                        "OFF COURSE: %.1f nm %s of track" % (abs(jet.xte), side),
                        BOX_RED, sw // 2, oc_y, align="center")

        # ---------- ICAO CODES + ALTITUDES AT THE LINE ENDS ----------
        orig_icao = AIRPORT_ICAO.get(orig_name, "????")
        dest_icao = AIRPORT_ICAO.get(dest_name, "????")

        icao_y = line_y - int(sh * 0.160)   # top line: the ICAO code
        alt_y  = line_y - int(sh * 0.127)   # under it: ALT xxFT
        row3_y = line_y - int(sh * 0.094)   # bottom line: heading / distance

        # Origin airport: extreme left, above the dashed line,
        # with the outbound heading tucked under the ALT readout
        render_text(screen, lfont, orig_icao, TEXT_YELLOW, line_left, icao_y, align="left")
        render_alt_ft(screen, lfont, int(origin_elev(route)), line_left, alt_y, align="left")
        render_text(screen, lfont, "HDG OUT %d°" % route["hdg"], TEXT_YELLOW, line_left, row3_y, align="left")

        # Destination airport: extreme right, above the dashed line,
        # with distance-from-origin + origin ICAO under its ALT readout
        render_text(screen, lfont, dest_icao, TEXT_YELLOW, line_right, icao_y, align="right")
        render_alt_ft(screen, lfont, route["elev"], line_right, alt_y, align="right")
        dist_txt = "%03d%s" % (route["dist"], orig_icao)
        render_text(screen, lfont, dist_txt, TEXT_YELLOW, line_right, row3_y, align="right")

        # Intermediate airports: each centred on its own star, showing the
        # same information as the origin and destination airports --
        # ICAO code, elevation, and distance-from-origin readout
        for v, frac in zip(vias, via_fracs):
            via_x = int(line_left + frac * line_span)
            render_text(screen, lfont, AIRPORT_ICAO.get(v["name"], "????"),
                        TEXT_YELLOW, via_x, icao_y, align="center")
            render_alt_ft(screen, lfont, int(v["elev"]),
                          via_x, alt_y, align="center")
            via_dist_txt = "%03d%s" % (int(round(v["dist"])), orig_icao)
            render_text(screen, lfont, via_dist_txt,
                        TEXT_YELLOW, via_x, row3_y, align="center")

        info_y = int(sh * 0.79)
        info_txt = ("Distance: %d nm  |  Suggested FL: FL%d  |  Fuel: %d lb"
                    % (route["dist"], route["fl"], int(route_fuel(route))))
        if route.get("real_time"):   # v56: say so before the captain commits
            info_txt += "  |  REAL TIME - the clock runs 1:1"
        render_text(screen, fonts["body"], info_txt, TEXT_DIM, sw // 2, info_y, align="center")

        prompt_y = int(sh * 0.88)
        pulse = int(128 + 127 * abs(math.sin(pygame.time.get_ticks() / 800)))
        if in_flight:
            render_text(screen, fonts["prompt"], "Press any key to return to the cockpit ...",
                        (pulse, pulse, pulse), sw // 2, prompt_y, align="center")
        else:
            render_text(screen, fonts["prompt"], "Press any key to taxi onto the runway ...",
                        (pulse, pulse, pulse), sw // 2, prompt_y, align="center")
            render_text(screen, fonts["small"], "[R] back to Route Selection      [ESC] to quit", TEXT_WHITE, sw // 2, prompt_y + int(sh*0.04), align="center")
        pygame.display.flip()


# ----------------------------------------------------------------------
#  THE AIRPLANE CLASS
# ----------------------------------------------------------------------
class Jet:
    # v51: every INFO: message carries the sim-time it was posted.  A
    # message not re-asserted for MSG_TTL_S sim-seconds is cleared by
    # step(); continuous warnings (STALL!, CAB PRESS...) re-post every
    # step, so they stay lit while their condition holds and fade 30
    # sim-seconds after it ends.
    @property
    def msg(self):
        return getattr(self, "_msg", "")

    @msg.setter
    def msg(self, text):
        self._msg = text
        self._msg_t = getattr(self, "elapsed", 0.0)

    def __init__(self, route):
        self.route = route
        self.dme = float(route["dist"])
        self.dist_flown = 0.0      # nm travelled from origin (DME + channel)
        self.dme_chan = "-"        # "-" = dist to destination, "+" = dist from
                                   # origin, "v0","v1" ... = each enroute field
        # Like the VZ-200 original, she starts 90 degrees OFF the
        # runway heading -- the takeoff is always into the wind, so
        # the first job after engine start is to turn her round with
        # [A]/[D] until HDG reads the runway heading.
        self.hdg = (float(route["hdg"]) - 90.0) % 360.0
        self.bug = float(route["hdg"])   # the runway heading: the target
        self.obs = float(route["hdg"])  # OBS course: auto-set at start to
                                        # the course bearing for the airport
        self.xte = 0.0                  # cross-track error, nm
                                        # (+ = right of the course line)
        self.off_course_said = False
        # v25: the fly-around advisory has spoken for THIS overshoot --
        # re-arms once she is a mile back out from the field.
        self.overshoot_said = False
        # Enroute stopover (v22): after a full stop at an intermediate
        # airport the captain may continue the flight -- parked on the
        # runway, free to rotate at ANY heading (the into-wind rule is
        # waived for that one departure; cleared again at liftoff).
        self.free_departure = False
        # ...or may press [R] instead, which sets this flag so main()
        # goes straight back to Route Selection, no flight summary.
        self.to_routes = False
        # [Z] abandon (v24): the first press puts this offer on the
        # table -- a second, fresh [Z] (or a click on the flashing
        # placard) confirms and hands the flight back to Route
        # Selection; any other key flies on.
        self.abandon_offer = False
        # DESKTOP double-check (v73): the first click on the DESKTOP
        # button only MAKES the offer -- the button itself becomes a
        # flashing DESKTOP? placard, and a second click on it confirms;
        # any other click, or any key, cancels and flies on (the [Z]
        # routine, brought to the mouse).
        self.desktop_offer = False
        # Gentle wind aloft: which way the heading wanders this flight
        # (left or right, picked once at the start of the flight).
        self.wind_drift_dir = random.choice((-1.0, 1.0))
        # The SURFACE WIND SHOW (v68): the per-airport DISPLAY-ONLY wind
        # speeds the INFO line reads, {airport name: figure} -- each
        # drawn from the 10-30 range the first time the airport is tuned
        # on the DME, then held for the rest of the flight (see
        # surface_wind_show). FOR SHOW ONLY: the flight model reads
        # nothing of it; the gentle wander above is the only wind she
        # feels. The dict travels with the save; an old save simply
        # draws its figures as they are first asked for.
        self.wind_show = {}
        self.ias = 0.0
        self.alt = origin_elev(route)
        self.vsi = 0.0
        self.vsi_cmd = 0.0
        self.level_cap = False     # nuanced [L] level-off capture in progress
        self.level_target = 0.0    # altitude to level at (alt when [L] pressed)
        self.level_phase = 0       # 0=ease to a stop, 1=shallow dip, 2=settle,
                                   # 3=holding the captured level (v23)
        self.level_dip = 0.0       # the "just below/above" point of the dip
        self.level_dir = 1         # +1 pressed while climbing, -1 descending
        self.thrust = 0.0
        self.n1 = 0.0
        self.itt = 15.0
        self.fuel = route_fuel(route)   # published figure + 25% (v30)
        self.flap = 0
        self.flap_lift = 0.0       # flap-lift balloon (fpm), slewed in step()
        self.gear_down = True
        # Progressive gear lights: [top(E), bottom-left, bottom-right].
        # Raising the gear puts them out one at a time in the order
        # top -> bottom-right -> bottom-left; lowering it brings them
        # back on in reverse, ending with "three greens".
        self.gear_lights = [True, True, True]
        self.gear_seq_dir = 0        # 0 = idle, -1 = retracting, +1 = extending
        self.gear_t = 0.0            # sim-seconds since the transit began
        self.door_light = True       # the yellow *D placard (lit = gear down)
        self.door_delay = -1.0       # sim-s until the *D may change (-1 = idle)
        self.brakes = True
        self.reverser = False        # [R] on the runway: buckets out, engine
                                     # power brakes you (works WITH brakes)
        self.engines = False
        self.eng_start_t = None  # sim-time the engines were (last) started,
                                 # drives the spinning diagonal cells
        self.ap = False
        self.ass_fl = 0
        self.airborne = False
        self.rollout = False
        self.dead = False
        self.done = False
        self.quit = False
        self.paused = False          # [SPACE] or the PAUSE button freezes the world
        self.landing_snd_on = False  # v63: the landing recording is looping
                                     # (the led 400 ft mark -- v66 --
                                     # down to the full stop)
        self.why = ""
        self.elapsed = 0.0
        # The REAL countdown's per-leg bookkeeping (v55): the countdown
        # RESETS at every intermediate stopover, so the current leg runs
        # on its own clock and its own budget. leg_elapsed0 is the sim-
        # time this leg began (0 = the origin brake-release); leg_base_min
        # is the measured sim-minute budget of the field this leg started
        # FROM (0 = the origin). Both are re-armed by enroute_departure()
        # when the captain presses [C] at the stopover prompt.
        self.leg_elapsed0 = 0.0
        self.leg_base_min = 0.0
        # The LIVE ETA's cache (v80): the ghost flight's last answer and
        # the sim-time it was flown at, so the panel ticks the figure
        # down live between recomputes instead of flying the ghost every
        # frame. The key is the configuration the answer belongs to --
        # any change (flap, gear, engines, autoland, brakes, DME channel)
        # re-flies the ghost on the spot.
        self._eta_val = None
        self._eta_t = None
        self._eta_key = ""
        # REAL TIME legs (v56): TOWNSVILLE-CAIRNS and KARRATHA-PERTH fly
        # at an honest 1:1 clock -- no compression at all, every minute
        # aloft a minute of yours. The scale travels WITH the flight (not
        # the global TIME_SCALE dial), so the world's step, the ETA box's
        # countdown conversion and a reloaded save all read the leg's own
        # figure. The other twelve legs run the usual 2.9.
        self.time_scale = 1.0 if route.get("real_time") else TIME_SCALE
        self.touch_vsi = 0.0
        self.gs_dev = None
        self.gs_frac = None       # angular G/S deviation, -1..+1 (v46)
        self.gs_alive = False
        self.landed_name = None    # airport actually touched down at
        self.landed_elev = 0.0
        self.landed_dist = 0.0     # nm from origin to the end of its runway
        # Per-enroute-airport flags, keyed by airport name (a route can
        # carry several enroute fields -- Brisbane-Townsville has two).
        # via_said: the "airport ahead" callout has been made.
        # via_done: the airport is genuinely behind us -- overflown past
        # its runway, landed on, or crossed low over its threshold
        # (touch-and-go / go-around). From then on the sim stays quiet
        # about it: no more advisories for that airport.
        self.via_said = {}
        self.via_done = {}
        # Time-based descent guidance: the last advisory line shown at
        # INFO (kept so the same advice is never repeated twice).
        self.guid_last = ""
        self.autoland = False        # [Y] accepted: the autopilot lands the jet
        self.al_offer = False        # AUTOLAND invitation currently on the table
        self.al_offer_t = 0.0        # sim-time the invitation appeared
        self.al_offer_apt = None     # airport the current invitation is for
        self.al_apt = None           # airport the autoland is flying to
        self.al_done = []            # airports whose invitation has expired
        self.al_expire_t = -999.0    # sim-time the offer expired (message
                                     # gets a few quiet seconds at INFO)
        self.spd_warn = False        # INFO currently shows one of OUR speed
                                     # warnings -- cleared when speed is back
        self.low_fuel_said = False
        self.said_empty = False
        # CAB PRESS: the pressurisation light is out, but the clock is
        # already ticking toward the first possible failure -- a very
        # infrequent, random sim-time. It can only strike above 10,000
        # ft, and only descending below 10,000 ft puts it out again.
        self.cab_light = False
        self.cab_next_t = random.uniform(CAB_PRESS_MIN_S, CAB_PRESS_MAX_S)
        # Attitude Indicator: live pitch and bank, updated in step()
        self.pitch = 0.0          # degrees, + = nose up
        self.bank = 0.0           # degrees, + = right wing down
        self.bank_target = 0.0    # where bank is trying to go
        self.bank_turn_t = 0.0    # sim-time of last turn command
        # v46: the approach chop while the AUTOPILOT has her -- two slow
        # random walks (heading degrees, vertical fpm) that her steering
        # and path laws chase back, so the corrections show on the AI
        # needle, the CDI and the glideslope tape. ap_tex fades the
        # texture out through the last 600 feet of the approach.
        self.ap_gust_h = 0.0
        self.ap_gust_v = 0.0
        self.ap_tex = 0.0
        # Flight recorder: the crash debrief reads these to review the
        # whole flight and rate the handling as a percentage.
        self.airborne_time = 0.0        # sim-seconds in the air
        self.hours_committed = 0.0      # v78: how much of airborne_time is
                                        # already banked into the career
                                        # flight-hours file -- a save/load
                                        # can neither lose nor double-count
        self.dist_committed = 0.0       # v87: how much of dist_flown is
                                        # already banked into the logbook's
                                        # career distance -- the same
                                        # save/load-safe marker as the hours
        self.cab_survivals = 0          # v87: pressurisation failures
                                        # survived this flight (the light
                                        # went out below 10,000 ft)
        self.max_alt = origin_elev(route)
        self.gear_raised = False        # wheels came up while airborne
        self.flaps_used = False         # flap 10+ at low speed, airborne
        self.gear_down_low = False      # wheels down low near the field
        self.gs_time = 0.0              # sim-seconds within 150 ft of G/S
        self.stall_count = 0
        self.in_stall = False
        self.overspeed_count = 0
        self.gear_overspeed_count = 0
        self.flap_overspeed_count = 0
        self.warn_kind = ""             # active speed-warning category
        self.warn_msg = ""              # the exact speed-warning text at
                                        # INFO, so retiring it clears ONLY
                                        # its own message, never another
        self.terrain_count = 0
        self.terrain_now = False
        self.offcourse_count = 0
        # v56: on a REAL TIME leg the very first INFO line says so.
        if route.get("real_time"):
            self.msg = ("REAL TIME leg - the clock runs 1:1, every minute "
                        "aloft is a minute of yours. Start engines [E] when "
                        "ready. Settle in, captain.")
        else:
            self.msg = "Start engines [E] when ready."


def into_wind(j):
    """True when the jet is lined up on the runway heading (within half
    a 5-degree turn step -- so, in practice, exactly on it). Rotation
    is refused until she points into the wind."""
    rwy = float(j.route["hdg"])
    return abs((j.hdg - rwy + 540.0) % 360.0 - 180.0) < 2.6


def on_obs(j):
    """True when HDG matches the OBS course readout (within half a
    5-degree turn step -- so, in practice, exactly on it). v24: on the
    ground at the origin the engines may only IDLE for the turn onto
    the runway -- no thrust for the roll until HDG reads what OBS
    reads."""
    obs = getattr(j, "obs", float(j.route["hdg"]))
    return abs((j.hdg - obs + 540.0) % 360.0 - 180.0) < 2.6


def taxi_turn_msg(j):
    """INFO line for a ground turn: count down to the runway heading,
    then the all-clear to roll once she is into wind."""
    rwy = int(j.route["hdg"])
    if getattr(j, "free_departure", False):
        # Enroute-stop departure (v22): silent -- the [C] "Depart ...
        # resume flight" message already says it all for this one.
        return
    if into_wind(j):
        j.msg = "Into wind, runway %03d! Brakes off [B], full thrust [+]." % rwy
    else:
        j.msg = "Taxi turn ... HDG %03d, runway is %03d." % (int(j.hdg), rwy)


def stall_speed(j):
    # Real Learjet 35: ~110 kt clean. Must stay BELOW the 125 kt rotation
    # speed or the stall pusher forces the nose down right after liftoff.
    return 110.0 - j.flap * 0.85 + (4.0 if j.gear_down else 0.0)


def mach_number(ias_kt, alt_ft):
    """The Mach number for the panel's IAS/MACH changeover (v38).
    Arcade-accurate: true airspeed grows about 2% per 1,000 ft over the
    indicated, and the speed of sound falls from 661.7 kt at sea level
    with the standard lapse, settling at 573.8 kt in the stratosphere
    (above 36,089 ft the air stops getting colder)."""
    tas = ias_kt * (1.0 + 0.02 * (alt_ft / 1000.0))
    if alt_ft < 36089.0:
        a = 661.7 * math.sqrt(max(0.05, 1.0 - 1.9812 * (alt_ft / 1000.0) / 288.15))
    else:
        a = 573.8
    return tas / a


def flap_lift_fpm(j):
    """Extra lift (feet per minute) from flap extension, airborne only.

    Extending flap at speed genuinely adds lift: the nose balloons and
    the VSI shows it, so you re-trim with [S]. Retracting flap takes the
    lift away again. The effect is strongest at approach speeds, fades
    out toward the flap overspeed limits, and fades in below 120 kt as
    the airflow over the flap builds. Full flap 50 at 120-170 kt gives
    the maximum balloon of about +350 fpm; flap 20 gives +140 fpm."""
    if not j.airborne or j.flap <= 0:
        return 0.0
    ias = j.ias
    if ias < 80.0:
        speed_f = 0.0
    elif ias < 120.0:
        speed_f = (ias - 80.0) / 40.0
    elif ias <= 170.0:
        speed_f = 1.0
    elif ias < 260.0:
        speed_f = (260.0 - ias) / 90.0
    else:
        speed_f = 0.0
    return 350.0 * (j.flap / 50.0) * speed_f


def ground_elev(j):
    """Terrain elevation under the aircraft, interpolated piecewise
    origin -> each enroute airport in turn -> destination."""
    r = j.route
    pos = r["dist"] - j.dme       # nm from the origin start line
    pts = [(0.0, origin_elev(r))]
    for v in route_vias(r):
        pts.append((v["dist"], v["elev"]))
    pts.append((float(r["dist"]), float(r["elev"])))
    for (d0, e0), (d1, e1) in zip(pts, pts[1:]):
        if pos <= d1:
            frac = max(0.0, min(1.0, (pos - d0) / (d1 - d0))) if d1 > d0 else 1.0
            return e0 + (e1 - e0) * frac
    return pts[-1][1]


def route_airports(route):
    """Airports that can be landed at, in route order. Each airport's
    'dist' is nm from the origin start line to the END of its runway."""
    apts = [{"name": v["name"], "elev": v["elev"], "dist": v["dist"]}
            for v in route_vias(route)]
    apts.append({"name": route["name"].split("-")[1],
                 "elev": float(route["elev"]), "dist": float(route["dist"])})
    return apts


def next_airport(j):
    """The next airport ahead of the aircraft (the one it could land at
    now): each enroute airport in turn until it is behind us, then the
    destination."""
    pos = j.route["dist"] - j.dme
    for apt in route_airports(j.route):
        if pos <= apt["dist"] + 0.3:
            return apt
    return route_airports(j.route)[-1]


# ----------------------------------------------------------------------
#  GENTLE WIND ALOFT -- a slow heading wander. The heading drifts by
#  WIND_DRIFT_DEG degrees every WIND_DRIFT_MIN minutes, so over a long
#  flight the CDI needle quietly walks off the course line and you must
#  occasionally nudge back on. (1.5 deg per 30 min = ~3 deg per hour.)
# ----------------------------------------------------------------------
WIND_DRIFT_DEG = 0.0   # TEMPORARILY DISABLED (was 1.5) -- no wind
                       # drift, so the CDI needle stays where it is put.
                       # Restore 1.5 to bring the gentle drift back.
WIND_DRIFT_MIN = 30.0
WIND_DRIFT_DPS = WIND_DRIFT_DEG / (WIND_DRIFT_MIN * 60.0)

# ITT gauge response: the temperature needles CHASE their target at a
# steady rate instead of snapping to it -- a lazy thermal lag of SEVERAL
# MINUTES for a full-throttle swing, in BOTH directions, so the gauges
# wind up slowly on throttle-up and wind down just as slowly when the
# thrust comes back. Rates are per SIM-second (the sim runs 6x real
# time): 0.8 up means the full ~720 degC swing takes about two and a
# half real minutes; 0.6 down takes nearly three and a half -- turbine
# metal always cools slower than it heats. Raise for a quicker gauge,
# lower for an even lazier one.
ITT_UP_DPS = 0.8     # degC per sim-second while heating (~2.5 real min full swing)
ITT_DOWN_DPS = 0.6   # degC per sim-second while cooling (~3.5 real min full swing)

# AUTOLAND: with the autopilot on and the next airport ahead inside this
# range -- the enroute field or the destination (v19: the offer used to be
# destination-only) -- INFO offers an automatic landing; the offer stays
# on the table for this many seconds, then a manual landing at that field
# is assumed and late [Y] is refused. The offer comes with the glideslope
# itself -- 100 NM out -- so an early [Y] hands her the whole 3-degree
# path from a long way downrange.
AL_OFFER_NM = 100.0
AL_OFFER_SECS = 30.0
# v59: KARRATHA-PERTH alone invites the AUTOLAND this far out -- 200 NM
# from EVERY field on the route, Carnarvon and Perth alike -- so the
# descent to the 3-degree path has ample time at the prescribed rate
# (the v57 1,400 fpm cap) even from the high cruising levels. The v47
# guard stands behind the early Carnarvon offer: engaged low, far out
# and below the beam, she holds her height until the path comes down.
AL_OFFER_NM_KP = 200.0
# v51: INFO: messages are removed 30 sim-seconds after they were posted -
# the same thirty the AUTOLAND window counts (v27 taught that INFO times
# are sim time).
MSG_TTL_S = 30.0

# THE THREE-SECOND ARRIVAL (v73): at the full stop -- Intermediate or
# Destination alike -- the panel holds the landed details EXACTLY as they
# are for this many REAL seconds before the continue options are offered
# (the [C]/[R] stopover choice, or the any-key road to the flight
# summary). All sound continues through the hold -- audio_update reads
# the same deadline (see _landed_hold_until) and keeps the full-stop
# hush off until the options appear.
LANDED_HOLD_S = 3.0

# CAB PRESS failures: at very infrequent, random times while the jet is
# above 10,000 ft the pressurisation light comes on, and it burns until
# she is brought below 10,000 ft. Once clear she may climb back to her
# level -- the clock quietly re-arms for the next, equally rare,
# failure, just as it used to occur in the original game. The figures
# are sim-seconds: one possible failure every 15-25 sim-hours aloft --
# one in twenty hours' flying on average, so effectively hardly ever
# (v76; was every 20-70 sim-minutes). And the v72 rule stands: no
# failures at all on the two 1:1 REAL TIME legs.
CAB_PRESS_MIN_S = 15.0 * 3600.0
CAB_PRESS_MAX_S = 25.0 * 3600.0

# THE GLIDE (v37): with the engines dead -- fuel exhausted, or shut
# down in the air -- the jet is a glider: GLIDE_NM_PER_10K nautical
# miles for every 10,000 ft of height, about 15:1, the real Learjet's
# own figure, in the clean configuration at best-glide speed (~150
# kt). GLIDE_BOOST strengthens the descent speed-credit while she is
# engineless, sized so 150 kt clean holds her speed at a ~1,000 fpm
# sink. Dirty or fast steepens the glide, exactly as it should.
GLIDE_NM_PER_10K = 25.0
GLIDE_BOOST = 4.55


def step(j, h):
    if j.dead or j.done:
        return
    j.elapsed += h
    # v51: retire an INFO: message that has not been re-asserted for
    # MSG_TTL_S sim-seconds.  Pause and the dead/done early-return above
    # freeze the clock, so a parked or finished flight keeps its last word.
    if j.msg and j.elapsed - getattr(j, "_msg_t", j.elapsed) > MSG_TTL_S:
        j.msg = ""

    # Flight recorder for the post-crash review: air time, highest
    # altitude, and honest configuration habits, gathered as we go.
    if j.airborne:
        j.airborne_time += h
        j.max_alt = max(j.max_alt, j.alt)
        if not j.gear_down:
            j.gear_raised = True
        if j.flap >= 10 and j.ias < 180.0:
            j.flaps_used = True

    want_n1 = 0.0
    if j.engines and j.fuel > 0.0:
        want_n1 = max(j.thrust, 18.0)
        if (not j.airborne and not j.rollout
                and not getattr(j, "free_departure", False)
                and not on_obs(j)):
            # v24: THE OBS GATE -- at the origin she may only idle for
            # the turn onto the runway; the lever stays where the pilot
            # put it, but the engines hold idle until HDG reads what
            # OBS reads. (The enroute-stop departure, free to roll at
            # any heading, is exempt.)
            want_n1 = min(want_n1, 18.0)
    j.n1 += max(-35.0 * h, min(20.0 * h, want_n1 - j.n1))

    itt_want = 15.0 + j.n1 * 8.75
    itt_rate = ITT_UP_DPS if itt_want > j.itt else ITT_DOWN_DPS
    j.itt += max(-itt_rate * h, min(itt_rate * h, itt_want - j.itt))

    # v57: FUEL FOR HEIGHT -- the flow scales with altitude on the
    # captain's table (FL200 the baseline, 52% saved by FL450).
    burn = (j.n1 / 100.0) * 2500.0 / 3600.0 * fuel_flow_factor(j.alt)
    j.fuel = max(0.0, j.fuel - burn * h)
    if j.fuel <= 0.0 and not j.said_empty:
        j.said_empty = True
        j.engines = False   # both engines flamed out -- a glider now (v37)
        j.msg = ("FUEL EXHAUSTED - both engines flamed out! She glides ~25 NM "
                 "per 10,000 ft: clean her up [F][G], hold 150 kt, land soon.")
        play_bing("bing2")
    elif j.fuel < 600.0 and not j.low_fuel_said:
        j.low_fuel_said = True
        j.msg = "LOW FUEL - less than 600 lb remaining."
        play_bing("bing2")

    drag = 6.0 + (j.ias / 260.0) ** 2 * 34.0
    # Flap drag: a gentle linear term PLUS a mild quadratic term, so the
    # landing settings (30-50) are noticeably draggy like the real jet --
    # flap 10 -> +5, 20 -> +11, 30 -> +17, 40 -> +24, 50 -> +33 units
    # (was +4.5/+9/+13.5/+18/+22.5). Holding 120-140 kt on final with
    # flap 40 and gear down now asks for roughly three-quarter thrust,
    # and pulling the power washes the speed off promptly.
    # Flap AND gear drag are aerodynamic, so they scale with dynamic
    # pressure (full strength at 140 kt, fading as the jet slows) --
    # this is what lets the rollout run long instead of grabbing.
    qf = (j.ias / 140.0) ** 2
    drag += (j.flap * 0.45 + (j.flap / 10.0) ** 2 * 0.4) * qf
    if j.gear_down:
        drag += 10.0 * qf
    if j.brakes:
        # Gentle wheel brakes: a normal 120-140 kt touchdown rolls
        # 1,650-1,870 m -- most of the 2,000 m runway -- before the
        # full stop. (Was a fierce +45: stopped in about 400 m.)
        drag += 10.0 if not j.airborne else 6.0
    # Reverse thrust: with the buckets out on the ground, engine power
    # pushes BACKWARD -- the more N1, the harder the braking. It scales
    # with dynamic pressure like the real thing: a strong helper at
    # touchdown speed, fading as the jet slows (the wheel brakes still
    # do the work at walking pace). Full reverse alone stops a 130 kt
    # arrival in ~1,200 m; brakes AND reverse together in ~800 m.
    if not j.airborne and j.reverser:
        accel = (-j.n1 * 0.25 * qf - drag) * 0.14
    else:
        accel = (j.n1 * 0.62 - drag) * 0.14
    # v53: standing brakes HOLD her. With the brakes on, engine power
    # alone can no longer start her rolling or wind her speed up -- she
    # moves only when [B] lets the brakes off. (Braking a rolling jet is
    # untouched: the brakes' drag still washes the speed off.)
    if not j.airborne and j.brakes and accel > 0.0:
        accel = 0.0
    if j.airborne and j.reverser:
        j.reverser = False
        j.msg = "Reverse stowed for flight."
    # The descent<->speed exchange: descending buys speed, climbing
    # spends it. With the engines DEAD (v37) the jet is a glider and
    # the exchange runs GLIDE_BOOST times stronger, so a clean jet at
    # ~150 kt holds her speed with about a 1,000 fpm sink -- 25 NM
    # for every 10,000 ft -- and pulling up (the deadstick flare)
    # spends speed just as honestly.
    accel -= (j.vsi / 6000.0) * 3.2 * (
        GLIDE_BOOST if (j.airborne and j.n1 < 1.0) else 1.0)
    j.ias = max(0.0, j.ias + accel * h)

    if j.ias > 360.0:
        warn_msg = "OVERSPEED - barber pole! Slow down!"
        warn = "over"
    elif j.gear_down and j.ias > 200.0:
        warn_msg = "Gear overspeed! Max 200 kt with gear down."
        warn = "gear"
    elif j.flap >= 40 and j.ias > 165.0:
        warn_msg = "Flap overspeed! Max 165 kt with flap 40."
        warn = "flap"
    elif j.flap >= 20 and j.ias > 190.0:
        warn_msg = "Flap overspeed! Max 190 kt with flap 20."
        warn = "flap"
    elif j.flap >= 10 and j.ias > 230.0:
        warn_msg = "Flap overspeed! Max 230 kt with flap 10."
        warn = "flap"
    else:
        warn = ""
        warn_msg = ""
    if warn:
        j.spd_warn = True
        j.warn_msg = warn_msg
        j.msg = warn_msg
    elif j.spd_warn:
        # Back inside the limits -- retire the warning, but ONLY if the
        # INFO line still shows it. Another system (descent advice, gear
        # transit, ...) may have taken the line over since; that message
        # must be left alone. (Was: j.msg = "" unconditionally, which
        # blanked whatever happened to be showing.)
        j.spd_warn = False
        if j.msg == j.warn_msg:
            j.msg = ""
        j.warn_msg = ""
    # Flight recorder: count each excursion once, so the debrief can say
    # how often the limits were busted (not how long they stayed busted).
    if warn and warn != j.warn_kind:
        if warn == "over":
            j.overspeed_count += 1
        elif warn == "gear":
            j.gear_overspeed_count += 1
        else:
            j.flap_overspeed_count += 1
    j.warn_kind = warn

    # Flap lift: slew the balloon toward its target over a few seconds,
    # like real flap travel, so an extension is felt rather than
    # teleported in. On the ground the target is zero and it dies away.
    want_lift = flap_lift_fpm(j)
    j.flap_lift += max(-200.0 * h, min(200.0 * h, want_lift - j.flap_lift))

    if not j.airborne:
        j.vsi = 0.0
        j.pitch = 0.0
        # Wings LEVEL on the ground (v33): taxi turns don't bank the
        # jet -- the needle settles gently to zero (v34's first-order
        # chase) whatever the last turn command asked for.
        j.bank += -j.bank * min(1.0, h / BANK_IN_TAU)
        j.bank = max(-BANK_MAX, min(BANK_MAX, j.bank))  # the 40-degree limit (v40)
        if j.free_departure:
            # Parked at an enroute stop (v22): the altimeter reads the
            # ground beneath her -- the enroute airport's elevation (or
            # the terrain if she has taxied away from the field), never
            # the ORIGIN's -- so the second takeoff rotates from the
            # right height and doesn't "land" again the moment she
            # leaves the ground.
            j.alt = ground_elev(j)
        elif j.rollout:
            j.alt = j.landed_elev
        else:
            j.alt = origin_elev(j.route)
    else:
        if j.autoland:
            # AUTOLAND flies the whole profile from the 100 nm capture:
            # configuration, speed, the 3-degree path, and the flare.
            # v19: she flies to the airport the invitation was accepted
            # for -- the next field ahead, enroute or destination -- so
            # the elevation and distances below travel with al_apt (an
            # old save without al_apt falls back to the destination).
            al_name = j.al_apt or j.route["name"].split("-")[1]
            al_apt = next((a for a in route_airports(j.route)
                           if a["name"] == al_name),
                          route_airports(j.route)[-1])
            al_pos = float(j.route["dist"]) - j.dme
            dest_elev = al_apt["elev"]
            d_end = al_apt["dist"] - al_pos   # nm to the runway END
            d_thr = d_end - RWY_NM        # nm to the threshold
            # Flaps and gear come out on schedule, inside their limits --
            # but only once the field is close: from the 100 nm capture
            # to 25 nm she stays clean and fast like a real managed
            # descent, then configures on the usual gates.
            if j.ias < 200.0 and d_end < 25.0 and j.flap < 10:
                j.flap = 10
            if j.ias < 165.0 and d_end < 12.0 and j.flap < 20:
                j.flap = 20
            if j.ias < 150.0 and d_end < 7.0 and j.flap < 40:
                j.flap = 40
            if (d_end < 8.0 and j.ias < 190.0 and not j.gear_down
                    and j.gear_seq_dir == 0):
                j.gear_seq_dir = +1
                j.gear_t = 0.0
            # Auto-thrust: hold the right speed for this stage -- a fast
            # clean run-in beyond 25 nm, then the approach speeds.
            tgt_ias = (240.0 if d_end > 25.0
                       else 155.0 if d_end > 12.0
                       else 140.0 if d_end > 7.0 else 130.0)
            j.thrust = max(0.0, min(100.0,
                j.thrust + max(-20.0 * h, min(20.0 * h, (tgt_ias - j.ias) * 1.5))))
            # Vertical: ride the 3-degree path, then flare in two gentle
            # steps to a firm-but-tidy arrival just past the threshold.
            # (An uncapped shallow flare floated her clean off the far
            # end -- the steps put her DOWN with runway in hand.)
            gs_alt = dest_elev + max(0.0, d_thr) * 300.0
            agl = j.alt - dest_elev
            if d_end < -0.5:
                # v19 safety net: past the target runway still airborne --
                # hand her back before the law flies her into the ground
                # beyond the field (can only happen at an enroute field;
                # at the destination the v25 fly-around advisory below
                # takes over instead).
                j.autoland = False
                j.vsi_cmd = 500.0
                j.msg = ("AUTOLAND missed the runway at %s - you have her, "
                         "go around!" % al_name)
            elif agl > 60.0:
                err = gs_alt - j.alt      # + = below the path
                # The 3-degree path asks ~1,200 fpm at the 240 kt
                # run-in speed, so the sink cap beyond 25 nm is deeper;
                # inside 25 nm (155 kt and slowing) 900 fpm holds it
                # comfortably. (A flat cap here let her drift high on a
                # long capture and she floated clean off the far end.)
                sink_cap = -1400.0 if d_end > 25.0 else -900.0
                j.vsi_cmd = max(sink_cap, min(-100.0, err * 5.0 - 500.0)) - j.flap_lift
                # v47: NEVER chase the beam into the ground. A close-in
                # offer (Dunk Is. is only 87 nm out, so its invitation is
                # only ever there right after take-off) used to command a
                # descent from a thousand feet toward a path still twenty
                # thousand feet overhead -- controlled flight into
                # terrain forty miles short. Engaged low and far below
                # the beam, she now holds her height and lets the path
                # come down to her, joining it when they meet. (The guard
                # sleeps through an ordinary approach: there the path is
                # under her, err is negative, and nothing changes.)
                if err > 0.0 and agl < 3000.0 and d_end > 10.0:
                    j.vsi_cmd = max(j.vsi_cmd, -j.flap_lift)   # net zero
            else:
                j.vsi_cmd = (-350.0 if agl > 25.0 else -180.0) - j.flap_lift
            # THE APPROACH CHOP (v46): two slow random walks, pulled back
            # to zero the way a gusty sky nudges and releases. The heading
            # walk is applied here; the vertical walk rides the VSI chase
            # target below. The autopilot's own laws correct every wobble,
            # and THAT correction activity is what the pilot now sees on
            # the AI needle, the CDI and the glideslope tape. ap_tex fades
            # the texture out from 600 ft down to 250, so the flare, the
            # touchdown and the v20 fence meet clean air.
            j.ap_tex = max(0.0, min(1.0, (agl - 250.0) / 350.0))
            j.ap_gust_h += (-0.20 * j.ap_gust_h + random.gauss(0.0, 0.85)) * h
            j.ap_gust_h = max(-4.0, min(4.0, j.ap_gust_h))
            j.ap_gust_v += (-0.22 * j.ap_gust_v + random.gauss(0.0, 75.0)) * h
            j.ap_gust_v = max(-220.0, min(220.0, j.ap_gust_v))
            j.hdg = (j.hdg + j.ap_gust_h * j.ap_tex * h) % 360.0
        elif j.level_cap:
            # Nuanced level-off capture: wash off the climb, dip just
            # past the target, then ease back and settle on the level.
            if j.level_phase == 0:
                # Phase 0 - keep rising/descending, but slow the rate away.
                j.vsi_cmd += max(-350.0 * h, min(350.0 * h, -j.flap_lift - j.vsi_cmd))
                if abs(j.vsi) < 30.0:
                    over = j.alt - j.level_target
                    dip = max(10.0, min(80.0, abs(over) * 0.6))
                    j.level_dir = 1 if over >= 0 else -1
                    j.level_dip = j.level_target - dip * j.level_dir
                    j.level_phase = 1
            elif j.level_phase == 1:
                # Phase 1 - run gently to just below (or above) the target,
                # keeping at least 100 fpm on so the dip doesn't dawdle.
                g1 = j.level_dip - j.alt
                cmd1 = max(-400.0, min(400.0, g1 * 5.0))
                if abs(g1) > 8.0 and abs(cmd1) < 100.0:
                    cmd1 = 100.0 if g1 > 0 else -100.0
                j.vsi_cmd = cmd1 - j.flap_lift
                if abs(j.alt - j.level_dip) < 8.0:
                    j.level_phase = 2
            elif j.level_phase == 2:
                # Phase 2 - ease back onto the exact level.
                g2 = j.level_target - j.alt
                cmd2 = max(-250.0, min(250.0, g2 * 6.0))
                if abs(g2) > 3.0 and abs(cmd2) < 50.0:
                    cmd2 = 50.0 if g2 > 0 else -50.0
                j.vsi_cmd = cmd2 - j.flap_lift
                if abs(j.alt - j.level_target) < 3.0 and abs(j.vsi) < 60.0:
                    j.level_phase = 3   # captured -- move into the HOLD (v23)
                    # Trim the flap balloon OUT, so the jet truly holds the
                    # captured level. (Was vsi_cmd = 0.0: with flaps out the
                    # balloon kept pushing and the "level" wandered away.)
                    j.vsi_cmd = -j.flap_lift
                    play_bing()
                    if j.ap:
                        j.ass_fl = max(10, min(450, int(round(j.level_target / 100.0))))
                        j.msg = "Level flight - autopilot holding FL%d." % j.ass_fl
                    else:
                        j.msg = "Level flight - holding %s ft." % format(
                            int(round(j.level_target / 100.0) * 100), ",")
            else:
                # Phase 3 - HOLD the captured level for good (v23): the same
                # gentle correction law the autopilot's level hold uses. The
                # old code ended the capture here and froze vsi_cmd at the
                # completion instant; as the speed -- and with it the flap
                # balloon -- moved on, the frozen trim went stale and she
                # leaked a couple of feet a minute forever, so every fresh
                # [L] re-captured the sunk altitude a few feet lower. Any
                # [W]/[S] press releases the hold (it clears level_cap).
                diff = j.level_target - j.alt
                j.vsi_cmd = -j.flap_lift + max(-150.0, min(150.0, diff * 2.0))
        elif j.ap and j.ass_fl > 0:
            diff = j.ass_fl * 100.0 - j.alt
            if abs(diff) < 40.0:
                # Hold level against the flap balloon, with a gentle
                # correction so a changing balloon can't drift the jet.
                j.vsi_cmd = -j.flap_lift + max(-150.0, min(150.0, diff * 2.0))
            else:
                j.vsi_cmd = max(-1800.0, min(2200.0, diff * 1.2)) - j.flap_lift
        if j.ias < stall_speed(j):
            j.vsi_cmd = min(j.vsi_cmd, -1500.0)
            j.msg = "STALL! Nose down [S] and add thrust [+]!"
            if not j.in_stall:
                j.in_stall = True
                j.stall_count += 1      # flight recorder: each stall entry
        else:
            j.in_stall = False

        # Attitude: the ladder reads the flight-path angle, pure and
        # simple -- atan2(vsi, ias). The v46 angle-of-attack offset on
        # top of it read truly (a jet on a three-degree final really
        # does hold her nose on the horizon) but it broke the older
        # contract that matters more (v48): the ladder's degrees and
        # the [W]/[S] degree commands speak flight-path angle, so a
        # degree commanded must be a degree shown. With the offset,
        # three presses of [S] on final still showed the aircraft on
        # the horizon -- nothing below it. Gone now: [S] drops the
        # nose below the horizon from the first press, at any speed.
        # The gauge still lives through an autopilot approach -- the
        # v46 chop ripples the path itself, and the bank needle works
        # every correction.
        if j.ias > 5.0:
            j.pitch = math.degrees(math.atan2(j.vsi, j.ias * 101.3))
        else:
            j.pitch = 0.0
        # Return bank to level only when the turn is DONE (v33): she
        # holds her bank through the whole turn -- fresh commands keep
        # it on -- and releases it TURN_HOLD_S after the last one, the
        # time the final 5-degree step takes to turn through.
        if j.elapsed - j.bank_turn_t > TURN_HOLD_S:
            j.bank_target = 0.0
        # The GENTLE NEEDLE (v34): the bank CHASES its target with a
        # first-order lag instead of a flat-rate slew -- the needle
        # develops smoothly as the turn develops, and once released
        # she fights back to straight-ahead flight on the slower
        # BANK_OUT_TAU, easing to zero rather than motoring home.
        tau = BANK_IN_TAU if j.bank_target != 0.0 else BANK_OUT_TAU
        j.bank += (j.bank_target - j.bank) * min(1.0, h / tau)
        j.bank = max(-BANK_MAX, min(BANK_MAX, j.bank))  # the 40-degree limit (v40)
        # The VSI chases the command PLUS the flap-lift balloon, so the
        # pilot sees the extra lift on the gauge and trims it out by hand.
        # (v46: in an autoland the vertical chop rides the target too --
        # faded to nothing below 600 ft -- so the VSI shimmers and the
        # glideslope needle hunts around the notch while the AP trims.)
        vsi_target = j.vsi_cmd + j.flap_lift
        if j.autoland:
            vsi_target += j.ap_gust_v * j.ap_tex
        j.vsi += max(-1500.0 * h, min(1500.0 * h, vsi_target - j.vsi))
        j.alt += j.vsi / 60.0 * h
        j.alt = min(j.alt, MAX_FL * 100.0)

    if j.ap:
        diff = (j.bug - j.hdg + 540.0) % 360.0 - 180.0
        j.hdg = (j.hdg + max(-3.0 * h, min(3.0 * h, diff))) % 360.0
        # THE LIVE AI (v40): the gauge used to freeze the moment the
        # autopilot took the aircraft -- the AP steered the heading with
        # no bank at all, so the needle parked at zero and the whole
        # instrument went dead while the jet turned. She now shows the
        # turn the autopilot is flying: a bank into it -- two degrees of
        # bank for every degree the heading is off the bug, up to the
        # forty-degree limit -- easing back to wings level as the bug is
        # captured, so the needle works exactly as a hand-flown turn does.
        if j.airborne:
            j.bank_target = max(-BANK_MAX, min(BANK_MAX, diff * 2.0))
            j.bank_turn_t = j.elapsed   # hold the v33 release timer off
                                        # while the AP owns the turn

    # AUTOLAND lateral: steer the heading bug so the CDI needle centres --
    # drift right of the course line and the bug steps left, and back.
    if j.autoland and j.airborne:
        course = getattr(j, "obs", float(j.route["hdg"]))
        j.bug = (course - max(-15.0, min(15.0, j.xte * 6.0)) + 360.0) % 360.0

    # Progressive gear transit: one light changes every GEAR_STEP_SIM
    # sim-seconds. Retraction order top -> bottom-right -> bottom-left;
    # extension runs the same sequence in reverse. The gear itself only
    # counts as up (or down) once the last light has changed.
    if j.gear_seq_dir != 0:
        j.gear_t += h
        order = [0, 2, 1] if j.gear_seq_dir < 0 else [1, 2, 0]
        stage = min(3, int(j.gear_t / GEAR_STEP_SIM))
        for n, idx in enumerate(order):
            if j.gear_seq_dir < 0:
                j.gear_lights[idx] = n >= stage   # lights go OFF one by one
            else:
                j.gear_lights[idx] = n < stage    # lights come ON one by one
        if stage >= 3:
            j.gear_down = (j.gear_seq_dir > 0)
            j.gear_seq_dir = 0
            # The *D placard does not follow the last green instantly --
            # it turns over one fifth of a second later (ticked below).
            j.door_delay = DOOR_DELAY_SIM
            j.msg = "Gear DOWN - three greens." if j.gear_down else "Gear UP and locked."
            play_bing()

    # The yellow *D placard: out one fifth of a second after the third
    # green extinguishes on retraction; back on one fifth of a second
    # after the third green lights on extension.
    if j.door_delay >= 0.0:
        j.door_delay -= h
        if j.door_delay < 0.0:
            j.door_light = j.gear_down

    # Along-route motion: airborne, in the landing rollout, or rolling on
    # the ground after an enroute stop (free_departure, v22) -- the last
    # so a back-taxi to the threshold and the takeoff roll itself move
    # the DME and the Enroute-screen square. At the ORIGIN the takeoff
    # roll still stays put: the runway IS the start line there.
    if j.airborne or j.rollout or j.free_departure:
        dist_step = j.ias * h / 3600.0
        if j.airborne:
            # Gentle wind aloft: the heading slowly wanders off course,
            # so the CDI needle creeps away and you must ease it back.
            j.hdg = (j.hdg + j.wind_drift_dir * WIND_DRIFT_DPS * h) % 360.0
            # Cross-track navigation: the OBS course line runs straight
            # from the origin to the destination. Any angle between the
            # heading and the OBS course builds cross-track error (nm),
            # and only the along-track part of the flight makes progress
            # down the route -- drifting off course costs you distance.
            course = getattr(j, "obs", float(j.route["hdg"]))
            off_rad = math.radians((j.hdg - course + 540.0) % 360.0 - 180.0)
            j.xte = getattr(j, "xte", 0.0) + math.sin(off_rad) * dist_step
            along_step = dist_step * math.cos(off_rad)
        else:
            # On the ground the wheels follow the nose (v22): rolling
            # WITH the course makes progress along the route, rolling
            # the other way -- back-taxiing to the threshold after an
            # enroute landing, or a downwind intersection departure --
            # unwinds it again, so the DME metre readout and the red
            # square on the Enroute screen tell the truth while taxiing.
            course = getattr(j, "obs", float(j.route["hdg"]))
            off_rad = math.radians((j.hdg - course + 540.0) % 360.0 - 180.0)
            along_step = dist_step * math.cos(off_rad)
        j.dme = max(0.0, j.dme - along_step)
        j.dist_flown += along_step

    apt = next_airport(j)
    pos = j.route["dist"] - j.dme          # nm from the origin start line
    dme_apt = apt["dist"] - pos            # nm to the END of its runway

    # Mark each intermediate airport as history once it is genuinely
    # behind us: overflown past the runway end (the very moment the red
    # square passes its star on the Enroute screen), landed on, or
    # crossed low past its mid-runway point (a touch-and-go or go-around).
    # From then on the sim stays silent about it: via_quiet suppresses
    # every NEW advisory aimed at it, and any INFO line still talking
    # about it is cleared on the spot, so nothing about it lingers.
    via_names = {v["name"] for v in route_vias(j.route)}
    for v in route_vias(j.route):
        v_name = v["name"]
        if j.via_done.get(v_name):
            continue
        v_end = v["dist"]
        if pos > v_end:
            j.via_done[v_name] = True               # overflew the field
        elif j.rollout and j.landed_name == v_name:
            j.via_done[v_name] = True               # landed there
        elif (j.airborne and pos > v_end - RWY_NM * 0.5
                and j.alt < v["elev"] + 1500.0):
            # v19: low past MID-RUNWAY (was the threshold) -- an approach
            # keeps its glideslope, gear warning and descent chatter all
            # the way to the flare; only a touch-and-go / go-around that
            # is genuinely leaving is silenced.
            j.via_done[v_name] = True               # low over the runway
        if j.via_done.get(v_name):
            # The INFO line is sticky: retire any message that still
            # names this airport (e.g. "START YOUR DESCENT TO YBRK ...",
            # "Glideslope alive for ROCKHAMPTON ...") so it cannot keep
            # showing after the airport is behind us, and reset the
            # guidance memory so the next airport's advice starts fresh.
            v_icao = AIRPORT_ICAO.get(v_name, "")
            if j.msg and (v_name in j.msg or (v_icao and v_icao in j.msg)):
                j.msg = ""
            j.guid_last = ""
    via_quiet = bool(j.via_done.get(apt["name"], False))

    # Glideslope wakes 100 NM out at every airport, intermediate and
    # destination alike. The slope aims 300 m INTO the runway (the
    # touchdown-zone markers), so flying the needle to the ground
    # crosses the fence 48 ft up and settles onto the runway with the
    # rollout ahead. (v20: it used to aim at the threshold itself at
    # field elevation plus zero -- the tiniest low wobble was turf.)
    gs_range = GS_ACTIVE_NM
    if 0.0 < dme_apt < gs_range and j.airborne and not via_quiet:
        # v20: the path flattens at the runway surface inside the
        # touchdown zone, so the needle can never command flight below
        # the runway; and in the last 250 feet in the zone its job is
        # done -- it parks (gs_dev None) and the landing is by the
        # taught flare, not by chasing the needle into the ground.
        # (v46: the park height rose from 100 to 250 feet because the
        # new angular scale would otherwise swing the marker across the
        # tape over the last feet of a beam that has already flattened
        # onto the runway.)
        gs_alt = apt["elev"] + max(0.0, dme_apt - RWY_NM + GS_AIM_NM) * 300.0
        if dme_apt < RWY_NM - GS_AIM_NM and j.alt < apt["elev"] + 250.0:
            j.gs_dev = None
            j.gs_frac = None
        else:
            j.gs_dev = j.alt - gs_alt
            # v46: the tape reads the deviation the way a real receiver
            # does -- as an ANGLE off the beam, not a fixed number of
            # feet. Far out the full scale spans thousands of feet and
            # the marker rides in off the peg as she joins the path;
            # close in the needle grows sensitive enough to show every
            # correction the autopilot makes around the notch.
            d_beam = max(0.2, dme_apt - RWY_NM + GS_AIM_NM) * 6076.12
            ang = math.degrees(math.atan2(j.gs_dev, d_beam))
            j.gs_frac = max(-1.0, min(1.0, ang / GS_FULL_DEG))
            # Flight recorder: time spent within 150 ft of the slope
            # counts as genuine instrument skill in the debrief.
            if abs(j.gs_dev) < 150.0:
                j.gs_time += h
        if not j.gs_alive:
            j.gs_alive = True
            j.msg = "Glideslope alive for %s (%s) - follow the G/S down." % (
                apt["name"], AIRPORT_ICAO.get(apt["name"], "????"))
            play_bing("bing2")
    else:
        j.gs_dev = None
        j.gs_frac = None
        j.gs_alive = False

    # AUTOLAND invitation: autopilot on, the next airport ahead inside
    # the offer range -- the enroute field OR the destination, exactly
    # as the v10 note always promised (the offer used to be destination-
    # only). 100 NM everywhere, save one: KARRATHA-PERTH invites at
    # 200 NM from EVERY field on the route (v59) -- Carnarvon and Perth
    # alike -- so the descent has ample time at the prescribed rate. It
    # lives at INFO for 30 seconds; after that a manual landing at THAT
    # field is assumed and late [Y] presses for it are politely refused
    # -- but the next airport down the route gets its own invitation.
    al_range = AL_OFFER_NM
    if j.route["name"] == "KARRATHA-PERTH":
        al_range = AL_OFFER_NM_KP
    if (j.ap and j.airborne and not j.rollout
            and not via_quiet and RWY_NM < dme_apt <= al_range
            and not j.autoland and not j.al_offer
            and apt["name"] not in j.al_done
            # v81: THE THOUSAND-FOOT FLOOR. Where the next field lies
            # inside the offer range from the moment of take-off (Dunk
            # Is. is 87 nm out of Townsville, Karratha 100 out of Port
            # Hedland, Adelaide 95 out of Whyalla), the invitation used
            # to be on the table the very first airborne frame -- and an
            # [Y] pressed a heartbeat after liftoff engaged the landing
            # law at a few DOZEN feet above the field. Down in the flare
            # band (under 60 ft) the v47 hold-height guard does not even
            # run: the two-step flare simply put her in the terrain
            # ninety-odd miles short, every single time. Above it, the
            # guard held a couple of hundred feet all the way to the
            # field, where no safe path down remained -- the same prang,
            # later. The offer now waits for a thousand feet above the
            # field ahead -- the height v47's own invitation arrived at
            # -- where holding for the beam is the tested, safe answer.
            and j.alt - apt["elev"] >= 1000.0):
        j.al_offer = True
        j.al_offer_apt = apt["name"]
        j.al_offer_t = j.elapsed
        j.msg = ("AUTOLAND to %s? [Y] accepts, [N] declines - %d seconds to "
                 "decide." % (apt["name"], AL_OFFER_SECS))
        play_bing()
    if j.al_offer and j.elapsed - j.al_offer_t > AL_OFFER_SECS:
        j.al_offer = False
        j.al_done.append(j.al_offer_apt)
        j.al_expire_t = j.elapsed
        j.msg = "AUTOLAND time expired - she's all yours, captain."

    # One-time callout as each enroute airport comes into range (kept
    # after the glideslope block so it isn't overwritten the moment it
    # appears). Not while the AUTOLAND is committed: she is already
    # landing at her tuned field, so the land-here-or-overfly question
    # is moot and the INFO line stays quiet.
    if (j.airborne and not via_quiet and not j.via_said.get(apt["name"])
            and not j.autoland
            and apt["name"] in via_names and 0.0 < dme_apt < 12.0):
        j.via_said[apt["name"]] = True
        play_bing()
        j.msg = "%s (%s) ahead - land, or overfly for %s." % (
            apt["name"], AIRPORT_LETTERS.get(apt["name"], "?"),
            j.route["name"].split("-")[1])

    # Off-course advisory at INFO: speaks once when you stray beyond two
    # nautical miles, and arms again once you're back near the line.
    if j.airborne:
        if abs(j.xte) > 2.0 and not j.off_course_said:
            j.off_course_said = True
            j.offcourse_count += 1     # flight recorder: each excursion
            play_bing("bing2")
            j.msg = "OFF COURSE - the course line is to your %s. Centre the CDI needle." % (
                "left" if j.xte > 0.0 else "right")
        elif abs(j.xte) < 0.5:
            j.off_course_said = False

    # CAB PRESS: a pressurisation failure at very infrequent, random
    # times -- but only while above 10,000 ft. The light burns (the box
    # face flashes red on the panel) until the jet is brought below
    # 10,000 ft; once it clears there she is free to climb back to her
    # level, and the clock re-arms for the next, equally rare, failure.
    # v72: SUSPENDED on the REAL TIME legs (TOWNSVILLE-CAIRNS and
    # KARRATHA-PERTH) -- no failure at all there, so the cruise sound
    # effect continues undisturbed until the aircraft has landed.
    if j.route.get("real_time"):
        j.cab_light = False                 # no failures on the 1:1 legs
    elif j.cab_light:
        if j.alt < 10000.0:
            j.cab_light = False
            j.cab_survivals = getattr(j, "cab_survivals", 0) + 1   # v87:
                                   # the logbook counts every failure
                                   # safely brought down below 10,000 ft
            j.cab_next_t = j.elapsed + random.uniform(CAB_PRESS_MIN_S,
                                                      CAB_PRESS_MAX_S)
            j.msg = "CAB PRESS normal below 10,000 ft - climb away when ready."
            play_bing()
    elif j.airborne and j.alt > 10000.0 and j.elapsed >= j.cab_next_t:
        j.cab_light = True
        j.msg = "CAB PRESS - cabin altitude rising! Get below 10,000 ft."
        play_bing("bing2")

    # ----- Time-based descent guidance at INFO -----
    # Profile: be at the airport's elevation PLUS 1,000 ft for every
    # minute still to run TO THE RUNWAY THRESHOLD (a steady 1,000 fpm
    # descent to the field). v19: the profile used to aim at field
    # elevation at the runway END -- a full runway-length long, which
    # brought a faithful follower over the fence some 500 ft high --
    # and it now hushes inside 10 nm, where the G/S needle rules the
    # final (the TOO LOW - GEAR and terrain warnings below still speak).
    # Guidance starts when the moment to begin down is five minutes
    # away, then calls the recommended altitude at each whole minute
    # to run -- saying whether the aircraft is high, low, or on it.
    # (It only speaks when the advice changes.)
    if (j.airborne and j.ias >= 40.0 and dme_apt > 10.0 and not via_quiet
            and not j.autoland):
        # (The descent chatter also stays quiet while AUTOLAND is
        # engaged -- she is flying her own profile, and her messages
        # must not be overwritten by advice meant for the pilot.)
        ttg_min = max(0.0, dme_apt - RWY_NM) / j.ias * 60.0   # minutes to the
                                                            # THRESHOLD (v19)
        need_min = (j.alt - apt["elev"]) / 1000.0   # minutes needed at 1,000 fpm
        lead_min = ttg_min - need_min               # time left before you must start down
        apt_icao = AIRPORT_ICAO.get(apt["name"], "????")   # name the field
        advice = ""
        if j.alt > apt["elev"] + 1200.0 and ttg_min > 0.5:
            run = max(1, int(round(ttg_min)))
            tgt = apt["elev"] + run * 1000.0
            tgt_txt = format(int(round(tgt / 100.0) * 100), ",")
            if lead_min > 5.0:
                pass                                # too early - enjoy the cruise
            elif lead_min > 0.75:
                mins = int(math.ceil(lead_min))
                advice = "START YOUR DESCENT TO %s WITHIN %d MINUTE%s." % (
                    apt_icao, mins, "S" if mins != 1 else "")
            elif j.vsi > -100.0:
                advice = "START YOUR DESCENT TO %s NOW - %d MINUTE%s TO GO." % (
                    apt_icao, run, "S" if run != 1 else "")
            else:
                where = ("ON PROFILE" if abs(j.alt - tgt) <= 750.0
                         else "TOO HIGH" if j.alt > tgt else "TOO LOW")
                advice = "%s FOR %s - THE AIRCRAFT SHOULD BE AT %s FT WITH %d MINUTE%s TO GO." % (
                    where, apt_icao, tgt_txt, run, "S" if run != 1 else "")
        if (advice and advice != j.guid_last and not j.al_offer
                and j.elapsed - j.al_expire_t > 8.0):
            # (The descent chatter stays quiet while the AUTOLAND
            # invitation is on the table, and for a few seconds after
            # it expires, so neither message can be overwritten.)
            j.guid_last = advice
            j.msg = advice
            play_bing()

    g = ground_elev(j)
    # Terrain: a very-low alert only -- it speaks below 200 ft above the
    # ground, hushed within 15 nm of ANY landable airport (including one
    # just passed, so a touch-and-go climb-out isn't scolded). The INFO
    # line is sticky, so the moment the jet climbs back above 200 ft (or
    # comes near a field) the warning is actively CLEARED, not left
    # hanging there at 5,000 ft. (Was 800 ft and sticky-forever: it
    # nagged through every climb-out and never went away.)
    near_d = min(abs(a["dist"] - pos) for a in route_airports(j.route))
    terr_active = j.airborne and near_d > 15.0 and j.alt < g + 200.0
    if terr_active:
        j.msg = "TERRAIN! TERRAIN! Climb!"
        if not j.terrain_now:
            j.terrain_now = True
            j.terrain_count += 1      # flight recorder: each scare, once
    elif j.msg == "TERRAIN! TERRAIN! Climb!":
        j.msg = ""                    # climbed away - retire the warning
    j.terrain_now = terr_active

    if (j.airborne and 0.0 < dme_apt < 8.0 and j.alt < apt["elev"] + 2000.0
            and not j.gear_down and not via_quiet and not j.autoland):
        # (No false alarm while AUTOLAND is engaged: she lowers the gear
        # herself inside 8 nm, and the transit takes a few seconds.)
        j.msg = "TOO LOW - GEAR! Put the wheels down [G]!"

    # v25: THE FLY-AROUND ADVISORY. Reaching the destination still
    # airborne no longer teleports her back to DME 12 nm with the
    # descent still running (the old "ATC vectors you back", which
    # simply repeated the same approach until she finally landed). She
    # holds over the far end -- the DME pins at 0.0, progress resuming
    # the moment she turns back -- while INFO advises the fly-around:
    # climb away, turn back, re-join for another attempt. Speaks once
    # per overshoot, re-arming (and retiring its own message) once she
    # is a mile back out. AUTOLAND is left to its own missed-runway
    # hand-back, and settling onto the far end anyway still meets the
    # 2,000 m overrun rule, as before.
    if j.airborne and not j.autoland:
        if j.dme <= 0.0:
            if not getattr(j, "overshoot_said", False):
                j.overshoot_said = True
                j.msg = ("Overshot the field - FLY AROUND for another "
                         "attempt: climb away [W], turn back [A]/[D], "
                         "and re-join.")
                play_bing("bing2")
        elif j.dme > 1.0:
            j.overshoot_said = False
            if j.msg.startswith("Overshot the field"):
                j.msg = ""

    # Flight recorder: properly configured for landing -- wheels down,
    # low, near the field -- earns credit in the debrief.
    if (j.airborne and j.gear_down and 0.0 < dme_apt < 10.0
            and j.alt < apt["elev"] + 2500.0):
        j.gear_down_low = True

    # Ground contact. Near an airport the local ground is the airport's
    # own elevation (flat airfield); the runway occupies the LAST 2,000 m
    # before the airport's distance mark (the runway end).
    rwy_start = apt["dist"] - RWY_NM
    in_zone = (apt["dist"] - APCH_ZONE_NM) <= pos <= apt["dist"] + 0.3
    if j.airborne:
        local_g = apt["elev"] if in_zone else g
        if j.alt <= local_g:
            if not in_zone:
                crash(j, "Controlled flight into terrain.")
            elif pos < rwy_start:
                short_m = int((rwy_start - pos) * M_PER_NM)
                crash(j, "Down %d m short of the runway at %s - crashed at the airport!"
                         % (short_m, apt["name"]))
            else:
                touchdown(j, apt)

    # Rollout: must be stopped before the runway end, 2,000 m on.
    if j.rollout:
        if pos >= j.landed_dist:
            crash(j, "Ran off the end of the 2,000 m runway at %s!" % j.landed_name)
        elif j.ias < 2.0:
            # v55: a full stop reads ZERO. The stop is declared the moment
            # the speed dips under 2 kt and step() ignores a done jet, so
            # without this snap the gauge used to freeze at "001 K".
            j.ias = 0.0
            j.done = True
            bank_arrival_stats(j)   # v87: the logbook counts the landing
                                    # HERE -- a [C] stopover-continue flies
                                    # on, so the flight-end bank in
                                    # flight_hud would never see it. step()
                                    # ignores a done jet: once per stop.

    # AUTOLAND on the ground: brakes on, buckets out, power against her
    # until she slows, then a gentle roll to the full stop.
    if j.autoland and j.rollout:
        j.brakes = True
        j.reverser = True
        j.thrust = 60.0 if j.ias > 40.0 else 0.0
        if j.ias < 2.0:
            j.autoland = False
            j.thrust = 0.0
            j.msg = "AUTOLAND complete - welcome to %s!" % (
                j.landed_name or "the field")

    # v53: once she has come to a stop on the ground the buckets stow
    # themselves -- the R/TH cluster stops flashing and the reverse
    # system returns to stand-by. (Silently right after an autoland, so
    # the welcome message keeps the INFO line.)
    if not j.airborne and j.reverser and j.ias <= 2.0:
        j.reverser = False
        if not j.msg.startswith("AUTOLAND complete"):
            j.msg = "Full stop - reverse thrust stowed, standing by."


# ----------------------------------------------------------------------
#  THE LIVE ETA (v80) -- a ghost flight to the tuned runway.
#
#  Once she is airborne, the ETA box no longer counts down the
#  captain's-table budget; it flies a copy of the jet forward in
#  fast-time with the sim's own physics -- the same drag model, the
#  same N1 spool, the same descent-buys-speed exchange, the same
#  3-degree path, configuration gates and two-step flare the AUTOLAND
#  uses -- and counts the seconds to the runway surface. Distance,
#  flight level, airspeed, flap, gear, brakes, fuel and the heading
#  off the course line all move the figure, because they all move the
#  ghost. With the AUTOLAND committed the ghost flies the autoland's
#  own laws, so the prediction IS the plan -- on final approach the
#  ETA is the truth, counting down to zero at the touchdown.
#  Hand-flown, the ghost holds the speed she has and the climb or
#  sink she is in until the 3-degree path must be joined, then slows
#  and configures on the usual gates -- any landing has to.
# ----------------------------------------------------------------------
ETA_RECOMP_NEAR_S = 2.0    # sim-seconds between ghost flights, close in
ETA_RECOMP_FAR_S  = 6.0    # ... and far out (the figure ticks down between)


def eta_tuned_airport(jet):
    """The airport the ETA speaks for -- the DME's tuned station: the
    destination on "-", each enroute field on "v0","v1" ... The "+"
    origin channel only ever looks back, so it has no ETA."""
    if jet.dme_chan == "+":
        return None
    if jet.dme_chan.startswith("v"):
        vias = route_vias(jet.route)
        vi = int(jet.dme_chan[1:]) if jet.dme_chan[1:].isdigit() else 0
        if 0 <= vi < len(vias):
            return {"name": vias[vi]["name"], "dist": float(vias[vi]["dist"]),
                    "elev": float(vias[vi]["elev"])}
        return None
    return {"name": jet.route["name"].split("-")[1],
            "dist": float(jet.route["dist"]),
            "elev": float(jet.route["elev"])}


def eta_ground_floor(pts, apt, d_end):
    """The ground the ghost can meet, as an altitude: the tuned
    airport's own flat elevation inside its approach zone (the runway
    model's rule), the interpolated terrain everywhere else."""
    if -0.3 <= d_end <= APCH_ZONE_NM:
        return apt["elev"]
    total = pts[-1][0]
    pos = total - d_end
    for (d0, e0), (d1, e1) in zip(pts, pts[1:]):
        if pos <= d1:
            f = max(0.0, min(1.0, (pos - d0) / (d1 - d0))) if d1 > d0 else 1.0
            return e0 + (e1 - e0) * f
    return pts[-1][1]


def eta_predict_s(jet, apt):
    """Fly a copy of the jet from her present state to the tuned
    field's runway surface, fast, with the sim's own physics and
    control laws. Returns the SIM-seconds to touchdown, or None when
    there is no arrival to predict (pointed away from the field, or a
    glide that cannot make it)."""
    pos = float(jet.route["dist"]) - jet.dme
    d_end = apt["dist"] - pos
    if d_end <= 0.0:
        return None                     # that field is already behind her
    course = getattr(jet, "obs", float(jet.route["hdg"]))
    off = math.radians((jet.hdg - course + 540.0) % 360.0 - 180.0)
    cosfac = math.cos(off)
    if cosfac <= 0.01:
        return None                     # flying away from her, or across it
    # The planned cruise level for a hand-flown ship: the route card's
    # FL, the autopilot's ASS FL if one is set, or the level she is
    # actually at -- whichever is highest (a climb continues; a chosen
    # cruise is honoured).
    plan_alt = float(jet.route.get("fl", 200)) * 100.0
    if jet.ap and getattr(jet, "ass_fl", 0) > 0:
        plan_alt = max(plan_alt, jet.ass_fl * 100.0)
    cruise_alt = max(plan_alt, jet.alt)
    # Terrain line, origin -> each enroute field -> destination.
    pts = [(0.0, origin_elev(jet.route))]
    for v in route_vias(jet.route):
        pts.append((v["dist"], v["elev"]))
    pts.append((float(jet.route["dist"]), float(jet.route["elev"])))
    # The ghost herself -- a handful of floats, no panel state.
    alt = float(jet.alt); ias = float(jet.ias); vsi = float(jet.vsi)
    thrust = float(jet.thrust); n1 = float(jet.n1)
    flap = float(jet.flap); gear = bool(jet.gear_down)
    brakes = bool(jet.brakes); engines = bool(jet.engines)
    fuel = float(jet.fuel); al = bool(jet.autoland); elev = float(apt["elev"])
    tgt_hold = ias                        # hand-flown: hold today's speed
    vsi0 = vsi                            # ... and today's climb or sink
    t = 0.0
    for _ in range(12000):
        # Adaptive step: fine close in, coarse far out.
        est = d_end / max(ias, 60.0) * 3600.0
        h = 0.5 if est < 120.0 else 1.0 if est < 900.0 else 2.0 if est < 3600.0 else 4.0
        # --- the pilot the ghost believes in -------------------------
        glider = not engines
        if glider:
            # Dead stick: hold the 150 kt best glide, clean until the
            # field is made, then a late flap 20 and gear.
            q = (max(ias, 1.0) / 260.0) ** 2 * 34.0 + 6.0
            net = -q * 0.14 * 6000.0 / (3.2 * GLIDE_BOOST) + (ias - 150.0) * 10.0
            if d_end < 6.0 and alt - elev < 1500.0:
                if flap < 20 and ias < 185.0:
                    flap = 20.0
                if not gear and ias < 190.0:
                    gear = True
            net = max(-2500.0, min(500.0, net))
        else:
            # Configuration gates -- the sim's own schedule (only ever
            # adds flap and gear, exactly like the autoland).
            if ias < 200.0 and d_end < 25.0 and flap < 10:
                flap = 10.0
            if ias < 165.0 and d_end < 12.0 and flap < 20:
                flap = 20.0
            if ias < 150.0 and d_end < 7.0 and flap < 40:
                flap = 40.0
            if d_end < 8.0 and ias < 190.0:
                gear = True
            # Speed: the autoland's staged targets; hand-flown holds
            # her present speed until the 25 nm gates.
            if al:
                tgt = (240.0 if d_end > 25.0 else 155.0 if d_end > 12.0
                       else 140.0 if d_end > 7.0 else 130.0)
            else:
                tgt = (tgt_hold if d_end > 25.0 else 155.0 if d_end > 12.0
                       else 140.0 if d_end > 7.0 else 130.0)
            thrust = max(0.0, min(100.0,
                thrust + max(-20.0 * h, min(20.0 * h, (tgt - ias) * 1.5))))
            agl = alt - elev
            if agl <= 60.0:
                net = -350.0 if agl > 25.0 else -180.0    # the two-step flare
            else:
                gs_alt = elev + max(0.0, d_end - RWY_NM) * 300.0
                err = gs_alt - alt          # + = below the path
                if al:
                    sink_cap = -1400.0 if d_end > 25.0 else -900.0
                    net = max(sink_cap, min(-100.0, err * 5.0 - 500.0))
                    if err > 0.0 and agl < 3000.0 and d_end > 10.0:
                        net = max(net, 0.0)   # hold height below the beam
                elif err >= 0.0:
                    # Below the path: a climb in hand continues to the
                    # planned level; otherwise hold height and let the
                    # path come down to her.
                    net = vsi0 if (alt < cruise_alt - 50.0 and vsi0 > 300.0) else 0.0
                elif vsi0 < -300.0:
                    net = min(vsi0, err * 5.0 - 500.0)   # keep her sink,
                                                         # don't dive through
                else:
                    net = max(-1800.0, min(-100.0, err * 5.0 - 500.0))
        if ias < 110.0 - flap * 0.85 + (4.0 if gear else 0.0):
            net = min(net, -1500.0)         # the stall law
        # --- the sim's own longitudinal physics, verbatim ------------
        want_n1 = max(thrust, 18.0) if (engines and fuel > 0.0) else 0.0
        n1 += max(-35.0 * h, min(20.0 * h, want_n1 - n1))
        if engines:
            fuel = max(0.0, fuel - (n1 / 100.0) * 2500.0 / 3600.0
                       * fuel_flow_factor(alt) * h)
            if fuel <= 0.0:
                engines = False             # flameout: a glider now
        qf = (ias / 140.0) ** 2
        drag = 6.0 + (ias / 260.0) ** 2 * 34.0
        drag += (flap * 0.45 + (flap / 10.0) ** 2 * 0.4) * qf
        if gear:
            drag += 10.0 * qf
        if brakes:
            drag += 6.0
        accel = (n1 * 0.62 - drag) * 0.14
        accel -= (vsi / 6000.0) * 3.2 * (GLIDE_BOOST if n1 < 1.0 else 1.0)
        ias = max(0.0, ias + accel * h)
        vsi += max(-1500.0 * h, min(1500.0 * h, net - vsi))
        alt = min(alt + vsi / 60.0 * h, MAX_FL * 100.0)
        d_end -= ias * h / 3600.0 * cosfac
        t += h
        # --- arrival? -------------------------------------------------
        if alt <= eta_ground_floor(pts, apt, d_end):
            # Ground contact: an arrival only inside the tuned field's
            # own zone; into the terrain anywhere else is no arrival.
            return t if -0.3 <= d_end <= APCH_ZONE_NM else None
        if d_end <= -0.3:
            return t                        # overhead the runway end
    return None


def eta_live_s(jet):
    """The live ETA in SIM-seconds to the tuned field's runway -- the
    ghost flight's answer, re-flown every couple of sim-seconds (and
    the moment any configuration changes) and ticked down live between
    flights. None while on the ground (the plan budget keeps the box
    there), when the tuned field is behind her, or when the ghost can
    find no arrival."""
    if jet.dead or jet.done:
        return getattr(jet, "_eta_val", None)     # frozen with the world
    if not jet.airborne:
        if jet.rollout:
            # Rolling out: she is AT a field -- 0:00 if it is the tuned
            # one, else no live figure (the onward leg's plan takes it).
            apt0 = eta_tuned_airport(jet)
            if apt0 is not None:
                pos0 = float(jet.route["dist"]) - jet.dme
                if abs(apt0["dist"] - pos0) <= 0.6:
                    return 0.0
        return None
    apt = eta_tuned_airport(jet)
    if apt is None:
        return None
    pos = float(jet.route["dist"]) - jet.dme
    if apt["dist"] - pos <= 0.0:
        return None                     # that field is already behind her
    key = "%s|%s|%s|%s|%s|%s" % (jet.dme_chan, jet.flap, jet.gear_down,
                                 jet.engines, jet.autoland, jet.brakes)
    now = jet.elapsed
    val = getattr(jet, "_eta_val", None)
    t0 = getattr(jet, "_eta_t", None)
    cadence = (ETA_RECOMP_NEAR_S if (val is not None and val < 900.0)
               else ETA_RECOMP_FAR_S)
    if t0 is None or key != getattr(jet, "_eta_key", "") or now - t0 >= cadence:
        val = eta_predict_s(jet, apt)
        jet._eta_val, jet._eta_t, jet._eta_key = val, now, key
    if jet._eta_val is None:
        return None
    return max(0.0, jet._eta_val - (now - jet._eta_t))


def update(j, dt):
    n = max(1, int(round(dt / 0.5)))
    h = dt / n
    for _ in range(n):
        step(j, h)


def touchdown(j, apt):
    j.touch_vsi = j.vsi
    j.landed_name = apt["name"]
    j.landed_elev = apt["elev"]
    j.landed_dist = apt["dist"]
    if not j.gear_down:
        crash(j, "Gear-up landing at %s - sparks all the way down the runway!" % apt["name"])
    elif j.vsi < -900.0:
        # v19: was -700 -- the 3-degree glideslope itself asks 600-700 fpm
        # at the taught 120-140 kt, so a good needle-arrival used to
        # collapse the gear right at the top of the approach speed band.
        crash(j, "A very hard arrival at %s - the gear collapsed." % apt["name"])
    elif j.ias > 140.0:
        # Above 140 kt the gentle brakes cannot stop inside 2,000 m.
        crash(j, "Touchdown far too fast at %s - off the end of the runway!" % apt["name"])
    elif j.ias < 95.0:
        crash(j, "Stalled onto the runway from short final at %s." % apt["name"])
    elif j.flap < 20 and j.ias > 120.0:
        # Too little flap means a fast, flat arrival: above 120 kt the
        # gentle brakes cannot stop inside 2,000 m. (This branch was dead
        # code -- it used to test j.ias > 140.0, which the branch two
        # lines above had already caught, so it could never fire.)
        crash(j, "Landed with too little flap at %s - overrun!" % apt["name"])
    else:
        j.airborne = False
        j.rollout = True
        j.thrust = 0.0
        j.vsi = j.vsi_cmd = 0.0
        j.msg = "Touchdown at %s! Brakes [B] - stop inside 2,000 m!" % apt["name"]
        play_bing()


def crash(j, why):
    j.dead = True
    j.why = why
    play_bing("crash")


def enroute_departure(j):
    """Set the jet up for the onward leg after a full stop at an
    intermediate airport (the captain pressed [C] at the prompt, v22):
    parked on the runway where she stopped, engines running, brakes on,
    autopilot off -- and free to rotate at ANY heading, into wind or
    not, so she can turn round and go from where she sits, or back-taxi
    to the threshold 2,000 m behind the runway end, turn round there
    and take off. The OBS is laid back on the course to the destination
    and the cross-track count restarts from zero at the field, so the
    CDI shows the correct track the moment she is airborne again. The
    airport itself is already marked behind us (via_done on touchdown),
    so its glideslope and advisories stay silent for the rest of the
    flight."""
    dest_name = j.route["name"].split("-")[1]
    j.done = False
    j.rollout = False
    j.airborne = False
    j.brakes = True
    j.thrust = 0.0
    j.reverser = False
    j.ap = False
    j.autoland = False
    j.al_offer = False
    j.al_apt = None
    j.level_cap = False
    j.vsi = j.vsi_cmd = 0.0
    j.gs_dev = None
    j.gs_frac = None
    j.gs_alive = False
    j.obs = float(j.route["hdg"])
    j.xte = 0.0
    j.free_departure = True
    j.alt = j.landed_elev            # parked at the enroute airport's
                                     # elevation, not the origin's (v22)
    # v55: the REAL countdown re-arms for the onward leg. The leg's clock
    # starts NOW, and the leg's base is the measured sim-minute budget of
    # the field she has just landed at -- so the countdown to any airport
    # ahead reads that airport's budget LESS this field's, melting toward
    # 0:00 as the onward leg runs (a field with no measured figure falls
    # back to the same distance estimate the panel uses).
    j.leg_elapsed0 = j.elapsed
    _via_mins = j.route.get("via_sim_min", [])
    j.leg_base_min = 0.0
    for _vi, _v in enumerate(route_vias(j.route)):
        if _v["name"] == j.landed_name:
            j.leg_base_min = (float(_via_mins[_vi]) if _vi < len(_via_mins)
                              else 10.0 + 0.20 * float(_v["dist"]))
            break
    j.msg = ("Depart %s and resume flight to %s. Establish aircraft on "
             "runway threshold and take off."
             % (j.landed_name, dest_name))


# ----------------------------------------------------------------------
#  SAVE / LOAD GAME  (one save slot, a JSON file beside the program)
# ----------------------------------------------------------------------
SAVE_PATH = os.path.join(_writable_dir(), "learjet_save.json")
                         # v42: beside the .exe when frozen -- __file__
                         # would point inside PyInstaller's throwaway
                         # unpack folder and every save would vanish on
                         # exit. v81: _writable_dir() -- beside the
                         # program normally, the profile folder when the
                         # program's own folder is read-only


def save_jet(jet):
    """Write the whole flight -- route plus every piece of the jet's
    state -- to the save file. Returns True on success."""
    bank_flight_hours(jet)   # v78: bank the hours first, so the save and
                             # the career file always tell the same story
    bank_career_distance(jet)   # v87: and the logbook's distance with them
    try:
        data = {"route": jet.route, "jet": jet.__dict__}
        with open(SAVE_PATH, "w") as f:
            json.dump(data, f)
        return True
    except Exception:
        return False


def load_jet():
    """Rebuild a Jet from the save file. Returns the Jet, or None if
    there is no usable save."""
    try:
        with open(SAVE_PATH, "r") as f:
            data = json.load(f)
        route = data["route"]
        jet = Jet(route)
        jet.__dict__.update(data["jet"])
        jet.route = route
        # Migrate a pre-v56 save: the REAL TIME flag arrived with this
        # version, so a save made before it carries a route dict without
        # the flag -- re-read the clock from the current route table by
        # name (the figure Jet.__init__ set from the saved dict is right
        # for every save made since v56, so this only ever moves C and H).
        for _r in ROUTES:
            if _r["name"] == route["name"]:
                jet.time_scale = 1.0 if _r.get("real_time") else TIME_SCALE
                break
        # Migrate a pre-v15 save: the single enroute airport's boolean
        # via_said / via_done flags become per-airport entries, and the
        # old "v" DME channel becomes "v0" (the first enroute field).
        vias = route_vias(route)
        for attr in ("via_said", "via_done"):
            val = getattr(jet, attr, {})
            if not isinstance(val, dict):
                setattr(jet, attr,
                        {vias[0]["name"]: True} if (val and vias) else {})
        if jet.dme_chan == "v":
            jet.dme_chan = "v0" if vias else "-"
        # Migrate a pre-v19 save: the old al_late boolean (the expired
        # invitation was destination-only then) becomes an al_done entry
        # for the destination, so no second invitation appears for it.
        if getattr(jet, "al_late", False) and not jet.al_done:
            jet.al_done = [route["name"].split("-")[1]]
        return jet
    except Exception:
        return None


# ----------------------------------------------------------------------
#  CAREER FLIGHT HOURS (v78) -- the total REAL time played over every
#  route since installation, banked to a tiny JSON file beside the
#  program, so the ETA box's middle readout opens each route with the
#  hours already flown on all the others -- across sessions, shutdowns
#  and computer restarts alike.
# ----------------------------------------------------------------------
HOURS_PATH = os.path.join(_writable_dir(), "learjet_hours.json")  # v81:
                         # beside the program normally; the profile folder
                         # when the program's own folder is read-only
_career_hours_s = 0.0    # REAL seconds aloft, banked since installation


def load_career_hours():
    """Read the banked career total from disc at startup. Missing or
    unreadable file simply means a fresh career at zero."""
    global _career_hours_s
    try:
        with open(HOURS_PATH, "r") as f:
            _career_hours_s = max(0.0, float(json.load(f).get("hours_s", 0.0)))
    except Exception:
        _career_hours_s = 0.0


def bank_flight_hours(jet):
    """Bank the jet's as-yet-unbanked airborne time into the career
    file. The airborne sim-seconds are converted by the leg's own
    clock, so a compressed hour aloft counts the real minutes it
    truly took (the 1:1 REAL TIME legs convert one for one). The jet
    remembers how much of her airborne_time is banked, so calling
    this often -- every fifteen real seconds aloft, at every save, at
    every flight's end -- never double-counts, and a reloaded save
    picks the marker up with the rest of the jet's state."""
    global _career_hours_s
    committed = getattr(jet, "hours_committed", 0.0)
    airborne = max(0.0, getattr(jet, "airborne_time", 0.0))
    delta = airborne - committed
    if delta <= 0.0:
        return
    _career_hours_s += delta / max(0.1, getattr(jet, "time_scale", TIME_SCALE))
    jet.hours_committed = airborne
    try:
        with open(HOURS_PATH, "w") as f:
            json.dump({"hours_s": _career_hours_s}, f)
    except Exception:
        pass


def career_hours_now(jet):
    """The figure the ETA box shows: the banked career total plus the
    current flight's unbanked airborne minutes, in REAL seconds -- so
    the readout ticks up live as you fly, on top of every hour flown
    since installation."""
    committed = getattr(jet, "hours_committed", 0.0)
    airborne = max(0.0, getattr(jet, "airborne_time", 0.0))
    unbanked = max(0.0, airborne - committed)
    return _career_hours_s + unbanked / max(0.1, getattr(jet, "time_scale",
                                                        TIME_SCALE))


# ----------------------------------------------------------------------
#  THE PILOT'S LOGBOOK (v87) -- the career statistics on the
#  Introduction screen. Everything the flight recorder already watched
#  used to die with the flight; now the tale is banked to a little JSON
#  file beside the save and the hours, and the front door shows it.
#
#  THREE banking moments:
#    * bank_career_distance() rides with bank_flight_hours() -- every
#      fifteen real seconds aloft, at every save, at every flight's end
#      -- the save/load-safe committed-marker pattern the hours use.
#    * bank_arrival_stats() fires at EACH full stop (from step()), so a
#      [C] stopover-continue counts its landing before flying on.
#    * bank_flight_end_stats() fires once per flight at flight_hud's
#      exit, whatever ended her -- landing, prang, abandon or quit.
#  The ETA ghost (v80) is pure floats -- no Jet, no step(), no banking.
# ----------------------------------------------------------------------
STATS_PATH = os.path.join(_writable_dir(), "learjet_stats.json")
                         # beside the program normally; the profile folder
                         # when the program's own folder is read-only

_stats = {}             # the career logbook, loaded at startup

_STATS_DEFAULTS = {
    "flights": 0,             # flights that got airborne, any ending
    "arrivals": 0,            # full stops, every airport, stopovers too
    "arrivals_hand": 0,       # ... of which hand-flown
    "arrivals_auto": 0,       # ... of which the autoland's
    "prangs": 0,
    "greasers": 0,            # hand-flown arrivals gentler than 150 fpm
    "best_touch_fpm": None,   # smoothest HAND-FLOWN touchdown (fpm, < 0)
    "best_touch_apt": "",     # ... and where it was
    "distance_nm": 0.0,       # career distance flown
    "highest_alt": 0.0,       # highest altitude ever reached
    "airports": [],           # every airport ever put down on (sorted)
    "legs_done": [],          # routes finished at their destination
    "route_counts": {},       # flights per route name -- the favourite
    "best_rating": 0,         # best crash-debrief handling percentage
    "deadstick": 0,           # landed after the tanks ran dry (v37)
    "cab_survivals": 0,       # pressurisation failures survived
    "streak": 0,              # current run of clean-arrival flights
    "best_streak": 0,         # ... and the best run ever
    "first_flight": "",       # "Mar 2026" -- the day the career began
    "last_flight": "",        # "KARRATHA-PERTH, Tue 15 Sep"
}

LAP_NM = sum(int(r["dist"]) for r in ROUTES)   # the whole Lap: 6,294 nm


def load_stats():
    """Read the logbook from disc at startup. A missing or unreadable
    file simply means a fresh, unwritten book."""
    global _stats
    _stats = dict(_STATS_DEFAULTS)
    try:
        with open(STATS_PATH, "r") as f:
            data = json.load(f)
        for k, v in data.items():
            if k in _STATS_DEFAULTS:
                _stats[k] = v
    except Exception:
        pass


def _save_stats():
    """Write the logbook. Guarded like the hours file: any trouble and
    the book simply waits for the next banking moment."""
    try:
        with open(STATS_PATH, "w") as f:
            json.dump(_stats, f)
    except Exception:
        pass


def bank_career_distance(jet):
    """Bank the jet's as-yet-unbanked distance into the logbook. The
    same committed-marker pattern as bank_flight_hours(): the jet
    remembers how much of her dist_flown is banked, so calling this
    often never double-counts, and a reloaded save picks the marker
    up with the rest of her state. (A fly-around counts her furthest
    reach; the miles back to the field are not flown twice.)"""
    committed = getattr(jet, "dist_committed", 0.0)
    flown = max(0.0, getattr(jet, "dist_flown", 0.0))
    delta = flown - committed
    if delta <= 0.0:
        return
    _stats["distance_nm"] = float(_stats.get("distance_nm", 0.0)) + delta
    jet.dist_committed = flown
    _save_stats()


def bank_arrival_stats(jet):
    """Bank ONE landing, called from step() at the moment of the full
    stop -- so every landing counts, the enroute stopover included,
    even when the captain presses [C] and the flight flies on. The
    greasers and the smoothest-touchdown record book HAND-FLOWN
    arrivals only: an autoland greaser is hers, not yours."""
    _stats["arrivals"] = int(_stats.get("arrivals", 0)) + 1
    hand = not getattr(jet, "autoland", False)   # still True at the stop;
    # the autoland releases herself a breath later in the same step()
    if hand:
        _stats["arrivals_hand"] = int(_stats.get("arrivals_hand", 0)) + 1
        sink = float(getattr(jet, "touch_vsi", 0.0))
        if sink > -150.0:
            _stats["greasers"] = int(_stats.get("greasers", 0)) + 1
        best = _stats.get("best_touch_fpm")
        if best is None or sink > float(best):
            _stats["best_touch_fpm"] = int(round(sink))
            _stats["best_touch_apt"] = getattr(jet, "landed_name", "") or ""
    else:
        _stats["arrivals_auto"] = int(_stats.get("arrivals_auto", 0)) + 1
    name = getattr(jet, "landed_name", None)
    if name:
        apts = set(_stats.get("airports", []))
        apts.add(name)
        _stats["airports"] = sorted(apts)
    if getattr(jet, "said_empty", False):
        # Landed after the tanks ran dry -- the v37 glide, earned.
        _stats["deadstick"] = int(_stats.get("deadstick", 0)) + 1
    bank_career_distance(jet)
    _save_stats()


def bank_flight_end_stats(jet, outcome):
    """Bank the flight's own record, once, at flight_hud's exit.
    outcome: "crash" (the prang), "destination" (full stop at the
    route's end), "stopover" (the [R] road home from an enroute full
    stop), "abandon" (the [Z]), "quit" (ESC / DESKTOP mid-flight).
    Only a concluded flight -- landed or pranged -- moves the streak
    and earns a handling rating; an abandon or a quit simply leaves
    the streak be."""
    airborne = getattr(jet, "airborne_time", 0.0) > 0.0
    route_name = ""
    try:
        route_name = jet.route["name"]
    except Exception:
        pass
    if airborne and route_name:
        _stats["flights"] = int(_stats.get("flights", 0)) + 1
        counts = dict(_stats.get("route_counts", {}))
        counts[route_name] = int(counts.get(route_name, 0)) + 1
        _stats["route_counts"] = counts
        if not _stats.get("first_flight"):
            _stats["first_flight"] = time.strftime("%b %Y")
        _stats["last_flight"] = "%s, %s" % (route_name,
                                            time.strftime("%a %d %b"))
        _stats["highest_alt"] = max(float(_stats.get("highest_alt", 0.0)),
                                    float(getattr(jet, "max_alt", 0.0)))
    if outcome in ("crash", "destination", "stopover"):
        # A concluded flight earns its handling rating, whatever the
        # ending -- the crash screen always rated the prangs; now the
        # logbook keeps the best day's figure from every landing too.
        try:
            rating = flight_review(jet)[0]
            _stats["best_rating"] = max(int(_stats.get("best_rating", 0)),
                                        int(rating))
        except Exception:
            pass
        _stats["cab_survivals"] = (int(_stats.get("cab_survivals", 0))
                                   + int(getattr(jet, "cab_survivals", 0)))
    if outcome == "crash":
        _stats["prangs"] = int(_stats.get("prangs", 0)) + 1
        _stats["streak"] = 0
    elif outcome in ("destination", "stopover"):
        _stats["streak"] = int(_stats.get("streak", 0)) + 1
        _stats["best_streak"] = max(int(_stats.get("best_streak", 0)),
                                    int(_stats["streak"]))
        if outcome == "destination" and route_name:
            legs = set(_stats.get("legs_done", []))
            legs.add(route_name)
            _stats["legs_done"] = sorted(legs)
    bank_career_distance(jet)
    _save_stats()

# ----------------------------------------------------------------------
#  SOUND -- bings, buzzers and the siren synthesised in code; the
#  flight-long cruise ambience is a real recording (v41, see
#  CRUISE_SOUND_CANDIDATES), with the synthesised loops as fallback
# ----------------------------------------------------------------------
SND_RATE = 44100
AUDIO_OK = False
SND = {}
_ch_idle = _ch_whine = _ch_wind = _ch_buzz = _ch_rumble = _ch_purr = None
_ch_siren = None
_ch_takeoff = None
_ch_landing = None
_sound_muted = False
_cruise_music_ok = False   # True once the cabin-atmos recording is loaded
_takeoff_snd_ok = False    # True once the takeoff recording is loaded (v62)
_landing_snd_ok = False    # True once the landing recording is loaded (v63)
_landed_hold_until = 0     # v73: pygame ticks when the post-full-stop
                           # three-second hold on the landed details ends.
                           # While it runs the full stop does NOT hush the
                           # cockpit -- all sound continues (audio_update
                           # reads it through _landed_hold_active()).


def _tone(freq, ms, vol=0.5, decay=True, shape="sine"):
    """A mono float tone. decay=False gives a seamless 1-second loop."""
    n = int(SND_RATE * ms / 1000)
    out = []
    for i in range(n):
        t = i / SND_RATE
        s = math.sin(2.0 * math.pi * freq * t)
        if shape == "square":
            s = (0.8 if s >= 0 else -0.8) + 0.2 * s   # softened square
        env = math.exp(-4.0 * i / n) if decay else 1.0
        out.append(vol * s * env)
    return out


def _sweep(f0, f1, ms, vol=0.5):
    """A tone that slides from f0 to f1 Hz while fading away."""
    n = int(SND_RATE * ms / 1000)
    out = []
    ph = 0.0
    for i in range(n):
        f = f0 + (f1 - f0) * i / n
        ph += 2.0 * math.pi * f / SND_RATE
        out.append(vol * math.sin(ph) * math.exp(-3.0 * i / n))
    return out


def _mix(*tracks):
    n = max(len(t) for t in tracks)
    out = [0.0] * n
    for t in tracks:
        for i, s in enumerate(t):
            out[i] += s
    peak = max(1.0, max(abs(s) for s in out))
    return [s / peak * 0.95 for s in out]


def _loop_tones(freqs, vols):
    """Seamless 1-second loop of steady sines (integer Hz, whole cycles)."""
    n = SND_RATE
    out = [0.0] * n
    for f, v in zip(freqs, vols):
        for i in range(n):
            out[i] += v * math.sin(2.0 * math.pi * f * i / SND_RATE)
    peak = max(1.0, max(abs(s) for s in out))
    return [s / peak * 0.95 for s in out]


def _to_sound(pcm):
    a = array.array("h")
    for s in pcm:
        v = int(max(-1.0, min(1.0, s)) * 32767)
        a.append(v)
        a.append(v)                      # same sample on L and R
    return pygame.mixer.Sound(buffer=a.tobytes())


def audio_init():
    """Build every sound and start the continuous loops (at volume 0).
    Any audio trouble HERE and the whole game simply stays silent. The
    three real recordings (v41/v62/v63) then load separately, each on
    its own -- trouble THERE can no longer silence the sim (v81)."""
    global AUDIO_OK, _ch_idle, _ch_whine, _ch_wind, _ch_buzz, _ch_rumble, _ch_purr
    global _ch_siren, _cruise_music_ok, _ch_takeoff, _takeoff_snd_ok
    global _ch_landing, _landing_snd_ok
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init(SND_RATE, -16, 2, 512)
        # Twelve channels, the first NINE RESERVED for the sim's own
        # loops (0-6), the takeoff roar (7, v62) and the landing voice
        # (8, v63): an auto-picked bing or crash tone (channels 9-11)
        # can never steal either recording mid-flight.
        pygame.mixer.set_num_channels(12)
        pygame.mixer.set_reserved(9)
        # The BING - a cabin chime: three harmonics with a gentle decay.
        bing = _mix(_tone(880, 400, 0.55), _tone(1318, 400, 0.22),
                    _tone(659, 400, 0.18))
        gap = [0.0] * int(SND_RATE * 0.12)
        SND["bing"] = _to_sound(bing)
        SND["bing2"] = _to_sound(bing + gap + bing)         # double bing
        SND["crash"] = _to_sound(_sweep(400, 90, 900, 0.5))  # the prangs
        # Continuous loops
        SND["idle"] = _to_sound(_loop_tones([80, 160, 240],
                                            [0.30, 0.15, 0.08]))
        SND["whine"] = _to_sound(_loop_tones([500, 1000, 1500, 2200],
                                             [0.22, 0.16, 0.10, 0.05]))
        SND["wind"] = _to_sound(_loop_tones([180, 260, 340, 420, 500],
                                            [0.12, 0.10, 0.08, 0.06, 0.05]))
        # The CRUISE VOICE, part 1: a deep airframe rumble, felt as much
        # as heard -- the engine core turning over beneath everything.
        SND["rumble"] = _to_sound(_loop_tones([45, 90, 135],
                                              [0.30, 0.18, 0.08]))
        # The CRUISE VOICE, part 2: a smooth high "purr" for the fans at
        # speed -- the buzzy climb whine crossfades into this gentler
        # whistle as the jet slides into the cruise.
        SND["purr"] = _to_sound(_loop_tones([440, 880, 1320],
                                            [0.20, 0.10, 0.04]))
        SND["buzz"] = _to_sound(_buzzer_loop())
        # The CAB PRESS siren (v30): the police-style HIGH-LOW loop.
        SND["siren"] = _to_sound(_siren_loop())
        _ch_idle = pygame.mixer.Channel(0)
        _ch_whine = pygame.mixer.Channel(1)
        _ch_wind = pygame.mixer.Channel(2)
        _ch_buzz = pygame.mixer.Channel(3)
        _ch_rumble = pygame.mixer.Channel(4)
        _ch_purr = pygame.mixer.Channel(5)
        _ch_siren = pygame.mixer.Channel(6)
        _ch_takeoff = pygame.mixer.Channel(7)   # the takeoff roar (v62)
        _ch_landing = pygame.mixer.Channel(8)   # the landing voice (v63)
        for ch, key in ((_ch_idle, "idle"), (_ch_whine, "whine"),
                        (_ch_wind, "wind"), (_ch_buzz, "buzz"),
                        (_ch_rumble, "rumble"), (_ch_purr, "purr"),
                        (_ch_siren, "siren")):
            ch.set_volume(0.0)
            ch.play(SND[key], loops=-1)
        AUDIO_OK = True
    except Exception:
        AUDIO_OK = False
    if not AUDIO_OK:
        return
    # The three real recordings each load on their OWN (v81): they live
    # outside the core guard now, so a codec hiccup, a short file or a
    # bare print() on a console-less --windowed build can never cost the
    # sim its synthesised voice -- the bings, the buzzer and the siren
    # are already alive above, whatever happens below.
    _load_cruise_music()
    _load_takeoff_sound()
    _load_landing_sound()


def _load_cruise_music():
    """The cruise atmosphere (v41): stream the real recording on the
    music channel, looping forever at volume 0 -- audio_update() raises
    it while a flight is live and lowers it afterwards. Missing or
    undecodable file: the flag stays False and the synthesised v8 cruise
    voice carries on as the fallback. The load REPORTS itself, as the
    roar and the landing voice always have (v81) -- the report also
    lands in the little log file beside the program."""
    global _cruise_music_ok
    _cruise_music_ok = False
    try:
        for path in CRUISE_SOUND_CANDIDATES:
            try:
                if path and os.path.exists(path):
                    pygame.mixer.music.load(path)
                    pygame.mixer.music.set_volume(0.0)
                    pygame.mixer.music.play(-1)   # loops for the session
                    _cruise_music_ok = True
                    _say("Cruise atmosphere loaded: %s" % path)
                    break
            except Exception as exc:
                _say("Cruise atmosphere would not load from %s (%s)"
                     % (path, exc))
        if not _cruise_music_ok:
            _say("CRUISE ATMOSPHERE NOT LOADED -- looked in:")
            for path in CRUISE_SOUND_CANDIDATES:
                _say("    %s  %s" % (path, "(found)"
                      if os.path.exists(path) else "(missing)"))
    except Exception:
        _cruise_music_ok = False


def _load_takeoff_sound():
    """The takeoff roar (v62): load the trimmed takeoff recording onto
    its reserved channel's sound. The load REPORTS itself -- a missing
    or undecodable file must never fail in silence. Any trouble: the
    flag stays False and the ambience carries the takeoff as before."""
    global _takeoff_snd_ok
    _takeoff_snd_ok = False
    try:
        for path in TAKEOFF_SOUND_CANDIDATES:
            try:
                if path and os.path.exists(path):
                    SND["takeoff"] = pygame.mixer.Sound(file=path)
                    _takeoff_snd_ok = True
                    _say("Takeoff sound loaded: %s" % path)
                    break
            except Exception as exc:
                _say("Takeoff sound would not load from %s (%s)"
                     % (path, exc))
        if not _takeoff_snd_ok:
            _say("TAKEOFF SOUND NOT LOADED -- looked in:")
            for path in TAKEOFF_SOUND_CANDIDATES:
                _say("    %s  %s" % (path, "(found)"
                      if os.path.exists(path) else "(missing)"))
    except Exception:
        _takeoff_snd_ok = False


def _load_landing_sound():
    """The landing voice (v63): the landing recording, looping from the
    led 400 ft mark above the field (v66) until the wheels stop. Same
    codec note as the roar -- WAV first, MP3 welcome; the load reports
    itself either way."""
    global _landing_snd_ok
    _landing_snd_ok = False
    try:
        for path in LANDING_SOUND_CANDIDATES:
            try:
                if path and os.path.exists(path):
                    SND["landing"] = pygame.mixer.Sound(file=path)
                    _landing_snd_ok = True
                    _say("Landing sound loaded: %s" % path)
                    break
            except Exception as exc:
                _say("Landing sound would not load from %s (%s)"
                     % (path, exc))
        if not _landing_snd_ok:
            _say("LANDING SOUND NOT LOADED -- looked in:")
            for path in LANDING_SOUND_CANDIDATES:
                _say("    %s  %s" % (path, "(found)"
                      if os.path.exists(path) else "(missing)"))
    except Exception:
        _landing_snd_ok = False


def _siren_loop():
    """The CAB PRESS siren (v30): a police-style HIGH-LOW two-tone,
    looping. Half a second at 880 Hz, half a second at 660 Hz -- whole
    cycles of each, so the loop joins seamlessly -- with odd harmonics
    for the bite a warning needs to cut through the wind and the fans."""
    out = []
    for i in range(SND_RATE):
        t = i / SND_RATE
        f = 880.0 if t < 0.5 else 660.0
        w = 2.0 * math.pi * f * t
        s = math.sin(w) + 0.30 * math.sin(3.0 * w) + 0.12 * math.sin(5.0 * w)
        out.append(0.42 * s)
    return out


def _buzzer_loop():
    """The stall buzzer: a 220 Hz pulse, eight times a second, looping."""
    n = SND_RATE // 2          # half a second: 110 cycles, 4 pulses exactly
    out = []
    for i in range(n):
        t = i / SND_RATE
        gate = 1.0 if (t * 8.0) % 1.0 < 0.55 else 0.0
        s = math.sin(2.0 * math.pi * 220.0 * t)
        s = (0.8 if s >= 0 else -0.8) + 0.2 * s
        out.append(0.45 * s * gate)
    return out


def play_bing(kind="bing"):
    if AUDIO_OK and not _sound_muted and kind in SND:
        try:
            SND[kind].play()
        except Exception:
            pass


def play_takeoff_sound(j):
    """THE TAKEOFF ROAR (v62): the instant the thrust lever reaches 100%
    for the roll -- engines running, on the ground, never in the landing
    rollout (where [+] winds the reversers) -- the takeoff recording
    starts on its reserved channel and plays out in full, the cabin
    ambience stepping aside until it ends (audio_update owns that
    hand-back). A press of [+] while the roar is already playing does
    NOT restart it. If the file never loaded, the call is a no-op and
    the flight sounds exactly as it always has."""
    if not (AUDIO_OK and _takeoff_snd_ok):
        return
    if j.airborne or j.rollout or j.dead or j.done:
        return
    try:
        if not _ch_takeoff.get_busy():
            _ch_takeoff.play(SND["takeoff"])
            _ch_takeoff.set_volume(
                0.0 if (_sound_muted or j.paused) else TAKEOFF_SND_VOL)
    except Exception:
        pass


def _landed_hold_active():
    """v73: True during the three REAL seconds the landed details hold on
    the panel after the full stop -- all sound continues meanwhile, so the
    j.done hush in audio_update waits for the hold to run out."""
    return _landed_hold_until > pygame.time.get_ticks()


def audio_update(j):
    """Called every HUD frame: the voice of the jet, re-voiced for cruise.

    Real cruise is WIND-led: the rush of air over the fuselage is the
    loudest sound at high speed, with the fans purring smoothly beneath
    it and a deep airframe rumble below everything. So:
      - the wind now SWELLS with airspeed and leads the mix in the
        cruise (was a quiet background wash),
      - the buzzy climb whine crossfades into a smooth high "purr" as
        the speed builds past 150-250 kt, and softens as N1 settles,
      - a faint low rumble hums along whenever the engines are turning.
    The stall buzzer still sounds while the wing is stalled, the CAB
    PRESS siren wails its police-style HIGH-LOW the whole time the
    pressurisation warning burns -- until the jet is brought below
    10,000 ft and the light goes out (v30) -- and the cockpit falls
    silent while paused, muted, or the flight is over.

    v41: the whole synthesised ambience above (idle hum, climb whine,
    wind rush, rumble and purr) is REPLACED by the cabin-atmosphere
    recording on the music stream; v43: it plays at a steady level
    from ENGINE START to shutdown. If the recording failed to load,
    _cruise_music_ok is False and the old mix below runs unchanged.
    v62: while the takeoff recording plays it LEADS the mix instead --
    the ambience steps aside and is heard again the moment the roar is
    done."""
    if not AUDIO_OK:
        return
    n1f = j.n1 / 100.0
    # v73: during the three-second hold on the landed details the full
    # stop does NOT hush the cockpit -- all sound continues until the
    # continue options appear.
    done_hush = j.done and not _landed_hold_active()
    if _sound_muted or j.paused or j.dead or done_hush:
        ev = wv = bv = sv = 0.0
    else:
        ev = 1.0 if j.engines else 0.0
        # Wind: the power curve keeps it modest on the takeoff roll and
        # lets it bloom into the lead once the jet is truly moving.
        wv = (min(1.0, j.ias / 330.0) ** 1.4) if j.airborne else 0.0
        bv = 1.0 if ((j.ias < stall_speed(j)) and j.airborne) else 0.0
        # The CAB PRESS siren (v30): on with the warning light, off the
        # moment the light goes out below 10,000 ft.
        sv = 1.0 if getattr(j, "cab_light", False) else 0.0
    # Whine -> purr crossfade, keyed on airspeed: fully buzzy below
    # 150 kt (takeoff and approach), fully smooth above 250 kt (cruise),
    # blending between. The purr also eases off a touch as N1 settles
    # toward cruise, so the fans recede UNDER the wind as they should.
    mix = max(0.0, min(1.0, (j.ias - 150.0) / 100.0)) if j.airborne else 0.0
    n1_soft = 1.0 - 0.30 * max(0.0, min(1.0, (n1f - 0.70) / 0.25))
    whine_base = 0.60 * ev * n1f
    # v43: the recording waits for the engines -- [E] brings the cabin
    # alive, shutdown or flameout hushes it. Mute, pause and the end
    # of the flight still silence it too.
    ambience_on = j.engines and not (_sound_muted or j.paused or j.dead or done_hush)
    # v62: the takeoff roar. While the recording plays it LEADS -- the
    # cabin ambience steps aside and is heard again the moment the roar
    # ends. A rejected takeoff (the lever chopped below 100% before
    # liftoff, or the engines shut down on the ground) ends it early;
    # the prang and the full stop end it at once; the pause holds it
    # mid-note, and [M] silences it like everything else.
    takeoff_playing = False
    try:
        if _takeoff_snd_ok:
            takeoff_playing = _ch_takeoff.get_busy()
            if takeoff_playing and (j.dead or done_hush):
                _ch_takeoff.stop()
                takeoff_playing = False
            elif (takeoff_playing and not j.airborne and not j.rollout
                    and (j.thrust < 100.0 or not j.engines)):
                _ch_takeoff.stop()      # the rejected takeoff
                takeoff_playing = False
            if takeoff_playing:
                if j.paused:
                    _ch_takeoff.pause()     # hold the roar mid-note
                else:
                    _ch_takeoff.unpause()
                _ch_takeoff.set_volume(
                    0.0 if (_sound_muted or j.paused) else TAKEOFF_SND_VOL)
    except Exception:
        pass
    # v63: the landing voice. Descending toward 400 ft above the field
    # ahead starts the landing recording LOOPING, and only the FULL STOP
    # ends it -- the prang ends it sooner, and a go-around that climbs
    # back above the re-arm ends it and re-arms the trigger for the next
    # attempt. v66: the trigger now LEADS the 400 ft mark by
    # LANDING_LEAD_S real seconds, flown against the live sink rate and
    # the leg's own clock -- the file starts the same few real seconds
    # early on every leg. While it leads, the cabin ambience steps
    # aside, exactly as it does for the takeoff roar; the pause holds
    # it mid-note and [M] silences it like everything else. A [V] peek
    # at the map hushes it (audio_off), and it rejoins on the return
    # to the cockpit. v74: on the two 1:1 REAL TIME legs she does not
    # fly at all -- the cruise recording continues undisturbed there,
    # by the captain's standing order.
    landing_playing = False
    try:
        if _landing_snd_ok:
            # v74: no landing voice on the two 1:1 REAL TIME legs -- by
            # the captain's standing order the cruise recording simply
            # continues undisturbed there, all the way to the full stop.
            # Every COMPRESSED leg keeps her, exactly as v63/v66 made her.
            if j.dead or done_hush or j.route.get("real_time"):
                j.landing_snd_on = False       # the full stop / the prang /
                                               # a REAL TIME leg (v74) --
                                               # the v73 three-second hold
                                               # lets her play on meanwhile
            else:
                agl = j.alt - float(next_airport(j)["elev"])
                # v66: the moving trigger -- 400 ft plus the lead. The
                # lead is LANDING_LEAD_S REAL seconds of the CURRENT
                # sink rate (fpm -> ft per sim-second, times the leg's
                # own clock), capped so a steep, fast descent cannot
                # wake the voice hundreds of feet early. v122: the lead
                # is retired to 0.0, so the trigger IS the 400 ft mark
                # and the recording starts at its proper cue, not four
                # loops ahead of it.
                sink_fps = max(0.0, -j.vsi) / 60.0
                lead_ft = min(LANDING_LEAD_MAX_FT,
                              LANDING_LEAD_S
                              * getattr(j, "time_scale", TIME_SCALE)
                              * sink_fps)
                trig_ft = LANDING_TRIG_FT + lead_ft
                rearm_ft = trig_ft + LANDING_REARM_GAP_FT
                # v75: THE MOVING-TARGET RACE, FIXED. The old crossing
                # test -- prev_agl > trig_ft >= agl -- compared LAST
                # frame's height against THIS frame's trigger, but the
                # trigger itself moves with the live sink rate, and the
                # v46 approach chop dances it up and down by a couple of
                # hundred feet. Whenever the sink deepened between frames
                # the trigger jumped UP over the descending jet and the
                # strict test never registered: the voice stayed silent
                # for the whole approach. A coin toss at every airport --
                # on the unlucky Melbourne-Sydney run Merimbula sounded
                # and Sydney never did. The state machine is now explicit:
                # she ARMS whenever she is up above the re-arm line (and
                # disarms on the ground, so a low departure past a high
                # next field still cannot wake it), and an armed jet
                # descending at/below the led mark starts the voice. The
                # moving trigger now only chooses WHERE the file starts,
                # never WHETHER it starts. (_lnd_armed defaults True for a
                # save loaded in mid-air, matching the old first-frame
                # branch; on the ground the next line disarms it.)
                armed = getattr(j, "_lnd_armed", bool(j.airborne))
                if not j.airborne:
                    armed = False
                elif agl > rearm_ft:
                    armed = True
                if (armed and j.airborne and j.vsi < 0.0
                        and agl <= trig_ft):
                    j.landing_snd_on = True    # down to/below the led mark
                    armed = False
                elif (getattr(j, "landing_snd_on", False)
                        and j.airborne and agl > rearm_ft):
                    j.landing_snd_on = False   # the go-around re-arms it
                j._lnd_armed = armed
            landing_playing = getattr(j, "landing_snd_on", False)
            if landing_playing:
                if not _ch_landing.get_busy():
                    _ch_landing.play(SND["landing"], loops=-1)
                if j.paused:
                    _ch_landing.pause()      # hold the voice mid-note
                else:
                    _ch_landing.unpause()
                _ch_landing.set_volume(
                    0.0 if (_sound_muted or j.paused) else LANDING_SND_VOL)
            elif _ch_landing.get_busy():
                _ch_landing.stop()
    except Exception:
        pass
    fx_playing = takeoff_playing or landing_playing
    try:
        if _cruise_music_ok:
            # The recording carries the flight: the synthesised idle,
            # whine, wind, rumble and purr stay silent under it. While
            # the roar or the landing voice leads (v62/v63) the
            # recording waits at zero.
            pygame.mixer.music.set_volume(
                CRUISE_MUSIC_VOL if (ambience_on and not fx_playing)
                else 0.0)
            _ch_idle.set_volume(0.0)
            _ch_whine.set_volume(0.0)
            _ch_purr.set_volume(0.0)
            _ch_rumble.set_volume(0.0)
            _ch_wind.set_volume(0.0)
        else:
            # The synthesised fallback ducks too while a recording leads.
            duck = 0.0 if fx_playing else 1.0
            _ch_idle.set_volume(0.30 * ev * duck)
            _ch_whine.set_volume(whine_base * (1.0 - mix) * duck)
            _ch_purr.set_volume(whine_base * mix * n1_soft * duck)
            _ch_rumble.set_volume(0.22 * ev * (0.4 + 0.6 * n1f) * duck)
            _ch_wind.set_volume(0.62 * wv * duck)
        _ch_buzz.set_volume(0.50 * bv)
        _ch_siren.set_volume(0.50 * sv)
    except Exception:
        pass


def audio_off():
    """Silence every loop (called when leaving the cockpit)."""
    if not AUDIO_OK:
        return
    try:
        for ch in (_ch_idle, _ch_whine, _ch_wind, _ch_buzz,
                   _ch_rumble, _ch_purr, _ch_siren):
            ch.set_volume(0.0)
        if _takeoff_snd_ok:
            _ch_takeoff.stop()   # v62: the roar never outlives the flight
        if _landing_snd_ok:
            _ch_landing.stop()   # v63: the map and the screens hush the
                                 # landing voice; it rejoins on the return
        if _cruise_music_ok:
            pygame.mixer.music.set_volume(0.0)
    except Exception:
        pass


def stop_enroute_sound():
    """Silence the Enroute screen's voice as the screen is left (v84):
    the cabin-atmosphere recording is dropped back to zero -- the
    cockpit's audio_update() raises it again on the next frame if the
    flight is due hers -- and the fallback blink-buzzer is left silent
    too (audio_update sets the buzzer channel correctly again the same
    way)."""
    if AUDIO_OK:
        try:
            _ch_buzz.set_volume(0.0)
        except Exception:
            pass
        try:
            if _cruise_music_ok:
                pygame.mixer.music.set_volume(0.0)
        except Exception:
            pass

# ----------------------------------------------------------------------
#  KEY HANDLING
# ----------------------------------------------------------------------
def turn_step(j, direction):
    """One 5-degree turn step: [A] = -1 (left), [D] = +1 (right). Both the
    keypress itself and the hold-to-turn auto-repeat (see flight_hud) come
    through here, so the two paths behave identically: with the autopilot
    on the heading BUG moves instead; on the ground the engines must be
    running, and the ground turn speaks through taxi_turn_msg."""
    if j.ap:
        j.bug = (j.bug + 5.0 * direction) % 360.0
        j.msg = "Heading bug %03d." % j.bug
    elif not j.airborne and not j.engines:
        j.msg = "Engines are off - start them [E] to turn her."
    else:
        j.hdg = (j.hdg + 5.0 * direction) % 360.0
        j.bug = j.hdg
        # Attitude Indicator: command a 40-degree bank into the turn
        # (v40: was thirty), HELD through the turn (v33) -- see
        # TURN_HOLD_S in step().
        j.bank_target = TURN_BANK_DEG * direction
        j.bank_turn_t = j.elapsed
        if not j.airborne:
            taxi_turn_msg(j)


PITCH_STEP_DEG = 1.0    # one key press = one degree of pitch (v35)
PITCH_CMD_MAX = 30.0    # the pitch command lives within thirty degrees
                      # either way (v36: was ten) -- matching the AI's
                      # pitch ladder, whose labels run to 30
MACH_SHOW = 0.4         # IAS/MACH changeover (v38): faster than this --
MACH_ALT_FT = 18000.0   # or above this altitude -- the IAS box reads MACH


def accept_autoland(j):
    """Accept the AUTOLAND invitation on the table -- [Y], or a click on
    the flashing A/L? placard (v60). The autoland IS the autopilot, so
    [P] is forced back on even if it was pressed after the invitation
    appeared; a level-off capture would only confuse the profile."""
    j.al_apt = j.al_offer_apt   # whose landing she is flying (v19)
    j.al_offer = False
    j.autoland = True
    j.ap = True
    j.level_cap = False
    j.msg = ("AUTOLAND engaged to %s - gear, flaps, speed and sink are "
             "mine. [Y] again hands her back." % (j.al_apt or "the airport"))
    play_bing()


def cancel_autoland(j, how):
    """Every voluntary way OUT of an engaged autoland runs through here
    (v60). [Y] asks for her back POLITELY: the autopilot keeps the
    heading bug and levels her where she is (the v23 capture), so the
    hand-back is steady at any point of the approach, short final
    included. [W]/[S] or [P] take her the direct way -- the autopilot
    comes fully off too, so "you have the controls" is finally the truth
    (it used to leave the AP flying the vertical toward the assigned
    flight level -- a quiet climb order on short final). Either way the
    field joins al_done, so the invitation cannot pop straight back up
    while she is still in range, and the expiry grace keeps the descent
    chatter quiet for a few seconds. (The v19 missed-runway hand-back is
    no request of the captain's and keeps its own path.)"""
    apt = j.al_apt
    j.autoland = False
    j.al_apt = None
    if apt and apt not in j.al_done:
        j.al_done.append(apt)
    j.al_expire_t = j.elapsed   # the 8-s descent-chatter grace
    # No play_bing() in here -- each caller decides whether the way out
    # earns a chime.
    if how == "y":
        if j.airborne:
            # Ask for her back politely and the hand-back is steady:
            # the level-off capture (v23) engages HERE, the autopilot
            # keeping the heading bug.
            j.level_cap = True
            j.level_target = j.alt
            j.level_phase = 0
            j.msg = ("Autoland OFF - levelling at %s ft, autopilot on the "
                     "bug. [P] for full manual." % format(
                         int(round(j.alt / 100.0) * 100), ","))
        else:
            # She is rolling out -- the brakes and reverser stay as the
            # autoland set them; the v53 full-stop logic tidies up.
            j.msg = "Autoland OFF - you have the rollout, captain."
    elif how == "pitch":
        # [W]/[S] take her the direct way -- the autopilot comes fully
        # off too, so "you have the controls" is finally the truth.
        j.ap = False
        j.msg = "Autoland OFF - you have the controls."
    elif how == "p":
        j.msg = "Autopilot OFF - autoland cancelled, you have her."


def pitch_step(j, direction):
    """One one-degree pitch step: [W] = +1 (nose up), [S] = -1 (nose
    down), airborne only. v35: the pitch command speaks DEGREES now --
    read the flight-path angle the VSI command currently asks for at
    the present speed (the flap balloon included, since the VSI carries
    it too), snap it a whole degree in the stepped direction, and write
    back the VSI command that flies the new angle at the present speed.
    Both the keypress itself and the hold-to-repeat steps come through
    here, so the two paths behave identically -- like the [A]/[D]
    turns. Any pitch input still releases a level-off capture and
    cancels the autoland -- v60: genuinely now, the autopilot comes
    off too, exactly as the old fpm steps did."""
    if not j.airborne:
        return
    j.level_cap = False   # pilot overrides the level-off capture
    if j.autoland:
        cancel_autoland(j, "pitch")
    ias = max(30.0, j.ias)
    cur_deg = math.degrees(math.atan2(j.vsi_cmd + j.flap_lift, ias * 101.3))
    if direction > 0:
        new_deg = math.floor(cur_deg + 1e-6) + PITCH_STEP_DEG
    else:
        new_deg = math.ceil(cur_deg - 1e-6) - PITCH_STEP_DEG
    new_deg = max(-PITCH_CMD_MAX, min(PITCH_CMD_MAX, new_deg))
    j.vsi_cmd = math.tan(math.radians(new_deg)) * ias * 101.3 - j.flap_lift


RAPID_THRUST_STEP = 25.0  # v110: with Shift down, [+] (or [Up]) winds this
                          # many points a press instead of one -- the rapid
                          # increase. Four presses take the lever from idle
                          # to full thrust. THE knob: nudge it and fly again.


def thrust_step(j, sign, step=1.0):
    """One point of thrust, up or down (v93) -- or RAPID_THRUST_STEP points
    when Shift is down (v110). Every path that moves the lever -- the
    single keypress, the held-key repeat and the Shift ram alike -- comes
    through here, so the lever's disciplines hold for all of them:
      - v26: no engines, no thrust -- a reminder at INFO, the lever
        stays at idle;
      - v24: no thrust for the roll until HDG reads OBS (the enroute-
        stop departure, free at any heading, is exempt) -- a CHECK
        HEADING reminder, retired the moment she lines up;
      - v62: 100% selected on the ground starts the takeoff roar (never
        in the landing rollout, where [+] winds the reversers).
    """
    if sign > 0:
        if not j.engines:
            j.msg = "Engines are off - start them [E] first."
        elif (not j.airborne and not j.rollout
                and not getattr(j, "free_departure", False)
                and not on_obs(j)):
            j.msg = "CHECK HEADING - HDG %03d, OBS %03d: no thrust until they match. Turn [A]/[D]." % (
                int(j.hdg) % 360,
                int(getattr(j, "obs", float(j.route["hdg"]))) % 360)
        else:
            j.thrust = max(0.0, min(100.0, j.thrust + step))
            if "CHECK HEADING" in j.msg:
                j.msg = ""        # lined up now -- retire the reminder
            if (j.thrust >= 100.0 and not j.airborne and not j.rollout
                    and not j.reverser):
                # v62: 100% selected for the takeoff roll -- the roar
                # starts NOW (a repeat while it plays does not restart
                # it; play_takeoff_sound guards).
                play_takeoff_sound(j)
    else:
        j.thrust = max(0.0, min(100.0, j.thrust - step))


def handle_key(j, event):
    if j.dead or j.done:
        return
    k = event.unicode.lower() if event.unicode else ""
    shift_held = bool(event.mod & pygame.KMOD_SHIFT)
    if k == "q":
        j.quit = True
    elif k == "m":
        global _sound_muted
        _sound_muted = not _sound_muted
        j.msg = "Sound OFF." if _sound_muted else "Sound ON."
    elif k == "e":
        if j.engines:
            j.engines = False
            j.msg = "Engines shut down."
        elif j.fuel <= 0.0:
            j.msg = "No fuel - they will not start!"
        else:
            j.engines = True
            j.eng_start_t = j.elapsed
            j.msg = "Engines started. Turn into wind [A]/[D] - runway %03d." % j.route["hdg"]
    elif k == "b":
        j.brakes = not j.brakes
        j.msg = "Brakes " + ("ON." if j.brakes else "OFF.")
    elif k == "r":
        # Reverse thrust: runway only, engines running. The buckets turn
        # the thrust lever into a brake -- the more [+] you wind on, the
        # harder you stop. Works WITH the wheel brakes [B], not instead.
        if j.airborne:
            j.msg = "Reverse is for the runway only - not in the air!"
        elif not j.engines:
            j.msg = "Engines are off - nothing to reverse."
        else:
            j.reverser = not j.reverser
            if j.reverser:
                j.msg = "Reverse thrust DEPLOYED - add power [+] to brake harder."
            else:
                j.msg = "Reverse thrust stowed."
            play_bing()
    elif k == "f":
        if shift_held:
            j.flap = max(0, j.flap - 10)
        else:
            j.flap = min(50, j.flap + 10)
        j.msg = "Flaps now %d degrees." % j.flap
    elif k == "g":
        if not j.airborne:
            j.msg = "Cannot move gear while on the ground."
        elif j.gear_seq_dir != 0:
            j.msg = "Gear is already in transit - wait for it to lock."
        elif j.gear_down:
            j.gear_seq_dir = -1       # start the retraction sequence
            j.gear_t = 0.0
            j.msg = "Gear coming up ..."
        else:
            j.gear_seq_dir = +1       # start the extension sequence
            j.gear_t = 0.0
            j.msg = "Gear coming down ..."
    elif k == "p":
        if not j.airborne:
            j.msg = "Autopilot is for the air - turn into wind with [A]/[D] here."
        elif j.ap:
            j.ap = False
            if j.autoland:
                cancel_autoland(j, "p")
            else:
                j.msg = "Autopilot OFF - you have the aircraft."
            play_bing()
        elif j.ass_fl <= 0:
            j.msg = "Set an assigned flight level first [K]."
        else:
            j.ap = True
            j.msg = "Autopilot ON - flying the bug, capturing FL%d." % j.ass_fl
            play_bing()
    elif k == "a":
        turn_step(j, -1.0)
    elif k == "d":
        turn_step(j, +1.0)
    elif k == "w":
        if not j.airborne:
            if not j.engines:
                j.msg = "Engines are off! Press [E] first."
            elif j.reverser:
                j.msg = "Reverse is still deployed - stow it [R] first!"
            elif not into_wind(j) and not getattr(j, "free_departure", False):
                j.msg = "Not into wind! Turn onto runway %03d with [A]/[D]." % j.route["hdg"]
            elif j.ias >= 125.0 and j.flap <= 20:
                j.airborne = True
                j.rollout = False        # a touch-and-go is airborne now --
                                         # the landing rollout is over
                j.free_departure = False   # the enroute-stop concession
                                           # ends at liftoff (v22)
                j.vsi = 500.0
                j.vsi_cmd = 1200.0
                j.msg = "Positive rate - gear up [G]!"
            elif j.ias >= 125.0:
                j.msg = "Too much flap for takeoff (use 0-20)."
            else:
                j.msg = "Not yet - rotate at 125 kt."
        else:
            pitch_step(j, +1.0)   # v35: one degree of pitch up a press
    elif k == "s":
        if j.airborne:
            pitch_step(j, -1.0)   # v35: one degree of pitch down a press
        else:
            j.msg = "Still on the runway - [W] rotates at 125 kt."
    elif k in ("+", "="):
        # v93: ONE point a press (was five); a held key keeps winding a
        # point at a time until released -- flight_hud's hold-to-repeat
        # calls thrust_step() directly for the held steps. All the
        # lever's disciplines (v24/v26/v62) live in thrust_step now, so
        # the keypress and the held repeat share the one path.
        # v110: with Shift down this is the RAPID increase --
        # RAPID_THRUST_STEP points a press. (Typing [+] on the main
        # keyboard IS Shift+[=], so the unshifted [=] and the keypad's
        # [+] keep the one-point fine control.)
        thrust_step(j, +1.0, RAPID_THRUST_STEP if shift_held else 1.0)
    elif k in ("-", "_"):
        thrust_step(j, -1.0)
    elif event.key == pygame.K_UP:
        # v110: THE SECONDARY LEVER -- the Up/Down arrows drive the very
        # same thrust lever, one point a press exactly like [+]/[-],
        # with the same Shift ram on the way up.
        thrust_step(j, +1.0, RAPID_THRUST_STEP if shift_held else 1.0)
    elif event.key == pygame.K_DOWN:
        thrust_step(j, -1.0)
    elif k == "l":
        # Level off HERE - but gently. The jet keeps its climb/descent for
        # a moment, washes the rate off, dips just past the altitude it had
        # when the key was pressed, then eases back and settles on it.
        if not j.airborne:
            j.msg = "Still on the ground - [W] rotates at 125 kt."
        elif j.autoland:
            # She is flying the profile herself; a level-off order now
            # would only confuse the picture.
            j.msg = "AUTOLAND is flying - [Y] hands her back, or [W]/[S] for the controls."
        else:
            if j.level_cap and j.level_phase == 3 \
                    and abs(j.alt - j.level_target) < 5.0:
                # Already holding this level (v23): just confirm it --
                # re-capturing HERE would only dip her a few feet and
                # come back to the very same altitude.
                j.msg = "Level flight - holding %s ft." % format(
                    int(round(j.level_target / 100.0) * 100), ",")
            else:
                j.level_cap = True
                j.level_target = j.alt
                j.level_phase = 0
                j.msg = "Levelling off - capturing this altitude ..."
    elif k == "y":
        # THE CAPTAIN'S VETO (v60): [Y] is the autoland's whole life --
        # it ACCEPTS the invitation on the table, and once engaged the
        # same key WITHDRAWS the request and takes her back (steadily:
        # the autopilot keeps the bug and levels her where she is).
        if j.autoland:
            cancel_autoland(j, "y")
            play_bing()
        elif j.al_offer:
            accept_autoland(j)
        elif next_airport(j)["name"] in j.al_done:
            j.msg = "Too late for AUTOLAND - manual landing now."
        else:
            j.msg = "AUTOLAND is offered on approach with the autopilot on."
    elif k == "n":
        # THE CAPTAIN'S VETO (v60): [N] DECLINES the invitation on the
        # table -- the field joins the declined list so the offer cannot
        # pop straight back up, and the expiry grace keeps the descent
        # chatter quiet for a few seconds. An answer key, not a command:
        # with no offer up, [N] says nothing at all.
        if j.al_offer:
            j.al_done.append(j.al_offer_apt)
            j.al_offer = False
            j.al_expire_t = j.elapsed
            j.msg = ("AUTOLAND declined for %s - she's all yours, captain."
                     % j.al_offer_apt)
            play_bing()
    elif k == "k":
        # [K] winds the assigned flight level UP ten at a time and
        # [Shift+K] winds it back DOWN (v35) -- both wrap around the
        # 10..450 cycle, never parking at zero once set.
        if shift_held:
            j.ass_fl = (j.ass_fl - 10) % 460
            if j.ass_fl == 0:
                j.ass_fl = 450
        else:
            j.ass_fl = (j.ass_fl + 10) % 460
            if j.ass_fl == 0:
                j.ass_fl = 10
        j.msg = "Assigned FL%d (%s ft)." % (j.ass_fl, format(j.ass_fl * 100, ","))
    elif k == "h":
        if not j.airborne:
            j.msg = "Heading bug is for the air - turn with [A]/[D] here."
        else:
            j.bug = (j.bug + 10.0) % 360.0
            if not j.ap:
                j.hdg = j.bug
            j.msg = "Heading bug %03d." % j.bug
    elif k == "o":
        # Twist the OBS course selector five degrees at a time
        # ([Shift+O] winds it back the other way).
        step_deg = -5.0 if shift_held else 5.0
        j.obs = (getattr(j, "obs", float(j.route["hdg"])) + step_deg) % 360.0
        j.msg = "OBS course %03d - centre the CDI needle to fly it." % int(j.obs)
    elif k == "c":
        # Cycle the DME through its stations: destination, each enroute
        # airport in route order (if the route has any), then origin --
        # the two title letters plus every enroute airport's letter.
        o_name, d_name = j.route["name"].split("-")
        vias = route_vias(j.route)
        chans = ["-"] + ["v%d" % i for i in range(len(vias))] + ["+"]
        idx = chans.index(j.dme_chan) if j.dme_chan in chans else 0
        j.dme_chan = chans[(idx + 1) % len(chans)]
        if j.dme_chan == "-":
            j.msg = "DME(%s): distance to %s." % (AIRPORT_LETTERS.get(d_name, "?"), d_name)
        elif j.dme_chan == "+":
            j.msg = "DME(%s): distance from %s." % (AIRPORT_LETTERS.get(o_name, "?"), o_name)
        else:
            v_name = vias[int(j.dme_chan[1:])]["name"]
            j.msg = "DME(%s): distance to %s." % (AIRPORT_LETTERS.get(v_name, "?"), v_name)


# ==============================================================================
#  PHOTO-COCKPIT PANEL  --  the HUD over the stripped cockpit photograph
# ------------------------------------------------------------------------------
#  The panel canvas is 2160 x 1440: exactly TWICE the 1080 x 720 reference
#  HUD screenshot, and the same 3:2 aspect as the stripped cockpit photo,
#  so the photograph fills the canvas with no crop and no distortion, every
#  HUD element sits at 2x its reference position, and the side windows and
#  the overhead lights stay balanced at any window size. v131: the whole
#  panel is COVER-scaled onto the screen as one picture (centre-cropped,
#  the intro photo's own treatment) -- the HUD fills the whole display
#  like every other screen, and the black side bars are gone.
#  Without the photo the panel falls back to the old dark-green glass.
# ==============================================================================
PANEL_W, PANEL_H = 2160, 1440

PANEL_BG_CANDIDATES = _resource_candidates(
    "learjet_panel_bg.png", r"D:\code\learjet_panel_bg.png")

_PANEL_BG = None      # cached surface once loaded; False if missing


def _load_panel_bg():
    """The stripped cockpit photograph, scaled once to the panel canvas."""
    global _PANEL_BG
    if _PANEL_BG is not None:
        return _PANEL_BG or None
    for path in PANEL_BG_CANDIDATES:
        try:
            if path and os.path.exists(path):
                img = pygame.image.load(path).convert()
                _PANEL_BG = pygame.transform.smoothscale(img, (PANEL_W, PANEL_H))
                _say("Panel background loaded: %s" % path)
                break
        except Exception as exc:
            _say("Panel background would not load from %s (%s)" % (path, exc))
    if _PANEL_BG is None:
        _PANEL_BG = False
        _say("PANEL BACKGROUND NOT LOADED -- dark glass fallback")
    return _PANEL_BG or None


# v131: THE FULL-SCREEN HUD FIT. The panel used to letterbox -- scaled
# to FIT inside the screen, never up, centred over black -- the thick
# black side bars on every widescreen display. It now COVER-scales, the
# intro photo's own treatment: the whole panel (photograph and
# instruments together, one picture) grows until it covers the screen
# and the overflow crops away centred. The crop is BOUNDED so it can
# never eat the furniture -- at most PANEL_SAFE_CROP_Y panel pixels off
# the top and bottom (the top boxes begin 242 px down; the INFO line
# ends by ~1230 of 1440) and PANEL_SAFE_CROP_X off the sides (the IAS
# box begins 152 px in; the buttons end 114 px from the right). A
# screen so unusually shaped that even the bounded crop cannot cover
# it keeps the old centred behaviour, margins and all.
PANEL_SAFE_CROP_Y = 200
PANEL_SAFE_CROP_X = 100


def _panel_screen_fit(sw, sh):
    """The panel's cover-fit onto the screen (v131). Returns
    (scale, ox, oy, pw, ph): the panel-to-screen factor, the screen
    position of the panel's top-left corner (NEGATIVE when the
    centre-crop pushes it off-screen), and the scaled panel size.
    flight_hud draws with these figures AND maps mouse clicks back
    through them, so a button always lands exactly where it is seen."""
    cover = max(sw / PANEL_W, sh / PANEL_H)
    scale = min(cover,
                sh / float(PANEL_H - 2 * PANEL_SAFE_CROP_Y),
                sw / float(PANEL_W - 2 * PANEL_SAFE_CROP_X))
    pw, ph = int(PANEL_W * scale), int(PANEL_H * scale)
    if scale >= cover:
        # Covering the screen: a pixel to SPARE, so int() truncation
        # can never leave a one-pixel black line down an edge (the v90
        # lesson from the other screens' photographs).
        pw = max(pw, sw)
        ph = max(ph, sh)
    return scale, (sw - pw) // 2, (sh - ph) // 2, pw, ph


# Translucency recipe. v107: the near-clear TOP_FILL glass is now the
# panel's own look -- the top status boxes, HDG/OBS, the big data boxes
# (IAS / ALT / ASS FL / DME / GROUND SPEED / ETA) and the CDI track all
# wear it, so the photograph ghosts through them exactly as it does
# through CAB PRESS. The old SKY_FILL blue glass and NAVY_FILL navy
# glass are retired (v16's tidy rule: a colour nothing referenced is
# gone).
CELL_W, CELL_H = 36, 48             # the black/white diagonal cell graphic
SKY_BORD   = (240, 246, 255, 235)   # the data boxes' white inner rim
TOP_FILL   = ( 15,  30, 110,  60)   # the near-clear glass -- barely there
ETA_INFO_INK = (130, 170, 250)  # v122: the captain's colour photograph
                                    # of the ETA box settles the bottom
                                    # line -- the pale SKY BLUE its
                                    # countdown, wall clock, captions and
                                    # FLIGHT HOURS wear there, opaque, on
                                    # the box's bare glass. (The journey:
                                    # dim blue v44, ribbon navy v111,
                                    # amber v113-114, half yellow v115,
                                    # blue-on-seats v116, canary green
                                    # v117, v44 restored v118.)
ETA_INFO_SEAT = (  8,  26, 110,   0)  # v122: PARKED at alpha 0 -- the
                                    # captain's colour photograph shows
                                    # the ETA box's bottom line on BARE
                                    # glass, no badge pills behind it,
                                    # so the v116 navy seats stand down
                                    # (alpha 0 = no seat; the new pale
                                    # sky-blue ink carries the line on
                                    # its own). Raise the alpha toward
                                    # 205 only to bring the pills back.
ETA_INFO_DIM = 255              # v114's text-alpha dimmer, PARKED at
                                    # full (v115): the seat-and-ink recipe
                                    # does the dimming now -- opaque
                                    # strokes survive the 0.5 panel-to-
                                    # screen scale. Lower toward 150 only
                                    # to fade a BRIGHT ink toward the
                                    # photograph.
ETA_BOX_BLUE = (  5,  49, 245, 255)   # v123: the captain's colour
                                    # photograph's own ETA blue. v124:
                                    # worn as two SOLID BANDS hugging
                                    # the box's messages -- one behind
                                    # the big white ETA and its MIN
                                    # badge, one behind the bottom
                                    # line's three readouts, each band
                                    # the thickness of its own line --
                                    # the rest of the rectangle back on
                                    # the near-clear glass, exactly as
                                    # the photo shows. v125: the bottom
                                    # band splits in two -- a pill behind
                                    # the countdown, a pill behind the
                                    # wall clock; the hours and minutes
                                    # between them sit clear. v127: the
                                    # top band hugs the ETA figures
                                    # alone (MIN's badge sits on the
                                    # glass now) and the wall clock's
                                    # pill is retired -- only the
                                    # countdown keeps its blue. v128:
                                    # the top band is retired too --
                                    # the white ETA reads on the bare
                                    # glass; the countdown's little
                                    # pill is the box's last blue.
                                    # v129: the blue returns as TWO
                                    # full-width bands -- one behind
                                    # the whole bottom line, one
                                    # behind the captions along the
                                    # top -- each hugging its line's
                                    # ink and fitted 2 px inside the
                                    # inner white rim all round.
TOP_BORD   = ( 20,  60, 255, 255)   # the top status boxes' thick blue rim
AI_ALPHA   = 216                    # the whole attitude gauge ghosts a touch

# Panel fonts (same faces as before; at the 0.5 panel-to-screen scale they
# land exactly the size the reference HUD shows)
_panel_font = None
_panel_small_font = None
_panel_big_font = None
_panel_tiny_font = None
_panel_fh_font = None
_panel_cap_font = None
_panel_cdi_font = None
_panel_cdi_title_font = None
_panel_top_font = None

BORDER_THICK = 8   # the top status boxes' rim; the windscreen frame is 6

# The working clock on the centre window strut (v95), seated exactly over
# the photograph's own frozen clock (v96): centre and rim radius in panel
# coordinates, measured off learjet_panel_bg.png -- the panel is 2x the
# photograph, whose rim reads photo (543, 173.5), radius 20.5.
STRUT_CLOCK_CX, STRUT_CLOCK_CY, STRUT_CLOCK_R = 1086, 347, 43

# Clickable rects on the HUD (panel coordinates), filled in by draw_panel
PANEL_BUTTONS = {}


def _init_panel_fonts():
    global _panel_font, _panel_small_font, _panel_big_font, _panel_tiny_font
    global _panel_fh_font, _panel_cap_font, _panel_cdi_font, _panel_cdi_title_font
    global _panel_top_font
    _panel_font = pygame.font.SysFont("consolas", 44)
    # v94: the top status row's own smaller face -- a size down from the
    # panel face, so STALL / 1 / 2 / CAB PRESS sit well inside their
    # pills with a thick margin of box all round the letters.
    _panel_top_font = pygame.font.SysFont("consolas", 34)
    _panel_small_font = pygame.font.SysFont("consolas", 36)
    _panel_big_font = pygame.font.SysFont("consolas", 88)
    _panel_tiny_font = pygame.font.SysFont("consolas", 24)
    # The FLIGHT HOURS fallback face: a size under the tiny clock face,
    # for the rare state where the figures at the clocks' own size cannot
    # keep their seat between them. The caption face is for the three
    # little labels above the bottom line's readouts.
    _panel_fh_font = pygame.font.SysFont("consolas", 18)
    _panel_cap_font = pygame.font.SysFont("consolas", 14)
    _panel_cdi_font = pygame.font.SysFont("consolas", 40)
    # v93: the CDI nameplate's own smaller face -- at 28 the words span
    # the gauge's own width, so the title balances over the track.
    _panel_cdi_title_font = pygame.font.SysFont("consolas", 28)


def _rrect(surf, rect, fill=None, border=None, bw=0, radius=24):
    """Rounded rect on an SRCALPHA surface: translucent fill and/or rim."""
    if fill is not None:
        pygame.draw.rect(surf, fill, rect, border_radius=radius)
    if border is not None and bw > 0:
        pygame.draw.rect(surf, border, rect, bw, border_radius=radius)


def _draw_text(surf, txt, x, y, color=PANEL_YELLOW, f=None):
    if f is None:
        f = _panel_font
    img = f.render(txt, True, color)
    surf.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


_fit_fonts = {}


def _fit_font(size):
    """Cached consolas fonts for INFO lines that need shrinking."""
    f = _fit_fonts.get(size)
    if f is None:
        f = pygame.font.SysFont("consolas", size)
        _fit_fonts[size] = f
    return f


def _draw_text_fit(surf, txt, x, y, right_edge, color=PANEL_WHITE, f=None):
    """Draw txt at (x, y) in the given face -- unless it would run past
    right_edge, in which case set it in the largest smaller size that
    fits, vertically centred on the normal text line. Lines that fit
    are drawn exactly as before."""
    if f is None:
        f = _panel_font
    img = f.render(txt, True, color)
    if x + img.get_width() <= right_edge:
        surf.blit(img, (x, y))
        return img.get_rect(topleft=(x, y))
    size = f.get_height()
    small = img
    while size > 10:
        size -= 2
        small = _fit_font(size).render(txt, True, color)
        if x + small.get_width() <= right_edge:
            break
    yy = y + max(0, (img.get_height() - small.get_height()) // 2)
    surf.blit(small, (x, yy))
    return small.get_rect(topleft=(x, yy))


def _draw_text_centered(surf, txt, rect, color=PANEL_YELLOW, f=None):
    if f is None:
        f = _panel_font
    img = f.render(txt, True, color)
    r = img.get_rect()
    x = rect.centerx - r.width // 2
    y = rect.centery - r.height // 2
    surf.blit(img, (x, y))
    return img.get_rect(topleft=(x, y))


def _draw_diag_shape(surf, x, y, on_color=PANEL_YELLOW, off_color=(0, 0, 0),
                     flip=False, w=None, h=None):
    if w is None or h is None:
        w, h = _panel_font.size("A")
    w2 = w // 2
    h2 = h // 2
    tl = pygame.Rect(x,      y,      w2, h2)
    tr = pygame.Rect(x + w2, y,      w - w2, h2)
    bl = pygame.Rect(x,      y + h2, w2, h - h2)
    br = pygame.Rect(x + w2, y + h2, w - w2, h - h2)
    if flip:
        # The same graphic mirrored -- alternating flip True/False makes
        # the diagonal "spin", just like the VZ-200 original.
        pygame.draw.rect(surf, off_color, tl)
        pygame.draw.rect(surf, on_color,  tr)
        pygame.draw.rect(surf, on_color,  bl)
        pygame.draw.rect(surf, off_color, br)
    else:
        pygame.draw.rect(surf, on_color,  tl)
        pygame.draw.rect(surf, off_color, tr)
        pygame.draw.rect(surf, off_color, bl)
        pygame.draw.rect(surf, on_color,  br)
def _draw_idle_cells(surf, box, n_cells):
    """A static row of the black/white diagonal cells, centred in a data
    box -- the VZ-200 'display asleep' graphic (v54). Same shape the
    spinning cells by START/F/F use, but nothing moves: every cell is
    drawn the same way round (flip off), exactly like the ALT window's
    standing graphics. Shown until the engines are started."""
    x0 = box.centerx - (n_cells * CELL_W) // 2
    y0 = box.centery - CELL_H // 2
    for i in range(n_cells):
        _draw_diag_shape(surf, x0 + i * CELL_W, y0,
                         PANEL_WHITE, (0, 0, 0), flip=False,
                         w=CELL_W, h=CELL_H)

def draw_attitude_indicator(surf, jet, rect):
    """Attitude Indicator (AI) — pygame port of the tkinter ADI gauge.
    Drawn inside *rect* with the prototype's own 4 cm x 10 cm layout:
    a black instrument face, the white bank scale on the black top
    band, sky and ground below, the black pitch ladder with degree
    labels, and the fixed white aircraft symbol. The horizon and the
    ladder ride with pitch; the needle rides with bank -- both read
    live from the jet."""
    x, y, w, h = rect
    cx = x + w // 2

    bank = max(-BANK_MAX, min(BANK_MAX, getattr(jet, 'bank', 0.0)))
    pitch = getattr(jet, 'pitch', 0.0)

    # Everything is placed in the tkinter prototype's 152 x 378 design
    # coordinates and scaled into the rect, so the port keeps the
    # prototype's exact proportions at any size.
    sx = w / 152.0
    sy = h / 378.0
    def X(v): return x + int(round(v * sx))
    def Y(v): return y + int(round(v * sy))

    BLACK  = (16, 16, 22)
    SKY    = (13, 168, 234)
    GROUND = (210, 140, 60)
    WHITE  = (255, 255, 255)

    # --- 1. Black instrument face ---
    pygame.draw.rect(surf, BLACK, rect)

    # --- 2. Sky and ground (the horizon rides with pitch) ---
    sky_top = Y(100)
    pitch_cy = Y(240)
    px_per_deg = 3.6 * sy
    horizon_y = max(sky_top, min(y + h, pitch_cy + int(pitch * px_per_deg)))
    if horizon_y > sky_top:
        pygame.draw.rect(surf, SKY, (x, sky_top, w, horizon_y - sky_top))
    if horizon_y < y + h:
        pygame.draw.rect(surf, GROUND, (x, horizon_y, w, y + h - horizon_y))
    pygame.draw.line(surf, BLACK, (x, horizon_y), (x + w, horizon_y),
                     max(2, int(round(3 * sy))))

    # --- 3. Pitch ladder (rides with the horizon) ---
    for deg in (25, 15, 5, -5, -15, -25):
        ly = horizon_y - int(deg * px_per_deg)
        if sky_top + 4 < ly < y + h - 4:
            pygame.draw.line(surf, BLACK, (X(66), ly), (X(86), ly),
                             max(1, int(round(1.5 * sy))))
    label_font = pygame.font.SysFont("consolas", max(8, int(round(11 * sx))), bold=True)
    for deg in (30, 20, 10, -10, -20, -30):
        ly = horizon_y - int(deg * px_per_deg)
        if sky_top + 4 < ly < y + h - 4:
            pygame.draw.line(surf, BLACK, (X(53), ly), (X(99), ly),
                             max(2, int(round(2 * sy))))
            txt = label_font.render("%d\u00b0" % abs(deg), True, BLACK)
            surf.blit(txt, txt.get_rect(center=(X(37), ly)))
            surf.blit(txt, txt.get_rect(center=(X(115), ly)))

    # --- 4. Bank scale on the black band: radial ticks and labels ---
    # 0-40 degrees each side (v40): ten-degree rests at 10, 20 and 30,
    # the last rest at 40 -- the 45 mark is gone, and 40 is the limit.
    # The scale is spread a little further round the semicircle: each
    # degree of bank draws BANK_VISUAL degrees round the arc, so the
    # outermost 40 rest sits sixty degrees off the top instead of forty.
    # Every label rides the one ring at radius 70 -- with the 45 gone
    # there is no fifth label to make room for.
    arc_cx, arc_cy = X(76), Y(82)
    tick_font = pygame.font.SysFont("arial", max(7, int(round(8 * sx))))
    tick_w = max(2, int(round(2 * sx)))
    for angle in (0, 10, 20, 30, 40, -10, -20, -30, -40):
        rad = math.radians(90 - angle * BANK_VISUAL)
        co, si = math.cos(rad), math.sin(rad)
        pygame.draw.line(surf, WHITE,
                         (arc_cx + 50 * sx * co, arc_cy - 50 * sy * si),
                         (arc_cx + 56 * sx * co, arc_cy - 56 * sy * si), tick_w)
        timg = tick_font.render(str(abs(angle)), True, WHITE)
        tr = timg.get_rect(center=(arc_cx + 70.0 * sx * co,
                                   arc_cy - 70.0 * sy * si))
        surf.blit(timg, tr)

    # --- 5. Bank needle with arrowhead ---
    # The needle reads the same spread scale as the rests (v40): bank
    # degrees times BANK_VISUAL round the arc, so at the forty-degree
    # limit it points straight at the outermost 40 rest.
    pivot_x, pivot_y = arc_cx, Y(78)
    needle_len = 52 * sy
    nrad = math.radians(90 - bank * BANK_VISUAL)
    end_x = pivot_x + needle_len * math.cos(nrad)
    end_y = pivot_y - needle_len * math.sin(nrad)
    pygame.draw.line(surf, WHITE, (pivot_x, pivot_y), (end_x, end_y), tick_w)
    asz = 5 * sx
    lr = math.radians(90 - bank * BANK_VISUAL - 135)
    rr = math.radians(90 - bank * BANK_VISUAL + 135)
    pygame.draw.polygon(surf, WHITE, [(end_x, end_y),
                                      (end_x + asz * math.cos(lr), end_y - asz * math.sin(lr)),
                                      (end_x + asz * math.cos(rr), end_y - asz * math.sin(rr))])

    # --- 6. Fixed aircraft symbol on the pitch centre ---
    wy = pitch_cy
    def PX(v): return cx + int(round(v * sx))
    def PY(v): return wy + int(round(v * sy))
    def P(pts): return [(PX(a), PY(b)) for a, b in pts]
    ow = max(1, int(round(1 * sx)))
    # Wings
    pygame.draw.polygon(surf, WHITE, P([(-34, -2), (-6, 0), (-6, 3), (-34, 1)]))
    pygame.draw.polygon(surf, BLACK, P([(-34, -2), (-6, 0), (-6, 3), (-34, 1)]), ow)
    pygame.draw.polygon(surf, WHITE, P([(6, 0), (34, -2), (34, 1), (6, 3)]))
    pygame.draw.polygon(surf, BLACK, P([(6, 0), (34, -2), (34, 1), (6, 3)]), ow)
    # Engine nacelles
    pygame.draw.ellipse(surf, WHITE, pygame.Rect(PX(-10), PY(-8), max(2, int(5 * sx)), max(2, int(6 * sy))))
    pygame.draw.ellipse(surf, WHITE, pygame.Rect(PX(5),  PY(-8), max(2, int(5 * sx)), max(2, int(6 * sy))))
    # Fuselage
    fus = pygame.Rect(PX(-6), PY(-5), max(2, int(12 * sx)), max(2, int(10 * sy)))
    pygame.draw.ellipse(surf, (0xdc, 0xdc, 0xdc), fus)
    pygame.draw.ellipse(surf, BLACK, fus, ow)
    # Tail post and fin
    pygame.draw.rect(surf, WHITE, pygame.Rect(PX(-1), PY(-14), max(1, int(2 * sx)), max(2, int(10 * sy))))
    pygame.draw.polygon(surf, WHITE, P([(-12, -16), (12, -16), (9, -13), (-9, -13)]))
    pygame.draw.polygon(surf, BLACK, P([(-12, -16), (12, -16), (9, -13), (-9, -13)]), ow)

def surface_wind_show(j, apt_name):
    """The surface wind SPEED shown at INFO for an airport (v68): a
    DISPLAY-ONLY figure. Each airport draws its own from the 10-30 range
    the first time the DME is tuned to it, then keeps it for the rest of
    the flight -- so the readout varies from field to field and from
    flight to flight, but never flickers frame to frame. FOR SHOW ONLY,
    as ordered: the flight model reads nothing of it (the only wind she
    feels is still wind_drift_dir's gentle heading wander). The dict
    lives on the jet so it travels with the save; a pre-v68 save simply
    draws its figures as they are first asked for."""
    show = getattr(j, "wind_show", None)
    if not isinstance(show, dict):
        show = j.wind_show = {}
    if apt_name not in show:
        show[apt_name] = random.randint(10, 30)
    return show[apt_name]


def _draw_strut_clock(s):
    """The working clock on the centre window strut (v95), seated exactly
    over the photograph's own frozen clock (v96) and wearing its livery:
    a near-black rim, an ivory dial, black ticks and black hands.

    Real local time -- the same wall clock as the Current Time readout in
    the ETA box -- with hour and minute hands and a sweeping second hand,
    redrawn every frame. It keeps on ticking while the sim is paused:
    the pause freezes the jet, not the world.
    """
    now = time.time()
    lt = time.localtime(now)
    sec = lt.tm_sec + (now - math.floor(now))
    minute = lt.tm_min + sec / 60.0
    hour = (lt.tm_hour % 12) + minute / 60.0
    cx, cy, r = STRUT_CLOCK_CX, STRUT_CLOCK_CY, STRUT_CLOCK_R

    ink = (18, 18, 22)          # the dial's black ink
    ivory = (170, 162, 150)     # the photographed dial's shaded ivory

    # Rim and dial, swallowing the photographed clock whole.
    pygame.draw.circle(s, (6, 6, 8), (cx, cy), r)
    pygame.draw.circle(s, ivory, (cx, cy), r - 7)

    # Hour ticks: long at 12/3/6/9, short otherwise.
    for i in range(12):
        a = math.radians(i * 30)
        big = (i % 3 == 0)
        r1 = r - (16 if big else 12)
        r2 = r - 9
        pygame.draw.line(s, ink,
                         (cx + r1 * math.sin(a), cy - r1 * math.cos(a)),
                         (cx + r2 * math.sin(a), cy - r2 * math.cos(a)),
                         3 if big else 2)

    # The hands, in the same black ink: hour and minute, then the thin
    # sweeping second hand with its little counterweight tail.
    def _hand(deg, length, w, tail=0):
        a = math.radians(deg)
        dx, dy = math.sin(a), -math.cos(a)
        pygame.draw.line(s, ink, (cx - tail * dx, cy - tail * dy),
                         (cx + length * dx, cy + length * dy), w)

    _hand(hour * 30.0, r - 22, 5)
    _hand(minute * 6.0, r - 13, 3)
    _hand(sec * 6.0, r - 11, 2, tail=8)

    # Centre pin.
    pygame.draw.circle(s, ink, (cx, cy), 3)
    pygame.draw.circle(s, ivory, (cx, cy), 1)


def draw_panel(surf, jet, WIDTH=PANEL_W, HEIGHT=PANEL_H, sh=1080, scale=1.0):
    """Draw the HUD over the stripped cockpit photograph (2160 x 1440)."""
    if _panel_font is None:
        _init_panel_fonts()

    font = _panel_font
    small_font = _panel_small_font

    altitude_ft = jet.alt
    ias_kts = jet.ias
    # IAS/MACH changeover (v38): faster than Mach 0.4, or above 18,000
    # ft, the IAS box reports the Mach number with a MACH badge; back
    # below both and the knots readout with its "K" returns.
    mach_now = mach_number(ias_kts, altitude_ft)
    mach_mode = mach_now > MACH_SHOW or altitude_ft > MACH_ALT_FT
    vsi_fpm = jet.vsi
    thrust_percent = jet.thrust
    fuel_kg = jet.fuel
    gear_down = jet.gear_down
    stall = (jet.ias < stall_speed(jet)) and jet.airborne
    # The wind on every field of the route blows straight down the course
    # line -- direction = route track + 180 -- so she always arrives (and
    # departs) heading right into it. The SPEED shown is a per-airport
    # show figure, picked up at the INFO line below where the tuned
    # airport is known (see surface_wind_show).
    wind_dir = (int(jet.route["hdg"]) + 180) % 360
    flap_pos = float(jet.flap)

    # DME channels, cycled with [C]:
    #   "-"        = distance to the END of the DESTINATION runway (To letter)
    #   "v0","v1"  = distance to the END of each ENROUTE airport's runway,
    #                in route order (one channel per enroute field)
    #   "+"        = distance flown from the ORIGIN (title From letter)
    # From 10,000 m before the tuned runway's threshold the readout
    # switches to metres, counting down to the end of the runway.
    orig_name, dest_name = jet.route["name"].split("-")
    pos = jet.route["dist"] - jet.dme
    if jet.dme_chan == "+":
        station_ltr = AIRPORT_LETTERS.get(orig_name, "?")
        dme_digits = f"{jet.dist_flown:.1f}"
        dme_unit = "NM"
    else:
        apt_name, apt_dist = dest_name, float(jet.route["dist"])
        if jet.dme_chan.startswith("v"):
            vias = route_vias(jet.route)
            vi = int(jet.dme_chan[1:]) if jet.dme_chan[1:].isdigit() else 0
            if 0 <= vi < len(vias):
                apt_name, apt_dist = vias[vi]["name"], vias[vi]["dist"]
        station_ltr = AIRPORT_LETTERS.get(apt_name, "?")
        d_end_nm = apt_dist - pos
        d_end_m = d_end_nm * M_PER_NM
        if 0.0 <= d_end_m <= APCH_METRES_M + RWY_M:
            dme_digits = "%d" % max(0, int(d_end_m))
            dme_unit = "M"
        else:
            dme_digits = f"{d_end_nm:.1f}" if d_end_nm > 0 else "---"
            dme_unit = "NM"
    ass_fl = jet.ass_fl
    itt = int(jet.itt)
    engines = jet.engines
    ap = jet.ap
    brakes = jet.brakes
    msg = jet.msg

    # ---------- BACKGROUND: the photograph, else the old dark glass ----------
    bg = _load_panel_bg()
    if bg is not None:
        surf.blit(bg, (0, 0))
    else:
        surf.fill(PANEL_GREEN)

    # Everything HUD-like draws onto one alpha overlay, so the translucent
    # blue glass can ghost the photograph through, then lands in one blit.
    ov = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    s = ov

    # Pre-compute character size
    char_w, char_h = font.size("A")

    # ---------- TOP STATUS ROW ----------
    # STALL / 1 / 2 / CAB PRESS: near-clear boxes with a thick blue rim,
    # tucked under the overhead panel between its two dome lights. The
    # labels wear their own smaller face (v94), so a thick margin of box
    # stands all round the letters.
    stall_rect = pygame.Rect(244, 252, 208, 88)
    box1       = pygame.Rect(724, 252, 148, 88)
    box2       = pygame.Rect(1276, 252, 152, 88)
    box3       = pygame.Rect(1576, 252, 300, 88)

    if stall:
        _rrect(s, stall_rect, fill=(220, 0, 0, 235), border=PANEL_YELLOW,
               bw=BORDER_THICK, radius=24)
        _draw_text_centered(s, "STALL", stall_rect, PANEL_WHITE,
                            _panel_top_font)
    else:
        # v107: the CAB PRESS near-clear glass, by the captain's order
        # (the v93 solid panel blue is retired).
        _rrect(s, stall_rect, fill=TOP_FILL, border=TOP_BORD,
               bw=BORDER_THICK, radius=24)
        _draw_text_centered(s, "STALL", stall_rect, PANEL_YELLOW,
                            _panel_top_font)

    # Engine 1 and 2 indicators
    eng1_active = engines and jet.n1 > 50
    eng2_active = engines and jet.n1 > 50
    for box, active, label in ((box1, eng1_active, "1"),
                               (box2, eng2_active, "2")):
        _rrect(s, box, fill=TOP_FILL,
               border=PANEL_YELLOW if active else TOP_BORD,
               bw=BORDER_THICK, radius=24)
        _draw_text_centered(s, label, box, PANEL_YELLOW, _panel_top_font)

    # CAB PRESS: normally a plain blue-rimmed box. While the warning
    # burns, its face FLASHES red (half-second cadence) until the jet is
    # below 10,000 ft.
    cab_flash = getattr(jet, "cab_light", False) \
                and (pygame.time.get_ticks() // 500) % 2 == 0
    _rrect(s, box3, fill=(220, 0, 0, 235) if cab_flash else TOP_FILL,
           border=TOP_BORD, bw=BORDER_THICK, radius=24)
    _draw_text_centered(s, "CAB PRESS", box3,
                        PANEL_WHITE if cab_flash else PANEL_YELLOW,
                        _panel_top_font)

    # ---------- SAVE / LOAD / PAUSE / DESKTOP BUTTONS (top-right) ----------
    # Clickable with the mouse, or [F5] to save and [F9] to load.
    btn_font = pygame.font.SysFont("consolas", 28, bold=True)
    btn_w, btn_h = 150, 48
    save_btn    = pygame.Rect(1896, 242, btn_w, btn_h)
    load_btn    = pygame.Rect(1896, 302, btn_w, btn_h)
    pause_btn   = pygame.Rect(1896, 364, btn_w, btn_h)
    desktop_btn = pygame.Rect(1896, 426, btn_w, btn_h)
    paused = getattr(jet, "paused", False)
    for rect, label in ((save_btn, "SAVE GAME"), (load_btn, "LOAD GAME"),
                        (pause_btn, "RESUME" if paused else "PAUSE")):
        face = PANEL_ORANGE if (rect is pause_btn and paused) else PANEL_YELLOW
        pygame.draw.rect(s, face, rect)
        pygame.draw.rect(s, PANEL_BLUE, rect, 4)
        _draw_text_centered(s, label, rect, PANEL_BLUE, btn_font)
    # The DESKTOP button draws on its own: while its offer is on the
    # table it flashes on the ABANDON placard's half-second cadence,
    # asking for the second, confirming click.
    if getattr(jet, "desktop_offer", False):
        flash = (pygame.time.get_ticks() // 500) % 2 == 0
        dk_face = PANEL_RED if flash else PANEL_ORANGE
        dk_text = PANEL_WHITE if flash else PANEL_BLUE
        pygame.draw.rect(s, dk_face, desktop_btn)
        pygame.draw.rect(s, PANEL_BLUE, desktop_btn, 4)
        _draw_text_centered(s, "DESKTOP?", desktop_btn, dk_text, btn_font)
    else:
        pygame.draw.rect(s, PANEL_YELLOW, desktop_btn)
        pygame.draw.rect(s, PANEL_BLUE, desktop_btn, 4)
        _draw_text_centered(s, "DESKTOP", desktop_btn, PANEL_BLUE, btn_font)
    PANEL_BUTTONS.clear()
    PANEL_BUTTONS["save"] = save_btn
    PANEL_BUTTONS["load"] = load_btn
    PANEL_BUTTONS["pause"] = pause_btn
    PANEL_BUTTONS["desktop"] = desktop_btn

    # [Z] ABANDON offer: while the first [Z] is on the table, a flashing
    # placard asks for the second [Z] -- and is itself clickable to
    # confirm. It sits on the DESKTOP row, immediately to the button's
    # left. Half-second cadence, like the CAB PRESS warning.
    if getattr(jet, "abandon_offer", False):
        abandon_btn = pygame.Rect(0, 0, btn_w, btn_h)
        abandon_btn.right = desktop_btn.left - 10
        abandon_btn.top = desktop_btn.top
        flash = (pygame.time.get_ticks() // 500) % 2 == 0
        ab_face = PANEL_RED if flash else PANEL_ORANGE
        ab_text = PANEL_WHITE if flash else PANEL_BLUE
        pygame.draw.rect(s, ab_face, abandon_btn)
        pygame.draw.rect(s, PANEL_BLUE, abandon_btn, 4)
        _draw_text_centered(s, "ABANDON? Z", abandon_btn, ab_text, btn_font)
        PANEL_BUTTONS["abandon"] = abandon_btn

    # ---------- HDG / OBS (near-clear glass, white rim -- v107) ----------
    hdg_readout = "%03d" % (int(jet.hdg) % 360)
    obs_readout = "%03d" % (int(getattr(jet, "obs", float(jet.route["hdg"]))) % 360)
    hdg_box = pygame.Rect(776, 362, 240, 72)
    obs_box = pygame.Rect(1128, 362, 240, 72)
    for box, part in ((hdg_box, "HDG " + hdg_readout + "\u00b0"),
                      (obs_box, "OBS " + obs_readout + "\u00b0")):
        _rrect(s, box, fill=TOP_FILL, border=(235, 242, 255, 220), bw=4,
               radius=20)
        _draw_text_centered(s, part, box, PANEL_YELLOW)

    # Flashing P A U S E D placard between the HDG/OBS line and the IAS row.
    if paused and (pygame.time.get_ticks() // 400) % 2 == 0:
        pz_img = font.render("P A U S E D", True, PANEL_ORANGE)
        pz_rect = pz_img.get_rect(center=(1080, 444))
        s.blit(pz_img, pz_rect)

    # ---------- MAIN ROW: IAS / ALT / ASS FL (near-clear glass -- v107) ----------
    label_font = _panel_cdi_font
    ias_box = pygame.Rect(152, 496, 344, 138)
    alt_box = pygame.Rect(502, 496, 352, 138)
    ass_box_outer = pygame.Rect(874, 496, 346, 138)

    def data_box(box, label):
        # v107: the CAB PRESS near-clear glass (the SKY_FILL blue glass
        # is retired)
        _rrect(s, box, fill=TOP_FILL, radius=24)
        inner = box.inflate(-12, -12)
        _rrect(s, inner, border=SKY_BORD, bw=4, radius=20)
        lab_img = label_font.render(label, True, PANEL_YELLOW)
        s.blit(lab_img, (box.centerx - lab_img.get_width() // 2,
                         box.top - lab_img.get_height() - 4))

    data_box(ias_box, "IAS")
    data_box(alt_box, "ALT")
    data_box(ass_box_outer, "ASS FL")

    # ---------- IAS ----------
    # In Mach mode the readout reports the Mach number ("0.57") and the
    # unit badge reads MACH in a smaller face; otherwise the familiar
    # three-figure knots with its "K".
    if mach_mode:
        ias_str = "%0.2f" % mach_now
        unit_txt, unit_f = "MACH", small_font
    else:
        ias_str = f"{int(ias_kts):03d}"
        unit_txt, unit_f = "K", font
    num_img = font.render(ias_str, True, PANEL_WHITE)
    num_rect = num_img.get_rect()
    num_rect.centery = ias_box.centery
    num_rect.centerx = ias_box.centerx - 20
    s.blit(num_img, num_rect.topleft)

    k_img = unit_f.render(unit_txt, True, PANEL_BLUE)
    k_rect = k_img.get_rect()
    k_rect.midleft = (num_rect.right + 16, num_rect.centery)
    k_bg = pygame.Rect(k_rect.x - 4, k_rect.y - 4, k_rect.width + 8, k_rect.height + 8)
    pygame.draw.rect(s, PANEL_YELLOW, k_bg, border_radius=8)
    s.blit(k_img, k_rect.topleft)

    # ---------- ALT ----------
    alt_int = int(altitude_ft)
    thousands = alt_int // 1000
    remainder = alt_int % 1000

    # Below 1,000 ft: keep the two black/white graphics. At/above 1,000
    # ft: replace them with the thousands number (no leading zero) and
    # show only the last three digits after the comma. Dropping below
    # 1,000 restores the graphics automatically through this same branch.
    if thousands > 0:
        lead_text = str(thousands)
        alt_str = f"{remainder:03d}"
    else:
        lead_text = ""
        alt_str = f"{alt_int:03d}"

    lead_img = font.render(lead_text, True, PANEL_WHITE) if lead_text else None
    num_alt_img = font.render(alt_str, True, PANEL_WHITE)
    ft_img = font.render("FT", True, PANEL_BLUE)
    comma_img = font.render(",", True, PANEL_WHITE)

    lead_w = 2 * CELL_W
    digits_w = num_alt_img.get_width()
    comma_w = comma_img.get_width()
    ft_w = ft_img.get_width() + 8

    gap_diag_comma = 2    # the comma already owns a full monospace cell
    gap_comma_digits = 4
    gap_digits_ft = 12

    total_w = (lead_w + gap_diag_comma + comma_w + gap_comma_digits
               + digits_w + gap_digits_ft + ft_w)

    start_x = alt_box.centerx - total_w // 2
    center_y = alt_box.centery
    cell_top = center_y - CELL_H // 2

    x_lead = start_x
    x_comma = x_lead + lead_w + gap_diag_comma
    x_digits = x_comma + comma_w + gap_comma_digits
    x_ft_bg = x_digits + digits_w + gap_digits_ft

    if lead_img is not None:
        lead_rect = lead_img.get_rect()
        lead_rect.midright = (x_lead + lead_w, center_y)
        s.blit(lead_img, lead_rect.topleft)
    else:
        _draw_diag_shape(s, x_lead, cell_top, on_color=PANEL_WHITE, off_color=(0, 0, 0),
                         w=CELL_W, h=CELL_H)
        _draw_diag_shape(s, x_lead + CELL_W, cell_top, on_color=PANEL_WHITE, off_color=(0, 0, 0),
                         w=CELL_W, h=CELL_H)

    comma_rect = comma_img.get_rect()
    comma_rect.midleft = (x_comma, center_y)
    s.blit(comma_img, comma_rect.topleft)

    num_alt_rect = num_alt_img.get_rect()
    num_alt_rect.midleft = (x_digits, center_y)
    s.blit(num_alt_img, num_alt_rect.topleft)

    ft_rect = ft_img.get_rect()
    ft_rect.midleft = (x_ft_bg + 4, center_y)
    ft_bg = pygame.Rect(x_ft_bg, ft_rect.top - 4, ft_img.get_width() + 8,
                        ft_img.get_height() + 8)
    pygame.draw.rect(s, PANEL_YELLOW, ft_bg, border_radius=8)
    s.blit(ft_img, ft_rect.topleft)

    # ---------- ASS FL ----------
    a_img = font.render("A", True, PANEL_BLUE)
    ass_num_str = f"{ass_fl:03d}" if ass_fl > 0 else "000"
    num_ass_img = font.render(ass_num_str, True, PANEL_WHITE)

    a_rect = a_img.get_rect()
    num_ass_rect = num_ass_img.get_rect()

    total_width = a_rect.width + 8 + num_ass_rect.width
    center_x = ass_box_outer.centerx
    center_y = ass_box_outer.centery

    a_rect.x = center_x - total_width // 2
    a_rect.y = center_y - a_rect.height // 2

    num_ass_rect.x = a_rect.right + 8
    num_ass_rect.y = center_y - num_ass_rect.height // 2

    a_bg = pygame.Rect(a_rect.x - 4, a_rect.y - 4, a_rect.width + 8, a_rect.height + 8)
    pygame.draw.rect(s, PANEL_YELLOW, a_bg, border_radius=8)
    s.blit(a_img, a_rect.topleft)
    s.blit(num_ass_img, num_ass_rect.topleft)

    # ---------- BR band ----------
    # The yellow ON/OFF box stands BETWEEN two detached red guard bars,
    # a dark gap either side -- the AUTO PILOT flag's own v93 style
    # turned upright, exactly as the photograph shows. ON while the
    # brakes hold, OFF once they release.
    br_label_img = label_font.render("BR", True, PANEL_YELLOW)
    s.blit(br_label_img, (1590 - br_label_img.get_width() // 2, 482))
    br_bar_t = pygame.Rect(1538, 534, 124, 20)
    br_band  = pygame.Rect(1538, 560, 124, 62)
    br_bar_b = pygame.Rect(1538, 628, 124, 20)
    pygame.draw.rect(s, PANEL_RED, br_bar_t)
    pygame.draw.rect(s, PANEL_YELLOW, br_band)
    pygame.draw.rect(s, PANEL_RED, br_bar_b)
    br_status = "ON" if brakes else "OFF"
    _draw_text_centered(s, br_status, br_band, PANEL_BLUE)

    # ---------- ITT ----------
    _draw_text(s, "ITT", 1780, 470, PANEL_YELLOW, label_font)
    eng_box_w, eng_box_h = 38, 50
    eng1_rect = pygame.Rect(1776, 524, eng_box_w, eng_box_h)
    pygame.draw.rect(s, PANEL_YELLOW, eng1_rect)
    pygame.draw.rect(s, PANEL_BLUE, eng1_rect, 4)
    _draw_text_centered(s, "1", eng1_rect, PANEL_GREEN, small_font)
    itt1_box = pygame.Rect(eng1_rect.right + 16, eng1_rect.y, 150, eng_box_h)
    itt1_str = f"{itt:04d}"
    _draw_text_centered(s, itt1_str, itt1_box, PANEL_WHITE)

    # Engine 2 runs a steady couple of degrees hotter than her twin,
    # all the way up the dial (v102). The old x0.95+50 put the split
    # mostly in the +50, so a COLD engine 2 read 64 degC against her
    # twin's ambient 15 -- the "0015 / 0064" on the parked panel.
    itt2 = int(jet.itt) + 2
    eng2_rect = pygame.Rect(1776, 598, eng_box_w, eng_box_h)
    pygame.draw.rect(s, PANEL_YELLOW, eng2_rect)
    pygame.draw.rect(s, PANEL_BLUE, eng2_rect, 4)
    _draw_text_centered(s, "2", eng2_rect, PANEL_GREEN, small_font)
    itt2_box = pygame.Rect(eng2_rect.right + 16, eng2_rect.y, 150, eng_box_h)
    itt2_str = f"{itt2:04d}"
    _draw_text_centered(s, itt2_str, itt2_box, PANEL_WHITE)

    # ---------- DME(-) / GROUND SPEED / ETA ROW (near-clear glass -- v107) ----------
    dme_box = pygame.Rect(154, 760, 314, 140)
    gs_box  = pygame.Rect(502, 760, 352, 140)
    eta_box = pygame.Rect(890, 760, 310, 140)

    # DME(-): the bracket shows the tuned airport's ID letter: DME(M)
    # destination, DME(U) enroute, DME(S) origin.
    dme_label = "DME(%s)" % station_ltr
    data_box(dme_box, dme_label)

    dme_digits_img = font.render(dme_digits, True, PANEL_WHITE)
    digits_rect = dme_digits_img.get_rect()
    digits_rect.centery = dme_box.centery
    digits_rect.centerx = dme_box.centerx - 24
    s.blit(dme_digits_img, digits_rect.topleft)

    # Unit badge in the same style as the IAS "K": yellow backing, blue
    # letters. DME is a distance, so the badge is NM (or M once the
    # readout has switched to metres inside the last 12,000 m).
    dme_unit_img = font.render(dme_unit, True, PANEL_BLUE)
    dme_unit_rect = dme_unit_img.get_rect()
    dme_unit_rect.midleft = (digits_rect.right + 16, digits_rect.centery)
    dme_unit_bg = pygame.Rect(dme_unit_rect.x - 4, dme_unit_rect.y - 4,
                              dme_unit_rect.width + 8, dme_unit_rect.height + 8)
    pygame.draw.rect(s, PANEL_YELLOW, dme_unit_bg, border_radius=8)
    s.blit(dme_unit_img, dme_unit_rect.topleft)

    # G/S register: the current ground speed in knots (no wind is
    # modelled, so ground speed equals airspeed). Spelled out in full so
    # it can't be confused with the G/S glideslope tape lower down.
    # Asleep until the engines are started -- a static row of the
    # black/white diagonal cells; [E] swaps the cells for the readout.
    data_box(gs_box, "GROUND SPEED")
    if not engines:
        _draw_idle_cells(s, gs_box, 4)
    else:
        gs_num_str = "%03d" % int(round(ias_kts))
        gs_num_img = font.render(gs_num_str, True, PANEL_WHITE)
        gs_num_rect = gs_num_img.get_rect()
        gs_num_rect.centery = gs_box.centery
        gs_num_rect.centerx = gs_box.centerx - 20
        s.blit(gs_num_img, gs_num_rect.topleft)

        k_img = font.render("K", True, PANEL_BLUE)
        k_rect = k_img.get_rect()
        k_rect.midleft = (gs_num_rect.right + 16, gs_num_rect.centery)
        k_bg = pygame.Rect(k_rect.x - 4, k_rect.y - 4, k_rect.width + 8, k_rect.height + 8)
        pygame.draw.rect(s, PANEL_YELLOW, k_bg, border_radius=8)
        s.blit(k_img, k_rect.topleft)

    # ETA: asleep until the engines are started -- the same static
    # black/white diagonal cells as the G/S register. [E] swaps the cells
    # for the ETA, the MIN badge and the shadowy real countdown.
    data_box(eta_box, "ETA")
    if not engines:
        _draw_idle_cells(s, eta_box, 6)
    else:
        # The estimate follows the airport the DME is tuned to (apt_dist
        # was resolved by the DME block above): the time to the
        # destination on "-", and to each enroute field on "v0","v1" ...
        # Any airport already passed reads "--:--" -- just as the DME
        # itself reads "---" -- so the "+" origin channel, which only
        # ever looks back, always shows "--:--".
        # On a REAL TIME leg the sim minute IS the wall-clock minute, so
        # the white ETA and the shadowy countdown beneath it tell ONE
        # time: both are driven by the countdown's own figure -- the
        # tuned field's measured sim-minute budget less the time this leg
        # has run -- the white reading minutes:seconds, the dim-amber line
        # the same duration in hours:minutes:seconds. The twelve
        # compressed legs are untouched: there the ETA stays distance
        # over speed in sim minutes and the countdown the plan remaining
        # in real ones -- two different times by design.
        # THE LIVE ETA: once she is airborne (or rolling out) the white
        # ETA is the ghost flight's figure -- the sim's own physics
        # fast-forwarded from her present state to the tuned runway, in
        # sim seconds (eta_predict_s). It answers to every setting that
        # moves the ship -- distance, flight level, airspeed, flap, gear,
        # brakes, fuel, the heading off the course line -- and with the
        # AUTOLAND committed it is the autoland's own plan, exact to the
        # second on final. remain_s carries the same duration in REAL
        # seconds for the dim-amber countdown (the leg's own clock
        # converts), so the 1:1 legs still tell one time and the
        # compressed legs keep their sim/real split. A live clock never
        # runs "late": the minus sign belongs to the ground phase, where
        # the box keeps its old manners -- the planned leg budget
        # counting down from brake release.
        real_time_leg = getattr(jet, "time_scale", TIME_SCALE) == 1.0
        tscale = max(0.1, getattr(jet, "time_scale", TIME_SCALE))
        live_s = eta_live_s(jet)

        if live_s is not None or jet.airborne or jet.rollout:
            overtime = False
            if live_s is None:
                # No arrival to predict -- the tuned field is behind her,
                # she is pointed away from it, or the glide cannot make it.
                eta_num_str = "--:--"
                remain_s = None
            else:
                eta_num_str = "%d:%02d" % (int(live_s // 60.0),
                                           int(live_s % 60.0))
                remain_s = live_s / tscale
        else:
            # On the ground: the countdown's budget -- the measured
            # sim-minutes the leg to the TUNED airport genuinely takes:
            # the destination on "-", each enroute field on "v0","v1"
            # (every one timed on the model, just as the route legs
            # were). Worked out ahead of the white readout, because on a
            # real-time leg the white readout is driven by it.
            budget_min = None
            if jet.dme_chan == "-":
                budget_min = float(jet.route.get("sim_min",
                                   10.0 + 0.20 * float(jet.route["dist"])))
            elif jet.dme_chan.startswith("v"):
                vias = route_vias(jet.route)
                vi = int(jet.dme_chan[1:]) if jet.dme_chan[1:].isdigit() else 0
                if 0 <= vi < len(vias):
                    via_mins = jet.route.get("via_sim_min", [])
                    budget_min = (float(via_mins[vi]) if vi < len(via_mins)
                                  else 10.0 + 0.20 * float(vias[vi]["dist"]))
            if budget_min is not None and apt_dist - pos <= 0.0:
                budget_min = None       # that field is already behind her
            if budget_min is None:
                remain_s = None         # a field behind her, or the "+" channel
                overtime = False
            else:
                # The countdown runs on the CURRENT leg, not the whole
                # flight -- the tuned airport's budget less the field
                # this leg started from, against the leg's own clock
                # (both re-armed at every intermediate stopover; both
                # zero from the origin, so a non-stop flight reads
                # exactly as it always has).
                leg_base = getattr(jet, "leg_base_min", 0.0)
                leg_t0 = getattr(jet, "leg_elapsed0", 0.0)
                remain_s = ((budget_min - leg_base) * 60.0
                            - (jet.elapsed - leg_t0)) / tscale
                overtime = remain_s < 0.0

            if jet.dme_chan == "+":
                eta_num_str = "--:--"
            elif real_time_leg:
                # On a real-time leg the white ETA states the countdown's
                # own figure in minutes:seconds -- the very duration the
                # dim-amber line below states in hours:minutes:seconds,
                # minus sign included when the flight runs late.
                if remain_s is None:
                    eta_num_str = "--:--"
                else:
                    _eta_s = abs(remain_s)
                    eta_num_str = "%d:%02d" % (int(_eta_s // 60.0),
                                               int(_eta_s % 60.0))
                    if overtime:
                        eta_num_str = "-" + eta_num_str
            else:
                d_go_nm = apt_dist - pos
                if jet.ias >= 40.0 and d_go_nm > 0.0:
                    mins = d_go_nm / jet.ias * 60.0
                    eta_num_str = "%d:%02d" % (int(mins), int((mins % 1.0) * 60.0))
                else:
                    eta_num_str = "--:--"
        eta_num_img = font.render(eta_num_str, True, PANEL_WHITE)
        eta_num_rect = eta_num_img.get_rect()
        eta_num_rect.centery = eta_box.centery
        eta_num_rect.centerx = eta_box.centerx - 40

        min_img = font.render("MIN", True, PANEL_BLUE)
        min_rect = min_img.get_rect()
        min_rect.midleft = (eta_num_rect.right + 16, eta_num_rect.centery)
        min_bg = pygame.Rect(min_rect.x - 4, min_rect.y - 4, min_rect.width + 8, min_rect.height + 8)
        # v124: THE TOP BAND. The photo's vivid blue appears ONLY
        # directly behind the top message -- from just left of the ETA
        # figures to just right of the MIN badge, and only the thickness
        # of the line itself. The rest of the box is clear glass again.
        # v127: the band now hugs the ETA FIGURES alone, ending before
        # the MIN badge -- the captain found the blue running through
        # the word MIN and slightly beyond it, and ordered it out: the
        # yellow badge sits on the bare glass, as the bottom line's
        # readouts have since v125. Same line thickness, same padding.
        # v128: and one step further -- the band is retired outright.
        # The big white ETA itself (the HH:MM reading, or the --:--
        # of no estimate) still wore the vivid blue; the figures now
        # read on the bare glass like everything else on the line.
        s.blit(eta_num_img, eta_num_rect.topleft)
        pygame.draw.rect(s, PANEL_YELLOW, min_bg, border_radius=8)
        s.blit(min_img, min_rect.topleft)

        # The REAL countdown: INSIDE the ETA box, along its bottom edge,
        # in the dim amber -- a vague, shadowy clock you barely
        # notice. It counts DOWN the real minutes the flight still needs,
        # converted from sim time by the compression. Pauses freeze it
        # with the world, a loaded save resumes it honestly, touchdown
        # parks it at the spare minutes -- and a flight that runs long
        # quietly counts past zero. It follows the DME channel [C],
        # exactly like the ETA above it; on a real-time leg the white ETA
        # reads this same remain_s figure, so the two clocks agree for
        # the whole flight (and in overtime both carry the minus sign).
        if remain_s is None:
            real_str = "--:--"
        else:
            _cd_s = abs(remain_s)
            # KARRATHA-PERTH counts down in hours:minutes only -- the
            # seconds are deleted on the long haul. Every other leg keeps
            # its seconds.
            if jet.route.get("name") == "KARRATHA-PERTH":
                real_str = "%d:%02d" % (int(_cd_s // 3600.0),
                                        int((_cd_s % 3600.0) // 60.0))
            elif _cd_s >= 3600.0:
                real_str = "%d:%02d:%02d" % (int(_cd_s // 3600.0),
                                             int((_cd_s % 3600.0) // 60.0),
                                             int(_cd_s % 60.0))
            else:
                real_str = "%d:%02d" % (int(_cd_s // 60.0), int(_cd_s % 60.0))
            if overtime:
                real_str = "-" + real_str
        # v116: THE BADGE SEATS. Each little readout sits on a NAVY
        # pill -- the key ribbon's own recipe in miniature: a dark blue
        # band with light writing. The v44 shy blue reads on it exactly
        # as it did on the pre-v88 dark blue glass, and no patch of
        # photograph -- dark corner or bright glare -- can swallow it,
        # because the seat IS the background. (v112's PALE frost seat
        # washed its ink out light-on-light; navy seats make light ink
        # glow.) One knob: ETA_INFO_SEAT -- alpha 0 parks the seats,
        # back to bare glass.
        def _eta_seat(rect):
            if ETA_INFO_SEAT[3]:
                _rrect(s, rect.inflate(12, 8), fill=ETA_INFO_SEAT, radius=8)

        # v114/v115: THE DIMMER. The six shadowy readouts all blit
        # through here. v114 dimmed the text ALPHA (the shy amber) --
        # but at screen scale the faint tiny strokes vanished entirely,
        # so v115 parks ETA_INFO_DIM at 255 and lets the half-
        # intensity yellow INK do the dimming. The helper stays: one
        # line fades all six if a bright ink ever needs it.
        def _eta_blit(img, pos):
            if ETA_INFO_DIM < 255:
                img.set_alpha(ETA_INFO_DIM)
            s.blit(img, pos)

        real_img = _panel_tiny_font.render(real_str, True, ETA_INFO_INK)
        real_rect = real_img.get_rect()
        # The countdown anchors at the box's left inner edge now, under
        # its own "Real Time" label, opening the middle of the bottom
        # line so the FLIGHT HOURS figures can sit between the two clocks
        # at the clocks' own size. v129: the line rides 3 px lower
        # (bottom - 13), so its INK centres on the full-width band and
        # the band's top edge clears the MIN badge above by 2 px.
        real_rect.left = eta_box.left + 16
        real_rect.bottom = eta_box.bottom - 13

        # The wall clock: the current time of day in 24-hour HH:MM, in
        # the countdown's own style -- the same tiny face and the same
        # shadowy amber -- on the very same line, against the right
        # edge of the box. The countdown shows how long is left; this
        # shows what time it is. (Worked out up here since v125, so
        # the split bottom band can seat both end messages before a
        # single letter of ink goes down.)
        now_img = _panel_tiny_font.render(time.strftime("%H:%M"),
                                          True, ETA_INFO_INK)
        now_rect = now_img.get_rect()
        now_rect.right = eta_box.right - 16
        now_rect.bottom = eta_box.bottom - 13

        # v125: THE BOTTOM BAND, SPLIT IN TWO. The captain found blue
        # still sitting behind the hours and minutes and ordered it
        # out: the vivid band now hugs the two END messages only --
        # one pill behind the countdown at the left edge, one behind
        # the wall clock at the right, each the thickness of its own
        # line. The FLIGHT HOURS figures between them -- the hours
        # and minutes themselves -- sit on clear glass now, and so
        # does every gap. The little captions above keep their place
        # on the clear glass, as the photo shows. v127: and the wall
        # clock's pill follows them off the blue -- the captain found
        # the vivid band under the HH:MM and ordered it out; the clock
        # now sits on the bare glass, and only the countdown at the
        # left edge keeps its pill. v129: THE FULL-WIDTH BAND. The
        # captain's re-think: the vivid blue returns as ONE band
        # spanning the ENTIRE bottom of the box, with all three
        # readouts on it in the paler blue. The band hugs the line's
        # INK (the tight bounding rects) by 4 px top and bottom, and
        # fits 2 px inside the inner white rim on every side -- the rim's
        # inner edge stands 10 px in from the box (the 6 px inset plus
        # its 4 px stroke), so the 12 px inset and the bottom - 12
        # clamp keep the blue off the white ALWAYS, corners rounded
        # inside the rim's own. Up top the band never closes nearer
        # than 2 px below the MIN badge. (The flight-hours figures are
        # worked out first now, so the band can measure all three
        # messages' ink before a drop of blue goes down.)
        fl_s = career_hours_now(jet)
        fl_nums = "%d h: %02d m" % (int(fl_s // 3600.0),
                                    int((fl_s % 3600.0) // 60.0))
        fh_gap_l = real_rect.right + 4
        fh_gap_r = now_rect.left - 4
        fh_font = _panel_cap_font            # last resort, cannot miss
        for _f in (_panel_tiny_font, _panel_fh_font, _panel_cap_font):
            if _f.size(fl_nums)[0] <= fh_gap_r - fh_gap_l:
                fh_font = _f
                break
        fh_img = fh_font.render(fl_nums, True, ETA_INFO_INK)
        fh_rect = fh_img.get_rect()
        fh_rect.centerx = (fh_gap_l + fh_gap_r) // 2
        fh_rect.bottom = eta_box.bottom - 13

        _bot_parts = ((real_img, real_rect), (fh_img, fh_rect),
                      (now_img, now_rect))
        _bt = max(min(r.top + i.get_bounding_rect().top
                      for i, r in _bot_parts) - 4,
                  min_bg.bottom + 2)
        _bb = min(max(r.top + i.get_bounding_rect().bottom
                      for i, r in _bot_parts) + 4,
                  eta_box.bottom - 12)
        band_bot = pygame.Rect(eta_box.left + 12, _bt,
                               eta_box.width - 24, _bb - _bt)
        pygame.draw.rect(s, ETA_BOX_BLUE, band_bot, border_radius=8)
        _eta_seat(real_rect)
        _eta_blit(real_img, real_rect.topleft)
        _eta_seat(fh_rect)
        _eta_blit(fh_img, fh_rect.topleft)
        _eta_seat(now_rect)
        _eta_blit(now_img, now_rect.topleft)

        # The three labels, always above their outputs. "Real Time" takes
        # the countdown's left edge, "Current Time" the wall clock's
        # right edge, and "Flight Hours" centres over its figures, nudged
        # only if it would touch a neighbour.
        rt_lab = _panel_cap_font.render("Real Time", True, ETA_INFO_INK)
        rt_rect = rt_lab.get_rect()
        rt_rect.left = eta_box.left + 16
        rt_rect.top = eta_box.top + 16
        ct_lab = _panel_cap_font.render("Current Time", True, ETA_INFO_INK)
        ct_rect = ct_lab.get_rect()
        ct_rect.right = eta_box.right - 16
        ct_rect.top = eta_box.top + 16
        fh_lab = _panel_cap_font.render("Flight Hours", True, ETA_INFO_INK)
        fh_lab_rect = fh_lab.get_rect()
        fh_lab_rect.centerx = fh_rect.centerx
        fh_lab_rect.top = eta_box.top + 16
        if fh_lab_rect.left < rt_rect.right + 6:
            fh_lab_rect.left = rt_rect.right + 6
        if fh_lab_rect.right > ct_rect.left - 6:
            fh_lab_rect.right = ct_rect.left - 6
        # v129: THE TOP BAND, arranged like the bottom's -- one vivid
        # band spanning the ENTIRE top of the box behind all three
        # captions, hugging their ink by 4 px and fitted 2 px inside
        # the inner white rim on every side (the top + 12 clamp keeps
        # it off the white ALWAYS); well clear of the big ETA line
        # below.
        _cap_parts = ((rt_lab, rt_rect), (fh_lab, fh_lab_rect),
                      (ct_lab, ct_rect))
        _ct = max(min(r.top + i.get_bounding_rect().top
                      for i, r in _cap_parts) - 4,
                  eta_box.top + 12)
        _cb = max(r.top + i.get_bounding_rect().bottom
                  for i, r in _cap_parts) + 4
        band_caps = pygame.Rect(eta_box.left + 12, _ct,
                                eta_box.width - 24, _cb - _ct)
        pygame.draw.rect(s, ETA_BOX_BLUE, band_caps, border_radius=8)
        _eta_seat(rt_rect)
        _eta_seat(fh_lab_rect)
        _eta_seat(ct_rect)
        _eta_blit(rt_lab, rt_rect.topleft)
        _eta_blit(fh_lab, fh_lab_rect.topleft)
        _eta_blit(ct_lab, ct_rect.topleft)

    # ---------- ATTITUDE INDICATOR ----------
    # The gauge itself renders into its own little surface so the whole
    # instrument can ghost the photograph through at one steady alpha.
    # v107: the nameplate and the gauge ride ONE ROW up -- the register's
    # own 48 px row pitch -- by the captain's order; the gauge's top now
    # sits level with the THRUST title. (The nameplate seats itself off
    # ai_rect.top, so it rides up with the gauge.)
    ai_rect = pygame.Rect(1234, 718 - 48, 194, 452)
    ai_surf = pygame.Surface((ai_rect.width, ai_rect.height), pygame.SRCALPHA)
    draw_attitude_indicator(ai_surf, jet, ai_surf.get_rect())
    ai_surf.set_alpha(AI_ALPHA)
    s.blit(ai_surf, ai_rect.topleft)

    # The nameplate: the title "ATT IND" balanced across the top of the
    # instrument, letter-spaced so the word spans a touch WIDER than the
    # gauge -- a small overlap on either side.
    att_txt = "ATT IND"
    att_overlap = max(2, ai_rect.width // 14)   # the small overlap each side
    att_chars = [font.render(ch, True, PANEL_YELLOW) for ch in att_txt]
    att_adv = [max(1, font.size(ch)[0]) for ch in att_txt]
    att_span = ai_rect.width + 2 * att_overlap
    att_gap = max(0, int(round((att_span - sum(att_adv))
                               / (len(att_txt) - 1))))
    att_x = ai_rect.centerx - (sum(att_adv) + att_gap * (len(att_txt) - 1)) // 2
    att_y = ai_rect.top - 12 - max(c.get_height() for c in att_chars)
    for ch_img, adv in zip(att_chars, att_adv):
        s.blit(ch_img, (att_x, att_y))
        att_x += adv + att_gap

    # ---------- G/S GLIDESLOPE DEVIATION TAPE ----------
    # A vertical yellow tape in the same style as the flap gauge; its
    # centre notch is exactly on the glideslope. The thin white line is
    # always on it: parked at the bottom until the glideslope comes alive
    # on approach, then it rides the tape -- above the notch = HIGH, on
    # it = on the glideslope, below it = LOW. The ride is ANGULAR: a
    # degree off the beam for full scale, so the marker tells the truth
    # from a hundred miles out down to the last mile.
    gs_cx = 1514
    gs_g_w = 38
    _draw_text(s, "G/S", gs_cx - label_font.size("G/S")[0] // 2, 700,
               PANEL_YELLOW, label_font)
    track = pygame.Rect(gs_cx - gs_g_w // 2, 766, gs_g_w, 352)
    pygame.draw.rect(s, PANEL_YELLOW, track)
    # Centre notch = exactly on the glideslope
    notch = pygame.Rect(track.x - 10, track.centery - 3, gs_g_w + 20, 6)
    pygame.draw.rect(s, PANEL_BLUE, notch)
    gs_frac = getattr(jet, "gs_frac", None)
    if gs_frac is None:
        frac = -1.0             # parked at the bottom until the G/S wakes
    else:
        frac = max(-1.0, min(1.0, float(gs_frac)))
    mk = pygame.Rect(0, 0, gs_g_w + 40, 8)
    mk.centerx = gs_cx
    mk.centery = track.centery - int(frac * (track.height // 2))
    pygame.draw.rect(s, PANEL_WHITE, mk)

    # ---------- FLAP ----------
    # The yellow vertical bar carries the settings 0-50 down its length;
    # the blue star sits opposite the selected one.
    flap_center_x = 1605
    flap_label = "FLAP"
    flw = label_font.size(flap_label)[0]
    _draw_text(s, flap_label, 1632 - flw // 2, 700, PANEL_YELLOW, label_font)
    flap_track = pygame.Rect(1580, 766, 50, 352)
    pygame.draw.rect(s, PANEL_YELLOW, flap_track)

    ticks = [0, 10, 20, 30, 40, 50]
    tick_step = 60
    tick_top = 790
    tick_font = font
    for i, t in enumerate(ticks):
        y = tick_top + i * tick_step
        num_img = tick_font.render(str(t), True, PANEL_YELLOW)
        num_rect = num_img.get_rect()
        num_rect.centerx = 1669
        num_rect.centery = y
        s.blit(num_img, num_rect.topleft)

    fp = max(0.0, min(50.0, flap_pos))
    rel = fp / 50.0
    star_y = tick_top + int(rel * (len(ticks) - 1) * tick_step)

    # The marker is an ORANGE square on the bar opposite the selected
    # setting, the blue asterisk centred in the middle of the square
    # (centred by its INK, so the star sits truly central). At the 0 and
    # 50 gates the square clamps flush to the bar's own ends.
    sq = pygame.Rect(0, 0, flap_track.width, 64)
    sq.centerx = flap_track.centerx
    sq.centery = star_y
    if sq.top < flap_track.top:
        sq.top = flap_track.top
    if sq.bottom > flap_track.bottom:
        sq.bottom = flap_track.bottom
    pygame.draw.rect(s, PANEL_ORANGE, sq)
    star_img = font.render("*", True, (30, 60, 235))
    star_ink = star_img.get_bounding_rect()
    s.blit(star_img, (sq.centerx - star_ink.centerx,
                      sq.centery - star_ink.centery))

    # ---------- THRUST ----------
    thr_label_x = 1858 - font.size("THRUST")[0] // 2
    _draw_text(s, "THRUST", thr_label_x, 670, PANEL_YELLOW)
    # The down stroke of the label's last T: the right-hand purple
    # bar's left edge lines up with it (v100).
    thr_stem_x = thr_label_x + font.size("THRUS")[0] + font.size("T")[0] // 2

    # PURPLE BARS -- the thrust gauge's two tracks, their tops flush
    # with the crown of the 100% mark, the right-hand bar's left edge
    # falling on the last T's down stroke, as the photograph shows.
    # v105: the bars now END at the foot of the 0% mark -- NO purple
    # below the scale's bottom line, either side, by the captain's
    # order (the bottoms are set once the 0% mark is laid out below).
    left_bar_rect  = pygame.Rect(1754, 726, 46, 224)
    right_bar_rect = pygame.Rect(thr_stem_x, 726, 44, 224)

    # The fixed "100%" and "0%" SCALE marks (v103): every output figure
    # on the gauge reads WHITE now, the fixed marks included, by the
    # captain's order -- v102's small yellow legends are retired. The
    # "100%" mark's INK top stays flush with the tops of the two bars
    # (v100 -- get_bounding_rect finds the crown however much ascent
    # padding the font adds above the digits).
    pct_img = font.render("100%", True, PANEL_WHITE)
    pct_ink = pct_img.get_bounding_rect()
    pct_rect = pct_img.get_rect(topleft=(1810, left_bar_rect.top - pct_ink.top))
    s.blit(pct_img, pct_rect.topleft)

    # The fixed "0%" mark, RIGHT-aligned on the "100%" mark's own right
    # edge, so its % unit stands squarely beneath the "100%" mark's unit
    # (v99 -- it was left-aligned before and drifted left of the column).
    # v103, second fitting: the gauge's three lines now stack SINGLE-
    # SPACED, one line pitch apart, like one three-line readout -- 100%
    # on the top line, the live figure on the line directly beneath it,
    # 0% on the line directly beneath that. Exactly one line of space
    # between the fixed marks, never more: the old foot-of-scale perch
    # (top = 886) left a three-line void for the middle figure to float
    # in. The pitch is the panel face's own line height.
    thr_pitch = font.get_linesize()
    zero_img = font.render("0%", True, PANEL_WHITE)
    zero_rect = zero_img.get_rect()
    zero_rect.top = pct_rect.top + 2 * thr_pitch
    zero_rect.right = pct_rect.right
    s.blit(zero_img, zero_rect.topleft)

    # No purple below the 0% line (v105): both bars end flush with the
    # foot of the 0% mark's ink, so the tracks frame exactly the three
    # lines of the scale -- the 100% crown at the top to the 0% foot at
    # the bottom -- and no further. (get_bounding_rect finds the ink's
    # foot however much descent padding the font adds below the digits.)
    # v106: set the HEIGHT, never the bottom edge -- assigning to a
    # pygame Rect's "bottom" SLIDES the whole rectangle (its height
    # unchanged), which is how the bars came to rise above the 100%
    # crown. The tops stay put, flush with the top of the 100%.
    zero_ink = zero_img.get_bounding_rect()
    for rect in (left_bar_rect, right_bar_rect):
        rect.height = zero_rect.top + zero_ink.bottom - rect.top

    # Live thrust readout on the MIDDLE of the gauge's three lines --
    # the fixed scale marks top and bottom, the live figure between
    # them. It counts up and down as the throttle keys are worked, and
    # the blank spaces in the purple bars ride alongside it all the way
    # to 100% and back down again. v103: the middle line speaks for 1%
    # to 99% ONLY -- at the two ends it is EXTINGUISHED and the fixed
    # marks do the talking (the v101 behaviour, restored by order):
    # the top line never reads anything but 100%, the bottom line
    # never anything but 0%, and no figure is ever printed twice. The
    # DISPLAYED figure is gated, so a rounding at the very ends (0.4%
    # rounding to 0, 99.6% to 100) can never sneak an end reading
    # onto the middle line.
    thr_value = int(round(thrust_percent))
    thr_readout = "%d%%" % thr_value
    thr_read_img = font.render(thr_readout, True, PANEL_WHITE)
    thr_read_rect = thr_read_img.get_rect()
    # One line pitch below the 100% mark and one above the 0% mark --
    # with the single-spaced stack that IS the midpoint of the two
    # fixed marks. Right-aligned on the same edge as them, so the %
    # units stack in one column, however wide the number itself is.
    thr_read_rect.centery = pct_rect.centery + thr_pitch
    thr_read_rect.right = pct_rect.right
    if 1 <= thr_value <= 99:
        s.blit(thr_read_img, thr_read_rect.topleft)

    thrust_ratio = max(0.0, min(1.0, thrust_percent / 100.0))
    # Use the centres of the 100% and 0% marks as the gauge endpoints, so
    # at zero thrust the blank spaces sit level with the 0% mark.
    thrust_top_mark = pct_rect.centery
    thrust_zero_mark = zero_rect.centery
    hash_y = int(thrust_zero_mark - thrust_ratio * (thrust_zero_mark - thrust_top_mark))

    # The SELECTED thrust reads as a pair of BLANK SPACES, one in each
    # purple bar: a square notch where the bar is simply NOT painted, so
    # the photograph's own detail shows clean through, the pair riding
    # up and down TOGETHER with the lever to mark the level set (v97 --
    # the v94 blue-framed squares are retired; the marker is the absence
    # of bar now).
    for rect in (left_bar_rect, right_bar_rect):
        gap = pygame.Rect(rect.x, hash_y - rect.width // 2,
                          rect.width, rect.width)
        if gap.top < rect.top:
            gap.top = rect.top
        if gap.bottom > rect.bottom:
            gap.bottom = rect.bottom
        if gap.top > rect.top:
            pygame.draw.rect(s, PANEL_PURPLE,
                             pygame.Rect(rect.x, rect.y,
                                         rect.width, gap.top - rect.top))
        if gap.bottom < rect.bottom:
            pygame.draw.rect(s, PANEL_PURPLE,
                             pygame.Rect(rect.x, gap.bottom,
                                         rect.width, rect.bottom - gap.bottom))

    # The # marks ride INSIDE the blank spaces either side of the
    # thrust figure, one in each bar at the setting currently held
    # (v100 -- they used to stay home at the 0% line as the idle
    # detent). Drawn over the bars so they show at every setting; with
    # the levers closed they rest at the 0% line, as the photograph's
    # parked panel shows.
    for rect in (left_bar_rect, right_bar_rect):
        hash_img = font.render("#", True, PANEL_YELLOW)
        hrect = hash_img.get_rect()
        hrect.center = (rect.centerx, hash_y)
        s.blit(hash_img, hrect)

    # Reverse thrust announced HERE: while the buckets are out the R/TH
    # label flashes yellow-red and the two red guard squares beside it
    # flash red-yellow in step, on the same half-second cadence as the
    # CAB PRESS warning.
    rev_flash = (getattr(jet, "reverser", False)
                 and (pygame.time.get_ticks() // 500) % 2 == 0)
    sq_face = PANEL_YELLOW if rev_flash else PANEL_RED
    rth_color = PANEL_RED if rev_flash else PANEL_YELLOW

    # v122: THE R/TH CLUSTER, RAISED TO THE BARS. The two red guard
    # squares ride up hard under the purple thrust bars -- their tops a
    # single millimetre below the bars' feet (a PHYSICAL millimetre:
    # cm_px measures it on the screen and the panel-to-screen scale
    # converts it back, so it is 1 mm at any window size) -- and the
    # label is balanced between the squares' top and bottom by its INK
    # (the tight bounding rect), not by the glyph cell, so it no longer
    # rides high. Horizontally the label centres on the midpoint
    # between the two bars.
    gsq_gap = max(1, int(round(cm_px(sh, 0.1) / max(scale, 0.2))))
    gsq_top = left_bar_rect.bottom + gsq_gap
    gsq_bottom = gsq_top + 48
    for rect in (left_bar_rect, right_bar_rect):
        gsq = pygame.Rect(0, 0, rect.width, 48)
        gsq.midtop = (rect.centerx, gsq_top)
        pygame.draw.rect(s, sq_face, gsq)
        pygame.draw.rect(s, PANEL_BLUE, gsq, 4)

    rth_img = font.render("R/TH", True, rth_color)
    rth_ink = rth_img.get_bounding_rect()
    rth_cx = (left_bar_rect.centerx + right_bar_rect.centerx) // 2
    s.blit(rth_img, (rth_cx - rth_ink.centerx,
                     (gsq_top + gsq_bottom) // 2 - rth_ink.centery))

    # ---------- GEAR ----------
    # Three plain green squares -- nose (top), left and right mains
    # (bottom row) -- with nothing hanging off them: the down-stem under
    # the top square is gone (v94). Each square follows its own entry in
    # jet.gear_lights -- [top(E), bottom-left, bottom-right] -- so they
    # go out and come back on one at a time during the transit.
    # v104: the WHOLE assembly -- the yellow GEAR label bar, the three
    # green squares and the *D door light -- rides lower, at the
    # register's own row pitch (ROW_PITCH = 48, the photograph's
    # measured pitch), by the captain's order. v106: raised back ONE
    # row -- the net drop is now a single row. v122: the label bar
    # ALONE lifts to one register row below the bottoms of the red
    # R/TH guard squares above (the squares moved up to the bars, and
    # the word follows them). v123: and the three green squares FOLLOW
    # the word up -- the top square's cap rides a millimetre below the
    # label bar (the R/TH squares' own physical millimetre, gsq_gap),
    # its middle centred exactly on the word GEAR; the bottom pair and
    # the *D door light keep the formation. (GEAR_DROP is retired --
    # v16's tidy rule: a knob nothing references is gone.)
    # v126: the bar -- and with it the word GEAR -- now centres on the
    # R/TH label's own centreline (rth_cx, the midpoint between the two
    # red guard squares either side of R/TH), by the captain's order.
    # Its row and its size are untouched. v130: and now the three green
    # squares FOLLOW the word -- the top square's middle lines up under
    # the E and A of GEAR (the bar's own centreline), the bottom pair
    # and the *D door light keeping the formation; the old 1851 pin
    # retires.
    gear_bg_rect = pygame.Rect(1800, gsq_bottom + 48, 102, 50)
    gear_bg_rect.centerx = rth_cx
    pygame.draw.rect(s, PANEL_YELLOW, gear_bg_rect)
    _draw_text_centered(s, "GEAR", gear_bg_rect, PANEL_BLUE, font)

    block = 56
    gear_sq_top = gear_bg_rect.bottom + gsq_gap
    gear_cx = gear_bg_rect.centerx
    e_rect    = pygame.Rect(gear_cx - block // 2,
                            gear_sq_top, block, block)
    new1_rect = pygame.Rect(gear_cx - 83, gear_sq_top + block, block, block)
    new2_rect = pygame.Rect(gear_cx + 29, gear_sq_top + block, block, block)
    door_rect = pygame.Rect(gear_cx + 95, gear_sq_top + block, block, block)

    gl = getattr(jet, "gear_lights", [gear_down, gear_down, gear_down])

    # v97: an out light is a FAINT grey ghost of its square -- barely
    # there against the photograph -- not the near-black slab of before.
    GEAR_OFF_GREY = (120, 124, 134, 96)

    pygame.draw.rect(s, BRIGHT_GREEN if gl[0] else GEAR_OFF_GREY, e_rect)
    pygame.draw.rect(s, BRIGHT_GREEN if gl[1] else GEAR_OFF_GREY, new1_rect)
    pygame.draw.rect(s, BRIGHT_GREEN if gl[2] else GEAR_OFF_GREY, new2_rect)

    # Yellow *D gear-door light: right of the bottom-right green. It
    # trails the greens by one fifth of a second: lit all through the
    # retraction sequence, out a beat after the third green vanishes, and
    # back on a beat after the third green returns on extension. When out
    # it leaves the same faint grey ghost as the green squares (v97).
    door_lit = getattr(jet, "door_light", gear_down)
    pygame.draw.rect(s, PANEL_YELLOW if door_lit else GEAR_OFF_GREY, door_rect)
    if door_lit:
        # Drawn as "*D" the asterisk hugs the top of the square while the
        # D stands full height. Set the two glyphs separately, centring
        # each one's INK, so the star floats level with the middle of the
        # D. (Monospace: two single glyphs tile exactly like "*D".)
        d_img = font.render("D", True, PANEL_BLUE)
        dstar_img = font.render("*", True, PANEL_BLUE)
        dd_x = door_rect.centerx - (dstar_img.get_width() + d_img.get_width()) // 2
        dd_y = door_rect.centery - d_img.get_height() // 2
        d_ink = d_img.get_bounding_rect()
        dstar_ink = dstar_img.get_bounding_rect()
        s.blit(dstar_img, (dd_x, dd_y + d_ink.centery - dstar_ink.centery))
        s.blit(d_img, (dd_x + dstar_img.get_width(), dd_y))

    # ---------- LOWER LEFT (START, F/F, AUTO PILOT, FUEL, VSI, INFO) ----------
    # The yellow register block on the lower-left window post. The dark
    # squares left of START are dark glass the photo ghosts through --
    # the same look as the big boxes, only darker; the panes behind the
    # FUEL / VSI figures wear the CAB PRESS near-clear glass (v109).
    bf = small_font                       # the band's own face
    bcw, _bch = bf.size("A")
    line_h = bf.get_linesize()

    # v93: THE REGISTER, REBUILT TO THE CAPTAIN'S PHOTOGRAPH. The block
    # stands one row below the DME row (v111 -- it hugged it until the
    # captain's one-row drop) and stretches from the IAS/DME column's
    # left edge to the ALT/GROUND SPEED column's left edge. Its profile
    # is the castle of the original panel: START and F/F stand as raised
    # tabs with the dark cell bay beside them, the full-width field
    # below carries AUTO PILOT: / FUEL: / VSI:, the right column runs
    # unbroken from F/F down through LB and FPM, and the INFO: tag is
    # the left column continuing one row below the field. v108: the
    # START word sits over character columns 2-6 of the AUTO PILOT:
    # line -- the 'S' directly above the 'T' of AUTO, the final 'T'
    # directly above the 'I' of PILOT -- and the yellow bar is trimmed
    # ink-tight beneath the word. The four slow cells between START
    # and F/F keep their bay exactly as it was; the two rapid cells
    # gain the old tab's left overhang -- room to spin, unsquashed.
    block_left  = 184                     # clear of the windscreen frame's
                                          # left post (it reaches x=172 at
                                          # mid-block; the photograph's
                                          # flush 150 would sit ON it)
    block_right = 502                     # the ALT/GROUND SPEED column's
                                          # left edge
    left_x = block_left + 12              # the labels' left margin

    tab_h    = line_h + 8                 # the START / F/F tab row
    # v111: the WHOLE register rides ONE ROW down, by the captain's
    # order -- tabs, cell bays, the AUTO PILOT / FUEL / VSI field with
    # its figures, the ON/OFF flag, the AUTOLAND placard and the INFO
    # tag and line all keep their places WITHIN the block; the block
    # itself drops one register row (the same 48 px pitch the GEAR
    # cluster's drop used). The DME row above and the CDI stay
    # exactly where they were. One knob:
    REGISTER_DROP = 1 * 48                # one register row, in pixels
    tab_top  = dme_box.bottom + 8 + REGISTER_DROP
    field_top = tab_top + tab_h
    auto_y   = field_top + 4
    ROW_PITCH = 48                        # the photograph's measured pitch
    fuel_y   = auto_y + ROW_PITCH
    vsi_y    = auto_y + 2 * ROW_PITCH
    # v97: flush with the VSI cutout's bottom (was +9) -- the 3px margin
    # read as a thin yellow line spanning to the F/F column's right edge.
    field_bottom = vsi_y + line_h + 6
    info_y   = field_bottom + 4

    # The castle profile, as rectangles. v108: the START word occupies
    # character columns 2-6 of the register's monospace line ("AUTO
    # PILOT:" below starts at the same left_x), so its 'S' stands
    # directly above the 'T' of AUTO and its final 'T' directly above
    # the 'I' of PILOT, exactly as the captain's photograph shows. The
    # yellow tab is trimmed INK-TIGHT under the word -- from the left
    # edge of the 'S' to the right edge of the final 'T', no yellow
    # side margins -- which hands the old tab's left overhang to the
    # two-cell bay. The F/F column and the four-cell bay are unmoved.
    ff_col     = pygame.Rect(427, tab_top, block_right - 427,
                             field_bottom - tab_top)
    start_txt_x = left_x + 2 * bcw      # the 'T'-of-AUTO column
    start_word = bf.render("START", True, PANEL_BLUE)
    start_ink  = start_word.get_bounding_rect()   # the tight S-to-T ink
    start_tab  = pygame.Rect(start_txt_x + start_ink.x, tab_top,
                             start_ink.width, tab_h)
    duo_hole   = pygame.Rect(block_left, tab_top,
                             start_tab.left - block_left, tab_h)
    quad_hole  = pygame.Rect(start_tab.right, tab_top,
                             ff_col.left - start_tab.right, tab_h)
    field_rect = pygame.Rect(block_left, field_top,
                             block_right - block_left,
                             field_bottom - field_top)
    info_bg    = pygame.Rect(block_left, field_bottom,
                             12 + bf.size("INFO:")[0] + 14, tab_h)

    hole_fill = (50, 75, 125, 203)        # the parked-cell glass; v122:
                                          # transparency down a QUARTER,
                                          # by the captain's order (alpha
                                          # 185 -> 203: the see-through
                                          # share 70/255 is now 52/255)

    # YELLOW BLOCKS
    pygame.draw.rect(s, PANEL_YELLOW, field_rect)   # the full-width field
    pygame.draw.rect(s, PANEL_YELLOW, start_tab)    # the raised START tab
    pygame.draw.rect(s, PANEL_YELLOW, ff_col)       # F/F + LB + FPM column
    pygame.draw.rect(s, PANEL_YELLOW, info_bg)      # the INFO: tag below

    # Dark cell bays: two left of START, four between START and F/F.
    pygame.draw.rect(s, hole_fill, duo_hole)
    pygame.draw.rect(s, hole_fill, quad_hole)

    # The FUEL / VSI figure panes (v109): the CAB PRESS near-clear glass
    # behind the readings -- the near-opaque dark cutout is retired --
    # each pane stepping in to hug its own label, as the photo shows.
    value_right_x = 410                   # the fixed right edge of both
    cut_right = ff_col.left - 2
    fuel_cut = pygame.Rect(left_x + bf.size("FUEL:")[0] + 28, fuel_y - 6,
                           cut_right - (left_x + bf.size("FUEL:")[0] + 28),
                           line_h + 12)
    vsi_cut = pygame.Rect(left_x + bf.size("VSI:")[0] + 28, vsi_y - 6,
                          cut_right - (left_x + bf.size("VSI:")[0] + 28),
                          line_h + 12)
    # v122: the register's glass loses a quarter of its transparency
    # too, by the captain's order -- the panes wear a LOCAL fill now
    # (alpha 60 -> 109: the see-through share 195/255 is now 146/255),
    # so TOP_FILL itself is untouched and the rest of the panel's
    # glass is exactly as it was. (The register's yellows are opaque
    # already, so they do not move.)
    pane_fill = (15, 30, 110, 109)
    pygame.draw.rect(s, pane_fill, fuel_cut)
    pygame.draw.rect(s, pane_fill, vsi_cut)

    # Row texts (blue on yellow). START is NOT centred in its tab
    # (v108): its letters hold character columns 2-6 of the register's
    # monospace grid, and the ink-tight tab wraps the word; F/F, LB and
    # FPM right-align inside their column, three edges on the one line.
    s.blit(start_word, (start_txt_x,
                        start_tab.centery - start_word.get_height() // 2))
    _draw_text(s, "AUTO PILOT:", left_x, auto_y, PANEL_BLUE, bf)
    _draw_text(s, "FUEL:", left_x, fuel_y, PANEL_BLUE, bf)
    _draw_text(s, "VSI:", left_x, vsi_y, PANEL_BLUE, bf)

    def _col_text(txt, y):
        img = bf.render(txt, True, PANEL_BLUE)
        s.blit(img, (ff_col.right - 7 - img.get_width(), y))

    _col_text("F/F", start_tab.top + 4)

    # Readings right-justified against the one fixed right edge, so the
    # LAST digit of every reading sits in the same column at all times --
    # a five-character VSI reading grows LEFT into the dark cutout
    # instead of pushing the unit badges about.
    fuel_value_text = f"{int(fuel_kg):4d}"
    fuel_value_img = bf.render(fuel_value_text, True, PANEL_WHITE)
    s.blit(fuel_value_img, (value_right_x - fuel_value_img.get_width(), fuel_y))
    _col_text("LB", fuel_y)

    vsi_value_text = f"{int(vsi_fpm):4d}"
    vsi_value_img = bf.render(vsi_value_text, True, PANEL_WHITE)
    s.blit(vsi_value_img, (value_right_x - vsi_value_img.get_width(), vsi_y))
    _col_text("FPM", vsi_y)

    # Autopilot output (v93): the yellow ON/OFF box now stands BETWEEN
    # two detached red guard bars, a dark gap either side, centred on
    # the AUTO PILOT line -- the old red picture frame is gone, as the
    # photograph shows.
    ap_text = "ON" if ap else "OFF"
    ap_box = pygame.Rect(570, 0, 78, 48)
    ap_box.centery = auto_y + line_h // 2
    ap_bar_l = pygame.Rect(ap_box.left - 18, ap_box.top, 12, ap_box.height)
    ap_bar_r = pygame.Rect(ap_box.right + 6, ap_box.top, 12, ap_box.height)
    pygame.draw.rect(s, PANEL_RED, ap_bar_l)
    pygame.draw.rect(s, PANEL_RED, ap_bar_r)
    pygame.draw.rect(s, PANEL_YELLOW, ap_box)
    _draw_text_centered(s, ap_text, ap_box, PANEL_BLUE, bf)

    # ---------- CDI (course deviation indicator) ----------
    # Horizontal gauge right of the AUTO PILOT assembly. The blue
    # vertical needle sits in the middle when the aircraft is exactly on
    # the OBS course line; drift off course and it walks TOWARD the
    # course (full scale = 2 nm either side), so working the [A]/[D] turn
    # keys moves the line. Two dots each side of centre mark the scale.
    xte_nm = getattr(jet, "xte", 0.0)
    CDI_FULL_NM = 2.0
    cdi_w = 408
    cdi_track = pygame.Rect(734, 1000, cdi_w, 44)
    # v107: the CAB PRESS near-clear glass (was solid yellow) -- the
    # blue rim, the dots and the needle are unchanged.
    pygame.draw.rect(s, TOP_FILL, cdi_track)
    pygame.draw.rect(s, PANEL_BLUE, cdi_track, 4)
    cdi_frac = max(-1.0, min(1.0, xte_nm / CDI_FULL_NM))
    needle_x = cdi_track.centerx - int(cdi_frac * (cdi_w // 2 - 10))
    # Five dots: one at the centre (the on-course mark, so the needle
    # has a dot to light up even at start-up) plus two each side.
    dot_xs = [cdi_track.centerx]
    for dot_i in (1, 2):
        for dot_s in (-1, 1):
            dot_xs.append(cdi_track.centerx + dot_s * dot_i * (cdi_w // 6))
    for dot_x in dot_xs:
        pygame.draw.circle(s, PANEL_BLUE, (dot_x, cdi_track.centery), 4)
    pygame.draw.line(s, PANEL_BLUE,
                     (needle_x, cdi_track.y + 4),
                     (needle_x, cdi_track.bottom - 4), 6)
    # The dot under the needle is painted ON TOP of it, so a bright white
    # dot shines through the blue needle; it turns blue again once the
    # needle moves on.
    for dot_x in dot_xs:
        if abs(needle_x - dot_x) <= 6:
            pygame.draw.circle(s, PANEL_WHITE,
                               (dot_x, cdi_track.centery), 5)
    # The nameplate (v93): the big label face used to sprawl well past
    # both ends of the track, centred off to boot. It is now set in its
    # own smaller face, fitted to the track's width and centred exactly
    # over the needle's travel.
    cdi_lab = _panel_cdi_title_font.render("Course Deviation Indicator",
                                           True, PANEL_YELLOW)
    s.blit(cdi_lab, (cdi_track.centerx - cdi_lab.get_width() // 2,
                     cdi_track.y - cdi_lab.get_height() - 2))

    # AUTOLAND flag on the START row, right of the band: "A/L? Y/N"
    # while the offer is on the table, "AUTOLAND" once [Y] hands the
    # landing to the autopilot. Blue-on-yellow with a blue border, the
    # SAVE GAME button's own style, and itself a button.
    al_on = getattr(jet, "autoland", False)
    al_pending = getattr(jet, "al_offer", False)
    if al_on or al_pending:
        al_text = "AUTOLAND" if al_on else "A/L? Y/N"
        al_flag = pygame.Rect(0, 0, btn_font.size(al_text)[0] + 28,
                              btn_font.get_linesize() + 12)
        al_flag.left = 556
        # v111: rides the START row down with the register (the hard 916
        # was the old tab_top + 8 -- the offset is kept, the row moves).
        al_flag.top = tab_top + 8
        pygame.draw.rect(s, PANEL_YELLOW, al_flag)
        pygame.draw.rect(s, PANEL_BLUE, al_flag, 4)
        _draw_text_centered(s, al_text, al_flag, PANEL_BLUE, btn_font)
        # The placard is a button, like the [Z] ABANDON placard --
        # register its rect for the MOUSEBUTTONDOWN handler. The dict is
        # cleared at the top of every draw, so no stale rect survives.
        PANEL_BUTTONS["autoland"] = al_flag

    # ---------- SPINNING DIAGONAL CELLS (VZ-200 tribute) ----------
    # The black/white diagonal cells STAND in their bays at all times
    # (v109: before the engines are started they rest in the standing
    # pattern -- until now the bays were bare dark glass before [E], so
    # the checkered rectangles looked missing). The moment the engines
    # start, the TWO bays immediately left of START spin RAPIDLY -- and
    # KEEP spinning all the way to liftoff; they park once she leaves
    # the ground, and fall quiet again if the engines are shut down on
    # the ground. The FOUR bays between START and F/F spin for the rest
    # of the flight -- at TWICE the old leisurely rate. (v108: the
    # ink-tight START tab hands its old left overhang to the two rapid
    # bays; the four slow bays keep their span exactly as it was.)
    # Every cell is drawn the same way round (nothing inverted), so no
    # two same-coloured rectangles ever touch.
    eng_t0 = getattr(jet, "eng_start_t", None)
    if eng_t0 is None and engines:
        eng_t0 = 0.0            # loaded an old save with engines running
    if eng_t0 is not None:
        since_start = jet.elapsed - eng_t0
        RAPID_FLIP_SIM = 1.5    # fast spin: flip every 1.5 sim-seconds ...
                                # ... until she leaves the ground
        SLOW_FLIP_SIM = 3.0     # the bays between START and F/F: flip
                                # every 3 sim-seconds -- TWICE the old
                                # 6-sim-second rate
        rapid_flip = (int(since_start / RAPID_FLIP_SIM) % 2 == 1) \
                     if (engines and not jet.airborne) else False
        slow_flip = int(jet.elapsed / SLOW_FLIP_SIM) % 2 == 1
    else:
        rapid_flip = slow_flip = False   # parked: the standing pattern
    # Two cells immediately left of START, filling the bay exactly
    duo_cw = max(8, duo_hole.width // 2)
    for i in range(2):
        _draw_diag_shape(s, duo_hole.x + i * duo_cw, duo_hole.y,
                         PANEL_WHITE, (0, 0, 0), flip=rapid_flip,
                         w=duo_cw, h=line_h)
    # Four cells between START and F/F, filling the gap exactly
    quad_cw = max(8, quad_hole.width // 4)
    for i in range(4):
        _draw_diag_shape(s, quad_hole.x + i * quad_cw, quad_hole.y,
                         PANEL_WHITE, (0, 0, 0), flip=slow_flip,
                         w=quad_cw, h=line_h)

    # ---------- INFO / WIND ----------
    info_text = "INFO:"
    info_img = bf.render(info_text, True, PANEL_BLUE)
    # The yellow tag itself is drawn with the register block above (v93):
    # it is the block's left column continuing one row below the field.
    s.blit(info_img, (left_x, info_y))

    wind_x = info_bg.right + 20
    if paused:
        msg_display = "PAUSED - [SPACE] or the RESUME button to fly on."
    else:
        # The default INFO line: the surface wind at the airport tuned
        # in the DME -- the destination on "-", each enroute field on
        # "v0","v1" ..., the origin on "+" -- named by its ICAO code
        # (YMML Melbourne, YSSY Sydney, ...). The wind direction shown is
        # always the route track + 180, so she arrives heading straight
        # into the wind; the speed is a per-airport figure from the
        # 10-30 range -- FOR SHOW ONLY; the flight model reads nothing of
        # it.
        dme_apt_name = orig_name if jet.dme_chan == "+" else apt_name
        dme_icao = AIRPORT_ICAO.get(dme_apt_name, "????")
        wind_spd = surface_wind_show(jet, dme_apt_name)   # for show
        msg_display = msg if msg else "%s SURFACE WIND %03d %d" % (
            dme_icao, wind_dir, wind_spd)
    # Over-long INFO lines are set in a smaller font so they end inside
    # the windscreen; lines that fit are drawn exactly as before.
    _draw_text_fit(s, msg_display, wind_x, info_y, 2040, PANEL_WHITE, bf)

    _draw_strut_clock(s)

    # Land the whole HUD on the photograph in one blit.
    surf.blit(ov, (0, 0))

    # NOTE: the bottom help legend is deliberately NOT drawn here any more.
    # It is drawn by draw_help_legend() AFTER the panel has been scaled to
    # the screen (in flight_hud), at native screen resolution, so the
    # downscale can no longer erode the thin strokes of '+' and '-' (which
    # used to make '[+/-]' read as '[|/ ]' on smaller screens).


# ----------------------------------------------------------------------
#  HELP LEGEND  --  drawn AFTER scaling, at native screen resolution
# ----------------------------------------------------------------------
HELP_TEXT = ("[E] engines [B] brakes [R] rev [F/Shift+F] flaps [G] gear [C] DME "
             "[V] enroute [W/S] pitch [+/-/Up/Dn] thrust [Shift++] rapid [A/D] turn [O] OBS "
             "[K/Shift+K] FL [L] level [P] AP [Y/N] autoland [M] sound [SPC] pause [Z] abandon")


def draw_help_legend(screen, px, py, pw, ph, scale, sh):
    """Draw the key-press legend straight onto the screen, over the bottom
    of the already-scaled panel. Drawing it here -- after transform.scale --
    keeps every glyph pin-sharp, so thin strokes like the '-' and the '+'
    crossbar can no longer be eaten by the downscale.

    The box is the reference HUD's wide ribbon of navy glass with a blue
    rim. v131: the panel now COVERS the screen, its bottom edge cropped
    away below the display, so the ribbon can no longer anchor to the
    panel's bottom edge -- it centres on the panel and seats itself a
    few pixels above the SCREEN's bottom edge, over the photograph.

    px, py  = top-left corner of the scaled panel on screen
    pw, ph  = scaled panel size, in screen pixels
    scale   = the factor the panel was scaled by
    sh      = the screen's height, in pixels
    """
    s = max(scale, 0.2)
    box = pygame.Rect(0, 0, min(int(1920 * s), pw), int(48 * s))
    box.centerx = px + pw // 2
    box.bottom = sh - max(4, int(6 * s))
    help_size = max(8, int(34 * s))
    tiny_font = pygame.font.SysFont("consolas", help_size)
    max_help_w = box.width - 2 * max(3, int(20 * s))
    while help_size > 8 and tiny_font.size(HELP_TEXT)[0] > max_help_w:
        help_size -= 1
        tiny_font = pygame.font.SysFont("consolas", help_size)
    help_surf = tiny_font.render(HELP_TEXT, True, PANEL_WHITE)
    glass = pygame.Surface((box.width, box.height), pygame.SRCALPHA)
    glass.fill((8, 26, 110, 205))         # the ribbon's own navy (the
                                          # v111 tie to the ETA box's ink
                                          # retired with the navy itself,
                                          # v113)
    pygame.draw.rect(glass, (50, 120, 255, 245), glass.get_rect(),
                     max(2, int(4 * s)))
    screen.blit(glass, box.topleft)
    screen.blit(help_surf, (box.centerx - help_surf.get_width() // 2,
                            box.centery - help_surf.get_height() // 2))

# ----------------------------------------------------------------------
#  SCREEN 4: MAIN FLIGHT HUD (2X scaled panel)
# ----------------------------------------------------------------------
def flight_hud(screen, sw, sh, fonts, jet):
    clock = pygame.time.Clock()
    pygame.key.set_repeat(200, 50)

    panel_surf = pygame.Surface((PANEL_W, PANEL_H))
    last_pause_toggle = 0           # debounce so held SPACE can't flicker
    turn_held = set()               # A/D/W/S/V keys physically held down --
                                    # pygame's own repeat KEYDOWNs are
                                    # ignored until key-up
    turn_repeat = {}                # hold-to-turn: K_a/K_d -> the real time
                                    # (ms) the next held-key step falls due
    # Hold-to-turn cadence: a single [A]/[D] tap still steps exactly 5
    # degrees; keep the key held and, after a short pause, the heading
    # (or the bug, under the autopilot) keeps stepping at this measured
    # pace until the key comes back up.
    TURN_HELD_DELAY_MS = 450        # pause after the first step
    TURN_HELD_STEP_MS  = 300        # interval between further held steps
    # v93: the thrust lever joins the hold-to-repeat family -- one point
    # a press, and while held a point every 100 ms after the usual pause
    # (a brisker cadence than the turns: a lever winds faster than a
    # heading). The keypad +/- ride along too. v110: the Up/Down arrows
    # join as the SECONDARY lever -- same points, same cadence -- and
    # with Shift down the increases run RAPID (RAPID_THRUST_STEP a step).
    THRUST_KEYS = (pygame.K_EQUALS, pygame.K_PLUS, pygame.K_KP_PLUS,
                   pygame.K_MINUS, pygame.K_KP_MINUS,
                   pygame.K_UP, pygame.K_DOWN)
    THRUST_HELD_STEP_MS = 100
    global _landed_hold_until       # v73: shared with audio_update -- the
                                    # three-second hold keeps the sound on
    _landed_hold_until = 0
    last_hours_bank = pygame.time.get_ticks()   # v78: the career flight
                                    # hours bank to disc every fifteen
                                    # real seconds aloft, so even a
                                    # computer shutdown loses at most a
                                    # quarter-minute of flying
    dwell_start = None              # set when the rollout ends: admire the
                                    # parked jet for as long as you like
    dwell_done = False              # any key during the dwell ends it
    stop_prompt = False             # full stop at an intermediate airport:
                                    # waiting on the [C]/[R] choice (v22)

    # A crash or quit exits at once; a full stop dwells on the panel first.
    while not (jet.dead or jet.quit):
        dt = clock.tick(60) / 1000.0
        dwell_active = dwell_start is not None
        # v73: the three-second hold on the landed details -- the screen
        # stays EXACTLY as it is, all sound continues, and the continue
        # options are not on offer yet (ESC and the DESKTOP button stay
        # live, as ever).
        landed_hold = (jet.done and dwell_start is None
                       and not stop_prompt and _landed_hold_until > 0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jet.quit = True
            if event.type == pygame.KEYDOWN:
                if jet.desktop_offer:
                    # DESKTOP double-check (v73): while the offer is on the
                    # table ANY key cancels it and flies on -- exactly as
                    # any key (ESC included) cancels the [Z] ABANDON offer.
                    # The world is frozen and the cockpit silent meanwhile
                    # (see the update gate below).
                    jet.desktop_offer = False
                    jet.msg = "Desktop cancelled - she's still yours, captain."
                elif jet.abandon_offer:
                    # [Z] abandon confirmation (v24): only a SECOND, fresh
                    # [Z] confirms -- the arming press (and any held-key
                    # auto-repeat still arriving from before the offer) is
                    # ignored, and every other key, ESC included, cancels
                    # the offer and flies on. The world is frozen meanwhile
                    # (see the update gate below).
                    if event.key == pygame.K_z and event.key not in turn_held:
                        jet.to_routes = True   # Route Selection, no summary
                    elif event.key in turn_held:
                        pass                   # stale auto-repeat: ignore
                    else:
                        jet.abandon_offer = False
                        jet.msg = "Abandon cancelled - she's still yours, captain."
                elif event.key == pygame.K_ESCAPE:
                    jet.quit = True
                elif stop_prompt:
                    # Enroute full-stop prompt (v22): only the two offered
                    # keys act -- every other key is swallowed while the
                    # captain decides. [C] sets her up for the onward leg;
                    # [R] hands the flight back to Route Selection.
                    if event.key == pygame.K_c:
                        enroute_departure(jet)
                        stop_prompt = False
                        play_bing()
                    elif event.key == pygame.K_r:
                        jet.to_routes = True
                elif landed_hold:
                    pass                # v73: the landed details hold for
                                        # three seconds -- the options are
                                        # not on offer yet, so keys rest
                elif dwell_active:
                    dwell_done = True   # admire her at leisure, then any key
                elif event.key == pygame.K_z:
                    # [Z] abandon the flight (v24): the first press only
                    # MAKES the offer -- a flashing placard beside the
                    # DESKTOP button and a line at INFO -- so a
                    # stray key can never throw the flight away. The
                    # arming press goes into turn_held so its own
                    # auto-repeat cannot count as the confirming press.
                    jet.abandon_offer = True
                    turn_held.add(pygame.K_z)
                    jet.msg = ("ABANDON FLIGHT? Press [Z] again (or click "
                               "the placard) to confirm - any other key "
                               "to fly on.")
                    play_bing()
                elif event.key == pygame.K_SPACE:
                    if pygame.time.get_ticks() - last_pause_toggle > 250:
                        last_pause_toggle = pygame.time.get_ticks()
                        jet.paused = not jet.paused
                elif event.key == pygame.K_F5:
                    jet.msg = "Game saved." if save_jet(jet) else "Save failed - sorry!"
                    play_bing()
                elif event.key == pygame.K_F9:
                    loaded = load_jet()
                    if loaded is not None:
                        # v78: bank the outgoing flight's career hours
                        # before the saved jet's state replaces hers
                        bank_flight_hours(jet)
                        bank_career_distance(jet)   # v87: and her distance
                        jet.__dict__.update(loaded.__dict__)
                        jet.msg = "Saved flight loaded - welcome back!"
                        play_bing()
                    else:
                        jet.msg = "No saved game found yet."
                elif event.key == pygame.K_v:
                    # Peek at the Enroute screen: the Learjet's nose
                    # shows how far along the route she now is. One
                    # press = one peek: key auto-repeat must not bounce
                    # the map open and shut while [V] is held, so repeat
                    # KEYDOWNs are swallowed until the key physically
                    # comes back up (the same protection the [A]/[D]
                    # turn keys have).
                    if event.key not in turn_held:
                        turn_held.add(event.key)
                        briefing_screen(screen, sw, sh, fonts, jet.route, jet)
                else:
                    if not jet.paused:      # controls are locked while paused
                        if event.key in (pygame.K_a, pygame.K_d,
                                         pygame.K_w, pygame.K_s):
                            # One press = one step; pygame's repeat KEYDOWNs
                            # are swallowed until the key comes back up --
                            # and HOLDING any of the four schedules the
                            # measured hold-to-repeat steps processed below
                            # the event loop: [A]/[D] wind the turn, and
                            # v35 gives [W]/[S] the same treatment, one
                            # degree a step until released. [W]/[S] repeat
                            # only once airborne -- on the ground one [W]
                            # press is the rotation, and that is that.
                            if event.key not in turn_held:
                                turn_held.add(event.key)
                                handle_key(jet, event)
                                if event.key in (pygame.K_a, pygame.K_d):
                                    turn_repeat[event.key] = (
                                        pygame.time.get_ticks()
                                        + TURN_HELD_DELAY_MS)
                                elif jet.airborne:
                                    turn_repeat[event.key] = (
                                        pygame.time.get_ticks()
                                        + TURN_HELD_DELAY_MS)
                        elif event.key in THRUST_KEYS:
                            # v93: one press = one point of thrust; a
                            # held key keeps winding a point at a time
                            # until it comes up -- the same hold-to-
                            # repeat machinery the turn and pitch keys
                            # use, at the lever's own brisker cadence.
                            # Pygame's own repeat KEYDOWNs are swallowed
                            # until the key physically returns.
                            if event.key not in turn_held:
                                turn_held.add(event.key)
                                handle_key(jet, event)
                                turn_repeat[event.key] = (
                                    pygame.time.get_ticks()
                                    + TURN_HELD_DELAY_MS)
                        elif event.key == pygame.K_g:
                            # [G] is a toggle: swallow auto-repeat KEYDOWNs so
                            # a held key cannot reverse the gear the instant it
                            # locks. One physical press = one toggle.
                            if event.key not in turn_held:
                                turn_held.add(event.key)
                                handle_key(jet, event)
                        elif event.key in (pygame.K_y, pygame.K_n):
                            # One press = one decision (v60): a HELD [Y]
                            # must not accept and cancel in the same
                            # blink, so repeat KEYDOWNs are swallowed
                            # until the key physically comes back up --
                            # the same protection [V] and [Z] enjoy.
                            if event.key not in turn_held:
                                turn_held.add(event.key)
                                handle_key(jet, event)
                        else:
                            handle_key(jet, event)
            elif event.type == pygame.KEYUP:
                turn_held.discard(event.key)
                turn_repeat.pop(event.key, None)
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # The panel is cover-scaled and centred on screen (v131)
                # -- map the click back into panel coordinates through
                # the SAME fit the draw below used, before testing.
                sc, ox, oy, _pw, _ph = _panel_screen_fit(sw, sh)
                mx = (event.pos[0] - ox) / sc
                my = (event.pos[1] - oy) / sc
                save_rect = PANEL_BUTTONS.get("save")
                load_rect = PANEL_BUTTONS.get("load")
                pause_rect = PANEL_BUTTONS.get("pause")
                desktop_rect = PANEL_BUTTONS.get("desktop")
                abandon_rect = PANEL_BUTTONS.get("abandon")
                al_rect = PANEL_BUTTONS.get("autoland")
                if (desktop_rect is not None and not jet.abandon_offer
                        and desktop_rect.collidepoint(mx, my)):
                    # DESKTOP double-check (v73): the FIRST click only
                    # MAKES the offer -- the button itself becomes a
                    # flashing DESKTOP? placard (see draw_panel) with a
                    # line at INFO, the world frozen and the cockpit
                    # silent while the captain decides. A SECOND click on
                    # the button confirms and closes the sim to the
                    # desktop; a click anywhere else -- or any key --
                    # cancels and flies on. The [Z] ABANDON routine,
                    # brought to the mouse. Live in every state the key
                    # is live in: paused, at the enroute stop prompt,
                    # through the landed hold and the full-stop dwell.
                    # (While the [Z] offer is up, a click away from the
                    # placard cancels it instead -- as ESC does.)
                    if jet.desktop_offer:
                        jet.quit = True
                    else:
                        jet.desktop_offer = True
                        jet.msg = ("QUIT TO DESKTOP? Click the DESKTOP "
                                   "button again to confirm - any other "
                                   "click or key to fly on.")
                        play_bing()
                elif jet.desktop_offer:
                    # While the DESKTOP offer is up (v73): a click anywhere
                    # else cancels it and flies on.
                    jet.desktop_offer = False
                    jet.msg = "Desktop cancelled - she's still yours, captain."
                elif landed_hold:
                    pass                # v73: during the three-second hold
                                        # only the DESKTOP button stays live
                elif dwell_active:
                    pass                # clicks rest with the parked jet --
                                        # only the DESKTOP button stays live
                elif jet.abandon_offer:
                    # While the ABANDON offer is up (v24): clicking the
                    # flashing placard confirms; clicking anywhere else
                    # flies on.
                    if abandon_rect is not None and abandon_rect.collidepoint(mx, my):
                        jet.to_routes = True
                    else:
                        jet.abandon_offer = False
                        jet.msg = "Abandon cancelled - she's still yours, captain."
                elif (al_rect is not None and al_rect.collidepoint(mx, my)
                        and not jet.paused):
                    # v60: the placard is a button -- click A/L? Y/N to
                    # accept, click AUTOLAND to hand her back.
                    if jet.autoland:
                        cancel_autoland(jet, "y")
                        play_bing()
                    elif jet.al_offer:
                        accept_autoland(jet)
                elif pause_rect is not None and pause_rect.collidepoint(mx, my):
                    jet.paused = not jet.paused
                elif save_rect is not None and save_rect.collidepoint(mx, my):
                    jet.msg = "Game saved." if save_jet(jet) else "Save failed - sorry!"
                elif load_rect is not None and load_rect.collidepoint(mx, my):
                    loaded = load_jet()
                    if loaded is not None:
                        # v78: bank the outgoing flight's career hours
                        # before the saved jet's state replaces hers
                        bank_flight_hours(jet)
                        bank_career_distance(jet)   # v87: and her distance
                        jet.__dict__.update(loaded.__dict__)
                        jet.msg = "Saved flight loaded - welcome back!"
                    else:
                        jet.msg = "No saved game found yet."

        # Hold-to-turn: while [A] or [D] is physically held, keep stepping
        # the heading at the measured cadence until key-up. One step per
        # frame at most, and silent while paused, dwelling, holding the
        # landed details, at the enroute stop prompt, or while either
        # offer ([Z] / DESKTOP) is on the table -- exactly as a fresh
        # keypress would be.
        if (not jet.paused and not stop_prompt and not dwell_active
                and not landed_hold
                and not jet.abandon_offer and not jet.desktop_offer):
            now_ms = pygame.time.get_ticks()
            for rep_key, due_ms in list(turn_repeat.items()):
                if rep_key not in turn_held:
                    turn_repeat.pop(rep_key, None)      # missed key-up
                elif now_ms >= due_ms:
                    if rep_key in (pygame.K_a, pygame.K_d):
                        turn_step(jet, -1.0 if rep_key == pygame.K_a else 1.0)
                        turn_repeat[rep_key] = now_ms + TURN_HELD_STEP_MS
                    elif rep_key in THRUST_KEYS:
                        # Held [+]/[-] (v93): a point a step, at the
                        # lever's own brisker cadence, until key-up.
                        # v110: with Shift down the increases run RAPID --
                        # RAPID_THRUST_STEP a step. Shift is read LIVE
                        # (get_mods), so it can be pressed or released
                        # mid-hold and the lever changes gear on the spot.
                        # Decreases keep their one-point manners either way.
                        if rep_key in (pygame.K_MINUS, pygame.K_KP_MINUS,
                                       pygame.K_DOWN):
                            thrust_step(jet, -1.0)
                        elif pygame.key.get_mods() & pygame.KMOD_SHIFT:
                            thrust_step(jet, +1.0, RAPID_THRUST_STEP)
                        else:
                            thrust_step(jet, +1.0)
                        turn_repeat[rep_key] = now_ms + THRUST_HELD_STEP_MS
                    elif jet.airborne:
                        # Held [W]/[S] (v35): a degree a step until key-up.
                        pitch_step(jet, 1.0 if rep_key == pygame.K_w else -1.0)
                        turn_repeat[rep_key] = now_ms + TURN_HELD_STEP_MS

        # Advance physics by the REAL frame time (x game speed), clamped so
        # pauses (e.g. peeking at the Enroute screen) can't jump the world.
        # When PAUSED the world is frozen - the panel still redraws, and
        # [SPACE], the buttons, [V], [F5] and [F9] all stay live. The world
        # also freezes -- and the cockpit falls silent -- while the [Z]
        # ABANDON offer or the DESKTOP offer (v73) is on the table, so she
        # holds station while the captain decides. (The three-second landed
        # hold is different by order: the screen holds AND the sound plays
        # on -- see _landed_hold_until.)
        if not jet.paused and not jet.abandon_offer and not jet.desktop_offer:
            update(jet, min(dt, 0.1) * getattr(jet, "time_scale", TIME_SCALE))  # v56: the leg's own clock
        # v78: bank the career flight hours every fifteen real seconds.
        if pygame.time.get_ticks() - last_hours_bank >= 15000:
            last_hours_bank = pygame.time.get_ticks()
            bank_flight_hours(jet)
            bank_career_distance(jet)   # v87: the logbook's nm tick too
        # v74: the moment the wheels stop, arm the three-second hold HERE,
        # BEFORE audio_update runs -- v73 armed it a frame later (below),
        # so the j.done hush cut the landing voice at the stop itself, and
        # she never rejoined for the very hold that promised "all sound
        # continues".
        if (jet.done and not _landed_hold_until
                and dwell_start is None and not stop_prompt):
            _landed_hold_until = (pygame.time.get_ticks()
                                  + int(LANDED_HOLD_S * 1000))
        if jet.abandon_offer or jet.desktop_offer:
            audio_off()
        else:
            audio_update(jet)

        # The moment the rollout ends, the jet sits on the runway so you
        # can admire your work and contemplate the numbers AT LEISURE.
        # The INFO line invites a keypress: any key moves on to the
        # flight summary, and from there back to Route Selection.
        if stop_prompt and not jet.done:
            stop_prompt = False      # an in-flight save was loaded [F9]
                                     # right over the prompt - carry on
        if _landed_hold_until and not jet.done:
            _landed_hold_until = 0   # the same defence for the v73 hold
        if jet.done and dwell_start is None and not stop_prompt:
            # v73 (1): the wheels have stopped -- the landed details hold
            # EXACTLY as they are for LANDED_HOLD_S REAL seconds before any
            # option is offered. ALL sound continues meanwhile: the hold
            # itself is armed the frame the wheels stop, BEFORE
            # audio_update (see above -- v74), and audio_update reads the
            # same deadline through _landed_hold_active() to keep the
            # full-stop hush off until the options appear.
            if pygame.time.get_ticks() >= _landed_hold_until:
                via_names = {v["name"] for v in route_vias(jet.route)}
                if jet.landed_name in via_names:
                    # Full stop at an INTERMEDIATE airport (v22): ask the
                    # captain -- [C] continue the flight, [R] return to
                    # Route Selection. The world stays frozen meanwhile
                    # (step() ignores a done jet).
                    stop_prompt = True
                    jet.msg = ("Full stop at %s! [C] continue the flight to "
                               "%s, [R] return to Route Selection."
                               % (jet.landed_name, jet.route["name"].split("-")[1]))
                else:
                    dwell_start = pygame.time.get_ticks()
                    jet.msg = ("Full stop at %s! Press any key: flight summary, "
                               "then Route Selection." % (jet.landed_name or "the field"))
        if dwell_done or jet.to_routes:
            break
        # Scale the panel to COVER the screen (v131) -- the intro, route
        # and enroute photographs' own treatment, so the HUD fills the
        # whole display like every other screen. Worked out BEFORE the
        # panel is drawn, so draw_panel can convert physical sizes (the
        # quarter-inch gaps, the 4 x 10 cm AI gauge) from screen pixels
        # into panel pixels and they survive the scale.
        scale, px, py, scaled_w, scaled_h = _panel_screen_fit(sw, sh)
        draw_panel(panel_surf, jet, PANEL_W, PANEL_H, sh, scale)

        screen.fill((0, 0, 0))
        scaled_surf = pygame.transform.scale(panel_surf, (scaled_w, scaled_h))
        # px/py go NEGATIVE where the centre-crop pushes the panel past
        # the screen's edge -- pygame clips the blit, which IS the crop.
        screen.blit(scaled_surf, (px, py))

        # The legend goes on AFTER the scaling, at native resolution -- crisp.
        draw_help_legend(screen, px, py, scaled_w, scaled_h, scale, sh)

        pygame.display.flip()

    bank_flight_hours(jet)  # v78: whatever ended the flight -- landing,
                            # prang, abandon or quit -- her airborne time
                            # joins the career total on the way out
    # v87: and her tale joins the logbook. Each landing was already
    # counted at its own full stop (step); here the FLIGHT banks --
    # the route flown, the streak, the rating, the records.
    if jet.dead:
        bank_flight_end_stats(jet, "crash")
    elif jet.done and not jet.to_routes:
        bank_flight_end_stats(jet, "destination")
    elif jet.done and jet.to_routes:
        bank_flight_end_stats(jet, "stopover")    # [R] from a full stop
    elif jet.to_routes:
        bank_flight_end_stats(jet, "abandon")     # the [Z], confirmed
    else:
        bank_flight_end_stats(jet, "quit")        # ESC / DESKTOP / close
    audio_off()
    return jet.dead, jet.done, jet.quit
# ----------------------------------------------------------------------
#  END SCREENS
# ----------------------------------------------------------------------
def success_screen(screen, sw, sh, fonts, jet):
    clock = pygame.time.Clock()
    running = True
    smooth = max(0, int(600 + jet.touch_vsi))
    score = int(jet.fuel) + smooth
    greaser = "a greaser!" if jet.touch_vsi > -150 else "nice and gentle." if jet.touch_vsi > -350 else "a firm arrival."
    mins = int(jet.elapsed // 60)
    secs = int(jet.elapsed % 60)

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                else:
                    return True
        screen.fill(BG_GREEN)
        render_text(screen, fonts["title"], "*** WELCOME - YOU MADE IT ***", TITLE_GOLD, sw//2, int(sh*0.15), align="center")
        y = int(sh * 0.30)
        gap = int(sh * 0.07)
        render_text(screen, fonts["body"], "Landed at ......... %s" % (jet.landed_name or jet.route["name"].split("-")[1]), TEXT_YELLOW, sw//2, y, align="center")
        y += gap
        render_text(screen, fonts["body"], "Touchdown sink ..... %d fpm (%s)" % (int(jet.touch_vsi), greaser), TEXT_YELLOW, sw//2, y, align="center")
        y += gap
        render_text(screen, fonts["body"], "Fuel remaining ..... %s lb" % format(int(jet.fuel), ","), TEXT_YELLOW, sw//2, y, align="center")
        y += gap
        render_text(screen, fonts["body"], "Flight time ........ %d:%02d" % (mins, secs), TEXT_YELLOW, sw//2, y, align="center")
        y += gap
        render_text(screen, fonts["data"], "Score .............. %d points" % score, TEXT_YELLOW, sw//2, y, align="center")
        prompt_y = int(sh * 0.85)
        pulse = int(128 + 127 * abs(math.sin(pygame.time.get_ticks() / 800)))
        render_text(screen, fonts["prompt"], "Do you want to fly again? Press any key to continue, or [ESC] to quit", (pulse, pulse, pulse), sw//2, prompt_y, align="center")
        pygame.display.flip()


def crash_tip(why):
    """A one-line tip matched to the way she came down."""
    w = why.lower()
    if "gear-up" in w:
        return "TIP: wheels first, always - three greens before touchdown."
    if "hard arrival" in w:
        return "TIP: arrive under 900 fpm - one [W] tap over the fence flares her."
    if "too fast" in w:
        return "TIP: 120-140 kt on final - energy is the enemy of a short runway."
    if "short of the runway" in w:
        return "TIP: undershot - carry a little power all the way to the threshold."
    if "terrain" in w:
        return "TIP: the ground always wins - keep altitude in hand near high country."
    if "too little flap" in w:
        # Checked before "overrun": this crash's own message ends in
        # "overrun!", and the generic overrun tip used to win the match.
        return "TIP: flap 30-40 for landing - it lets her fly slowly and safely."
    if "off the end" in w or "overrun" in w:
        return "TIP: touch down early, then brakes [B] and reverse [R] with power on against the buckets."
    if "stalled onto the runway" in w:
        return "TIP: the wing stops flying below the stall - guard the speed on final."
    if "fuel" in w:
        return "TIP: watch the FUEL counter - land before the tanks run dry."
    return "TIP: Flying School [T] on the intro screen covers every phase."


def rating_verdict(r):
    """The words under the skill rating percentage."""
    if r >= 80:
        return "SUBSTANTIAL IMPROVEMENT - captain material, one moment from glory."
    if r >= 60:
        return "GOOD HANDLING - a sound flight with a hard lesson at the end."
    if r >= 40:
        return "COMPETENT IN PARTS - the fundamentals are clearly forming."
    if r >= 20:
        return "LEARNING - keep practising; Flying School [T] will help."
    return "STUDENT LEVEL - little handling shown this flight."


def flight_review(j):
    """Review the WHOLE flight for the crash debrief. Returns
    (rating, goods, lessons, tip): the rating is a handling percentage
    -- 0% = no plane-handling skill shown, 80%+ = a substantial
    improvement (a crash caps the day at 88); goods and lessons are
    short review lines; tip matches the way she came down."""
    good, lessons = [], []
    score = 8.0      # credit for starting the engines and giving it a go
    air_s = getattr(j, "airborne_time", 0.0)

    # ---------- CREDITS: what the flight showed you can do ----------
    if air_s > 0.0:
        score += 15
        good.append("You got her airborne - the takeoff itself was flown.")
    if getattr(j, "gear_raised", False):
        score += 8
        good.append("Gear came up after takeoff - clean and tidy.")
    if getattr(j, "max_alt", 0.0) > 5000.0:
        score += 8
    if air_s > 120.0:
        score += 8
        good.append("You managed the aircraft in cruise for a good while.")
    if air_s > 60.0 and getattr(j, "offcourse_count", 0) == 0:
        score += 8
        good.append("Navigation was tidy - you held the course line.")
    if getattr(j, "flaps_used", False):
        score += 6
        good.append("Flaps were used at the right speeds - good configuration sense.")
    if getattr(j, "gear_down_low", False):
        score += 8
        good.append("Wheels down low near the field - properly configured to land.")
    if getattr(j, "gs_time", 0.0) > 30.0:
        score += 10
        good.append("You found the glideslope and held it - real instrument work.")
    if air_s > 60.0 and getattr(j, "stall_count", 0) == 0:
        score += 8
        good.append("No stalls - the wing was kept flying all flight.")
    if air_s > 60.0 and (getattr(j, "overspeed_count", 0)
                         + getattr(j, "gear_overspeed_count", 0)
                         + getattr(j, "flap_overspeed_count", 0)) == 0:
        score += 8
        good.append("Speed discipline was sound - no limits busted.")
    if not j.said_empty and air_s > 0.0:
        score += 5

    # ---------- LESSONS: what the flight says to work on ----------
    stalls = getattr(j, "stall_count", 0)
    if stalls:
        score -= 5 * min(stalls, 3)
        lessons.append("Stalled %d time%s - nose down [S], power on, speed is life."
                       % (stalls, "s" if stalls != 1 else ""))
    if getattr(j, "overspeed_count", 0):
        score -= 5 * min(j.overspeed_count, 3)
        lessons.append("Overspeeded the airframe - watch the barber pole at 360 kt.")
    if getattr(j, "gear_overspeed_count", 0):
        score -= 4
        lessons.append("Gear overspeed - slow below 200 kt with the wheels out.")
    if getattr(j, "flap_overspeed_count", 0):
        score -= 4
        lessons.append("Flap overspeed - mind the limits: 230/190/165 kt by setting.")
    terr = getattr(j, "terrain_count", 0)
    if terr:
        score -= 5 * min(terr, 3)
        lessons.append("Terrain warning sounded - give the ground more room.")
    if getattr(j, "offcourse_count", 0) > 0 and air_s > 60.0:
        score -= 3
        lessons.append("Wandered off course - centre the CDI needle now and then.")
    if j.said_empty:
        score -= 10
        lessons.append("Ran the tanks dry - fuel is a promise, not a suggestion.")
    if not getattr(j, "gear_raised", False) and air_s > 60.0:
        score -= 4
        lessons.append("The gear stayed down all flight - drag cost you speed and fuel.")
    if air_s <= 0.0:
        lessons.append("Never left the runway - the takeoff drill is in Flying School [T].")
    elif air_s < 60.0:
        lessons.append("Ended in the first minute - the climb-out needs gentle hands.")

    rating = int(round(max(0.0, min(88.0, score))))
    return rating, good, lessons, crash_tip(j.why)


def crash_screen(screen, sw, sh, fonts, jet):
    """Crash debrief: why she came down, a tip, a review of the whole
    flight, and a skill rating as a percentage -- 0% = no handling
    shown, 80%+ = a substantial improvement. [T] escapes to Flying
    School straight from the debrief (v32)."""
    clock = pygame.time.Clock()
    running = True
    rating, goods, lessons, tip = flight_review(jet)
    verdict = rating_verdict(rating)

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_t:
                    return "tutorial"   # [T]: Flying School, from the prang (v32)
                else:
                    return True
        screen.fill(BG_GREEN)
        render_text(screen, fonts["title"], "*** C R A S H ***", BOX_RED,
                    sw // 2, int(sh * 0.09), align="center")
        render_text(screen, fonts["body"], jet.why, TEXT_YELLOW,
                    sw // 2, int(sh * 0.175), align="center")
        render_text(screen, fonts["small"], tip, TEXT_WHITE,
                    sw // 2, int(sh * 0.218), align="center")

        render_text(screen, fonts["label"], "THE FLIGHT IN REVIEW", TITLE_GOLD,
                    sw // 2, int(sh * 0.285), align="center")
        y = int(sh * 0.33)
        step_y = int(sh * 0.042)
        shown = 0
        for g in goods[:3]:
            render_text(screen, fonts["small"], "+ " + g, BOX_GREEN_L,
                        sw // 2, y, align="center")
            y += step_y
            shown += 1
        for b in lessons[:3]:
            render_text(screen, fonts["small"], "- " + b, BOX_ORANGE,
                        sw // 2, y, align="center")
            y += step_y
            shown += 1
        if shown == 0:
            render_text(screen, fonts["small"],
                        "The flight ended before any handling could be shown.",
                        TEXT_DIM, sw // 2, y, align="center")
            y += step_y

        render_text(screen, fonts["data"], "SKILL RATING: %d%%" % rating,
                    TITLE_GOLD, sw // 2, y + int(sh * 0.035), align="center")
        render_text(screen, fonts["body"], verdict, TEXT_YELLOW,
                    sw // 2, y + int(sh * 0.095), align="center")

        render_text(screen, fonts["small"],
                    "The Learjet is a write-off, but the simulator rebuilds it for free.",
                    TEXT_DIM, sw // 2, int(sh * 0.81), align="center")
        pulse = int(128 + 127 * abs(math.sin(pygame.time.get_ticks() / 800)))
        render_text(screen, fonts["prompt"],
                    "Press any key to try again   |   [T] Flying School   |   [ESC] to quit",
                    (pulse, pulse, pulse), sw // 2, int(sh * 0.88), align="center")
        pygame.display.flip()


# ----------------------------------------------------------------------
#  CLEAN EXIT TO THE DESKTOP (v67) -- one shared shutdown for every way
#  out of the sim: the DESKTOP button, [ESC], or the window's own close
# ----------------------------------------------------------------------
def _close_sublime_text():
    """Ask Sublime Text to close, GRACEFULLY: a WM_CLOSE to each of its
    top-level windows -- the same as clicking its own [X], so it shuts
    down through its normal path and hot-exit keeps the work. Windows
    only; a no-op anywhere else, or if Sublime is not running."""
    if os.name != "nt":
        return
    try:
        import ctypes
        u32 = ctypes.windll.user32
        k32 = ctypes.windll.kernel32
        targets = []

        @ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
        def _each_window(hwnd, _lparam):
            try:
                if u32.IsWindowVisible(hwnd):
                    pid = ctypes.c_ulong(0)
                    u32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
                    hproc = k32.OpenProcess(0x1000, False, pid.value)
                    if hproc:
                        buf = ctypes.create_unicode_buffer(512)
                        buflen = ctypes.c_ulong(512)
                        if k32.QueryFullProcessImageNameW(
                                hproc, 0, buf, ctypes.byref(buflen)):
                            if os.path.basename(buf.value).lower() \
                                    == "sublime_text.exe":
                                targets.append(hwnd)
                        k32.CloseHandle(hproc)
            except Exception:
                pass
            return True

        u32.EnumWindows(_each_window, 0)
        for hwnd in targets:
            u32.PostMessageW(hwnd, 0x0010, 0, 0)    # WM_CLOSE
    except Exception:
        pass


def clean_exit_to_desktop(farewell):
    """THE CLEAN DESK (v67): one tidy shutdown for every exit path --
    the DESKTOP button, [ESC], the window's own close. The mixer is
    silenced and its device released, the pygame window closed, the
    goodbye line printed (guarded: a --windowed .exe has no console, so
    there it simply vanishes), Sublime Text asked to close if it is
    still open, and the process itself ended outright -- so the sim
    always returns cleanly to the desktop, run from Sublime, from a
    terminal, or from the converted single-file .exe."""
    audio_off()
    try:
        pygame.mixer.music.stop()
        pygame.mixer.stop()
        pygame.mixer.quit()
    except Exception:
        pass
    try:
        pygame.quit()
    except Exception:
        pass
    _say("\n" + farewell + "\n")   # v81: the guarded _say -- a --windowed
                                   # .exe has no console, so there the
                                   # goodbye line simply vanishes
    _close_sublime_text()
    os._exit(0)     # the process ends HERE: no lingering mixer thread,
                    # no half-closed window -- straight to the desktop


# ----------------------------------------------------------------------
#  MAIN GAME LOOP
# ----------------------------------------------------------------------
def main():
    screen, sw, sh = init_display()
    audio_init()
    fonts = load_fonts(sh)
    load_career_hours()     # v78: the career flight hours, banked over
                            # every route since installation, ride along
                            # from the moment the sim wakes
    load_stats()            # v87: and the pilot's logbook with them,
                            # for the Introduction screen's career card

    while True:
        result = intro_screen(screen, sw, sh, fonts)
        if not result:
            clean_exit_to_desktop("     Goodbye. Blue skies!")
        if result == "tutorial":
            tut = tutorial_screen(screen, sw, sh, fonts)
            if tut == "quit":
                clean_exit_to_desktop("     Goodbye. Blue skies!")
            continue
        break

    # v83: [F9] pressed at the intro -- resume the saved flight
    # straight from the front door, no Route Selection in between.
    # A failed load simply falls through to the route screen.
    jet = None
    if result == "load":
        jet = load_jet()
        if jet is not None:
            jet.msg = "Saved flight loaded - welcome back!"

    while True:
        if jet is None:
            route = route_screen(screen, sw, sh, fonts)
            if route is None:
                break
            if route == "__LOAD__":
                # Straight back into a saved flight - no briefing needed.
                jet = load_jet()
                if jet is None:
                    continue
                jet.msg = "Saved flight loaded - welcome back!"
            else:
                result = briefing_screen(screen, sw, sh, fonts, route)
                if result == "routes":
                    continue            # v63: [R] at the briefing -- back to
                                        # Route Selection, never leaving the gate
                if not result:
                    break
                jet = Jet(route)
        dead, done, quit_game = flight_hud(screen, sw, sh, fonts, jet)
        to_routes = getattr(jet, "to_routes", False)
        if quit_game:
            break
        if to_routes:
            jet = None
            continue            # [R] at the enroute full-stop prompt (v22):
                                # straight back to Route Selection, no summary
        if dead:
            result = crash_screen(screen, sw, sh, fonts, jet)
            jet = None        # the flight is over; choose a route next
            if result == "tutorial":
                # [T] at the crash screen (v32): straight to Flying
                # School, then back to Route Selection when class is
                # over (a window-close in school still ends the game).
                if tutorial_screen(screen, sw, sh, fonts) == "quit":
                    break
                continue
        elif done:
            result = success_screen(screen, sw, sh, fonts, jet)
            jet = None        # the flight is over; choose a route next
        else:
            break
        if not result:
            break

    clean_exit_to_desktop("     Thanks for flying Learjet.")


if __name__ == "__main__":
    main()