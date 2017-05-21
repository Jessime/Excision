Decisions
=====

File parsing with a touch of statistics
-----

It's Sunday evening and you're sitting in your house staring at the computer. You can't figure out what to do. You've got work in the morning, so you really shouldn't stay up much later. But you feel like if you just sit quietly for a little bit longer you might get the inspiration you've been looking for. It should be so simple; all you have to do is put yourself in their shoes. What would you need if you were in their position? But the words on the screen are doing nothing to make you think like them. Maybe if you were just a little more… what's the word? Sociopathic.

Despite having a thousand things on your plate, the weekend hasn't been productive as a whole. Sure, you have taken care of a few technical details, getting some operational systems up and running, but you have bigger fish to fry. It can be difficult ramping up a large undertaking like this, true, but that really isn't a good enough excuse when you have people depending on you. Come Monday, how are you going to explain to your team that they'll be waiting even longer for their assignments because your constant indecision forced you to marathon two seasons of House of Cards this weekend instead of doing your job? It isn't acceptable. You take a deep breath and mentally gear up to go over the facts one more time.

The past year of your life has catapulted you from a Novice at the Academy to the head director of the Agency, making you far and away the youngest director in the storied history of the institution. The circumstances which lead to your rise were decidedly unpleasant and have left you with a laundry list of equally unpleasant tasks to resolve. Namely, the full weight of the Agency has found itself pitted against Gene Corporation, which is currently one of the largest organizations on the planet. Gene Corp has a wonderful public image known for quite literally 'healing the sick and curing the blind'. While the technologies they have created have revolutionized several areas of life, you've seen their dark underbelly first hand. Just last week your team found some decently solid evidence that one of Gene Corp's subsidiaries, Theraptrix has been bribing the environmental officers in Oregon for years. They have been using the freedom they bought to pump waste chemicals directly into the air instead of following waste treatment and filtering protocol.

Bribery and industrial waste may or may not seem like fact-of-life issues when dealing with large corporations, but there's also the evidence that Life/Better, LLC (another child company of Gene Corp) has been illegally testing neurotropic drugs on pregnant women. Oh, and there was the incident when Gene Corp used an artificial intelligence system system to assassinate your mentor and attempted to take over the world. Besides Theraptrix and Life/Better, LLC, Gene Corp has another 47 companies under its name.

The problem is that this giant is in full armor and ready for a fight. You don't have the resources to take it down all at once. Your only option is to divide and conquer, taking out the subsidiaries one at a time. But where should you strike first? That question is the heart of your indecision. Where is Gene Corp investing most of their defenses? What do they expect you to do? You know that if you lose this initial battle, your chances of winning the war decrease dramatically. You currently have the best cases against Theraptrix and Life/Better, LLC, but at which of the two should you direct your focus?

With a sigh, you decide to let the numbers make the choice. Yesterday, your team recovered a DNA sequencing data set performed by Theraptrix on a sample population of people near their main factory. The informant who aided you in acquiring the data says that Theraptrix suspects they may be causing genetic mutations in Oregon residents. If, on top of the bribery, you can prove a statistically significant difference between mutation rates of people in the Oregon data and a control population, you'll concentrate your investigation on Theraptrix. Otherwise, you'll go after Life/Better, LLC.

Oregon Trail
=====

An introduction to arrays
-----

You walk into the office Monday morning and make an announcement. A team is going to head out to the Theraptrix plant as soon as they can get their bags packed. You'll lead the expedition with Anita, who you've promoted to coordinate the investigation against Gene Corp.

Within the hour, you've boarded the jet. And by the time you're in the air, you and Anita are deep in conversation, trying to play out possible long-term senarios. You've ask Anita about her thoughts on the Konrads. Rumor has it that the current CEO of Gene Corp is nothing more than a figure head. It's a pair of Polish twins, the Konrads, running the ship as COO and CTO. Anita replies that she's been researching the possibility of playing the twins off one another, in an effort to distract Gene Corp's leadership while the Agency is building their case.  

Your plane touches down in Klamath Falls Airport near Medford Oregon, and  you head straight to a local place called Sherry's Shack where you can grab a sandwhich. Sherry, somewhat of a minor celebrity in these parts, serves lunch to you herself. She tries to strike up a bit of a conversation since the restaurant isn’t busy this late in the afternoon. You and Anita are also using the Shack as an operations base, so you're thankful when Sherry quickly picks up on the tension and moves on to the few other customers currently in the diner.

The goal for today is simple: gain access to Theraptrix's file system, particularly their projects directory. The path to achieving this goal is less simple. After all, while the current plan isn't strictly illegal, it definitely isn't by the books. If you offically issue a warrant for the data, they'll just delete it before you can get to it. Instead, you're going to have a member of your team join each of the factory tours given today. Each team member will sneak in an extremely low power digital thermometer past Theraptrix's device detector. The good news is that the thermometers are inconspicuous enough to not trigger alarms, and are capable of creating a 2D map of temperatures in the building. The bad news is, these devices are so low power that they aren't particularly reliable. That's why you're sending in multiple agents (that, and so agents now have the option to abort if necessary, without ruining the mission). The consensus of the devices, however, should provide a literal heatmap of the building.This means you'll be able to find the server room by finding which location is hottest.

Anita and you can use the rest of the day for additional planning, as soon as you write this program. Down time is rarely in excess, so you'd better get writing!

T
=====

Analyzing structured data (Part I)
-----

All portions of the mission have been going exactly as planned. You've got the location of the servers. Joe, the last field agent to go on a tour of the Theraptrix plant, swipes an employee access card on his way to the "restroom". Within four minutes, he's ducked inside the server room, inserted the 512 GB micro flashdrive he'd hidden in his shoe, copied the contents of one of the server disks, and returned to politely inform the employee that they must have dropped their badge on the ground at some point. It would have been ideal to access to more data, of course, but this flashdrive will have to do.

It doesn't do. Joe was lucky to have gotten out of there at all, because you must have triggered some sort of alarm. Your best guess is that the Theraptrix security system doesn't allow unauthorized USBs. Upon looking at the contents of the USB and realizing that you've gained approximately 512 GB of pure garbage, you do three things. First, you make backup copies of the only two files which appear to be of any consequence. Second, you disconnect from Sherry's free WiFi and wipe your own system. Third, you pack up your team and leave Oregon.


All this work for two files. And not even that. The first file, entitled five_prime_colossus.pdb, now only contains a single line:

HEADER    TRANSPORT PROTEIN                       22-JUL-15   5A

The second file, ENCFF239FSU.bed, appears to contain genomic coordinates. Given that this is your only lead for the moment, you'd better find a way to connect ENCFF239FSU.bed with the pdb file you found.

