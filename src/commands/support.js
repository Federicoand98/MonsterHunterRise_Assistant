const { SlashCommandBuilder } = require('@discordjs/builders');
const { MessageEmbed } = require('discord.js');
require('dotenv').config({ path: '../.env' });

module.exports = {
    data: new SlashCommandBuilder()
    .setName('support')
    .setDescription('Contact the developer'),

    async execute(interaction) {
        var str = 'If you are having any problem with the bot or you would like to report a bug do not hesitate to contact the developer at:\n\n';
        str += 'GitHub: https://github.com/Federicoand98/MonsterHunterRise_Assistant/issues\n';
        str += `Email: ${process.env.EMAIL}`;

        const embed = new MessageEmbed()
        .setColor('#0099ff')
        .setTitle('Contact the developer')
        .setAuthor({ name: 'Federyeeco', url: 'https://github.com/Federicoand98'})
        .setDescription(str)
        .setFooter('MonsterHunter Rise Assistant created by Federico Andrucci');

    await interaction.reply({ embeds: [embed] });
    }
}