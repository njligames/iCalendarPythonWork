#!/usr/local/bin/python3

from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
from datetime import timedelta
import os
from pathlib import Path

cal = Calendar()
cal.add('attendee', 'MAILTO:abc@example.com')
cal.add('attendee', 'MAILTO:xyz@example.com')

event = Event()
event.add('summary', 'Python meeting about calendaring')
event.add('description', 'description')
event.add('dtstart', datetime(2022, 10, 4, 16, 0, 0, tzinfo=pytz.utc))
event.add('dtend', datetime(2022, 10, 4, 18, 0, 0, tzinfo=pytz.utc))
event.add('dtstamp', datetime(2022, 10, 4, 0, 10, 0, tzinfo=pytz.utc))
event.add('rrule', {'COUNT': [2], 'FREQ': ['WEEKLY']})

organizer = vCalAddress('MAILTO:hello@example.com')
organizer.params['cn'] = vText('Sir Jon')
organizer.params['role'] = vText('CEO')
event['organizer'] = organizer
event['location'] = vText('London, UK')

# Adding events to calendar
cal.add_component(event)

directory = str(Path(__file__).parent.parent) + "/"
print("ics file will be generated at ", directory)
f = open(os.path.join(directory, 'example.ics'), 'wb')
f.write(cal.to_ical())
f.close()

workouts = [
        {
            0,
            "Chest & Back",
            "It’s all about pushing and pulling during this resistance workout. With 12 dynamic exercises to strengthen, tighten, tone, and build the major muscles of the upper torso, you’ll quickly feel the burn. While the majority of exercises will be either push-ups or pull-ups, there are a few that will require the use of dumbbells or bands.",
            52,
            50
        },
        {
            1,
            "Plyometrics",
            "You’d better Bring It! when you take on this dynamic cardio workout (some call it \"the Beast\"). With more than 30 explosive jumping moves, you won’t be spending much time on the ground during this routine. Just be sure to wear some shock-absorbing footwear and work with a good shock-absorbing mat.",
            58,
            36
        },
        {
            2,
            "Shoulders & Arms",
            "Get out those dumbbells and/or bands. This workout incorporates a potent combination of pressing, curling, and fl y movements that will do wonders for the development of the deltoid muscles (shoulders) and the biceps and triceps (arms).",
            59,
            53
        },
        {
            3,
            "Yoga X",
            "If you think this’ll be the day to relax and take a breather, forget it. This yoga workout will challenge you like never before. You’ll sweat, twist, stretch, and hold all kinds of unfamiliar positions, but you’ll leave feeling energized, invigorated, and maybe even a little enlightened.",
            92,
            24
        },
        {
            4,
            "Legs & Back",
            "Get ready to squat, lunge, and pull during this unique series of exercises for both the lower and upper body. While the main focus lies in strengthening and developing the glutes, quads, hamstrings, and calves, there’s also a handful of some highly effective pull-up exercises to give your legs a quick breather while you work the upper body. Some of the leg exercises during this routine require the use of dumbbells or bands",
            58,
            56
        },
        {
            5,
            "Kenpo X",
            "The word Kenpo means \"law of the fist.\" and that’s exactly what you’ll be throwing during this cardio-intense workout. That and a whole bunch of kicks, elbows, knees, and forearms. You’ll learn a highly effective way to defend yourself, while at the same time getting one heck of a total-body, super-cardio workout. ",
            55,
            46
        },
        {
            6,
            "X Stretch",
            "Keeping limber and loose is vital to the success of any fitness program. Aside from the stretching exercises that take place before, during, and after each P90X workout, we’ve created this entire 57-minute stretching routine to minimize the potential for injury and keep you at the top of your game.",
            57,
            32
        },
        {
            7,
            "Core Synergistics",
            "This total-body workout incorporates cardio, stretching, and resistance to strengthen the core muscles (the muscle groups that gird the waistline and back). Building a solid foundation with strong supporting muscles is the goal of this state-of-the-art workout. By strengthening your core, you’ll be more prepared to tackle the resistance and cardio moves throughout this program, while reducing the chance of injury. You’ll also improve your flexibility, balance, and coordination—all vital to the success of your total-body development.",
            57,
            32
        },
        {
            8,
            "Chest, Shoulders & Triceps",
            "You’ll want to hit the beach and show off your lean, ripped muscles after finishing this intense upper-body blowout. This routine combines a variety of fun and challenging moves that will hit new muscles to build up your strength and definition. Push-ups, dips, flys, and tricep kickbacks constitute the majority of the exercises.",
            55,
            44
        },
        {
            9,
            "Back & Biceps",
            "If Popeye had a favorite P90X workout, this would be it. With a boatload of curls and pullups, you’ll add some real ammo to your guns. But don’t worry, ladies—by using lighter weights, you can focus on toning and tightening those upper arms without adding the size that most guys are trying to develop. Additionally, this workout also provides some great definition to the back.",
            51,
            36
        },
        {
            10,
            "Cardio X",
            "In this workout, you’ll keep your heart rate well below its anaerobic threshold, the point where strength gains are made and muscle fiber is broken down. Instead, you’ll sweat comfortably as your body pumps oxygenated blood through your system, flushing out lactic acid and increasing your number of capillaries. This routine can be performed in addition to your standard P90X workload, or as a substitute if your body needs a break.",
            43,
            18
        },
        {
            11,
            "Ab Ripper X",
            "This quick routine takes only 16 minutes to complete, yet still hits all areas of the midsection to burn the fat and tone the muscle. From sit-ups to Pilates moves, you’ll find everything you need to flatten your stomach and get the six-pack you’ve always wanted.",
            16,
            7
        }
    ]

