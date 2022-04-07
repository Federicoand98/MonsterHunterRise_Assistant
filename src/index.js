const { Client, Intents } = require('discord.js');
const { token } = require('../config.json');
const fs = require('fs');
const deployCommand = require('./deploy-commands');
const client = new Client({intents: [Intents.FLAGS.GUILDS]});

var monsters;

client.once('ready', () => {
    fs.readFile('/Users/federyeeco/Sviluppo/Git/MonsterHunterRise_Assistant/src/db/monsters.json', (err, data) => {
        if(err)
            throw err;
    
        let x = JSON.parse(data);
        monsters = x.monsters;
        
        /*
        console.log(x.monsters[0].sort(function(a, b) {
            if(a.name < b.name) return -1;
            if(a.name > b.name) return 1;
            return 0;
        }).map(monster => monster.name));
        */
    });

    console.log('Ready');
});

client.on('message', message => {
        
        message.channel.send(monsters[0].sort(function(a, b) {
            if(a.name < b.name) return -1;
            if(a.name > b.name) return 1;
            return 0;
        }).map(monster => monster.name));
    
});

client.login(token);