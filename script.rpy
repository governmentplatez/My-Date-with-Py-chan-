# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the

#characters 

define p = Character(_("Py-chan"), color = "#385dff")
define player = Character("You", color = "#000103")





# sprites 

transform half_size:
    zoom 0.3

image p smile = "py mouth open.png"
image p shocked = "py shocked.png"
image p closed smile = "pychanclosedsmile.png"
image p apprehensive = "py apprehensive.png"
image p angry = "py angry.png"
image p blush = "py blush.png"



# The game starts here.



label start:
    
    scene cafe
 
    play music "parisnogogo.ogg"
    player "# I take a walk outside, it's a nice day out....  "
    player "# Today I'm supposed to be going on a date with some girl. I've never seen her before.... I hope she's nice"
    player "# She says to meet me at a cafe. I have been there a couple of times before, the coffee is great."
    player "# I'm approaching the cafe and I head inside. The smell of coffee wafts my nose and I am engulfed by the cozy atmosphere."
    player "# I reach for my phone"
    player "# I wonder if she's here yet...... "
    player "# I begin walking around the cafe"
    player "Suddenly a strange looking woman bumps into me"
    show p shocked at half_size
    p "Ah!!! I'm so sorry!!!"
    "# She has these weird little things on her ears... and shes "
    p "Ah there you are!!!"
    show p smile at half_size
    p "I'm glad we found each other, even if it was on accident hehehe"
    player "Oh so it is you. P.....Py..... What was your name again?"
    p "My name is Pyper, but you can call me Py for short!"
    show p closed smile at half_size
    p "Lets go find somewhere to sit!"
    
    scene seated with fade
    "# We find a nice spot by the window"
    player "So tell me about yourself"
    show p smile at half_size
    p "Well I'm a student at IDE university and I study data science!"
    p "I transferred quite some time ago... 3 months ago I believe"
    player "Nice, that's about the same time I started school."
    p "Ah.. Are you a transfer as well?"
    player "Nah these is my first few years of college ever"
    "# A server comes by and takes both of our orders. She orders black tea with a chocolate chip scone"
    "# I order a black coffee and a muffin"
    "# I should prod her more about what she likes and stuff..."

    menu:
            "What should I say?"

            "Data Science seems super cool! Is it fun?":

                jump isitfun

            "Yaaawn sounds super lame and hard":

                jump itslame

label isitfun: 
    show p closed smile at half_size
    p "Yes!! It is. It so fun to learn ways to analyze data!!!"
    p "And the data can be really helpful for people in the future!"
    player "Hmmm that does sound fun..."
    p "I really love helping others... I help out a lot at the library too!"
    "# I watch her play with her hair excitedly"
    p "My friend lets me analyze the library data sometimes...."
    player "Do you work there or do you just do it for fun?"
    show p smile at half_size
    p "All for fun, haha. It's more rewarding than making money wh"
    p "Your turn. tell me what you do!"
    "# She takes a bite out of her pastry"
    player "I'm a student too"
    "# Her face lights up with excitement"
    p "Woah really! Just like me!!"
    p "Whats your major!!!!"
    player "I'm a computer science major. So I'm pretty much in the same field as you are, heh."
    show p closed smile at half_size
    p "So cool!!!! What have you been learning!"
    player "Math, programming, machine learning, a little bit about databases..."
    player "I've been interested in computer science ever since I was in middle school. So I thought why not just go out there and learn everything I can about it like I've always had."
    p "Wow thats so cool!!"
    p "You wouldn't happen to like video games as well?"

menu: 

        "What should I say?"

        "I don't like them":

            jump inoheartvideo

        "I love them!":

            jump iheartvideo

label iheartvideo:
    show p smile at half_size
    p "Wow really! What kind of games do you like?"
    player "Apex Legends, Minecraft, Warhammer, a few visual novels here and there"
    player "I mostly play PC games, but I have a nintendo switch too."
    p "Which visual novels do you like? I've played a few and some of my favorites are Clannad, Totono.....I really like romance visual novels"
    player "Totono's a classic! I'm a big fan of the When They Cry series!"
    p "I love When They Cry! Though I've only played Higurashi, I definetly need to check out Umineko"
    player "Umineko is my favorite!!"
    show p closed smile at half_size
    "# We talk more and more about our favorite visual novels until the waitress comes over with our food"
    "# She begins digging into her food"
    p "So yummy! I just love sweets so much!"
    player "Which one is your favorite?"
    p "I really like cake! My favorite kind is shortcake"
    stop music 
    play music "orangecoloredtime.ogg"
    show p blush at half_size
    p "Man we really do have a lot in common... You're also really cute!"
    menu: 
            "#What do I say?"

            "You're really cute too, Py-chan":
                jump confession

            "I'm sorry I don't feel the same way...":
                jump noreturnedfeelings


