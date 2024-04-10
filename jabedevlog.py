import random

def generate_paragraph(intro_sentence, body_sentences, conclusion_sentences, num_sentences):
    
    paragraph = [intro_sentence]

    
    for _ in range(num_sentences - 1):  # Subtract 1 for the intro sentence
        paragraph.append(random.choice(body_sentences))

    
    paragraph.append(random.choice(conclusion_sentences))

    
    return ' '.join(paragraph)


intro_sentence = "Seb's Devlog #69: 9/11/2001 What happened?"


body_sentences = [
    "A new redesign for two things, the character sprites (Again) and the thumbnail, which is being planned. That also includes the title screen for possibly THREE more screens. I'll get into that later by the next devlog, but let's talk about why I wanted to do a redesign the character sprites. ",
    "While true, it sounds REALLY redundant, this is because there's no other way for me at least to make ANOTHER costume for Sasara. While I can't say much about it (Because it's more or less story relevant for her later on.), the point is that I don't think a chibi version of her new form would work, so I thought why not redesign it to the point where every character has a sense of proportion because well, 48x48 is limiting but I don't see why I shouldn't increase more so expect sprites to be 72x72 or so. ",
    "Now the thumbnail, there's nothing wrong with the thumbnail itself, it's that I kinda want the thumbnail to match the title screen for the game. Now, unlike the other thumbnails or title screens, the difference is that I wanted the emphasize on the characters mainly to show the whole friendship mechanic for the game. ",
    "Sure, the previous thumbnails did show the party, but not so much of the emphasize and just still. The first one was just four characters facing mostly forward, but I wanted to change that, so then the second thumbnail design came in. While there's no problems with it, in fact I like to an extent it's arguably my second favorite BECAUSE it's made within 16:9 and 4:3 back when I thought it would be easy to upload the game on Itch.io. It isn't, but it doesn't reflect the emphasized mechanics of current JABE, so a redesign is needed. ",
    "Well, there is progress going on. ",
    "Well not much to say, aside from thinking about how I'll write for another game that I'm working that'll hopefully be out on April 1st. ",
    "I guess. ",
    "Not much to write, but I am going to write a documentary. ",
    "Now, the purpose of the documentary serves as a way for me to write another thing for another game. ",
    "The important thing about the documentary is that it serves as a ''how NOT to program events in RPG Maker.'' ",
    "Yes, I'm reworking on the Main Party portraits because when you have new artwork, you're going to have to replace the old ones or else there's going to be inconsistency. ",
    "Well shit, missed a date. Oh well, that's because I was too tired to do it. ",
    "Now I have done some new image assets for both Kabi and Imasu. Yes, I'm doing it in reverse but ehh... So here's the comparsions. ",
    "Surprise, today's the day I'm telling you that JABE is going to have a graphical makeover. ",
    "Now, for starters, I'm redoing most of the party member's face artwork. How can this be? Mainly because for one, the old artwork isn't exactly up to stuff in my tastes, so we're going to redraw a lot of faces, which means possibly better expressions and also better ways to demonstrate the character's personalities more. ",
    "I don't like Sasara's face artwork and that's mainly because it feels out of place for her. She's a tomboy but we only get to see her eye expression more than the general facial expression you can see, which is something that would best suit for Imasu. I don't know why I drew it as is, though fun fact, she's the only one that's drawn with a symmetrical tool, because everyone else doesn't. To compensate Imasu's lack of facial expressions, I thought of his face artwork including some hand gestures to not only contrast with the other party members, but also makes you actively pay attention to what he's saying. ",
    "And also it does include the thumbnail as well and along with the description of the game, just that I've not planned on what is going to be changed exactly. ",
    "Not much progress to speak but hopefully I get more content out by next week. ",
    "Okay, I skipped a day, whatever. ",
    "As mentioned before, I'm working some effort onto the game. ",
    "Now, obviously I don't have any video project to demonstrate what I can do in Vegas Pro yet, but if it's done and ready to go, then I'll show it in here, but again, I'm setting up the new standards here. ",
    "But the important thing here is NO trailers until the games' (Yes, PLURAL.) are around 99% done. If it's done, then I can make a trailer for them. This is so that I can just focus on fixing bugs more rather than shoving in new content that require WAY more time to finish with. ",
    "And I don't mean all of the games altogether, I mean when that game meets that standard. So yes, JABE is technically getting another trailer, just no promises for it. ",
    "Though I have an idea for JABE, now, considering how friendship works, as a standard likes me, likes me not thing that affects the story to some degree and also gameplay. ",
    "But then when I look back at Persona 3's flawed albeit crucial Social Links and also game overs for Hotel Dusk, I thought of something. ",
    "Why not make friendships be progressed like Persona 3's Social Links BUT a broken social link is presented much like a Game Over from Hotel Dusk, except the game doesn't end when this happened. ",
    "Essentially, let's allow the player to make BAD choices that affects not only characters, but also gameplay. ",
    "The idea would be if you were to complete a friendship with a character, this causes two things, your friendship is locked into the Like status and this will improve abilities of the characters. ",
    "For example, completing Imasu's friendship increases his max SP. However, if you were to fail a friendship with say Kabi, this causes the relationship to be in a shattered status, Kabi can Snap much more easily, as the minimum to trigger this is lowered and the chances are much increased for her, not to mention this rage further empowers her. ",
    "A shattered status locks away the player's ability to enter or stay in the Like status, which forces them to stay in either a neutral or sink down to a hate status. Whether these abilities can serve an advantage to the player or not ultimately depends on your choices.So anyway, I made a new game that I'm putting effort into. ",
    "...Although effort and a shitpost sounds like two things that don't mix well. ",
    "But hey, at least I can test out my new video editor and that's Vegas Pro 18. Finally, a better video editor than fucking Movie Studio. ",
    "Okay, so let's talk about ZDSFLP. Now, if you're here for the standard JABE news, start skipping this until a seperator appears. Okay go. ",
    "Now, why cancel ZDSFLP? It's not interesting enough to develop the game anymore. Now, I set out to make games for the passion of the medium of itself, I play lots of games, like The Denpa Men, Sonic Unleashed (Although I got the Wii version.), WarioWare Smooth Moves, that stuff. ",
    "Sure, I'm the only one or there's another person helping me out developing the games, but the problem is that the project isn't interesting as something like Zane's Bizarre Candy Hunt. ",
    "I don't set out to make games and then later on cancel them, but that gets harder the more you work on said passion. You see, what makes these games separate despite having ZANE in it is how Zane is depicted. ",
    "You see, Zane's a character in the Mangled Kitten Dragon, or rather by a friend of mine named Sharkynatty. And for ZDSFLP, it followed a more different lore. In Mangled Kitten Dragon (Or just MKD), Zane's a byproduct of two scientists (One of them is named Natty, the other depends on which version you're talking about, old MKD had Barney and new MKD had Matthew.) and she's a hybrid cat-dragon. While ZDSFLP does follow who Zane is, their lore and personalities are different enough and kinda shows why I'm not interested in continuing it. ",
    "Now, in ZDSFLP, Zane's more shaped by player's choices, she's not as assertive compared to Enaz (Who has a completely different personality.) but she's a woman who can stand up for herself, except she's torn by two people, Enaz, her girlfriend, and Anthony, a muscly neighbor she also has feelings for. ",
    "Depending on choices in the game, you can have one of the other or BOTH. But this design is, dare I say, stolen from Catherine and that already does the thing better, just not as a turn-based RPG or any LGBT+ themes tied in. "
    "While you might think it's interesting to explore a conflict by the character's goals, original Zane is a completely different bitch compared to ZDSFLP Zane. And that's because she IS a bitch towards others. ",
    "Zane's a nutjob conservative who insists she identifies as a dildo and that women should belong in the kitchen. She can't entertain the idea of men who don't fit the stereotypical bill despite the fact that she's more of a tomboy. ",
    "LGBT+ people? Fuck that, she could care fuck less if her son's bisexual, but she would care more if he looked a lot more like Adam, her husband and father of Alex, the son, and Amelia Jr., the daughter. Top of that, she's sexually harasses a lot of people. ",
    "Whether it's a family member, her son or daughter, or not, she could care less about it; nobody can rival her insane libido and nobody is allowed to question about it. Now tell me, what would be a fun character when it comes to creating drama or conflict, a tomboy who won't cause problems on purpose and the drama's driven on her indecisiveness on whether or not she wants to bang a chick, a dude, or both, or a unlikable demented sex offender who's a mother of two children who does causes problems ON purpose? My answer is the mother. ",
    "Okay, so let's talk about JABE. So remember last Sunday I was talking about Cat Slimes, so let's elaborate at the colors more. ",
    "So this is what colors Cat Slimes have. ",
    "Now, out of the 12 colors I've mentioned, only 9 of them are used, but why just 9? This is because of two things: One, I want to make them colorful, so no white or black slimes (Which would make them hard to see depending on what map they're in.), and two, this is because of the limitations of the NES's color palette. ",
    "You see, the NES has actually 52 colors, so let's take a look at said 52 colors. ",
    "Now, the thing is that some colors just don't work, like yellow, magneta, or pink, and that's because of rules I set up. First of all, the color schemes should not have the same shades of color. ",
    "This means red cannot share the same dark shade for green and vice versa, so if it's fails that rule, it doesn't get used. Second of all, a color scheme should at least match what the original scheme is. ",
    "Purple is harder because its' color barely matches any in the palette, it can get closer to the hue but not in saturation or vice versa. So those colors get thrown out. So in actuality, there's only 6 colors used here. ",
    "Not much... But let's talk about redesigns and stuff! ",
    "Okay, so first up, the characters. Yes. Nerd is going to be in the game somewhere. Don't know exactly where but I'll get to that later. ",
    "When I compare the writings of characters from how the project was back when it was still called ''Jonathan's Adventure'', no bullshit ''Classic'' or Doom references, Kabi's the most unchanged character, while Sasara is the most changed one. ",
    "Why? Because Sasara is the one character that I didn't know how to write, but then I realized something: why not design her character around her background AND design? Make her a competent tomboy who's good at fighting but she doesn't have a family because she's a Rotom, she can't have one. ",
    "Imasu has changed much like Sasara, but not enough on her level, so his flaw is that despite his experience and much of a guy who's independent and smart, he's not a guy who can express much emotion from his stone face and not much of an extrovert. Jonathan... Well, he hasn't changed much. ",
    "Though when redesigning the characters, I did consider their Zodiac signs for their characters, so Jonathan's a Gemini, Sasara's an Aries, Imasu's an Aquarius, and Kabi's a Pisces. Yes, this means the other birthdays aren't correct anymore, but I treated the birthdays for them when playing Tomodachi Life as a mundane detail. Hey, it's one way to design the characters, I was like the guy writing most of the plot myself. ",
    "Though just in case, I'll leave the drafts of what was JAC going to be somewhere in the final version of the game because it was like one of the things that I kinda don't wanna leave out. ",
    "Second of all, let's talk about enemy design! It's sorta not my thing. ",
    "Okay well, it is, it's that putting in monsters isn't really my kind of deal. Though I have struck a chord in the third dungeon and that's because of Cat Slimes. Originally, I wasn't expecting these monsters to appear ANYWHERE in JAC. ",
    "There's not really a place for them to appear aside from maybe in the first dungeon but that's because it's a dump of RPG Maker MV art. But a third dungeon that's meant to be a RPG game would be a place for these little fuckers and so it is. ",
    "Not much, but hey, at least I'm making some progress. ",
    "More sprites as usual for Secret Pokemon Game. ",
    "Though for the Gardevoir faces, I tried to use a process where I draw the face in 144x144, then I linear scale it down to 48x48, and use said results as more like a traced reference. But because my computer crashed the minute a Japanese guy says: So say something like: You smell bad, die! It screwed me over BIG TIME.  ",
    "So that means I have to redo the title screen (Because I need to change the logo for other languages just in case.). Thankfully I do my pixel art in Aseprite and it recovers whenever my PC crashes or I'm too lazy to close down every single tab. So here's what the work I was referring to looks like now. ",
    "Not much, but let's talk about the game I was blabbing about last time, which for the sake of THIS devlogs, let's call it the Secret Pokemon Game, or SPG. ",
    "Though if there was any problems with this, it's that originally I wanted to do like patterns you see in print manga, which a LOT of artists use as a way to convey different colors, since they were printed in black and white. In case if you don't know what I'm talking about, it's basically something like the comics you make in WarioWare: DIY. Except I don't think people use pixels for them. ",
    "Also working on a new project but this time, it merges the idea I had from like several devlogs ago and combine them into one project. ",
    "This project, let's call it the Pokemon Part Project, is a RPG game that the story is in parts. Part 1 and 2. For two parts, you have seperate parties. Part 1 is much different from Part 2, in which in that one, if the Hero dies, then it's game over, which Part 2 explains as to why this mechanic ONLY exists in that section of the game. Two, what you see in either part may conflict each other. ",
    "This is because in Part 1, the Hero is a unreliable narrator. And three, I tried to get a group of people to throw in some ideas for the game, but it wasn't what I was expecting. I did get ideas BUT the amount of them was under my expectations. ",
    "What, you were expecting a Tomodachi Life segment? You're not getting it THIS time. ",
    "Now, the Ink Game has around 8 chapters on the main project, while the 9th chapter is arguably in the development hell build. I think Chapter 8 really needs a overhaul because a lot of ideas thrown into it really NEEDS to be cut or reworked. I swear, the chapter itself was just too big compared to the other chapters, so it had to be cut down. ",
    "Something like breakable screwdrivers or fail events for unscrewing events had to be scrapped because they would've made the chapter be longer because you would have to go steal more of them from the guards, which isn't in the build yet. ",
    "Speaking of more complaints about it, the most difficult part of it was designing 4 puzzles you have to complete in order to progress to the next chapter. While I decided that one puzzle was based on Chess, the other based on your progress in the game, I haven't even remotely thought of what the other two puzzles are. ",
    "I don't know, maybe I feel sadistic enough to put in something like this or maybe, if I feel like a complete sadist, a teleportation room puzzle. ",
    "Now, I'll probably plan out to do some work for JABE, which at least we're getting SOMEWHERE. ",
    "So anyway I finally graduated so at least a new place to learn. Now, the next thing I was doing was more writing and more graphics, since Sven, as much I needed his art for the projects, doesn't wanna do it, since requests are closed, so I had to do some sprites on my own, which isn't horrible, but again, I wasn't expected to be thrown at a different art style that I don't have the necessary experience to replicate what I wanted, but you gotta do what 'chu gotta do. ",
    "Except animating Sasara/Sasha bitch slapping is something I'll be proud of for this year, but that's for the project I was talking about from the previous devlog. ",
    "...Speaking of devlogs, since obviously this time I'm skipping the Tomodachi Life segment AGAIN, I'm not so sure if I should end the segment by the end of this journal. I don't know, but if we get there, we'll get to it. ",
    "But back to the project, I was going to insert ANOTHER title screen, but this time it was a reference to Redline Rumble 2: Detonator, but considering the font for Detonator is actually an original, I was feeling impatient to finish it, considering I got a bunch of other requests to fulfill at this week. So maybe it'll go in the trash...? I don't know. Maybe I'll actually finish it. ",
    "But I wanna note something. ",
    "It's so weird seeing a blip that basically means SOMEONE out there has actually downloaded a build of JABE, because normally, it would just be nobody doing so, but I guess last week's lucky today? But I'm not praying it will go higher when I mention this. ",
    "Since last week was finals for us, this meant less time for the projects, so essentially that wasn't so much progress and I'm delaying the Tomodachi Life segment to the next devlog. Yeah, can't win it for my poor time management skills for this first Sunday. ",
    "So essentially you'll still have the JA cast, just in a different game. It's not like JABE, it might be similar in terms of gameplay, but I'm not going to say it's like JABE. Mainly because of how the Difficulty selection is handled. You see, because I'm using RPG Maker 2k3 instead of MV or MZ, it doesn't have a way for developers to create a streamlined difficulty option. ",
    "Another reason why it's not like JABE is because the story's much more shorter. I would say that assuming if you want to play the game by the plot itself, I would say that the game would be definitely shorter than JABE and there's nothing wrong with that. It's a special game made for a special occasion, so I don't see why it needs to be long unless the plot demands it. It wouldn't hurt to have a game be that short. ",
    "Currently making new costumes for the game. Now, costumes are purely cosmetic, they exist more or less as a way to have references to other media and that kind of deal, except for one equipment type but that's until the game's released.",
    "There IS however costumes that can affect the story, and that's mainly a set of costumes that are a reference to another work that I'm also working on, but don't get your hopes too high; it simply affects only the party member's names and it only adds debatably TWO cutscenes, because one can be completely missed if you're not wearing the costumes at the time, while the other isn't assuming you have the costumes.",
    "I don't know when am I going to redesign the place here, so expect it to happen probably unannounced.",
    "and frankly my dick was fucking weird yesteday because my foreskin got some sort of cut or something, but i didn't wanna tell anyone about it because why the hell would they wanna know ",
    "no, it wasn't that, i just stroked too hard so it's arguably why ",

]


conclusion_sentences = [
    "That's all for this devlog and for this month, see you next month.",
    "So anyway, I can't mention much progress so I'll see you next time... On the last Sunday.",
    "I can't remember much from last week, but yeah, there will be progress to show by next week. See you then.",
    "There's not much I can talk about right now, so see ya next time.",
    "Yeah, see you next month. Bye.",
    "So I'll see you on the next Sunday, see ya.",
    "See you then.",
    "So yeah, that's all for the devlog, thank you for reading this.",
    "So see you next time",
    "See ya.",
    "Okay bye.",
    "See ya on the next week.",
    "That's it for today.",

]


num_sentences = 3


generated_paragraph = generate_paragraph(intro_sentence, body_sentences, conclusion_sentences, num_sentences)
print(generated_paragraph)
