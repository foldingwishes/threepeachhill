label bookstore:
    # July 10
    
    "It's been a slow summer. Slower than usual. The buzzing of cicadas and unyielding humidity drown our little town in syrupy hot summer."

    "They seem to say, \"You have all the time in the world.\" A clock hanging by the cluttered storefront counter slowly tic tic tics in agreement."

    "I adjust the angle of my desk fan to get a better breeze. It helps, but sweat still sticks my crisp white dress shirt to my skin."

    "Business has been slow. Too slow."

    "I need to do something about it this summer, or the bookstore might have to close."
    
    "My ear twitches at the sound of bells jingling, the shop door swinging open slowly. I fidget with the fan some more and say,"


    a neutral "\"Welcome in, feel free to browse.\""


    "I look up and my breath catches."


    show erin happy at center:
        subpixel True
        zoom 0.3
        yoffset -350


    "She's adorable. No, beautiful. Her warm brown eyes sparkle, and her dark hair is pulled up into a bun tied with a blue scarf. I have just a moment to take it all in before time freezes."

    show erin shocked

    "She locks eyes with me, her lips parting in an \"oh\" of surprise, and immediately trips over the box of peaches that my neighbor so kindly left by the door for me. Which I forgot about."

    "I knew I should have moved it while it was on my mind. Damn."

    hide erin

    "The fall is epic."

    "I watch it as if it's all happening in slow motion. Her tote bag soars, colored gel pens tumbling out and bouncing across the floor in a myriad rainbow."
    
    "A bundle of loose pages slides out the bag and splays across the floor, some pages really making an effort to escape."

    "Her body slams into the book rack near the entrance, and she pivots, angling the shelf away from the front counter. Away from me."

    "She tumbles to the ground in a heap as the rack slams into a shelf, knocking off an heirloom lamp that, moments before, had minded its own business for as long as I can remember."

    "The girl survived the fall. The lamp did not."

menu:
    "Quick! What should I do?!"

    "Go to the girl":
            $ kind_points += 1
            jump bookstore_Girl

    "Go to the lamp":
        jump bookstore_Lamp




label bookstore_Girl:


    "I rush over to her, taking hold of her arm and helping her upright."

    a shocked "\"Are you okay?!\""

    "She groans as she sits up in a pile of books, clutching at her left shin. She puts a hand to her brow and groans again, this time in dismay, as she sees the destruction her fumble wrought upon the store."

    "The fallen shelves. The shattered lamp. My concerned expression."

    e gloom "\"I'm so sorry, I didn't see the box, I hope nothing...\""

    "Her gaze slides to the broken lamp and she gulps."

    e "\"...well, I hope nothing else got too damaged. I'm really sorry.\""

    a neutral "Don't worry about that right now, are you injured?"

    "She shakes her head and lets me help her up. Up close, she's XX APPEARANCE."

    e sad "\"No, but... The lamp.\""

    jump Deal


label bookstore_Lamp:
    $ lamp_check = True

    "Surveying the shattered lamp yields nothing I didn't already suspect. The glass lampshade was a mosaic of stained glass pieces welded together."
    
    "Four panels had joined at their long edges to create a shade reminiscent of a boxy, blue, crystalline moth."

    "Now, the intricate panels are shattered, the floor a dazzling array of blue edges. The electrical fixture is bent at an odd angle."

    show erin gloom at right:
        zoom 0.7 yalign 0.15
    
    a sad "The perpetrator of the crime groans as she sits up in a pile of books, clutching at her left shin. She puts a hand to her brow and groans, this time in dismay, as she sees the destruction her fumble wrought upon the store."
    
    
    "The fallen shelves. The shattered lamp. My distraught expression."

    "I almost expect her to run away. She's young, maybe a college student? And she's human! I open my mouth to say something, to tell her off or ask if she's okay, but..."
    
    "I can't find the words as I watch her stand up, dust herself off, and limp over to inspect the shattered lamp."

    hide erin with dissolve

    e shocked "\"Oh shit, I'm so sorry about that. I didn't see the box... Here, I'll clean this up.\""

    "She reaches down to pick up a large piece of glass."

    # CHOICE
    menu:
        "Grab her hand":
            $ kind_points += 1
            jump lamp_grab

        "Freeze in surprise":
            jump lamp_freeze



    label lamp_grab:

        "My hand darts out and grabs hold of the girl's wrist."

        a shocked "\"Don't! Don't, you could hurt yourself.\""

        "She freezes, then turns to look me in the eye."

        jump Deal


    label lamp_freeze:

        $ lamp_freeze_outcome = True

        "It takes my brain a moment to catch up to what's happening, and by the time I realize what she's doing, it's too late."

        "The girl quickly starts to put pieces in a pile and hisses in pain when one odd-angled piece slices a shallow line across her finger."

        a neutral "\"Stop,\""

        "I say quietly. But she doesn't. So I say it again louder this time."

        a tsuntsun "\"Stop!\""

        "Finally, she stops fiddling with the broken shards. She clutches her bleeding finger and looks up at me."

        jump Deal