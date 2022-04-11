const { REST } = require('@discordjs/rest');
const { Routes } = require('discord-api-types/v9');
require('dotenv').config({ path: '../.env' });
const fs = require('fs');

function registerCommands(clientId, guildId) {
	const commandFiles = fs.readdirSync('./commands').filter(file => file.endsWith('.js'));
	const commands = [];

	for (const file of commandFiles) {
		const command = require(`./commands/${file}`);
		console.log(command.data.name + ' ' + guildId);
		commands.push(command.data.toJSON());
	}
	
	const rest = new REST({ version: '9' }).setToken(process.env.TOKEN);
	
	rest.put(Routes.applicationGuildCommands(clientId, guildId), { body: commands })
		.then(() => console.log('Successfully registered application commands.'))
		.catch(console.error);
}

function unregisterCommands(clientId, guildId) {
	const rest = new REST({ version: '9' }).setToken(process.env.TOKEN);

	rest.get(Routes.applicationGuildCommands(clientId, guildId)).then(data => {
		const promises = [];
		for(const command of data) {
			const deleteUrl = `${Routes.applicationGuildCommands(clientId, guildId)}/${command.id}`;
			promises.push(rest.delete(deleteUrl));
		}
	
		return Promise.all(promises);
	});

	console.log('Successfullt unregistered all commands in ' + guildId);
}

module.exports = {
	registerCommands,
	unregisterCommands
}