label confession:
    p "Gosh.... You know..... I think I really like you... "
    p  "We have so much in common and you're so fun to talk to..."
    p "And so smart and so cool...."
    p "I think we should be more than friends.. Do you love me too?"

    menu: 
            "# How do I feel?"

            "I love you too...":    
                jump good

            "I don't feel the same way":
                jump noreturnedfeelings


label noreturnedfeelings: 
    player "I'm sorry as much as I really like you, I don't know..."
    player "I don't think I'm ready for a relationship yet..."
    show p apprehensive at half_size
    p "I understand..."
    "# The waiteress comes to our table and we pay for food"
    "# She get's up from her seat"
    p "I hope we can still be friends...."
    hide p with dissolve
    jump neutral

label inoheartvideo:
    show p apprehensive at half_size
    p "Aw man... We have so much in common, I would have figured you're a big gamer like me!"
    player "Well tell me about the ones that you like"
    p "I like playing Minecraft, I've read a ton of romance visual novels.. like Clannad and Totono"
    player "Ah, tell me about those ones"
    "# She explain the plots of both as we nibbled on our food and sipped on our drinks"
    "# It all sounds very interesting but I understand none of it"
    "# I should probably say something else but I have no idea what else to say.."
    "# We don't really have much in common besides being in similar fields of study.."
    "# Ah... this isn't going as good as I thought it would"
    player "I'm sorry for not having a whole lot to talk about with you... The games you play do sound interesting"
    p "That's alright..."
    "#The silence between us is so awkward...Soon she says that she needs to leave to go do something"
    hide p with dissolve
    jump neutral
    


# byad ending
label itslame:
    show p shocked at half_size
    p "Huh? What do you mean..?"
    p "As hard as it sounds, once you start learning and getting the hang of it, it's pretty easy! and I think its pretty intreresting...."
    player "And how long before it starts to become less hard and tedious and more easy and fun?"
    p "...."
    player "My point is, it can't be as easy, fun AND interesting as what I do for school"
    p "Hm... What do you do then?"
    "#I shoot her a smug look"
    player "I'm a computer science major and I'm learning how program. I specialize in python, I use it to make games and all sorts of helpful apps."
    player  "I also know a thing or two about machine learning"
    show p angry at half_size
    p "Well I'll have you know that you can python for data science. Not only that it is an excellent tool for organizing data"
    p "You can use python for data manipulation and data analysis. You can also use machine learning models in order to help organize data "
    player "....."

menu:   
        "# What do I say?"

        "....I'm sorry":
            jump apology

        "Okay well you dress weird":
            jump weird


label apology:
    show p shocked at half_size
    player "I'm sorry. I don't really know what came over me. I was just teasing"
    p "That's alright....... Just don't be so harsh next time okay?"
    "# We sit in awkward silence until our food comes"
    "# We begin eating"
    "# Shoot I should probably say something...."
    player "So..... How's your food....."
    show p apprehensive at half_size
    p "It's yummy... I really like sweet things.."
    player "What's your favorite dessert"
    show p smile at half_size
    "# Her face lightens up a bit"
    p "I really like shortcake! And cheesecake. I really like cake it's my favorite"
    p "Do you like sweets too?"

menu:
        "# What do I say?"  
        "Yes, my favorite is ice cream": 
            jump icecream
        "No, Sweets make you fat":
            jump rude


label icecream:
    show p smile closed at half_size
    p "Ah~ I love ice cream! What's your favorite flavor?"
    player "I think strawberry is the best!"
    p "My favorite is cookies and cream! Strawberry is yummy too"
    "# She finishes the last of her tea"
    p "You know even if you are a little mean, I like you a lot..."
    show p apprehensive at half_size
    p "but I don't think I could see you as anything beyond a friend..."
    player "I'm fine with that."
    jump neutral 



