const { registerCommands, unregisterCommands } = require('../deploy-commands');

module.exports = {
    name: 'ready',
    once: 'true',
    execute(client) {
        const guilds = client.guilds.cache.map(guild => guild.id);
        const clientId = client.user.id;

        guilds.forEach(element => {
            registerCommands(clientId, element);
            //unregisterCommands(clientId, element);
        });
    }
}