noleg(dolphin).
swim(dolphin).
baby(dophin).

swim(bear).
baby(bear).

haslane(lion).
hastail(lion).
baby(lion).

longneck(ostrich).
haswings(ostrich).
eggs(ostrich).

canfly(parrot).
eggs(parrot).

eggs(lizard).
coolblood(lizard).


baby(dolphin):- noleg(dolphin).
baby(dolphin) :- swim(dolphin).
mammal(dolphin) :- baby(dolphin).

baby(bear) :- swim(bear).
mammal(bear) :- baby(bear).

baby(line) :- haslane(lion).
mammal(lion) :- baby(lion).

birds(ostrich) :- haswings(ostrich).
haswings(ostrich) :- longneck(ostrich).

birds(parrot) :-  haswings(parrot).
haswings(parrot) :- canfly(parrot).

reptilia(lizard) :- coolblood(lizard).
coolblood(lizard) :- eggs(lizard).