phase_description = [
        "During this phase, your goal should be to master each movement and finish the workouts in one piece. So for now, focus less on the amount of weight you’re lifting and instead try to achieve your desired number of repetitions while maintaining strict form. Remember to record your rep count and weight amount on your FREE P90X Worksheets, downloadable at P90XWorkoutSheets.com or TeamBeachbody.com/P90X.",
        "If you really want to add some size, now’s the time to go for it. Use enough weight on each exercise so you max out at 8 to 10 reps. If you just want to continue developing lean muscle, use enough weight so you max out between 12 and 15 reps. Never do 11... (we kid you). Also keep in mind that your body only builds muscle while at rest. So try to get at least 7 hours of sleep—which should be easy, because this schedule will wipe you out.",
        "Extreme Muscle Confusion is what this phase is all about. At the onset of this stage, you should be rested and ready to leave everything you’ve got on your exercise mat. No holding back. This will be the time to push to exhaustion and near muscle failure on every single set. Give it your maximum effort, each and every day, and you’ll know the true meaning of X. C’mon—we dare you."
        ]



def createWorkoutEvent(item, dt, organizer, location):
    summary = item[1]
    description = item[2]
    minutes = timedelta(minutes=item[3])
    seconds = timedelta(seconds=item[4])

    event = Event()

    event.add('summary', summary)
    event.add('description', description)
    event.add('dtstart', dt)
    event.add('dtend', dt + minutes + seconds)
    event.add('rrule', {'COUNT': [3], 'FREQ': ['WEEKLY']})
    event['organizer'] = organizer
    event['location'] = location

    return event

def addChestBackAbRipperPhase1(cal, startDate, organizer, location):
    item = workouts[0]
    dt1 = startDate
    cal.add_component(createWorkoutEvent(item, dt1, organizer, location))
    minutes = timedelta(minutes=item[3])
    seconds = timedelta(seconds=item[4])
    dt2 = startDate + minutes + seconds
    cal.add_component(createWorkoutEvent(workouts[11], dt, organizer, location))

def addPhaseOne(cal, startDate, organizer, location):
    # https://bod-cms-assets.prod.cd.beachbodyondemand.com/bod-cms/wp-content/uploads/2017/06/P90X_FitnessGuide_06082017.pdf
    addChestBackAbRipper(cal, startDate, organizer, location)


def _createEvent(summary, start, end, dtstamp, organizer, location):
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', start)
    event.add('dtend', end)
    # event.add('dtstamp', dtstamp)
    event['organizer'] = organizer
    event['location'] = location
    return event

def createEvent(summary, startDate, daysAfterStart, organizer, location):
    return _createEvent(summary,
            startDate + timedelta(days=daysAfterStart),
            startDate + timedelta(days=daysAfterStart),
            startDate + timedelta(days=daysAfterStart),
            organizer,
            location)

def _addPhaseEnd(cal, startDate, organizer, location, week, weekMultiplyer):
    cal.add_component(createEvent("Yoga X",             startDate, 0 + (week * weekMultiplyer), organizer, location))
    cal.add_component(createEvent("Core Synergistics",  startDate, 1 + (week * weekMultiplyer), organizer, location))
    cal.add_component(createEvent("Kenpo X",            startDate, 2 + (week * weekMultiplyer), organizer, location))
    cal.add_component(createEvent("X Stretch",          startDate, 3 + (week * weekMultiplyer), organizer, location))
    cal.add_component(createEvent("Core Synergistics ", startDate, 4 + (week * weekMultiplyer), organizer, location))
    cal.add_component(createEvent("Yoga X",             startDate, 5 + (week * weekMultiplyer), organizer, location))
    cal.add_component(createEvent("Rest or X Stretch",  startDate, 6 + (week * weekMultiplyer), organizer, location))

def _addPhase1(cal, startDate, organizer, location, week):
    cal.add_component(createEvent("Chest & Back, Ab Ripper X",     startDate, 0 + (week * 7), organizer, location))
    cal.add_component(createEvent("Plyometrics",                   startDate, 1 + (week * 7), organizer, location))
    cal.add_component(createEvent("Shoulders & Arms, Ab Ripper X", startDate, 2 + (week * 7), organizer, location))
    cal.add_component(createEvent("Yoga X",                        startDate, 3 + (week * 7), organizer, location))
    cal.add_component(createEvent("Legs & Back, Ab Ripper X",      startDate, 4 + (week * 7), organizer, location))
    cal.add_component(createEvent("Kenpo X",                       startDate, 5 + (week * 7), organizer, location))
    cal.add_component(createEvent("Rest or X Stretch",             startDate, 6 + (week * 7), organizer, location))

