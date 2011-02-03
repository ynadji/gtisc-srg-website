import sys
import datetime
from dateutil.parser import parse
from optparse import OptionParser

def springfall(today):
    if today < datetime.datetime(today.year, 6, 20):
        return "Spring %s" % str(today.year)
    else:
        return "Fall %s" % str(today.year)

def obfuscateemail(email):
    return email.replace('.', ' DOT ').replace('@', ' AT ')

def main():
    """main function for standalone usage"""
    usage = "usage: %prog [options] firstday lastday"
    parser = OptionParser(usage=usage)
    parser.add_option('-o', '--organizer', default='Yacin Nadji')
    parser.add_option('-e', '--email', default='yacin@gatech.edu')
    parser.add_option('-w', '--website', default='http://yacin.nadji.us')
    parser.add_option('-l', '--location', default='GTISC War Room (KACB 3126)')
    parser.add_option('-t', '--time', default='Thursdays, 11 AM - 12 PM')

    (options, args) = parser.parse_args()

    if len(args) != 2:
        parser.print_help()
        return 2
    header = \
"""<html>

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=US-ASCII">
  <base href="http://research.gtisc.gatech.edu/srg/">
  <title>Security Reading Group</title>
</head>

<body>

<table width="650" align="center">
<tbody><tr>
<td>

<h1 align="center">GTISC Security Reading Group <br>%s</h1>
<hr width="100%%">

<h2>Overview</h2>
<p>
The GTISC Security Reading Group</b> is a weekly informal seminar for discussing research papers, new ideas and GTISC student research. This semester the SRG is organized by <a href="%s">%s</a> and run by all of the students in the GTISC lab. Lunches are paid for by <a href="http://www.gtisc.gatech.edu">GTISC</a> (thanks!). If you are interested in participating, please read the "Informaion for Participants" section below. If you have any questions please contact &lt; %s &gt;
</p>

<p><b>Location</b>: %s</p>
<p><b>Time</b>: %s</p>
<p><b>Mailing List</b>: <a href="https://mailman.cc.gatech.edu/mailman/listinfo/security-reading-group">SRG Mailman Page</a></p>

<h2>Schedule</h2>
<table cellpadding="5" cellspacing="1" border="1" width="100%%">

<tbody>"""

    footer = \
"""</tbody></table>

<h2><a name="ParticipantInfo">Information for Participants</a></h2>
<p>If you are presenting a paper, it should be recent (preferably not more than a year old).
The paper can be from any conference, but good ones tend to be published in places like:
IEEE S&P (Oakland),
Usenix Security, NDSS, CCS, SOSP, OSDI, SIGCOMM, or NSDI.  Papers from other
conferences (e.g, RAID, Esorics, ACSAC, DSN, IMC) are acceptable if the paper is
<emph>interesting</emph> enough. Interesting is an intentionally flexible term; we all
read big papers in our area at the major conferences so please feel free to present work
you find to be creative/cute/etc. if you think it's worth knowing about. The paper doesn't
have to be perfect, but it should bring about interesting discussion. Everyone should read
the paper beforehand, but this doesn't happen very often so keep that in mind when you
present.</p>
<p>If you are practicing for a conference, let the group know if you want to be: timed,
(not)? interrupted, etc. before you begin your talk. We will provide as much feedback as
possible to prepare you for your presentation.</p>
<p>If you would like to present on your current work or a new idea for the purposes of
receiving feedback, the format is very open-ended. Slides, dry-erase board, whatever you
want as long as you let the organizer know ahead of time if you need anything special.
Bear in mind that whatever you do should take up the whole meeting time, so come prepared.
The more information you can provide (an abstract instead of just a title) the better.</p>

<h2><a href="archive.html">SRG Archive</a></h2>

</td>
</tr>

<tr><td><p><a href="https://github.com/ynadji/gtisc-srg-website">GitHub page</a></p></td></tr>
</tbody></table>

</div></body></html>"""

    nocolorday = \
"""<tr>
<td>%s</td>
<td>
  <p><b>Presenter</b>: <br />
  <b>Topic</b>: </p>
</td>
</tr>"""
    colorday = \
"""<tr>
<td bgcolor="#dddddd">%s</td>
<td bgcolor="#dddddd">
  <p><b>Presenter</b>: <br />
  <b>Topic</b>: </p>
</td>
</tr>"""

    # do stuff
    start = parse(args[0])
    today = start
    end = parse(args[1])
    delta = datetime.timedelta(7)
    options.email = obfuscateemail(options.email)

    print(header % (springfall(today), options.website, options.organizer,
                    options.email, options.location, options.time))
    i = 0
    while today <= end:
        day = nocolorday if i % 2 == 0 else colorday
        print(day % today.strftime("%b %d"))
        i += 1
        today += delta

    print(footer)

if __name__ == '__main__':
    sys.exit(main())
