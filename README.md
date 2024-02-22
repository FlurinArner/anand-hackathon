# anand-hackathon
Build catapults and possibly a drone, to shoot down a programmable Roomba.

## General Idea
Create a game a random walk/RC car is targeted by competing catapults.

### Components:
- 1. buy base RC (omni wheels?) with controllable/programmable motion
- 2. build catapults to shoot at target (programmable or mechanic?)
- 3. small drone with release mechanism to drop "bomb"
- fallback to manual shooting if too complex or insufficient funds

- 4. video summary of weekend or trailer of the game
- 5. OpenSource all code on GitHub
 
## 1) The current idea for the BaseTargetPlatform is this:
- use the [Roomba SCI](http://www.robotappstore.com/Knowledge-Base/1-Introduction-to-Roomba-Programming/15.html) (list of commands that can be sent to the Roomba, [docs](https://www.usna.edu/Users/weaprcon/esposito/_files/roomba.matlab/Roomba_SCI.pdf), possible [C++ library](https://github.com/steventwheeler/libroomba)), programmed on 
-a [Arduino](https://www.mouser.ch/ProductDetail/Arduino/ABX00087?qs=ulEaXIWI0c%252Bc7tXbIsM2Bg%3D%3D) (23.-, ARM-based microcontroller) or [RasPi](https://www.mouser.ch/ProductDetail/Raspberry-Pi/SC0065?qs=rQFj71Wb1eX99SHol2bUwA%3D%3D) (14.-, ARM-based single board computer) to control
- a [Roomba 780](https://www.tutti.ch/de/vi/aargau/haushalt/geraete-utensilien/roomba-780/63396971) (~50.- on tutti)

Option:
- if manual control of BaseTargetPlatform is desired
  - ~~over WiFi with [NodeRed](https://nodered.org/) on a [droplet](https://www.digitalocean.com/products/droplets)~~ (too complex)
  - connect to "playstation controller" remotely with USB adapter (I have one at home)
Fallback solution, if programming Roomba is too hard:
- let the roomba do its work autonomously 😂
 

## 2) The catapults could be entirely "mechanic". 
The aiming and control of the catapult power (how FAR it shoots) would be entirely controlled manually. 
This way we'd include a more hands-on part to the hackathon, which non-coders could also find fun! 

Either we find buildable small model catapults which you can buy as such, or we can come up with a concept of how this could be best achieved for this purpose!

## 3) Separate drone and gripper systems 
The only doable option I see, is separating the drone from the gripper. A Tello drone (from DJI) is available, but it needs new batteries. After checking buying options, [this](https://www.galaxus.ch/en/s1/product/ryze-tech-tello-boost-combo-13-min-80-g-5-mpx-drone-9458332?shid=1324845) used one from Galaxus is the cheapest and quickest solution for the batteries. We even would get a second drone for the 117.-, not just the needed spare parts.. This way we have a usable drone, which I think would serve the purpose. If someone wants to go through the drones available on tutti.ch ([example](https://www.tutti.ch/de/vi/luzern/spielzeuge-basteln/modellbau/neue-drone/65372639)), feel free =) I don't want to spend more time evaluating which drones might work and which ones are too flimsy.. 😬

Now we "only" need to find a remote button (IR or bluetooth switch or so?), which can trigger the open/close of the gripper to "drop the bomb" 😂

## 4) Video summary of weekend or trailer of the game
Someone still has to take the lead on this topic. One simple proposal is using a GoPro to create a timelapse of the hackathon.

## 5) OpenSource the code and documentation for the hackathon
Th present repository serves this goal.