def _addPhase2(cal, startDate, organizer, location, week):
    cal.add_component(createEvent("Chest, Shoulders & Triceps, Ab Ripper X", startDate, 0 + (week * 14), organizer, location))
    cal.add_component(createEvent("Plyometrics",                             startDate, 1 + (week * 14), organizer, location))
    cal.add_component(createEvent("Back & Biceps, Ab Ripper X",              startDate, 2 + (week * 14), organizer, location))
    cal.add_component(createEvent("Yoga X",                                  startDate, 3 + (week * 14), organizer, location))
    cal.add_component(createEvent("Legs & Back, Ab Ripper X",                startDate, 4 + (week * 14), organizer, location))
    cal.add_component(createEvent("Kenpo X",                                 startDate, 5 + (week * 14), organizer, location))
    cal.add_component(createEvent("Rest or X Stretch",                       startDate, 6 + (week * 14), organizer, location))

def _addPhase3(cal, startDate, organizer, location, week):
    cal.add_component(createEvent("Chest & Back, Ab Ripper X",               startDate, 0 + (week * 21), organizer, location))
    cal.add_component(createEvent("Plyometrics",                             startDate, 1 + (week * 21), organizer, location))
    cal.add_component(createEvent("Shoulders & Arms, Ab Ripper X",           startDate, 2 + (week * 21), organizer, location))
    cal.add_component(createEvent("Yoga X",                                  startDate, 3 + (week * 21), organizer, location))
    cal.add_component(createEvent("Legs & Back, Ab Ripper X",                startDate, 4 + (week * 21), organizer, location))
    cal.add_component(createEvent("Kenpo X",                                 startDate, 5 + (week * 21), organizer, location))
    cal.add_component(createEvent("Rest or X Stretch",                       startDate, 6 + (week * 21), organizer, location))

def addPhaseWeek(cal, startDate, organizer, location, week, multiplier, s1, s2, s3, s4, s5, s6, s7):
    cal.add_component(createEvent(s1, startDate, 0 + (week * multiplier), organizer, location))
    cal.add_component(createEvent(s2, startDate, 1 + (week * multiplier), organizer, location))
    cal.add_component(createEvent(s3, startDate, 2 + (week * multiplier), organizer, location))
    cal.add_component(createEvent(s4, startDate, 3 + (week * multiplier), organizer, location))
    cal.add_component(createEvent(s4, startDate, 4 + (week * multiplier), organizer, location))
    cal.add_component(createEvent(s6, startDate, 5 + (week * multiplier), organizer, location))
    cal.add_component(createEvent(s7, startDate, 6 + (week * multiplier), organizer, location))

def addPhase1(cal, startDate, organizer, location):
    _addPhase1(cal,   startDate, organizer, location, 0)
    _addPhase1(cal,   startDate, organizer, location, 1)
    _addPhase1(cal,   startDate, organizer, location, 2)

    _addPhaseEnd(cal, startDate, organizer, location, 3, 7)

def addPhase2(cal, startDate, organizer, location):
    _addPhase2(cal,   startDate, organizer, location, 4)
    _addPhase2(cal,   startDate, organizer, location, 5)
    _addPhase2(cal,   startDate, organizer, location, 6)

    _addPhaseEnd(cal, startDate, organizer, location, 7, 14)

def addPhase3(cal, startDate, organizer, location):
    _addPhase3(cal,   startDate, organizer, location, 8)
    _addPhase3(cal,   startDate, organizer, location, 9)
    _addPhase3(cal,   startDate, organizer, location, 10)

    _addPhaseEnd(cal, startDate, organizer, location, 11, 21)

def createP90XClassic():
    cal = Calendar()
    cal.add('attendee', 'MAILTO:jamesfolk1@gmail.com')
    cal.add('attendee', 'MAILTO:natashagabrielsen@gmail.com')

    startDate = datetime(2022, 4, 9, 16, 0, 0, tzinfo=pytz.utc)

    organizer = vCalAddress('MAILTO:jamesfolk1@gmail.com')
    organizer.params['cn'] = vText('James Folk')
    organizer.params['role'] = vText('Organizer')

    location = vText('70 Casey Lane, Mt. Sinai, NY 11766')

    addPhase1(cal, startDate, organizer, location)
    addPhase2(cal, startDate, organizer, location)
    addPhase3(cal, startDate, organizer, location)

    directory = str(Path(__file__).parent) + "/"
    print("ics file will be generated at ", directory)
    f = open(os.path.join(directory, 'p90xclassic.ics'), 'wb')
    f.write(cal.to_ical())
    f.close()

# createP90XClassic()
