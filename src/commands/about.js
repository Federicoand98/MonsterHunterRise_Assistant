const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');

module.exports = {
    data: new SlashCommandBuilder()
    .setName('about')
    .setDescription('About the Bot'),

    async execute(interaction) {
        var str = 'Monster Hunter Rise Assistant is a Discord bot that provides you informations about Monster Hunter Rise monsters.\n\n';
        str += 'GitHub: https://github.com/Federicoand98/MonsterHunterRise_Assistant';

        const embed = new MessageEmbed()
            .setColor('#0099ff')
            .setTitle('About MonsterHunterRise Assistant')
            .setAuthor({ name: 'Federyeeco', url: 'https://github.com/Federicoand98'})
            .setDescription(str)
            .setFooter('MonsterHunter Rise Assistant created by Federico Andrucci');

        await interaction.reply({ embeds: [embed] });
    }
}