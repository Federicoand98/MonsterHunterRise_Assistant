const { registerCommands, unregisterCommands } = require('../deploy-commands');
require('dotenv').config({ path: '../.env' });

module.exports = {
    name: 'guildCreate',
    once: 'true',
    execute(guild) {
        console.log("Joined a new guild: " + guild.name);
        const clientId = process.env.BOTID;

        console.log(clientId);
        console.log(guild.id);

        registerCommands(clientId, guild.id);
    }
}