label rude:
    show p angry at half_size
    p "You know if you're just going to keep being rude, I can leave"
    player "Well it's true! They do make you fat if you eat too much of it"
    p "Well why does that matter?!"
    player "All I'm saying is if you eat way too much you're gonna get fat"
    "# She incredibly upset"
    p "As soon as I finish my food I can just leave.... If you really don't like me you could just say that."
    "# She finishes her scone and starts taking sips of her tea"
    player "I was just joking, Py-chan it's no big deal..."
    p "Well jokes are supposed to be funny! You're just being rude!"
    player "I'm sorry"
    p "Hmph!"

menu: 

        "#What should I do?"

        "Offer to buy her something sweet as conpensation":
            jump offer

        "Just say nothing and let her leave":
            jump bad


label offer: 
    player "Hey, tell you what.... I'll buy you a slice of shortcake as an apology"
    p "Whatever you'll just say something about it making me fat again"
    player "It was just a joke! C'mon seriously I'll buy you whatever cake you want after this to make up for my poor behavior."
    p "Even a whole one......."
    player "Yes"
    p "Deal...."
    "# We both pay for our food and leave the cafe"
    jump neutral
    

label weird: 
    show p angry at half_size
    p "Eh?! Whats wrong with the way I look?! You're being really mean!"
    p "Is this some sort of joke?"
    player "Nah, I'm serious why do you dress like that"
    player "What are those things on your ears?"
    show p shocked at half_size
    p "I-I don't know I was just born like this...."
    player "Oh really?"
    "# She nods"
    p "I've had these ever since I was little.... I can't take them off ever"
    player "And what happens if you do?"
    p "I don't know....."
    player "Really? You've never tried to take them off ever"
    "# She shakes her head"

    menu:
            "#What do I do?"
            "Reach over the table to take them off":
                jump yoink 

            "Try to change the subject":
                jump change

label yoink:
    "#I reach over the table and try to take the two crosses off of her ears" 
    p "EEEEK!!!"
    show p shocked at half_size
    "#She slaps me"
    show p angry at half_size
    p "WHAT IS YOUR PROBLEM! YOU CAN'T JUST DO THINGS LIKE THAT"
    player "But I justed wanted to know whats under them"
    "#I try reaching for them again, she slaps me even harder"
    p "I was really hoping that we could be friends or probably something more but you just seem like such a jerk!"
    p "I was really excited to meet you too... Why did things have to end up this way."
    jump bad



label good:
    show p blush at half_size
    "# We pay for our food and head outside"
    "# Py-chan looks at me, I look at her"
    "# She stands on her tip-toes and leans in for a kiss"
    "# I accept the kiss, once I release her lips from mine she says something to me"
    "# I understand nothing, she's only making beeping noises for some reason"
    stop music
    play sound "alarm.ogg"
    "# The beeps get louder and louder"
    player "Py-chan..?"
    hide p with dissolve
    show bedroom with dissolve
    "I wake up on my desk and my phone alarm is blaring in my ear loudly. I reach over and turn it off"
    "I must have dozed off......"
    "I look down at my Py-chan drawing.... Such an odd dream"
    "I rub my eyes and look up at my PC screen"
    "My homework is all done... Huh..." 
    return 

label bad:
    stop music
    p "Goodbye"
    hide p with dissolve
    "#She gets up and walks out of the cafe"
    play sound "ringtone.ogg"
    "# There is a faint beeping in the background and suddenly it gets louder and louder"
    show bedroom with dissolve 
    "I wake up on my desk"
    "Huh...."
    "What a strange dream.... I do feel bad though I feel like such a jerk"
    "I wake up on my desk. Dammit I must have fallen asleep doing homework again."
    "I look down at the sketchy of Py-chan in my notes under where I slept"
    player "Sorry I was so mean to you...." 
    "I boot up my PC. I wonder how much I got done before I dozed off"
    "EH?! All of my code is gone!"
    return 

label neutral:
    stop  music
    hide p with dissolve
    show bedroom with dissolve 
    "I wake up on my desk"
    "I look down at my doodle of Py-chan in my notes"
    player "Weird..."
    "Ah, I forgot I was doing an assignment..."
    "I boot up my PC. I wonder how much I've gotten done before I dozed off"
    "I only did half of it I'd better get it done before it ends up being late"
    return
