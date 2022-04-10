const { MessageEmbed } = require('discord.js');
const { Table } = require('embed-table');

class Monster {
    constructor(name, type, image, part_list, ailment_list) {
        this.name = name;
        this.type = type;
        this.image = image;
        this.part_list = part_list;
        this.ailment_list = ailment_list;
    }

    createPartTable() {
        const table = new Table({
            titles: ['Type', 'State', 'Slash', 'Strike', 'Shell', 'Fire', 'Water', 'Ice', 'Thunder', 'Dragon', 'Stun'],
            titleIndexes: [0, 8, 16, 24, 32, 40, 48, 56, 64, 72, 80],
            columnIndexes: [0, 9, 11, 17, 23, 28, 33, 39, 44, 51, 58],
            start: '`',
            end: '`',
            padEnd: 0
        });

        // TODO: appena possibile fixare element.state (obbligato ad escludere stati alterati per la limitazione di 1024 char)
        this.part_list.forEach(element => {
            if(element.state === '0') {
                table.addRow([
                    `${element.type.replace(/\s/g, '')}`,
                    `${element.state}`,
                    `${element.slash}`,
                    `${element.strike}`,
                    `${element.shell}`,
                    `${element.fire}`,
                    `${element.water}`,
                    `${element.ice}`,
                    `${element.thunder}`,
                    `${element.dragon}`,
                    `${element.stun}`
                ])
            }
        });

        return table;
    }

    createAilmentTable() {
        const table = new Table({
            titles: ['Ailment', 'Buildup', 'Decay', 'Damage', 'Duration'],
            titleIndexes: [0, 26, 54, 69, 92],
            columnIndexes: [0, 14, 29, 41, 53],
            start: '`',
            end: '`',
            padEnd: 0
        });

        this.ailment_list.forEach(element => {
            table.addRow([
                `${element.type.replace(/\s/g, '')}`,
                `${element.buildup.replace(/\s/g, '')}`,
                `${element.decay.replace(/\s/g, '')}`,
                `${element.damage.replace(/\s/g, '')}`,
                `${element.duration.replace(/\s/g, '')}`
            ]);
        });

        return table;
    }

    getMessageEmbed() {
        const partsTable = this.createPartTable();
        const ailmentsTable = this.createAilmentTable();

        const embed = new MessageEmbed()
            .setColor('#0099ff')
            .setTitle(this.name)
            .setDescription(this.type)
            .setImage(this.image)
            .addFields(partsTable.field())
            .addFields(ailmentsTable.field())
            .setFooter('MonsterHunter Rise Assistant created by Federico Andrucci');
        return embed;
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