import random as r


class Hive():
    def __init__(this, num_start, repchance, deathchance):
        this.num_start = num_start
        this.repchance = repchance
        this.deathchance = deathchance
        this.bees = []
        this.populate()

    def __str__(this):
        rep = 0;
        death = 0;
        pop = len(this.bees)

        for bee in this.bees:
            rep += bee.repchance
            death += bee.deathchance
        rep /= pop
        death /= pop
        return "rep: " + str(rep) + " death: " + str(death) + " pop: " + str(pop)

    def populate(this):
        for x in range(this.num_start):
            this.newbee(this.repchance, this.deathchance)

    def newbee(this, repchance, deathchance):
        this.bees.append(Bee(repchance + (r.random() - 0.5) / 5, deathchance + (r.random() - 0.5) / 5))

    def day(this):
        for bee in this.bees:
            bee.day()

    def kill(this, bee):
        this.bees.remove(bee)


class Bee():
    def __init__(this, repchance, deathchance):
        if (repchance < 0 or repchance > 1):
            repchance = round(repchance)
        if (deathchance < 0 or deathchance > 1):
            deathchance = round(deathchance)
        this.repchance = repchance
        this.deathchance = deathchance

    def __str__(this):
        return str(this.repchance) + " " + str(this.deathchance)

    def replicate(this):
        hive.newbee(this.repchance, this.deathchance)

    def die(this):
        hive.kill(this)

    def day(this):
        if(r.random() < this.repchance):
            this.replicate()

        if(r.random() < this.deathchance + len(hive.bees) * c):
            this.die()



c = 0.001
hive = Hive(20, 0.5, 0.5)
time = 100
for x in range(time):
    if(x % 1 == 0):
        print(hive)
    hive.day()
