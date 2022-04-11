const { Client, Intents, Collection } = require('discord.js');
const fs = require('fs');
const client = new Client({intents: [Intents.FLAGS.GUILDS]});
const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));
const eventFiles = fs.readdirSync('./events').filter(file => file.endsWith('.js'));
require('dotenv').config({ path: '../.env' });

client.commands = new Collection();

for (const file of commandFiles) {
    const command = require(`./commands/${file}`);
    client.commands.set(command.data.name, command);
}

for (const file of eventFiles) {
    const event = require(`./events/${file}`);
    if(event.once)
        client.once(event.name, (...args) => event.execute(...args));
    else
        client.on(event.name, (...args) => event.execute(...args));
}

var monsters;

client.once('ready', () => {
    fs.readFile('./db/monsters.json', (err, data) => {
        if(err)
            throw err;
    
        let x = JSON.parse(data);
        monsters = x.monsters;
    });
});

client.on('interactionCreate', async interaction => {
    if(!interaction.isCommand())
        return;

    const command = client.commands.get(interaction.commandName);

    if(!command)
        return

    try {
        await command.execute(interaction, monsters);
    } catch (error) {
        console.error(error);
        await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
    }
});

client.login(process.env.TOKEN);