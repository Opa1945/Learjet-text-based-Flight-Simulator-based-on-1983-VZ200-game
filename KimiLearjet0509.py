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
          pyinstaller --onefile --windowed --add-data "learjet_cruise_atmos.mp3;." --add-data "learjet_takeoff.jpg;." learjet_full_panel_2x.py
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

 The flight HUD uses the user's pixel-perfect panel recreation,
 scaled 2x for better visibility, wired to live flight physics.

 Requires: pygame
     pip install pygame

 Run:
     python learjet_full_panel_2x.py
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
CLOCK_BLUE     = (70, 105, 175)    # the shy real-time countdown (v44): a
                                   # dim, shadowy light blue INSIDE the blue
                                   # ETA box -- you barely notice it

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
# recording simply continues undisturbed all the way down. v66: the
# trigger now LEADS the 400 ft mark by
# LANDING_LEAD_S real seconds, flown against the live sink rate and the
# leg's own clock, so the file starts the same few real seconds early on
# every leg, fast machine or slow, 2.9 or 1:1. WAV first, for the same
# codec reason as the roar; the load reports itself on the console.
LANDING_SOUND_CANDIDATES = (
    _resource_candidates("learjet_landing_atmos.wav",
                         r"D:\code\learjet_landing_atmos.wav")
    + _resource_candidates("learjet_landing_atmos.mp3",
                           r"D:\code\learjet_landing_atmos.mp3"))
LANDING_SND_VOL = 0.90    # the landing voice leads the mix, like the roar
LANDING_TRIG_FT = 400.0   # the mark the start leads: this height above
                          # the field ahead
LANDING_LEAD_S = 17.0     # v66: start this many REAL seconds BEFORE the
                          # 400 ft mark; v68 added three, v69 five, v70
                          # four more -- trial and error toward the exact
                          # start. Converted to feet through the live sink
                          # rate and the leg's own clock (jet.time_scale).
                          # THE knob for the recording's timing: nudge it
                          # and fly again.
LANDING_LEAD_MAX_FT = 600.0   # cap on the lead's altitude, so a steep,
                              # fast descent cannot wake the voice
                              # hundreds of feet early. v70: up from 450
                              # -- at the 2.9 clock seventeen real seconds
                              # of a 600-700 fpm final is 493-575 ft of
                              # altitude, and the old cap silently handed
                              # back the very seconds being added
LANDING_REARM_GAP_FT = 100.0  # the go-around re-arm rides this far ABOVE
                              # the (now moving) trigger -- a fixed 550 ft
                              # could fall BELOW a led trigger, and one
                              # small wobble on short final would silence
                              # the voice for the rest of the approach

