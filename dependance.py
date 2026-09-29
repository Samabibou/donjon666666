from principal import *


bumpers = [Stickers("princess","mononoke","XL",15),
           Stickers("family","stickman","XL",10),
           Stickers("Ifyoucanreadthis","funny","XL",5)]
for i in range(len(bumpers)):
    print(bumpers[i].nom)
