const { SlashCommandBuilder } = require('@discordjs/builders');
const { Monster, Part, Ailment } = require('../model/classes')

module.exports = {
    data: new SlashCommandBuilder()
        .setName('monster')
        .setDescription('Retrieve monster informations!')
        .addStringOption(option => 
            option.setName('name')
                .setDescription('The name of the monster')
                .setRequired(true)),

    async execute(interaction, monsters) {
        const name = interaction.options.getString('name');
        var m;

        monsters[0].map(monster => {
            if(monster.name.toLowerCase() === name.toLowerCase()) {

                var parts = [];
                var ailments = [];

                monster.parts_list.forEach(element => {
                    part = new Part(element.type, element.state, element.hit_slash, element.hit_strike, element.hit_shell, element.fire, element.water, element.ice, element.thunder, element.dragon, element.stun);
                    parts.push(part);
                });

                monster.ailments_list.forEach(element => {
                    ailment = new Ailment(element.type, element.buildup, element.decay, element.damage, element.duration);
                    ailments.push(ailment);
                });

                m = new Monster(monster.name, monster.type, parts, ailments);
                res = m.toString();
            }
        })

        await interaction.reply(res);
    },
};