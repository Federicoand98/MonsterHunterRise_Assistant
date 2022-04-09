class Monster {
    constructor(name, type, part_list, ailment_list) {
        this.name = name;
        this.type = type;
        this.part_list = part_list;
        this.ailment_list = ailment_list;
    }

    getMessageEmbed() {
        const str = '';
        return str;
    }

    toString() {
        var res = this.name + '\n' + this.type + '\n';
        
        this.part_list.forEach(element => {
            res += element.type + ' ' + element.state + ' ' + element.slash + ' ' + element.strike + ' ' + element.shell + ' ' + 
                element.fire + ' ' + element.water + ' ' + element.ice + ' ' + element.dragon + ' ' + element.stun + '\n';
        });

        this.ailment_list.forEach(element => {
            res += element.type + ' ' + element.buildup + ' ' + element.decay + ' ' + element.damage + ' ' + element.duration + '\n';
        })

        return res;
    }
}

class Part {
    constructor(type, state, slash, strike, shell, fire, water, ice, thunder, dragon, stun) {
        this.type = type;
        this.state = state;
        this.slash = slash;
        this.strike = strike;
        this.shell = shell;
        this.fire = fire;
        this.water = water;
        this.ice = ice;
        this.thunder = thunder;
        this.dragon = dragon;
        this.stun = stun;
    }
}

class Ailment {
    constructor(type, buildup, decay, damage, duration) {
        this.type = type;
        this.buildup = buildup;
        this.decay = decay;
        this.damage = damage;
        this.duration = duration;
    }
}

module.exports = {
    Monster,
    Part,
    Ailment
}