# ----------------------------------------------------------------------
#  PYGAME SETUP
# ----------------------------------------------------------------------
def init_display():
    # Ask Windows for the display's TRUE physical pixels before the
    # window exists. Without DPI awareness, a desktop running at 125% /
    # 150% scaling bitmap-stretches the game window: everything gets a
    # little blurry, and no pixel maths can make a "quarter inch" gap
    # measure a real quarter inch. (No-op off Windows.)
    try:
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(2)   # per-monitor aware
    except Exception:
        try:
            import ctypes
            ctypes.windll.user32.SetProcessDPIAware()    # Vista+ fallback
        except Exception:
            pass
    try:
        pygame.mixer.pre_init(44100, -16, 2, 512)
    except Exception:
        pass
    pygame.init()
    pygame.display.set_caption("Learjet 35A Flight Simulator")
    info = pygame.display.Info()
    sw, sh = info.current_w, info.current_h
    try:
        screen = pygame.display.set_mode((sw, sh), pygame.FULLSCREEN | pygame.DOUBLEBUF)
    except Exception:
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
                scale = max(sw / img.get_width(), sh / img.get_height())
                new_size = (max(1, int(img.get_width() * scale)),
                            max(1, int(img.get_height() * scale)))
                img = pygame.transform.smoothscale(img, new_size)
                x = (img.get_width() - sw) // 2
                y = (img.get_height() - sh) // 2
                return img.subsurface((x, y, sw, sh)).copy()
        except Exception:
            pass
    return None


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

    # Text colours: title and prompt stay dark blue as originally designed;
    # the rest is white over the photo backdrop, dark grey on the white panel.
    TEXT_SOFT = WHITE if photo_bg is not None else DARK_GREY

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
                return True           # any other key = continue

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
                    sw // 2, sub_y + int(sh * 0.035), align="center")
        render_text(screen, fonts["tiny"], "Managed by J Vromans", TEXT_SOFT,
                    sw // 2, sub_y + int(sh * 0.055), align="center")

        # Centred art (old layout only, when no photo file is found)
        jet_y = sub_y + int(sh * 0.08)
        if jet_surface is not None:
            jet_alpha = min(255, jet_alpha + jet_fade_speed)
            jet_surface.set_alpha(jet_alpha)
            jet_x = (sw - jet_width) // 2
            screen.blit(jet_surface, (jet_x, jet_y))

        # Info line
        info_y = jet_y + art_height + int(sh * 0.06)
        render_text(screen, fonts["body"], "Python 3.11  —  no extra libraries needed  —  run from terminal or double-click",
                    TEXT_SOFT, sw // 2, info_y, align="center")

        # Prompt box at bottom
        prompt_y = box_y + box_h - int(sh * 0.10)
        prompt_text = "Press any key to begin ..."

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
        hint_y = min(prompt_y + CM2, int(sh * 0.90))
        render_text(screen, fonts["small"], "New to the Learjet? Press [T] for Flying School - no experience needed.",
                    TEXT_YELLOW, sw // 2, offer_y, align="center")

        # Small hint
        render_text(screen, fonts["small"], "[T] tutorial  |  [ESC] to quit", TEXT_SOFT, sw // 2, hint_y, align="center")

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
            "Use [N] or [SPACE] for the next page, [P] to go back, [ESC] to leave school.",
        ]),
        ("YOUR OFFICE - WHAT THE BOXES MEAN", [
            "IAS: airspeed in knots. Near the ground, too slow is the real danger.",
            "ALT: altitude in feet. VSI: vertical speed in feet per minute, up or down.",
            "THRUST: engine power. FLAP: lift and drag. GEAR: wheels. Three greens = down.",
            "DME: distance. GROUND SPEED: speed over the ground.",
            "ETA: time to the field the DME is tuned to.",
            "> REAL TIME legs: the ETA and the dim blue clock beneath it read the SAME time.",
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
            "The Enroute picture [V] shows the route as a dashed line. The red square is you.",
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

        screen.fill(BG_GREEN)
        draw_box(screen, BOX_GREEN, box_x, int(sh * 0.05), box_w, int(sh * 0.88), radius=12)
        title_text = "YOUR CHOICE OF ROUTE ?"
        render_text(screen, fonts["title"], "*   " + title_text + "   *", TITLE_GOLD, sw // 2, title_y, align="center")
        draw_box(screen, BOX_GREEN, route_box_x, route_box_y, route_box_w, route_box_h, border=8, border_colour=BORDER_BLUE, radius=4)

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
            render_text(screen, fonts["route"], key_text, TEXT_YELLOW, col_key, y, align="left")
            render_text(screen, fonts["route"], name_text, TEXT_YELLOW, col_name, y, align="left")
            render_text(screen, fonts["route"], dots, TEXT_YELLOW, dots_start_x, y, align="left")
            render_text(screen, fonts["route"], dist_text, TEXT_YELLOW, col_dist, y, align="right")

        render_text(screen, fonts["hint"], "Press the letter of your chosen route  |  [ESC] to quit",
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

    # Silence the cockpit while the map is up: the engine hum, wind rush
    # and stall buzzer all fall quiet for the duration. When you return
    # to the HUD, audio_update() restores every loop on its next frame,
    # so the engine is heard again the moment you're back in the seat.
    audio_off()

    _blink_buzz_on = False   # tracks the buzzer tied to the blinking square

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop_blink_buzz()
                return False
            if event.type == pygame.KEYDOWN:
                stop_blink_buzz()       # never leave the buzzer sounding
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
            pygame.draw.rect(screen, BG_GREEN, sr)     # erase dashes behind
            screen.blit(star_img, (sr.centerx - star_ink.centerx,
                                   line_y - star_ink.centery))

        # Red square on the line at the aircraft's position, blinking
        # steadily: on for half a second, off for half a second.
        # progress 0.0 = extreme left (start), 1.0 = extreme right (arrival)
        frac = max(0.0, min(1.0, progress))
        sq = int(star_w * 1.2)
        sq_x = int(line_left + frac * line_span - sq / 2)
        # Off-course drift: while viewing from the cockpit with [V], the
        # red square rides ABOVE or BELOW the dashed line by the
        # aircraft's cross-track error (full drift at 2 nm off course),
        # so you can see at a glance how the navigation is going.
        sq_drift = 0
        if in_flight:
            sq_drift = int(max(-1.0, min(1.0, getattr(jet, "xte", 0.0) / 2.0)) * sh * 0.06)
        sq_y = line_y - sq_drift - sq // 2
        square_on = (pygame.time.get_ticks() // 500) % 2 == 0
        if square_on:
            pygame.draw.rect(screen, BOX_RED, (sq_x, sq_y, sq, sq))

        # Buzz with the blink: the buzzer sounds the moment the red
        # square comes ON and falls silent the moment it goes OFF,
        # chirping along with the flash. Respects the [M] mute.
        if square_on != _blink_buzz_on:
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
            render_text(screen, fonts["small"],
                        "OFF COURSE: %.1f nm %s of track" % (abs(jet.xte), side),
                        BOX_RED, sw // 2, line_y + int(sh * 0.05), align="center")

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
# are sim-seconds: one possible failure every 20-70 sim-minutes aloft.
CAB_PRESS_MIN_S = 20.0 * 60.0
CAB_PRESS_MAX_S = 70.0 * 60.0

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
            and apt["name"] not in j.al_done):
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
SAVE_PATH = os.path.join(_exe_dir(), "learjet_save.json")  # v42: beside the
                         # .exe when frozen -- __file__ would point inside
                         # PyInstaller's throwaway unpack folder and every
                         # save would vanish on exit


def save_jet(jet):
    """Write the whole flight -- route plus every piece of the jet's
    state -- to the save file. Returns True on success."""
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
    Also load the cabin-atmosphere recording (v41) onto the music stream
    and set it looping silently -- audio_update() raises it for each
    flight. Any audio trouble and the whole game simply stays silent."""
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
        # The cruise atmosphere (v41): stream the real recording on the
        # music channel, looping forever at volume 0 -- audio_update()
        # raises it while a flight is live and lowers it afterwards.
        # Missing or undecodable file: the flag stays False and the
        # synthesised v8 cruise voice carries on as the fallback.
        _cruise_music_ok = False
        for path in CRUISE_SOUND_CANDIDATES:
            try:
                if path and os.path.exists(path):
                    pygame.mixer.music.load(path)
                    pygame.mixer.music.set_volume(0.0)
                    pygame.mixer.music.play(-1)   # loops for the session
                    _cruise_music_ok = True
                    break
            except Exception:
                pass
        # The takeoff roar (v62): load the trimmed takeoff recording
        # onto its reserved channel's sound. The load REPORTS itself on
        # the console now -- a missing or undecodable file used to fail
        # in silence. Any trouble: the flag stays False and the
        # ambience carries the takeoff as before.
        _takeoff_snd_ok = False
        for path in TAKEOFF_SOUND_CANDIDATES:
            try:
                if path and os.path.exists(path):
                    SND["takeoff"] = pygame.mixer.Sound(file=path)
                    _takeoff_snd_ok = True
                    print("Takeoff sound loaded: %s" % path)
                    break
            except Exception as exc:
                print("Takeoff sound would not load from %s (%s)"
                      % (path, exc))
        if not _takeoff_snd_ok:
            print("TAKEOFF SOUND NOT LOADED -- looked in:")
            for path in TAKEOFF_SOUND_CANDIDATES:
                print("    %s  %s" % (path, "(found)"
                      if os.path.exists(path) else "(missing)"))
        # The landing voice (v63): the landing recording, looping from
        # the led 400 ft mark above the field (v66) until the wheels
        # stop. Same codec note
        # as the roar -- WAV first, MP3 welcome; the load reports
        # itself on the console either way.
        _landing_snd_ok = False
        for path in LANDING_SOUND_CANDIDATES:
            try:
                if path and os.path.exists(path):
                    SND["landing"] = pygame.mixer.Sound(file=path)
                    _landing_snd_ok = True
                    print("Landing sound loaded: %s" % path)
                    break
            except Exception as exc:
                print("Landing sound would not load from %s (%s)"
                      % (path, exc))
        if not _landing_snd_ok:
            print("LANDING SOUND NOT LOADED -- looked in:")
            for path in LANDING_SOUND_CANDIDATES:
                print("    %s  %s" % (path, "(found)"
                      if os.path.exists(path) else "(missing)"))
        AUDIO_OK = True
    except Exception:
        AUDIO_OK = False


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
                # wake the voice hundreds of feet early. A level or
                # near-level approach keeps the old 400 ft mark.
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


def stop_blink_buzz():
    """Make sure the Enroute screen's blink buzzer is left silent
    (called as the screen is exited). The cockpit's audio_update()
    will set the buzzer channel correctly again on the next frame."""
    if AUDIO_OK:
        try:
            _ch_buzz.set_volume(0.0)
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
        if not j.engines:
            # v26: no engines, no thrust -- the lever used to wind up to
            # 100% on the gauge with the engines dead (and nothing
            # moving); the request is now refused with a reminder.
            j.msg = "Engines are off - start them [E] first."
        elif (not j.airborne and not j.rollout
                and not getattr(j, "free_departure", False)
                and not on_obs(j)):
            # v24: an attempt to roll before HDG matches OBS earns a
            # CHECK HEADING reminder at INFO -- turn her with [A]/[D]
            # first, the engines idling.
            j.msg = "CHECK HEADING - HDG %03d, OBS %03d: no thrust until they match. Turn [A]/[D]." % (
                int(j.hdg) % 360,
                int(getattr(j, "obs", float(j.route["hdg"]))) % 360)
        else:
            j.thrust = max(0.0, min(100.0, j.thrust + 5.0))
            if "CHECK HEADING" in j.msg:
                j.msg = ""        # lined up now -- retire the reminder
            if (j.thrust >= 100.0 and not j.airborne and not j.rollout
                    and not j.reverser):
                # v62: 100% selected for the takeoff roll -- the roar
                # starts NOW. The landing rollout is excluded: there
                # [+] winds the reversers, not the takeoff.
                play_takeoff_sound(j)
    elif k in ("-", "_"):
        j.thrust = max(0.0, min(100.0, j.thrust - 5.0))
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
#  PIXEL-PERFECT PANEL DRAWING  --  2X SCALED
# ==============================================================================

# 2X scaled fonts
_panel_font = None
_panel_small_font = None
_panel_big_font = None
_panel_tiny_font = None

BORDER_THICK = 16  # was 8, now 2x

# Clickable rects on the HUD (panel coordinates), filled in by draw_panel
PANEL_BUTTONS = {}


def _init_panel_fonts():
    global _panel_font, _panel_small_font, _panel_big_font, _panel_tiny_font
    _panel_font = pygame.font.SysFont("consolas", 44)       # was 22
    _panel_small_font = pygame.font.SysFont("consolas", 36)  # was 18
    _panel_big_font = pygame.font.SysFont("consolas", 88)    # was 44
    _panel_tiny_font = pygame.font.SysFont("consolas", 24)   # was 12


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


def _draw_text_fit(surf, txt, x, y, right_edge, color=PANEL_WHITE):
    """Draw txt at (x, y) in the panel font -- unless it would run past
    right_edge, in which case set it in the largest smaller size that
    fits, vertically centred on the normal text line. Lines that fit
    are drawn exactly as before."""
    img = _panel_font.render(txt, True, color)
    if x + img.get_width() <= right_edge:
        surf.blit(img, (x, y))
        return img.get_rect(topleft=(x, y))
    size = 44
    small = img
    while size > 20:
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


def _draw_diag_shape(surf, x, y, on_color=PANEL_YELLOW, off_color=(0, 0, 0), flip=False):
    char_w, char_h = _panel_font.size("A")
    w2 = char_w // 2
    h2 = char_h // 2
    tl = pygame.Rect(x,         y,         w2, h2)
    tr = pygame.Rect(x + w2,    y,         char_w - w2, h2)
    bl = pygame.Rect(x,         y + h2,    w2, char_h - h2)
    br = pygame.Rect(x + w2,    y + h2,    char_w - w2, char_h - h2)
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
    char_w, char_h = _panel_font.size("A")
    x0 = box.centerx - (n_cells * char_w) // 2
    y0 = box.centery - char_h // 2
    for i in range(n_cells):
        _draw_diag_shape(surf, x0 + i * char_w, y0,
                         PANEL_WHITE, (0, 0, 0), flip=False)

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

    BLACK  = (0, 0, 0)
    SKY    = (0x4c, 0xbc, 0xd6)
    GROUND = (0x9e, 0x78, 0x4f)
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


def draw_panel(surf, jet, WIDTH=2000, HEIGHT=1200, sh=1080, scale=1.0):
    """Draw the 2X scaled pixel-perfect Learjet panel."""
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
    # v52: the wind on every field of the route blows straight down the
    # course line -- direction = route track + 180 -- so she always
    # arrives (and departs) heading right into it. v68: the SPEED shown
    # is a per-airport show figure now, picked up at the INFO line below
    # where the tuned airport is known (see surface_wind_show).
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

    surf.fill(PANEL_GREEN)

    # ---------- OUTER FRAME ----------
    panel_rect = pygame.Rect(50, 50, WIDTH - 100, HEIGHT - 100)  # balanced margins
    pygame.draw.rect(surf, PANEL_BLUE, panel_rect, BORDER_THICK)

    LEFT_INSET = 38  # was 19
    inner_left = panel_rect.x + LEFT_INSET
    inset = inner_left - panel_rect.x
    inner_right = panel_rect.right - inset

    # Pre-compute character size for shift calculations
    char_w, char_h = font.size("A")

    # ----------------------------------------------------------------------
    #  LEFT-BLOCK SHIFT for Attitude Indicator space
    # ----------------------------------------------------------------------
    # The left block (IAS, ALT, ASS FL, DME/G/S/ETA row, and the lower
    # section down to INFO) shifts left so the gap from the inside edge
    # of the left blue border to the IAS box is exactly a quarter inch.
    # The right block (BR, ITT, THRUST, GEAR, *D) stays at its original
    # absolute positions; the FLAP gauge, the G/S tape and the attitude
    # indicator are laid out as one group in the band between the ETA
    # box and the THRUST system's left purple bar (see the Elevation /
    # G/S / FLAP band below).
    # ----------------------------------------------------------------------
    _ias_w, _ias_h = 320, 160
    _alt_w = 520
    _ass_w = 320
    _br_w, _br_h = 120, 48
    _orig_gap = (inner_right - inner_left - (_ias_w + _alt_w + _ass_w + _br_w)) / 5.0 * 0.6
    _orig_ias_x = int(inner_left + _orig_gap)
    _orig_alt_x = int(_orig_ias_x + _ias_w + _orig_gap)
    _orig_ass_x = int(_orig_alt_x + _alt_w + _orig_gap)
    _orig_br_x = int(_orig_ass_x + _ass_w + _orig_gap)
    _orig_eta_right = _orig_ass_x + _ias_w

    # Physical sizes are wanted on the SCREEN, but everything here is
    # drawn in panel pixels and the panel is blitted scaled down by
    # `scale` -- so a physical size in screen pixels is divided by the
    # scale to size it in panel pixels (phys = the conversion factor).
    phys = 1.0 / max(scale, 0.2)
    # Quarter-inch physical gap from the inside blue border (0.635 cm)
    qtr_inch = cm_px(sh, 0.635) * phys
    _target_ias_x = panel_rect.left + BORDER_THICK + qtr_inch
    LEFT_SHIFT = int(round(_target_ias_x - _orig_ias_x))

    # Right block: quarter-inch gap from the right blue border.
    # Right block: quarter-inch gap from the right blue border.
    # Trace the original (unshifted) right block using the EXACT same
    # geometry as the drawing code below to find where *D ends up.
    _orig_rgn_left = _orig_eta_right + 40
    _orig_rgn_right = inner_right - 40
    _orig_rgn_mid = (_orig_rgn_left + _orig_rgn_right) // 2
    _orig_thr_cx = (_orig_rgn_mid + _orig_rgn_right) // 2 + 2 * char_w
    _orig_thr_x = int(_orig_thr_cx - font.size("THRUST")[0] // 2)
    _t_w = font.size("T")[0]
    _pct_x = _orig_thr_x + _t_w
    _pct_y = panel_rect.y + 400 + 2 * font.get_linesize() + 2 * font.get_linesize() - 8
    _pct_img = font.render("100%", True, PANEL_WHITE)
    _pct_rect = _pct_img.get_rect(topleft=(_pct_x, _pct_y))
    # The drawing code re-centres on the % of the 100% mark before
    # placing the 0% mark (thr_center_x is reassigned there). Mirror
    # that here -- tracing from _orig_thr_cx lands the right block two
    # characters too far right, so the *D light all but touches the
    # blue border and the quarter-inch gap vanishes.
    _pct_cx = _pct_x + font.size("100")[0] + font.size("%")[0] // 2
    _zero_x = _pct_cx - (font.size("0")[0] + font.size("%")[0] / 2)
    _zero_y = _pct_rect.bottom + 4 + small_font.get_linesize() + 8
    _zero_img = font.render("0%", True, PANEL_WHITE)
    _zero_rect = _zero_img.get_rect(topleft=(_zero_x, _zero_y))
    _content_left = _pct_x
    _content_right = _zero_x + _zero_img.get_width()
    _lbx = _content_left - 20 - 56
    _rbx = _content_right + 20
    _mbb = (_lbx + 56 + _rbx) / 2
    _rth_x = int(_mbb - font.size("R/TH")[0] / 2)
    # Door rect right edge: e_rect(56) + new2_rect(56) + 10 + door_rect(56)
    _bar_w = 56
    _door_right = _rth_x + 3 * _bar_w + 10
    _right_target = panel_rect.right - BORDER_THICK - qtr_inch
    RIGHT_SHIFT = int(round(_right_target - _door_right))
    # ----------------------------------------------------------------------

    # ---------- TOP STATUS ROW ----------
    stall_text = "STALL"
    tmp = font.render(stall_text, True, PANEL_WHITE)
    tw, th = tmp.get_size()
    pad_x, pad_y = 16, 8  # was 8,4

    TOP_GAP = 20 + font.get_linesize()  # one blank row under the top blue border
    stall_y = panel_rect.y + TOP_GAP

    stall_w = tw + 2 * pad_x
    box_h = th + 2 * pad_y

    space_w, _ = font.size(" ")
    digit_w, _ = font.size("1")
    digit_box_w = digit_w + 6 * space_w

    cab_text = "CAB PRESS"
    cab_w, cab_h = font.size(cab_text)
    cab_pad_x = 20  # was 10
    cab_box_w = cab_w + 2 * cab_pad_x

    total_boxes_w = stall_w + digit_box_w + digit_box_w + cab_box_w

    margin_left = inner_left
    margin_right = inner_right
    gap = (margin_right - margin_left - total_boxes_w) / 5.0

    stall_x = margin_left + gap
    stall_rect = pygame.Rect(int(stall_x), stall_y, stall_w, box_h)

    box1_x = stall_rect.right + gap
    box1 = pygame.Rect(int(box1_x), stall_y, digit_box_w, box_h)

    box2_x = box1.right + gap
    box2 = pygame.Rect(int(box2_x), stall_y, digit_box_w, box_h)

    box3_x = box2.right + gap
    box3 = pygame.Rect(int(box3_x), stall_y, cab_box_w, box_h)

    # STALL box (thick border kept; corners rounded to match the IAS box)
    if stall:
        pygame.draw.rect(surf, PANEL_RED, stall_rect, border_radius=24)
        pygame.draw.rect(surf, PANEL_YELLOW, stall_rect, BORDER_THICK, border_radius=24)
        _draw_text(surf, stall_text, stall_rect.x + pad_x, stall_rect.y + pad_y, PANEL_WHITE)
    else:
        pygame.draw.rect(surf, PANEL_BLUE, stall_rect, BORDER_THICK, border_radius=24)
        _draw_text(surf, stall_text, stall_rect.x + pad_x, stall_rect.y + pad_y, PANEL_YELLOW)

    # Engine 1 and 2 indicators
    eng1_active = engines and jet.n1 > 50
    eng2_active = engines and jet.n1 > 50
    pygame.draw.rect(surf, PANEL_YELLOW if eng1_active else PANEL_BLUE, box1, BORDER_THICK, border_radius=24)
    pygame.draw.rect(surf, PANEL_YELLOW if eng2_active else PANEL_BLUE, box2, BORDER_THICK, border_radius=24)
    # CAB PRESS: normally a plain blue-bordered box. While the warning
    # burns, its dark face FLASHES red (half-second cadence, like the
    # Enroute screen's blinking square) until the jet is below 10,000 ft.
    if getattr(jet, "cab_light", False) and (pygame.time.get_ticks() // 500) % 2 == 0:
        pygame.draw.rect(surf, PANEL_RED, box3, border_radius=24)
    pygame.draw.rect(surf, PANEL_BLUE, box3, BORDER_THICK, border_radius=24)

    _draw_text(surf, "1", box1.x + (digit_box_w - digit_w) // 2, box1.y + pad_y, PANEL_YELLOW)
    _draw_text(surf, "2", box2.x + (digit_box_w - digit_w) // 2, box2.y + pad_y, PANEL_YELLOW)
    _draw_text(surf, cab_text, box3.x + cab_pad_x, box3.y + pad_y, PANEL_YELLOW)

    # ---------- SAVE / LOAD / PAUSE / DESKTOP BUTTONS (top-right) ----------
    # Clickable with the mouse, or [F5] to save and [F9] to load.
    btn_font = pygame.font.SysFont("consolas", 28, bold=True)
    btn_w = btn_font.size("LOAD GAME")[0] + 28
    btn_h = btn_font.get_linesize() + 12
    save_btn = pygame.Rect(0, 0, btn_w, btn_h)
    save_btn.right = inner_right - 20
    save_btn.top = stall_y
    load_btn = pygame.Rect(0, 0, btn_w, btn_h)
    load_btn.right = inner_right - 20
    load_btn.top = save_btn.bottom + 10
    # PAUSE button under them: turns orange and reads RESUME while paused.
    paused = getattr(jet, "paused", False)
    pause_btn = pygame.Rect(0, 0, btn_w, btn_h)
    pause_btn.right = inner_right - 20
    pause_btn.top = load_btn.bottom + 10
    # DESKTOP button at the foot of the stack (v65). v73: now with the
    # double-check -- the first click only MAKES the offer (the button
    # itself becomes the flashing placard); a second click confirms.
    desktop_btn = pygame.Rect(0, 0, btn_w, btn_h)
    desktop_btn.right = inner_right - 20
    desktop_btn.top = pause_btn.bottom + 10
    for rect, label in ((save_btn, "SAVE GAME"), (load_btn, "LOAD GAME"),
                        (pause_btn, "RESUME" if paused else "PAUSE")):
        face = PANEL_ORANGE if (rect is pause_btn and paused) else PANEL_YELLOW
        pygame.draw.rect(surf, face, rect)
        pygame.draw.rect(surf, PANEL_BLUE, rect, 4)
        _draw_text_centered(surf, label, rect, PANEL_BLUE, btn_font)
    # The DESKTOP button draws on its own now: while its offer is on the
    # table (v73) it flashes on the ABANDON placard's half-second cadence,
    # asking for the second, confirming click.
    if getattr(jet, "desktop_offer", False):
        flash = (pygame.time.get_ticks() // 500) % 2 == 0
        dk_face = PANEL_RED if flash else PANEL_ORANGE
        dk_text = PANEL_WHITE if flash else PANEL_BLUE
        pygame.draw.rect(surf, dk_face, desktop_btn)
        pygame.draw.rect(surf, PANEL_BLUE, desktop_btn, 4)
        _draw_text_centered(surf, "DESKTOP?", desktop_btn, dk_text, btn_font)
    else:
        pygame.draw.rect(surf, PANEL_YELLOW, desktop_btn)
        pygame.draw.rect(surf, PANEL_BLUE, desktop_btn, 4)
        _draw_text_centered(surf, "DESKTOP", desktop_btn, PANEL_BLUE, btn_font)
    PANEL_BUTTONS.clear()
    PANEL_BUTTONS["save"] = save_btn
    PANEL_BUTTONS["load"] = load_btn
    PANEL_BUTTONS["pause"] = pause_btn
    PANEL_BUTTONS["desktop"] = desktop_btn

    # [Z] ABANDON offer (v24): while the first [Z] is on the table, a
    # flashing placard asks for the second [Z] -- and is itself clickable
    # to confirm. With the DESKTOP button now at the foot of the stack
    # (v65) the placard moves to the DESKTOP row, immediately to the
    # button's left -- the band directly under the stack belongs to the
    # ITT label, so the ITT 1/2 spacing is untouched. Half-second
    # cadence, like the CAB PRESS warning and the Enroute screen's
    # blinking square.
    if getattr(jet, "abandon_offer", False):
        abandon_btn = pygame.Rect(0, 0, btn_w, btn_h)
        abandon_btn.right = desktop_btn.left - 10
        abandon_btn.top = desktop_btn.top
        flash = (pygame.time.get_ticks() // 500) % 2 == 0
        ab_face = PANEL_RED if flash else PANEL_ORANGE
        ab_text = PANEL_WHITE if flash else PANEL_BLUE
        pygame.draw.rect(surf, ab_face, abandon_btn)
        pygame.draw.rect(surf, PANEL_BLUE, abandon_btn, 4)
        _draw_text_centered(surf, "ABANDON? Z", abandon_btn, ab_text, btn_font)
        PANEL_BUTTONS["abandon"] = abandon_btn

    # Keep +HDG+ in its original position so only the status rectangles
    # move down; the main rows below stay exactly where they were.
    # Keep HDG in its original position; use the three positions to the
    # right for the aircraft's current heading, followed by a degree
    # symbol -- no asterisks any more, and the same single space
    # between label and output as the OBS readout beside it.
    hdg_readout = "%03d" % (int(jet.hdg) % 360)
    obs_readout = "%03d" % (int(getattr(jet, "obs", float(jet.route["hdg"]))) % 360)
    # One blank row above the HDG line (the extra get_linesize()).
    # The OBS course readout sits alongside the heading, the two centred
    # as a pair so the line stays balanced across the panel.
    # Each part gets its own thin white rounded margin border, using the
    # same corner curves as the gauge boxes below (4 px white, radius 20).
    hdg_part = "HDG " + hdg_readout + "\u00b0"
    obs_part = "OBS " + obs_readout + "\u00b0"
    hdg_w, _ = font.size(hdg_part)
    obs_w, _ = font.size(obs_part)
    gap_w, _ = font.size("   ")
    nav_total = hdg_w + gap_w + obs_w
    nav_x = panel_rect.x + panel_rect.width // 2 - nav_total // 2
    nav_y = panel_rect.y + 20 + box_h + 8 + 2 * font.get_linesize()
    nav_pad_x, nav_pad_y = 18, 8
    hdg_txt_rect = _draw_text(surf, hdg_part, nav_x, nav_y, PANEL_YELLOW)
    obs_txt_rect = _draw_text(surf, obs_part, nav_x + hdg_w + gap_w, nav_y, PANEL_YELLOW)
    for txt_rect in (hdg_txt_rect, obs_txt_rect):
        nav_border = txt_rect.inflate(2 * nav_pad_x, 2 * nav_pad_y)
        pygame.draw.rect(surf, PANEL_WHITE, nav_border, 4, border_radius=20)

    # Flashing P A U S E D placard in the blank row between the status
    # boxes and the *HDG* line (panel font, so it fits the band exactly).
    if paused and (pygame.time.get_ticks() // 400) % 2 == 0:
        pz_img = font.render("P A U S E D", True, PANEL_ORANGE)
        pz_rect = pz_img.get_rect(center=(panel_rect.centerx,
                                          panel_rect.y + 20 + box_h + 8 + int(1.4 * font.get_linesize())))
        surf.blit(pz_img, pz_rect)

    # ---------- MAIN ROW LAYOUT ----------
    ias_w, ias_h = 320, 160       # was 160,80
    alt_w = 520                   # was 260 (height shares ias_h)
    ass_w = 320                   # was 160 (height shares ias_h)
    br_w, br_h = 120, 48          # was 60,24

    # Left block shifted; right block pinned at original coordinates.
    # The gaps BETWEEN the instrument rectangles are all the same
    # quarter inch as the IAS box to the left blue border: IAS-ALT and
    # ALT-ASS FL, and -- because the DME/G/S/ETA row hangs off the same
    # x positions -- DME-G/S and G/S-ETA too. Four narrow gaps in all.
    ias_x = _orig_ias_x + LEFT_SHIFT
    alt_x = ias_x + ias_w + qtr_inch
    ass_x = alt_x + ias_w + qtr_inch
    br_x = _orig_br_x             # right block: do not shift

    itt_x = br_x + br_w + 80      # was +40

    TOP_GAP = 20
    # Two extra text rows: one above *HDG*, one blank row below it.
    label_y = panel_rect.y + TOP_GAP + box_h + 30 + 70 + 2 * font.get_linesize()

    # ---------- IAS ----------
    ias_box = pygame.Rect(ias_x, label_y + 30, ias_w, ias_h)  # was +20
    pygame.draw.rect(surf, PANEL_BLUE, ias_box, border_radius=24)  # was 12
    inset_ias = 6  # was 3
    ias_inner = ias_box.inflate(-2 * inset_ias, -2 * inset_ias)
    pygame.draw.rect(surf, PANEL_WHITE, ias_inner, 4, border_radius=20)  # was 2,10

    # v53: the title sits as far above its rectangle as the titles of the
    # row below sit above theirs -- its line ends right at the box top.
    _draw_text(surf, "IAS", ias_box.centerx - font.size("IAS")[0] // 2,
               ias_box.top - font.get_linesize(), PANEL_YELLOW)

    # The IAS/MACH changeover (v38): in Mach mode the readout reports
    # the Mach number ("0.57") and the unit badge reads MACH in a
    # smaller face so the word fits the badge; otherwise the familiar
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
    num_rect.centerx = ias_box.centerx - 20  # was -10

    num_bg = pygame.Rect(num_rect.x - 8, num_rect.y - 8, num_rect.width + 16, num_rect.height + 16)  # was -4,+8
    pygame.draw.rect(surf, PANEL_BLUE, num_bg, border_radius=8)  # was 4
    surf.blit(num_img, num_rect.topleft)

    k_img = unit_f.render(unit_txt, True, PANEL_BLUE)
    k_rect = k_img.get_rect()
    k_rect.midleft = (num_rect.right + 16, num_rect.centery)  # was +8
    k_bg = pygame.Rect(k_rect.x - 4, k_rect.y - 4, k_rect.width + 8, k_rect.height + 8)  # was -2,+4
    pygame.draw.rect(surf, PANEL_YELLOW, k_bg, border_radius=8)  # was 4
    surf.blit(k_img, k_rect.topleft)

    # ---------- ALT ----------
    alt_box = pygame.Rect(alt_x, label_y + 30, ias_w, ias_h)
    pygame.draw.rect(surf, PANEL_BLUE, alt_box, border_radius=24)
    inset_alt = 6
    alt_inner = alt_box.inflate(-2 * inset_alt, -2 * inset_alt)
    pygame.draw.rect(surf, PANEL_WHITE, alt_inner, 4, border_radius=20)

    _draw_text(surf, "ALT", alt_box.centerx - font.size("ALT")[0] // 2,
               alt_box.top - font.get_linesize(), PANEL_YELLOW)

    alt_int = int(altitude_ft)
    thousands = alt_int // 1000
    remainder = alt_int % 1000

    # Below 1,000 ft: keep the two black/white graphics. At/above 1,000 ft:
    # replace them with the thousands number (no leading zero) and show only
    # the last three digits after the comma. Dropping below 1,000 restores the
    # graphics automatically through this same branch.
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

    lead_w = 2 * char_w
    digits_w = num_alt_img.get_width()
    comma_w = comma_img.get_width()
    ft_w = ft_img.get_width() + 8  # was +4

    gap_diag_comma = 2    # was 8 (v71): the comma already owns a full
    gap_comma_digits = 4  # monospace cell -- 8 px each side read roomy
    gap_digits_ft = 12    # was 6

    total_w = (lead_w + gap_diag_comma + comma_w + gap_comma_digits + digits_w + gap_digits_ft + ft_w)

    start_x = alt_box.centerx - total_w // 2
    center_y = alt_box.centery
    cell_top = center_y - char_h // 2

    x_lead = start_x
    x_comma = x_lead + lead_w + gap_diag_comma
    x_digits = x_comma + comma_w + gap_comma_digits
    x_ft_bg = x_digits + digits_w + gap_digits_ft

    if lead_img is not None:
        lead_rect = lead_img.get_rect()
        lead_rect.midright = (x_lead + lead_w, center_y)
        surf.blit(lead_img, lead_rect.topleft)
    else:
        _draw_diag_shape(surf, x_lead, cell_top, on_color=PANEL_WHITE, off_color=(0, 0, 0))
        _draw_diag_shape(surf, x_lead + char_w, cell_top, on_color=PANEL_WHITE, off_color=(0, 0, 0))

    comma_rect = comma_img.get_rect()
    comma_rect.midleft = (x_comma, center_y)
    surf.blit(comma_img, comma_rect.topleft)

    num_alt_rect = num_alt_img.get_rect()
    num_alt_rect.midleft = (x_digits, center_y)
    surf.blit(num_alt_img, num_alt_rect.topleft)

    ft_rect = ft_img.get_rect()
    ft_rect.midleft = (x_ft_bg + 4, center_y)  # was +2
    ft_bg = pygame.Rect(x_ft_bg, ft_rect.top - 4, ft_img.get_width() + 8, ft_img.get_height() + 8)  # was -2,+4
    pygame.draw.rect(surf, PANEL_YELLOW, ft_bg, border_radius=8)  # was 4
    surf.blit(ft_img, ft_rect.topleft)

    # ---------- ASS FL ----------
    # ass_x comes from the main-row layout: one quarter inch right of ALT.
    ass_box_outer = pygame.Rect(ass_x, label_y + 30, ias_w, ias_h)
    pygame.draw.rect(surf, PANEL_BLUE, ass_box_outer, border_radius=24)
    inset_ass = 6
    ass_inner = ass_box_outer.inflate(-2 * inset_ass, -2 * inset_ass)
    pygame.draw.rect(surf, PANEL_WHITE, ass_inner, 4, border_radius=20)

    _draw_text(surf, "ASS FL", ass_box_outer.centerx - font.size("ASS FL")[0] // 2,
               ass_box_outer.top - font.get_linesize(), PANEL_YELLOW)

    a_img = font.render("A", True, PANEL_BLUE)
    ass_num_str = f"{ass_fl:03d}" if ass_fl > 0 else "000"
    num_ass_img = font.render(ass_num_str, True, PANEL_WHITE)

    a_rect = a_img.get_rect()
    num_ass_rect = num_ass_img.get_rect()

    total_width = a_rect.width + 8 + num_ass_rect.width  # was +4
    center_x = ass_box_outer.centerx
    center_y = ass_box_outer.centery

    a_rect.x = center_x - total_width // 2
    a_rect.y = center_y - a_rect.height // 2

    num_ass_rect.x = a_rect.right + 8  # was +4
    num_ass_rect.y = center_y - num_ass_rect.height // 2

    a_bg = pygame.Rect(a_rect.x - 4, a_rect.y - 4, a_rect.width + 8, a_rect.height + 8)  # was -2,+4
    pygame.draw.rect(surf, PANEL_YELLOW, a_bg, border_radius=8)  # was 4
    surf.blit(a_img, a_rect.topleft)
    surf.blit(num_ass_img, num_ass_rect.topleft)

    # ---------- BR band ----------
    br_band = pygame.Rect(br_x, ass_box_outer.centery - br_h // 2, br_w, br_h)
    pygame.draw.rect(surf, PANEL_YELLOW, br_band)
    bw = font.size("BR")[0]
    _draw_text(surf, "BR", br_band.centerx - bw // 2, label_y, PANEL_YELLOW)
    band_thickness = 16   # thinner red bars
    band_gap = 8          # keeps them close to the yellow BR output band

    top_red = pygame.Rect(br_band.x,
                          br_band.top - band_gap - band_thickness,
                          br_band.width,
                          band_thickness)
    bottom_red = pygame.Rect(br_band.x,
                             br_band.bottom + band_gap,
                             br_band.width,
                             band_thickness)

    pygame.draw.rect(surf, PANEL_RED, top_red)
    pygame.draw.rect(surf, PANEL_RED, bottom_red)

    br_status = "ON" if brakes else "OFF"
    _draw_text_centered(surf, br_status, br_band, PANEL_BLUE)

    # ---------- ITT ----------
    _draw_text(surf, "ITT", itt_x, label_y, PANEL_YELLOW)
    itt_inner_x = itt_x
    itt_inner_y = label_y + 30 + 15  # was +20+10
    eng_box_w, eng_box_h = 48, 48    # was 24,24
    eng_gap_y = 40                   # was 20

    eng1_rect = pygame.Rect(itt_inner_x, itt_inner_y, eng_box_w, eng_box_h)
    pygame.draw.rect(surf, PANEL_YELLOW, eng1_rect)
    pygame.draw.rect(surf, PANEL_BLUE, eng1_rect, 4)  # was 2
    _draw_text_centered(surf, "1", eng1_rect, PANEL_GREEN)
    itt1_box = pygame.Rect(eng1_rect.right + 12, eng1_rect.y, 140, eng_box_h)  # was +6,70
    itt1_str = f"{itt:04d}"
    _draw_text_centered(surf, itt1_str, itt1_box, PANEL_WHITE)

    itt2 = int(jet.itt * 0.95 + 50)
    eng2_rect = pygame.Rect(itt_inner_x, eng1_rect.y + eng_box_h + eng_gap_y, eng_box_w, eng_box_h)
    pygame.draw.rect(surf, PANEL_YELLOW, eng2_rect)
    pygame.draw.rect(surf, PANEL_BLUE, eng2_rect, 4)
    _draw_text_centered(surf, "2", eng2_rect, PANEL_GREEN)
    itt2_box = pygame.Rect(eng2_rect.right + 12, eng2_rect.y, 140, eng_box_h)
    itt2_str = f"{itt2:04d}"
    _draw_text_centered(surf, itt2_str, itt2_box, PANEL_WHITE)

    # ---------- DME(-) / G/S / ETA ROW ----------
    # Add one blank horizontal text row above the DME / G/S / ETA row.
    second_row_y = label_y + 30 + max(ias_h, ias_h, ias_h) + 50 + font.get_linesize()

    dme_x = ias_x

    # DME(-)
    dme_box = pygame.Rect(dme_x, second_row_y, ias_w, ias_h)
    pygame.draw.rect(surf, PANEL_BLUE, dme_box, border_radius=24)
    dme_inner = dme_box.inflate(-12, -12)  # was -6,-6
    pygame.draw.rect(surf, PANEL_WHITE, dme_inner, 4, border_radius=20)

    # Airport letter lives inside the DME bracket.
    # [C] cycles the DME station; the bracket shows the tuned airport's
    # ID letter: DME(M) destination, DME(U) enroute, DME(S) origin.
    dme_label = "DME(%s)" % station_ltr

    dme_label_y = second_row_y - font.get_linesize()
    label_w, _ = font.size(dme_label)
    _draw_text(surf, dme_label, dme_box.centerx - label_w // 2, dme_label_y, PANEL_YELLOW)

    dme_digits_img = font.render(dme_digits, True, PANEL_WHITE)
    digits_rect = dme_digits_img.get_rect()
    digits_rect.centery = dme_box.centery
    digits_rect.centerx = dme_box.centerx - 20
    surf.blit(dme_digits_img, digits_rect.topleft)

    # Unit badge in the same style as the IAS "K": yellow backing,
    # blue letters. DME is a distance, so the badge is NM (or M once
    # the readout has switched to metres inside the last 12,000 m).
    dme_unit_img = font.render(dme_unit, True, PANEL_BLUE)
    dme_unit_rect = dme_unit_img.get_rect()
    dme_unit_rect.midleft = (digits_rect.right + 16, digits_rect.centery)
    dme_unit_bg = pygame.Rect(dme_unit_rect.x - 4, dme_unit_rect.y - 4,
                              dme_unit_rect.width + 8, dme_unit_rect.height + 8)
    pygame.draw.rect(surf, PANEL_YELLOW, dme_unit_bg, border_radius=8)
    surf.blit(dme_unit_img, dme_unit_rect.topleft)

    # G/S
    gs_box = pygame.Rect(alt_box.left, second_row_y, ias_w, ias_h)
    pygame.draw.rect(surf, PANEL_BLUE, gs_box, border_radius=24)
    gs_inner = gs_box.inflate(-12, -12)
    pygame.draw.rect(surf, PANEL_WHITE, gs_inner, 4, border_radius=20)

    # Spelled out in full so it can't be confused with the G/S
    # glideslope tape lower down the panel.
    gs_label = "GROUND SPEED"
    gs_label_w, _ = font.size(gs_label)
    gs_label_x = gs_box.centerx - gs_label_w // 2
    gs_label_y = gs_box.top - font.get_linesize()
    _draw_text(surf, gs_label, gs_label_x, gs_label_y, PANEL_YELLOW)

    # G/S register: the current ground speed in knots (no wind is
    # modelled, so ground speed equals airspeed). Glideslope guidance
    # lives on its own vertical tape lower down the panel.
    # v54: asleep until the engines are started -- a static row of the
    # black/white diagonal cells (the graphic that stands left of
    # START and between START and F/F); nothing moves. [E] swaps the
    # cells for the live readout.
    if not engines:
        _draw_idle_cells(surf, gs_box, 4)
    else:
        gs_num_str = "%03d" % int(round(ias_kts))
        gs_num_img = font.render(gs_num_str, True, PANEL_WHITE)
        gs_num_rect = gs_num_img.get_rect()
        gs_num_rect.centery = gs_box.centery
        gs_num_rect.centerx = gs_box.centerx - 20  # was -10
        surf.blit(gs_num_img, gs_num_rect.topleft)

        k_img = font.render("K", True, PANEL_BLUE)
        k_rect = k_img.get_rect()
        k_rect.midleft = (gs_num_rect.right + 16, gs_num_rect.centery)  # was +8
        k_bg = pygame.Rect(k_rect.x - 4, k_rect.y - 4, k_rect.width + 8, k_rect.height + 8)
        pygame.draw.rect(surf, PANEL_YELLOW, k_bg, border_radius=8)
        surf.blit(k_img, k_rect.topleft)

    # ETA
    eta_box = pygame.Rect(ass_box_outer.left, second_row_y, ias_w, ias_h)
    pygame.draw.rect(surf, PANEL_BLUE, eta_box, border_radius=24)
    eta_inner = eta_box.inflate(-12, -12)
    pygame.draw.rect(surf, PANEL_WHITE, eta_inner, 4, border_radius=20)

    eta_label = "ETA"
    eta_label_w, _ = font.size(eta_label)
    eta_label_x = eta_box.centerx - eta_label_w // 2
    eta_label_y = eta_box.top - font.get_linesize()
    _draw_text(surf, eta_label, eta_label_x, eta_label_y, PANEL_YELLOW)

    # v54: asleep until the engines are started -- the same static
    # black/white diagonal cells as the G/S register. [E] swaps the
    # cells for the ETA, the MIN badge and the shadowy real countdown.
    if not engines:
        _draw_idle_cells(surf, eta_box, 6)
    else:
        # The estimate follows the airport the DME is tuned to (apt_dist was
        # resolved by the DME block above): the time to the destination on
        # "-", and to each enroute field on "v0","v1" ... Any airport already
        # passed reads "--:--" -- just as the DME itself reads "---" -- so
        # the "+" origin channel, which only ever looks back, always shows
        # "--:--".
        # v64: on a REAL TIME leg the sim minute IS the wall-clock minute,
        # so the white ETA and the shadowy countdown beneath it must tell
        # ONE time, not two. Both are now driven by the countdown's own
        # figure -- the tuned field's measured sim-minute budget less the
        # time this leg has run -- the white reading minutes:seconds as
        # ever, the dim-blue line the same duration in hours:minutes:
        # seconds. The distance-over-speed estimate (a 4-hour "ETA" at
        # 161 kt just off the ground, when the leg genuinely takes 2:24)
        # no longer contradicts the honest countdown on the 1:1 legs. The
        # twelve compressed legs are untouched: there the ETA stays
        # distance over speed in sim minutes and the countdown the plan
        # remaining in real ones -- two different times by design.
        real_time_leg = getattr(jet, "time_scale", TIME_SCALE) == 1.0

        # The countdown's budget -- the measured sim-minutes the leg to the
        # TUNED airport genuinely takes: the destination on "-", each
        # enroute field on "v0","v1" (every one timed on the model, just as
        # the route legs were). Worked out ahead of the white readout now,
        # because on a real-time leg the white readout is driven by it.
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
            # v55: the countdown runs on the CURRENT leg, not the whole
            # flight -- the tuned airport's budget less the field this leg
            # started from, against the leg's own clock (both re-armed at
            # every intermediate stopover; both zero from the origin, so
            # a non-stop flight reads exactly as it always has).
            leg_base = getattr(jet, "leg_base_min", 0.0)
            leg_t0 = getattr(jet, "leg_elapsed0", 0.0)
            remain_s = ((budget_min - leg_base) * 60.0
                        - (jet.elapsed - leg_t0)) / max(0.1, getattr(jet, "time_scale", TIME_SCALE))
            overtime = remain_s < 0.0

        if jet.dme_chan == "+":
            eta_num_str = "--:--"
        elif real_time_leg:
            # v64: the white ETA states the countdown's own figure in
            # minutes:seconds -- the very duration the dim-blue line below
            # states in hours:minutes:seconds, minus sign included when the
            # flight runs late.
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
        eta_num_rect.centerx = eta_box.centerx - 40  # was -20
        surf.blit(eta_num_img, eta_num_rect.topleft)

        min_img = font.render("MIN", True, PANEL_BLUE)
        min_rect = min_img.get_rect()
        min_rect.midleft = (eta_num_rect.right + 16, eta_num_rect.centery)  # was +8
        min_bg = pygame.Rect(min_rect.x - 4, min_rect.y - 4, min_rect.width + 8, min_rect.height + 8)
        pygame.draw.rect(surf, PANEL_YELLOW, min_bg, border_radius=8)
        surf.blit(min_img, min_rect.topleft)

        # The REAL countdown (v44): INSIDE the ETA box, along its bottom
        # edge, in the dim CLOCK_BLUE -- a vague, shadowy clock you barely
        # notice. It counts DOWN the real minutes the flight still needs,
        # converted from sim time by the compression. Pauses freeze it with
        # the world, a loaded save resumes it honestly, touchdown parks it
        # at the spare minutes -- and a flight that runs long quietly
        # counts past zero.
        # v47: the countdown follows the DME channel [C], exactly like the
        # ETA above it -- the budget it counts from (worked out just above)
        # is the tuned field's own measured figure. A field already passed
        # reads "--:--", and so does the "+" origin channel, which only
        # ever looks back -- just as the ETA above it always has.
        # v64: on a real-time leg it is no longer a second opinion -- the
        # white ETA above reads this same remain_s figure, so the two
        # clocks agree for the whole flight (and in overtime both carry
        # the minus sign).
        if remain_s is None:
            real_str = "--:--"
        else:
            _cd_s = abs(remain_s)
            if _cd_s >= 3600.0:
                real_str = "%d:%02d:%02d" % (int(_cd_s // 3600.0),
                                             int((_cd_s % 3600.0) // 60.0),
                                             int(_cd_s % 60.0))
            else:
                real_str = "%d:%02d" % (int(_cd_s // 60.0), int(_cd_s % 60.0))
            if overtime:
                real_str = "-" + real_str
        real_img = _panel_tiny_font.render(real_str, True, CLOCK_BLUE)
        real_rect = real_img.get_rect()
        # No "REAL" label (v45): the leading DIGIT sits directly under the
        # ETA's own leading digit, so the two clocks read as one column of
        # time -- the sim's above, the real world's below. In overtime the
        # minus sign hangs one character to the left, keeping the digits
        # (not the sign) on the shared column.
        real_rect.left = eta_num_rect.left
        if overtime:
            real_rect.left -= _panel_tiny_font.size("-")[0]
        real_rect.bottom = eta_box.bottom - 16   # clear of the inner border
        surf.blit(real_img, real_rect.topleft)

        # The wall clock (v55): the current time of day in 24-hour HH:MM,
        # in the countdown's own style -- the same tiny face and the same
        # shadowy CLOCK_BLUE -- on the very same line, against the right
        # edge of the box. The countdown shows how long is left; this
        # shows what time it is.
        now_img = _panel_tiny_font.render(time.strftime("%H:%M"),
                                          True, CLOCK_BLUE)
        now_rect = now_img.get_rect()
        now_rect.right = eta_box.right - 16
        now_rect.bottom = eta_box.bottom - 16
        surf.blit(now_img, now_rect.topleft)

    # ---------- FLAP ----------
    region_left = _orig_eta_right + 40 + RIGHT_SHIFT
    region_right = inner_right - 40 + RIGHT_SHIFT
    region_mid = (region_left + region_right) // 2

    thr_center_x  = (region_mid + region_right) // 2 + 2 * char_w   # two cells right, so the thrust readouts sit under the ITT figures

    bar_width = 56       # was 28
    GS_LINE_OVERHANG = 20   # px each side of the G/S yellow bar (~1/2 cm
                            # on a typical desktop screen once the panel
                            # is scaled)
    GS_LINE_THICK = 4       # px - a thin line

    # ---------- ELEVATION / G/S / FLAP BAND ----------
    # The Elevation (attitude indicator), the G/S glideslope tape and
    # the FLAP gauge share the clear band between the right edge of the
    # ETA box and the left purple bar of the THRUST system, with four
    # equal gaps -- ETA to AI, AI to G/S, G/S to FLAP, FLAP to the
    # purple bar -- so the G/S and FLAP labels no longer collide and
    # the FLAP tick numbers stay clear of the purple bar. The purple
    # bar's left edge is traced from thr_center_x exactly as the THRUST
    # block below computes it (thr_x -> pct_x -> left bar), so the band
    # is known before anything inside it is drawn.
    _thr_x_trace = int(thr_center_x - font.size("THRUST")[0] // 2)
    _pct_x_trace = _thr_x_trace + font.size("T")[0]
    purple_left_x = _pct_x_trace - 20 - 56      # margin_side + bar_w_side

    band_left = eta_box.right
    band_right = purple_left_x

    gs_g_w = bar_width // 2                     # half the flap bar's thickness
    gs_eff_w = gs_g_w + 2 * GS_LINE_OVERHANG    # incl. the line's overhang
    flap_gauge_w = bar_width + 24 + font.size("50")[0]  # bar + gap + tick nos.

    ai_width = int(round(cm_px(sh, 4.0) * phys))        # the designed 4 cm

    band_gap = (band_right - band_left
                - (ai_width + gs_eff_w + flap_gauge_w)) / 4.0
    if band_gap < 8:
        # Very narrow panel: shrink the AI rather than let the tapes touch.
        band_gap = 8
        ai_width = max(60, int(band_right - band_left
                               - gs_eff_w - flap_gauge_w - 4 * band_gap))

    ai_x = int(band_left + band_gap)
    gs_cx = int(band_left + 2 * band_gap + ai_width + gs_eff_w / 2)
    # flap_center_x centres the FLAP *bar* (the label and the orange
    # square hang off it); the tick numbers extend to its right and end
    # one band_gap short of the purple bar.
    flap_center_x = int(band_left + 3 * band_gap + ai_width + gs_eff_w
                        + bar_width / 2)

    flap_text_y = panel_rect.y + 400 + 2 * font.get_linesize()  # was 240
    flap_label_rect = _draw_text(surf, "FLAP", int(flap_center_x - font.size("FLAP")[0] // 2), flap_text_y, PANEL_YELLOW)

    bar_x = flap_label_rect.centerx - bar_width // 2
    bar_top = flap_text_y + 2 * font.get_linesize() + 12  # was +6

    ticks = [0, 10, 20, 30, 40, 50]
    step_h = font.get_linesize()
    bar_height = (len(ticks) - 1) * step_h
    bar_rect = pygame.Rect(bar_x, bar_top, bar_width, bar_height)
    box_w = bar_width
    box_h = bar_width
    # Yellow vertical bar: the full gauge PLUS half a square beyond each
    # end, so every spot the orange square can occupy stays yellow when
    # the square moves away.
    track_rect = pygame.Rect(bar_x, bar_top - box_h // 2, bar_width, bar_height + box_h)
    pygame.draw.rect(surf, PANEL_YELLOW, track_rect)

    tick_area_top = bar_top
    tick_area_height = bar_height

    for i, t in enumerate(ticks):
        y = tick_area_top + i * step_h
        # Centre each number exactly on its flap-setting position, so the
        # orange square sits dead opposite the number it points to, and
        # the yellow track lines up with the 0 and the 50.
        num_img = font.render(str(t), True, PANEL_YELLOW)
        num_rect = num_img.get_rect()
        num_rect.left = bar_rect.right + 24
        num_rect.centery = y
        surf.blit(num_img, num_rect.topleft)

    fp = max(0.0, min(50.0, flap_pos))
    rel = fp / 50.0
    star_y = tick_area_top + int(rel * tick_area_height)

    # Orange square opposite the selected flap setting, with the asterisk
    # inside it. No border. The asterisk glyph rides high in the font's
    # line box, so centring the rendered surface leaves the visible star
    # touching the top of the square -- centre the glyph's INK (its
    # bounding rect) instead, which lands it dead centre whatever the font.
    star_box = pygame.Rect(0, 0, box_w, box_h)
    star_box.center = (bar_rect.centerx, star_y)
    pygame.draw.rect(surf, PANEL_ORANGE, star_box)
    star_font = pygame.font.SysFont("consolas", box_h, bold=True)
    star_img = star_font.render("*", True, PANEL_BLUE)
    star_ink = star_img.get_bounding_rect()
    surf.blit(star_img, (star_box.centerx - star_ink.centerx,
                         star_box.centery - star_ink.centery))

    # ---------- THRUST ----------
    thr_y = panel_rect.y + 400 + 2 * font.get_linesize()       # was 240
    thr_x = int(thr_center_x - font.size("THRUST")[0] // 2)
    _draw_text(surf, "THRUST", thr_x, thr_y, PANEL_YELLOW)

    t_w = font.size("T")[0]
    pct_x = thr_x + t_w
    pct_y = thr_y + 2 * font.get_linesize() - 8  # was -4

    pct_img = font.render("100%", True, PANEL_WHITE)
    pct_rect = pct_img.get_rect(topleft=(pct_x, pct_y))
    surf.blit(pct_img, pct_rect.topleft)

    # Live thrust readout in the space between the 100% and 0% marks --
    # it counts up and down with the throttle as you work it.
    num_width_100 = font.size("100")[0]
    percent_x_100 = pct_x + num_width_100
    pct_w = font.size("%")[0]
    thr_center_x = percent_x_100 + pct_w // 2   # % centre line of the 100% mark
    # (At 0% and 100% the fixed marks already say it, so the live
    # readout only appears between them - no doubling, no crowding.)
    if 0.0 < thrust_percent < 100.0:
        thr_readout = "%d%%" % int(round(thrust_percent))
        thr_read_img = font.render(thr_readout, True, PANEL_WHITE)
        thr_read_rect = thr_read_img.get_rect()
        # Right-align the readout so its % symbol sits exactly on the %
        # centre line shared by the 100% and 0% marks, however wide the
        # number itself is.
        thr_read_rect.top = pct_rect.bottom + 4
        thr_read_rect.right = thr_center_x + pct_w // 2
        surf.blit(thr_read_img, thr_read_rect.topleft)

    zero_img = font.render("0%", True, PANEL_WHITE)
    num_width_0 = font.size("0")[0]
    pct_char_w = font.size("%")[0]
    zero_x = thr_center_x - (num_width_0 + pct_char_w / 2)
    zero_y = pct_rect.bottom + 4 + small_font.get_linesize() + 8  # keeps 0% where it was
    zero_rect = zero_img.get_rect(topleft=(zero_x, zero_y))
    surf.blit(zero_img, zero_rect.topleft)

    # PURPLE BARS
    bar_w_side = 56      # was 28
    margin_side = 20     # was 10
    side_top = pct_y
    side_bottom = zero_y + font.get_linesize()
    side_h = max(0, side_bottom - side_top)
    content_left = pct_x
    content_right = zero_x + zero_img.get_width()

    left_bar_x = content_left - margin_side - bar_w_side
    left_bar_rect = pygame.Rect(left_bar_x, side_top, bar_w_side, side_h)
    pygame.draw.rect(surf, PANEL_PURPLE, left_bar_rect)

    right_bar_x = content_right + margin_side
    right_bar_rect = pygame.Rect(right_bar_x, side_top, bar_w_side, side_h)
    pygame.draw.rect(surf, PANEL_PURPLE, right_bar_rect)

    thrust_ratio = max(0.0, min(1.0, thrust_percent / 100.0))

    # Use the centres of the 100% and 0% marks as the gauge endpoints,
    # so at zero thrust the # symbols sit level with the 0% mark.
    thrust_top_mark = pct_rect.centery
    thrust_zero_mark = zero_rect.centery
    hash_y = int(thrust_zero_mark - thrust_ratio * (thrust_zero_mark - thrust_top_mark))

    hash_band_h = font.get_linesize()

    for rect in (left_bar_rect, right_bar_rect):
        band_rect = pygame.Rect(rect.x, hash_y - hash_band_h // 2, rect.width, hash_band_h)
        pygame.draw.rect(surf, PANEL_GREEN, band_rect)
        hash_img = font.render("#", True, PANEL_YELLOW)
        hrect = hash_img.get_rect()
        hrect.centerx = rect.centerx
        hrect.centery = hash_y
        surf.blit(hash_img, hrect)

    # ---------- R/TH and GEAR ----------
    rth_label = "R/TH"
    rth_w, rth_h = font.size(rth_label)
    mid_between_bars = (left_bar_rect.right + right_bar_rect.left) / 2
    rth_x = int(mid_between_bars - rth_w / 2)
    rth_y = zero_rect.bottom + 16  # was +8

    square_size = bar_w_side
    spacing = 20     # was 10
    sq_centery = rth_y + font.get_linesize() // 2

    left_sq_centerx = int(mid_between_bars - rth_w / 2) - spacing - square_size // 2
    right_sq_centerx = int(mid_between_bars + rth_w / 2) + spacing + square_size // 2

    left_sq = pygame.Rect(0, 0, square_size, square_size)
    right_sq = pygame.Rect(0, 0, square_size, square_size)
    left_sq.center = (left_sq_centerx, sq_centery)
    right_sq.center = (right_sq_centerx, sq_centery)

    # Reverse thrust announced HERE now (v50 -- the v49 REV placard
    # under the THRUST title is gone after one version): while the
    # buckets are out the R/TH label flashes yellow-red and its two
    # guard squares flash red-yellow in step, on the same half-second
    # cadence as the CAB PRESS warning.
    rev_flash = (getattr(jet, "reverser", False)
                 and (pygame.time.get_ticks() // 500) % 2 == 0)
    sq_face = PANEL_YELLOW if rev_flash else PANEL_RED
    rth_color = PANEL_RED if rev_flash else PANEL_YELLOW
    pygame.draw.rect(surf, sq_face, left_sq)
    pygame.draw.rect(surf, sq_face, right_sq)
    pygame.draw.rect(surf, PANEL_BLUE, left_sq, 4)  # was 2
    pygame.draw.rect(surf, PANEL_BLUE, right_sq, 4)

    _draw_text(surf, rth_label, rth_x, rth_y, rth_color)

    # GEAR indicator
    gear_label = "GEAR"
    g_w = font.size("G")[0]
    gear_x = rth_x - g_w
    gear_y = rth_y + font.get_linesize() + 8  # was +4
    gear_text_img = font.render(gear_label, True, PANEL_BLUE)
    gear_bg_rect = gear_text_img.get_rect(topleft=(gear_x, gear_y))
    pygame.draw.rect(surf, PANEL_YELLOW, gear_bg_rect)
    surf.blit(gear_text_img, gear_bg_rect.topleft)

    e_w, e_h = font.size("E")
    e_x = gear_x + g_w
    e_y = gear_bg_rect.bottom
    block_w = block_h = bar_w_side

    # Progressive gear lights: each square follows its own entry in
    # jet.gear_lights -- [top(E), bottom-left, bottom-right] -- so they
    # go out and come back on one at a time during the transit.
    gl = getattr(jet, "gear_lights", [gear_down, gear_down, gear_down])

    e_rect = pygame.Rect(e_x, e_y, block_w, block_h)
    pygame.draw.rect(surf, BRIGHT_GREEN if gl[0] else (40, 40, 40), e_rect)

    new1_x = e_rect.left - block_w
    new1_y = e_rect.bottom
    new1_rect = pygame.Rect(new1_x, new1_y, block_w, block_h)
    pygame.draw.rect(surf, BRIGHT_GREEN if gl[1] else (40, 40, 40), new1_rect)

    new2_x = e_rect.right
    new2_y = e_rect.bottom
    new2_rect = pygame.Rect(new2_x, new2_y, block_w, block_h)
    pygame.draw.rect(surf, BRIGHT_GREEN if gl[2] else (40, 40, 40), new2_rect)

    # Yellow *D gear-door light: 10 px right of the bottom-right green.
    # It trails the greens by one fifth of a second: lit all through the
    # retraction sequence, out a beat after the third green vanishes, and
    # back on a beat after the third green returns on extension. When out
    # it leaves the same dark grey placeholder as the green squares.
    door_lit = getattr(jet, "door_light", gear_down)
    door_rect = pygame.Rect(new2_rect.right + 10, new2_rect.y, block_w, block_h)
    pygame.draw.rect(surf, PANEL_YELLOW if door_lit else (40, 40, 40), door_rect)
    if door_lit:
        # Same glyph-rides-high fix as the FLAP star: drawn as "*D" the
        # asterisk hugs the top of the square while the D stands full
        # height. Set the two glyphs separately, centring each one's
        # INK, so the star floats level with the middle of the D.
        # (Monospace: two single glyphs tile exactly like "*D".)
        d_img = font.render("D", True, PANEL_BLUE)
        dstar_img = font.render("*", True, PANEL_BLUE)
        dd_x = door_rect.centerx - (dstar_img.get_width() + d_img.get_width()) // 2
        dd_y = door_rect.centery - d_img.get_height() // 2
        d_ink = d_img.get_bounding_rect()
        dstar_ink = dstar_img.get_bounding_rect()
        surf.blit(dstar_img, (dd_x, dd_y + d_ink.centery - dstar_ink.centery))
        surf.blit(d_img, (dd_x + dstar_img.get_width(), dd_y))

    # ---------- GLIDESLOPE DEVIATION TAPE ----------
    # A vertical yellow tape in the Elevation / G/S / FLAP band between
    # the ETA box and the THRUST system's left purple bar, in the same
    # style as the flap gauge; its centre (gs_cx) and width (gs_g_w)
    # come from the band layout above. The tape is always on the panel,
    # and the thin white line is always on it: parked at the bottom
    # until the glideslope comes alive on approach, then it rides the
    # tape: above the centre notch = HIGH, on it = on the glideslope,
    # below it = LOW. Full scale top-to-bottom is +/-500 ft.
    # Same top-to-bottom extent as the flap gauge, but HALF its
    # thickness, so the two tapes read as a slender matched pair.
    gs_top = bar_top - box_h // 2        # same top as the flap track
    gs_g_h = bar_height + box_h          # same bottom as the flap track

    # ---------- ATTITUDE INDICATOR (ELEVATION) ----------
    # Sized as the instrument was designed: 4 cm wide x 10 cm tall (the
    # tkinter prototype's 152 x 378 px at 96 DPI), measured with the
    # panel's physical-unit helper so it holds that true size on screen.
    # Its width and x position come from the Elevation / G/S / FLAP band
    # layout above; its bottom edge rests a quarter inch above the INFO
    # line.
    ai_height = int(round(cm_px(sh, 10.0) * phys))
    # Top of the INFO output area (== bg2_rect.bottom in the lower-left
    # section below: base_y + 60 + line_h for FUEL, + 60 + line_h for VSI).
    info_top = panel_rect.y + 640 + 120 + 4 * font.get_linesize()
    ai_rect = pygame.Rect(ai_x, info_top - qtr_inch - ai_height,
                          ai_width, ai_height)
    draw_attitude_indicator(surf, jet, ai_rect)

    # The nameplate (v39, retitled v72): the title "ATT IND" balanced
    # across the top of the instrument, one eighth of an inch above it,
    # in the same panel yellow as the IAS / G/S / FLAP labels. The
    # letters are letter-spaced so the word spans a touch WIDER than the
    # gauge -- a small overlap on either side -- measured with the
    # physical-unit helper, so the gap is a true eighth of an inch on
    # any screen.
    eighth_inch = max(1, int(round(cm_px(sh, 0.3175) * phys)))
    att_txt = "ATT IND"
    att_overlap = max(2, ai_rect.width // 14)   # the small overlap each side
    att_chars = [font.render(ch, True, PANEL_YELLOW) for ch in att_txt]
    att_adv = [max(1, font.size(ch)[0]) for ch in att_txt]
    att_span = ai_rect.width + 2 * att_overlap
    att_gap = max(0, int(round((att_span - sum(att_adv))
                               / (len(att_txt) - 1))))
    att_x = ai_rect.centerx - (sum(att_adv) + att_gap * (len(att_txt) - 1)) // 2
    att_y = ai_rect.top - eighth_inch - max(c.get_height() for c in att_chars)
    for ch_img, adv in zip(att_chars, att_adv):
        surf.blit(ch_img, (att_x, att_y))
        att_x += adv + att_gap

    lab = "G/S"
    _draw_text(surf, lab, gs_cx - font.size(lab)[0] // 2,
               flap_text_y, PANEL_YELLOW)   # level with the FLAP and THRUST labels
    track = pygame.Rect(gs_cx - gs_g_w // 2, gs_top, gs_g_w, gs_g_h)
    pygame.draw.rect(surf, PANEL_YELLOW, track)
    # Centre notch = exactly on the glideslope
    notch = pygame.Rect(track.x - 10, track.centery - 3, gs_g_w + 20, 6)
    pygame.draw.rect(surf, PANEL_BLUE, notch)
    # Thin white horizontal line, ALWAYS on the bar. Before the
    # glideslope wakes it sits parked at the bottom; once the G/S is
    # alive it rides the tape -- climbs as you go high, sinks as you go
    # low. (v46: the ride is ANGULAR now, a degree off the beam for full
    # scale instead of a fixed 500 feet, so the marker keeps telling the
    # truth from a hundred miles out -- walking in off the peg as the
    # path is joined -- down to the last mile, where it hunts around the
    # notch with every correction the autopilot makes.) Overhangs the bar.
    gs_frac = getattr(jet, "gs_frac", None)
    if gs_frac is None:
        frac = -1.0             # parked at the bottom until the G/S wakes
    else:
        frac = max(-1.0, min(1.0, float(gs_frac)))
    mk = pygame.Rect(0, 0, gs_g_w + 2 * GS_LINE_OVERHANG, GS_LINE_THICK)
    mk.centerx = gs_cx
    mk.centery = track.centery - int(frac * (gs_g_h // 2))
    pygame.draw.rect(surf, PANEL_WHITE, mk)

    # ---------- LOWER LEFT (START, F/F, AUTO PILOT, H/L, FUEL, VSI) ----------
    base_y = panel_rect.y + 640 + 2 * font.get_linesize()  # was 380
    left_x = panel_rect.x + 120 + LEFT_SHIFT     # track shifted main row

    line_h = font.get_linesize()
    char_w, _ = font.size("A")

    start_text = "START"
    start_img = font.render(start_text, True, PANEL_BLUE)
    start_x = left_x + 2 * char_w
    start_y = base_y
    auto_y = base_y + 60            # was 30

    ff_text = "F/F"
    ff_w, ff_h = font.size(ff_text)
    ff_x = start_x + 10 * char_w

    auto_text = "AUTO PILOT:"
    auto_w, auto_h = font.size(auto_text)

    hl_text = "H/L"
    hl_w, hl_h = font.size(hl_text)
    hl_x = ff_x

    fuel_y = auto_y + line_h
    fuel_x = left_x

    fuel_label_text = "FUEL"
    fuel_label_img = font.render(fuel_label_text, True, PANEL_BLUE)
    fuel_label_w, fuel_label_h = fuel_label_img.get_size()

    colon_text = ":"
    colon_img = font.render(colon_text, True, PANEL_BLUE)
    colon_w, colon_h = colon_img.get_size()
    colon_x = fuel_x + fuel_label_w
    colon_y = fuel_y

    # The FUEL and VSI figures share ONE fixed right edge (v67): both are
    # right-justified against it, so the LAST digit of every reading sits in
    # the same column at all times -- a five-character VSI reading (a descent
    # past 1,000 fpm, e.g. "-1224") grows LEFT into the dark cutout instead
    # of jumping one space right, and the LB/FPM badges never shift either.
    # (Was left-anchored: the fifth character pushed the reading's last
    # digit one character to the right.)
    fuel_value_text = f"{int(fuel_kg):4d}"
    fuel_value_w, fuel_value_h = font.size(fuel_value_text)
    value_right_x = colon_x + colon_w + 5 * char_w   # the fixed right edge
    fuel_value_x = value_right_x - fuel_value_w

    g_target_x = hl_x + 2 * char_w
    kg_text = "LB"   # fuel is counted in pounds everywhere else (route
                     # fuel figures, the LOW FUEL call, the success screen)
    kg_w, kg_h = font.size(kg_text)
    kg_x = g_target_x - 1 * char_w

    min_kg_x = fuel_value_x + fuel_value_w + char_w
    if kg_x < min_kg_x:
        kg_x = min_kg_x

    vsi_y = fuel_y + 60             # was 30
    vsi_label = "VSI:"
    vsi_label_img = font.render(vsi_label, True, PANEL_BLUE)
    vsi_label_w, _ = vsi_label_img.get_size()

    vsi_value_text = f"{int(vsi_fpm):4d}"
    vsi_value_w, vsi_value_h = font.size(vsi_value_text)
    vsi_value_x = value_right_x - vsi_value_w   # right-justified too (v67)

    fpm_text = "FPM"
    fpm_img = font.render(fpm_text, True, PANEL_BLUE)
    fpm_w, fpm_h = font.size(fpm_text)
    fpm_x = vsi_value_x + vsi_value_w + 2 * char_w

    # Move group one space left
    ff_x -= char_w
    hl_x -= char_w
    fuel_value_x -= char_w
    kg_x -= char_w
    vsi_value_x -= char_w
    fpm_x -= char_w
    fuel_value_x += char_w
    vsi_value_x += char_w

    # Wide-value guard: with the values right-justified (v67) their right
    # edge never moves, so this is a fixed relationship now -- the guard
    # simply makes sure the LB/FPM unit column always starts clear of that
    # shared right edge, whatever the base geometry hands it, and the dark
    # cutout below is sized to match (see cut_width). (Before v67 the
    # values were left-anchored: a five-character reading -- VSI past
    # +/-1000, e.g. "-1224", or a five-figure FUEL -- pushed its last digit
    # onto the yellow unit backing, and the v54 nudge chased it, so the
    # whole column jumped a space.)
    value_right = max(fuel_value_x + fuel_value_w, vsi_value_x + vsi_value_w)
    unit_shift = max(0, value_right + char_w - kg_x)
    kg_x += unit_shift
    fpm_x += unit_shift

    lower_right = max(kg_x + kg_w, fpm_x + fpm_w)

    # YELLOW BLOCKS
    bg1_top = start_y
    bg1_bottom = auto_y + line_h
    bg1_height = bg1_bottom - bg1_top
    bg1_left = left_x - 16          # was -8
    bg1_right = lower_right
    bg1_rect = pygame.Rect(bg1_left, bg1_top, bg1_right - bg1_left, bg1_height)
    pygame.draw.rect(surf, PANEL_YELLOW, bg1_rect)

    clear_left_rect = pygame.Rect(bg1_left, start_y, start_x - bg1_left, line_h)
    pygame.draw.rect(surf, PANEL_GREEN, clear_left_rect)

    start_end_x = start_x + start_img.get_width()
    if ff_x > start_end_x:
        clear_start_to_ff = pygame.Rect(start_end_x, start_y, ff_x - start_end_x, line_h)
        pygame.draw.rect(surf, PANEL_GREEN, clear_start_to_ff)

    bg2_top = fuel_y
    bg2_bottom = vsi_y + line_h
    bg2_height = bg2_bottom - bg2_top
    bg2_left = left_x - 16
    bg2_right = lower_right
    bg2_rect = pygame.Rect(bg2_left, bg2_top, bg2_right - bg2_left, bg2_height)
    pygame.draw.rect(surf, PANEL_YELLOW, bg2_rect)

    cut_start_x = colon_x + colon_w
    # One character of dark past the widest value, so a five-character
    # FUEL/VSI reading can no longer spill onto the yellow unit backing.
    cut_width = value_right + char_w - cut_start_x
    clear_rect = pygame.Rect(cut_start_x, bg2_top, cut_width, bg2_height)
    pygame.draw.rect(surf, PANEL_GREEN, clear_rect)

    vsi_clear_start_x = left_x + vsi_label_w
    vsi_clear_width = 2 * char_w
    vsi_clear_rect = pygame.Rect(vsi_clear_start_x, bg2_top, vsi_clear_width, bg2_height)
    pygame.draw.rect(surf, PANEL_GREEN, vsi_clear_rect)

    kg_bg_start_x = kg_x - char_w
    kg_bg_width = char_w
    kg_bg_rect = pygame.Rect(kg_bg_start_x, bg2_top, kg_bg_width, bg2_height)
    pygame.draw.rect(surf, PANEL_YELLOW, kg_bg_rect)

    fpm_clear_x = fpm_x - char_w
    fpm_clear_w = char_w
    fpm_clear_lower = pygame.Rect(fpm_clear_x, bg2_top, fpm_clear_w, bg2_height)
    pygame.draw.rect(surf, PANEL_GREEN, fpm_clear_lower)
    fpm_clear_upper = pygame.Rect(fpm_clear_x, bg1_top, fpm_clear_w, bg1_height)
    pygame.draw.rect(surf, PANEL_GREEN, fpm_clear_upper)

    # Draw all text on top
    surf.blit(start_img, (start_x, start_y))

    ff_bg_rect = pygame.Rect(ff_x, start_y, ff_w, line_h)
    pygame.draw.rect(surf, PANEL_YELLOW, ff_bg_rect)
    _draw_text(surf, ff_text, ff_x, base_y, PANEL_BLUE)

    _draw_text(surf, auto_text, left_x, auto_y, PANEL_BLUE)

    hl_bg_rect = pygame.Rect(hl_x, auto_y, hl_w, line_h)
    pygame.draw.rect(surf, PANEL_YELLOW, hl_bg_rect)
    # The 'H/L' letters are gone -- the yellow patch stays, empty.

    # Autopilot output between the red bars: a yellow box showing the
    # autopilot's live state -- ON or OFF (same style as the BR band).
    ap_text = "ON" if ap else "OFF"
    ap_box_x = hl_x + hl_w + 3 * char_w
    ap_box_w = 3 * char_w + 8
    ap_box = pygame.Rect(ap_box_x, auto_y, ap_box_w, line_h)
    pygame.draw.rect(surf, PANEL_YELLOW, ap_box)
    _draw_text_centered(surf, ap_text, ap_box, PANEL_BLUE)

    # RED VERTICAL BARS -- same style as the BR band: half thickness,
    # tucked in close to the output
    ap_bar_w = char_w // 2
    ap_gap = char_w // 4

    bar_rect = pygame.Rect(ap_box_x - ap_gap - ap_bar_w, auto_y, ap_bar_w, line_h)
    pygame.draw.rect(surf, PANEL_RED, bar_rect)

    bar2_rect = pygame.Rect(ap_box.right + ap_gap, auto_y, ap_bar_w, line_h)
    pygame.draw.rect(surf, PANEL_RED, bar2_rect)

    # ---------- CDI (course deviation indicator) ----------
    # Horizontal gauge immediately right of the AUTO PILOT ON/OFF
    # assembly, about four centimetres wide. The blue vertical needle
    # sits in the middle when the aircraft is exactly on the OBS course
    # line; drift off course and it walks TOWARD the course (full scale
    # = 2 nm either side), so working the [A]/[D] turn keys moves the
    # line. Two dots each side of centre mark the scale.
    xte_nm = getattr(jet, "xte", 0.0)
    CDI_FULL_NM = 2.0
    cdi_w = 375                          # about ten centimetres on screen
    cdi_h = line_h - 10
    cdi_x = bar2_rect.right + 3 * char_w
    cdi_track = pygame.Rect(cdi_x, auto_y + 5, cdi_w, cdi_h)
    pygame.draw.rect(surf, PANEL_YELLOW, cdi_track)
    pygame.draw.rect(surf, PANEL_BLUE, cdi_track, 4)
    cdi_frac = max(-1.0, min(1.0, xte_nm / CDI_FULL_NM))
    needle_x = cdi_track.centerx - int(cdi_frac * (cdi_w // 2 - 10))
    # Five dots: one at the centre (the on-course mark, so the needle
    # has a dot to light up even at start-up) plus two each side.
    dot_xs = [cdi_track.centerx]
    for dot_i in (1, 2):
        for dot_s in (-1, 1):
            dot_xs.append(cdi_track.centerx + dot_s * dot_i * (cdi_w // 6))
    for dot_x in dot_xs:
        pygame.draw.circle(surf, PANEL_BLUE, (dot_x, cdi_track.centery), 4)
    pygame.draw.line(surf, PANEL_BLUE,
                     (needle_x, cdi_track.y + 4),
                     (needle_x, cdi_track.bottom - 4), 6)
    # The dot under the needle is painted ON TOP of it, so a bright white
    # dot shines through the blue needle; it turns blue again once the
    # needle moves on.
    for dot_x in dot_xs:
        if abs(needle_x - dot_x) <= 6:
            pygame.draw.circle(surf, PANEL_WHITE,
                               (dot_x, cdi_track.centery), 5)
    cdi_lab = _panel_tiny_font.render("Course Deviation Indicator", True, PANEL_YELLOW)
    surf.blit(cdi_lab, (cdi_track.centerx - cdi_lab.get_width() // 2,
                        cdi_track.y - cdi_lab.get_height() - 2))

    # AUTOLAND flag above the ON/OFF box: "A/L? Y/N" while the offer is
    # on the table (v60: the whole choice named on the placard),
    # "AUTOLAND" once [Y] hands the landing to the autopilot.
    # Same size and format as the SAVE GAME button (bold consolas 28,
    # blue-on-yellow with a blue border), placed after the CDI so its
    # right edge always stops short of the "Course Deviation Indicator"
    # words with a small gutter, whatever font the system supplies.
    al_on = getattr(jet, "autoland", False)
    al_pending = getattr(jet, "al_offer", False)
    if al_on or al_pending:
        al_text = "AUTOLAND" if al_on else "A/L? Y/N"
        al_flag = pygame.Rect(0, 0, btn_font.size(al_text)[0] + 28,
                              btn_font.get_linesize() + 12)
        al_flag.left = ap_box_x
        al_flag.top = start_y
        cdi_lab_left = cdi_track.centerx - cdi_lab.get_width() // 2
        if al_flag.right > cdi_lab_left - 8:
            al_flag.right = cdi_lab_left - 8
        pygame.draw.rect(surf, PANEL_YELLOW, al_flag)
        pygame.draw.rect(surf, PANEL_BLUE, al_flag, 4)
        _draw_text_centered(surf, al_text, al_flag, PANEL_BLUE, btn_font)
        # v60: the placard is a button, like the [Z] ABANDON placard --
        # register its rect for the MOUSEBUTTONDOWN handler. The dict is
        # cleared at the top of every draw, so no stale rect survives.
        PANEL_BUTTONS["autoland"] = al_flag

    # FUEL label
    surf.blit(fuel_label_img, (fuel_x, fuel_y))

    # colon with yellow background
    colon_bg_rect = pygame.Rect(colon_x, colon_y, colon_w, colon_h)
    pygame.draw.rect(surf, PANEL_YELLOW, colon_bg_rect)
    surf.blit(colon_img, (colon_x, colon_y))

    # FUEL value in white
    fuel_value_img = font.render(fuel_value_text, True, PANEL_WHITE)
    surf.blit(fuel_value_img, (fuel_value_x, fuel_y))

    # LB in blue -- the same colour as F/F and FPM on their yellow patches
    surf.blit(font.render(kg_text, True, PANEL_BLUE), (kg_x, fuel_y))

    # VSI label + white value
    surf.blit(vsi_label_img, (left_x, vsi_y))
    vsi_value_img = font.render(vsi_value_text, True, PANEL_WHITE)
    surf.blit(vsi_value_img, (vsi_value_x, vsi_y))

    # yellow background + FPM
    fpm_bg_rect = pygame.Rect(fpm_x, vsi_y, fpm_w, line_h)
    pygame.draw.rect(surf, PANEL_YELLOW, fpm_bg_rect)
    surf.blit(fpm_img, (fpm_x, vsi_y))

    # PATCH: fill black column just left of 'H/L'
    patch_x = hl_x - char_w
    patch_top = start_y
    patch_height = (auto_y + line_h) - patch_top
    patch_rect = pygame.Rect(patch_x, patch_top, char_w, patch_height)
    pygame.draw.rect(surf, PANEL_YELLOW, patch_rect)

    _draw_text(surf, auto_text, left_x, auto_y, PANEL_BLUE)
    # 'H/L' is not re-drawn here either -- the yellow patch stays empty.

    # Remove yellow background one space to the left of 'F/F'
    clear_ff_left_x = ff_x - char_w
    clear_ff_left_rect = pygame.Rect(clear_ff_left_x, start_y, char_w, line_h)
    pygame.draw.rect(surf, PANEL_GREEN, clear_ff_left_rect)

    surf.blit(start_img, (start_x, start_y))

    # ---------- SPINNING DIAGONAL CELLS (VZ-200 tribute) ----------
    # The moment the engines start, the black/white diagonal graphic from
    # the ALT window appears in the TWO black squares immediately left of
    # START and spins RAPIDLY -- and KEEPS spinning all the way to
    # liftoff (v26 -- was the first fifteen real seconds, then rest).
    # The cells park once she leaves the ground, and fall quiet again if
    # the engines are shut down on the ground. The FOUR black squares
    # between START and F/F spin for the rest of the flight -- at TWICE
    # the old leisurely rate since v73. Every cell is drawn the same way
    # round (nothing inverted), so no two same-coloured rectangles ever
    # touch.
    eng_t0 = getattr(jet, "eng_start_t", None)
    if eng_t0 is None and engines:
        eng_t0 = 0.0            # loaded an old save with engines running
    if eng_t0 is not None:
        since_start = jet.elapsed - eng_t0
        RAPID_FLIP_SIM = 1.5    # fast spin: flip every 1.5 sim-seconds ...
                                # ... until she leaves the ground (v26)
        SLOW_FLIP_SIM = 3.0     # the cells between START and F/F: flip
                                # every 3 sim-seconds -- TWICE the old
                                # 6-sim-second rate (v73)
        rapid_flip = (int(since_start / RAPID_FLIP_SIM) % 2 == 1) \
                     if (engines and not jet.airborne) else False
        slow_flip = int(jet.elapsed / SLOW_FLIP_SIM) % 2 == 1
        cell_w, cell_h = font.size("A")
        cell_y = start_y + (line_h - cell_h) // 2
        # Two cells immediately left of START, centred in the space
        duo_w = 2 * cell_w
        duo_x = bg1_left + (start_x - bg1_left - duo_w) // 2
        for i in range(2):
            _draw_diag_shape(surf, duo_x + i * cell_w, cell_y,
                             PANEL_WHITE, (0, 0, 0), flip=rapid_flip)
        # Four cells between START and F/F, filling the gap exactly
        for i in range(4):
            _draw_diag_shape(surf, start_end_x + i * cell_w, cell_y,
                             PANEL_WHITE, (0, 0, 0), flip=slow_flip)

    # ---------- INFO / WIND ----------
    info_y = bg2_rect.bottom

    info_text = "INFO:"
    info_img = font.render(info_text, True, PANEL_BLUE)
    info_w, info_h = info_img.get_size()

    info_x = left_x     # keep INFO aligned with shifted bottom section

    info_bg_left = bg2_rect.x
    info_bg_width = (info_x - info_bg_left) + info_w

    info_bg = pygame.Rect(info_bg_left, info_y, info_bg_width, info_h)
    pygame.draw.rect(surf, PANEL_YELLOW, info_bg)
    surf.blit(info_img, (info_x, info_y))

    wind_x = info_bg.right + 20     # was +10
    if paused:
        msg_display = "PAUSED - [SPACE] or the RESUME button to fly on."
    else:
        # The default INFO line: the surface wind at the airport tuned
        # in the DME -- the destination on "-", each enroute field on
        # "v0","v1" ..., the origin on "+" -- named by its ICAO code
        # (YMML Melbourne, YSSY Sydney, ...).
        # (Was the hardcoded "ASSY" left over from the VZ-200 original.)
        # v52: the wind direction shown is always the route track + 180,
        # so she arrives heading straight into the wind. v68: the speed is
        # a per-airport figure from the 10-30 range (was the perpetual 23)
        # -- FOR SHOW ONLY; the flight model reads nothing of it.
        dme_apt_name = orig_name if jet.dme_chan == "+" else apt_name
        dme_icao = AIRPORT_ICAO.get(dme_apt_name, "????")
        wind_spd = surface_wind_show(jet, dme_apt_name)   # v68: for show
        msg_display = msg if msg else "%s SURFACE WIND %03d %d" % (
            dme_icao, wind_dir, wind_spd)
    # Over-long INFO lines are set in a smaller font so they end inside
    # the blue margin; lines that fit are drawn exactly as before.
    _draw_text_fit(surf, msg_display, wind_x, info_y, inner_right - 10, PANEL_WHITE)

    # NOTE: the bottom help legend is deliberately NOT drawn here any more.
    # It is drawn by draw_help_legend() AFTER the panel has been scaled to
    # the screen (in flight_hud), at native screen resolution, so the
    # downscale can no longer erode the thin strokes of '+' and '-' (which
    # used to make '[+/-]' read as '[|/ ]' on smaller screens).


# ----------------------------------------------------------------------
#  HELP LEGEND  --  drawn AFTER scaling, at native screen resolution
# ----------------------------------------------------------------------
HELP_TEXT = ("[E] engines [B] brakes [R] rev [F/Shift+F] flaps [G] gear [C] DME "
             "[V] enroute [W/S] pitch [+/-] thrust [A/D] turn [O] OBS "
             "[K/Shift+K] FL [L] level [P] AP [Y/N] autoland [M] sound [SPC] pause [Z] abandon")


def draw_help_legend(screen, px, py, pw, ph, scale):
    """Draw the key-press legend straight onto the screen, over the bottom
    of the already-scaled panel. Drawing it here -- after transform.scale --
    keeps every glyph pin-sharp, so thin strokes like the '-' and the '+'
    crossbar can no longer be eaten by the downscale.

    px, py  = top-left corner of the scaled panel on screen
    pw, ph  = scaled panel size, in screen pixels
    scale   = the factor the panel was scaled by (1.0 = no scaling)
    """
    s = max(scale, 0.2)
    # Same anchoring as before, translated from panel space to screen space:
    # centred on the panel, with the bottom edge of its black box resting
    # 30 (scaled) px above the inside edge of the bottom blue border.
    # (50 = panel bottom margin, BORDER_THICK = blue border, 30 = the lift.)
    bottom_inset = int((50 + BORDER_THICK + 30) * s)
    max_help_w = int(((2000 - 100) - 2 * BORDER_THICK - 100) * s)
    help_size = max(8, int(24 * s))
    tiny_font = pygame.font.SysFont("consolas", help_size)
    while help_size > 8 and tiny_font.size(HELP_TEXT)[0] > max_help_w:
        help_size -= 1
        tiny_font = pygame.font.SysFont("consolas", help_size)
    help_surf = tiny_font.render(HELP_TEXT, True, PANEL_WHITE)
    box_pad_x = max(3, int(20 * s))
    box_pad_y = max(2, int(6 * s))
    help_bg = pygame.Rect(0, 0,
                          help_surf.get_width() + 2 * box_pad_x,
                          help_surf.get_height() + 2 * box_pad_y)
    help_bg.centerx = px + pw // 2
    help_bg.bottom = py + ph - bottom_inset
    pygame.draw.rect(screen, (0, 0, 0), help_bg)
    pygame.draw.rect(screen, PANEL_BLUE, help_bg, max(1, int(2 * s)))
    screen.blit(help_surf, (help_bg.x + box_pad_x, help_bg.y + box_pad_y))

# ----------------------------------------------------------------------
#  SCREEN 4: MAIN FLIGHT HUD (2X scaled panel)
# ----------------------------------------------------------------------
def flight_hud(screen, sw, sh, fonts, jet):
    clock = pygame.time.Clock()
    pygame.key.set_repeat(200, 50)

    PANEL_W, PANEL_H = 2000, 1200   # Tightened panel size
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
    global _landed_hold_until       # v73: shared with audio_update -- the
                                    # three-second hold keeps the sound on
    _landed_hold_until = 0
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
                        jet.__dict__.update(loaded.__dict__)
                        jet.msg = "Saved flight loaded - welcome back!"
                        play_bing()
                    else:
                        jet.msg = "No saved game found yet."
                elif event.key == pygame.K_v:
                    # Peek at the Enroute screen: the red square shows
                    # how far along the route the aircraft now is. One
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
                # The panel is scaled and centred on screen -- map the
                # click back into panel coordinates before testing.
                sc = min(sw / PANEL_W, sh / PANEL_H, 1.0)
                pw, ph = int(PANEL_W * sc), int(PANEL_H * sc)
                ox, oy = (sw - pw) // 2, (sh - ph) // 2
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
        # Scale panel to fit screen with balanced margins. Worked out
        # BEFORE the panel is drawn, so draw_panel can convert physical
        # sizes (the quarter-inch gaps, the 4 x 10 cm AI gauge) from
        # screen pixels into panel pixels and they survive the shrink.
        scale = min(sw / PANEL_W, sh / PANEL_H, 1.0)  # Only scale down, never up
        draw_panel(panel_surf, jet, PANEL_W, PANEL_H, sh, scale)

        screen.fill((0, 0, 0))

        if scale < 1.0:
            scaled_w = int(PANEL_W * scale)
            scaled_h = int(PANEL_H * scale)
            scaled_surf = pygame.transform.scale(panel_surf, (scaled_w, scaled_h))
            px = (sw - scaled_w) // 2
            py = (sh - scaled_h) // 2
            screen.blit(scaled_surf, (px, py))
        else:
            scaled_w, scaled_h = PANEL_W, PANEL_H
            px = (sw - PANEL_W) // 2
            py = (sh - PANEL_H) // 2
            screen.blit(panel_surf, (px, py))

        # The legend goes on AFTER the scaling, at native resolution -- crisp.
        draw_help_legend(screen, px, py, scaled_w, scaled_h, scale)

        pygame.display.flip()

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
    try:
        print("\n" + farewell + "\n", flush=True)
    except Exception:
        pass
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

    while True:
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
        if quit_game:
            break
        if getattr(jet, "to_routes", False):
            continue            # [R] at the enroute full-stop prompt (v22):
                                # straight back to Route Selection, no summary
        if dead:
            result = crash_screen(screen, sw, sh, fonts, jet)
            if result == "tutorial":
                # [T] at the crash screen (v32): straight to Flying
                # School, then back to Route Selection when class is
                # over (a window-close in school still ends the game).
                if tutorial_screen(screen, sw, sh, fonts) == "quit":
                    break
                continue
        elif done:
            result = success_screen(screen, sw, sh, fonts, jet)
        else:
            break
        if not result:
            break

    clean_exit_to_desktop("     Thanks for flying Learjet.")


if __name__ == "__main__":
    main()